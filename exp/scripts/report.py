"""report.html: every result of the experiments so far in one page, computed from runs/*/scores.json and
the traces (so the numbers are those of the repository).

    python3 exp/scripts/report.py            # -> exp/report.html

The old-prompt API runs (label claude-opus-5-5) were scored with the model's own alignment; for the
comparison of prompts they are scored again here with the alignment removed and computed by autoalign,
as every later run is (in a scratch directory under .cache/, not in runs/).
"""
import html
import json
import os
import re
import sys

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(EXP, "lib"))
sys.path.insert(0, EXP)
sys.path.insert(0, os.path.join(EXP, "scripts"))
import breakdown as B  # noqa: E402
import charts as C  # noqa: E402
import cost as K  # noqa: E402

RUNS = os.path.join(EXP, "runs")
ZH, EN = ["zh-0028", "zh-0032"], ["en-0008"]
DOCS = ZH + EN
SUBS = B.SUBS
NAME = {"s1-abridged": "s1-abridged：缩略版 guideline", "s1-full": "s1-full：完整 guideline",
        "s2-search": "s2-search：缩略版 + guideline 搜索", "s2-propbank": "s2-propbank：缩略版 + PropBank",
        "s2-gold": "s2-gold：缩略版 + gold 例子", "s3-all": "s3-all：缩略版 + 三个工具",
        "a1-sentence-propbank": "a1：PropBank，一句句跑", "a2-sentence-all": "a2：三个工具，一句句跑"}
HEATNAME = {"juːmæʧ F": "juːmæʧ", "Smatch F": "Smatch", "b_event_sense": "b 谓词义项号",
            "a_event_concept": "a 事件概念", "a_entity_concept": "a 实体概念", "d_core_args_event": "d 事件核心论元",
            "d_core_args_abstract": "d 抽象事件核心论元", "e_core_labels": "e 核心角色标签",
            "e_peripheral_labels": "e 非核心角色标签", "c_aspect": "c aspect", "c_refer": "c 人称/数（代词）",
            "f_name_tokens": "f 名字的词", "g_reentrancy": "g 重入", "h_temporal": "h 文档级时间",
            "i_modal": "i 文档级模态", "j_coref_chain": "j 共指链"}
HEATCOL = {"s1-full": "full", "s2-search": "+search", "s2-propbank": "+PropBank", "s2-gold": "+gold",
           "s3-all": "+三个工具", "a1-sentence-propbank": "a1", "a2-sentence-all": "a2"}
SHORTNAME = {"s1-abridged": "abridged", "s1-full": "full", "s2-search": "+search", "s2-propbank": "+PropBank",
             "s2-gold": "+gold", "s3-all": "+三个工具", "a1-sentence-propbank": "a1 一句句·PropBank",
             "a2-sentence-all": "a2 一句句·三个工具"}
CLAUDE, SOL = "claude-opus-5-5-v2", "gpt-6.1-sol-medium"


def e(x):
    return html.escape(str(x))


def fmt(x, signed=False):
    if x is None:
        return "–"
    return ("%+.1f" % x) if signed else ("%.1f" % x)


OBS = B.OBSOLETE    # ../obsolete/exp/runs: the old-prompt Claude runs and gpt-6-astra


def m(method, sub, label, docs, root=RUNS):
    s = B.load(method, sub, label, root)
    if s is None:
        return None
    r, have = B.metrics(s, docs)
    return r if r is not None and len(have) == len(docs) else None


class H(str):
    """A table cell that is HTML already (links): not escaped."""


GH = "https://github.com/sxndqc/HarnessOntologyAnnotation/%s/claude/happy-mccarthy-ml6ttj/"


def link(path, text):
    """A link to a file (or, ending in /, a folder) of the repository on GitHub; path from the repo root."""
    kind = "tree" if path.endswith("/") else "blob"
    return '<a href="%s%s">%s</a>' % (GH % kind, html.escape(path.rstrip("/"), quote=True), e(text))


def table(head, rows, best=None, note=None, title="表格", open_=False):
    """rows: [[cell, ...]]; best: indices of columns among which the highest number of a row is bold.
    Folded under a <details> (title is its summary)."""
    esc = lambda c: c if isinstance(c, H) else e(c)
    out = ["<details%s><summary>%s</summary>" % (" open" if open_ else "", e(title)),
           "<table>", "<thead><tr>" + "".join("<th>%s</th>" % e(h) for h in head) + "</tr></thead><tbody>"]
    for r in rows:
        cells = list(r)
        num = lambda c: not isinstance(c, H) and re.match(r"^[+-]?\d+(\.\d+)?$", str(c))
        if best:
            vals = [float(cells[i]) for i in best if num(cells[i])]
            top = max(vals) if len(vals) > 1 else None
            cells = [("<b>%s</b>" % e(c)) if top is not None and i in best and num(c) and float(c) == top else esc(c)
                     for i, c in enumerate(cells)]
        else:
            cells = [esc(c) for c in cells]
        cls = ' class="sep"' if str(r[0]).startswith("对照") else ""
        out.append("<tr%s>" % cls + "".join("<td>%s</td>" % c for c in cells) + "</tr>")
    out.append("</tbody></table></details>")
    if note:
        out.append('<p class="note">%s</p>' % note)
    return "\n".join(out)


def md_table(lines, title="表格"):
    """A Markdown table of breakdown.table() as HTML (folded)."""
    if not lines:
        return "<p>（没有数据）</p>"
    head = [c.strip() for c in lines[0].strip("|").split("|")]
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines[2:]]
    return table(head, rows, best=None, title=title)


def trace_stats(method, sub, label, docs):
    """Per document: (tool calls, requests or turns, output tokens, cost $ or None)."""
    out = []
    for d in docs:
        if method == "api":
            p = os.path.join(RUNS, "api", sub, label, d + ".trace.json")
            if not os.path.exists(p):
                out.append(None)
                continue
            t = json.load(open(p, encoding="utf-8"))
            tools = sum(len(c["tool_calls"]) for c in t["calls"])
            reqs = sum(c["turns"] for c in t["calls"])
            outp = sum(c["usage"].get("output_tokens", 0) for c in t["calls"])
            cost = None
            if not label.startswith("gpt"):
                cost = sum((c["usage"].get("input_tokens", 0) * 4 + c["usage"].get("output_tokens", 0) * 20 +
                            c["usage"].get("cache_creation_input_tokens", 0) * 5 +
                            c["usage"].get("cache_read_input_tokens", 0) * 0.2) / 1e6 for c in t["calls"])
            out.append((tools, reqs, outp, cost))
        else:
            p = os.path.join(EXP, "harness", sub, "answers", label, d + ".meta.json")
            if not os.path.exists(p):
                out.append(None)
                continue
            t = json.load(open(p, encoding="utf-8"))
            tools = sum(1 for c in t["tool_calls"] if "tools/" in c["input"])
            out.append((tools, t["num_turns"], (t["usage"] or {}).get("output_tokens", 0), t["cost_usd"]))
    return out


def _measured_as(d, key):
    """{doc: (input $, output $)} of the run directory d, priced as the model key."""
    out = {}
    for f in os.listdir(d):
        if f.endswith(".trace.json"):
            t = json.load(open(os.path.join(d, f), encoding="utf-8"))
            ins = outs = 0.0
            for c in t["calls"]:
                i, o = K.priced(key, c["usage"])
                ins += i
                outs += o
            out[f[:-11]] = (ins, outs)
    return out


def v1_autoaligned():
    """The old-prompt runs (label claude-opus-5-5) with the alignment removed and computed by autoalign."""
    import run as R
    import umrdoc
    out_dir = os.path.join(EXP, ".cache", "report-v1-autoalign")
    os.makedirs(out_dir, exist_ok=True)
    res = {}
    for sub in SUBS:
        J = [0, 0, 0]
        for d in ZH:
            raw = open(os.path.join(OBS, "api", sub, "claude-opus-5-5", d + ".raw.txt"), encoding="utf-8").read()
            noal = re.sub(r"# alignment:\n(?:[^\n#(]*\n)*", "", raw)
            umr, _ = umrdoc.parse_answer(R.doc_of(d), noal)
            p = os.path.join(out_dir, "%s.%s.umr" % (sub, d))
            open(p, "w", encoding="utf-8").write(umr)
            J = [a + b for a, b in zip(J, R.score_file(p, d, extra=False)["jumach"])]
        res[sub] = B.f1(*J)
    return res


CSS = """
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Noto Sans CJK SC",sans-serif;
 max-width:1180px;margin:2rem auto;padding:0 1.2rem;line-height:1.6;color:#1d1d1f;background:#fff}
h1{font-size:1.7rem;margin-bottom:.2rem} h2{font-size:1.3rem;margin-top:2.4rem;border-bottom:1px solid #ddd;padding-bottom:.2rem}
h3{font-size:1.05rem;margin-top:1.6rem}
table{border-collapse:collapse;margin:.6rem 0;font-size:.86rem;display:block;overflow-x:auto;max-width:100%}
th,td{border:1px solid #ddd;padding:.25rem .5rem;text-align:right;white-space:nowrap}
th{background:#f5f5f7;position:sticky;top:0} td:first-child,th:first-child{text-align:left}
tr.sep td{color:#666;background:#fafafa}
.note{font-size:.83rem;color:#555;margin-top:.2rem} .lead{color:#444}
code{background:#f2f2f2;padding:0 .25rem;border-radius:3px}
ul{padding-left:1.3rem} li{margin:.2rem 0}
details{margin:.6rem 0} summary{cursor:pointer;font-weight:600}
nav a{margin-right:.8rem}
.tiles{display:flex;gap:12px;flex-wrap:wrap;margin:.6rem 0}
.tile{border:1px solid rgba(11,11,11,.10);border-radius:8px;padding:10px 14px;min-width:220px}
.tl{font-size:.82rem;color:#52514e} .tv{font-size:2rem;font-weight:600} .td{font-size:.82rem;color:#52514e}
@media (prefers-color-scheme: dark){.tl,.td{color:#aaa} .tile{border-color:#333} body{background:#111;color:#e6e6e6} th{background:#222} th,td{border-color:#333}
 tr.sep td{background:#181818;color:#999} code{background:#222} .note,.lead{color:#aaa} h2{border-color:#333}}
"""


def facets_for(rows_of, series_defs, docs, root=RUNS):
    """facet_hbar facets (Smatch, AnCast++, juːmæʧ) for rows_of: [(method, sub, label) per series per row]."""
    facets = []
    for metric, key, rp in (("Smatch", "Smatch", True), ("AnCast++（综合）", "AnCast Comprehensive", False),
                            ("juːmæʧ", "juːmæʧ", True)):
        vals, marks = {}, {}
        for si in range(len(series_defs)):
            xs = [m(*rows_of[ci][si], docs, root) or {} if rows_of[ci][si] else {} for ci in range(len(rows_of))]
            vals[si] = [x.get(key + (" F" if rp else "")) for x in xs]
            if rp:
                marks[si] = [(x[key + " R"], x[key + " P"]) if x else None for x in xs]
        facets.append((metric, vals, marks if rp else None))
    return facets


def run_dir(method, sub, label, root=RUNS):
    """The repository path of a run directory (from the repo root)."""
    base = "exp/runs" if root == RUNS else "obsolete/exp/runs"
    return "%s/%s/%s/%s/" % (base, method, sub, label) if sub else "%s/%s/%s/" % (base, method, label)


def file_links(method, sub, label, d, root=RUNS):
    """Links to one file's records: the answer as written, the parsed .umr that is scored, the prompt, the
    whole conversation, the scores."""
    rd = run_dir(method, sub, label, root)
    disk = os.path.join(os.path.dirname(EXP), rd)
    out = [link(rd + d + ".raw.txt", "回答原文"), link(rd + d + ".umr", "解析结果 .umr")]
    if method == "api":
        if os.path.isdir(os.path.join(disk, d + ".calls")):
            out.append(link(rd + d + ".calls/", "每次调用的 prompt 和对话"))
        else:
            out += [link(rd + d + ".prompt.md", "prompt"), link(rd + d + ".transcript.json", "完整对话")]
    elif method == "harness":
        a = "exp/harness/%s/answers/%s/" % (sub, label)
        out += [link(a + d + ".prompt.md", "prompt"), link(a + d + ".transcript.jsonl", "完整会话")]
    elif method == "chat":
        out.append(link("exp/chat/%s/prompts/%s.md" % (sub, d), "prompt"))
    out += [link(rd + d + ".trace.json", "解析问题"), link(rd + "scores.md", "分数")]
    return H(" · ".join(out))


RSI_RUNS = os.path.join(EXP, "rsi", "runs")
TRAJ = [("s3-all-rules-claude-opus-5-5", "三个工具 · 规则型", 1, "circle"),
        ("s3-all-examples-claude-opus-5-5", "三个工具 · 例子型", 2, "diamond"),
        ("s1-abridged-rules-claude-opus-5-5", "无工具 · 规则型", 3, "circle"),
        ("s1-abridged-examples-claude-opus-5-5", "无工具 · 例子型", 4, "diamond")]
STEPS = [("v0", "起点"), ("after-b1", "batch 1 后"), ("after-b2", "batch 2 后"), ("after-b3", "batch 3 后"),
         ("after-b4", "batch 4 后")]


def rsi_cost(d):
    """List-price cost of every call of a trajectory, by kind."""
    import glob
    tot = {}
    for f in glob.glob(os.path.join(d, "**", "*.transcript.json"), recursive=True):
        t = json.load(open(f, encoding="utf-8"))
        c = sum(K.priced(CLAUDE, r["usage"])[0] + K.priced(CLAUDE, r["usage"])[1] for r in t["responses"])
        k = ("critique" if f.endswith("critique.transcript.json") else "reflect" if f.endswith("reflect.transcript.json")
             else "test" if os.sep + "test" + os.sep in f else "annotate")
        tot[k] = tot.get(k, 0) + c
    return tot


def rsi_section(P):
    TESTD = ["zh-0028", "zh-0032"]
    P.append('<h2 id="rsi">第四步：RSI（改 instruction）</h2>')
    P.append("<p>从 s3-all（缩略版 guideline + 三个工具）或 s1-abridged（只有缩略版 guideline，没有工具）出发，只改 instruction"
             "（任务说明和缩略版 guideline；输出格式和工具说明不改）。训练文档 <code>chinese_umr-0001</code>（shared task 训练数据，"
             "训练时 gold 搜索不返回它），每 5 句一个 batch，共 4 个 batch（第 1–20 句）：标注 → umrjudge 和 gold 对比 → critique"
             "（看判错的单元，提修改意见，可以用三个工具核对）→ reflect（改 instruction，≤3 万字符，不抄测试文档）→ 重标这一批，"
             "AnCast++ 综合分比之前最好的高才保留；每个 batch 反思 3 次。每个 batch 后用当时最好的版本标测试文档 zh-0028、zh-0032。"
             "两种反思方式：<b>规则型</b>只写一般规则，不准记录细节（也不准抄训练文档）；<b>例子型</b>把出错的地方整理成具体例子记进 "
             "instruction。模型都是 Claude Opus 5.5（API，effort medium）。代码 %s，说明见 exp/README.md。</p>"
             % link("exp/rsi/rsi.py", "exp/rsi/rsi.py"))
    data = {}
    for traj, _, _, _ in TRAJ:
        for tag, _ in STEPS:
            p = os.path.join(RSI_RUNS, traj, "test", tag, "scores.json")
            if os.path.exists(p):
                data[(traj, tag)] = B.metrics(json.load(open(p, encoding="utf-8"))["docs"], TESTD)[0]
    series = [(name, slot, mk) for _, name, slot, mk in TRAJ]
    facets = []
    for metric, key in (("Smatch F", "Smatch F"), ("AnCast++ 综合", "AnCast Comprehensive"), ("juːmæʧ F", "juːmæʧ F")):
        facets.append((metric, {si: [(data.get((t[0], tag)) or {}).get(key) for tag, _ in STEPS] for si, t in enumerate(TRAJ)}))
    P.append(C.line_facets("测试文档 zh-0028 + zh-0032 上的学习曲线", ["起点", "b1", "b2", "b3", "b4"], facets, series,
                           ymin=35, ymax=65, step=5))
    P.append('<p class="note">横轴是起点和每个 batch（b1–b4）结束后的版本；颜色区分四条轨迹，圆点 = 规则型、菱形 = 例子型。悬停在某一列上看四条轨迹的数值。'
             "起点的 Smatch 在四条轨迹间有零点几的差别，是 Smatch 自身的随机性（同样的文件）。</p>")
    rows = []
    for traj, name, _, _ in TRAJ:
        st = json.load(open(os.path.join(RSI_RUNS, traj, "state.json"), encoding="utf-8"))
        vers = {"v0": 0}
        vers.update({"after-b%d" % b["batch"]: b["version"] for b in st["batches"]})
        for tag, label in STEPS:
            x = data.get((traj, tag))
            if not x:
                continue
            v = vers.get(tag, 0)
            vp = "exp/rsi/runs/%s/versions/v%d.md" % (traj, v)
            size = len(open(os.path.join(os.path.dirname(EXP), vp), encoding="utf-8").read())
            rows.append([name, label, fmt(x["Smatch F"]), fmt(x["Smatch R"]), fmt(x["Smatch P"]),
                         fmt(x.get("AnCast Comprehensive")), fmt(x.get("AnCast F")), fmt(x["juːmæʧ F"]),
                         fmt(x["juːmæʧ R"]), fmt(x["juːmæʧ P"]), H(link(vp, "v%d（%d 字符）" % (v, size))),
                         H(link("exp/rsi/runs/%s/test/%s/" % (traj, tag), "测试结果"))])
    P.append(table(["轨迹", "版本", "Smatch F", "S R", "S P", "AnCast++ 综合", "AnCast 句子级 F", "juːmæʧ F", "J R", "J P",
                    "instruction", "目录"], rows, title="每条轨迹、每个 batch 后的测试分数和 instruction"))
    rows = []
    for traj, name, _, _ in TRAJ:
        st = json.load(open(os.path.join(RSI_RUNS, traj, "state.json"), encoding="utf-8"))
        for b in st["batches"]:
            refl = []
            for r in b["reflections"]:
                refl.append("–（没改成）" if r["score"] is None else "%.1f%s" % (r["score"], " ✓" if r.get("accepted") else ""))
            rows.append([name, "batch %d（第 %d–%d 句）" % (b["batch"], b["first"], b["last"]), "%.1f" % b["start"]]
                        + refl + ["%.1f" % b["end"], "v%d" % b["version"],
                                  H(link("exp/rsi/runs/%s/b%d/" % (traj, b["batch"]), "critique、reflect、改动"))])
    P.append(table(["轨迹", "batch", "开始", "反思 1", "反思 2", "反思 3", "结束", "版本", "记录"], rows,
                   title="训练：每个 batch 上的 AnCast++ 综合分（✓ = 保留）",
                   note="batch 上的分数是改过 instruction 之后在同一批句子上重标的，critique 看过这批句子的 gold，所以会涨得很高（到 80–100），"
                        "主要是对这一批的拟合；真正看学到没有要看测试文档。instruction 在第 2–3 个 batch 就接近 3 万字符的上限，"
                        "之后每次修改都要删掉一些东西才能加。"))
    cols, delta = [], {}
    for traj, name, _, _ in TRAJ:
        cols += [("%s 起点" % name, traj, "test", "v0"), ("%s batch 4 后（差）" % name, traj, "test", "after-b4")]
        delta["%s batch 4 后（差）" % name] = "%s 起点" % name
    P.append(md_table(B.table(cols, TESTD, delta, root=RSI_RUNS), "测试文档上的全部分项：起点和 batch 4 后的差"))
    rows = []
    for traj, name, _, _ in TRAJ:
        c = rsi_cost(os.path.join(RSI_RUNS, traj))
        rows.append([name] + ["$%.2f" % c.get(k, 0) for k in ("annotate", "critique", "reflect", "test")]
                    + ["$%.2f" % sum(c.values()), H(link("exp/rsi/runs/%s/" % traj, "目录"))])
    P.append(table(["轨迹", "标注 batch", "critique", "reflect", "测试", "合计", "目录"], rows,
                   title="每条轨迹的花费（按 Opus 5.5 价格算）",
                   note="包括起点测试（和 s3-all、s1-abridged 是同样的请求，走的缓存，实际没花钱）。另外三条轨迹第一次跑时因为解析 bug 中途作废，"
                        "那部分大约又花了 $25–30，不在表里。规则型 + 三个工具这条用的 reflect prompt 少了后来加的一句"
                        "“（如果标注模型有工具）”，其余相同。"))


def main():
    import subprocess
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=EXP, capture_output=True, text=True).stdout.strip()
    P = []
    P.append("<h1>UMR 整篇文档标注实验：目前为止的全部结果</h1>")
    P.append('<p class="lead">HarnessOntologyAnnotation <code>exp/</code>，提交 <code>%s</code>，由 <code>python3 exp/scripts/report.py</code> '
             "从仓库里的分数和记录生成。测试数据和打分方式与 DMR 2026 UMR parsing shared task 一致（UMR 2.2 官方测试集和 gold）。"
             "所有表格默认折叠，点开查看；表里的链接指向 GitHub 上的文件。</p>" % e(commit))
    P.append("<nav>" + "".join('<a href="#%s">%s</a>' % (a, t) for a, t in [
        ("setup", "设定"), ("main", "主结果"), ("methods", "三种方法"), ("chat", "chat"), ("breakdown", "分项"),
        ("ablation", "一句句跑"), ("alltools", "三个工具"), ("usage", "工具与用量"), ("cost", "花费"),
        ("rsi", "第四步：RSI"), ("files", "逐文件结果与链接"), ("archived", "已归档的旧结果"), ("caveats", "局限")]) + "</nav>")

    # ---------------------------------------------------------------- setup
    P.append('<h2 id="setup">设定</h2>')
    P.append(table(["测试文件", "语言", "句数", "词数"], [["zh-0028", "中文", 12, 250], ["zh-0032", "中文", 6, 187],
                                                    ["en-0008", "英文", 9, 140]], title="测试文件"))
    P.append(table(["条件", "给模型的资源"], [
        ["s1-abridged", "缩略版 guideline（1.4 万字符）"], ["s1-full", "完整 guideline（36.6 万字符）"],
        ["s2-search", "缩略版 + search_guidelines 工具（搜完整 guideline）"],
        ["s2-propbank", "缩略版 + propbank_lookup 工具"],
        ["s2-gold", "缩略版 + search_annotations 工具（shared task 训练数据的 gold，不含测试句子）"],
        ["s3-all", "缩略版 + 三个工具都能用（search_guidelines、propbank_lookup、search_annotations）；只用 API"],
        ["a1-sentence-propbank", "s2-propbank 的资源，一句句跑：先每句单独标句子图；全部标完后，每句再给它和前五句的原文与图，标这一句的文档级关系；只用 API"],
        ["a2-sentence-all", "s3-all 的资源（三个工具），一句句跑，做法同 a1；只用 API"]], title="条件（子实验）"))
    P.append(table(["方法", "模型 / 标签", "说明"], [
        ["API", "claude-opus-5-5（标签 claude-opus-5-5-v2）", "effort medium，adaptive thinking；不开拒答回退，每个回答都出自这个模型"],
        ["API", "gpt-6.1-sol（gpt-6.1-sol-medium）", "OpenAI Responses API，reasoning effort medium，同样的 prompt、工具和循环"],
        ["Claude Code", "claude-opus-5-5（claude-code）", "订阅；每篇一个工作目录（TASK.md + guideline 文件 + 工具命令），只能读本目录、运行工具、写 answer.txt"],
        ["chat", "Claude chat（claude-chat）", "人工把 prompt 贴进 claude.ai 的 chat 窗口，附件代替工具"],
        ["chat", "ChatGPT（chatgpt、chatgpt-6-astra-high）", "同上，ChatGPT 的 chat 窗口"],
        ["Codex", "–", "OpenAI 这边的 harness，还没做"],
        ["API（已归档）", "gpt-6-astra（gpt-6-astra-medium）", "先跑的另一个 GPT 模型；后来改用 gpt-6.1-sol，见“已归档的旧结果”"]],
        title="方法和模型"))
    P.append("<h3>打分</h3><ul>"
             "<li><b>Smatch</b> 和 <b>AnCast++</b>：Smatch 只比句子图；AnCast++ 的综合分（Comprehensive）把句子级和文档级（时间、模态、"
             "共指）合在一起。两者都靠自己的节点配对，不看词对齐。</li>"
             "<li><b>juːmæʧ</b>（shared task 的主指标，umrtools compare_umr.pl）：先用词对齐配对节点，所以预测必须带对齐。"
             "模型不写对齐，对齐由 <code>lib/autoalign.py</code> 从图和句子生成。</li>"
             "<li>中文两篇：Smatch、juːmæʧ 把计数加总再算；AnCast++ 取两篇的平均。<b>umrjudge</b> 的分项见“分项”一节。</li></ul>")
    vr = []
    for line in open(os.path.join(RUNS, "shared-task", "verify.md"), encoding="utf-8"):
        if line.startswith("| orange") or line.startswith("| sema"):
            vr.append([c.strip() for c in line.strip().strip("|").split("|")])
    P.append(table(["系统", "语言", "juːmæʧ（这里）", "论文表 2", "Smatch（这里）", "论文表 5"], vr,
                   title="打分核对：重算两支参赛队伍的输出，和概述论文对照",
                   note="juːmæʧ 差 0.5 以内，Smatch 差 0.3 以内（Smatch 本身有随机性）。"))

    # ---------------------------------------------------------------- main
    P.append('<h2 id="main">主结果：API，每个条件</h2>')
    series_defs = [("Claude Opus 5.5", 1), ("GPT-6.1 Sol", 2)]
    for lang, ds in (("中文（zh-0028 + zh-0032）", ZH), ("英文（en-0008）", EN)):
        rows_of = [[("api", s, CLAUDE), ("api", s, SOL)] for s in B.API_SUBS]
        o = m("shared-task", "", "orange", ds)
        refs = {0: [("Orange %.0f" % o["Smatch F"], o["Smatch F"])],
                1: [("Orange %.0f" % o["AnCast Comprehensive"], o["AnCast Comprehensive"])] if o.get("AnCast Comprehensive") else [],
                2: [("Orange %.0f" % o["juːmæʧ F"], o["juːmæʧ F"])]}
        P.append(C.facet_hbar("%s：Smatch、AnCast++、juːmæʧ" % lang, [SHORTNAME[s] for s in B.API_SUBS],
                              facets_for(rows_of, series_defs, ds), series_defs, refs=refs, label_w=140, panel_w=210))
    P.append('<p class="note">三栏同一个 0–100 的刻度。每个条件两根条：Claude Opus 5.5（蓝）和 GPT-6.1 Sol（橙），effort 都是 medium。'
             "条的长度是 F1；Smatch 和 juːmæʧ 的圆点是召回 R、菱形是精确 P（AnCast++ 综合分没有召回和精确）。竖线是参赛队伍 Orange "
             "在同样文件上的分数。数值见悬停提示和下表。</p>")
    rows = []
    cell = lambda x: [fmt(x and x["Smatch F"]), fmt(x and x["Smatch R"]), fmt(x and x["Smatch P"]),
                      fmt(x and x.get("AnCast Comprehensive")), fmt(x and x.get("AnCast F")),
                      fmt(x and x["juːmæʧ F"]), fmt(x and x["juːmæʧ R"]), fmt(x and x["juːmæʧ P"])]
    for sub in B.API_SUBS:
        r = [NAME[sub]]
        for docs in (ZH, EN):
            for lab in (CLAUDE, SOL):
                r += cell(m("api", sub, lab, docs))
        r.append(H(link(run_dir("api", sub, CLAUDE), "Claude") + " · " + link(run_dir("api", sub, SOL), "GPT")))
        rows.append(r)
    for sysname in ("orange", "sema"):
        r = ["对照：参赛队伍 %s" % sysname.capitalize()]
        for docs in (ZH, EN):
            r += cell(m("shared-task", "", sysname, docs)) + [""] * 8
        rows.append(r + [""])
    head = ["条件"] + ["%s %s %s" % (lg, md, k) for lg in ("中文", "英文") for md in ("Claude", "GPT")
                       for k in ("Smatch F", "S R", "S P", "AnCast++ 综合", "AnCast 句子级 F", "juːmæʧ F", "J R", "J P")] + ["结果目录"]
    P.append(table(head, rows, best=[1, 9], title="主表：每个条件的 Smatch、AnCast++、juːmæʧ（含召回、精确）和结果目录",
                   note="S = Smatch，J = juːmæʧ；F = F1，R = 召回，P = 精确。中文 = zh-0028 + zh-0032，英文 = en-0008。"
                        "粗体：这一行中文两个模型里 Smatch 较高的。参赛队伍的列放在 Claude 的位置上，只作对照。"))

    # ---------------------------------------------------------------- methods
    P.append('<h2 id="methods">三种用法：API、harness、chat</h2>')
    P.append("<h3>Claude（Claude Opus 5.5）：API、Claude Code、Claude chat，中文两篇</h3>")
    sd = [("API", 1), ("Claude Code", 2), ("Claude chat", 3)]
    rows_of = [[("api", s, CLAUDE), ("harness", s, "claude-code"), ("chat", s, "claude-chat")] for s in SUBS]
    P.append(C.facet_hbar("Claude 的三种用法（中文两篇）", [SHORTNAME[s] for s in SUBS], facets_for(rows_of, sd, ZH), sd,
                          label_w=110, panel_w=200))
    P.append('<p class="note">没有条的是没跑：Claude chat 只有 abridged 的两篇；它的 +PropBank 只有 zh-0032 一篇，不在两篇合计里（见 chat 一节）。</p>')
    P.append("<h3>OpenAI：API（gpt-6.1-sol）、ChatGPT chat，abridged，逐个文件</h3>")
    sd = [("API gpt-6.1-sol", 1), ("ChatGPT chat", 2), ("Codex（未做）", 3)]
    chat_of = {"zh-0032": "chatgpt-6-astra-high", "en-0008": "chatgpt"}
    facets = []
    for metric, key, rp in (("Smatch", "Smatch", True), ("AnCast++（综合）", "AnCast Comprehensive", False), ("juːmæʧ", "juːmæʧ", True)):
        vals, marks = {}, {}
        for si, kind in enumerate(("api", "chat", "codex")):
            xs = []
            for d in DOCS:
                if kind == "api":
                    x = m("api", "s1-abridged", SOL, [d])
                elif kind == "chat" and d in chat_of:
                    x = m("chat", "s1-abridged", chat_of[d], [d])
                else:
                    x = None
                xs.append(x or {})
            vals[si] = [x.get(key + (" F" if rp else "")) for x in xs]
            if rp:
                marks[si] = [(x[key + " R"], x[key + " P"]) if x else None for x in xs]
        facets.append((metric, vals, marks if rp else None))
    P.append(C.facet_hbar("OpenAI 的用法（abridged，每个文件）", DOCS, facets, sd, label_w=90, panel_w=200))
    P.append('<p class="note">ChatGPT chat 只有两份回答：zh-0032（chatgpt-6-astra-high）和 en-0008（标签 chatgpt）；zh-0028 没有。'
             "Codex 的 harness 还没做，所以第三根条是空的。</p>")
    rows = []
    for sub in SUBS:
        r = [NAME[sub]]
        for docs in (ZH, EN):
            for method, lab in (("api", CLAUDE), ("harness", "claude-code"), ("chat", "claude-chat")):
                s = B.load(method, sub, lab)
                x, have = B.metrics(s, docs) if s else (None, [])
                r.append("–" if x is None else "%s / %s / %s%s" % (fmt(x["Smatch F"]), fmt(x.get("AnCast Comprehensive")),
                                                                   fmt(x["juːmæʧ F"]),
                                                                   "" if len(have) == len(docs) else "（仅 %s）" % ",".join(have)))
        rows.append(r)
    P.append(table(["条件", "中文 API", "中文 Claude Code", "中文 Claude chat", "英文 API", "英文 Claude Code", "英文 Claude chat"],
                   rows, title="Claude 三种用法的分数（Smatch / AnCast++ 综合 / juːmæʧ）",
                   note="Claude Code 没跑英文；Claude chat 只做了 s1-abridged 和 s2-propbank。"))

    # ---------------------------------------------------------------- chat
    P.append('<h2 id="chat">chat 的每一份回答</h2>')
    rows = []
    for sub in SUBS:
        for lab in ("claude-chat", "chatgpt", "chatgpt-6-astra-high"):
            s = B.load("chat", sub, lab)
            if not s:
                continue
            for d in sorted(s):
                x = m("chat", sub, lab, [d])
                api = m("api", sub, CLAUDE, [d])
                rows.append([sub, lab, d, fmt(x["Smatch F"]), fmt(x.get("AnCast Comprehensive")), fmt(x["juːmæʧ F"]),
                             "是" if s[d]["valid"]["passed"] else "否", fmt(api and api["juːmæʧ F"]),
                             file_links("chat", sub, lab, d)])
    P.append(table(["条件", "chat 模型", "文件", "Smatch F", "AnCast++ 综合", "juːmæʧ F", "通过格式检查",
                    "同条件 Claude API 的 juːmæʧ", "文件"], rows, title="chat 的回答和文件链接",
                   note="格式检查是 umrtools validate.py --level 2；没通过的都是图里有环，gold 在同样的句子也有环，照常计分。"))

    # ---------------------------------------------------------------- breakdown
    P.append('<h2 id="breakdown">分项（umrjudge 每项检查、AnCast++ 各项）</h2>')
    P.append("<p>umrjudge 的每项检查有三行：F1、召回 R（gold 一侧的单元：correct、partial、wrong、missing 的平均得分）和"
             "精确 P（预测一侧：correct、partial、wrong、extra 的平均得分），百分制；中文两篇把单元合在一起算。"
             "同样的表也在 <code>exp/breakdown.md</code>。</p>")
    systems = [("Claude API", "api", CLAUDE), ("GPT API", "api", SOL)]
    keys = ["Smatch F", "juːmæʧ F", "b_event_sense", "a_event_concept", "a_entity_concept", "d_core_args_event",
            "d_core_args_abstract", "e_core_labels", "e_peripheral_labels", "c_aspect", "c_refer", "f_name_tokens",
            "g_reentrancy", "h_temporal", "i_modal", "j_coref_chain"]

    def key_of(k, metric):
        if metric == "F":
            return k
        return k[:-2] + " " + metric if k in ("juːmæʧ F", "Smatch F") else k + " " + metric
    P.append('<div class="metricbar" data-group="heat" role="group" aria-label="热力图显示哪一个指标">'
             '<button data-metric="F" aria-pressed="true">F1</button><button data-metric="R" aria-pressed="false">召回 R</button>'
             '<button data-metric="P" aria-pressed="false">精确 P</button></div>')
    for metric, mname in (("F", "F1"), ("R", "召回 R"), ("P", "精确 P")):
        hm = []
        for title, lab in (("Claude Opus 5.5", CLAUDE), ("GPT-6.1 Sol", SOL)):
            base = m("api", "s1-abridged", lab, ZH)
            cols = B.API_SUBS[1:]
            vals = []
            for k in keys:
                kk = key_of(k, metric)
                vals.append([None if not (x := m("api", sub, lab, ZH)) or x.get(kk) is None or base.get(kk) is None
                             else x[kk] - base[kk] for sub in cols])
            hm.append(C.heatmap("%s：%s 相对 abridged 的变化（中文，分）" % (title, mname), [HEATNAME.get(k, k) for k in keys],
                                [HEATCOL[s] for s in cols], vals, vmax=20, label_w=190, cell=(60, 22)))
        P.append('<div class="vizrow" data-metric-group="heat" data-metric-view="%s"%s>%s</div>' % (
            metric, "" if metric == "F" else " hidden", "".join(hm)))
    P.append('<p class="note">用上面的按钮切换 F1、召回、精确。每格是这个条件减去同一模型 s1-abridged 的分差：蓝 = 更高，红 = 更低，'
             "灰 = 不变；±20 分以上颜色不再加深。a1 = PropBank 一句句跑，a2 = 三个工具一句句跑。数值见悬停提示和下面的表。</p>")
    for lang, ds in (("中文（zh-0028 + zh-0032）", ZH), ("英文（en-0008）", EN)):
        cols = [("%s %s" % (n, B.SHORT[s]), mm, s, l) for n, mm, l in systems for s in B.API_SUBS]
        P.append(md_table(B.table(cols, ds), "%s：API 每个条件的全部分项（绝对分数）" % lang))
        cols, delta = [], {}
        for n, mm, l in systems:
            cols.append(("%s %s" % (n, B.SHORT["s1-abridged"]), mm, "s1-abridged", l))
            for s in B.API_SUBS[1:]:
                h = "%s %s" % (n, B.SHORT[s])
                cols.append((h, mm, s, l))
                delta[h] = "%s %s" % (n, B.SHORT["s1-abridged"])
        P.append(md_table(B.table(cols, ds, delta), "%s：API 每个条件相对 abridged 的变化" % lang))
        cols = []
        for s in SUBS:
            cols += [("API %s" % B.SHORT[s], "api", s, CLAUDE), ("Claude Code %s" % B.SHORT[s], "harness", s, "claude-code"),
                     ("Claude chat %s" % B.SHORT[s], "chat", s, "claude-chat")]
        for lab in ("chatgpt-6-astra-high", "chatgpt"):
            cols += [("ChatGPT chat (%s) %s" % (lab, B.SHORT[s]), "chat", s, lab) for s in SUBS]
        P.append(md_table(B.table(cols, ds), "%s：Claude 三种用法和 ChatGPT chat 的分项" % lang))

    # ---------------------------------------------------------------- ablation
    P.append('<h2 id="ablation">一句句跑对整篇一次标：a1（PropBank）对 s2-propbank，a2（三个工具）对 s3-all</h2>')
    pairs = ["s2-propbank", "a1-sentence-propbank", "s3-all", "a2-sentence-all"]
    cats = ["PropBank：整篇", "PropBank：一句句", "三个工具：整篇", "三个工具：一句句"]
    for lang, ds in (("中文", ZH), ("英文", EN)):
        rows_of = [[("api", s, CLAUDE), ("api", s, SOL)] for s in pairs]
        P.append(C.facet_hbar("%s：整篇对一句句" % lang, cats, facets_for(rows_of, series_defs, ds), series_defs,
                              label_w=120, panel_w=200))
    for lang, ds in (("中文", ZH), ("英文", EN)):
        cols, delta = [], {}
        for n, mm, l in systems:
            cols += [("%s PropBank 整篇" % n, mm, "s2-propbank", l), ("%s PropBank 一句句（差）" % n, mm, "a1-sentence-propbank", l),
                     ("%s 三个工具 整篇" % n, mm, "s3-all", l), ("%s 三个工具 一句句（差）" % n, mm, "a2-sentence-all", l)]
            delta["%s PropBank 一句句（差）" % n] = "%s PropBank 整篇" % n
            delta["%s 三个工具 一句句（差）" % n] = "%s 三个工具 整篇" % n
        P.append(md_table(B.table(cols, ds, delta), "%s：整篇和一句句的全部分项（一句句一列是差值）" % lang))
    P.append('<p class="note">一句句跑每篇的调用次数 = 2 × 句数；每次调用的 prompt 和完整对话在 '
             "<code>runs/api/&lt;条件&gt;/&lt;标签&gt;/&lt;文件&gt;.calls/</code>（逐文件一节有链接）。</p>")

    # ---------------------------------------------------------------- all three tools
    P.append('<h2 id="alltools">三个工具都能用：模型查了什么</h2>')
    rows = []
    for sub in ("s3-all", "a2-sentence-all"):
        for title, lab in (("Claude Opus 5.5", CLAUDE), ("GPT-6.1 Sol", SOL)):
            for d in DOCS:
                t = json.load(open(os.path.join(RUNS, "api", sub, lab, d + ".trace.json"), encoding="utf-8"))
                cnt = {}
                for c in t["calls"]:
                    for x in c["tool_calls"]:
                        cnt[x["name"]] = cnt.get(x["name"], 0) + 1
                x = m("api", sub, lab, [d])
                rows.append([NAME[sub], title, d, cnt.get("search_guidelines", 0), cnt.get("propbank_lookup", 0),
                             cnt.get("search_annotations", 0), fmt(x["Smatch F"]), fmt(x["juːmæʧ F"]),
                             file_links("api", sub, lab, d)])
    P.append(table(["条件", "模型", "文件", "search_guidelines", "propbank_lookup", "search_annotations", "Smatch F",
                    "juːmæʧ F", "文件"], rows, title="每篇每个工具的调用次数",
                   note="Claude 两种方案都从不搜 guideline：整篇一次标时每篇只查 2–3 次，一句句跑时每篇 18–30 次，最多的是 gold 例子。"
                        "GPT 三个工具都用：整篇一次标时每篇 15–16 次，一句句跑时每篇 91–170 次。"))

    # ---------------------------------------------------------------- usage
    P.append('<h2 id="usage">工具调用和用量</h2>')
    tool_subs = ["s2-search", "s2-propbank", "s2-gold", "s3-all", "a1-sentence-propbank", "a2-sentence-all"]
    series = []
    for name, slot, lab in (("Claude Opus 5.5", 1, CLAUDE), ("GPT-6.1 Sol", 2, SOL)):
        vals = []
        for sub in tool_subs:
            st = [x for x in trace_stats("api", sub, lab, DOCS) if x]
            vals.append(sum(x[0] for x in st) / len(st) if st else None)
        series.append((name, slot, vals))
    P.append(C.grouped_hbar("每篇平均工具调用次数（三篇平均）", [SHORTNAME[s] for s in tool_subs], series,
                            140, step=20, label_w=150, width=620, fmt="%.0f"))
    rows = []
    for sub in B.API_SUBS:
        for title, method, lab in (("Claude API", "api", CLAUDE), ("GPT-sol API", "api", SOL),
                                   ("Claude Code", "harness", "claude-code")):
            st = trace_stats(method, sub, lab, DOCS)
            if not any(st):
                continue
            costs = [x[3] for x in st if x and x[3] is not None]
            rows.append([NAME[sub], title, " / ".join("–" if x is None else str(x[0]) for x in st),
                         " / ".join("–" if x is None else str(x[1]) for x in st), "%d" % sum(x[2] for x in st if x),
                         ("$%.2f" % sum(costs)) if costs else "–"])
    P.append(table(["条件", "系统", "工具调用（zh-0028 / zh-0032 / en-0008）", "请求数或轮数", "输出 token 合计", "花费"], rows,
                   title="每个条件、每个系统的工具调用、轮数、输出 token 和花费",
                   note="花费：Claude API 按 Opus 5.5 的价格算（输入 $4、输出 $20、写缓存 $5、读缓存 $0.20，每百万 token）；"
                        "Claude Code 是它自己报的 API 价格折算（实际走订阅）；GPT 在“花费”一节按 OpenAI 的价格算。"
                        "Claude Code 的工具调用只数运行 tools/ 命令的次数（不算 Read、Grep 等）。"))

    # ---------------------------------------------------------------- cost
    P.append('<h2 id="cost">花费：整个实验跑一遍要多少钱（估算）</h2>')
    est = K.estimate(("zh", "en"))
    tot = {lab: sum(r["total"] for r in est if r["label"] == lab) for lab in K.PRICES}
    zh_tot = {lab: sum(r["full"]["zh"] or 0 for r in est if r["label"] == lab) for lab in K.PRICES}
    tiles = []
    for lab, name in ((CLAUDE, "Claude Opus 5.5"), (SOL, "GPT-6.1 Sol")):
        tiles.append('<div class="tile"><div class="tl">%s，8 个条件全量（中文 + 英文）</div><div class="tv">$%.0f</div>'
                     '<div class="td">其中中文 15 篇 $%.0f</div></div>' % (e(name), tot[lab], zh_tot[lab]))
    P.append('<div class="tiles">%s</div>' % "".join(tiles))
    series = [(name, slot, [next((r["total"] for r in est if r["label"] == lab and r["sub"] == s), None) for s in B.API_SUBS])
              for name, slot, lab in (("Claude Opus 5.5", 1, CLAUDE), ("GPT-6.1 Sol", 2, SOL))]
    P.append(C.grouped_hbar("每个条件全量的估算花费（中文 15 篇 + 英文 5 篇）", [SHORTNAME[s] for s in B.API_SUBS], series, 80,
                            unit="", step=10, label_w=150, width=620, fmt="$%.0f"))
    rows = [[r["model"], NAME[r["sub"]], "$%.2f" % r["sample_cost"], "$%.0f" % (r["full"]["zh"] or 0),
             "$%.0f" % (r["full"]["en"] or 0), "$%.0f" % r["total"]] for r in est]
    P.append(table(["模型", "条件", "这 3 篇实际（按价格算）", "全量中文（15 篇）", "全量英文（5 篇）", "全量合计"], rows,
                   title="每个模型、每个条件的花费估算",
                   note="做法：把这 3 篇的用量按价格算成钱，分成输入侧（输入、写缓存、读缓存）和输出侧（输出，含思考），按语言外推到全部测试文件："
                        "输出侧按词数放大；输入侧在 s1-abridged、s1-full 按文件数（主要是每篇都一样的 guideline），一句句跑的按句数，其余按词数。"
                        "只有 3 篇，误差大约 ±50%；英文 en-0000 有 2,120 个词，整篇一次标可能碰到输出上限。价格（每百万 token）："
                        "claude-opus-5-5 输入 $4、写缓存 $5、读缓存 $0.20、输出 $20；gpt-6.1-sol 输入 $2、读缓存 $0.10、输出 $10"
                        "（OpenAI 价格页，2026 年 11 月）。Claude Code 和 chat 走订阅，不在这里。"))
    spent = {}
    for root in (RUNS, OBS):
        for sub in os.listdir(os.path.join(root, "api")):
            for lab in os.listdir(os.path.join(root, "api", sub)):
                key = CLAUDE if lab.startswith("claude") else lab
                if key not in K.PRICES:
                    continue
                for d, (i, o) in _measured_as(os.path.join(root, "api", sub, lab), key).items():
                    spent[key] = spent.get(key, 0) + i + o
    P.append('<p class="note">到目前为止 API 实际用掉的（按上面的价格算，所有跑过的 API 运行，包括已归档的）：Claude 约 $%.0f，'
             "gpt-6.1-sol 约 $%.0f，gpt-6-astra 约 $%.0f。</p>" % (spent.get(CLAUDE, 0), spent.get(SOL, 0),
                                                                spent.get("gpt-6-astra-medium", 0)))

    # ---------------------------------------------------------------- RSI
    rsi_section(P)

    # ---------------------------------------------------------------- per-file results and links
    P.append('<h2 id="files">逐文件结果与文件链接</h2>')
    P.append("<p>每一行是一次运行的一篇文件，链接到 GitHub 上的：模型的回答原文（<code>.raw.txt</code>）；"
             "<b>解析结果</b>（<code>.umr</code>：把回答解析、补上自动对齐、文档级关系分到各句后，按 shared task 格式写出的文件，"
             "打分用的就是它）；实际发出的 prompt；完整对话；解析时记下的问题（<code>.trace.json</code> 的 <code>parse.problems</code>）；"
             "这次运行的分数（<code>scores.md</code>）。</p>")
    for title, method, labels in (("API", "api", (CLAUDE, SOL)), ("Claude Code", "harness", ("claude-code",)),
                                  ("chat", "chat", ("claude-chat", "chatgpt", "chatgpt-6-astra-high"))):
        rows = []
        for sub in (B.API_SUBS if method == "api" else SUBS):
            for lab in labels:
                s = B.load(method, sub, lab)
                if not s:
                    continue
                for d in DOCS:
                    if d not in s:
                        continue
                    x = m(method, sub, lab, [d])
                    rows.append([sub, lab, d, fmt(x["Smatch F"]), fmt(x.get("AnCast Comprehensive")), fmt(x["juːmæʧ F"]),
                                 "是" if s[d]["valid"]["passed"] else "否", file_links(method, sub, lab, d)])
        P.append(table(["条件", "标签", "文件", "Smatch F", "AnCast++ 综合", "juːmæʧ F", "通过格式检查", "文件"], rows,
                       title="%s：每次运行、每篇文件" % title))

    # ---------------------------------------------------------------- archived
    P.append('<h2 id="archived">已归档的旧结果（<code>obsolete/exp/runs/</code>）</h2>')
    P.append("<p>被后来的结果取代、移到仓库根目录 <code>obsolete/</code> 的运行，见 %s"
             "（那里也放着 2026 年 10 月 AnnoForge 实验的数据快照 <code>obsolete/data/annoforge/</code>）。</p>"
             % link("obsolete/README.md", "obsolete/README.md"))
    rows = []
    for sub in SUBS:
        r = [NAME[sub]]
        for docs in (ZH, EN):
            x = m("api", sub, "gpt-6-astra-medium", docs, OBS)
            r += [fmt(x and x["Smatch F"]), fmt(x and x.get("AnCast Comprehensive")), fmt(x and x["juːmæʧ F"]),
                  fmt(x and x["juːmæʧ R"]), fmt(x and x["juːmæʧ P"])]
        r.append(H(link(run_dir("api", sub, "gpt-6-astra-medium", OBS), "目录")))
        rows.append(r)
    P.append(table(["条件", "中文 Smatch F", "AnCast++ 综合", "juːmæʧ F", "J R", "J P", "英文 Smatch F", "AnCast++ 综合",
                    "juːmæʧ F", "J R", "J P", "结果目录"], rows,
                   title="gpt-6-astra（effort medium，现在的 prompt）：后来改用 gpt-6.1-sol"))
    for lang, ds in (("中文（zh-0028 + zh-0032）", ZH), ("英文（en-0008）", EN)):
        P.append(md_table(B.table([("gpt-6-astra %s" % B.SHORT[s], "api", s, "gpt-6-astra-medium") for s in SUBS], ds,
                                  root=OBS), "%s：gpt-6-astra 的分项" % lang))
    v1 = v1_autoaligned()
    rows = []
    for sub in SUBS:
        x = m("api", sub, CLAUDE, ZH)
        rows.append([NAME[sub], fmt(v1[sub]), fmt(x and x["juːmæʧ F"]),
                     fmt(x["juːmæʧ F"] - v1[sub] if x else None, signed=True),
                     H(link(run_dir("api", sub, "claude-opus-5-5", OBS), "目录"))])
    P.append(table(["条件", "v1：原 prompt（要模型写对齐）", "v2：现在的 prompt（不写对齐，强调尽量正确、多查）", "差", "v1 结果目录"],
                   rows, title="prompt 的第一版（Claude API，中文，juːmæʧ F）",
                   note="v1 的回答在这里去掉模型自己写的对齐、改用自动对齐重新打分，所以两列可以直接比较。只改措辞，"
                        "同一篇的分数就会变 0.4–4.6 分，可以当作随机波动的一个参考。"))

    # ---------------------------------------------------------------- caveats
    P.append('<h2 id="caveats">局限</h2><ul>'
             "<li>3 篇文件、每个条件跑一次：没有量过同一条件重复跑的波动，也没有置信区间。</li>"
             "<li>effort 都是 medium；Claude 查资源的次数很少，资源条件的对照因此偏弱。</li>"
             "<li>juːmæʧ 依赖自动对齐：gold 的图配自动对齐，中文 87.4、英文 65.9（英文 gold 自己的对齐有不少错位），英文的 juːmæʧ 因此偏低；"
             "Smatch 和 AnCast++ 不受对齐影响。</li></ul>")

    page = ("<!DOCTYPE html>\n<html lang=\"zh\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" "
            "content=\"width=device-width, initial-scale=1\"><title>UMR 标注实验结果</title><style>%s%s</style></head>"
            "<body>\n%s\n<script>%s</script></body></html>\n" % (CSS, C.CSS, "\n".join(P), C.JS))
    with open(os.path.join(EXP, "report.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote exp/report.html (%d characters)" % len(page))


if __name__ == "__main__":
    main()
