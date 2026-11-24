"""The review items of a document: check them, and build the report, the points and the proposals from them.

    python3 pipeline/items.py check review/items/zh-0005.01-12.json     check one part (what a reviewer runs)
    python3 pipeline/items.py build                                      all parts -> review/reports/<doc>.md,
                                                                         review/points/<doc>.json,
                                                                         review/proposals/<doc>.json

A part file is review/items/<doc>.<from>-<to>.json: a list of items, one per comparison point:

    {"sent": 3, "n": 1, "topic": "「进口」的来源国", "cat": "role",
     "choices": [{"label": ":source 日本", "systems": ["gold", "s1f/r1"], "status": "bad", "grep": ":source"},
                 {"label": ":ARG2 日本", "systems": ["s1f/r2", "s3/r1", "s3/r2", "a2/r1", "a2/r2"], "status": "ok",
                  "grep": ":ARG2"}],
     "best": ":ARG2 日本",
     "text": "PropBank 进口.01 的 ARG2 是来源……",
     "fix": {"title": "进口来源国：:source → :ARG2", "conf": "high", "why": "……",
             "ops": [{"op": "mod_rel", "s": "s3x15", "r": "source", "t": "s3c2", "r2": "ARG2"}]}}

"fix" is null when the gold stays as it is.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import umrdoc  # noqa: E402

CATS = ["sense", "role", "concept", "structure", "attr", "doc-temporal", "doc-modal", "doc-coref"]
STATUS = ["ok", "minor", "bad", "open"]
def names_of(d):
    """gold and the systems that have an output for the document (the baseline has none for a non-test one)."""
    return ["gold"] + [k for k, _, _, rd in C.systems() if os.path.exists(os.path.join(rd, d["doc"] + ".umr"))]


ALL = ["gold"] + [k for k, *_ in C.systems()]
ITEMS = os.path.join(C.PKG, "review", "items")
MARK = {"ok": "✓", "minor": "△", "bad": "✗", "open": "？"}


def blocks(d):
    """annotation key -> sentence number -> the text of the sentence (graph + document level)."""
    out = {}
    files = [("gold", C.gold_path(d))] + [(k, os.path.join(rd, d["doc"] + ".umr")) for k, _, _, rd in C.systems()]
    for key, path in files:
        if not os.path.exists(path):
            continue
        out[key] = {s["index"]: s["gold"][umrdoc.SECTIONS[0]] + "\n" + s["gold"][umrdoc.SECTIONS[2]]
                    for s in umrdoc.load(path)["sents"]}
    return out


def part_name(path):
    m = re.match(r"([a-z]+-\d+)\.(\d+)-(\d+)\.json$", os.path.basename(path))
    if not m:
        raise SystemExit("a part file is named <doc>.<from>-<to>.json, e.g. zh-0005.01-12.json: %s" % path)
    return m.group(1), int(m.group(2)), int(m.group(3))


def proposals_of(doc, items):
    out, count = {}, {}
    for x in items:
        f = x.get("fix")
        if not f:
            continue
        k = count[x["sent"]] = count.get(x["sent"], 0) + 1
        best = next((c for c in x["choices"] if c["label"] == x.get("best")), None)
        p = {"id": "%s.s%d.p%d" % (doc, x["sent"], k), "title": f.get("title", x["topic"]), "refs": ["F%d" % x["n"]],
             "conf": f.get("conf"), "why": f.get("why") or x["text"],
             "support": [s for s in (best["systems"] if best else []) if s != "gold"], "ops": f.get("ops", [])}
        if f.get("excl"):
            p["excl"] = f["excl"]
        out.setdefault(str(x["sent"]), []).append(p)
    return out


def check(path):
    doc, lo, hi = part_name(path)
    d = C.docs(doc)[0]
    try:
        items = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        raise SystemExit("not valid JSON: %s" % e)
    B = blocks(d)
    ALL = names_of(d)
    errs, warns, seen = [], [], set()
    weak, nchoice, nogrep = [], 0, 0
    for idx, x in enumerate(items):
        tag = "item #%d (第 %s 句（%s）)" % (idx + 1, x.get("sent"), x.get("n"))
        for f in ("sent", "n", "topic", "cat", "choices", "text"):
            if not x.get(f):
                errs.append("%s: missing %s" % (tag, f))
        if "best" not in x or "fix" not in x:
            errs.append("%s: needs both \"best\" (a label or null) and \"fix\" (an object or null)" % tag)
        if errs and errs[-1].startswith(tag):
            continue
        if not isinstance(x["sent"], int) or not lo <= x["sent"] <= hi:
            errs.append("%s: sent must be a number from %d to %d" % (tag, lo, hi))
            continue
        if (x["sent"], x["n"]) in seen:
            errs.append("%s: the same sentence and n twice" % tag)
        seen.add((x["sent"], x["n"]))
        if x["cat"] not in CATS:
            errs.append("%s: cat must be one of %s" % (tag, ", ".join(CATS)))
        got, labels = [], []
        for c in x["choices"]:
            labels.append(c.get("label"))
            if c.get("status") not in STATUS:
                errs.append("%s: status of %r must be one of %s" % (tag, c.get("label"), ", ".join(STATUS)))
            got += c.get("systems", [])
            g = c.get("grep") or []
            nchoice += 1
            nogrep += 0 if g else 1
            others = [s for c2 in x["choices"] if c2 is not c for s in c2.get("systems", [])]
            for needle in ([g] if isinstance(g, str) else g):
                also = [s for s in others if s in B and needle in B[s].get(x["sent"], "")]
                if also and len(x["choices"]) > 1:
                    weak.append("%s: grep %r of %r is also in %s" % (tag, needle, c.get("label"), "、".join(also)))
                for s in c.get("systems", []):
                    if s in B and needle not in B[s].get(x["sent"], ""):
                        errs.append("%s: choice %r lists %s, but %r is not in %s's annotation of the sentence "
                                    "(wrong system, or wrong grep text)" % (tag, c.get("label"), s, needle, s))
        if len(set(labels)) != len(labels):
            errs.append("%s: two choices with the same label" % tag)
        for s in ALL:
            if got.count(s) != 1:
                errs.append("%s: %s must be in exactly one choice (it is in %d)" % (tag, s, got.count(s)))
        for s in got:
            if s not in ALL:
                errs.append("%s: unknown annotation %r (the names are %s)" % (tag, s, ", ".join(ALL)))
        if x["best"] is not None and x["best"] not in labels:
            errs.append("%s: best must be the label of a choice, or null" % tag)
        gold = next((c for c in x["choices"] if "gold" in c.get("systems", [])), None)
        f = x["fix"]
        if f:
            for k in ("title", "conf", "why", "ops"):
                if not f.get(k):
                    errs.append("%s: fix needs %s" % (tag, k))
            if f.get("conf") not in ("high", "mid", "low"):
                errs.append("%s: fix.conf must be high, mid or low" % tag)
            elif f["conf"] != "low" and gold and gold.get("status") == "ok":
                errs.append("%s: a fix with conf %s, but the gold's choice has status ok; make the status minor or "
                            "bad, or the conf low" % (tag, f["conf"]))
            if gold and x["best"] == gold.get("label"):
                errs.append("%s: there is a fix, but best is the gold's own choice" % tag)
        elif gold and gold.get("status") == "bad":
            warns.append("%s: the gold's choice is bad, but there is no fix (write one if the change can be expressed "
                         "in ops)" % tag)
    for i in range(lo, hi + 1):
        if not any(x.get("sent") == i for x in items):
            warns.append("第 %d 句 has no item" % i)
    if not errs:
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as t:
            json.dump(proposals_of(doc, items), t, ensure_ascii=False)
        r = subprocess.run(["node", os.path.join(C.PKG, "review", "validate.js"), doc, "--file", t.name, "--quiet"],
                           capture_output=True, text=True)
        os.unlink(t.name)
        if r.returncode:
            errs.append("the fixes do not all apply to the gold (ids are <doc>.s<sentence>.p<k>, the k-th fix of the "
                        "sentence):\n" + r.stdout.strip())
        else:
            print(r.stdout.strip().splitlines()[-1])
    for w in warns:
        print("warning:", w)
    for e in errs:
        print("ERROR:", e)
    print("%d of %d choices have no grep; %d grep texts are also found in annotations of another choice (they "
          "prove little; fine when the text is only meant to show the value is there)" % (nogrep, nchoice, len(weak)))
    if "--weak" in sys.argv:
        for w in weak:
            print("weak:", w)
    nfix = sum(1 for x in items if x.get("fix"))
    print("%d items, %d fixes, %d errors, %d warnings" % (len(items), nfix, len(errs), len(warns)))
    sys.exit(1 if errs else 0)


def build():
    parts = {}
    for name in sorted(os.listdir(ITEMS)):
        if name.endswith(".json") and not name.endswith(".s0.json"):
            doc, lo, hi = part_name(name)
            parts.setdefault(doc, []).append((lo, json.load(open(os.path.join(ITEMS, name), encoding="utf-8"))))
    total = 0
    for d in C.DOCS:
        doc = d["doc"]
        if doc not in parts:
            continue
        items = sorted((x for _, lst in sorted(parts[doc], key=lambda p: p[0]) for x in lst), key=lambda x: (x["sent"], x["n"]))
        words = {s["index"]: " ".join(s["words"]) for s in umrdoc.load(C.gold_path(d))["sents"]}
        lines = ["# Diff of %s" % doc, "",
                 "> 对比 gold 和各系统（s0 = 一句话 guideline 的 baseline，s1f = s1-full，s3 = s3-all，a2 = a2-sentence-all；r1、r2 是同一设定的两次运行）。"
                 "每条先列各标注的选择，记号：✓ 正确，△ 可接受但略差，✗ 错，？ 定不了。", ""]
        cur = None
        for x in items:
            if x["sent"] != cur:
                cur = x["sent"]
                lines += ["## 第 %d 句" % cur, "", "> " + words.get(cur, ""), ""]
            ch = "；".join("%s %s〔%s〕" % (MARK[c["status"]], c["label"], "、".join(c["systems"])) for c in x["choices"])
            tag = ""
            if x.get("fix"):
                tag = "【gold 有问题】" if x["fix"].get("conf") != "low" else "【值得商榷】"
            lines += ["（%d）**%s**%s　%s。%s" % (x["n"], x["topic"], tag, ch, x["text"]), ""]
        notes = os.path.join(ITEMS, doc + ".notes.md")
        with open(os.path.join(C.PKG, "review", "reports", doc + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        pts = [{"sent": x["sent"], "item": str(x["n"]), "topic": x["topic"], "cat": x["cat"],
                "choices": [{"label": c["label"], "systems": c["systems"], "status": c["status"]} for c in x["choices"]],
                "gold_fix": bool(x.get("fix") and x["fix"].get("conf") != "low"), "best": x.get("best")} for x in items]
        with open(os.path.join(C.PKG, "review", "points", doc + ".json"), "w", encoding="utf-8") as f:
            json.dump(pts, f, ensure_ascii=False, indent=1)
        with open(os.path.join(C.PKG, "review", "proposals", doc + ".json"), "w", encoding="utf-8") as f:
            json.dump(proposals_of(doc, items), f, ensure_ascii=False, indent=1)
        total += len(items)
        print("%s: %d items, %d fixes" % (doc, len(items), sum(1 for x in items if x.get("fix"))))
    print("%d items in %d documents" % (total, len(parts)))


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "check":
        check(sys.argv[2])
    elif len(sys.argv) >= 2 and sys.argv[1] == "build":
        build()
    else:
        raise SystemExit(__doc__)
