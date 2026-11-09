# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph and alignment, then all the document-level relations (temporal, modal, coreference) of the
document. Follow the guidelines below. The document is under **Input** at the end, one sentence per line.

## Guidelines

{guideline}

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

## Attached file

The **full** UMR guidelines are attached (`umr_guidelines.md`, umr4nlp/umr-guidelines; the document the
guidelines above abridge). Search them whenever the abridged guidelines do not settle a case. Note that the
full guidelines often write the older short names (AUTH, DCT, FullAff, :modstr); your answer uses the
release names listed under Output format.

## Input

Language: {lang}
Document: {doc_id} ({n} sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces
(the alignment refers to these word positions, counted from 1 in each sentence).

{sentences}
