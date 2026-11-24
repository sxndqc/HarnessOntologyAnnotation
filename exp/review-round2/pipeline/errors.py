"""Where the gold's errors are: counts from the review items (review/items/*.json).

    python3 pipeline/errors.py      -> analysis/gold-errors.md and analysis/gold-errors.json

Counts the fixes (conf high and mid: the ones that go into the corrected gold) by document, by category and by
what the edit does (which role became which, which modal strength became which, ...), and the comparison points
by the status of the gold's choice.
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

CAT = {"sense": "义项", "role": "角色", "concept": "概念/实体类型", "structure": "结构", "attr": "属性（aspect 等）",
       "doc-temporal": "文档级时间", "doc-modal": "文档级模态", "doc-coref": "文档级共指"}


def load():
    folder = os.path.join(C.PKG, "review", "items")
    out = []
    for name in sorted(os.listdir(folder)):
        m = re.match(r"([a-z]+-\d+)\.\d+-\d+\.json$", name)
        if m:
            for x in json.load(open(os.path.join(folder, name), encoding="utf-8")):
                x["doc"] = m.group(1)
                out.append(x)
    return out


def kinds(x):
    """What a fix does, as short labels (one per op, duplicates removed)."""
    out = []
    for o in x["fix"].get("ops", []):
        op = o.get("op")
        if op == "mod_rel":
            out.append("改角色 :%s → :%s" % (o.get("r"), o.get("r2")))
        elif op == "doc_mod":
            a, b = o.get("triple", ["", "", ""]), o.get("to", ["", "", ""])
            if a[1] != b[1]:
                out.append("%s 改关系 :%s → :%s" % (o.get("kind"), a[1], b[1]))
            elif a[0] != b[0]:
                out.append("%s 改父节点（%s）" % (o.get("kind"), "换 conceiver" if o.get("kind") == "modal" else "换参照"))
            else:
                out.append("%s 改子节点" % o.get("kind"))
        elif op == "doc_add":
            out.append("%s 补 :%s" % (o.get("kind"), (o.get("triple") or ["", ""])[1]))
        elif op == "doc_del":
            out.append("%s 删 :%s" % (o.get("kind"), (o.get("triple") or ["", ""])[1]))
        elif op in ("set_attr", "del_attr"):
            out.append("%s :%s" % ("设属性" if op == "set_attr" else "删属性", o.get("attr")))
        elif op == "rename":
            c = str(o.get("concept"))
            out.append("改义项编号" if re.search(r"-\d\d$", c) else "改概念")
        elif op == "add_node":
            out.append("补节点")
        elif op == "del_node":
            out.append("删节点")
        elif op in ("add_rel", "del_rel"):
            out.append("%s :%s" % ("补边" if op == "add_rel" else "删边", re.sub(r"\d", "n", str(o.get("r"))) if str(o.get("r")).startswith("op") else o.get("r")))
        elif op == "set_root":
            out.append("换根节点")
    return list(dict.fromkeys(out))


def main():
    items = load()
    docs = [d["doc"] for d in C.DOCS if any(x["doc"] == d["doc"] for x in items)]
    sents = {d["doc"]: d["sents"] for d in C.DOCS}
    fx = [x for x in items if x.get("fix") and x["fix"].get("conf") != "low"]
    low = [x for x in items if x.get("fix") and x["fix"].get("conf") == "low"]
    L = ["# gold 的错误在哪里（统计）", "",
         "%d 篇文档、%d 句，共 %d 个比较点。判定 gold 应改的 %d 处（high %d，mid %d），另有 %d 处值得商榷（low，不进修订版）。"
         "这些是审阅模型的判断，还没有经过人工确认。" % (
             len(docs), sum(sents[d] for d in docs), len(items), len(fx),
             sum(x["fix"]["conf"] == "high" for x in fx), sum(x["fix"]["conf"] == "mid" for x in fx), len(low)), ""]
    gs = collections.Counter()
    for x in items:
        g = next((c for c in x["choices"] if "gold" in c["systems"]), None)
        gs[(x["cat"], g["status"] if g else "open")] += 1
    L += ["## 按类别", "", "| 类别 | 比较点 | gold 正确 | gold 略差 | gold 错 | 定不了 | 应改（high） | 应改（mid） | 每百句应改 |",
          "|---|---|---|---|---|---|---|---|---|"]
    ns = sum(sents[d] for d in docs)
    stats = {"cats": {}, "docs": {}}
    for c, name in CAT.items():
        n = sum(v for (cc, _), v in gs.items() if cc == c)
        if not n:
            continue
        h = sum(1 for x in fx if x["cat"] == c and x["fix"]["conf"] == "high")
        m = sum(1 for x in fx if x["cat"] == c and x["fix"]["conf"] == "mid")
        L.append("| %s | %d | %d | %d | %d | %d | %d | %d | %.0f |" % (name, n, gs[(c, "ok")], gs[(c, "minor")], gs[(c, "bad")],
                                                                    gs[(c, "open")], h, m, 100 * (h + m) / ns))
        stats["cats"][c] = {"points": n, "ok": gs[(c, "ok")], "minor": gs[(c, "minor")], "bad": gs[(c, "bad")], "high": h, "mid": m}
    L += ["", "## 修改的具体类型（一处修改可以算进几类）", ""]
    for c, name in CAT.items():
        k = collections.Counter(t for x in fx if x["cat"] == c for t in kinds(x))
        if k:
            L.append("- **%s**（%d 处）：%s" % (name, sum(1 for x in fx if x["cat"] == c),
                                             "；".join("%s %d" % (t, n) for t, n in k.most_common(12))))
    lang = {d["doc"]: d.get("lang") for d in C.DOCS}
    L += ["", "## 按语言", "", "| 语言 | 文档 | 句数 | 比较点 | gold 正确 % | 应改（high） | 应改（mid） | 值得商榷 | 每句应改 |", "|---|---|---|---|---|---|---|---|---|"]
    stats["langs"] = {}
    for l in dict.fromkeys(lang[d] for d in docs):
        dl = [d for d in docs if lang[d] == l]
        it = [x for x in items if lang[x["doc"]] == l]
        gk = collections.Counter(next((c["status"] for c in x["choices"] if "gold" in c["systems"]), "open") for x in it)
        den = gk["ok"] + gk["minor"] + gk["bad"]
        h = sum(1 for x in fx if lang[x["doc"]] == l and x["fix"]["conf"] == "high")
        m = sum(1 for x in fx if lang[x["doc"]] == l and x["fix"]["conf"] == "mid")
        lo = sum(1 for x in low if lang[x["doc"]] == l)
        s = sum(sents[d] for d in dl)
        L.append("| %s | %d | %d | %d | %.1f | %d | %d | %d | %.1f |" % (l, len(dl), s, len(it), 100 * gk["ok"] / den if den else 0, h, m, lo, (h + m) / s))
        stats["langs"][l] = {"docs": len(dl), "sents": s, "points": len(it), "gold_ok": gk["ok"], "gold_judged": den, "high": h, "mid": m, "low": lo}
    L += ["", "## 按文档", "", "| 文档 | 句数 | 比较点 | 应改（high） | 应改（mid） | 值得商榷 | 每句应改 |", "|---|---|---|---|---|---|---|"]
    for d in docs:
        h = sum(1 for x in fx if x["doc"] == d and x["fix"]["conf"] == "high")
        m = sum(1 for x in fx if x["doc"] == d and x["fix"]["conf"] == "mid")
        lo = sum(1 for x in low if x["doc"] == d)
        n = sum(1 for x in items if x["doc"] == d)
        L.append("| %s | %d | %d | %d | %d | %d | %.1f |" % (d, sents[d], n, h, m, lo, (h + m) / sents[d]))
        stats["docs"][d] = {"sents": sents[d], "points": n, "high": h, "mid": m, "low": lo}
    os.makedirs(C.ANALYSIS, exist_ok=True)
    with open(os.path.join(C.ANALYSIS, "gold-errors.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(C.ANALYSIS, "gold-errors.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print("\n".join(L))


if __name__ == "__main__":
    main()
