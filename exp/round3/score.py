"""Scores of every run of round 3: umrjudge checks and juːmæʧ, each condition averaged over its runs.

    python3 score.py [--jobs 4]    -> analysis/scores.json

For a run (one wording, one repetition) and a group of documents, the umrjudge units of the documents are pooled
and each check gets recall, precision and F1; juːmæʧ sums its counts over the documents. A condition's figure
is the mean over its runs, with the standard deviation and the number of runs. Groups: test (4 files), test-zh,
test-en, train (4 files, against the clean training gold), and train-rev (against the revised gold of the
review, if review/data/gold_revised exists).
"""
import argparse
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
sys.path.insert(0, os.path.join(R2, "vendor", "umrancast"))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "judges"))
sys.path.insert(0, os.path.join(R2, "pipeline"))
CONFIG = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
KEEP = ("check", "verdict", "credit")


def one(t):
    import contextlib
    import io
    import umrjudge
    import jumach as J
    spec = umrjudge.load_spec()
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            units = umrjudge.judge_file(t[0], t[1], spec)["units"]
        except Exception as e:
            return {"error": "%s: %s" % (type(e).__name__, e)}
    try:
        ju = J.one(t[0], t[1])
    except Exception:
        ju = None
    return {"units": [{k: u[k] for k in KEEP if k in u} for u in units], "jumach": ju}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    import umrjudge
    spec = umrjudge.load_spec()
    checks = [c["id"] for c in spec["checks"]]
    G = CONFIG["groups"]
    gold = lambda d: os.path.join(HERE, "data", "gold", d + ".umr")
    rev = lambda d: os.path.join(HERE, "review", "data", "gold_revised", d + ".umr")
    groups = [("test", G["test"], gold), ("test-zh", [d for d in G["test"] if d.startswith("zh")], gold),
              ("test-en", [d for d in G["test"] if d.startswith("en")], gold), ("train", G["train"], gold)]
    if all(os.path.exists(rev(d)) for d in G["train"]):
        groups.append(("train-rev", G["train"], rev))
    runs = []
    for cond in sorted(os.listdir(os.path.join(HERE, "runs"))):
        for r in sorted(os.listdir(os.path.join(HERE, "runs", cond))):
            runs.append((cond, r, os.path.join(HERE, "runs", cond, r)))
    cache_path = os.path.join(HERE, "analysis", ".score-cache.json")
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    pairs = []
    for _, ds, gold_of in groups:
        for d in ds:
            for _, _, rd in runs:
                p = os.path.join(rd, d + ".umr")
                if os.path.exists(p):
                    key = "%s|%s|%d|%d" % (os.path.relpath(p, HERE), os.path.relpath(gold_of(d), HERE), os.path.getmtime(p), os.path.getmtime(gold_of(d)))
                    if key not in cache:
                        pairs.append((p, gold_of(d), key))
    pairs = list({x[2]: x for x in pairs}.values())
    print("%d pairs to score" % len(pairs), flush=True)
    with ProcessPoolExecutor(a.jobs) as pool:
        for t, r in zip(pairs, pool.map(one, pairs, chunksize=2)):
            cache[t[2]] = r
    json.dump(cache, open(cache_path, "w"))

    def get(p, g):
        key = "%s|%s|%d|%d" % (os.path.relpath(p, HERE), os.path.relpath(g, HERE), os.path.getmtime(p), os.path.getmtime(g))
        return cache.get(key)
    out = {"checks": checks, "groups": {}}
    for gid, ds, gold_of in groups:
        res = {}
        for cond, r, rd in runs:
            got = [get(os.path.join(rd, d + ".umr"), gold_of(d)) if os.path.exists(os.path.join(rd, d + ".umr")) else None for d in ds]
            if any(x is None or "error" in x for x in got):
                continue
            s = umrjudge.score([u for x in got for u in x["units"]], spec)
            row = {c: (None if s[c]["score"] is None else 100 * s[c]["score"]) for c in checks}
            row.update({c + "_r": (None if s[c]["recall"] is None else 100 * s[c]["recall"]) for c in checks})
            row.update({c + "_p": (None if s[c]["precision"] is None else 100 * s[c]["precision"]) for c in checks})
            if all(x["jumach"] for x in got):
                c_, g_, p_ = (sum(x["jumach"][i] for x in got) for i in range(3))
                row["jumach"] = 200.0 * c_ / (g_ + p_) if g_ + p_ else 0.0
            res.setdefault(cond, {})[r] = row
        table = {}
        for cond, rs in res.items():
            keys = list(next(iter(rs.values())))
            table[cond] = {"n": len(rs), "runs": sorted(rs)}
            for k in set(k for r in rs.values() for k in r):
                xs = [r.get(k) for r in rs.values()]
                xs = [x for x in xs if x is not None]
                if xs:
                    table[cond][k] = {"mean": statistics.mean(xs), "sd": statistics.pstdev(xs) if len(xs) > 1 else 0.0,
                                      "min": min(xs), "max": max(xs), "n": len(xs)}
        out["groups"][gid] = {"docs": ds, "conditions": table, "runs": res}
    json.dump(out, open(os.path.join(HERE, "analysis", "scores.json"), "w"), ensure_ascii=False, indent=1)
    for gid in out["groups"]:
        T = out["groups"][gid]["conditions"]
        print("\n==", gid)
        for cond, row in T.items():
            f = lambda k: "%5.1f±%.1f" % (row[k]["mean"], row[k]["sd"]) if k in row else "   –   "
            print("%-34s n=%-2d ju %s | sense %s | args %s | role %s | temp %s | modal %s | coref %s" % (
                cond, row["n"], f("jumach"), f("b_event_sense"), f("d_core_args_event"), f("e_core_labels"),
                f("h_temporal"), f("i_modal"), f("j_coref_chain")))


if __name__ == "__main__":
    main()
