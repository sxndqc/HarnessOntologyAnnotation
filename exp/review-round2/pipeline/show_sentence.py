"""One sentence as the gold and every system annotate it, one after the other (for writing the diff report).

    python3 pipeline/show_sentence.py zh-0005 12            gold + the 6 systems
    python3 pipeline/show_sentence.py zh-0005 12 --only gold,s3/r1,a2/r2
    python3 pipeline/show_sentence.py zh-0005 --grep 发行-01   which annotations have this text, per sentence
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import umrdoc  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc")
    ap.add_argument("sentence", nargs="?", type=int)
    ap.add_argument("--only", default="")
    ap.add_argument("--grep", default="")
    a = ap.parse_args()
    d = C.docs(a.doc)[0]
    files = [("gold", C.gold_path(d))]
    if C.revised_path(d):
        files.append(("gold-rev", C.revised_path(d)))
    files += [(k, os.path.join(run_dir, d["doc"] + ".umr")) for k, _, _, run_dir in C.systems()]
    only = [x for x in a.only.split(",") if x]
    for key, path in files:
        if only and key not in only:
            continue
        if not os.path.exists(path):
            print("=" * 20, key, "(no output)")
            continue
        doc = umrdoc.load(path)
        for s in doc["sents"]:
            if a.sentence and s["index"] != a.sentence:
                continue
            g = s["gold"]
            if a.grep:
                hits = [l.strip() for k in umrdoc.SECTIONS for l in g[k].splitlines() if a.grep in l]
                if hits:
                    print("%-9s snt%-3d %s" % (key, s["index"], " ‖ ".join(hits)[:300]))
                continue
            print("=" * 20, key, "snt%d" % s["index"])
            if key == "gold":
                print(" ".join("%d:%s" % (i + 1, w) for i, w in enumerate(s["words"])))
            print(g[umrdoc.SECTIONS[0]])
            print("# alignment: " + " | ".join(l.strip() for l in g[umrdoc.SECTIONS[1]].splitlines() if l.strip()))
            print(re.sub(r"\n\s+", "\n    ", g[umrdoc.SECTIONS[2]]))


if __name__ == "__main__":
    main()
