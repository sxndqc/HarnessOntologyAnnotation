"""Writes api/<sub>/ and chat/<sub>/ (registry.yaml and annotate/skill.md) for the five sub-experiments.

    python3 exp/scripts/make_subexps.py

The skills of one sub-experiment differ between the two methods only in how the extra resource reaches
the model: through a tool (api) or as an attached file (chat). Edit this script and run it again rather
than editing the generated files by hand, so the ten stay in step.
"""
import os

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
attached to this message as `umr_guidelines.md`. Read them before you annotate. They often write the older
short names (AUTH, DCT, FullAff, :modstr); your answer uses the release names listed under Output format.
"""

HEAD = """# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph and alignment, then all the document-level relations (temporal, modal, coreference) of the
document. Follow the guidelines below. The document is under **Input** at the end, one sentence per line.

## Guidelines

{guideline}
"""

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
    # alignment:
    s1t: 3-3
    s1p: 1-2
    s1n: 0-0
    s1f: 4-4
    s1t2: 5-5

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
- Alignment: one line per variable, `variable: first-last` with the word positions of the input line
  (counted from 1); `0-0` for a node with no word.
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
the document the guidelines above abridge) and returns the matching passages with their headings. Look a
rule up whenever the abridged guidelines do not settle a case (an abstract concept, a role, an aspect or
modal value, a temporal or coreference decision). Note that the full guidelines often write the older short
names (AUTH, DCT, FullAff, :modstr); your answer uses the release names listed under Output format.
""",
    "propbank_lookup": """
## Tools

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Look up every predicate before you choose its sense and its numbered roles; give all lemmas of a sentence
(and alternate forms) in one call.
""",
    "search_annotations": """
## Tools

`search_annotations(language, keywords, max_results)` returns gold UMR annotations of whole sentences of the
training data (other documents) that contain the keywords: words of the text, concepts (`have-org-role-92`), roles
(`:ARG1-of`), attribute values (`:aspect state`), document-level relations (`:same-entity`). Use it to see
how a construction, a word or a relation is annotated in the gold data before you annotate it.
""",
}

ATTACH = {
    "guidelines": """
## Attached file

The **full** UMR guidelines are attached (`umr_guidelines.md`, umr4nlp/umr-guidelines; the document the
guidelines above abridge). Search them whenever the abridged guidelines do not settle a case. Note that the
full guidelines often write the older short names (AUTH, DCT, FullAff, :modstr); your answer uses the
release names listed under Output format.
""",
    "propbank": """
## Attached file

The PropBank entries of the words of this document are attached (`<document>.propbank.md`): for each word
PropBank has, every roleset with its id, its numbered roles and its examples. Choose each predicate's sense
and numbered roles from it.
""",
    "gold": """
## Attached file

Gold UMR annotations of training sentences (other documents) are attached (`<document>.gold.md`): for
each sentence of this document, the training sentences that share most of its words, with their whole
annotation. Use them to see how a construction, a word or a relation is annotated in the gold data.
""",
}

INPUT = """
## Input

Language: {lang}
Document: {doc_id} ({n} sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces
(the alignment refers to these word positions, counted from 1 in each sentence).

{sentences}
"""

REGISTRY = """# {sub}（{method}）：{desc}
# 语法是 SkillParseUMR skillsets/REGISTRY.md 的最小子集，见 exp/lib/registry.py。
# 一波、一个 episode（整篇文档），一个 skill：输入是 shared task 的 blind 测试文件（一行一句，空格分词），输出每句的 PENMAN 图和对齐，
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
      umr: str                  # 回答原文：每句的图和对齐 + 文档级关系
    store: [umr]

dispatcher: {{}}
"""


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
            head = HEAD
            if method == "chat" and sub == "s1-full":      # 36.6 万字符：作为文件上传，不贴进 prompt
                head = HEAD.replace("{guideline}", GUIDELINE_ATTACHED)
                guideline = "\"\"                    # 完整 guideline 作为附件 exp/guidelines/umr_guidelines.md"
            with open(os.path.join(d, "skill.md"), "w", encoding="utf-8") as f:
                f.write(head + FORMAT + middle + INPUT)
            with open(os.path.join(EXP, method, sub, "registry.yaml"), "w", encoding="utf-8") as f:
                f.write(REGISTRY.format(sub=sub, method="直接调 API" if method == "api" else "chat 界面",
                                        desc=desc, guideline=guideline, extra=extra))
    print("wrote", ", ".join(SUBS))


if __name__ == "__main__":
    main()
