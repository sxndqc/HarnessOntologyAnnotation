"""umrjudge (exp/judges/umrjudge.py, the checks of exp/judges/umrjudge.yaml) on every run of this round, each
setting averaged over its runs.

    python3 pipeline/judge.py [--jobs 6]    -> analysis/judge.json, analysis/judge.md

For a run and a group of documents the units of every document are pooled and each check gets its recall,
precision and F1 (umrjudge.score). The figure of a setting is the mean of that F1 over its runs (r1, r2, and
any further run added to config.json); the table also shows every run, so the spread between runs can be read.
A run that lacks a document of the group is left out of the group.

Groups as in pipeline/breakdown.py: the 30 test files against the shared task's gold (data/gold_st22), all and
by language, and the 31 Chinese documents of the first round against data/gold.

Needs penman, PyYAML and numpy; AnCast (which matches the nodes) is the copy in vendor/umrancast.
"""
import argparse
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

sys.path.insert(0, os.path.join(C.PKG, "vendor", "umrancast"))
sys.path.insert(0, os.path.join(os.path.dirname(C.PKG), "judges"))

NAMES = {
    "a_event_found": "a 事件节点有没有找到", "a_event_concept": "a 事件概念对不对",
    "a_entity_found": "a 实体节点有没有找到", "a_entity_concept": "a 实体概念对不对",
    "b_event_sense": "b 谓词义项号", "c_aspect": "c aspect", "c_polarity": "c :polarity",
    "c_refer": "c 人称/数", "c_other_attributes": "c 其他属性值",
    "d_core_args_event": "d 事件的核心论元", "d_core_args_abstract": "d 抽象事件的核心论元",
    "d_peripheral_event": "d 事件的非核心角色", "d_peripheral_entity": "d 实体的非核心角色",
    "e_core_labels": "e 核心角色标签", "e_peripheral_labels": "e 非核心角色标签",
    "f_name_tokens": "f 名字的词", "h_temporal": "h 文档级时间", "i_modal": "i 文档级模态",
    "j_coref_chain": "j 共指链", "j_coref_subset": "j 共指 subset-of", "k_doc_format": "k 文档级格式"}
KEEP = ("check", "verdict", "credit")


def one(t):
    """The units of one (prediction, gold) pair, cut down to what the score needs."""
    import umrjudge
    spec = umrjudge.load_spec()
    try:
        units = umrjudge.judge_file(t[0], t[1], spec)["units"]
    except Exception as e:      # a file the judge cannot read at all: reported, the run left out of the group
        return "%s: %s" % (type(e).__name__, e)
    return [{k: u[k] for k in KEEP if k in u} for u in units]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    import umrjudge
    spec = umrjudge.load_spec()
    checks = [c["id"] for c in spec["checks"]]
    st = os.path.join(C.PKG, "data", "gold_st22")
    test = [d for d in C.DOCS if d.get("test")]
    zh31 = [d for d in C.DOCS if d["lang"] == "zh" and d["doc"] not in ("zh-0026", "zh-0036")]

    def st_gold(d):
        return os.path.join(st, d["doc"] + ".umr")
    groups = [("test", "测试集 30 篇（对 UMR 2.2 test-gold）", test, st_gold)]
    for l in dict.fromkeys(d["lang"] for d in test):
        ds = [d for d in test if d["lang"] == l]
        groups.append(("test-" + l, "测试集 %s（%d 篇，对 UMR 2.2 test-gold）" % (l, len(ds)), ds, st_gold))
    groups.append(("zh31", "中文 31 篇（对 data/gold）", zh31, C.gold_path))
    pairs = {}
    for _, _, ds, gold_of in groups:
        for d in ds:
            for _, _, _, rd in C.systems():
                pred = os.path.join(rd, d["doc"] + ".umr")
                if os.path.exists(pred):
                    pairs[(pred, gold_of(d))] = None
    keys = list(pairs)
    print("%d pairs" % len(keys), flush=True)
    with ProcessPoolExecutor(a.jobs) as pool:
        for t, units in zip(keys, pool.map(one, keys, chunksize=4)):
            pairs[t] = units
    failed = {t: u for t, u in pairs.items() if isinstance(u, str)}
    for t, u in failed.items():
        print("not judged: %s against %s: %s" % (os.path.relpath(t[0], C.PKG), os.path.relpath(t[1], C.PKG), u))
    out = {"checks": [[c, NAMES.get(c, c)] for c in checks], "groups": [],
           "not_judged": [[os.path.relpath(t[0], C.PKG), u] for t, u in failed.items()]}
    for gid, title, ds, gold_of in groups:
        G = {"id": gid, "title": title, "docs": [d["doc"] for d in ds], "runs": {}, "settings": {}}
        for k, _, _, rd in C.systems():
            ts = [(os.path.join(rd, d["doc"] + ".umr"), gold_of(d)) for d in ds]
            if any(t not in pairs or t in failed for t in ts):
                continue
            s = umrjudge.score([u for t in ts for u in pairs[t]], spec)
            G["runs"][k] = {c: {"f": s[c]["score"], "r": s[c]["recall"], "p": s[c]["precision"], "units": s[c]["units"],
                                "gold": sum(s[c][v] for v in spec["scoring"]["gold_side"])} for c in checks}
        for cond in dict.fromkeys(k.split("/")[0] for k in G["runs"]):
            runs = [k for k in G["runs"] if k.split("/")[0] == cond]
            row = {}
            for c in checks:
                for m in ("f", "r", "p"):
                    xs = [G["runs"][k][c][m] for k in runs]
                    row[c + "_" + m] = None if any(x is None for x in xs) else 100 * sum(xs) / len(xs)
            G["settings"][cond] = {"runs": runs, **row}
        out["groups"].append(G)
    with open(os.path.join(C.ANALYSIS, "judge.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    def n(x):
        return "–" if x is None else "%.1f" % x
    L = ["# umrjudge 分项（各设定，多次运行取平均）", "",
         "由 `python3 pipeline/judge.py` 生成。打分器是 `exp/judges/umrjudge.py`，分项定义在 `exp/judges/umrjudge.yaml`；"
         "节点粒度（a_granularity）、`:wiki`（f_wiki）、重入（g_reentrancy）三项不再判。",
         "每格是该设定各次运行的 F1 的平均，括号里是每次运行各自的 F1（依次为 %s）。一次运行的 F1：把该组文档的判定单元合在一起，"
         "召回 = gold 一侧单元（correct、partial、wrong、missing）的平均得分，精确 = 预测一侧单元（correct、partial、wrong、extra）的平均得分，"
         "F1 是两者的调和平均。“gold 单元”一列是 gold 一侧的单元数（第一个设定第一次运行的）。召回和精确在 judge.json 里。"
         % "、".join(m["key"] for m in C.CONFIG["models"]), ""]
    for G in out["groups"]:
        conds = list(G["settings"])
        if not conds:
            continue
        L += ["## " + G["title"], "", "| 分项 | gold 单元 | " + " | ".join(conds) + " |", "|---|---|" + "---|" * len(conds)]
        first = G["runs"][G["settings"][conds[0]]["runs"][0]]
        for c in checks:
            if all(G["settings"][k][c + "_f"] is None for k in conds):
                continue
            cells = []
            for k in conds:
                S = G["settings"][k]
                each = "/".join(n(None if G["runs"][r][c]["f"] is None else 100 * G["runs"][r][c]["f"]) for r in S["runs"])
                cells.append("%s（%s）" % (n(S[c + "_f"]), each))
            L.append("| %s（%s） | %d | %s |" % (NAMES.get(c, c), c, first[c]["gold"], " | ".join(cells)))
        L.append("")
    with open(os.path.join(C.ANALYSIS, "judge.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:32]))


if __name__ == "__main__":
    main()
