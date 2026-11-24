"""analysis/report.html: the report of round 3 (one self-contained page, Chinese).

    python3 build_report.py      (after score.py)

Numbers come from analysis/scores.json, the runs' meta files, skills/*.meta.json, analysis/chunking.json and the
review workspace; the prose that needs judgement is in analysis/report_notes.json (written by hand).
"""
import glob
import html
import json
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
J = lambda *p: json.load(open(os.path.join(HERE, *p), encoding="utf-8"))
CONFIG = J("config.json")
S = J("analysis", "scores.json")
NOTES = J("analysis", "report_notes.json") if os.path.exists(os.path.join(HERE, "analysis", "report_notes.json")) else {}
E_ = html.escape
ROWS = [("jumach", "juːmæʧ"), ("a_event_concept", "事件概念"), ("a_entity_concept", "实体概念"), ("b_event_sense", "谓词义项号"),
        ("c_aspect", "aspect"), ("c_polarity", ":polarity"), ("c_refer", "人称/数"), ("d_core_args_event", "事件的核心论元"),
        ("d_core_args_abstract", "抽象事件的核心论元"), ("d_peripheral_event", "事件的非核心角色"),
        ("d_peripheral_entity", "实体的非核心角色"), ("e_core_labels", "核心角色标签"), ("e_peripheral_labels", "非核心角色标签"),
        ("f_name_tokens", "名字的词"), ("h_temporal", "文档级时间"), ("i_modal", "文档级模态"), ("j_coref_chain", "共指链"),
        ("k_doc_format", "文档级格式")]
BASE5 = ["s0-oneline", "s1-abridged", "s2-guideline-search", "s2-propbank-search", "s3-full-two-tool"]
SHORT = {"s0-oneline": "s0 一句话", "s1-abridged": "s1 精简版", "s2-guideline-search": "s2 查 guideline",
         "s2-propbank-search": "s2 查 PropBank", "s3-full-two-tool": "s3 两个工具"}


def metas(cond, docs):
    out = []
    for p in glob.glob(os.path.join(HERE, "runs", cond, "p*r*", "*.meta.json")):
        m = json.load(open(p, encoding="utf-8"))
        if m["doc"] in docs:
            out.append(m)
    return out


def cell(row, key, ref=None):
    if not row or key not in row:
        return "<td class=n>–</td>"
    v = row[key]
    d = ""
    if ref and key in ref:
        diff = v["mean"] - ref[key]["mean"]
        cls = "up" if diff > 1.0 else "down" if diff < -1.0 else "flat"
        d = " <span class=%s>%+.1f</span>" % (cls, diff)
    return "<td class=n title='n=%d，最小 %.1f，最大 %.1f'>%.1f<small> ±%.1f</small>%s</td>" % (v["n"], v["min"], v["max"], v["mean"], v["sd"], d)


def table(group, conds, ref=None, names=None):
    T = S["groups"].get(group, {}).get("conditions", {})
    conds = [c for c in conds if c in T]
    if not conds:
        return "<p class=note>（还没有结果）</p>"
    h = "<table><tr><th>分项</th>" + "".join("<th>%s<br><small>n=%d</small></th>" % (E_((names or SHORT).get(c, c)), T[c]["n"]) for c in conds) + "</tr>"
    for key, name in ROWS:
        if not any(key in T[c] for c in conds):
            continue
        h += "<tr><td>%s</td>" % name + "".join(cell(T[c], key, T.get(ref) if ref and c != ref else None) for c in conds) + "</tr>"
    return h + "</table>"


def usage_table(conds, docs, names=None):
    h = "<table><tr><th>设定</th><th>运行数</th><th>每次查询次数（平均）</th><th>其中查 guideline</th><th>其中查 PropBank</th><th>零查询的运行</th><th>输出 token（平均）</th><th>耗时（分，平均）</th><th>重试过的运行</th></tr>"
    for c in conds:
        ms = metas(c, docs)
        if not ms:
            continue
        g = lambda f: statistics.mean(f(m) for m in ms)
        h += "<tr><td>%s</td><td class=n>%d</td><td class=n>%.1f</td><td class=n>%.1f</td><td class=n>%.1f</td><td class=n>%d</td><td class=n>%.0f</td><td class=n>%.1f</td><td class=n>%d</td></tr>" % (
            E_((names or SHORT).get(c, c)), len(ms), g(lambda m: m["lookups"]), g(lambda m: m["lookups_by_tool"].get("search_guidelines", 0)),
            g(lambda m: m["lookups_by_tool"].get("propbank_lookup", 0)), sum(1 for m in ms if m["lookups"] == 0 and m["lookups_by_tool"]),
            g(lambda m: m["usage"]["output_tokens"] or 0), g(lambda m: m["seconds"] / 60), sum(1 for m in ms if m["attempts"] > 1))
    return h + "</table>"


def wording_table(group, conds):
    """juːmæʧ by wording: is the spread between wordings larger than between the two repetitions?"""
    R = S["groups"].get(group, {}).get("runs", {})
    h = "<table><tr><th>设定</th>" + "".join("<th>措辞 %d</th>" % v for v in range(1, 6)) + "<th>措辞之间的标准差</th><th>同一措辞两次之差（平均）</th></tr>"
    for c in conds:
        if c not in R:
            continue
        by = {}
        for r, row in R[c].items():
            if "jumach" in row:
                by.setdefault(int(r[1]), []).append(row["jumach"])
        if len(by) < 2:
            continue
        means = [statistics.mean(by[v]) for v in sorted(by)]
        gaps = [abs(x[0] - x[1]) for x in by.values() if len(x) == 2]
        h += "<tr><td>%s</td>" % SHORT.get(c, c) + "".join("<td class=n>%s</td>" % ("%.1f" % statistics.mean(by[v]) if v in by else "–") for v in range(1, 6))
        h += "<td class=n>%.2f</td><td class=n>%s</td></tr>" % (statistics.pstdev(means), "%.2f" % statistics.mean(gaps) if gaps else "–")
    return h + "</table>"


def skills_block():
    out = ""
    for p in sorted(glob.glob(os.path.join(HERE, "skills", "m*-r*.meta.json"))):
        m = json.load(open(p))
        text = open(p.replace(".meta.json", ".md"), encoding="utf-8").read()
        out += "<details><summary>方法 %d，第 %d 轮：%d 条，%d 字符</summary><pre>%s</pre></details>" % (
            m["method"], m["round"], m["bullets"], m["chars"], E_(text))
    return out or "<p class=note>（还没有 skill）</p>"


def skills_table():
    rows = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(HERE, "skills", "m*-r*.meta.json")))]
    if not rows:
        return ""
    h = "<table><tr><th>skill</th><th>条数</th><th>字符数</th><th>反思输入（字符）</th></tr>"
    for m in rows:
        h += "<tr><td>方法 %d 第 %d 轮</td><td class=n>%d</td><td class=n>%d</td><td class=n>%d</td></tr>" % (m["method"], m["round"], m["bullets"], m["chars"], m["prompt_chars"])
    return h + "</table>"


def main():
    test, train = CONFIG["groups"]["test"], CONFIG["groups"]["train"]
    skill_conds = ["s3-full-two-tool"] + ["s3-full-two-tool+m%d-r%d" % (m, r) for m in (1, 2, 3) for r in (1, 2)]
    skill_names = {"s3-full-two-tool": "s3（无 skill）", **{"s3-full-two-tool+m%d-r%d" % (m, r): "方法 %d 第 %d 轮" % (m, r) for m in (1, 2, 3) for r in (1, 2)}}
    ch = J("analysis", "chunking.json")
    N = lambda k: NOTES.get(k, "")
    page = open(os.path.join(HERE, "report_template.html"), encoding="utf-8").read()
    fill = {
        "SUMMARY": N("summary"), "GUIDELINE": N("guideline"), "CHUNK_OLD": json.dumps(ch["old"]), "CHUNK_NEW": json.dumps(ch["new"]),
        "CHUNK_TABLE": "<table><tr><th></th><th>修订前</th><th>修订后</th></tr>" + "".join(
            "<tr><td>%s</td><td class=n>%s</td><td class=n>%s</td></tr>" % (n, ch["old"][k], ch["new"][k]) for k, n in [
                ("chunks", "段落数"), ("max", "最长的段（字符）"), ("median", "中位长度（字符）"), ("over8000", "超过 8,000 字符的段"),
                ("html_chunks", "含 HTML 标签的段"), ("unbalanced_fence", "把一个示例切成两半的段")]) + "</table>",
        "SETUP": N("setup"), "T_TEST": table("test", BASE5, ref="s0-oneline"), "T_TEST_ZH": table("test-zh", BASE5, ref="s0-oneline"),
        "T_TEST_EN": table("test-en", BASE5, ref="s0-oneline"), "USAGE": usage_table(BASE5, test), "WORDING": wording_table("test", BASE5),
        "RESULTS_NOTE": N("results"), "REVIEW": N("review"), "SKILL_NOTE": N("skills"), "SKILL_TABLE": skills_table(),
        "T_SK_TRAIN": table("train", skill_conds, ref="s3-full-two-tool", names=skill_names),
        "T_SK_TRAINREV": table("train-rev", skill_conds, ref="s3-full-two-tool", names=skill_names),
        "T_SK_TEST": table("test", skill_conds, ref="s3-full-two-tool", names=skill_names),
        "T_SK_TEST_ZH": table("test-zh", skill_conds, ref="s3-full-two-tool", names=skill_names),
        "T_SK_TEST_EN": table("test-en", skill_conds, ref="s3-full-two-tool", names=skill_names),
        "USAGE_SK": usage_table(skill_conds, test + train, names=skill_names),
        "SKILLS": skills_block(), "CAVEATS": N("caveats"), "FILES": N("files"),
    }
    for k, v in fill.items():
        page = page.replace("{{%s}}" % k, v)
    open(os.path.join(HERE, "analysis", "report.html"), "w", encoding="utf-8").write(page)
    print("wrote analysis/report.html", len(page))


if __name__ == "__main__":
    main()
