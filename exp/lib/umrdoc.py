"""UMR documents: the gold, the input a model sees, and the model's answer as a .umr file.

    doc = load_blind(".cache/umr22/test-blind/zh-0023.txt")   the shared task's input: one sentence per
                               line, tokens separated by spaces
    doc = load(".cache/umr22/test-gold/zh-0023.umr")          a .umr file (the gold)
    doc["sents"]               [{index, words, head, gold}]: head is the block's header (# :: sntN,
                               Index:, Words:), gold the three sections as the file has them
    input_lines(doc)           the document as the model sees it: one sentence per line,
                               "<number>\t<words separated by spaces>"
    gold_umr(doc)              the gold as a .umr text, normalised the same way as predictions (for
                               AnCast and umrjudge; juːmæʧ and Smatch read the official gold file itself)
    parse_answer(doc, text)    a model's answer -> (.umr text in the shared task's file format, report)

The answer gives, for each sentence, `# ::snt N`, its sentence-level PENMAN graph and its alignment,
and at the end one `# document level relations:` graph holding every temporal, modal and coreference
relation of the document. parse_answer puts each relation into the document-level graph of the latest
sentence it mentions (that is how the UMR release files are written), so that AnCast, juːmæʧ and
umrjudge read the result as they read the gold.
"""
import os
import re

import penman

import autoalign

SECTIONS = ("# sentence level graph:", "# alignment:", "# document level annotation:")
RULE = "#" * 80
VAR = re.compile(r"^s(\d+)[a-z][\w-]*$")
DOC_GROUP = re.compile(r":(temporal|modal|coref)\s*\(")   # a group, not the relation of (root :modal author)
DOC_TRIPLE = re.compile(r"\(\s*([^\s()]+)\s+:([\w-]+)\s+([^\s()]+)\s*\)")


# ------------------------------------------------------------------ reading the gold

def blocks(text):
    """[[head, {section: text}]] of a .umr file, one per sentence block."""
    out = []
    for chunk in re.split(r"^#{20,}\s*$", text, flags=re.M):
        if not chunk.strip():
            continue
        head, sections, current = [], {}, None
        for line in chunk.splitlines():
            marker = next((m for m in SECTIONS if line.strip().startswith(m)), None)
            if marker:
                current = marker
                sections[current] = ""
                continue
            if current:
                sections[current] += line + "\n"
            elif line.strip():
                head.append(line)
        out.append(["\n".join(head), sections])
    return out


def load(path):
    with open(path, encoding="utf-8-sig") as f:
        text = f.read()
    sents = []
    for head, sections in blocks(text):
        m = re.search(r"#\s*::\s*snt(\d+)", head)
        if not m:
            continue
        words = re.search(r"^Words:\s*(.*)$", head, re.M)
        words = words.group(1).split() if words else []
        lines = [l for l in head.splitlines() if not l.startswith(("Index:", "Words:"))]
        head = "\n".join(lines + ["Index: " + " ".join(str(k + 1) for k in range(len(words))),
                                  "Words: " + " ".join(words)])
        sents.append({"index": int(m.group(1)), "words": words, "head": head,
                      "gold": {k: sections.get(k, "").strip() for k in SECTIONS}})
    name = os.path.basename(path)[:-4]
    return {"name": name, "lang": lang_of(name), "sents": sents, "path": path}


def lang_of(name):
    """zh-0023 -> zh, en-0005 -> en (the shared task's file names); chinese_umr-0023 -> zh."""
    if name.startswith("chinese"):
        return "zh"
    if name.startswith("english"):
        return "en"
    return name.split("-")[0]


def load_blind(path):
    """A blind test file of the shared task: one sentence per line, tokens separated by spaces."""
    with open(path, encoding="utf-8-sig") as f:
        lines = [l.rstrip("\n").rstrip("\r") for l in f]
    while lines and not lines[-1].strip():
        lines.pop()
    sents = []
    for k, line in enumerate(lines, 1):
        words = line.split(" ") if line.strip() else []
        words = [w for w in words if w != ""]
        head = "\n".join(["# :: snt%d" % k, "Index: " + " ".join(str(i + 1) for i in range(len(words))),
                          "Words: " + " ".join(words)])
        sents.append({"index": k, "words": words, "head": head, "gold": {}})
    name = os.path.basename(path)[:-4]
    return {"name": name, "lang": lang_of(name), "sents": sents, "path": path}


def input_lines(doc):
    return "\n".join("%d\t%s" % (s["index"], " ".join(s["words"])) for s in doc["sents"])


def gold_umr(doc):
    """The gold, read and written back by the same code as the predictions (graphs re-encoded, every
    variable aligned), so that every scorer reads both sides the same way."""
    out = []
    for s in doc["sents"]:
        graph, align, _ = sentence_sections(s["index"], s["gold"][SECTIONS[0]], s["gold"][SECTIONS[1]], strict=False)
        triples = read_doc(s["gold"][SECTIONS[2]])
        out.append((s["head"], {SECTIONS[0]: graph, SECTIONS[1]: align, SECTIONS[2]: render_doc(s["index"], triples)}))
    return render(out)


# ------------------------------------------------------------------ notation

# the older short names the full guideline uses -> the names of the UMR release data
NAMES = [
    (r":modstr\b", ":modal-strength"), (r":ref-person\b", ":refer-person"), (r":ref-number\b", ":refer-number"),
    (r":quot\b", ":quote"), (r"\bAUTH\b", "author"), (r"\bDCT\b", "document-creation-time"), (r"\bROOT\b", "root"),
    (r"\bPAST_REF\b", "past-reference"), (r"\bPRESENT_REF\b", "present-reference"),
    (r"\bFUTURE_REF\b", "future-reference"), (r"\bNULL_CONCEIVER\b", "null-conceiver"),
]
STRENGTH = {"fullaff": "full-affirmative", "prtaff": "partial-affirmative", "neutaff": "neutral-affirmative",
            "fullneg": "full-negative", "prtneg": "partial-negative", "neutneg": "neutral-negative",
            "unsp": "unspecified", "aff": "full-affirmative"}
LOWER_VALUES = re.compile(r"(:aspect|:refer-person|:refer-number|:mode|:modal-strength)\s+\"?([A-Za-z0-9-]+)\"?")


def normalise_names(text):
    for pattern, repl in NAMES:
        text = re.sub(pattern, repl, text)
    text = re.sub(r":(FullAff|PrtAff|NeutAff|FullNeg|PrtNeg|NeutNeg|Unsp|AFF)\b",
                  lambda m: ":" + STRENGTH[m.group(1).lower()], text)
    def value(m):
        v = m.group(2)
        v = STRENGTH.get(v.lower(), v)
        return "%s %s" % (m.group(1), v.lower())
    return LOWER_VALUES.sub(value, text)


# ------------------------------------------------------------------ one sentence

def balance(text):
    """Drop closing brackets that close nothing and close what is left open."""
    out, depth, quoted = [], 0, False
    for ch in text:
        if ch == '"':
            quoted = not quoted
        if not quoted and ch == "(":
            depth += 1
        elif not quoted and ch == ")":
            if depth == 0:
                continue
            depth -= 1
        out.append(ch)
    return "".join(out) + ")" * depth


def sentence_sections(index, graph_text, align_text, strict=True, problems=None, words=None):
    """(graph, alignment, variables) of one sentence; an unparseable graph becomes (sNx0 / empty).
    With words, a variable the alignment text does not give is aligned by autoalign (the answer has no
    alignment); without, it gets 0-0."""
    problems = problems if problems is not None else []
    graph_text = normalise_names(graph_text.strip())
    g = None
    for attempt in ([graph_text] if strict else []) + [balance(graph_text)]:
        try:
            g = penman.decode(attempt)
            break
        except Exception as e:
            err = str(e)
    if g is None or not g.triples:
        problems.append("sentence %d: graph does not parse (%s)" % (index, (err if g is None else "empty")[:160]))
        return "(s%dx0 / empty)" % index, "s%dx0: 0-0" % index, {"s%dx0" % index}
    if graph_text != balance(graph_text) and strict:
        problems.append("sentence %d: brackets repaired" % index)
    # variables must start with s<N>: rename the others
    prefix = "s%d" % index
    rename = {}
    for v in g.variables():
        if not re.match(r"^%s[a-z]" % prefix, v):
            new = prefix + re.sub(r"^s\d+", "", v)
            new = new if re.match(r"^%s[a-z]" % prefix, new) else prefix + "x" + re.sub(r"\W", "", v)
            while new in g.variables() or new in rename.values():
                new += "x"
            rename[v] = new
    if rename:
        problems.append("sentence %d: variables renamed %s" % (index, ", ".join("%s->%s" % kv for kv in rename.items())))
        g = penman.Graph([(rename.get(s, s), r, rename.get(t, t) if isinstance(t, str) else t) for s, r, t in g.triples],
                         top=rename.get(g.top, g.top))
    variables = set(g.variables())
    if strict:
        # a fresh layout: every node is defined where it first occurs, so there are no forward references
        # (the shared task's validator rejects them)
        g = penman.Graph(g.triples, top=g.top)
    graph = penman.encode(g, indent=4)
    align = []
    for line in align_text.splitlines():
        m = re.match(r"^\s*(\S+?)\s*:\s*(-?\d+\s*-\s*-?\d+(?:\s*,\s*-?\d+\s*-\s*-?\d+)*)\s*$", line)
        if m:
            v = rename.get(m.group(1), m.group(1))
            ranges = [re.sub(r"\s", "", r) for r in m.group(2).split(",")]
            if v in variables and not any(a.startswith(v + ":") for a in align):
                align.append("%s: %s" % (v, ",".join(ranges)))
        elif line.strip():
            problems.append("sentence %d: alignment line not understood: %s" % (index, line.strip()[:60]))
    auto = autoalign.align(g, words) if words is not None else {}
    for v in sorted(variables - {a.split(":")[0] for a in align}):
        span = auto.get(v)
        align.append("%s: %s" % (v, "%d-%d" % span if span else "0-0"))
    return graph, "\n".join(align), variables


# ------------------------------------------------------------------ document level

def read_doc(text):
    """[(group, parent, relation, child)] of a document-level graph or of several."""
    text = normalise_names(text)
    marks = [(m.start(), m.group(1)) for m in DOC_GROUP.finditer(text)]
    out = []
    for k, (start, group) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(text)
        for a, r, b in DOC_TRIPLE.findall(text[start:end]):
            t = (group, a, r, b.rstrip(")"))
            if t not in out:
                out.append(t)
    return out


def render_doc(index, triples):
    lines = ["(s%ds0 / sentence" % index]
    for group in ("temporal", "modal", "coref"):
        mine = ["(%s :%s %s)" % (a, r, b) for g, a, r, b in triples if g == group]
        if mine:
            lines.append("    :%s (%s)" % (group, ("\n" + " " * (len(group) + 7)).join(mine)))
    return "\n".join(lines) + ")"


def sentence_of(x):
    m = VAR.match(x)
    return int(m.group(1)) if m else None


def distribute(triples, indices, variables, problems):
    """{sentence index: [triples]}: each triple goes to the latest sentence it mentions; a triple with
    no variable (root :modal author) goes to every sentence that has modal relations (as the release
    files have it) or, for other groups, to the first sentence. Triples naming a variable that no
    graph defines are dropped."""
    out = {i: [] for i in indices}
    loose = []
    for t in triples:
        g, a, r, b = t
        ends = [x for x in (a, b) if sentence_of(x) is not None]
        unknown = [x for x in ends if x not in variables]
        if unknown:
            problems.append("document relation dropped, undefined variable %s: (%s :%s %s)" % (unknown[0], a, r, b))
            continue
        if not ends:
            loose.append(t)
            continue
        k = max(sentence_of(x) for x in ends)
        if k in out and t not in out[k]:
            out[k].append(t)
    for t in loose:
        if t[0] == "modal":
            for i in indices:
                if any(x[0] == "modal" for x in out[i]) and t not in out[i]:
                    out[i].insert(0, t)
        elif indices and t not in out[indices[0]]:
            out[indices[0]].append(t)
    return out


# ------------------------------------------------------------------ the answer

SNT = re.compile(r"^\s*#\s*::\s*snt\s*(\d+)\b.*$", re.M | re.I)
FINAL = re.compile(r"^\s*#\s*document[ -]level relations\s*:?\s*$", re.M | re.I)


def parse_answer(doc, text):
    """(.umr text, report). report: {"problems": [...], "sentences_found": n, "relations": n}."""
    problems = []
    text = text.replace("\r", "")
    text = re.sub(r"^\s*```\w*\s*$", "", text, flags=re.M)
    final = list(FINAL.finditer(text))
    doc_text = ""
    if final:
        doc_text = text[final[-1].end():]
        text = text[:final[-1].start()]
    else:
        problems.append("no '# document level relations:' block")
    marks = list(SNT.finditer(text))
    found = {}
    for k, m in enumerate(marks):
        end = marks[k + 1].start() if k + 1 < len(marks) else len(text)
        found[int(m.group(1))] = text[m.end():end]
    graphs, aligns, variables = {}, {}, set()
    for s in doc["sents"]:
        i = s["index"]
        body = found.get(i)
        if body is None:
            problems.append("sentence %d: missing" % i)
            graphs[i], aligns[i], vs = "(s%dx0 / empty)" % i, "s%dx0: 0-0" % i, {"s%dx0" % i}
        else:
            parts = split_sections(body)
            doc_text += "\n" + parts.get(SECTIONS[2], "")    # per-sentence relations, if the model wrote any
            graphs[i], aligns[i], vs = sentence_sections(i, parts.get(SECTIONS[0], ""), parts.get(SECTIONS[1], ""),
                                                         problems=problems, words=s["words"])
        variables |= vs
    triples = read_doc(doc_text)
    indices = [s["index"] for s in doc["sents"]]
    per = distribute(triples, indices, variables, problems)
    out = [(s["head"], {SECTIONS[0]: graphs[s["index"]], SECTIONS[1]: aligns[s["index"]],
                        SECTIONS[2]: render_doc(s["index"], per[s["index"]])}) for s in doc["sents"]]
    report = {"sentences_found": sum(1 for s in doc["sents"] if s["index"] in found),
              "sentences": len(doc["sents"]), "relations": sum(len(v) for v in per.values()), "problems": problems}
    return render(out), report


def split_sections(body):
    """{section: text} of one sentence of the answer; a bare graph counts as the sentence graph."""
    found, current = {}, None
    for line in body.splitlines():
        low = line.strip().lower()
        marker = next((m for m in SECTIONS if low.startswith(m)), None)
        if marker is None and low.startswith("# document level relations"):
            marker = SECTIONS[2]
        if marker:
            current = marker
            found.setdefault(current, "")
            continue
        if current is None and line.strip().startswith("("):
            current = SECTIONS[0]
            found.setdefault(current, "")
        if current:
            found[current] += line + "\n"
    return found


def render(items):
    out = []
    for head, sections in items:
        pieces = [head.strip()] + ["%s\n%s" % (k, (sections.get(k) or "").strip()) for k in SECTIONS]
        out.append(RULE + "\n" + "\n\n".join(pieces))
    return "\n\n\n".join(out) + "\n\n\n"
