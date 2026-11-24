"""AnCast++ of every run, the tests between conditions, and analysis/ancast-report.html.

    python3 ancast_stats.py [--jobs 4]   -> analysis/ancast.json, analysis/ancast-report.html

A run's score on a group of documents is the mean over the documents of AnCast's document-scope F scores
(sentence, modal, temporal, coreference, comprehensive), as in round 2 (review-round2/pipeline/ancast_run.py,
the copy of AnCast in review-round2/vendor). juːmæʧ of the run (analysis/scores.json) is carried along.

Tests: the unit is a run. Two conditions are compared by the difference of their means, with Welch's 95%
interval and a two-sided exact permutation test on the runs (every way of splitting the pooled runs into two
groups of the same sizes); the p-values of one table and one metric are also given after Holm's correction.
"""
import argparse
import glob
import html
import itertools
import json
import math
import os
import statistics as st
import sys
from concurrent.futures import ThreadPoolExecutor

from scipy import stats as S

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
sys.path.insert(0, os.path.join(R2, "pipeline"))
import ancast_run as A  # noqa: E402

A.CACHE = os.path.join(HERE, "analysis", ".cache", "ancast")
CONFIG = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
METRICS = [("comp", "AnCast 综合"), ("sent", "句子级"), ("temporal", "文档级时间"), ("modal", "文档级模态"), ("coref", "共指"),
           ("jumach", "juːmæʧ")]
BASE = "s3-full-two-tool"
FIVE = ["s0-oneline", "s1-abridged", "s2-guideline-search", "s2-propbank-search", BASE]
NAME = {"s0-oneline": "s0 一句话", "s1-abridged": "s1 精简版", "s2-guideline-search": "s2 查 guideline",
        "s2-propbank-search": "s2 查 PropBank", BASE: "s3 两个工具（无 skill）"}
NAME.update({"%s+m%d-r%d" % (BASE, m, r): "方法 %d 第 %d 轮" % (m, r) for m in (1, 2, 3) for r in (1, 2)})
E_ = html.escape


def perm_p(a, b):
    """Two-sided exact permutation test of the difference of means (Monte Carlo above 400,000 splits)."""
    pool, n = a + b, len(a)
    obs = abs(st.mean(a) - st.mean(b))
    total = sum(pool)
    if math.comb(len(pool), n) <= 400000:
        hits = cnt = 0
        for idx in itertools.combinations(range(len(pool)), n):
            sa = sum(pool[i] for i in idx)
            d = abs(sa / n - (total - sa) / (len(pool) - n))
            hits += d >= obs - 1e-9
            cnt += 1
        return hits / cnt
    import random
    rnd = random.Random(0)
    hits = 0
    for _ in range(200000):
        rnd.shuffle(pool)
        sa = sum(pool[:n])
        hits += abs(sa / n - (total - sa) / (len(pool) - n)) >= obs - 1e-9
    return (hits + 1) / 200001


def compare(a, b):
    """b minus a: difference, Welch 95% interval, Welch p, permutation p."""
    d = st.mean(b) - st.mean(a)
    va, vb = st.variance(a) / len(a), st.variance(b) / len(b)
    se = math.sqrt(va + vb)
    if se == 0:
        return {"d": d, "lo": d, "hi": d, "p_welch": None, "p_perm": perm_p(a, b)}
    df = (va + vb) ** 2 / ((va ** 2 / (len(a) - 1) if va else 0) + (vb ** 2 / (len(b) - 1) if vb else 0))
    t = S.t.ppf(0.975, df)
    return {"d": d, "lo": d - t * se, "hi": d + t * se, "p_welch": float(S.ttest_ind(b, a, equal_var=False).pvalue),
            "p_perm": perm_p(a, b), "na": len(a), "nb": len(b)}


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    out, run = [None] * len(ps), 0
    for k, i in enumerate(order):
        run = max(run, min(1.0, ps[i] * (len(ps) - k)))
        out[i] = run
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    G = CONFIG["groups"]
    gold = lambda d: os.path.join(HERE, "data", "gold", d + ".umr")
    rev = lambda d: os.path.join(HERE, "review", "data", "gold_revised", d + ".umr")
    groups = [("test", "测试集 4 篇", G["test"], gold), ("test-zh", "测试集中文 2 篇", [d for d in G["test"] if d.startswith("zh")], gold),
              ("test-en", "测试集英语 2 篇", [d for d in G["test"] if d.startswith("en")], gold),
              ("train-rev", "训练集 4 篇，对修订版 gold", G["train"], rev), ("train", "训练集 4 篇，对原 gold", G["train"], gold)]
    runs = [(c, r) for c in sorted(os.listdir(os.path.join(HERE, "runs"))) for r in sorted(os.listdir(os.path.join(HERE, "runs", c)))]
    tasks = {}
    for _, _, ds, gold_of in groups:
        for d in ds:
            for c, r in runs:
                p = os.path.join(HERE, "runs", c, r, d + ".umr")
                if os.path.exists(p):
                    tasks[(p, gold_of(d))] = None
    keys = list(tasks)
    print(len(keys), "pairs", flush=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        for k, res in zip(keys, pool.map(lambda t: A.pair(*t), keys)):
            tasks[k] = res
    errors = [os.path.relpath(k[0], HERE) for k, v in tasks.items() if v.get("error")]
    JU = json.load(open(os.path.join(HERE, "analysis", "scores.json"), encoding="utf-8"))["groups"]
    data = {}                      # group -> condition -> metric -> [value per run]
    for gid, _, ds, gold_of in groups:
        data[gid] = {}
        for c, r in runs:
            got = [tasks.get((os.path.join(HERE, "runs", c, r, d + ".umr"), gold_of(d))) for d in ds]
            if any(x is None or x.get("error") for x in got):
                continue
            row = {}
            for m, _ in METRICS[:-1]:
                xs = [x["doc"].get(m) for x in got]
                row[m] = st.mean([x if x is not None else 0.0 for x in xs])
            ju = JU.get(gid, {}).get("runs", {}).get(c, {}).get(r, {}).get("jumach")
            if ju is not None:
                row["jumach"] = ju
            for m, v in row.items():
                data[gid].setdefault(c, {}).setdefault(m, []).append(v)
    out = {"errors": errors, "data": data, "tests": {}}

    def tests(gid, pairs):
        res = {}
        for m, _ in METRICS:
            rows = []
            for x, y in pairs:
                if x in data[gid] and y in data[gid] and m in data[gid][x] and m in data[gid][y]:
                    rows.append((x, y, compare(data[gid][x][m], data[gid][y][m])))
            for (x, y, t), h in zip(rows, holm([t["p_perm"] for _, _, t in rows])):
                t["p_holm"] = h
                res["%s|%s|%s" % (m, x, y)] = t
        return res
    five_pairs = [("s0-oneline", c) for c in FIVE[1:]] + [("s1-abridged", BASE), ("s2-guideline-search", BASE), ("s2-propbank-search", BASE)]
    skill_pairs = []
    for mth in (1, 2, 3):
        r1, r2 = "%s+m%d-r1" % (BASE, mth), "%s+m%d-r2" % (BASE, mth)
        skill_pairs += [(BASE, r1), (BASE, r2), (r1, r2)]
    for gid, _, _, _ in groups:
        out["tests"][gid] = {"five": tests(gid, five_pairs) if gid.startswith("test") else {}, "skill": tests(gid, skill_pairs)}
    json.dump(out, open(os.path.join(HERE, "analysis", "ancast.json"), "w"), ensure_ascii=False, indent=1)

    # ------------------------------------------------------------ the page
    def ms(gid, c, m):
        xs = data[gid].get(c, {}).get(m)
        return "<td class=n>–</td>" if not xs else "<td class=n title='n=%d，各次：%s'>%.1f<small> ±%.1f</small></td>" % (
            len(xs), "、".join("%.1f" % x for x in xs), st.mean(xs), st.stdev(xs) if len(xs) > 1 else 0)

    def score_table(gid, conds):
        conds = [c for c in conds if c in data[gid]]
        h = "<table><tr><th>设定</th><th>运行数</th>" + "".join("<th>%s</th>" % n for _, n in METRICS) + "</tr>"
        for c in conds:
            h += "<tr><td>%s</td><td class=n>%d</td>" % (NAME[c], len(data[gid][c]["comp"])) + "".join(ms(gid, c, m) for m, _ in METRICS) + "</tr>"
        return h + "</table>"

    def pcell(t):
        if t is None:
            return "<td class=n>–</td>"
        sig = t["p_holm"] < 0.05
        weak = (not sig) and t["p_perm"] < 0.05
        cls = ("up" if t["d"] > 0 else "down") if sig else "weak" if weak else "flat"
        mark = "**" if sig else "*" if weak else ""
        return "<td class='n %s' title='95%% 区间 %+.1f 到 %+.1f；置换检验 p=%.4f；Holm 校正后 p=%.4f；n=%d 对 %d'>%+.1f%s<small> p=%s</small></td>" % (
            cls, t["lo"], t["hi"], t["p_perm"], t["p_holm"], t.get("na", 0), t.get("nb", 0), t["d"], mark,
            "&lt;0.001" if t["p_perm"] < 0.001 else "%.3f" % t["p_perm"])

    def test_table(gid, kind, pairs):
        T = out["tests"][gid][kind]
        h = "<table><tr><th>比较（后者减前者）</th>" + "".join("<th>%s</th>" % n for _, n in METRICS) + "</tr>"
        for x, y in pairs:
            if not any("%s|%s|%s" % (m, x, y) in T for m, _ in METRICS):
                continue
            h += "<tr><td>%s → %s</td>" % (NAME[x], NAME[y]) + "".join(pcell(T.get("%s|%s|%s" % (m, x, y))) for m, _ in METRICS) + "</tr>"
        return h + "</table>"

    def evolution(gid):
        sk = {}
        for p in glob.glob(os.path.join(HERE, "skills", "m*-r*.meta.json")):
            j = json.load(open(p))
            sk[(j["method"], j["round"])] = j
        h = "<table><tr><th>方法</th><th>阶段</th><th>skill 长度</th>" + "".join("<th>%s</th>" % n for _, n in METRICS) + "</tr>"
        for mth in (1, 2, 3):
            for k, c in enumerate([BASE, "%s+m%d-r1" % (BASE, mth), "%s+m%d-r2" % (BASE, mth)]):
                if c not in data[gid]:
                    continue
                stage = ["无 skill", "第 1 轮反思后", "第 2 轮反思后"][k]
                ln = "–" if k == 0 else "%d 条 / %d 字符" % (sk[(mth, k)]["bullets"], sk[(mth, k)]["chars"])
                h += "<tr%s><td>%s</td><td>%s</td><td class=n>%s</td>" % (" class=top" if k == 0 else "", "方法 %d" % mth if k == 0 else "", stage, ln)
                h += "".join(ms(gid, c, m) for m, _ in METRICS) + "</tr>"
        return h + "</table>"
    notes = json.load(open(os.path.join(HERE, "analysis", "ancast_notes.json"), encoding="utf-8")) if os.path.exists(
        os.path.join(HERE, "analysis", "ancast_notes.json")) else {}
    page = open(os.path.join(HERE, "ancast_template.html"), encoding="utf-8").read()
    fill = {"SUMMARY": notes.get("summary", ""), "METHOD": notes.get("method", ""), "CAVEATS": notes.get("caveats", ""),
            "ERRORS": "没有打不了分的文件。" if not errors else "AnCast 打不了分的文件 %d 个（所在的运行不计入该组）：%s" % (len(errors), "、".join(errors[:12]))}
    order = FIVE + ["%s+m%d-r%d" % (BASE, m, r) for m in (1, 2, 3) for r in (1, 2)]
    for gid, _, _, _ in groups:
        key = gid.upper().replace("-", "_")
        fill["ALL_" + key] = score_table(gid, order)
        fill["EVO_" + key] = evolution(gid)
        fill["TS_" + key] = test_table(gid, "skill", skill_pairs)
        fill["TF_" + key] = test_table(gid, "five", five_pairs) if gid.startswith("test") else ""
    for k, v in fill.items():
        page = page.replace("{{%s}}" % k, v)
    open(os.path.join(HERE, "analysis", "ancast-report.html"), "w", encoding="utf-8").write(page)
    print("errors:", len(errors))
    for gid in ("test", "train-rev"):
        print("==", gid)
        for c in order:
            if c in data[gid]:
                print("%-28s n=%-2d " % (c[-28:], len(data[gid][c]["comp"])) + "  ".join("%s %.1f±%.1f" % (m, st.mean(data[gid][c][m]), st.stdev(data[gid][c][m])) for m, _ in METRICS if m in data[gid][c]))
    for gid in ("test", "train-rev"):
        print("== tests", gid)
        for k, t in out["tests"][gid]["skill"].items():
            if k.startswith(("comp|", "temporal|")):
                print("  %-70s %+.1f [%+.1f, %+.1f] p=%.4f holm=%.4f" % (k.replace(BASE, "s3")[:70], t["d"], t["lo"], t["hi"], t["p_perm"], t["p_holm"]))
        for k, t in out["tests"][gid]["five"].items():
            if k.startswith("comp|"):
                print("  %-70s %+.1f [%+.1f, %+.1f] p=%.4f holm=%.4f" % (k.replace(BASE, "s3")[:70], t["d"], t["lo"], t["hi"], t["p_perm"], t["p_holm"]))


if __name__ == "__main__":
    main()
