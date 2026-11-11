"""Writes api/<sub>/ and chat/<sub>/ (registry.yaml and annotate/skill.md) for the five sub-experiments.

    python3 exp/scripts/make_subexps.py

The skills of one sub-experiment differ between the two methods only in how the extra resource reaches
the model: through a tool (api) or as an attached file (chat). Edit this script and run it again rather
than editing the generated files by hand, so the ten stay in step.
"""
import os
import textwrap

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SUBS = {
    # name: (guideline, api tools, chat attachment, one-line description)
    "s1-abridged": ("guidelines/umr_guidelines_abridged.md", [], None,
                    "第一步：缩略版 guideline（exp/guidelines/umr_guidelines_abridged.md，约 1.4 万字符），没有工具"),
    "s1-full": ("guidelines/umr_guidelines.md", [], None,
                "第一步：完整 guideline（umr4nlp/umr-guidelines guidelines.md，36.6 万字符），没有工具"),
    "s2-search": ("guidelines/umr_guidelines_abridged.md", ["search_guidelines"], "guidelines",
                  "第二步：缩略版 guideline + 完整 guideline 的搜索（search_guidelines）"),
    "s2-propbank": ("guidelines/umr_guidelines_abridged.md", ["propbank_lookup"], "propbank",
                    "第二步：缩略版 guideline + PropBank（propbank_lookup，网页 repo 的 propbank/zh.json、en.json）"),
    "s2-gold": ("guidelines/umr_guidelines_abridged.md", ["search_annotations"], "gold",
                "第二步：缩略版 guideline + gold 数据（search_annotations，shared task 的训练数据 UMR 2.2 training-clean/dirty，不含测试句子）"),
}

GUIDELINE_ATTACHED = """The full UMR guidelines (umr4nlp/umr-guidelines `guidelines.md`, about 366,000 characters) are
attached to this message as `umr_guidelines.md`. Read them before you annotate, and go back to them for
every decision you are not sure of. They often write the older short names (AUTH, DCT, FullAff,
:modstr); your answer uses the release names listed under Output format.
"""

HEAD = """# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value
and document-level relation counts. Take the time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.
- Follow the examples: when a sentence has a construction an example shows, annotate it the way the
  example does.
- Do not guess when you can check: {check}
- Before you go on to the next sentence, check the graph against the guidelines once more: every word
  that carries meaning has its concept, every event its aspect, every role the right direction; and at
  the end check that the document-level relations cover every event and entity the guidelines ask for.

## Guidelines

{guideline}
"""

# "Do not guess when you can check: ..." for each sub-experiment and method
CHECK = {
    ("api", "s1-abridged"): "the answer to almost every question is in the guidelines above and their examples; "
                            "look it up there rather than answer from memory.",
    ("api", "s1-full"): "the answer to almost every question is in the guidelines above and their examples; "
                        "look it up there rather than answer from memory.",
    ("api", "s2-search"): "whenever the guidelines above do not settle a case, search the full guidelines with "
                          "`search_guidelines` (see Tools). Call it as often as you need: many calls are expected.",
    ("api", "s2-propbank"): "look up every predicate in PropBank with `propbank_lookup` (see Tools) before you choose "
                            "its sense and numbered roles. Call it as often as you need.",
    ("api", "s2-gold"): "look up how the gold data annotates a construction, a word or a relation with "
                        "`search_annotations` (see Tools). Call it as often as you need: many calls are expected.",
    ("chat", "s1-abridged"): "the answer to almost every question is in the guidelines above and their examples; "
                             "look it up there rather than answer from memory.",
    ("chat", "s1-full"): "the answer to almost every question is in the attached guidelines and their examples; "
                         "look it up there rather than answer from memory.",
    ("chat", "s2-search"): "whenever the guidelines above do not settle a case, look it up in the attached full "
                           "guidelines (see Attached file).",
    ("chat", "s2-propbank"): "check every predicate's sense and numbered roles in the attached PropBank entries "
                             "(see Attached file).",
    ("chat", "s2-gold"): "check how the attached gold annotations of similar sentences annotate a construction, a "
                         "word or a relation (see Attached file).",
}

FORMAT = """
## Output format

Write plain text only (no JSON, no commentary). For every sentence, in order:

    # ::snt 1
    # sentence level graph:
    (s1t / taste-01
        :ARG0 (s1p / person
            :name (s1n / name :op1 "Edmund" :op2 "Pope"))
        :ARG1 (s1f / free-04
            :ARG1 s1p
            :aspect state)
        :temporal (s1t2 / today)
        :aspect performance)

then, once, after the last sentence, every document-level relation of the whole document in one graph:

    # document level relations:
    (d / document
        :temporal ((document-creation-time :depends-on s1t2)
                   (s1t2 :contained s1t)
                   (s1t :before s2c))
        :modal ((root :modal author)
                (author :full-affirmative s1t)
                (author :full-affirmative s2c))
        :coref ((s1p :same-entity s2p)))

- `# ::snt N` uses the sentence number of the input line. Every sentence gets a graph, even a short one.
- Variables of sentence N start with `s` + N and a letter (`s3p`, `s3x2`), all different. A node that
  fills two roles in one sentence is written once and then named by its variable.
- No word alignment: it is computed from the graph. So a concept that comes from a word of the sentence
  is written as that word (in English its lemma: `taste-01` for "tasted"), and the `:op` strings of a
  name are the words of the name as the sentence writes them.
- Document level: `(parent :relation child)` triples, grouped under `:temporal`, `:modal`, `:coref`;
  each end is a variable of a sentence graph or a constant (`author`, `root`, `document-creation-time`,
  `past-reference`, `present-reference`, `future-reference`, `null-conceiver`).
- Use the names of the UMR release data: `author` (not AUTH), `document-creation-time` (not DCT),
  `full-affirmative`, `partial-affirmative`, `neutral-affirmative`, `neutral-negative`,
  `partial-negative`, `full-negative`, `unspecified` (not FullAff, ...), `:modal-strength` (not
  :modstr), `:refer-person` / `:refer-number` with lower-case values (`3rd`, `singular`), and lower-case
  aspect values (`performance`, `state`, ...).
- Write the whole document: do not stop early, do not summarise, do not skip sentences.
"""

TOOLS = {
    "search_guidelines": """
## Tools

`search_guidelines(keywords, max_results)` searches the **full** UMR guidelines (umr4nlp/umr-guidelines,
the document the guidelines above abridge) and returns the matching passages with their headings, with
their examples. The abridged guidelines leave out most details and examples, so use it a lot: look a rule
up whenever you are not sure of a case (an abstract concept, a role, a named entity type, an aspect or modal
value, a temporal or coreference decision), and look up each kind of construction the document has before
you annotate it. Search with the terms the guidelines would use (`aspect`, `have-rel-role-92`, `:quant`,
`modal strength`, `reentrancy`). Note that the full guidelines often write the older short names (AUTH,
DCT, FullAff, :modstr); your answer uses the release names listed under Output format.
""",
    "propbank_lookup": """
## Tools

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Look up every predicate (verbs, and nouns and adjectives that take arguments) before you choose its sense
and its numbered roles: compare the rolesets' meanings and examples with the sentence and take the one
that fits. Give all lemmas of a sentence (and alternate forms) in one call; call again for the next
sentences.
""",
    "search_annotations": """
## Tools

`search_annotations(language, keywords, max_results)` returns gold UMR annotations of whole sentences of the
training data (other documents) that contain the keywords: words of the text, concepts (`have-org-role-92`), roles
(`:ARG1-of`), attribute values (`:aspect state`), document-level relations (`:same-entity`). These are
annotated by the same experts as the gold you are compared with, so they show how this data annotates a
case. Use it a lot: for each sentence, look up its words and constructions you are not sure of (a word's
concept and sense, a light verb, a modal word, a named entity, a comparison, a quantity, a discourse
relation, the aspect of a kind of event) before you annotate it, and follow what the gold does.
""",
}

ATTACH = {
    "guidelines": """
## Attached file

The **full** UMR guidelines are attached (`umr_guidelines.md`, umr4nlp/umr-guidelines; the document the
guidelines above abridge, with many more details and examples). Read the parts this document needs, and
look a rule up whenever you are not sure of a case (an abstract concept, a role, a named entity type, an
aspect or modal value, a temporal or coreference decision). Note that the full guidelines often write the
older short names (AUTH, DCT, FullAff, :modstr); your answer uses the release names listed under Output
format.
""",
    "propbank": """
## Attached file

The PropBank entries of the words of this document are attached (`<document>.propbank.md`): for each word
PropBank has, every roleset with its id, its numbered roles and its examples. For every predicate, compare
the rolesets' meanings and examples with the sentence and take the one that fits, with its numbered roles.
""",
    "gold": """
## Attached file

Gold UMR annotations of training sentences (other documents) are attached (`<document>.gold.md`): for
each sentence of this document, the training sentences that share most of its words, with their whole
annotation. They are annotated by the same experts as the gold you are compared with: read them, and for
each word, construction and relation they share with this document, annotate it the way they do.
""",
}

INPUT = """
## Input

Language: {lang}
Document: {doc_id} ({n} sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces.

{sentences}
"""

REGISTRY = """# {sub}（{method}）：{desc}
# 语法是 SkillParseUMR skillsets/REGISTRY.md 的最小子集，见 exp/lib/registry.py。
# 一波、一个 episode（整篇文档），一个 skill：输入是 shared task 的 blind 测试文件（一行一句，空格分词），输出每句的 PENMAN 图（对齐由 exp/lib/autoalign.py 生成），
# 最后一张整篇文档的文档级关系图（exp/lib/umrdoc.py 把它分到各句，写成 .umr 再打分）。
# 本文件由 exp/scripts/make_subexps.py 生成。

waves:
  - name: document
    start: annotate
    init_input:
      context:
        lang: annotation.lang
        doc_id: annotation.name
        n: annotation.sentences
      input:
        sentences: annotation.lines

skills:
  annotate:
    path: annotate
    guideline: {guideline}{extra}
    input:
      sentences: str
    emit:
      umr: str                  # 回答原文：每句的图 + 文档级关系
    store: [umr]

dispatcher: {{}}
"""

# ------------------------------------------------------------------ harness (Claude Code): harness/<sub>/TASK.md
# The same five conditions, done by an agent in a working directory (exp/harness/claude_code.py builds
# it): the guidelines are files there, the tools are commands, the answer is written to answer.txt.

HARNESS_FILES = {
    "abridged": "- `guidelines/umr_guidelines_abridged.md`: the UMR guidelines, abridged (about 14,000 characters). "
                "Read all of it before you start.\n",
    "full": "- `guidelines/umr_guidelines.md`: the full UMR guidelines (umr4nlp/umr-guidelines, about 366,000 "
            "characters, with many examples). It is long: read it in parts (Read with offset and limit) and "
            "search it (Grep) for the terms of a case. Read the parts this document needs before you start, and "
            "go back to it for every decision you are not sure of. It often writes the older short names (AUTH, "
            "DCT, FullAff, :modstr); your answer uses the release names listed under Output format.\n",
}

HARNESS_CHECK = {
    "s1-abridged": "the answer to almost every question is in the guidelines file and its examples; look it up "
                   "there rather than answer from memory.",
    "s1-full": "the answer to almost every question is in the guidelines file and its examples; look it up "
               "there rather than answer from memory.",
    "s2-search": "whenever the abridged guidelines do not settle a case, search the full guidelines with "
                 "`tools/search_guidelines.py`. Look things up as often as you need: many lookups are expected.",
    "s2-propbank": "look up every predicate in PropBank (`tools/propbank_lookup.py`) before you choose its sense "
                   "and numbered roles.",
    "s2-gold": "look up how the gold data annotates a construction, a word or a relation "
               "(`tools/search_annotations.py`). Look things up as often as you need: many lookups are expected.",
}

HARNESS_TOOLS = {
    "search_guidelines": """
`python3 tools/search_guidelines.py KEYWORD [KEYWORD ...] [--max N]` searches the full UMR guidelines and
prints the matching passages with their headings (at most N, 1-10, default 3). Search with the terms the
guidelines would use (`aspect`, `have-rel-role-92`, `:quant`, "modal strength", `reentrancy`), and look up
each kind of construction the document has before you annotate it.
""",
    "propbank_lookup": """
`python3 tools/propbank_lookup.py --language {lang} LEMMA [LEMMA ...]` prints the PropBank rolesets of up
to 20 lemmas: each roleset's id, its numbered roles and its examples. Look up every predicate (verbs, and
nouns and adjectives that take arguments); compare the rolesets' meanings and examples with the sentence
and take the one that fits. Give all lemmas of a sentence in one call.
""",
    "search_annotations": """
`python3 tools/search_annotations.py --language {lang} KEYWORD [KEYWORD ...] [--max N]` prints gold UMR
annotations of whole training sentences (other documents) that contain the keywords (at most N, 1-10,
default 3): words of the text, concepts (`have-org-role-92`), roles (`:ARG1-of`), attribute values
(`:aspect state`), document-level relations (`:same-entity`). They are annotated by the same experts as
the gold you are compared with: for each sentence, look up the words and constructions you are not sure
of before you annotate it, and follow what the gold does.
""",
}

HARNESS_HEAD = """# Task: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line. Work in this directory only; the files you need are
listed under Files. Write the answer to `answer.txt` (see Output format). You may keep notes in `notes/`.

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value
and document-level relation counts. Take the time this needs:

- Read the guidelines carefully before you start, and go back to them for every decision you are not
  sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.
- Follow the examples: when a sentence has a construction an example shows, annotate it the way the
  example does.
- Do not guess when you can check: {check}
- Before you go on to the next sentence, check the graph against the guidelines once more: every word
  that carries meaning has its concept, every event its aspect, every role the right direction; and at
  the end check that the document-level relations cover every event and entity the guidelines ask for.

## Files

{files}"""

HARNESS_ANSWER = """- Write the answer to `answer.txt` in this directory: every sentence, then the document-level
  relations, in the format above, nothing else. It is long; you may write it in parts (for example
  sentence by sentence, adding to the file), but at the end the file must hold the whole answer.
"""

HARNESS_SUBS = {"s1-abridged": ["abridged"], "s1-full": ["full"], "s2-search": ["abridged"],
                "s2-propbank": ["abridged"], "s2-gold": ["abridged"]}


def harness_task(sub, tools):
    check = textwrap.fill("- Do not guess when you can check: " + HARNESS_CHECK[sub], 106,
                          subsequent_indent="  ", break_on_hyphens=False)
    files = "".join(textwrap.fill(HARNESS_FILES[k].strip(), 106, subsequent_indent="  ", break_on_hyphens=False)
                    + "\n" for k in HARNESS_SUBS[sub])
    if tools:
        files += "- `tools/`: commands (run them with Bash, from this directory):\n" + "".join(
            HARNESS_TOOLS[t] for t in tools)
    head = HARNESS_HEAD.replace("- Do not guess when you can check: {check}", check).replace("{files}", files)
    fmt = FORMAT.replace("- Write the whole document:", HARNESS_ANSWER + "- Write the whole document:")
    return head + fmt + INPUT


# ------------------------------------------------------------------ ablation a1-sentence-propbank (API only)
# The s2-propbank condition (abridged guidelines + propbank_lookup), sentence by sentence: wave 1 annotates
# each sentence alone (one call per sentence); wave 2, once every sentence has its graph, adds the
# document-level relations of each sentence (one call per sentence), given the sentence and the five
# before it (fewer at the start of the document) with their graphs.

A1_CHECK = ("look up every predicate in PropBank with `propbank_lookup` (see Tools) before you choose its sense "
            "and numbered roles. Call it as often as you need.")

A1_GRAPH_HEAD = """# Skill: the sentence-level UMR graph of one sentence

You annotate one sentence of a document in Uniform Meaning Representation (UMR): its sentence-level graph.
(Its document-level relations are added later, in another step.) The sentence is under **Input** at the
end.

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role and attribute
value counts. Take the time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity.
- Follow the examples: when the sentence has a construction an example shows, annotate it the way the
  example does.
- {check}
- Before you answer, check the graph against the guidelines once more: every word that carries meaning
  has its concept, every event its aspect, every role the right direction.

## Guidelines

{guideline}
"""

A1_GRAPH_FORMAT = """
## Output format

Write plain text only (no JSON, no commentary), exactly this, for the sentence number N of the input:

    # ::snt 1
    # sentence level graph:
    (s1t / taste-01
        :ARG0 (s1p / person
            :name (s1n / name :op1 "Edmund" :op2 "Pope"))
        :ARG1 (s1f / free-04
            :ARG1 s1p
            :aspect state)
        :temporal (s1t2 / today)
        :aspect performance)

- `# ::snt N` uses the sentence number of the input.
- Variables start with `s` + N and a letter (`s3p`, `s3x2`), all different. A node that fills two roles is
  written once and then named by its variable.
- No word alignment: it is computed from the graph. So a concept that comes from a word of the sentence
  is written as that word (in English its lemma: `taste-01` for "tasted"), and the `:op` strings of a
  name are the words of the name as the sentence writes them.
- Use the names of the UMR release data: `:modal-strength` (not :modstr) with `full-affirmative`,
  `partial-affirmative`, `neutral-affirmative`, `neutral-negative`, `partial-negative`, `full-negative`;
  `:refer-person` / `:refer-number` with lower-case values (`3rd`, `singular`); lower-case aspect values
  (`performance`, `state`, ...).
"""

A1_GRAPH_INPUT = """
## Input

Language: {lang}
Document: {doc_id}, sentence {num} of {n}

The sentence: its number, a tab, then its words separated by spaces.

{line}
"""

A1_REL_HEAD = """# Skill: the document-level relations of one sentence

You add the UMR document-level relations (temporal, modal, coreference) of one sentence of a document.
Every sentence of the document already has its sentence-level graph. Under **Input** at the end you get
this sentence and the sentences before it (at most five) with their graphs.

**Make the annotation as correct as you can.** It is compared, relation by relation, with an expert gold
annotation made by these guidelines, so every temporal, modal and coreference relation counts. Take the
time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: which events and entities get which relations, their reference times, conceivers and
  modal strengths, and which nodes corefer.
- Follow the examples: when the sentence has a case an example shows, annotate it the way the example
  does.
- {check}
- Before you answer, check that the relations cover every event and entity of this sentence that the
  guidelines ask for.

## Guidelines

{guideline}
"""

A1_REL_FORMAT = """
## Output format

Write plain text only (no JSON, no commentary): the document-level relations of this sentence (number N)
in one graph, for example for sentence 2:

    # document level relations:
    (d / document
        :temporal ((s1t :before s2t)
                   (document-creation-time :overlap s2s))
        :modal ((root :modal author)
                (author :full-affirmative s2t)
                (author :full-affirmative s2s))
        :coref ((s1p :same-entity s2p)))

- The relations of this sentence are those in which a node of sentence N takes part: with a constant
  (`author`, `root`, `document-creation-time`, `past-reference`, `present-reference`,
  `future-reference`, `null-conceiver`), with another node of sentence N, or with a node of one of the
  previous sentences given (for example coreference with an earlier mention, or an event of this sentence
  ordered after an event of the previous one). Do not repeat relations among the previous sentences only.
- `(parent :relation child)` triples, grouped under `:temporal`, `:modal`, `:coref`; each end is a
  variable of the graphs given, exactly as written there, or a constant.
- Use the names of the UMR release data: `author` (not AUTH), `document-creation-time` (not DCT),
  `full-affirmative`, ..., `unspecified` (not FullAff, ...).
- If the sentence has no document-level relation, write the graph with empty groups: `(d / document)`.
"""

A1_REL_INPUT = """
## Input

Language: {lang}
Document: {doc_id}, sentence {num} of {n}

The previous sentences (at most five; number, tab, words):

{prev_lines}

Their graphs:

{prev_graphs}

This sentence:

{line}

Its graph:

{graph}
"""

A1_REL_CHECK = ("the meaning of a predicate is in PropBank: look it up with `propbank_lookup` (see Tools) "
                "whenever it matters for a relation (whether an event is a state, who its conceiver is).")

A1_REL_TOOLS = """
## Tools

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Use it when the meaning of a predicate decides a relation.
"""

A1_REGISTRY = """# a1-sentence-propbank（直接调 API）：ablation：s2-propbank 的条件（缩略版 guideline + propbank_lookup）一句句跑。
# 第一波 sentence：每句单独一次调用，只给这一句，写这一句的句子图。
# 第二波 document：全部句子图都标好之后，每句再一次调用：给这一句和它前面最多五句（文档开头不足五句就从第一句给起）的
# 原文和句子图，写这一句的文档级关系。两波的结果拼成整篇的回答，再和其他子实验一样打分。
# 语法是 SkillParseUMR skillsets/REGISTRY.md 的最小子集（for_each、window），见 exp/lib/registry.py。
# 本文件由 exp/scripts/make_subexps.py 生成。

waves:
  - name: sentence
    start: graph
    parallel: 8
    init_input:
      for_each:
        sentence: annotation.sents
      context:
        lang: annotation.lang
        doc_id: annotation.name
        n: annotation.sentences
        num: sentence.index
      input:
        line: sentence.line
  - name: document
    start: relations
    parallel: 8
    init_input:
      for_each:
        sentence: annotation.sents
        tree: worktree.sentence
      context:
        lang: annotation.lang
        doc_id: annotation.name
        n: annotation.sentences
        num: sentence.index
        prev_lines:
          window: annotation.sents
          range: [-5, 0]
          pick: line
        prev_graphs:
          window: worktree.sentence
          range: [-5, 0]
          pick: graph
      input:
        line: sentence.line
        graph: tree.graph

skills:
  graph:
    path: graph
    guideline: guidelines/umr_guidelines_abridged.md
    tools: [propbank_lookup]
    input:
      line: str
    emit:
      graph: str                # 这一句的 # ::snt N / # sentence level graph:
    store: [graph]
  relations:
    path: relations
    guideline: guidelines/umr_guidelines_abridged.md
    tools: [propbank_lookup]
    input:
      line: str
      graph: str
    emit:
      relations: str            # 这一句的 # document level relations:
    store: [relations]

dispatcher: {{}}
"""


def ablation_a1():
    base = os.path.join(EXP, "api", "a1-sentence-propbank")
    for name, head, chk, fmt, tools, inp in (
            ("graph", A1_GRAPH_HEAD, A1_CHECK, A1_GRAPH_FORMAT, TOOLS["propbank_lookup"], A1_GRAPH_INPUT),
            ("relations", A1_REL_HEAD, A1_REL_CHECK, A1_REL_FORMAT, A1_REL_TOOLS, A1_REL_INPUT)):
        check = textwrap.fill("- Do not guess when you can check: " + chk, 106, subsequent_indent="  ",
                              break_on_hyphens=False)
        os.makedirs(os.path.join(base, name), exist_ok=True)
        with open(os.path.join(base, name, "skill.md"), "w", encoding="utf-8") as f:
            f.write(head.replace("- {check}", check) + fmt + tools + inp)
    with open(os.path.join(base, "registry.yaml"), "w", encoding="utf-8") as f:
        f.write(A1_REGISTRY.format())


def main():
    for method in ("api", "chat"):
        for sub, (guideline, tools, attach, desc) in SUBS.items():
            d = os.path.join(EXP, method, sub, "annotate")
            os.makedirs(d, exist_ok=True)
            middle = ""
            if method == "api":
                middle = "".join(TOOLS[t] for t in tools)
                extra = "\n    tools: [%s]" % ", ".join(tools)
            else:
                middle = ATTACH[attach] if attach else ""
                extra = ("\n    attachment: %s          # chat：随 prompt 一起上传的文件" % attach) if attach else ""
            check = textwrap.fill("- Do not guess when you can check: " + CHECK[(method, sub)], 106,
                                  subsequent_indent="  ", break_on_hyphens=False)
            head = HEAD.replace("- Do not guess when you can check: {check}", check)
            if method == "chat" and sub == "s1-full":      # 36.6 万字符：作为文件上传，不贴进 prompt
                head = head.replace("{guideline}", GUIDELINE_ATTACHED)
                guideline = "\"\"                    # 完整 guideline 作为附件 exp/guidelines/umr_guidelines.md"
            with open(os.path.join(d, "skill.md"), "w", encoding="utf-8") as f:
                f.write(head + FORMAT + middle + INPUT)
            with open(os.path.join(EXP, method, sub, "registry.yaml"), "w", encoding="utf-8") as f:
                f.write(REGISTRY.format(sub=sub, method="直接调 API" if method == "api" else "chat 界面",
                                        desc=desc, guideline=guideline, extra=extra))
    for sub, (guideline, tools, attach, desc) in SUBS.items():
        d = os.path.join(EXP, "harness", sub)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "TASK.md"), "w", encoding="utf-8") as f:
            f.write(harness_task(sub, tools))
    ablation_a1()
    print("wrote", ", ".join(SUBS), "and a1-sentence-propbank")


if __name__ == "__main__":
    main()
