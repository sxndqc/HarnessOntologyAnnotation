"""Node-to-word alignment computed from a sentence graph and its words (the answer no longer writes one).

    align(graph, words) -> {variable: (first, last) or None}     positions counted from 1; None is 0-0

juːmæʧ maps the nodes of the two files through the alignment first, so a graph without one scores far
lower than the same graph aligned. The rules follow how the UMR 2.2 gold aligns:

- a named entity (`(c / country :name (n / name :op1 "日本"))`) is aligned to the words of its name
  (the words whose concatenation is the :op strings), the `name` node itself to nothing;
- any other node whose concept, without its sense number (`恢复-02` -> `恢复`, `taste-01` -> `taste`), is a
  word of the sentence is aligned to that word: an unused occurrence first, in order;
- failing that, a word that contains the concept or that the concept contains (Chinese: a word of at
  least two characters; other languages: the same beginning, so `tasted` for `taste`);
- abstract concepts (`and`, `person`, `have-org-role-92`, ...) that are not words stay unaligned.
"""
import re

SENSE = re.compile(r"-\d+$")


def _norm(s):
    return s.strip('"').lower()


def _cjk(s):
    return any("㐀" <= ch <= "鿿" for ch in s)


def _name_span(words, ops):
    target = "".join(_norm(o) for o in ops)
    spaced = " ".join(_norm(o) for o in ops)
    if not target:
        return None
    low = [w.lower() for w in words]
    for i in range(len(low)):
        acc = ""
        for j in range(i, len(low)):
            acc += low[j]
            if acc == target or " ".join(low[i:j + 1]) == spaced:
                return (i + 1, j + 1)
            if len(acc) >= len(target):
                break
    return None


def _match(lemma, word):
    w = word.lower()
    if _cjk(lemma) or _cjk(w):
        return lemma in w or (len(w) >= 2 and w in lemma)
    stem = lemma[:-1] if lemma.endswith("e") and len(lemma) > 3 else lemma
    return len(stem) >= 3 and (w.startswith(stem) or (len(w) >= 4 and lemma.startswith(w)))


def align(graph, words):
    instances = [(v, c) for v, _, c in graph.instances() if c is not None]
    name_of = {s: t for s, r, t in graph.edges() if r == ":name"}
    ops = {}
    for s, r, t in graph.attributes():
        m = re.match(r"^:op(\d+)$", r)
        if m:
            ops.setdefault(s, []).append((int(m.group(1)), str(t)))
    out, used = {}, set()
    for v, n in name_of.items():
        span = _name_span(words, [t for _, t in sorted(ops.get(n, []))])
        out[n] = None
        if span:
            out[v] = span
            used.update(range(span[0], span[1] + 1))
    for v, c in instances:
        if v in out:
            continue
        lemma = _norm(SENSE.sub("", str(c)))
        exact = [i + 1 for i, w in enumerate(words) if w.lower() == lemma]
        cands = exact or [i + 1 for i, w in enumerate(words) if _match(lemma, w)]
        if not cands:
            out[v] = None
            continue
        free = [i for i in cands if i not in used]
        k = (free or cands)[0]
        out[v] = (k, k)
        used.add(k)
    return out
