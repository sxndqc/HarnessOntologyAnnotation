#!/usr/bin/env python3
"""Build review/umr-gold-review.html: gold + the system outputs + the diff report's items + gold fix proposals.

    python3 review/build.py [--docs zh-0028,zh-0032]

Reads, per document:
  data/gold/<gold name>.umr                        the gold being reviewed
  runs/<condition>/<model>-<effort>-<run>/<doc>.umr      the system outputs (config.json says which)
  review/reports/<doc>.md                          the diff report of the document (format: AGENTS.md, step 4);
                                                   <doc>.other.md, if there, is a second report (items cited as A<n>)
  review/proposals/<doc>.json                      the gold fix proposals (format: AGENTS.md, step 5)
  analysis/scores.json                             scores (pipeline/score.py), if there
A document is included when it has a report or proposals (or is named with --docs).
The page is one self-contained file: open it in a browser, accept or reject each proposal, export the revised
gold (<gold name>.revised.umr) and the decisions.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
import common as C  # noqa: E402

DIGITS = {c: i for i, c in enumerate("零一二三四五六七八九")}
DIGITS["〇"] = 0
DIGITS["两"] = 2


def number(s):
    """第十二句 / 第 12 句 -> 12."""
    s = s.strip()
    if s.isdigit():
        return int(s)
    n, cur = 0, 0
    for ch in s:
        if ch == "百":
            n += (cur or 1) * 100
            cur = 0
        elif ch == "十":
            n += (cur or 1) * 10
            cur = 0
        else:
            cur = DIGITS[ch]
    return n + cur


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def split_system(text):
    """sentence number -> {graph, al, doc} of a system output file."""
    out = {}
    parts = re.split(r"(?m)^# :: snt(\d+).*$", text)
    for i in range(1, len(parts), 2):
        body = re.sub(r"(?m)^#{20,}\s*\n?", "", parts[i + 1])
        body = re.sub(r"(?m)^# meta-info.*\n?", "", body)
        g = body.find("# sentence level graph:")
        a = body.find("# alignment:")
        d = body.find("# document level annotation:")
        if g < 0 or a < 0 or d < 0:
            out[int(parts[i])] = {"graph": body.strip(), "al": "", "doc": ""}
            continue
        out[int(parts[i])] = {
            "graph": body[g + len("# sentence level graph:"):a].strip(),
            "al": " | ".join(l.strip() for l in body[a + len("# alignment:"):d].strip().splitlines() if l.strip()),
            "doc": body[d + len("# document level annotation:"):].strip(),
        }
    return out


def parse_report(text, src, doc):
    """-> ({sentence: [{src, n, text}]}, summary markdown) of one document's report."""
    issues, summary = {}, []
    sent, cur, in_summary = None, None, False
    head_sent = re.compile(r"^#{2,3}\s*第\s*([零〇一二两三四五六七八九十百\d]+)\s*句")
    item = re.compile(r"^（(\d+)）")

    def flush():
        nonlocal cur
        if cur:
            cur["text"] = cur["text"].strip()
            issues.setdefault(sent, []).append(cur)
        cur = None

    for line in text.split("\n"):
        m = head_sent.match(line)
        if m:
            flush()
            sent, in_summary = number(m.group(1)), False
            continue
        if re.match(r"^#{1,3}\s", line) and not line.startswith("####"):
            flush()
            sent = None
            in_summary = "小结" in line or "summary" in line.lower()
            continue
        if sent is not None:
            m = item.match(line)
            if m:
                flush()
                cur = {"src": src, "n": int(m.group(1)), "text": line[m.end():].strip()}
            elif cur is not None and line.strip() not in ("---", ""):
                cur["text"] += "\n" + line.strip("　 ").rstrip()
        elif in_summary:
            summary.append(line)
    flush()
    return issues, "\n".join(summary).strip()


def doc_notes(d):
    """The reviewers' notes of the document (review/items/<doc>.<from>-<to>.notes.md) and its text repairs."""
    folder = os.path.join(HERE, "items")
    parts = []
    for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        m = re.match(r"%s\.(\d+)-(\d+)\.notes\.md$" % re.escape(d["doc"]), name)
        if m:
            body = re.sub(r"(?m)^#\s.*\n", "", read(os.path.join(folder, name)))
            parts.append("## 第 %d–%d 句\n\n%s" % (int(m.group(1)), int(m.group(2)), body.strip()))
    if parts and d.get("lang") == "zh" and d["doc"] not in ("zh-0026", "zh-0036"):
        parts.insert(0, "> 这些小结是第一轮审阅时写的。之后有两条规则做了统一更正：量词都保留为 :unit（小结里\"量词应去掉\"的说法作废）；"
                        ":part 以部分为父节点（小结里\":part 方向反\"的说法作废）。条目和方案已按更正后的规则处理。")
    rep = C.gold_text(d)[1]
    if rep:
        parts.insert(0, "## gold 文件的文本修补\n\n原始 gold 文件这几处格式不合法，审阅工具读不了，页面里显示和导出的是修补后的文本"
                        "（data/gold_text_repairs.json）：\n\n" + "\n".join("- 第 %d 行：%s" % (r["line"], r["why"]) for r in rep))
    return [("审阅小结", "\n\n".join(parts))] if parts else []


EXTRAS = [("总结", "SUMMARY.md"), ("错误类型", "error-patterns.md"), ("gold 错误统计", "gold-errors.md"),
          ("比较点：一致度、正确率、voting", "points.md"), ("AnCast 分数（按语言，修订前后）", "scores-by-language.md"), ("AnCast 分数（全部表）", "scores.md"), ("juːmæʧ（shared task 主指标）", "jumach.md"), ("分项 F1（各设定）", "breakdown.md"),
          ("AnCast 两两分数", "pairwise.md"), ("工具调用", "tool-calls.md")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="")
    a = ap.parse_args()
    systems = C.systems()
    sp = os.path.join(C.ANALYSIS, "scores.json")
    scores = json.loads(read(sp)) if os.path.exists(sp) else {}
    data = {"docs": [], "extras": [], "sys": [k for k, *_ in systems],
            "cond": {c["key"]: c["name"] for c in C.CONFIG["conditions"]},
            "srcNames": {"F": "报告", "A": "报告 2"}, "storageKey": "umr-gold-review-round2"}
    for title, name in EXTRAS:
        p = os.path.join(C.ANALYSIS, name)
        if os.path.exists(p):
            data["extras"].append({"title": title, "md": read(p)})
    want = [x for x in a.docs.split(",") if x]
    warnings = 0
    for d in C.DOCS:
        did = d["doc"]
        rp = os.path.join(HERE, "reports", did + ".md")
        pp = os.path.join(HERE, "proposals", did + ".json")
        if want and did not in want:
            continue
        if not want and not (os.path.exists(rp) or os.path.exists(pp)):
            continue
        outs = {}
        for key, _, _, run_dir in systems:
            p = os.path.join(run_dir, did + ".umr")
            if os.path.exists(p):
                outs[key] = split_system(read(p))
        props = json.loads(read(pp)) if os.path.exists(pp) else {}
        # 值得商榷（conf=low）的条目只保留问题描述，不给 gold 修改方案
        props = {k: [x for x in v if x.get("conf") != "low"] for k, v in props.items()}
        issues, summary = parse_report(read(rp), "F", did) if os.path.exists(rp) else ({}, "")
        issues = {str(k): v for k, v in issues.items()}
        op = os.path.join(HERE, "reports", did + ".other.md")      # a second, independent report of the document
        if os.path.exists(op):
            for k, v in parse_report(read(op), "A", did)[0].items():
                issues.setdefault(str(k), []).extend(v)
        data["docs"].append({
            "id": did, "goldName": d["gold"], "gold": C.gold_text(d)[0],
            "systems": {k: {str(n): v for n, v in s.items()} for k, s in outs.items()},
            "issues": issues, "proposals": props, "scores": scores.get(did, {}),
            "summaries": doc_notes(d),
        })
        ni = sum(len(v) for v in issues.values())
        npz = sum(len(v) for v in props.values())
        print("%s: %d systems, %d sentences with report items, %d items, %d proposals" % (did, len(outs), len(issues), ni, npz))
        for s, lst in props.items():
            keys = {x["src"] + str(x["n"]) for x in issues.get(s, [])}
            for p in lst:
                for r in p.get("refs", []):
                    if "§" not in r and r not in keys:
                        warnings += 1
                        print("   WARNING %s: ref %s is not an item of sentence %s in the report" % (p["id"], r, s))
    if not data["docs"]:
        raise SystemExit("no document has a report (review/reports/<doc>.md) or proposals yet")
    html = read(os.path.join(HERE, "template.html"))
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace("/*__ENGINE__*/", read(os.path.join(HERE, "engine.js")).replace("</", "<\\/"))
    html = html.replace("__DATA__", blob)
    out = os.path.join(HERE, "umr-gold-review.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %s, %d documents, %.0f KB, %d warnings" % (out, len(data["docs"]), len(html) / 1024, warnings))


if __name__ == "__main__":
    main()
