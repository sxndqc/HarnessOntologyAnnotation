"""breakdown.md: every score and every umrjudge check, per sub-experiment and system, side by side.

    python3 exp/scripts/breakdown.py [--docs zh-0028,zh-0032,en-0008]

Columns are runs (runs/<method>/<sub>/<label>/scores.json). Chinese files are pooled (juːmæʧ and Smatch:
counts summed; umrjudge: its units pooled, recall, precision and F1 of each check; AnCast++: mean over the files); a column that lacks one of the files is computed
on the files it has, and its header says which. Δ tables: a sub-experiment minus s1-abridged of the same
system, in points.
"""
import argparse
import json
import os

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(EXP, "runs")
OBSOLETE = os.path.join(os.path.dirname(EXP), "obsolete", "exp", "runs")   # superseded runs (obsolete/README.md)
SUBS = ["s1-abridged", "s1-full", "s2-search", "s2-propbank", "s2-gold"]
API_SUBS = SUBS + ["s3-all", "a1-sentence-propbank", "a2-sentence-all"]
SHORT = {"s3-all": "+all three tools", "a1-sentence-propbank": "+PropBank by sentence",
         "a2-sentence-all": "+all three by sentence", "s1-abridged": "abridged", "s1-full": "full", "s2-search": "+search", "s2-propbank": "+PropBank",
         "s2-gold": "+gold"}
ANCAST = ["Modal", "Temporal", "Coref", "Comprehensive"]
NAMES = {   # umrjudge checks (judges/umrjudge.yaml): what each one judges, in words
    "a_event_found": "a 事件节点有没有找到：gold 的事件/抽象事件节点能否配上（a_event_found）",
    "a_event_concept": "a 事件概念对不对：配上的事件节点，概念是否相同（a_event_concept）",
    "a_entity_found": "a 实体节点有没有找到：实体、命名实体、日期、数量（a_entity_found）",
    "a_entity_concept": "a 实体概念对不对（a_entity_concept）",
    "a_granularity": "a 节点切分粒度：一个节点是否对应和 gold 一样的词（a_granularity）",
    "b_event_sense": "b 谓词义项号：概念相同时 -01/-02 是否相同（b_event_sense）",
    "c_aspect": "c 事件的 aspect 值（c_aspect）",
    "c_modstr": "c 句内 :modal-strength（已移到文档级模态里判，这里为空）（c_modstr）",
    "c_polarity": "c 否定 :polarity（c_polarity）",
    "c_refer": "c 代词的 :refer-person / :refer-number（c_refer）",
    "c_other_attributes": "c 其他属性值（:quant、:mode、:value 等）（c_other_attributes）",
    "d_core_args_event": "d 事件的核心论元：ARG0–9 集合与 gold 的重合比例（d_core_args_event）",
    "d_core_args_abstract": "d 抽象事件（have-…-91、identity-91 等）的核心论元（d_core_args_abstract）",
    "d_peripheral_event": "d 事件的非核心角色集合（:temporal、:manner、:place 等）（d_peripheral_event）",
    "d_peripheral_entity": "d 实体的非核心角色集合（:mod、:quant、:poss 等）（d_peripheral_entity）",
    "e_core_labels": "e 核心角色标签：边存在时 ARGn 是否对（e_core_labels）",
    "e_peripheral_labels": "e 非核心角色标签：边存在时标签是否对（e_peripheral_labels）",
    "f_name_tokens": "f 名字的词：:op1、:op2… 是否和 gold 一样（f_name_tokens）",
    "f_wiki": "f :wiki 链接（f_wiki）",
    "g_reentrancy": "g 重入：同一节点被再次引用的边（g_reentrancy）",
    "h_temporal": "h 文档级时间关系：每个节点的时间父节点和关系（h_temporal）",
    "i_modal": "i 文档级模态关系：每个节点的认知者和模态强度（i_modal）",
    "j_coref_chain": "j 共指链：每个提及是否和 gold 连到同样的其他提及（j_coref_chain）",
    "j_coref_subset": "j 共指 subset-of 关系（j_coref_subset）",
    "k_doc_format": "k 文档级关系格式是否合法（不看 gold）（k_doc_format）"}


def f1(c, g, p):
    return 200.0 * c / (g + p) if g + p else 0.0


def _prf(c, g, p):
    """(F1, recall, precision) in percent from correct, gold and predicted counts."""
    R = 100.0 * c / g if g else None
    P = 100.0 * c / p if p else None
    F = 200.0 * c / (g + p) if g + p else 0.0
    return F, R, P


def metrics(scores, docs):
    """Every row of the tables for the files docs of a run: juːmæʧ and Smatch from the counts summed over
    the files; AnCast++ the mean over the files; each umrjudge check its F1, recall and precision from its
    units pooled over the files (judge_rp)."""
    have = [d for d in docs if d in scores]
    if not have:
        return None, have
    m = {}
    c, g, p = (sum(scores[d]["jumach"][i] for d in have) for i in range(3))   # correct, gold, predicted
    m["juːmæʧ F"], m["juːmæʧ R"], m["juːmæʧ P"] = _prf(c, g, p)
    c, p, g = (sum(scores[d]["smatch"][i] for d in have) for i in range(3))   # matched, predicted, gold
    m["Smatch F"], m["Smatch R"], m["Smatch P"] = _prf(c, g, p)
    for k in ANCAST:
        xs = [scores[d]["ancast"].get(k) for d in have if scores[d].get("ancast")]
        xs = [x for x in xs if x is not None]
        m["AnCast " + k] = sum(xs) / len(xs) if xs else None
    for ck in NAMES:
        t = [scores[d]["judge_rp"][ck] for d in have if ck in scores[d].get("judge_rp", {})]
        gn, gc = sum(x["gn"] for x in t), sum(x["gc"] for x in t)
        pn, pc = sum(x["pn"] for x in t), sum(x["pc"] for x in t)
        R = 100 * gc / gn if gn else None
        P = 100 * pc / pn if pn else None
        m[ck + " R"], m[ck + " P"] = R, P
        m[ck] = None if R is None and P is None else (P if R is None else R if P is None else
                                                      (2 * R * P / (R + P) if R + P else 0.0))
    return m, have


def load(method, sub, label, root=RUNS):
    p = os.path.join(root, method, sub, label, "scores.json")
    return json.load(open(p, encoding="utf-8"))["docs"] if os.path.exists(p) else None


ROWS = (["juːmæʧ F", "juːmæʧ R", "juːmæʧ P", "Smatch F", "Smatch R", "Smatch P"] + ["AnCast " + k for k in ANCAST]
        + [x for c in NAMES for x in (c, c + " R", c + " P")])
LABEL = {"juːmæʧ R": "　└ 召回 R", "juːmæʧ P": "　└ 精确 P", "Smatch R": "　└ 召回 R", "Smatch P": "　└ 精确 P",
         "AnCast Modal": "AnCast++ 文档级模态 F", "AnCast Temporal": "AnCast++ 文档级时间 F",
         "AnCast Coref": "AnCast++ 共指 F", "AnCast Comprehensive": "AnCast++ 综合 F"}
LABEL.update({c: NAMES[c] + " F1" for c in NAMES})
LABEL.update({c + " R": "　└ 召回 R" for c in NAMES})
LABEL.update({c + " P": "　└ 精确 P" for c in NAMES})


def fmt(x):
    return "–" if x is None else "%.1f" % x


def table(cols, docs, delta_of=None, root=RUNS):
    """cols: [(header, method, sub, label)]; delta_of: {header: header of its baseline}."""
    data = {}
    heads = []
    for h, method, sub, label in cols:
        s = load(method, sub, label, root)
        if s is None:
            continue
        m, have = metrics(s, docs)
        if m is None:
            continue
        if len(have) < len(docs):
            h += " (%s)" % ", ".join(have)
        data[h] = m
        heads.append((h, delta_of.get(h) if delta_of else None))
    if not heads:
        return []
    out = ["| | " + " | ".join(h for h, _ in heads) + " |", "|---" * (len(heads) + 1) + "|"]
    for r in ROWS:
        cells = []
        for h, base in heads:
            x = data[h].get(r)
            if base is not None and base in data:
                b = data[base].get(r)
                cells.append("–" if x is None or b is None else "%+.1f" % (x - b))
            else:
                cells.append(fmt(x))
        if all(c == "–" for c in cells):
            continue
        out.append("| %s | %s |" % (LABEL.get(r, r), " | ".join(cells)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="zh-0028,zh-0032,en-0008")
    a = ap.parse_args()
    docs = a.docs.split(",")
    groups = [("zh", [d for d in docs if d.startswith("zh")]), ("en", [d for d in docs if d.startswith("en")])]
    systems = [("Claude API", "api", "claude-opus-5-5-v2"), ("GPT API", "api", "gpt-6.1-sol-medium")]
    lines = ["# Breakdown", "",
             "Generated by `python3 exp/scripts/breakdown.py`. Files: %s. Chinese files pooled (juːmæʧ, Smatch: counts "
             "summed; umrjudge: units pooled; AnCast++: mean over files). Each umrjudge check has three rows: F1, recall "
             "(the gold side: correct, partial, wrong, missing) and precision (the prediction side: correct, partial, wrong, "
             "extra), in percent. Claude API = "
             "claude-opus-5-5, GPT API = gpt-6.1-sol, both effort medium, the same prompts and tools. +PropBank by sentence = the "
             "ablation a1-sentence-propbank (each sentence's graph alone, then each sentence's document-level relations "
             "given it and the five before it). Very few files: differences of a few points are within the noise." % ", ".join(docs), ""]
    for lang, ds in groups:
        if not ds:
            continue
        lines += ["## %s (%s)" % (lang, ", ".join(ds)), ""]
        lines += ["### API: every sub-experiment, Claude and GPT", ""]
        cols = [("%s %s" % (n, SHORT[s]), m, s, l) for n, m, l in systems for s in API_SUBS]
        lines += table(cols, ds) + [""]
        lines += ["### API: each sub-experiment minus abridged (points)", ""]
        cols, delta = [], {}
        for n, m, l in systems:
            cols.append(("%s %s" % (n, SHORT["s1-abridged"]), m, "s1-abridged", l))
            for s in API_SUBS[1:]:
                h = "%s %s" % (n, SHORT[s])
                cols.append((h, m, s, l))
                delta[h] = "%s %s" % (n, SHORT["s1-abridged"])
        lines += table(cols, ds, delta) + [""]
        lines += ["### API: PropBank sentence by sentence (a1) minus PropBank on the whole document (s2-propbank)", ""]
        cols, delta = [], {}
        for n, m, l in systems:
            cols += [("%s whole document" % n, m, "s2-propbank", l), ("%s by sentence" % n, m, "a1-sentence-propbank", l)]
            delta["%s by sentence" % n] = "%s whole document" % n
        lines += table(cols, ds, delta) + [""]
        lines += ["### Archived (obsolete/exp/runs): gpt-6-astra (effort medium), the GPT model used before gpt-6.1-sol", ""]
        lines += table([("gpt-6-astra %s" % SHORT[s], "api", s, "gpt-6-astra-medium") for s in SUBS], ds,
                       root=OBSOLETE) + [""]
        lines += ["### Claude: API, Claude Code, chat (claude.ai); ChatGPT chat as far as there are answers", ""]
        cols = []
        for s in SUBS:
            cols += [("API %s" % SHORT[s], "api", s, "claude-opus-5-5-v2"),
                     ("Claude Code %s" % SHORT[s], "harness", s, "claude-code"),
                     ("claude.ai %s" % SHORT[s], "chat", s, "claude-ai")]
        for label in ("chatgpt-6-astra-high", "chatgpt"):
            cols += [("ChatGPT chat (%s) %s" % (label, SHORT[s]), "chat", s, label) for s in SUBS]
        lines += table(cols, ds) + [""]
    with open(os.path.join(EXP, "breakdown.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
