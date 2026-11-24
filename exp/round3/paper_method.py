"""The improvement round of the paper's first version (10 October 2026, sections/method.tex "One improvement
round"), on this round's harness: annotate, align, find, plan, admit and apply.

    python3 paper_method.py [--jobs 6]     -> skills/pm-h<n>.md (the skill after document n), skills/pm/ (every round)

The harness here is s3-full-two-tool (one prompt per document, two lookup tools) plus one instruction file, the
parse skill, which starts empty; that file is what the rounds edit. As in the paper, the training documents are
taken in order, three rounds each; a round annotates the document with the previous round's skill.

  1. annotate   the document once with the current skill (wording 1)
  2. align      umrjudge against the corrected gold lists the units it does not count as correct
  3. find       for every sentence with such a unit, one call sees the sentence, both graphs, both sides'
                document-level relations and the units, and lists the divergences: kind, check, cause, and the
                convention the gold follows in general terms (or that the gold looks wrong, or a one-off)
  4. plan       one call reads up to 250 problems (taken in turn from each sentence) and the skill's full text and
                returns typed edits: add (after an anchor), modify (replace the anchor), delete (the anchor)
  5. admit      an edit applies only if its anchor occurs exactly once in the skill (an add may have no anchor: it
                goes to the end) and is rejected if its text shares eight consecutive characters with a sentence
                of the corpus, training or test (for English sentences: five consecutive words)

Not taken over from the paper: the attribution to one of several skills and to a step of the chain (there is one
instruction file and one step here), the trace of intermediate steps, and the proposals of new tools and steps.
The builder is the annotating model (config.json).
"""
import argparse
import collections
import contextlib
import io
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
sys.path.insert(0, os.path.join(R2, "vendor", "umrancast"))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "judges"))
sys.path.insert(0, HERE)
import reflect  # noqa: E402
import run_claude as RC  # noqa: E402
import umrjudge  # noqa: E402

CONFIG = RC.CONFIG
COND = [c for c in CONFIG["conditions"] if c["name"] == "s3-full-two-tool"][0]
OUT = os.path.join(HERE, "skills", "pm")
EMPTY = "- Follow the points below; they were learned from earlier documents.\n"

FIND = """You are helping to improve an annotator of Uniform Meaning Representation (UMR). The annotator is a language \
model that gets a short description of UMR, two lookup tools (the full UMR guidelines and PropBank), a list of \
instructions (its "parse skill") and a whole document, and writes every sentence's graph and the document-level \
temporal, modal and coreference relations.

Below is one sentence of a document it annotated: the sentence, the annotator's graph, the gold graph, both sides' \
document-level relations for this sentence, and the units an evaluator did not count as correct (check | verdict | \
gold | annotator).

List every divergence between the annotation and the gold. Merge divergences that have one cause. For each give:
- "kind": what is wrong, in a few words
- "check": the evaluator check it belongs to (the check names of the units)
- "cause": why the annotator went wrong, as far as you can tell
- "convention": if the gold follows a convention, that convention in general terms (a rule that would hold for any \
document), else ""
- "gold_error": true if the gold itself looks wrong here
- "one_off": true if this is about one word or one fact of this sentence and no general rule would prevent it

Answer with a JSON list of such objects and nothing else.
"""
PLAN = """You are improving an annotator of Uniform Meaning Representation (UMR). The annotator is a language model \
that gets a short description of UMR, two lookup tools (the full UMR guidelines and PropBank), a list of instructions \
(its "parse skill", below) and a whole document, and writes every sentence's graph and the document-level temporal, \
modal and coreference relations.

Below are the parse skill in full and the problems found when the annotator's last annotation of a document was \
compared with the gold, grouped by evaluator check.

Return edits to the parse skill. Each edit is an object with:
- "action": "add" (insert a missing rule, example or common error after the anchor), "modify" (replace an \
instruction, common error or example that is wrong or too narrow: the anchor is replaced by the text) or "delete" \
(remove text that causes an error or contradicts the gold: the anchor is removed)
- "anchor": text copied exactly from the parse skill that occurs in it exactly once (for "add" it may be "", and the \
text then goes to the end)
- "text": the new text (a bullet point starting with "- "; empty for "delete")
- "problems": the numbers of the problems it addresses

Edits must be general and checkable, one edit should fix many problems, and one-offs and gold errors get no edit. \
The parse skill is a list of bullet points and must stay short: prefer modifying or deleting to adding. Do not quote \
the documents: a rule must hold for any document.

Answer with a JSON object {"edits": [...], "suggestions": [...]} and nothing else; "suggestions" are changes outside \
the parse skill (to the tools, to the procedure) that you think are needed; they are recorded, not applied.
"""


def js(text):
    text = re.sub(r"^```\w*\s*|\s*```\s*$", "", text.strip())
    m = re.search(r"[\[{].*[\]}]", text, re.S)
    return json.loads(m.group(0) if m else text)


def corpus():
    zh, en = [], []
    for name in CONFIG["groups"]["train"] + CONFIG["groups"]["test"]:
        for line in open(os.path.join(HERE, "data", "input", name + ".txt"), encoding="utf-8"):
            (zh if name.startswith("zh") else en).append(line.split())
    return ["".join(w) for w in zh], [" ".join(w).lower() for w in en]


ZH, EN = corpus()


def leaks(text):
    plain = re.sub(r"\s+", "", text)
    for k in range(len(plain) - 7):
        piece = plain[k:k + 8]
        if re.search(r"[一-鿿]", piece) and any(piece in s for s in ZH):
            return piece
    words = re.findall(r"[a-z0-9'-]+", text.lower())
    for k in range(len(words) - 4):
        piece = " ".join(words[k:k + 5])
        if any(piece in s for s in EN):
            return piece
    return None


def annotate(doc, skill_text, tag):
    """One annotation of doc with the skill (wording 1); returns the .umr path."""
    out_dir = os.path.join(HERE, "runs-pm", tag)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, doc)
    if not os.path.exists(base + ".umr"):
        d = RC.umrdoc.load_blind(os.path.join(HERE, "data", "input", doc + ".txt"))
        prompt = RC.task(COND, 1, d, skill_text if skill_text.strip() != EMPTY.strip() else None)
        for _ in range(3):
            text, meta = RC.call(prompt, COND["tools"], base + ".calls.jsonl", 3600)
            if text is not None and RC.check(d, text)[0] is None:
                break
        if text is None:
            raise SystemExit("no annotation of %s (%s)" % (doc, meta.get("error")))
        open(base + ".raw.txt", "w", encoding="utf-8").write(text)
        umr, _ = RC.umrdoc.parse_answer(d, text)
        open(base + ".umr", "w", encoding="utf-8").write(umr)
    return base + ".umr"


def one_round(doc, rnd, skill_text, jobs):
    tag = "%s-r%d" % (doc, rnd)
    work = os.path.join(OUT, tag)
    os.makedirs(work, exist_ok=True)
    if os.path.exists(os.path.join(work, "skill.md")):
        return open(os.path.join(work, "skill.md"), encoding="utf-8").read()
    pred_path = annotate(doc, skill_text, tag)
    gold_path = os.path.join(HERE, "review", "data", "gold_revised", doc + ".umr")
    spec = umrjudge.load_spec()
    with contextlib.redirect_stdout(io.StringIO()):
        res = umrjudge.judge_file(pred_path, gold_path, spec)
    gold, pred = umrjudge.read_umr(gold_path), umrjudge.read_umr(pred_path)
    by = collections.defaultdict(list)
    for u in res["units"]:
        if u["verdict"] != "correct" and u["check"] not in ("k_doc_format",):
            by[u.get("sent", 0)].append(u)

    def doc_rels(s):
        return "\n".join("(%s :%s %s) [%s]" % (r["parent"], r["relation"], r["child"], r["section"]) for r in s.get("doc", [])) or "(none)"

    def find(n):
        g, p = gold.get(n), pred.get(n, {})
        if g is None:
            return n, []
        units = "\n".join("- %s | %s | %s | %s" % (u["check"], u["verdict"], str(u.get("gold") or "-")[:200], str(u.get("pred") or "-")[:200])
                          for u in by[n][:80])
        prompt = "\n\n".join([FIND, "## Sentence %d\n\n%s" % (n, g["words"]), "## Annotator's graph\n\n" + (p.get("graph") or "(none)"),
                              "## Gold graph\n\n" + g["graph"], "## Annotator's document-level relations\n\n" + doc_rels(p),
                              "## Gold document-level relations\n\n" + doc_rels(g), "## Units not counted as correct\n\n" + units])
        for _ in range(2):
            try:
                answer, _m = reflect.ask(prompt)
                return n, [x for x in js(answer) if isinstance(x, dict)]
            except Exception as e:
                err = str(e)
        print("  find failed for sentence", n, err[:100], flush=True)
        return n, []
    with ThreadPoolExecutor(jobs) as pool:
        found = dict(pool.map(find, sorted(n for n in by if n)))
    json.dump(found, open(os.path.join(work, "problems.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # up to 250 problems, taken in turn from each sentence
    queues = [list(found[n]) for n in sorted(found)]
    problems = []
    while any(queues) and len(problems) < 250:
        for q in queues:
            if q and len(problems) < 250:
                problems.append(q.pop(0))
    groups = collections.defaultdict(list)
    for k, pr in enumerate(problems, 1):
        groups[str(pr.get("check", "?"))].append((k, pr))
    lines = []
    for check in sorted(groups):
        lines.append("### %s" % check)
        for k, pr in groups[check]:
            flags = (" [gold looks wrong]" if pr.get("gold_error") else "") + (" [one-off]" if pr.get("one_off") else "")
            lines.append("%d. %s%s. Cause: %s. Convention: %s" % (k, pr.get("kind", ""), flags, pr.get("cause", ""), pr.get("convention", "") or "-"))
    prompt = "\n\n".join([PLAN, "## Parse skill\n\n" + skill_text, "## Problems (%d)\n\n%s" % (len(problems), "\n".join(lines))])
    open(os.path.join(work, "plan.prompt.md"), "w", encoding="utf-8").write(prompt)
    plan = {"edits": [], "suggestions": []}
    for _ in range(2):
        try:
            answer, _m = reflect.ask(prompt)
            open(os.path.join(work, "plan.answer.md"), "w", encoding="utf-8").write(answer)
            plan = js(answer)
            break
        except Exception as e:
            print("  plan failed", str(e)[:100], flush=True)
    log, new = [], skill_text
    for e in plan.get("edits", []) if isinstance(plan, dict) else []:
        action, anchor, text = e.get("action"), e.get("anchor") or "", (e.get("text") or "").strip()
        why = None
        if action not in ("add", "modify", "delete"):
            why = "unknown action"
        elif (anchor or action != "add") and new.count(anchor) != 1:
            why = "anchor occurs %d times" % new.count(anchor) if anchor else "no anchor"
        elif action != "delete" and not text:
            why = "no text"
        elif action != "delete" and leaks(text):
            why = "shares text with the corpus: %s" % leaks(text)
        if why is None:
            if action == "add":
                if anchor:
                    i = new.index(anchor) + len(anchor)
                    j = new.find("\n", i)
                    j = len(new) if j < 0 else j
                    new = new[:j] + "\n" + text + new[j:]
                else:
                    new = new.rstrip("\n") + "\n" + text + "\n"
            elif action == "modify":
                new = new.replace(anchor, text)
            else:
                new = new.replace(anchor, "")
                new = re.sub(r"\n\s*-?\s*\n", "\n", new)
        log.append({"action": action, "applied": why is None, "rejected": why, "anchor": anchor[:120], "text": text, "problems": e.get("problems")})
    new = "\n".join(l for l in new.split("\n") if l.strip() and l.strip() != "-") + "\n"
    json.dump({"doc": doc, "round": rnd, "sentences_with_errors": len(found), "problems": len(problems),
               "gold_errors": sum(1 for p in problems if p.get("gold_error")), "one_offs": sum(1 for p in problems if p.get("one_off")),
               "edits": log, "suggestions": plan.get("suggestions", []) if isinstance(plan, dict) else [],
               "skill_chars": len(new), "skill_bullets": sum(1 for l in new.split("\n") if l.lstrip().startswith("-"))},
              open(os.path.join(work, "round.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(work, "skill.md"), "w", encoding="utf-8").write(new)
    a = sum(1 for x in log if x["applied"])
    print("%s round %d: %d sentences with errors, %d problems, %d edits applied, %d rejected, skill %d characters" % (
        doc, rnd, len(found), len(problems), a, len(log) - a, len(new)), flush=True)
    return new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    skill = EMPTY
    for n, doc in enumerate(CONFIG["groups"]["train"], 1):
        for rnd in (1, 2, 3):
            skill = one_round(doc, rnd, skill, a.jobs)
        open(os.path.join(HERE, "skills", "pm-h%d.md" % n), "w", encoding="utf-8").write(skill)
        json.dump({"skill": "pm-h%d" % n, "chars": len(skill), "bullets": sum(1 for l in skill.split("\n") if l.lstrip().startswith("-"))},
                  open(os.path.join(HERE, "skills", "pm-h%d.meta.json" % n), "w"))
        print("H%d written" % n, flush=True)


if __name__ == "__main__":
    main()
