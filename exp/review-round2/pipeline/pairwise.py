"""How far the systems are from each other and from the gold: AnCast++ of every pair, per document.

    python3 pipeline/pairwise.py [--jobs 6] [--docs zh-0028,zh-0032]

Every unordered pair among the systems, the original gold and (where there is one) the corrected gold:
6 systems + gold = 21 pairs per document. Writes analysis/pairwise.json and analysis/pairwise.md: the matrix
(mean over documents of the Comprehensive score, and of sentence-level Smatch), each system's mean to the
others, and the means by kind of pair (the two runs of one condition, different conditions).

This is the automatic measure. The measure the earlier analysis preferred is agreement at the annotation
comparison points (pipeline/points_agree.py), which needs the diff reports coded into points first.
"""
import argparse
import itertools
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ancast_run as A  # noqa: E402
import common as C  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--docs", default="")
    a = ap.parse_args()
    systems = C.systems()
    tasks = []
    for d in C.docs(a.docs):
        files = {k: os.path.join(run_dir, d["doc"] + ".umr") for k, _, _, run_dir in systems}
        files = {k: p for k, p in files.items() if os.path.exists(p)}
        files["gold"] = C.gold_path(d)
        if C.revised_path(d):
            files["gold-rev"] = C.revised_path(d)
        for x, y in itertools.combinations(list(files), 2):
            tasks.append((d["doc"], x, y, files[x], files[y]))      # x as "prediction", y as "gold"
    print("%d AnCast runs (cached ones are instant)" % len(tasks), flush=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        results = list(pool.map(lambda t: A.pair(t[3], t[4]), tasks))
    per = {}
    for (doc, x, y, _, _), r in zip(tasks, results):
        if r.get("error"):
            print("FAILED", doc, x, y, r["error"][-300:])
            continue
        per.setdefault(doc, {})["%s|%s" % (x, y)] = {
            **r["doc"], "smatch": A.mean([v["smatch"] for v in r["sent"].values()]),
            "ancast": A.mean([v["ancast"] for v in r["sent"].values()])}
    os.makedirs(C.ANALYSIS, exist_ok=True)
    with open(os.path.join(C.ANALYSIS, "pairwise.json"), "w", encoding="utf-8") as f:
        json.dump(per, f, ensure_ascii=False, indent=1)

    keys = [k for k, *_ in systems] + ["gold", "gold-rev"]

    def val(x, y, metric):
        xs = []
        for doc, pairs in per.items():
            p = pairs.get("%s|%s" % (x, y)) or pairs.get("%s|%s" % (y, x))
            if p:
                xs.append(p.get(metric))
        return A.mean(xs), len([v for v in xs if v is not None])

    present = [k for k in keys if any(val(k, o, "comp")[1] for o in keys if o != k)]
    sys_keys = [k for k in present if not k.startswith("gold")]
    lines = ["# Pairwise distance between the annotations (AnCast++, document scope)", "",
             "Higher = more alike. Mean over the documents both have (%d documents scored)." % len(per), ""]
    for metric, title in (("comp", "Comprehensive"), ("sent", "sentence level"), ("smatch", "Smatch (mean over sentences)")):
        lines += ["## %s" % title, "", "| | " + " | ".join(present) + " |", "|---|" + "---|" * len(present)]
        for x in present:
            lines.append("| **%s** | %s |" % (x, " | ".join("–" if x == y else str(val(x, y, metric)[0]) for y in present)))
        lines.append("")
    lines += ["## Each system: mean to the other systems, and to the gold (Comprehensive)", "",
              "| system | mean to the other systems | to the original gold | to the corrected gold |", "|---|---|---|---|"]
    for k in sys_keys:
        lines.append("| %s | %s | %s | %s |" % (k, A.mean([val(k, o, "comp")[0] for o in sys_keys if o != k]),
                                               val(k, "gold", "comp")[0], val(k, "gold-rev", "comp")[0] or "–"))
    cond = lambda k: k.split("/")[0]
    model = lambda k: k.split("/")[1]
    groups = {"same condition, the two runs": [], "different conditions, same run": [], "different conditions, different runs": []}
    for x, y in itertools.combinations(sys_keys, 2):
        v = val(x, y, "comp")[0]
        name = ("same condition, the two runs" if cond(x) == cond(y) else
                "different conditions, same run" if model(x) == model(y) else "different conditions, different runs")
        groups[name].append(v)
    lines += ["", "## By kind of pair (Comprehensive)", "", "| pairs | n | mean |", "|---|---|---|"]
    for name, vs in groups.items():
        lines.append("| %s | %d | %s |" % (name, len(vs), A.mean(vs)))
    for m in sorted({model(k) for k in sys_keys}):
        vs = [val(x, y, "comp")[0] for x, y in itertools.combinations([k for k in sys_keys if model(k) == m], 2)]
        lines.append("| within run %s | %d | %s |" % (m, len(vs), A.mean(vs)))
    ranked = sorted(((val(x, y, "comp")[0], x, y) for x, y in itertools.combinations(sys_keys, 2)
                     if val(x, y, "comp")[0] is not None), reverse=True)
    lines += ["", "## Pairs from closest to farthest (Comprehensive)", ""] + ["- %s  %s ~ %s" % r for r in ranked]
    with open(os.path.join(C.ANALYSIS, "pairwise.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote analysis/pairwise.json, analysis/pairwise.md")


if __name__ == "__main__":
    main()
