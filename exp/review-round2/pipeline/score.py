"""Score every system output against the original gold and, where there is one, the corrected gold.

    python3 pipeline/score.py [--jobs 6]

Reads runs/<condition>/<model>-<effort>-<run>/<doc>.umr, data/gold/, data/gold_revised/<doc>.umr.
Writes analysis/scores.json (per document and per sentence; review/build.py shows it in the review page)
and analysis/scores.md (the tables).

The corrected gold of a document is data/gold_revised/<doc>.umr: made by `node review/apply_proposals.js`
(every proposal that is not low-confidence applied) or, better, the file the reviewer exported from the
review page. Documents without one are scored against the original gold only.
"""
import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ancast_run as A  # noqa: E402
import common as C  # noqa: E402

COLS = [("comp", "Comprehensive"), ("sent", "sentence"), ("modal", "modal"), ("temporal", "temporal"), ("coref", "coref")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    systems = C.systems()
    tasks = []
    for d in C.DOCS:
        golds = [("orig", C.gold_path(d))] + ([("rev", C.revised_path(d))] if C.revised_path(d) else [])
        if C.official_path(d):
            golds.append(("off", C.official_path(d)))
        for key, _, _, run_dir in systems:
            pred = os.path.join(run_dir, d["doc"] + ".umr")
            if os.path.exists(pred):
                tasks += [(d["doc"], key, ver, pred, g) for ver, g in golds]
        if C.revised_path(d):
            tasks.append((d["doc"], "gold", "rev", golds[0][1], C.revised_path(d)))
    print("%d AnCast runs (cached ones are instant)" % len(tasks), flush=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        results = list(pool.map(lambda t: A.pair(t[3], t[4]), tasks))
    out = {}
    for (doc, key, ver, _, _), r in zip(tasks, results):
        if r.get("error"):
            print("FAILED", doc, key, ver, r["error"][-300:])
            continue
        o = out.setdefault(doc, {"sent": {}, "doc": {}})
        if key == "gold":
            o["gold"] = {"doc": r["doc"], "sent": r["sent"]}
            continue
        o["doc"].setdefault(key, {})[ver] = r["doc"]
        for sid, v in r["sent"].items():
            o["sent"].setdefault(sid, {}).setdefault(key, {})[ver] = v
    os.makedirs(C.ANALYSIS, exist_ok=True)
    with open(os.path.join(C.ANALYSIS, "scores.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    keys = [k for k, *_ in systems]
    rev_docs = [d["doc"] for d in C.DOCS if "gold" in out.get(d["doc"], {})]
    lines = ["# Scores against the gold (AnCast++, document scope; Smatch from the same run)", "",
             "Mean over documents; sentence AnCast and Smatch are means over sentences. `n` is the number of "
             "documents a system has an output for.", ""]

    def table(title, ver, docs):
        rows = ["## " + title, "", "| system | n | " + " | ".join(l for _, l in COLS) + " | sentence AnCast | Smatch |",
                "|---|---|" + "---|" * (len(COLS) + 2)]
        for k in keys:
            have = [d for d in docs if ver in out.get(d, {}).get("doc", {}).get(k, {})]
            if not have:
                continue
            sent = [v[k][ver] for d in have for v in out[d]["sent"].values() if ver in v.get(k, {})]
            rows.append("| %s | %d | %s | %s | %s |" % (
                k, len(have), " | ".join(str(A.mean([out[d]["doc"][k][ver].get(c) for d in have])) for c, _ in COLS),
                A.mean([x["ancast"] for x in sent]), A.mean([x["smatch"] for x in sent])))
        return rows + [""]

    all_docs = [d["doc"] for d in C.DOCS]
    test_docs = [d["doc"] for d in C.DOCS if d.get("test")]
    off_docs = [d["doc"] for d in C.DOCS if C.official_path(d)]
    lines += table("Against the gold (data/gold; %d documents, every system on the documents it has)" % len(all_docs), "orig", all_docs)
    if test_docs and len(test_docs) < len(all_docs):
        lines += table("Against the gold, only the %d test documents of the shared task" % len(test_docs), "orig", test_docs)
        for lang in dict.fromkeys(d["lang"] for d in C.DOCS if d.get("test")):
            docs_l = [d["doc"] for d in C.DOCS if d.get("test") and d["lang"] == lang]
            lines += table("Test documents, %s (%d)" % (lang, len(docs_l)), "orig", docs_l)
    if off_docs:
        lines += table("Against the released gold where it is another version (data/gold_official; %d documents: %s)" % (
            len(off_docs), ", ".join(off_docs)), "off", off_docs)
        lines += table("The same %d documents against data/gold, for comparison" % len(off_docs), "orig", off_docs)
    if rev_docs:
        lines += table("Against the original gold, only the %d documents that have a corrected gold" % len(rev_docs),
                       "orig", rev_docs)
        lines += table("Against the corrected gold (%d documents: %s)" % (len(rev_docs), ", ".join(rev_docs)), "rev", rev_docs)
        lines += ["## Original gold against corrected gold", "",
                  "| document | " + " | ".join(l for _, l in COLS) + " |", "|---|" + "---|" * len(COLS)]
        for d in rev_docs:
            lines.append("| %s | %s |" % (d, " | ".join(str(out[d]["gold"]["doc"].get(c)) for c, _ in COLS)))
        lines.append("")
        lines += ["## Change per system when the gold is corrected (Comprehensive, corrected minus original)", "",
                  "| system | original | corrected | change |", "|---|---|---|---|"]
        for k in keys:
            have = [d for d in rev_docs if "rev" in out[d]["doc"].get(k, {}) and "orig" in out[d]["doc"].get(k, {})]
            if have:
                o = A.mean([out[d]["doc"][k]["orig"]["comp"] for d in have])
                r = A.mean([out[d]["doc"][k]["rev"]["comp"] for d in have])
                lines.append("| %s | %s | %s | %+.1f |" % (k, o, r, (r or 0) - (o or 0)))
        lines.append("")
    lines += ["## Per document, Comprehensive against the original gold", "",
              "| document | sentences | " + " | ".join(keys) + " |", "|---|---|" + "---|" * len(keys)]
    for d in C.DOCS:
        row = out.get(d["doc"], {}).get("doc", {})
        lines.append("| %s | %d | %s |" % (d["doc"], d["sents"], " | ".join(
            str(row.get(k, {}).get("orig", {}).get("comp", "–")) for k in keys)))
    with open(os.path.join(C.ANALYSIS, "scores.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote analysis/scores.json, analysis/scores.md")


if __name__ == "__main__":
    main()
