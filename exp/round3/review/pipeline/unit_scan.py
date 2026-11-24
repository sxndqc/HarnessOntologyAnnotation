"""For the classifier rule: where the annotations of a document have :unit, and the review items about it.

    python3 pipeline/unit_scan.py zh-0005

Part 1, per sentence that has a :unit anywhere or a review item about classifiers: the tokens, the :unit
concepts of the gold and of each system (with the node they hang on).
Part 2: the review items that mention 量词 or :unit, with file, position in the file, choices and fix.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import umrdoc  # noqa: E402

d = C.docs(sys.argv[1])[0]
files = [("gold", C.gold_path(d))] + [(k, os.path.join(rd, d["doc"] + ".umr")) for k, _, _, rd in C.systems()]
units, words = {}, {}
for key, path in files:
    for s in umrdoc.load(path)["sents"]:
        g = s["gold"][umrdoc.SECTIONS[0]]
        if key == "gold":
            words[s["index"]] = " ".join("%d:%s" % (i + 1, w) for i, w in enumerate(s["words"]))
        lines = g.splitlines()
        for i, l in enumerate(lines):
            m = re.search(r":unit\s+\(?\s*(\S+)\s*/\s*([^\s()]+)|:unit\s+([^\s()]+)", l)
            if m:
                ind = len(l) - len(l.lstrip())
                par = next((re.search(r"/\s*([^\s()]+)", p).group(1) for p in reversed(lines[:i])
                            if len(p) - len(p.lstrip()) < ind and "/" in p), "?")
                units.setdefault(s["index"], {}).setdefault(key, []).append("%s←%s" % (m.group(2) or m.group(3), par))
items = []
for f in sorted(glob.glob(os.path.join(C.PKG, "review", "items", d["doc"] + ".*.json"))):
    for i, x in enumerate(json.load(open(f, encoding="utf-8"))):
        blob = x["topic"] + x["text"] + " ".join(c["label"] for c in x["choices"]) + ((x.get("fix") or {}).get("title") or "")
        if "量词" in blob or ":unit" in blob or '"unit"' in json.dumps((x.get("fix") or {}).get("ops", [])):
            items.append((os.path.basename(f), i, x))
sents = sorted(set(units) | {x["sent"] for _, _, x in items})
print("===== 第 1 部分：各标注里的 :unit（量词←所挂的节点）")
for n in sents:
    print("\n第 %d 句  %s" % (n, words.get(n, "")))
    for key, _ in files:
        print("  %-7s %s" % (key, "，".join(units.get(n, {}).get(key, [])) or "—"))
print("\n===== 第 2 部分：提到量词或 :unit 的条目（%d 个）" % len(items))
for name, i, x in items:
    print("\n[%s #%d] 第 %d 句（%d）%s  cat=%s best=%s" % (name, i, x["sent"], x["n"], x["topic"], x["cat"], x.get("best")))
    for c in x["choices"]:
        print("    %s  %s  〔%s〕" % (c["status"], c["label"], "、".join(c["systems"])))
    print("    text: " + x["text"][:300])
    if x.get("fix"):
        print("    fix(%s): %s  ops=%s" % (x["fix"]["conf"], x["fix"]["title"], json.dumps(x["fix"]["ops"], ensure_ascii=False)))
