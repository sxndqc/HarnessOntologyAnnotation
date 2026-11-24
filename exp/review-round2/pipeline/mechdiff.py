"""A sentence as a mechanical diff: the gold graph, then only what the 7 annotations do not all share.

    python3 pipeline/mechdiff.py zh-0005 12          one sentence
    python3 pipeline/mechdiff.py zh-0005 3-8         a range

Nodes are named by the token they are aligned to ("19发挥"); a node without a token is named by its concept
and where it hangs ("and@8表示:ARG1"), a named entity by its name ("person«阿耀»"). Every fact (the concept on
a token, an edge, an attribute value, a document-level triple) is listed with the annotations that have it.
A fact every annotation has is left out. Inverse roles (:ARG1-of) are turned round.

This is an aid for writing the diff report: it shows who chose what, without copying mistakes. Different
alignments or different places for an abstract node make facts look different that mean the same; read the
graphs (pipeline/show_sentence.py) wherever the listing is not clear.
"""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import penman  # noqa: E402
import umrdoc  # noqa: E402

SPECIAL = {"author", "root", "document-creation-time", "null-conceiver", "past-reference", "present-reference",
           "future-reference"}


def parse_align(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"\s*(\S+?):\s*(-?\d+)-(-?\d+)", line)
        if m and int(m.group(2)) > 0:
            out[m.group(1)] = (int(m.group(2)), int(m.group(3)))
    return out


class Sent:
    """One annotation of one sentence: anchors of the variables and the facts."""

    def __init__(self, index, graph_text, align_text, words):
        self.index, self.words = index, words
        self.anchor, self.facts, self.ok = {}, collections.defaultdict(set), True
        self.concept = {}
        try:
            tree = penman.parse(graph_text)
        except Exception as e:  # noqa: BLE001
            self.ok = False
            self.err = str(e)[:80]
            return
        al = parse_align(align_text)
        nodes, self.edges, attrs, parent = {}, [], [], {}

        def walk(node, par=None, role=None):
            var, branches = node
            if var not in nodes:
                nodes[var] = None
                if par:
                    parent[var] = (par, role)
            for r, t in branches:
                if r == "/":
                    nodes[var] = t
                elif isinstance(t, tuple):
                    self.edges.append((var, r, t[0]))
                    walk(t, var, r)
                else:
                    self.edges.append((var, r, t))
        walk(tree.node)
        self.root = tree.node[0]
        self.concept = nodes
        names = {}
        for s, r, t in self.edges:
            if r == ":name" and t in nodes:
                ops = sorted((r2, t2) for s2, r2, t2 in self.edges if s2 == t and r2.startswith(":op"))
                names[s] = "".join(str(t2).strip('"') for _, t2 in ops)
                names[t] = None

        def anchor(v, depth=0):
            if v in self.anchor:
                return self.anchor[v]
            if names.get(v):
                a_ = "«%s»" % names[v]
            elif v in al:
                a, b = al[v]
                a_ = "%d%s" % (a, "".join(words[a - 1:b])) if b <= len(words) else "%d-%d" % (a, b)
            elif v in parent and depth < 6:
                p, r = parent[v]
                a_ = "%s@%s%s" % (nodes[v], anchor(p, depth + 1), r)
            else:
                a_ = "%s@ROOT" % nodes[v]
            self.anchor[v] = a_
            return a_
        for v in nodes:
            anchor(v)
        for v, c in nodes.items():
            if v in names and names[v] is None:
                continue                                     # the name node itself
            if v in al or names.get(v):
                self.facts["concept"].add((self.anchor[v], c))
        self.facts["root"].add((self.anchor[self.root],))
        for s, r, t in self.edges:
            if s in names and names[s] is None or r == ":name":
                continue
            if t in nodes:
                if r.endswith("-of") and r != ":consist-of":
                    s, r, t = t, r[:-3], s
                self.facts["edge"].add((self.anchor[s], r, self.anchor[t]))
            else:
                self.facts["attr"].add((self.anchor[s], r, str(t)))


def load_all(d):
    files = [("gold", C.gold_path(d))] + [(k, os.path.join(rd, d["doc"] + ".umr")) for k, _, _, rd in C.systems()]
    out = {}
    for key, path in files:
        if not os.path.exists(path):
            continue
        doc = umrdoc.load(path)
        sents, varmap = {}, {}
        for s in doc["sents"]:
            g = s["gold"]
            S = Sent(s["index"], g[umrdoc.SECTIONS[0]], g[umrdoc.SECTIONS[1]], s["words"])
            S.raw = g
            S.head = s.get("head", "")
            sents[s["index"]] = S
            for v, a in S.anchor.items():
                varmap[v] = "s%d:%s" % (s["index"], a)
        for i, S in sents.items():
            text = S.raw[umrdoc.SECTIONS[2]]
            for kind in ("temporal", "modal", "coref"):
                m = re.search(r":%s\s*\((.*?)\)\s*(?=:temporal|:modal|:coref|\)\s*$|$)" % kind, text, re.S)
                if not m:
                    continue
                for a, r, b in re.findall(r"\(\s*(\S+)\s+(:\S+)\s+([^\s()]+)\s*\)", m.group(1) + ")"):
                    def nm(x):
                        if x in SPECIAL:
                            return x
                        y = varmap.get(x, "?" + x)
                        return y[len("s%d:" % i):] if y.startswith("s%d:" % i) else y
                    S.facts[kind].add((nm(a), r, nm(b)))
        out[key] = sents
    return out


def who(keys, all_keys):
    if len(keys) == len(all_keys):
        return "全部"
    if len(keys) >= len(all_keys) - 2 and len(all_keys) > 3:
        return "除 %s 外全部" % "、".join(k for k in all_keys if k not in keys)
    return "、".join(keys)


def show(d, data, i):
    keys = list(data)
    S = {k: data[k].get(i) for k in keys}
    g = S["gold"]
    print("=" * 30, d["doc"], "第 %d 句" % i)
    print(" ".join("%d:%s" % (j + 1, w) for j, w in enumerate(g.words)))
    extra = [l for l in g.head.splitlines() if l.strip() and not re.match(r"\s*(#|Index:|Words:)", l)]
    if extra:       # glosses and translation of the gold file (Arapaho, Navajo): the systems did not see them
        print("--- gold 文件里这一句的注释行（词素、释义、翻译；系统看不到）\n" + "\n".join(" ".join(l.split()) for l in extra))
    print("--- gold 句子图（变量后面是它的名字）")
    text = g.raw[umrdoc.SECTIONS[0]].replace("\t", "  ")
    print(text)
    print("--- gold 变量: " + "  ".join("%s=%s" % (v, a) for v, a in g.anchor.items()))
    print("--- gold 文档级\n" + re.sub(r"\n\s+", "\n  ", g.raw[umrdoc.SECTIONS[2]]))
    for k in keys:
        if S[k] is None:
            print("!!! %s 没有这一句" % k)
        elif not S[k].ok:
            print("!!! %s 这一句的图解析失败（%s），下面的列表里没有它；请用 show_sentence.py 看原文" % (k, S[k].err))
    live = [k for k in keys if S[k] is not None and S[k].ok]
    # concepts per token
    print("--- 概念（按词；只列不一致的）")
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for k in live:
        for a, c in S[k].facts["concept"]:
            by[a][c].append(k)
    def tokkey(a):
        m = re.match(r"(\d+)", a)
        return (int(m.group(1)) if m else 999, a)
    for a in sorted(by, key=tokkey):
        have = {k for ks in by[a].values() for k in ks}
        if len(by[a]) == 1 and len(have) == len(live):
            continue
        parts = ["%s [%s]" % (c, who(ks, live)) for c, ks in sorted(by[a].items(), key=lambda x: -len(x[1]))]
        miss = [k for k in live if k not in have]
        if miss:
            parts.append("无节点 [%s]" % who(miss, live))
        print("  %s: %s" % (a, " | ".join(parts)))
    titles = [("root", "根"), ("edge", "边"), ("attr", "属性"),
              ("temporal", "文档级 temporal"), ("modal", "文档级 modal"), ("coref", "文档级 coref")]
    for kind, title in titles:
        facts = collections.defaultdict(list)
        for k in live:
            for f in S[k].facts[kind]:
                facts[f].append(k)
        rows = [(f, ks) for f, ks in facts.items() if len(ks) < len(live)]
        if not rows:
            continue
        print("--- %s（只列不一致的）" % title)
        if kind == "attr":      # per node and attribute: every value with who has it
            by2 = collections.OrderedDict()
            for f, ks in sorted(facts.items(), key=lambda x: (tokkey(x[0][0]), x[0])):
                by2.setdefault(f[:2], []).append((f[2], ks))
            for (a, r), vals in by2.items():
                have = {k for _, ks in vals for k in ks}
                if len(vals) == 1 and len(have) == len(live):
                    continue
                parts = ["%s [%s]" % (v, who(ks, live)) for v, ks in sorted(vals, key=lambda x: -len(x[1]))]
                miss = [k for k in live if k not in have]
                if miss:
                    parts.append("无 [%s]" % who(miss, live))
                print("  %s %s: %s" % (a, r, " | ".join(parts)))
            continue
        if kind != "root":
            # merge facts of the same annotations that differ only in the source (edges, attributes: same
            # role and target) or only in the target (document level: same source and relation)
            pos = 2 if kind in ("temporal", "modal", "coref") else 0
            merged = collections.OrderedDict()
            for f, ks in sorted(rows, key=lambda x: (tokkey(x[0][pos]), x[0])):
                rest = tuple(x for j, x in enumerate(f) if j != pos)
                merged.setdefault((rest, tuple(ks)), []).append(f[pos])
            rows = []
            for (rest, ks), vals in merged.items():
                v = vals[0] if len(vals) == 1 else "{" + "，".join(vals) + "}"
                f = list(rest)
                f.insert(pos, v)
                rows.append((tuple(f), list(ks)))
            rows.sort(key=lambda x: (tokkey(x[0][0].lstrip("{")), x[0]))
        for f, ks in rows:
            print("  %s  ⟵ %s" % (" ".join(f), who(ks, live)))


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    d = C.docs(sys.argv[1])[0]
    data = load_all(d)
    a, _, b = sys.argv[2].partition("-")
    for i in range(int(a), int(b or a) + 1):
        show(d, data, i)
        print()


if __name__ == "__main__":
    main()
