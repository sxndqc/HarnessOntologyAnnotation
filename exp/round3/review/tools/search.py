"""search_annotations and search_guidelines (copied from ai-native-annotator.github.io data/skillparse/web_tools/search.py;
here plain Python: files read from disk, the sentences to leave out set with set_skip).

    search_annotations(language, keywords)  gold UMR annotations of whole sentences that contain the
                                            keywords
    search_guidelines(keywords)             the sections of the UMR guidelines that contain them

The guidelines are the web repo's data/skillparse/resources/guidelines/umr_guidelines.md ($SP_RESOURCES, by
default the sibling checkout). The gold is the shared task's training data (UMR 2.2 training-clean only;
the dirty part is not used; $UMR22, by default exp/.cache/umr22), or with GOLD_SOURCE=web the web repo's gold.json.

The test documents (set_skip: their names, and the texts of the document being annotated, since
english_umr-0005 and -0007 are one text) are never returned: their answers must not leak.
"""
import json
import os
import re

MAX_RESULTS = 10
MAX_TEXT = 6000                 # characters of one returned annotation or section
CHUNK = 8000                    # a guideline section longer than this is returned in passages
LANGS = {"zh": "zh", "chinese": "zh", "中文": "zh", "汉语": "zh", "en": "en", "english": "en", "英文": "en", "英语": "en",
         "uz": "uz", "uzbek": "uz", "o'zbek": "uz", "oʻzbek": "uz", "o'zbekcha": "uz",
         "arp": "arp", "arapaho": "arp", "nv": "nv", "navajo": "nv", "la": "la", "latin": "la",
         "cs": "cs", "czech": "cs", "it": "it", "italian": "it"}
GOLD = ("zh", "en", "arp", "nv", "la", "cs")    # the languages there is training data for (not Italian)
_cache = {}
_skip = {"docs": set(), "texts": set()}


def set_skip(docs=(), texts=()):
    """Gold sentences search_annotations never returns: every sentence of these documents and these
    sentence texts (spaces ignored)."""
    _skip["docs"] = set(docs)
    _skip["texts"] = {_plain(t) for t in texts}


def search_annotations(language: str, keywords: list[str], max_results: int = 3) -> dict:
    """Find how a case is annotated: gold UMR annotations of whole sentences.

    language: "zh" (Chinese) or "en" (English).
    keywords: words or pieces to look for, matched anywhere in a sentence or its annotation:
    words of the text (e.g. "发生", "wanted to"), concepts ("have-org-role-91", "identity-91"),
    roles (":ARG1-of", ":manner"), attribute values (":aspect state"). Sentences with more of the
    keywords come first.
    max_results: how many gold sentences to return (at most 10).

    Returns {"gold": [{"doc", "sentence_number", "sentence", "annotation"}], where annotation is
    the sentence's whole annotation (words, sentence-level graph, alignment, document-level
    annotation); "found": how many gold sentences matched in all}.
    """
    lang = _lang(language)
    if lang is None:
        return {"gold": [], "error": f"language must be zh, en, cs, it, la, arp or nv, not {language!r}"}
    if lang not in GOLD:
        return {"gold": [], "found": 0, "note": f"there is no gold data for {language!r}"}
    words = _keywords(keywords)
    if not words:
        return {"gold": [], "error": "give at least one keyword"}
    n = _count(max_results, 3)
    skip = _skip["texts"]
    gold, left_out = [], 0
    for rec, low in _gold(lang, words):
        hits = _hits(low, words, lowered=True)
        if not hits[0]:
            continue
        if rec["doc"] in _skip["docs"] or _plain(rec["text"]) in skip:
            left_out += 1
            continue
        gold.append((hits, len(rec["annotation"]), rec))
    gold.sort(key=lambda x: (-x[0][0], -x[0][1], x[1]))
    out = {
        "gold": [{"doc": r["doc"], "sentence_number": r["snt"], "sentence": r["text"],
                  "annotation": _clip(r["annotation"])} for _, _, r in gold[:n]],
        "found": len(gold),
    }
    if left_out:
        out["left_out"] = f"{left_out} matching sentences of the test documents are not shown"
    return out


def search_guidelines(keywords: list[str], max_results: int = 3) -> dict:
    """Look a rule up in the UMR guidelines (umr4nlp/umr-guidelines, guidelines.md).

    keywords: terms to look for, e.g. "aspect", "modal strength", "have-rel-role-92", ":quant",
    "reentrancy". Passages with more of the keywords come first, then those whose heading has
    them, then those that mention them most.
    max_results: how many passages to return (at most 10).

    Returns {"sections": [{"heading": the passage's place in the guidelines ("Part 3. ... > Part
    3-3-1. Aspect"), "text": the passage (a section, or a part of a long one)}], "found": how
    many passages matched}.
    """
    words = _keywords(keywords)
    if not words:
        return {"sections": [], "error": "give at least one keyword"}
    n = _count(max_results, 3)
    found = []
    for path, text, low in _guideline_sections():
        hits = _hits(path + "\n" + text, words)
        if hits[0]:
            in_head = _hits(path, words)[0]
            found.append(((hits[0], in_head, hits[1] * 1000 // max(1, len(text))), len(text), path, text, low))
    # the table of contents and the alphabetical index come after every passage that states a rule
    found.sort(key=lambda x: (x[4], -x[0][0], -x[0][1], -x[0][2], x[1]))
    return {"sections": [{"heading": p, "text": t} for _, _, p, t, _ in found[:n]], "found": len(found)}


# ------------------------------------------------------------------ helpers

def _lang(language):
    return LANGS.get(str(language or "").strip().lower())


def _keywords(keywords):
    if isinstance(keywords, str):
        keywords = re.split(r"[,，;；\s]+", keywords)
    return [k.strip().lower() for k in (keywords or []) if isinstance(k, str) and k.strip()]


def _count(n, default):
    try:
        return max(1, min(MAX_RESULTS, int(n)))
    except (TypeError, ValueError):
        return default


def _hits(text, words, lowered=False):
    """(how many of the keywords occur, how many times in all)."""
    low = text if lowered else text.lower()
    counts = [low.count(w) for w in words]
    return sum(1 for c in counts if c), sum(counts)


def _plain(text):
    return re.sub(r"\s+", "", str(text))


def _clip(text):
    return text if len(text) <= MAX_TEXT else text[:MAX_TEXT] + "\n… (%d more characters)" % (len(text) - MAX_TEXT)


def _resources():
    """The web repo's resources folder: $SP_RESOURCES, else the sibling checkout of
    ai-native-annotator/ai-native-annotator.github.io next to this repository."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.environ.get("SP_RESOURCES") or os.path.normpath(os.path.join(
        here, "..", "..", "..", "ai-native-annotator.github.io", "data", "skillparse", "resources"))


def _read(rel):
    """A resource file's text, from the web repo's data/skillparse/resources/ (see _resources)."""
    if rel in _cache:
        return _cache[rel]
    path = os.path.join(_resources(), rel)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    _cache[rel] = text
    return text


GOLD_DIRS = {"zh": "chinese", "en": "english", "arp": "arapaho", "nv": "navajo", "la": "latin", "cs": "czech"}


def _umr22():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.environ.get("UMR22", os.path.join(here, "..", ".cache", "umr22"))


def _gold(lang, words=()):
    """(record, its sentence and annotation in lower case) of every training sentence that can match.

    The gold is the training data of the DMR 2026 UMR parsing shared task (UMR 2.2 training-clean only;
    the dirty part is not used; read from $UMR22), as the shared task allowed; with GOLD_SOURCE=web it is the web
    repo's gold/<lang>/gold.json instead.

    The sentences of a language are kept in one file, $UMR22/.records-<lang>.jsonl, a record per line,
    made at the first call and again when the folder's files change. It is read line by line, and a
    line is parsed only when it holds one of the keywords: Czech has 160,000 sentences, too many to
    load at every call."""
    if os.environ.get("GOLD_SOURCE") == "web":
        key = "gold:" + lang
        if key not in _cache:
            _cache[key] = [(r, (r["text"] + "\n" + r["annotation"]).lower())
                           for r in json.loads(_read("gold/%s/gold.json" % lang))]
        yield from _cache[key]
        return
    files = []
    for part in ("training-clean",):   # clean only: the dirty part is not used
        folder = os.path.join(_umr22(), part, GOLD_DIRS[lang])
        files += [os.path.join(folder, name) for name in sorted(os.listdir(folder))
                  if name.endswith(".umr")] if os.path.isdir(folder) else []
    stamp = "%d:%d" % (len(files), sum(os.path.getsize(f) for f in files))
    store = os.path.join(_umr22(), ".records-%s.jsonl" % lang)
    try:
        with open(store, encoding="utf-8") as f:
            ok = f.readline().strip() == stamp
    except OSError:
        ok = False
    if not ok:
        tmp = "%s.%d.tmp" % (store, os.getpid())
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(stamp + "\n")
            for path in files:
                for r in _umr_records(path, os.path.basename(path)[:-4]):
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp, store)
    # a keyword with a character JSON writes differently cannot be looked for in the raw line
    quick = [w for w in words if not re.search(r'["\\\n\t]', w)]
    with open(store, encoding="utf-8") as f:
        f.readline()
        for line in f:
            if quick and len(quick) == len(words):
                low = line.lower()
                if not any(w in low for w in quick):
                    continue
            r = json.loads(line)
            yield r, (r["text"] + "\n" + r["annotation"]).lower()


def _umr_records(path, doc):
    """{doc, snt, text, annotation} of every sentence block of a .umr file."""
    with open(path, encoding="utf-8-sig") as f:
        text = f.read()
    out = []
    for block in re.split(r"^#{20,}\s*$", text, flags=re.M):
        m = re.search(r"#\s*::\s*snt(\d+)", block)
        words = re.search(r"^Words:\s*(.*)$", block, re.M)
        if not m or not words:
            continue
        out.append({"doc": doc, "snt": int(m.group(1)), "text": " ".join(words.group(1).split()),
                    "annotation": block.strip()})
    return out


LOW = ("Table of Contents", "Alphabetical Index")   # sections that name every term and state no rule: ranked last


def _units(lines):
    """The pieces a section may be cut between: paragraphs, with a fenced example kept whole together with the
    'Example ...' line right above it."""
    units, cur, fence = [], [], False
    for line in lines:
        if line.strip().startswith("```"):
            fence = not fence
            cur.append(line)
            continue
        if not line.strip() and not fence:
            if cur:
                units.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        units.append(cur)
    out, label = [], False
    for u in units:
        if label:                                   # an example's number stays with the example
            out[-1] = out[-1] + [""] + u
        else:
            out.append(u)
        label = all(re.match(r"^(Example\b.*|\(?\d+[a-z]?\)?\.?|)$", x.strip()) for x in out[-1])
    return ["\n".join(u) for u in out]


def _cut_long(unit, CHUNK):
    """A single piece longer than CHUNK (a table, a list, an example without blank lines) cut at lines; the
    pieces of a table each repeat its two header lines, the pieces of a fenced example are each fenced."""
    if len(unit) <= CHUNK:
        return [unit]
    lines = unit.split("\n")
    head = []
    if len(lines) > 2 and lines[0].lstrip().startswith("|") and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[1]):
        head, lines = lines[:2], lines[2:]
    fenced = not head and lines[0].strip().startswith("```") and lines[-1].strip().startswith("```")
    if fenced:
        lines = lines[1:-1]
    room = CHUNK - sum(len(h) + 1 for h in head) - (8 if fenced else 0)
    parts, cur, size = [], [], 0
    for line in lines:
        # a list is cut before a top-level item, a table before any row, anything else before any line
        start = bool(head) or fenced or not line.startswith((" ", "\t"))
        if cur and size + len(line) + 1 > room and (start or size > room * 1.5):
            parts.append(cur)
            cur, size = [], 0
        cur.append(line)
        size += len(line) + 1
    if cur:
        parts.append(cur)
    return ["\n".join(["```"] + head + part + ["```"] if fenced else head + part) for part in parts]


def _guideline_sections():
    """[(heading path, text, low)] of the guidelines: one passage per section, a section longer than CHUNK cut
    into passages between paragraphs (never inside a fenced example, unless the example alone is longer).
    low marks the table of contents and the alphabetical index."""
    key = "guidelines"
    if key not in _cache:
        text = _read(os.environ.get("UMR_GUIDELINES", "guidelines-revised/umr_guidelines.md"))
        sections, path, body = [], [], []

        def close():
            if not body:
                return
            head_line, rest = (body[0], body[1:]) if path else ("", body)
            if not "\n".join(rest).strip():
                return                              # a heading with nothing under it but its subsections
            head = " > ".join(x for x in path[1:] if x) or path[0]     # without the document's title
            room = CHUNK - len(head_line) - 2
            pieces = [p for unit in _units(rest) for p in _cut_long(unit, room)]
            total = sum(len(p) + 2 for p in pieces)
            # passages of about the same length (no short tail), none over CHUNK
            want = -(-total // room)
            parts = None
            while parts is None or len(parts) > want:
                target = min(room, total / want * 1.08) if parts is None else room
                parts, cur = [], ""
                for piece in pieces:
                    if cur and len(cur) + len(piece) + 2 > target:
                        parts.append(cur)
                        cur = ""
                    cur = cur + "\n\n" + piece if cur else piece
                if cur:
                    parts.append(cur)
                if target == room:
                    break
            low = any(x in head for x in LOW)
            for k, part in enumerate(parts):
                name = head + (" (%d/%d)" % (k + 1, len(parts)) if len(parts) > 1 else "")
                sections.append((name, (head_line + "\n\n" if head_line else "") + part, low))
        fence = False
        for line in text.split("\n"):
            if line.strip().startswith("```"):
                fence = not fence
            m = None if fence else re.match(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if m:
                close()
                level = len(m.group(1))
                path = (path + [""] * level)[:level - 1] + [m.group(2)]
                body = [line.strip()]
            else:
                body.append(line)
        close()
        _cache[key] = sections
    return _cache[key]
