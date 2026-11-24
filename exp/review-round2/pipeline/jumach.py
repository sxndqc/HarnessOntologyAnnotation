"""juːmæʧ, the main metric of the DMR 2026 UMR parsing shared task, for every system on the test set.

    python3 pipeline/jumach.py [--jobs 6]    -> analysis/jumach.md, analysis/jumach.json

Scorer: ufal/umrtools compare_umr.pl (vendor/umrtools), `perl compare_umr.pl GOLD gold.umr SYS pred.umr --tsv`.
A language's score is the F1 of the counts (correct, gold, predicted) summed over its files, as umrtools
micro_average.pl does. Gold: the shared task's test gold, UMR 2.2 test-gold (data/gold_st22). The two
submitted systems (UMR 2.2 system-outputs: orange, sema) are scored the same way, to check the numbers
against the overview paper. For the 13 Chinese test files of the first round the gold under review
(data/gold) is scored too.
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

SCRIPT = os.path.join(C.PKG, "vendor", "umrtools", "compare_umr.pl")
ST = os.path.join(C.PKG, "data", "gold_st22")
OTHERS = os.path.join(C.ANALYSIS, "shared-task-systems")


def one(pred, gold):
    try:
        p = subprocess.run(["perl", SCRIPT, "GOLD", gold, "SYS", pred, "--tsv"], capture_output=True, text=True, timeout=1800)
    except subprocess.TimeoutExpired:
        return None
    for line in p.stdout.splitlines():
        cells = line.split("\t")
        if len(cells) >= 6 and cells[0].strip().startswith("ju"):
            return int(cells[3]), int(cells[4]), int(cells[5])
    return None


def f1(c, g, p):
    pr, rc = (c / p if p else 0), (c / g if g else 0)
    return round(100 * 2 * pr * rc / (pr + rc), 2) if pr + rc else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    docs = [d for d in C.DOCS if d.get("test")]
    systems = [(k, rd) for k, _, _, rd in C.systems()] + [(n, os.path.join(OTHERS, n)) for n in ("orange", "sema")
                                                           if os.path.isdir(os.path.join(OTHERS, n))]
    tasks = []
    for d in docs:
        for k, rd in systems:
            pred = os.path.join(rd, d["doc"] + ".umr")
            if os.path.exists(pred):
                st = os.path.join(ST, d["doc"] + ".umr")      # no shared-task gold for the document: the gold under review
                tasks.append((d["doc"], d["lang"], k, "st", pred, st if os.path.exists(st) else C.gold_path(d)))
                if C.official_path(d) and "/" in k:
                    tasks.append((d["doc"], d["lang"], k, "own", pred, C.gold_path(d)))
                if C.revised_path(d) and "/" in k:
                    tasks.append((d["doc"], d["lang"], k, "base", pred, C.gold_path(d)))
                    tasks.append((d["doc"], d["lang"], k, "rev", pred, C.revised_path(d)))
    print("%d comparisons" % len(tasks), flush=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        res = list(pool.map(lambda t: one(t[4], t[5]), tasks))
    out = {}
    for (doc, lang, k, ver, _, _), r in zip(tasks, res):
        if r is None:
            print("FAILED", doc, k, ver)
            continue
        out.setdefault(ver, {}).setdefault(doc, {})[k] = r
    with open(os.path.join(C.ANALYSIS, "jumach.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    keys = [k for k, _ in systems]
    langs = list(dict.fromkeys(d["lang"] for d in docs))

    def agg(ver, ds, k):
        rows = [out.get(ver, {}).get(d, {}).get(k) for d in ds]
        rows = [r for r in rows if r]
        return (f1(*[sum(x) for x in zip(*rows)]), len(rows)) if rows else (None, 0)

    L = ["# juːmæʧ（shared task 的主指标）", "",
         "打分器：ufal/umrtools `compare_umr.pl`。一种语言的分数是把该语言各文件的 correct / gold / predicted 计数加起来再算 F1。"
         "gold 是 shared task 的测试 gold（UMR 2.2 test-gold）。orange、sema 是两支参赛队伍公开的系统输出，用同一套打分重算，用来和概述论文对照。", "",
         "## 按语言（对 UMR 2.2 test-gold）", "", "| 系统 | " + " | ".join("%s (%d)" % (l, sum(d["lang"] == l for d in docs)) for l in langs) + " | 全部 %d 个文件 |" % len(docs),
         "|---|" + "---|" * (len(langs) + 1)]
    for k in keys:
        cells = []
        for l in langs:
            v, n = agg("st", [d["doc"] for d in docs if d["lang"] == l], k)
            cells.append("–" if v is None else "%.2f" % v)
        v, n = agg("st", [d["doc"] for d in docs], k)
        L.append("| %s | %s | %s |" % (k, " | ".join(cells), "–" if v is None else "%.2f" % v))
    own = sorted(out.get("own", {}))
    if own:
        L += ["", "## 上一轮的 13 篇中文测试文件：对两个版本的 gold", "", "| 系统 | 对 UMR 2.2 test-gold | 对在审的 gold（data/gold） |", "|---|---|---|"]
        for k in keys:
            if "/" in k:
                L.append("| %s | %s | %s |" % (k, agg("st", own, k)[0], agg("own", own, k)[0]))
    if out.get("rev"):
        L += ["", "## 对修订版 gold（data/gold_revised）：修订前 → 修订后", "",
              "修订版是在 data/gold 上应用审阅的 high、mid 修改方案得到的，所以这里的“修订前”是 data/gold（13 篇旧中文测试文件是在审版本，其余是 UMR 2.2 test-gold）。", "",
              "| 系统 | " + " | ".join(langs) + " | 全部 |", "|---|" + "---|" * (len(langs) + 1)]
        for k in keys:
            if "/" not in k:
                continue
            cells = []
            for ds in [[d["doc"] for d in docs if d["lang"] == l] for l in langs] + [[d["doc"] for d in docs]]:
                cells.append("%s → %s" % (agg("base", ds, k)[0], agg("rev", ds, k)[0]))
            L.append("| %s | %s |" % (k, " | ".join(cells)))
    L += ["", "## 逐篇（对 UMR 2.2 test-gold，单篇 F1）", "", "| 文档 | " + " | ".join(keys) + " |", "|---|" + "---|" * len(keys)]
    for d in docs:
        row = out.get("st", {}).get(d["doc"], {})
        L.append("| %s | %s |" % (d["doc"], " | ".join("%.1f" % f1(*row[k]) if k in row else "–" for k in keys)))
    with open(os.path.join(C.ANALYSIS, "jumach.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:16 + len(keys)]))


if __name__ == "__main__":
    main()
