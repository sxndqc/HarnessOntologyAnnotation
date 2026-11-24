"""F1 of every system against the gold, broken down by what is compared.

    python3 pipeline/breakdown.py [--jobs 6]    -> analysis/breakdown.json, analysis/breakdown.md

Nodes of the gold and of a system are matched by the token they are aligned to (as pipeline/mechdiff.py names
them: the aligned token, the name of a named entity, or, for a node without a token, its concept and where it
hangs). A row is the F1 of one kind of fact, with the counts (correct, gold, predicted) summed over the
documents of a group:

    sense        the concept with its sense number, of the nodes that have one (not the -91/-92 concepts)
    ev_concept   the concept without the sense number, of event nodes (:aspect or a sense number)
    en_concept   the concept of the other nodes (the name nodes left out)
    arg          parent-child pairs joined by :ARGn, parent an ordinary predicate (the label not compared)
    arg_abs      the same, parent a -91/-92 concept
    core_label   (parent, :ARGn, child)
    other_label  (parent, role, child) for every other relation between nodes
    aspect       (node, :aspect, value)
    refer        (node, :refer-person / :refer-number, value)
    name         the names (the :op strings joined), per sentence
    reentrancy   the edges into a node that has more than one parent
    temporal, modal   the document-level triples
    coref        pairs of nodes in the same coreference chain (the chains closed over :same-entity, :same-event)

Smatch is the mean over sentences of the AnCast run (analysis/scores.json); juːmæʧ is compare_umr.pl.
Two groups: the 31 Chinese documents of the first round against data/gold, and the 30 test files against the
shared task's gold (data/gold_st22), by language.
"""
import argparse
import collections
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import jumach as J  # noqa: E402
import mechdiff as M  # noqa: E402
import umrdoc  # noqa: E402

ROWS = [("smatch", "Smatch"), ("jumach", "juːmæʧ"), ("sense", "b 谓词义项号"), ("ev_concept", "a 事件概念"),
        ("en_concept", "a 实体概念"), ("arg", "d 事件核心论元"), ("arg_abs", "d 抽象事件核心论元"),
        ("core_label", "e 核心角色标签"), ("other_label", "e 非核心角色标签"), ("aspect", "c aspect"),
        ("refer", "c 人称/数（代词）"), ("name", "f 名字的词"), ("reentrancy", "g 重入"), ("temporal", "h 文档级时间"),
        ("modal", "i 文档级模态"), ("coref", "j 共指链")]
SENSE = re.compile(r"-\d{2,3}$")
ABS = re.compile(r"-9\d$")


def facts(path):
    """kind -> set of facts of a file (every fact carries its sentence number)."""
    out = collections.defaultdict(set)
    doc = umrdoc.load(path)
    varmap, sents = {}, {}
    for s in doc["sents"]:
        g = s["gold"]
        S = M.Sent(s["index"], g[umrdoc.SECTIONS[0]], g[umrdoc.SECTIONS[1]], s["words"])
        S.raw = g
        sents[s["index"]] = S
        if not S.ok:
            continue
        for v, a in S.anchor.items():
            varmap[v] = "s%d:%s" % (s["index"], a)
    for i, S in sents.items():
        if S.ok:
            A, con = S.anchor, S.concept
            attrs = collections.defaultdict(dict)
            node_edges = []
            for a, r, b in S.edges:
                if b in con:
                    node_edges.append((a, r, b))
                else:
                    attrs[a][r] = str(b)
            namenodes = {b for a, r, b in node_edges if r == ":name"}
            names = {}
            for a, r, b in node_edges:
                if r == ":name":
                    names[a] = "".join(v.strip('"') for k, v in sorted(attrs[b].items()) if k.startswith(":op"))
            for v, c in con.items():
                if v in namenodes or c is None:
                    continue
                event = ":aspect" in attrs[v] or bool(SENSE.search(c))
                if SENSE.search(c) and not ABS.search(c):
                    out["sense"].add((i, A[v], c))
                out["ev_concept" if event else "en_concept"].add((i, A[v], SENSE.sub("", c)))
                if ":aspect" in attrs[v]:
                    out["aspect"].add((i, A[v], attrs[v][":aspect"]))
                for k in (":refer-person", ":refer-number"):
                    if k in attrs[v]:
                        out["refer"].add((i, A[v], k, attrs[v][k]))
            for v, n in names.items():
                out["name"].add((i, n))
            indeg = collections.Counter(b for a, r, b in node_edges if r != ":name")
            for a, r, b in node_edges:
                if r == ":name" or a in namenodes:
                    continue
                if indeg[b] > 1:
                    out["reentrancy"].add((i, A[a], A[b]))
                if r.endswith("-of") and r != ":consist-of":
                    a, r, b = b, r[:-3], a
                if re.match(r":ARG\d", r):
                    out["arg_abs" if ABS.search(con.get(a) or "") else "arg"].add((i, A[a], A[b]))
                    out["core_label"].add((i, A[a], r, A[b]))
                else:
                    out["other_label"].add((i, A[a], r, A[b]))
        text = S.raw[umrdoc.SECTIONS[2]]

        def nm(x):
            return x if x in M.SPECIAL else varmap.get(x, "?" + x)
        for kind in ("temporal", "modal", "coref"):
            m = re.search(r":%s\s*\((.*?)\)\s*(?=:temporal|:modal|:coref|\)\s*$|$)" % kind, text, re.S)
            for a, r, b in re.findall(r"\(\s*(\S+)\s+(:\S+)\s+([^\s()]+)\s*\)", m.group(1) + ")") if m else []:
                out["_coref" if kind == "coref" else kind].add((nm(a), r, nm(b)))
    # coreference chains -> pairs
    par = {}

    def find(x):
        while par.setdefault(x, x) != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for a, r, b in out.pop("_coref", set()):
        if r in (":same-entity", ":same-event"):
            par[find(a)] = find(b)
    groups = collections.defaultdict(list)
    for x in list(par):
        groups[find(x)].append(x)
    for g in groups.values():
        g.sort()
        for k, a in enumerate(g):
            for b in g[k + 1:]:
                out["coref"].add((a, b))
    return out


def count(pred, gold):
    P, G = facts(pred), facts(gold)
    return {k: (len(P[k] & G[k]), len(G[k]), len(P[k])) for k, _ in ROWS if k not in ("smatch", "jumach")}


def f1(c, g, p):
    pr, rc = (c / p if p else 0), (c / g if g else 0)
    return 100 * 2 * pr * rc / (pr + rc) if pr + rc else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    st = os.path.join(C.PKG, "data", "gold_st22")
    zh31 = [d for d in C.DOCS if d["lang"] == "zh" and d["doc"] not in ("zh-0026", "zh-0036")]
    test = [d for d in C.DOCS if d.get("test")]
    if os.path.isdir(st):               # the second round: the Chinese documents of the first round, and the test set
        groups = [("zh31", "中文 31 篇（对 data/gold）", zh31, lambda d: C.gold_path(d), "orig")]
        groups.append(("test", "测试集 30 篇（对 UMR 2.2 test-gold）", test, lambda d: os.path.join(st, d["doc"] + ".umr"), None))
        for l in dict.fromkeys(d["lang"] for d in test):
            ds = [d for d in test if d["lang"] == l]
            groups.append(("test-" + l, "测试集 %s（%d 篇，对 UMR 2.2 test-gold）" % (l, len(ds)), ds,
                           lambda d: os.path.join(st, d["doc"] + ".umr"), None))
    else:                               # any other workspace: every document against data/gold, then by language
        groups = [("all", "全部 %d 篇（对 data/gold）" % len(C.DOCS), list(C.DOCS), lambda d: C.gold_path(d), "orig")]
        langs = list(dict.fromkeys(d["lang"] for d in C.DOCS))
        for l in langs if len(langs) > 1 else []:
            ds = [d for d in C.DOCS if d["lang"] == l]
            groups.append(("all-" + l, "%s（%d 篇，对 data/gold）" % (l, len(ds)), ds, lambda d: C.gold_path(d), "orig"))
    scores = json.load(open(os.path.join(C.ANALYSIS, "scores.json"), encoding="utf-8"))
    tasks = {}
    for _, _, ds, gold_of, _ in groups:
        for d in ds:
            for k, _, _, rd in C.systems():
                pred = os.path.join(rd, d["doc"] + ".umr")
                if os.path.exists(pred):
                    tasks[(pred, gold_of(d))] = None
    keys = list(tasks)
    print("%d pairs" % len(keys), flush=True)
    with ThreadPoolExecutor(a.jobs) as pool:
        ju = list(pool.map(lambda t: J.one(*t), keys))
    for t, j in zip(keys, ju):
        r = count(*t)
        r["jumach"] = j or (0, 0, 0)
        tasks[t] = r
    out = {"rows": ROWS, "groups": []}
    for gid, title, ds, gold_of, ver in groups:
        G = {"id": gid, "title": title, "docs": [d["doc"] for d in ds], "systems": {}}
        for k, _, _, rd in C.systems():
            have = [d for d in ds if (os.path.join(rd, d["doc"] + ".umr"), gold_of(d)) in tasks]
            if len(have) < len(ds):
                continue
            row = {}
            for key, _ in ROWS:
                if key == "smatch":
                    sm = []
                    for d in have:
                        for v in scores.get(d["doc"], {}).get("sent", {}).values():
                            x = v.get(k, {})
                            x = x.get("orig") if ver else (x.get("off") or x.get("orig"))   # test files: the released gold
                            if x and x.get("smatch") is not None:
                                sm.append(x["smatch"])
                    row[key] = round(sum(sm) / len(sm), 1) if sm else None
                    continue
                c = [sum(x) for x in zip(*[tasks[(os.path.join(rd, d["doc"] + ".umr"), gold_of(d))][key] for d in have])]
                row[key] = round(f1(*c), 1)
                row[key + "_n"] = c[1]
            G["systems"][k] = row
        out["groups"].append(G)
    with open(os.path.join(C.ANALYSIS, "breakdown.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    L = ["# 分项 F1（各设定）", "",
         "节点按对齐的词来对应（和 mechdiff 的命名相同），每一行是一类事实的 F1，计数在该组文档上加总。各行的定义见 pipeline/breakdown.py 开头。"
         "Smatch 是 AnCast 那次运行里逐句 Smatch 的平均；juːmæʧ 用 compare_umr.pl。括号里是 gold 里这类事实的个数。", ""]
    for G in out["groups"]:
        ks = list(G["systems"])
        L += ["## " + G["title"], "", "| 分项 | " + " | ".join(ks) + " |", "|---|" + "---|" * len(ks)]
        for key, name in ROWS:
            n = G["systems"][ks[0]].get(key + "_n")
            L.append("| %s%s | %s |" % (name, "（%d）" % n if n is not None else "", " | ".join(str(G["systems"][k][key]) for k in ks)))
        L.append("")
    with open(os.path.join(C.ANALYSIS, "breakdown.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:44]))


if __name__ == "__main__":
    main()
