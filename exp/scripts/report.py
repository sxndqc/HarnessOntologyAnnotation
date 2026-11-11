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

RUNS = os.path.join(EXP, "runs")
ZH, EN = ["zh-0028", "zh-0032"], ["en-0008"]
DOCS = ZH + EN
SUBS = B.SUBS
NAME = {"s1-abridged": "s1-abridged：缩略版 guideline", "s1-full": "s1-full：完整 guideline",
        "s2-search": "s2-search：缩略版 + guideline 搜索", "s2-propbank": "s2-propbank：缩略版 + PropBank",
        "s2-gold": "s2-gold：缩略版 + gold 例子", "a1-sentence-propbank": "a1：PropBank，一句句跑（ablation）"}
CLAUDE, SOL, ASTRA = "claude-opus-5-5-v2", "gpt-6.1-sol-medium", "gpt-6-astra-medium"


def e(x):
    return html.escape(str(x))


def fmt(x, signed=False):
    if x is None:
        return "–"
    return ("%+.1f" % x) if signed else ("%.1f" % x)


def m(method, sub, label, docs):
    s = B.load(method, sub, label)
    if s is None:
        return None
    r, have = B.metrics(s, docs)
    return r if r is not None and len(have) == len(docs) else None


def table(head, rows, best=None, note=None):
    """rows: [[cell, ...]]; best: indices of columns among which the highest number of a row is bold."""
    out = ["<table>", "<thead><tr>" + "".join("<th>%s</th>" % e(h) for h in head) + "</tr></thead><tbody>"]
    for r in rows:
        cells = list(r)
        if best:
            vals = [(float(cells[i]), i) for i in best if re.match(r"^[+-]?\d+(\.\d+)?$", str(cells[i]))]
            if len(vals) > 1:
                top = max(v for v, _ in vals)
                cells = [("<b>%s</b>" % e(c)) if i in best and re.match(r"^[+-]?\d+(\.\d+)?$", str(c))
                         and float(c) == top else e(c) for i, c in enumerate(cells)]
            else:
                cells = [e(c) for c in cells]
        else:
            cells = [e(c) for c in cells]
        cls = ' class="sep"' if str(r[0]).startswith("对照") else ""
        out.append("<tr%s>" % cls + "".join("<td>%s</td>" % c for c in cells) + "</tr>")
    out.append("</tbody></table>")
    if note:
        out.append('<p class="note">%s</p>' % note)
    return "\n".join(out)


def md_table(lines):
    """A Markdown table of breakdown.table() as HTML."""
    if not lines:
        return "<p>（没有数据）</p>"
    head = [c.strip() for c in lines[0].strip("|").split("|")]
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines[2:]]
    return table(head, rows, best=None)


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
            raw = open(os.path.join(RUNS, "api", sub, "claude-opus-5-5", d + ".raw.txt"), encoding="utf-8").read()
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
@media (prefers-color-scheme: dark){body{background:#111;color:#e6e6e6} th{background:#222} th,td{border-color:#333}
 tr.sep td{background:#181818;color:#999} code{background:#222} .note,.lead{color:#aaa} h2{border-color:#333}}
"""


def main():
    import subprocess
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=EXP, capture_output=True, text=True).stdout.strip()
    P = []
    P.append("<h1>UMR 整篇文档标注实验：目前为止的全部结果</h1>")
    P.append('<p class="lead">HarnessOntologyAnnotation <code>exp/</code>，提交 <code>%s</code>，由 <code>python3 exp/scripts/report.py</code> '
             "从仓库里的分数和记录生成。测试数据和打分方式与 DMR 2026 UMR parsing shared task 一致（UMR 2.2 官方测试集和 gold）。</p>" % e(commit))
    P.append("<nav>" + "".join('<a href="#%s">%s</a>' % (a, t) for a, t in [
        ("summary", "要点"), ("setup", "设定"), ("main", "主表"), ("methods", "三种方法"), ("chat", "chat"),
        ("prompt", "prompt 版本"), ("breakdown", "分项"), ("ablation", "ablation"), ("usage", "工具与用量"),
        ("caveats", "局限"), ("files", "文件")]) + "</nav>")

    # ---------------------------------------------------------------- summary
    P.append('<h2 id="summary">要点</h2><ul>')
    P += ["<li><b>样本很小</b>：只有 3 篇测试文件（中文 zh-0028、zh-0032，共 18 句；英文 en-0008，9 句），每个条件只跑一次。"
          "下面几分以内的差别都在噪声范围里；中文 15 篇、英文 5 篇的全量还没跑。</li>",
          "<li><b>所有 LLM 设置都明显高于两支参赛队伍</b>：这三篇上 juːmæʧ 中文 41.8–50.9（最低的是 Claude Code 的 s1-full），"
          "参赛队伍 32.0、32.2；英文 44.6–59.2，参赛队伍 41.0、35.6。</li>",
          "<li><b>五个条件之间总分差别很小</b>（Claude API 中文 48.1–50.0）；资源的作用在分项里：PropBank 让谓词义项和核心角色标签提高"
          " 9–17 分，gold 例子让共指和人称/数提高，guideline 搜索让角色标签提高约 10 分；几乎所有资源都让文档级模态关系略降。</li>",
          "<li><b>Claude 三种方法（API、Claude Code、claude.ai chat）总分基本一样</b>；Claude Code 的 s1-full 偏低（41.8）。</li>",
          "<li><b>GPT（gpt-6.1-sol）和 Claude 总分接近</b>：中文每个条件都是 Claude 略高（差 0.6–4.3）；英文各有高低，"
          "GPT 拿到完整 guideline（full、+search）后高于 Claude。GPT 调用工具的次数是 Claude 的几倍到几十倍，但分数没有因此更高。</li>",
          "<li><b>一句句跑的 ablation</b>（a1）和整篇一次标的 s2-propbank 总分相差 2 分以内。</li>",
          "<li><b>对齐不让模型写，由程序自动生成</b>：gold 的图配自动对齐，中文 juːmæʧ 87.4、英文 65.9（英文 gold 自己的对齐有不少错位）。"
          "自动对齐比模型自己写的对齐还好（同样的图高 3–9 分）。</li>"]
    P.append("</ul>")

    # ---------------------------------------------------------------- setup
    P.append('<h2 id="setup">设定</h2>')
    P.append(table(["测试文件", "语言", "句数", "词数"], [["zh-0028", "中文", 12, 250], ["zh-0032", "中文", 6, 187],
                                                    ["en-0008", "英文", 9, 140]]))
    P.append("<h3>条件（子实验）</h3>")
    P.append(table(["条件", "给模型的资源"], [
        ["s1-abridged", "缩略版 guideline（1.4 万字符）"], ["s1-full", "完整 guideline（36.6 万字符）"],
        ["s2-search", "缩略版 + search_guidelines 工具（搜完整 guideline）"],
        ["s2-propbank", "缩略版 + propbank_lookup 工具"],
        ["s2-gold", "缩略版 + search_annotations 工具（shared task 训练数据的 gold，不含测试句子）"],
        ["a1-sentence-propbank", "s2-propbank 的资源，一句句跑：先每句单独标句子图；全部标完后，每句再给它和前五句的原文与图，标这一句的文档级关系"]]))
    P.append("<h3>方法和模型</h3>")
    P.append(table(["方法", "模型 / 标签", "说明"], [
        ["API", "claude-opus-5-5（标签 claude-opus-5-5-v2）", "effort medium，adaptive thinking；不开拒答回退，每个回答都出自这个模型"],
        ["API", "gpt-6.1-sol（gpt-6.1-sol-medium）", "OpenAI Responses API，reasoning effort medium，同样的 prompt、工具和循环"],
        ["API", "gpt-6-astra（gpt-6-astra-medium）", "同上，先跑的另一个 GPT 模型，作参考"],
        ["Claude Code", "claude-opus-5-5（claude-code）", "订阅；每篇一个工作目录（TASK.md + guideline 文件 + 工具命令），只能读本目录、运行工具、写 answer.txt"],
        ["chat", "claude.ai（claude-ai）", "人工把 prompt 贴进 chat 窗口，附件代替工具"],
        ["chat", "ChatGPT（chatgpt、chatgpt-6-astra-high）", "同上"]]))
    P.append("<h3>打分</h3><ul>"
             "<li><b>juːmæʧ</b>（主指标，umrtools compare_umr.pl）和 <b>Smatch</b>；中文两篇把计数加总再算 F1。</li>"
             "<li><b>AnCast++</b>（Modal、Temporal、Coref、Comprehensive）和 <b>umrjudge</b>（25 项分项检查，见分项一节）作补充。</li>"
             "<li><b>对齐</b>：模型只写图，词对齐由 <code>lib/autoalign.py</code> 按 gold 的对齐方式生成（概念等于句中的词就对齐到这个词，"
             "有名字的实体对齐到名字的词，英文另加词形变化）。</li></ul>")
    P.append("<h3>打分核对：重算两支参赛队伍的输出，和概述论文对照</h3>")
    vr = []
    for line in open(os.path.join(RUNS, "shared-task", "verify.md"), encoding="utf-8"):
        if line.startswith("| orange") or line.startswith("| sema"):
            vr.append([c.strip() for c in line.strip().strip("|").split("|")])
    P.append(table(["系统", "语言", "juːmæʧ（这里）", "论文表 2", "Smatch（这里）", "论文表 5"], vr,
                   note="juːmæʧ 差 0.5 以内，Smatch 差 0.3 以内（Smatch 本身有随机性）。"))

    # ---------------------------------------------------------------- main
    P.append('<h2 id="main">主表：API，每个条件（juːmæʧ F / Smatch F）</h2>')
    rows = []
    for sub in B.API_SUBS:
        r = [NAME[sub]]
        for docs in (ZH, EN):
            for lab in (CLAUDE, SOL, ASTRA):
                x = m("api", sub, lab, docs)
                r += [fmt(x and x["juːmæʧ F"]), fmt(x and x["Smatch F"])]
        rows.append(r)
    for sysname in ("orange", "sema"):
        r = ["对照：参赛队伍 %s" % sysname.capitalize()]
        for docs in (ZH, EN):
            x = m("shared-task", "", sysname, docs)
            r += [fmt(x and x["juːmæʧ F"]), fmt(x and x["Smatch F"]), "", "", "", ""]
        rows.append(r)
    head = ["条件", "中文 Claude J", "S", "中文 GPT-sol J", "S", "中文 GPT-astra J", "S",
            "英文 Claude J", "S", "英文 GPT-sol J", "S", "英文 GPT-astra J", "S"]
    P.append(table(head, rows, best=[1, 3, 5],
                   note="J = juːmæʧ F，S = Smatch F。中文 = zh-0028 + zh-0032，英文 = en-0008。粗体：这一行中文三个模型里 juːmæʧ 最高的。"
                        "参赛队伍的英文列放在 Claude 的位置上，只作对照。"))

    # ---------------------------------------------------------------- methods
    P.append('<h2 id="methods">Claude 的三种方法：API、Claude Code、chat（juːmæʧ F）</h2>')
    rows = []
    for sub in SUBS:
        r = [NAME[sub]]
        for docs in (ZH, EN):
            for method, lab in (("api", CLAUDE), ("harness", "claude-code"), ("chat", "claude-ai")):
                s = B.load(method, sub, lab)
                if s is None:
                    r.append("–")
                    continue
                x, have = B.metrics(s, docs)
                if x is None:
                    r.append("–")
                else:
                    r.append(fmt(x["juːmæʧ F"]) + ("" if len(have) == len(docs) else "（仅 %s）" % ",".join(have)))
        rows.append(r)
    P.append(table(["条件", "中文 API", "中文 Claude Code", "中文 claude.ai", "英文 API", "英文 Claude Code", "英文 claude.ai"],
                   rows, note="Claude Code 没跑英文；chat 只做了 s1-abridged 和 s2-propbank。"))

    # ---------------------------------------------------------------- chat
    P.append('<h2 id="chat">chat 的每一份回答</h2>')
    rows = []
    for sub in SUBS:
        for lab in ("claude-ai", "chatgpt", "chatgpt-6-astra-high"):
            s = B.load("chat", sub, lab)
            if not s:
                continue
            for d in sorted(s):
                api = B.load("api", sub, CLAUDE) or {}
                rows.append([sub, lab, d, fmt(B.f1(*s[d]["jumach"])), fmt(B.f1(*s[d]["smatch"])),
                             "是" if s[d]["valid"]["passed"] else "否",
                             fmt(B.f1(*api[d]["jumach"])) if d in api else "–"])
    P.append(table(["条件", "chat 模型", "文件", "juːmæʧ F", "Smatch F", "通过格式检查", "同条件 Claude API 的 juːmæʧ"], rows,
                   note="格式检查是 umrtools validate.py --level 2；没通过的都是图里有环，gold 在同样的句子也有环，照常计分。"))

    # ---------------------------------------------------------------- prompt
    P.append('<h2 id="prompt">prompt 的两个版本（Claude API，中文，juːmæʧ F）</h2>')
    v1 = v1_autoaligned()
    rows = []
    for sub in SUBS:
        x = m("api", sub, CLAUDE, ZH)
        rows.append([NAME[sub], fmt(v1[sub]), fmt(x and x["juːmæʧ F"]),
                     fmt(x["juːmæʧ F"] - v1[sub] if x else None, signed=True)])
    P.append(table(["条件", "v1：原 prompt（要模型写对齐）", "v2：现在的 prompt（不写对齐，强调尽量正确、多查）", "差"], rows,
                   note="v1 的回答在这里去掉模型自己写的对齐、改用自动对齐重新打分，所以两列可以直接比较。只改措辞，"
                        "同一篇的分数就会变 0.4–4.6 分，可以当作随机波动的一个参考。"))

    # ---------------------------------------------------------------- breakdown
    P.append('<h2 id="breakdown">分项（umrjudge 每项检查、AnCast 各项）</h2>')
    P.append("<p>每一行是一项检查的正确率（%）；“相对 abridged”的表是每个条件减去同一模型 s1-abridged 的分差。"
             "同样的表也在 <code>exp/breakdown.md</code>。</p>")
    systems = [("Claude API", "api", CLAUDE), ("GPT API", "api", SOL)]
    for lang, ds in (("中文（zh-0028 + zh-0032）", ZH), ("英文（en-0008）", EN)):
        P.append("<h3>%s：每个条件的绝对分数</h3>" % lang)
        cols = [("%s %s" % (n, B.SHORT[s]), mm, s, l) for n, mm, l in systems for s in B.API_SUBS]
        P.append(md_table(B.table(cols, ds)))
        P.append("<h3>%s：相对 abridged 的变化</h3>" % lang)
        cols, delta = [], {}
        for n, mm, l in systems:
            cols.append(("%s %s" % (n, B.SHORT["s1-abridged"]), mm, "s1-abridged", l))
            for s in B.API_SUBS[1:]:
                h = "%s %s" % (n, B.SHORT[s])
                cols.append((h, mm, s, l))
                delta[h] = "%s %s" % (n, B.SHORT["s1-abridged"])
        P.append(md_table(B.table(cols, ds, delta)))
        P.append("<details><summary>%s：Claude 三种方法和 chat 的分项</summary>" % lang)
        cols = []
        for s in SUBS:
            cols += [("API %s" % B.SHORT[s], "api", s, CLAUDE), ("Claude Code %s" % B.SHORT[s], "harness", s, "claude-code"),
                     ("claude.ai %s" % B.SHORT[s], "chat", s, "claude-ai")]
        for lab in ("chatgpt-6-astra-high", "chatgpt"):
            cols += [("ChatGPT chat (%s) %s" % (lab, B.SHORT[s]), "chat", s, lab) for s in SUBS]
        P.append(md_table(B.table(cols, ds)) + "</details>")
        P.append("<details><summary>%s：gpt-6-astra 的分项</summary>" % lang)
        P.append(md_table(B.table([("gpt-6-astra %s" % B.SHORT[s], "api", s, ASTRA) for s in SUBS], ds)) + "</details>")

    # ---------------------------------------------------------------- ablation
    P.append('<h2 id="ablation">ablation：一句句跑（a1）对整篇一次标（s2-propbank）</h2>')
    for lang, ds in (("中文", ZH), ("英文", EN)):
        cols, delta = [], {}
        for n, mm, l in systems:
            cols += [("%s 整篇" % n, mm, "s2-propbank", l), ("%s 一句句（差）" % n, mm, "a1-sentence-propbank", l)]
            delta["%s 一句句（差）" % n] = "%s 整篇" % n
        P.append("<h3>%s</h3>" % lang + md_table(B.table(cols, ds, delta)))
    P.append('<p class="note">a1 每篇的调用次数 = 2 × 句数（Claude 和 GPT 各 54 次）；每次调用的 prompt 和完整对话在 '
             "<code>runs/api/a1-sentence-propbank/&lt;标签&gt;/&lt;文件&gt;.calls/</code>。</p>")

    # ---------------------------------------------------------------- usage
    P.append('<h2 id="usage">工具调用和用量</h2>')
    rows = []
    for sub in B.API_SUBS:
        for title, method, lab in (("Claude API", "api", CLAUDE), ("GPT-sol API", "api", SOL),
                                   ("GPT-astra API", "api", ASTRA), ("Claude Code", "harness", "claude-code")):
            st = trace_stats(method, sub, lab, DOCS)
            if not any(st):
                continue
            tools = " / ".join("–" if x is None else str(x[0]) for x in st)
            reqs = " / ".join("–" if x is None else str(x[1]) for x in st)
            outp = sum(x[2] for x in st if x)
            costs = [x[3] for x in st if x and x[3] is not None]
            rows.append([NAME[sub], title, tools, reqs, "%d" % outp, ("$%.2f" % sum(costs)) if costs else "–"])
    P.append(table(["条件", "系统", "工具调用（zh-0028 / zh-0032 / en-0008）", "请求数或轮数", "输出 token 合计", "花费"], rows,
                   note="花费：Claude API 按 Opus 5.5 的价格算（输入 $4、输出 $20、写缓存 $5、读缓存 $0.20，每百万 token）；"
                        "Claude Code 是它自己报的 API 价格折算（实际走订阅）；GPT 没有算钱，以 OpenAI 控制台为准。"
                        "Claude Code 的工具调用只数运行 tools/ 命令的次数（不算 Read、Grep 等）。"))

    # ---------------------------------------------------------------- caveats
    P.append('<h2 id="caveats">局限和下一步</h2><ul>'
             "<li>3 篇文件、每个条件跑一次：没有量过同一条件重复跑的波动，也没有置信区间。</li>"
             "<li>effort 都是 medium；模型查资源的次数（尤其 Claude）很少，资源条件的对照因此偏弱。</li>"
             "<li>英文的自动对齐上限只有 65.9（中文 87.4），英文的 juːmæʧ 会因此偏低；Smatch 不受对齐影响。</li>"
             "<li>下一步建议：中文 15 篇全量（API 和 Claude Code），同一条件重复 2–3 次量波动，按文件 bootstrap 求置信区间，"
             "以及让模型真正去查资源（调高 effort 或在 prompt 里规定每句都查）。</li></ul>")

    # ---------------------------------------------------------------- files
    P.append('<h2 id="files">文件</h2><ul>'
             "<li>prompt：<code>exp/api/&lt;条件&gt;/…/skill.md</code>、<code>exp/chat/&lt;条件&gt;/prompts/</code>、"
             "<code>exp/harness/&lt;条件&gt;/TASK.md</code>，都由 <code>exp/scripts/make_subexps.py</code> 生成。</li>"
             "<li>API 的结果：<code>exp/runs/api/&lt;条件&gt;/&lt;标签&gt;/</code>，每篇有回答原文、打分用的 .umr、实际发出的 prompt"
             "（<code>.prompt.md</code>）和完整对话（<code>.transcript.json</code>）。</li>"
             "<li>Claude Code：<code>exp/harness/&lt;条件&gt;/answers/claude-code/</code>（答案、命令和权限、完整会话记录）。</li>"
             "<li>chat：<code>exp/chat/&lt;条件&gt;/answers/&lt;chat 模型&gt;/</code>。</li>"
             "<li>分项表：<code>exp/breakdown.md</code>；本页：<code>exp/report.html</code>（<code>python3 exp/scripts/report.py</code>）。</li></ul>")

    page = ("<!DOCTYPE html>\n<html lang=\"zh\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" "
            "content=\"width=device-width, initial-scale=1\"><title>UMR 标注实验结果</title><style>%s</style></head>"
            "<body>\n%s\n</body></html>\n" % (CSS, "\n".join(P)))
    with open(os.path.join(EXP, "report.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote exp/report.html (%d characters)" % len(page))


if __name__ == "__main__":
    main()
