"""Copy the numbers the paper uses out of a SkillParseUMR checkout into data/.

    python analysis/extract_umr.py --src /path/to/SkillParseUMR [--bold /path/to/worktree-of-bold-curie]

--src    a checkout of sxndqc/SkillParseUMR at main (experiment/rsi-zh-critique, rsi-zh2, rsi-zh-refine,
         qwen-zh, qwen27-zh, rsi-zh-deepseek)
--bold   a checkout of the branch claude/bold-curie-nle80f (experiment/timeml, experiment/manifesto);
         optional, those two runs are not finished

Only small files are copied (scores, per-step scores, per-sentence smatch, skill sizes, edit counts).
data/PROVENANCE.md says which commit each file came from; rerun this script after the source
experiments have more rounds and the tables regenerate with analysis/make_tables.py.
"""
import argparse
import csv
import glob
import json
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def commit(path):
    out = subprocess.run(["git", "-C", path, "log", "-1", "--format=%h %ad %s", "--date=short"],
                         capture_output=True, text=True)
    return out.stdout.strip()


def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


def version_of(k, parse):
    """The skill version that made the parse `parse` of the k-th training document (1-based)."""
    if parse == "R0":
        return "R0"
    if parse == "iter1":
        return "R0" if k == 1 else "R%d3" % (k - 1)
    return {"iter2": "R%d1", "iter3": "R%d2", "after": "R%d3"}[parse] % k


def critique(src):
    base = os.path.join(src, "experiment", "rsi-zh-critique")
    out = os.path.join(DATA, "umr")
    copy(os.path.join(base, "scores.json"), os.path.join(out, "critique_scores.json"))
    copy(os.path.join(base, "steps.json"), os.path.join(out, "critique_steps.json"))

    # size of each skill (skill.md + reference/example.md) per version, in KB
    sizes = {}
    for v in sorted(os.listdir(os.path.join(base, "skills"))):
        sizes[v] = {}
        for skill in ("generate", "critique", "document"):
            total = 0
            for rel in ("skill.md", os.path.join("reference", "example.md")):
                p = os.path.join(base, "skills", v, skill, rel)
                if os.path.exists(p):
                    total += os.path.getsize(p)
            sizes[v][skill] = round(total / 1024, 1)
        sizes[v]["tools"] = sorted(os.listdir(os.path.join(base, "skills", v, "tools")))
        sizes[v]["skills"] = sorted(d for d in os.listdir(os.path.join(base, "skills", v))
                                    if os.path.isdir(os.path.join(base, "skills", v, d)) and d != "tools")
    with open(os.path.join(out, "critique_sizes.json"), "w") as f:
        json.dump(sizes, f, indent=1)

    # per-sentence smatch of every parse
    rows = []
    docs = sorted(d for d in os.listdir(os.path.join(base, "train")))
    for k, doc in enumerate(docs, 1):
        for parse in ("R0", "iter1", "iter2", "iter3", "after"):
            p = os.path.join(base, "train", doc, parse, "judge", "sentences.csv")
            if not os.path.exists(p):
                continue
            with open(p, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    rows.append([doc, parse, version_of(k, parse), r["sent"], r["status"], r["smatch"]])
    with open(os.path.join(out, "critique_sentences.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["doc", "parse", "version", "sent", "status", "smatch"])
        w.writerows(rows)

    # the edits of every round
    rounds = {}
    for k, doc in enumerate(docs, 1):
        for y in (1, 2, 3):
            d = os.path.join(base, "rsi", doc, "iter%d" % y)
            if not os.path.exists(os.path.join(d, "applied.json")):
                continue
            applied = json.load(open(os.path.join(d, "applied.json")))
            plan = json.load(open(os.path.join(d, "plan.json")))
            structural = json.load(open(os.path.join(d, "structural.json")))
            r = {"doc": doc, "edits": {}, "rejected": [], "analysis_chars": len(plan.get("analysis", "")),
                 "suggestions": len(plan.get("suggestions", [])), "structural": []}
            for e in applied:
                key = "%s/%s/%s" % (e["skill"], e["file"], e["action"])
                if e["status"] == "applied":
                    r["edits"][key] = r["edits"].get(key, 0) + 1
                else:
                    r["rejected"].append(str(e.get("why") or e.get("reason") or "")[:160])
            for s in structural:
                r["structural"].append({"kind": s["kind"], "name": s["name"], "status": s["status"],
                                        "why": (s.get("why") or "")[:1500]})
            rounds["R%d%d" % (k, y)] = r
    with open(os.path.join(out, "critique_rounds.json"), "w") as f:
        json.dump(rounds, f, indent=1, ensure_ascii=False)


def others(src, bold):
    out = os.path.join(DATA, "umr")
    for name, dst in [("rsi-zh2", "tree"), ("rsi-zh-refine", "refine")]:
        copy(os.path.join(src, "experiment", name, "scores.json"), os.path.join(out, dst + "_scores.json"))
    copy(os.path.join(src, "experiment", "rsi-zh-refine", "steps.json"), os.path.join(out, "refine_steps.json"))
    out = os.path.join(DATA, "other")
    for name, dst in [("qwen-zh", "qwen9b_zh"), ("qwen-en", "qwen9b_en"), ("qwen27-zh", "qwen27b_zh"),
                      ("rsi-zh-deepseek", "deepseek_zh")]:
        p = os.path.join(src, "experiment", name, "scores.json")
        if os.path.exists(p):
            copy(p, os.path.join(out, dst + "_scores.json"))
        p = os.path.join(src, "experiment", name, "scores.md")
        if os.path.exists(p):
            copy(p, os.path.join(out, dst + "_scores.md"))
    if bold:
        for name in ("timeml", "manifesto"):
            for f in ("scores.json", "scores.md", "SOTA.md"):
                p = os.path.join(bold, "experiment", name, f)
                if os.path.exists(p):
                    copy(p, os.path.join(out, "%s_%s" % (name, f)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--bold")
    args = ap.parse_args()
    critique(args.src)
    others(args.src, args.bold)
    with open(os.path.join(DATA, "PROVENANCE.md"), "w") as f:
        f.write("# Provenance of data/\n\nWritten by analysis/extract_umr.py.\n\n")
        f.write("- sxndqc/SkillParseUMR, %s\n" % commit(args.src))
        if args.bold:
            f.write("- sxndqc/SkillParseUMR branch claude/bold-curie-nle80f (timeml, manifesto; runs not finished), %s\n"
                    % commit(args.bold))
        f.write("\nFiles in data/umr/: critique_* from experiment/rsi-zh-critique, tree_scores.json from experiment/rsi-zh2, "
                "refine_* from experiment/rsi-zh-refine.\n"
                "Files in data/other/: qwen9b_zh, qwen9b_en, qwen27b_zh, deepseek_zh from the experiment directories of "
                "the same names (rsi-zh-deepseek for DeepSeek); timeml_*, manifesto_* from the bold-curie branch.\n")


if __name__ == "__main__":
    main()
