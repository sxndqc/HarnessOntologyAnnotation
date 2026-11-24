"""Write a parse skill from the errors on the training documents (three reflection methods, two rounds).

    python3 reflect.py evidence --tag ""            -> analysis/evidence/base.md   (errors of s3-full-two-tool)
    python3 reflect.py evidence --tag m1-r1         -> analysis/evidence/m1-r1.md  (errors of s3-full-two-tool+m1-r1)
    python3 reflect.py skill --method 1 --round 1   -> skills/m1-r1.md   (from the base errors)
    python3 reflect.py skill --method 1 --round 2   -> skills/m1-r2.md   (from skills/m1-r1.md and its errors)

Evidence: the runs of a condition on the four training documents compared with the revised gold of the review
(review/data/gold_revised) by umrjudge; every unit that is not correct, with the sentence, what the gold has and
what the run has, pooled over the five runs with the number of runs that made it. Round 1 also gets, for each
sentence, what the reviewers wrote about the systems' choices (review/items).

The three methods differ in one paragraph of the request (METHODS). The request starts by saying that the skill
is a list of bullet points and must stay short. The reflecting model is the one that annotates (config.json).
"""
import argparse
import collections
import contextlib
import glob
import io
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
sys.path.insert(0, os.path.join(R2, "vendor", "umrancast"))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "judges"))
CONFIG = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
BASE = "s3-full-two-tool"
LIMIT = 300000          # characters of evidence given to the reflecting model

HEAD = """You are improving an annotator of Uniform Meaning Representation (UMR). The annotator is a language model \
that gets a one-sentence description of UMR, two lookup tools (the full UMR guidelines and PropBank) and a whole \
document, and writes the sentence-level graph of every sentence and the document-level temporal, modal and \
coreference relations. Below are the errors it made on four Chinese training documents, found by comparing its \
annotations (five runs) with the corrected gold annotation. In round 1 the errors are the reviewers' notes on the \
annotator's choices; in a later round they are the mechanical differences from the corrected gold that at least \
three of the five runs share.

Write a "parse skill" for this annotator: a text that will be added to its instructions for every later document.

The skill is a list of bullet points, nothing else. Do not write too much: a skill that tries to cover everything \
grows without bound and stops being followed, so keep it short.
"""
METHODS = {
    1: "Look at the errors, summarise them, and from that write the points the annotator should follow.",
    2: "Look at the errors, and from them write the points the annotator should follow. Every point must be general: "
       "a rule that holds for any document, never a point about one case, one word or one sentence of these documents.",
    3: "Look at the errors and write the points the annotator should follow. Then restate these points once more as a "
       "summary that says the same in fewer words, so that the skill gets shorter; that restatement is the skill.",
}
TAIL = {
    1: "Answer with the skill only: the bullet points.",
    2: "Answer with the skill only: the bullet points.",
    3: "Answer in two parts: first the points under the line `## Points`, then the shortened restatement under the line "
       "`## Skill` (bullet points). Only the part under `## Skill` is used.",
}
AGAIN = """The annotator already uses the skill below, written from an earlier round of errors on the same documents. \
The errors listed further down are those it still makes with this skill. Write the new version of the whole skill \
(it replaces the current one): keep what works, change or drop what does not, add what the remaining errors call for.

## Current skill

%s
"""


def runs_of(tag):
    d = os.path.join(HERE, "runs", BASE + ("+" + tag if tag else ""))
    return sorted(glob.glob(os.path.join(d, "p*r*")))


def evidence(tag, with_review):
    import umrjudge
    spec = umrjudge.load_spec()
    out = ["# Errors on the training documents (%s)" % (BASE + ("+" + tag if tag else "")), ""]
    runs = runs_of(tag)
    notes = collections.defaultdict(list)
    if with_review:
        for p in sorted(glob.glob(os.path.join(HERE, "review", "review", "items", "*.json"))):
            doc = os.path.basename(p).split(".")[0]
            for it in json.load(open(p, encoding="utf-8")):
                wrong = [c for c in it["choices"] if c["status"] in ("bad", "minor") and any(s != "gold" for s in c["systems"])]
                if not wrong:
                    continue
                line = "- [%s] %s: " % (it["cat"], it["topic"])
                line += "; ".join("%s (%s, %d of 5 runs)" % (c["label"], "wrong" if c["status"] == "bad" else "acceptable but worse",
                                                             sum(1 for s in c["systems"] if s != "gold")) for c in wrong)
                if it.get("best"):
                    line += ". Better: %s" % it["best"]
                line += ". " + it["text"]
                notes[(doc, it["sent"])].append(line)
    for doc in CONFIG["groups"]["train"]:
        gold = os.path.join(HERE, "review", "data", "gold_revised", doc + ".umr")
        if not os.path.exists(gold):
            gold = os.path.join(HERE, "data", "gold", doc + ".umr")
        sents = umrjudge.read_umr(gold)
        units = collections.defaultdict(collections.Counter)
        n = 0
        for rd in runs:
            pred = os.path.join(rd, doc + ".umr")
            if not os.path.exists(pred):
                continue
            n += 1
            with contextlib.redirect_stdout(io.StringIO()):
                res = umrjudge.judge_file(pred, gold, spec)
            for u in res["units"]:
                if u["verdict"] == "correct" or u["check"] in ("k_doc_format", "a_event_found", "a_entity_found"):
                    continue
                key = (u["check"], u["verdict"], str(u.get("gold") or "-")[:160], str(u.get("pred") or "-")[:160])
                units[u.get("sent", 0)][key] += 1
        out += ["## Document %s (%d runs)" % (doc, n), ""]
        for s in sorted(sents):
            rows = [(k, c) for k, c in units.get(s, {}).items() if c >= 3]
            if not rows and not notes.get((doc, s)):
                continue
            out += ["### Sentence %d: %s" % (s, sents[s]["words"]), ""]
            if notes.get((doc, s)):
                out += ["Reviewer's notes on the annotator's choices:"] + notes[(doc, s)] + [""]
            if rows and not with_review:
                out += ["Differences from the corrected gold (check | kind | gold | annotator | runs):"]
                for (check, verdict, g, p), c in sorted(rows, key=lambda x: (x[0][0], -x[1])):
                    out.append("- %s | %s | %s | %s | %d" % (check, verdict, g, p, c))
                out.append("")
    text = "\n".join(out)
    os.makedirs(os.path.join(HERE, "analysis", "evidence"), exist_ok=True)
    path = os.path.join(HERE, "analysis", "evidence", (tag or "base") + ".md")
    open(path, "w", encoding="utf-8").write(text)
    print(path, len(text), "characters")
    return text


def clip(text):
    """The evidence cut to LIMIT characters: the same share of every document."""
    if len(text) <= LIMIT:
        return text
    parts = text.split("\n## Document ")
    share = LIMIT // max(1, len(parts) - 1)
    return parts[0] + "".join("\n## Document " + p[:share] + "\n(cut here: the rest of this document is left out)\n" for p in parts[1:])


def ask(prompt):
    work = tempfile.mkdtemp(prefix="r3-reflect-")
    r = subprocess.run(["claude", "-p", "--model", CONFIG["model"], "--effort", CONFIG["effort"], "--tools", "",
                        "--strict-mcp-config", "--setting-sources", "", "--output-format", "json",
                        "--system-prompt", "You are an expert annotator of Uniform Meaning Representation (UMR)."],
                       input=prompt, capture_output=True, text=True, timeout=3000, cwd=work)
    j = json.loads(r.stdout)
    if j.get("is_error"):
        raise SystemExit("reflection failed: %s" % str(j.get("result"))[:300])
    return j["result"], {"seconds": j.get("duration_ms", 0) / 1000, "output_tokens": j.get("usage", {}).get("output_tokens"),
                         "list_cost_usd": j.get("total_cost_usd")}


def skill(method, rnd):
    name = "m%d-r%d" % (method, rnd)
    prev = "m%d-r%d" % (method, rnd - 1)
    ev = open(os.path.join(HERE, "analysis", "evidence", ("base" if rnd == 1 else prev) + ".md"), encoding="utf-8").read()
    parts = [HEAD, METHODS[method]]
    if rnd > 1:
        parts.append(AGAIN % open(os.path.join(HERE, "skills", prev + ".md"), encoding="utf-8").read().strip())
    parts += [TAIL[method], clip(ev)]
    prompt = "\n\n".join(parts)
    os.makedirs(os.path.join(HERE, "skills"), exist_ok=True)
    open(os.path.join(HERE, "skills", name + ".prompt.md"), "w", encoding="utf-8").write(prompt)
    answer, meta = ask(prompt)
    open(os.path.join(HERE, "skills", name + ".answer.md"), "w", encoding="utf-8").write(answer)
    text = answer
    if method == 3 and "## Skill" in answer:
        text = answer.split("## Skill", 1)[1]
    text = "\n".join(l for l in text.strip().split("\n"))
    open(os.path.join(HERE, "skills", name + ".md"), "w", encoding="utf-8").write(text.strip() + "\n")
    bullets = sum(1 for l in text.split("\n") if l.lstrip().startswith(("-", "*", "•")))
    json.dump({"skill": name, "method": method, "round": rnd, "chars": len(text), "bullets": bullets,
               "prompt_chars": len(prompt), **meta}, open(os.path.join(HERE, "skills", name + ".meta.json"), "w"), indent=1)
    print(name, len(text), "characters,", bullets, "bullets")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["evidence", "skill"])
    ap.add_argument("--tag", default="")
    ap.add_argument("--method", type=int)
    ap.add_argument("--round", type=int)
    a = ap.parse_args()
    if a.what == "evidence":
        evidence(a.tag, with_review=not a.tag)
    else:
        skill(a.method, a.round)


if __name__ == "__main__":
    main()
