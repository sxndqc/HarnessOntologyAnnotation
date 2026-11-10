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
- abstract concepts (`and`, `person`, `have-org-role-92`, ...) that are not words stay unaligned;
  concepts with a -9N sense (`have-org-role-92`, `identity-91`) are never matched to a word.

English needs more than Chinese: inflected and irregular forms (`began` for `begin`, `denied` for `deny`),
derived words that share the beginning (`decision` for `decide`), and names written as an adjective
(`American`, `Russian`, `Russia's` for "America", "Russia").
"""
import re

SENSE = re.compile(r"-\d+$")
ABSTRACT_SENSE = re.compile(r"-9\d$")

IRREGULAR = {
    "be": "is are was were been being am 's 're 'm", "have": "has had having 've 'd", "do": "did does done doing",
    "say": "said says", "go": "went gone goes going", "give": "gave given", "take": "took taken", "make": "made",
    "begin": "began begun", "steal": "stole stolen", "get": "got gotten", "know": "knew known", "see": "saw seen",
    "come": "came", "find": "found", "think": "thought", "tell": "told", "become": "became", "leave": "left",
    "feel": "felt", "bring": "brought", "buy": "bought", "hold": "held", "keep": "kept", "write": "wrote written",
    "stand": "stood", "hear": "heard", "mean": "meant", "meet": "met", "run": "ran", "pay": "paid", "sit": "sat",
    "speak": "spoke spoken", "lead": "led", "grow": "grew grown", "lose": "lost", "fall": "fell fallen",
    "send": "sent", "build": "built", "understand": "understood", "break": "broke broken", "spend": "spent",
    "win": "won", "catch": "caught", "seek": "sought", "teach": "taught", "sell": "sold", "fight": "fought",
    "throw": "threw thrown", "choose": "chose chosen", "rise": "rose risen", "drive": "drove driven",
    "forget": "forgot forgotten", "eat": "ate eaten", "drink": "drank drunk", "fly": "flew flown",
    "wear": "wore worn", "hide": "hid hidden", "shoot": "shot", "lie": "lay lain lied", "bear": "bore born borne",
    "strike": "struck", "swear": "swore sworn", "forbid": "forbade forbidden", "withdraw": "withdrew withdrawn",
    "i": "me my mine myself", "we": "us our ours ourselves", "you": "your yours yourself yourselves",
    "he": "him his himself", "she": "her hers herself", "it": "its itself", "they": "them their theirs themselves",
}
FORMS = {lemma: set(forms.split()) for lemma, forms in IRREGULAR.items()}


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
    if len(ops) == 1 and not _cjk(target) and len(target) >= 4:
        # a one-word name written as an adjective or a possessive: American, Russian, Russia's
        stem = target[:-1] if target[-1] in "aeiouy" else target
        for i, w in enumerate(low):
            if w.startswith(stem) and len(w) - len(target) <= 3:
                return (i + 1, i + 1)
    return None


def _match(lemma, word):
    w = word.lower()
    if _cjk(lemma) or _cjk(w):
        return lemma in w or (len(w) >= 2 and w in lemma)
    if w in FORMS.get(lemma, ()):
        return True
    stem = lemma[:-1] if lemma.endswith("e") and len(lemma) > 3 else lemma
    if lemma.endswith("y") and len(lemma) > 3:
        stem = lemma[:-1]                       # deny: denied, denies
    if len(stem) >= 3 and (w.startswith(stem) or (len(w) >= 4 and lemma.startswith(w))):
        return True
    # a derived word with the same beginning: decide / decision, advise / advice
    k = max(4, len(lemma) - 2)
    return len(lemma) >= 5 and len(w) >= k and w[:k] == lemma[:k]


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
        if ABSTRACT_SENSE.search(str(c)):
            out[v] = None
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
