#!/usr/bin/env python3
"""Make a review workspace for a new set of gold files and parser outputs.

    python3 .claude/skills/umr-gold-review/scripts/new_workspace.py --to ../my-review \\
        --gold path/to/gold_dir --run s3/r1=path/to/outputs_a --run s3/r2=path/to/outputs_b --run a2/r1=path/to/outputs_c

--gold   a folder of gold .umr files (zh-0023.umr, en-0005.umr, chinese_umr-0023.umr, english_umr-0005.umr, ...)
--run    KEY=DIR, once per parser output: KEY is setting/run (s3/r1; a bare name gets /r1), DIR holds one .umr
         per document, named like the gold files
--toolkit  where the scripts are copied from (default: exp/review-round2 of this repository)

The workspace gets the toolkit's scripts (pipeline/, lib/, tools/, vendor/, the review page's files), a link to
its resources/, data/gold, data/input (the tokens of the gold, one sentence per line), data/docs.json,
config.json and runs/<setting>/sys-<run>/<doc>.umr. Nothing of the toolkit's own data or review is copied.
"""
import argparse
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
CODE = ["pipeline", "lib", "tools", "vendor", "requirements.txt"]
REVIEW = ["engine.js", "validate.js", "apply_proposals.js", "goldtext.js", "template.html", "build.py", "REVIEWER.md"]


def doc_id(stem):
    m = re.match(r"(chinese|english)_umr-(\d+)$", stem)
    return ("zh-" if m.group(1) == "chinese" else "en-") + m.group(2) if m else stem


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--to", required=True)
    ap.add_argument("--gold", required=True)
    ap.add_argument("--run", action="append", default=[], metavar="KEY=DIR")
    ap.add_argument("--toolkit", default=os.path.join(REPO, "exp", "review-round2"))
    a = ap.parse_args()
    tk, to = os.path.abspath(a.toolkit), os.path.abspath(a.to)
    if os.path.exists(to) and os.listdir(to):
        raise SystemExit("%s exists and is not empty" % to)
    if not a.run:
        raise SystemExit("give at least one --run KEY=DIR")
    for name in CODE:
        src = os.path.join(tk, name)
        dst = os.path.join(to, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "build", "*.egg-info"))
        else:
            os.makedirs(to, exist_ok=True)
            shutil.copy(src, dst)
    for sub in ("review/items", "review/reports", "review/points", "review/proposals", "data/gold", "data/input", "analysis"):
        os.makedirs(os.path.join(to, sub))
    for name in REVIEW:
        shutil.copy(os.path.join(tk, "review", name), os.path.join(to, "review", name))
    if os.path.isdir(os.path.join(tk, "resources")):
        os.symlink(os.path.join(tk, "resources"), os.path.join(to, "resources"))
    sys.path.insert(0, os.path.join(to, "lib"))
    import umrdoc
    docs = []
    for f in sorted(os.listdir(a.gold)):
        if not f.endswith(".umr"):
            continue
        stem = f[:-4]
        shutil.copy(os.path.join(a.gold, f), os.path.join(to, "data", "gold", f))
        d = umrdoc.load(os.path.join(to, "data", "gold", f))
        did = doc_id(stem)
        with open(os.path.join(to, "data", "input", did + ".txt"), "w", encoding="utf-8") as out:
            out.write("\n".join(" ".join(s["words"]) for s in d["sents"]) + "\n")
        docs.append({"doc": did, "gold": stem, "lang": umrdoc.lang_of(did), "sents": len(d["sents"]),
                     "tokens": sum(len(s["words"]) for s in d["sents"]), "test": True, "gold_source": os.path.abspath(a.gold)})
    if not docs:
        raise SystemExit("no .umr file in %s" % a.gold)
    with open(os.path.join(to, "data", "docs.json"), "w", encoding="utf-8") as f:
        json.dump({"docs": docs}, f, ensure_ascii=False, indent=1)
    conds, runs = [], []
    for spec in a.run:
        key, _, src = spec.partition("=")
        cond, _, run = key.partition("/")
        run = run or "r1"
        if not re.match(r"^[A-Za-z0-9_.-]+$", cond) or not re.match(r"^[A-Za-z0-9_.-]+$", run) or not os.path.isdir(src):
            raise SystemExit("bad --run %r: KEY=DIR, KEY like s3/r1, DIR an existing folder" % spec)
        if cond not in conds:
            conds.append(cond)
        if run not in runs:
            runs.append(run)
        dst = os.path.join(to, "runs", cond, "sys-" + run)
        os.makedirs(dst, exist_ok=True)
        n = 0
        for f in sorted(os.listdir(src)):
            if f.endswith(".umr") and any(d["doc"] == doc_id(f[:-4]) for d in docs):
                shutil.copy(os.path.join(src, f), os.path.join(dst, doc_id(f[:-4]) + ".umr"))
                n += 1
        print("%s/%s: %d of %d documents" % (cond, run, n, len(docs)))
    config = {"_comment": "made by new_workspace.py: one entry of conditions per setting, one of models per run; "
                          "the outputs are in runs/<condition name>/sys-<run>/<doc>.umr",
              "models": [{"key": r, "model": "sys", "effort": "", "run": r} for r in runs],
              "conditions": [{"key": c, "name": c} for c in conds],
              "lang_labels": {}}
    with open(os.path.join(to, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=1)
    print("workspace: %s (%d documents, %d sentences)" % (to, len(docs), sum(d["sents"] for d in docs)))
    print("next: edit review/REVIEWER.md (the table of systems, the decided rules), then follow SKILL.md from step 2")


if __name__ == "__main__":
    main()
