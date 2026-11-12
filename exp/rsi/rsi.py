"""Step 4: recursive self-improvement of the instruction (RSI), through the Messages API.

    python3 exp/rsi/rsi.py --variant rules      # A: the reflection may write general rules only
    python3 exp/rsi/rsi.py --variant examples   # B: the reflection records concrete examples

Start: the s3-all condition (abridged guidelines + search_guidelines, propbank_lookup, search_annotations),
whole-document annotation. Its instruction (everything of api/s3-all's system prompt before "## Output
format": the task, what to aim for, the abridged guidelines) is what the RSI may change; the output format
and the tools' descriptions stay fixed.

Training: a document of the shared task's training data (default chinese_umr-0001), in batches of five
sentences (sentences 1-5, 6-10, ...), each batch annotated as a short document of its own (the gold's
document-level relations to sentences outside the batch are left out). While training, search_annotations
never returns a sentence of the training document. For each batch:

1. annotate the batch with the current instruction; score it against the gold (AnCast++, umrjudge);
2. critique: the model reads the instruction, the batch, its annotation, the gold and the umrjudge units
   that are not correct, and writes the error patterns and what to change in the instruction;
3. reflect: the model edits the instruction (anchored replace / insert / delete, or a rewrite; at most
   MAX_CHARS characters; nothing copied from the test documents; variant rules: nothing copied from the
   training document either);
4. annotate the batch again with the edited instruction; it is kept when its AnCast++ comprehensive score
   on the batch is higher than the best so far, otherwise the best version stays;

steps 2-4 three times per batch (--reflections), starting each time from the best version; then the next
batch. After each batch the best version annotates the test documents (zh-0028, zh-0032), scored like
every other run. Model and effort as given (default claude-opus-5-5, medium); answers cached as in run.py.

Everything is written under rsi/runs/<variant>-<model>/: versions/v<k>.md (each accepted instruction),
b<n>/r<m>/ (critique and reflection with their prompts and transcripts, the edits proposed and applied,
the candidate instruction and its diff, the batch annotation and its scores), b<n>/r0/ (the batch
annotated by the version the batch started with), test/after-b<n>/ (test documents), log.md, state.json.
"""
import argparse
import difflib
import json
import os
import re
import sys
import time

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(EXP, "lib"))
sys.path.insert(0, EXP)
sys.path.insert(0, os.path.join(EXP, "scripts"))
import llm  # noqa: E402
import registry  # noqa: E402
import run as R  # noqa: E402
import score  # noqa: E402
import umrdoc  # noqa: E402

ALL_TOOLS = ["search_guidelines", "propbank_lookup", "search_annotations"]
TEST = ["zh-0028", "zh-0032"]
MAX_CHARS = 30000
LEAK = 8          # characters (spaces ignored) that may not be copied from a protected text
CACHE = os.path.join(EXP, ".cache", "answers")

VARIANT = {
    "rules": {
        "critique": "Give your advice as general rules only. Do not record details: no specific words, names, "
                    "sentences or annotations of these sentences; describe each case by its kind (e.g. a verb of "
                    "saying with a clause object, a noun modified by a measure phrase).",
        "reflect": "Write general rules only. Do not record details: no specific words, names, sentences or "
                   "annotations of these sentences, and no examples taken from them (short schematic patterns such "
                   "as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies %d or more characters of the "
                   "training document is rejected." % LEAK,
    },
    "examples": {
        "critique": "For each problem give one or two concrete examples from these sentences: the words, what the "
                    "annotation had, and the correct annotation fragment.",
        "reflect": "Record examples: for each problem you fix, add a short concrete example from these sentences (the "
                   "words and the correct annotation fragment, a line or two) to a section \"## Examples\" at the end "
                   "of the instruction (create it if it is not there), next to the rule it illustrates; keep the "
                   "examples short and drop or merge old ones when the instruction gets near its size limit.",
    },
}

CRITIQUE_SYSTEM = "You review UMR annotations made with an instruction, and say what in the instruction should change."

CRITIQUE = """An annotator (a model) annotated the sentences below in Uniform Meaning Representation (UMR), following the instruction below. A judge (umrjudge) then compared its annotation with the expert gold annotation, check by check (concepts, senses, roles, attributes, named entities, reentrancy, and the document-level temporal, modal and coreference relations).

Your task: find the error patterns that cost the most, explain why they happen given the instruction (a rule that is missing, unclear, wrong, or not followed), and say what to change in the instruction to fix them so that they do not recur on other documents. Order them by cost, most costly first. Say also what the annotator got right that the instruction should keep. {variant}

You may use the tools to check the guidelines (search_guidelines), PropBank (propbank_lookup) and how other gold annotations do a case (search_annotations).

# The instruction
<instruction>
{instruction}
</instruction>

# The sentences
{lines}

# The annotator's annotation (as scored)
<annotation>
{pred}
</annotation>

# The gold annotation
<gold>
{gold}
</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
{checks}

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
{units}

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction."""

REFLECT_SYSTEM = "You improve the instruction of a UMR annotator by editing it."

REFLECT = """You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format and the tools' descriptions are fixed and not part of the instruction: do not restate or change them. The instruction may be at most {max_chars} characters (now {size}). Never copy text of the test documents. {variant}

# The current instruction
<instruction>
{instruction}
</instruction>

# The critique (training batch {batch}: {doc}, sentences {first}-{last}; AnCast++ comprehensive {score})
<critique>
{critique}
</critique>

# Earlier edits
{history}

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{{"summary": "...", "edits": [...]}}, where each edit is one of
  {{"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}}
  {{"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}}
  {{"op": "append", "text": "<text to add at the end>"}}
  {{"op": "delete", "old": "<text that occurs exactly once>"}}
  {{"op": "rewrite", "text": "<the whole new instruction>"}}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped."""


def plain(text):
    return re.sub(r"\s+", "", text)


def copies(new_text, protected, n=LEAK):
    """The first run of n characters (spaces ignored) of new_text found in a protected text, or ''."""
    t = plain(new_text)
    for i in range(0, max(0, len(t) - n + 1)):
        if t[i:i + n] in protected:
            return t[i:i + n]
    return ""


def strip_alignment(umr_text):
    return re.sub(r"# alignment:\n(?:[^\n]*\S[^\n]*\n)*", "", umr_text)


class Runner:
    def __init__(self, a):
        self.a = a
        self.out = os.path.join(EXP, "rsi", "runs", "%s-%s" % (a.variant, a.model))
        os.makedirs(self.out, exist_ok=True)
        reg = registry.load(os.path.join(EXP, "api", "s3-all", "registry.yaml"))
        self.skill = reg["skills"]["annotate"]
        import tools.search as search
        self.search = search
        self.test_texts = R.test_texts()
        self.train_doc = umrdoc.load(os.path.join(R.UMR22, "training-clean", "chinese", a.train_doc + ".umr"))
        self.train_doc["name"], self.train_doc["lang"] = a.train_doc, "zh"
        self.protect_test = "".join(plain(" ".join(s["words"])) for d in TEST for s in R.doc_of(d)["sents"])
        self.protect_train = "".join(plain(" ".join(s["words"])) for s in self.train_doc["sents"])
        system, _ = self.render(R.doc_of(TEST[0]))
        cut = system.index("\n## Output format")
        self.instruction0, self.tail = system[:cut], system[cut:]

    def log(self, msg):
        line = "%s  %s" % (time.strftime("%H:%M:%S"), msg)
        print(line, flush=True)
        with open(os.path.join(self.out, "log.md"), "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def render(self, doc, doc_id=None):
        ann = R.annotation(doc)
        return registry.render(self.skill, {"lang": ann["lang"], "doc_id": doc_id or ann["name"],
                                            "n": ann["sentences"], "sentences": ann["lines"]})

    # ---------------------------------------------------------------- annotate and score

    def skip(self, training):
        self.search.set_skip(docs=[self.a.train_doc] if training else [], texts=self.test_texts)

    def annotate(self, instruction, doc, out_dir, name, doc_id=None, training=False):
        """Annotate doc with instruction; write <name>.raw.txt, .umr, .prompt.md, .transcript.json. Returns
        (umr path, parse report, llm result)."""
        os.makedirs(out_dir, exist_ok=True)
        _, user = self.render(doc, doc_id)
        system = instruction + self.tail
        self.skip(training)
        r = llm.answer(self.a.model, system, user, ALL_TOOLS, self.a.effort, CACHE)
        R.write_transcript(out_dir, name, self.a.model, self.a.effort, system, user, ALL_TOOLS, r)
        umr, report = umrdoc.parse_answer(doc, r["text"])
        open(os.path.join(out_dir, name + ".raw.txt"), "w", encoding="utf-8").write(r["text"])
        path = os.path.join(out_dir, name + ".umr")
        open(path, "w", encoding="utf-8").write(umr)
        json.dump({"doc": name, "parse": report, "calls": [{k: v for k, v in r.items()
                                                            if k not in ("text", "messages", "responses")}]},
                  open(os.path.join(out_dir, name + ".trace.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return path, report, r

    def batch(self, n):
        """(batch doc, first, last, gold path) of batch n (1-based)."""
        k = (n - 1) * 5
        sents = self.train_doc["sents"][k:k + 5]
        doc = {"name": self.a.train_doc, "lang": "zh", "sents": sents}
        idx = {s["index"] for s in sents}
        out = []
        for s in sents:
            graph, align, _ = umrdoc.sentence_sections(s["index"], s["gold"][umrdoc.SECTIONS[0]],
                                                       s["gold"][umrdoc.SECTIONS[1]], strict=False)
            keep = []
            for t in umrdoc.read_doc(s["gold"][umrdoc.SECTIONS[2]]):
                ends = [x for x in (t[1], t[3]) if umrdoc.VAR.match(x)]
                if all(int(umrdoc.VAR.match(x).group(1)) in idx for x in ends):
                    keep.append(t)
            out.append((s["head"], {umrdoc.SECTIONS[0]: graph, umrdoc.SECTIONS[1]: align,
                                    umrdoc.SECTIONS[2]: umrdoc.render_doc(s["index"], keep)}))
        gold = os.path.join(self.out, "gold", "b%d.umr" % n)
        os.makedirs(os.path.dirname(gold), exist_ok=True)
        open(gold, "w", encoding="utf-8").write(umrdoc.render(out))
        return doc, sents[0]["index"], sents[-1]["index"], gold

    def score_batch(self, pred, gold, out_dir):
        an = score.ancast(pred, gold)
        js, units = score.judge(pred, gold)
        sm = score.smatch(pred, gold)
        s = {"ancast": an, "smatch_F": round(100 * score.prf(sm[0], sm[2], sm[1])[2], 2),
             "judge": {k: {x: v.get(x) for x in ("recall", "precision", "score")} for k, v in js.items()}}
        json.dump(s, open(os.path.join(out_dir, "scores.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return s, units

    @staticmethod
    def comp(s):
        return (s["ancast"] or {}).get("Comprehensive") or 0.0

    # ---------------------------------------------------------------- critique and reflect

    def critique(self, instruction, doc, pred, gold, s, units, out_dir):
        checks = "\n".join("%s: R %s / P %s / F %s" % (k, *("–" if v[x] is None else "%.0f" % (100 * v[x])
                                                           for x in ("recall", "precision", "score")))
                           for k, v in s["judge"].items() if v["score"] is not None)
        bad = [u for u in units if u["verdict"] != "correct"]
        lines = ["%s | %s | %s: %s -> %s%s" % (u["check"], u["verdict"], u.get("unit", ""), u.get("gold") or "-",
                                               u.get("pred") or "-", (" | " + u["detail"]) if u.get("detail") else "")
                 for u in bad[:250]]
        if len(bad) > 250:
            lines.append("... (%d more)" % (len(bad) - 250))
        text = CRITIQUE.format(variant=VARIANT[self.a.variant]["critique"], instruction=instruction,
                               lines=R.annotation(doc)["lines"], pred=strip_alignment(open(pred, encoding="utf-8").read()),
                               gold=strip_alignment(open(gold, encoding="utf-8").read()), checks=checks,
                               units="\n".join(lines) or "(none)")
        self.skip(True)
        r = llm.answer(self.a.model, CRITIQUE_SYSTEM, text, ALL_TOOLS, self.a.effort, CACHE)
        R.write_transcript(out_dir, "critique", self.a.model, self.a.effort, CRITIQUE_SYSTEM, text, ALL_TOOLS, r)
        open(os.path.join(out_dir, "critique.md"), "w", encoding="utf-8").write(r["text"])
        return r["text"]

    def reflect(self, instruction, critique, n, first, last, sc, history, out_dir):
        text = REFLECT.format(max_chars=MAX_CHARS, size=len(instruction), variant=VARIANT[self.a.variant]["reflect"],
                              instruction=instruction, batch=n, doc=self.a.train_doc, first=first, last=last,
                              score="%.1f" % sc, critique=critique, history="\n".join(history) or "(none: the first edit)")
        r = llm.answer(self.a.model, REFLECT_SYSTEM, text, [], self.a.effort, CACHE)
        R.write_transcript(out_dir, "reflect", self.a.model, self.a.effort, REFLECT_SYSTEM, text, [], r)
        open(os.path.join(out_dir, "reflect.md"), "w", encoding="utf-8").write(r["text"])
        m = re.findall(r"```json\s*(.*?)```", r["text"], re.S)
        try:
            prop = json.loads(m[-1]) if m else {}
        except ValueError as e:
            prop = {"error": "the JSON block does not parse: %s" % e}
        json.dump(prop, open(os.path.join(out_dir, "edits.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return prop

    def apply(self, instruction, prop):
        """(new instruction, [(edit, applied?, why)])."""
        new, done = instruction, []
        for ed in prop.get("edits") or []:
            op = ed.get("op")
            added = ed.get("new") or ed.get("text") or ""
            why = ""
            leak = copies(added, self.protect_test)
            if leak:
                why = "copies the test documents: %s" % leak
            elif self.a.variant == "rules" and copies(added, self.protect_train):
                why = "copies the training document: %s" % copies(added, self.protect_train)
            elif op == "rewrite":
                cand = ed.get("text", "")
            elif op == "append":
                cand = new.rstrip() + "\n\n" + ed.get("text", "").strip() + "\n"
            elif op in ("replace", "delete", "insert_after"):
                key = ed.get("anchor") if op == "insert_after" else ed.get("old")
                if not key or new.count(key) != 1:
                    why = "the anchor occurs %d times" % (new.count(key) if key else 0)
                elif op == "replace":
                    cand = new.replace(key, ed.get("new", ""), 1)
                elif op == "delete":
                    cand = new.replace(key, "", 1)
                else:
                    cand = new.replace(key, key + ed.get("text", ""), 1)
            else:
                why = "unknown op %r" % op
            if not why and len(cand) > MAX_CHARS:
                why = "the instruction would have %d characters (at most %d)" % (len(cand), MAX_CHARS)
            if not why:
                new = cand
            done.append({"op": op, "applied": not why, "why": why,
                         "edit": {k: (v[:300] + "..." if isinstance(v, str) and len(v) > 300 else v) for k, v in ed.items()}})
        return new, done

    # ---------------------------------------------------------------- test

    def test(self, instruction, tag):
        out_dir = os.path.join(self.out, "test", tag)
        for d in TEST:
            self.annotate(instruction, R.doc_of(d), out_dir, d)
        res = R.score_dir(out_dir)
        import breakdown as B
        m, _ = B.metrics(res["docs"], TEST)          # the two test documents pooled (not the 15-file language)
        z = {k: round(m[k], 2) for k in ("Smatch F", "AnCast Comprehensive", "AnCast F", "juːmæʧ F") if m.get(k) is not None}
        self.log("test %s: Smatch %s, AnCast++ comp %s, AnCast F %s, juːmæʧ %s" % (
            tag, z.get("Smatch F"), z.get("AnCast Comprehensive"), z.get("AnCast F"), z.get("juːmæʧ F")))
        return z

    # ---------------------------------------------------------------- the trajectory

    def main(self):
        a = self.a
        best = self.instruction0
        versions = [best]
        vdir = os.path.join(self.out, "versions")
        os.makedirs(vdir, exist_ok=True)
        open(os.path.join(vdir, "v0.md"), "w", encoding="utf-8").write(best)
        state = {"variant": a.variant, "model": a.model, "effort": a.effort, "train_doc": a.train_doc,
                 "batches": [], "tests": {}}
        history = []
        self.log("start: %s, %s (%s), %d batches x %d reflections, instruction %d characters" % (
            a.variant, a.model, a.effort, a.batches, a.reflections, len(best)))
        state["tests"]["before"] = self.test(best, "v0")
        for n in range(1, a.batches + 1):
            doc, first, last, gold = self.batch(n)
            d0 = os.path.join(self.out, "b%d" % n, "r0")
            pred, _, _ = self.annotate(best, doc, d0, "batch", "%s, sentences %d-%d" % (a.train_doc, first, last), True)
            s, units = self.score_batch(pred, gold, d0)
            best_score, best_pred, best_units, best_s = self.comp(s), pred, units, s
            bstate = {"batch": n, "first": first, "last": last, "start": best_score, "reflections": []}
            self.log("batch %d (sentences %d-%d): AnCast++ comp %.1f with v%d" % (n, first, last, best_score, len(versions) - 1))
            for j in range(1, a.reflections + 1):
                rd = os.path.join(self.out, "b%d" % n, "r%d" % j)
                os.makedirs(rd, exist_ok=True)
                crit = self.critique(best, doc, best_pred, gold, best_s, best_units, rd)
                prop = self.reflect(best, crit, n, first, last, best_score, history, rd)
                cand, done = self.apply(best, prop)
                json.dump(done, open(os.path.join(rd, "applied.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                open(os.path.join(rd, "instruction.md"), "w", encoding="utf-8").write(cand)
                open(os.path.join(rd, "edits.diff"), "w", encoding="utf-8").write("".join(difflib.unified_diff(
                    best.splitlines(True), cand.splitlines(True), "before", "after")))
                rec = {"reflection": j, "summary": prop.get("summary") or prop.get("error", ""),
                       "edits": len(done), "applied": sum(e["applied"] for e in done)}
                if cand == best:
                    rec.update(score=None, accepted=False, why="no edit applied")
                else:
                    p2, _, _ = self.annotate(cand, doc, rd, "batch", "%s, sentences %d-%d" % (a.train_doc, first, last), True)
                    s2, units2 = self.score_batch(p2, gold, rd)
                    rec.update(score=self.comp(s2), accepted=self.comp(s2) > best_score)
                    if rec["accepted"]:
                        best, best_score, best_pred, best_units, best_s = cand, self.comp(s2), p2, units2, s2
                        versions.append(best)
                        rec["version"] = len(versions) - 1
                        open(os.path.join(vdir, "v%d.md" % rec["version"]), "w", encoding="utf-8").write(best)
                if rec["score"] is None:
                    outcome = "no edit applied"
                elif rec["accepted"]:
                    outcome = "AnCast++ comp %.1f on the batch, kept" % rec["score"]
                else:
                    outcome = "AnCast++ comp %.1f on the batch, not kept (the best was %.1f)" % (rec["score"], best_score)
                history.append("- batch %d, reflection %d (%d/%d edits applied): %s -> %s" % (
                    n, j, rec["applied"], rec["edits"], rec["summary"][:400], outcome))
                self.log("batch %d reflection %d: %d/%d edits applied, score %s, %s; instruction %d characters" % (
                    n, j, rec["applied"], rec["edits"], "–" if rec["score"] is None else "%.1f" % rec["score"],
                    "kept (v%d)" % rec["version"] if rec.get("accepted") else "not kept", len(best)))
                bstate["reflections"].append(rec)
            bstate["end"], bstate["version"] = best_score, len(versions) - 1
            state["batches"].append(bstate)
            state["tests"]["after-b%d" % n] = self.test(best, "after-b%d" % n)
            json.dump(state, open(os.path.join(self.out, "state.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        self.log("done: %d versions" % len(versions))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--variant", choices=sorted(VARIANT), required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--train-doc", default="chinese_umr-0001")
    ap.add_argument("--batches", type=int, default=4)
    ap.add_argument("--reflections", type=int, default=3)
    a = ap.parse_args()
    R.DOCS = [d for d in R.ALL_DOCS if d["lang"] in ("zh", "en")]
    Runner(a).main()


if __name__ == "__main__":
    main()
