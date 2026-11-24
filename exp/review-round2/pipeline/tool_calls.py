"""The tool calls of every session, per tool, from the session transcripts.

    python3 pipeline/tool_calls.py    -> analysis/tool-calls.md (summary) and analysis/tool-calls.csv (every call)

A call is one run of tools/propbank_lookup.py, tools/search_guidelines.py or tools/search_annotations.py in a
command of a session (runs/<condition>/<run>/<doc>.transcript.jsonl, and <doc>.calls/*.transcript.jsonl for
the sentence-by-sentence condition). A shell command with several runs counts each. Where a session called
the tools from a Python loop, the number of runs is taken from the loop's list of terms and marked as
estimated. The total per session is checked against "lookups" in the meta files (the runner's own count).
"""
import collections
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

TOOLS = ["propbank_lookup", "search_guidelines", "search_annotations"]
RUN = re.compile(r"python3?\s+(?:\./)?tools/(%s)\.py([^;|&\n]*)" % "|".join(TOOLS))


def calls_of(cmd):
    """[(tool, arguments, estimated?)] of one command."""
    m = re.match(r"^/bin/\w+ -lc (['\"])(.*)\1$", cmd, re.S)
    body = m.group(2) if m else cmd
    if "subprocess" in body or re.search(r"<<\s*'?PY", body):
        tools = [t for t in TOOLS if t in body]
        if not tools:
            return []
        n = 0
        for lst in re.findall(r"for\s+\w+(?:\s*,\s*\w+)*\s+in\s+\[(.*?)\]\s*:", body, re.S):
            n += max(1, len(re.findall(r"'[^']*'|\"[^\"]*\"|\(|\[", lst)) if "(" in lst or "[" in lst else len(re.findall(r"'[^']*'|\"[^\"]*\"", lst)))
        if not n:
            n = len(re.findall(r"subprocess\.\w+\(", body)) or 1
        return [(t, "(from a Python loop)", True) for t in tools for _ in range(max(1, n // len(tools)) if len(tools) > 1 else n)]
    return [(t, a.strip().strip("'\""), False) for t, a in RUN.findall(body)]


def main():
    rows, by, est, sess = [], collections.Counter(), collections.Counter(), collections.Counter()
    meta_total, lemmas = collections.Counter(), collections.Counter()
    for key, cond, m, run_dir in C.systems():
        files = glob.glob(os.path.join(run_dir, "*.transcript.jsonl")) + glob.glob(os.path.join(run_dir, "*.calls", "*.transcript.jsonl"))
        for mf in glob.glob(os.path.join(run_dir, "*.meta.json")):
            meta_total[key] += json.load(open(mf)).get("lookups", 0) or 0
        for p in sorted(files):
            rel = os.path.relpath(p, run_dir)
            doc = rel[:7]
            part = os.path.basename(p).split(".")[0] if ".calls" in rel else "doc"
            sess[key] += 1
            for line in open(p, encoding="utf-8"):
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                it = e.get("item") or {}
                if e.get("type") != "item.completed" or it.get("type") != "command_execution":
                    continue
                for tool, args, guess in calls_of(it.get("command", "")):
                    by[(key, tool)] += 1
                    by[(key, doc, tool)] += 1
                    by[(key, "pass:" + ("doc" if part == "doc" else part[0]), tool)] += 1
                    est[key] += guess
                    if tool == "propbank_lookup" and not guess:
                        lemmas[key] += len([x for x in args.replace("--language zh", "").split() if not x.startswith("-")])
                    rows.append([key, doc, part, tool, args[:300], "estimated" if guess else "", len(it.get("aggregated_output") or ""),
                                 it.get("exit_code")])
    os.makedirs(C.ANALYSIS, exist_ok=True)
    with open(os.path.join(C.ANALYSIS, "tool-calls.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["system", "doc", "session", "tool", "arguments", "estimated", "output_chars", "exit_code"])
        w.writerows(rows)
    keys = [k for k, *_ in C.systems()]
    L = ["# 工具调用记录（按工具分）", "",
         "从会话记录里数出来的：一次调用 = 一次运行 `tools/propbank_lookup.py`、`tools/search_guidelines.py` 或 "
         "`tools/search_annotations.py`。一条命令里连着运行几次的分别计数；`propbank_lookup` 一次可以查多个词，所以另列查词数。"
         "个别会话用 Python 循环批量调用工具，这部分的次数是按循环里的词表估的（\"估计\"一栏）。"
         "\"运行器计数\"是各会话 meta 文件里的 lookups（运行时由工具自己记的总数，不分工具），用来核对。每次调用的明细在 tool-calls.csv。", "",
         "| 系统 | 会话数 | propbank_lookup | 其中查词数 | search_guidelines | search_annotations | 合计 | 其中估计 | 运行器计数 |",
         "|---|---|---|---|---|---|---|---|---|"]
    for k in keys:
        tot = sum(by[(k, t)] for t in TOOLS)
        L.append("| %s | %d | %d | %d | %d | %d | %d | %d | %d |" % (k, sess[k], by[(k, "propbank_lookup")], lemmas[k],
                 by[(k, "search_guidelines")], by[(k, "search_annotations")], tot, est[k], meta_total[k]))
    L += ["", "## 逐句设定（a2）的两遍", "", "| 系统 | 哪一遍 | propbank_lookup | search_guidelines | search_annotations |", "|---|---|---|---|---|"]
    for k in keys:
        for ps, name in (("pass:g", "句子图"), ("pass:r", "文档级关系")):
            if any(by[(k, ps, t)] for t in TOOLS):
                L.append("| %s | %s | %d | %d | %d |" % (k, name, *[by[(k, ps, t)] for t in TOOLS]))
    L += ["", "## 按文档", "", "| 文档 | 句数 | " + " | ".join("%s P/G/A" % k for k in keys if sum(by[(k, t)] for t in TOOLS)) + " |",
          "|---|---|" + "---|" * sum(1 for k in keys if sum(by[(k, t)] for t in TOOLS))]
    for d in C.DOCS:
        L.append("| %s | %d | %s |" % (d["doc"], d["sents"], " | ".join(
            "/".join(str(by[(k, d["doc"], t)]) for t in TOOLS) for k in keys if sum(by[(k, t)] for t in TOOLS))))
    L += ["", "P/G/A = propbank_lookup / search_guidelines / search_annotations 的调用次数。"]
    with open(os.path.join(C.ANALYSIS, "tool-calls.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:22]))
    print("%d calls written to analysis/tool-calls.csv" % len(rows))


if __name__ == "__main__":
    main()
