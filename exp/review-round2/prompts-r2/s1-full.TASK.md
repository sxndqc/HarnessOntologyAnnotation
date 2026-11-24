# Task: the UMR of a whole document

Your job is the Uniform Meaning Representation (UMR) annotation of a whole document: a sentence-level
graph for each sentence, followed by the document-level relations of the whole document (temporal, modal,
coreference). You find the document at the end, under **Input**, with one sentence on each line. Stay in
this directory; Files lists what you need. The answer goes into `answer.txt` (see Output format), and
`notes/` is yours for notes.

**Accuracy is what matters here.** Experts annotated the same document by these guidelines, and your
annotation is checked against theirs node by node and relation by relation: each concept, sense, role,
attribute value and document-level relation is counted. Work as carefully and for as long as that takes:

- The examples are the model to follow: a construction that an example shows is annotated the way that
  example annotates it.
- Start by reading the guidelines closely. Whenever a decision is uncertain, return to them: which concept
  and which sense, a numbered or a non-core role, abstract concepts and named entities, aspect, modal
  strength, polarity, and the temporal, modal and coreference relations.
- Check instead of guessing: the answer to almost every question is in the guidelines file and its
  examples; look it up there rather than answer from memory.
- Finish each sentence with one more check of its graph against the guidelines before moving on: a concept
  for every word that carries meaning, an aspect for every event, the right direction for every role. When
  the document is done, make sure the document-level relations cover every event and entity the guidelines
  ask for.

## Files

- `guidelines/umr_guidelines.md`: the full UMR guidelines (umr4nlp/umr-guidelines, about 366,000
  characters, with many examples). It is long: read it in parts and search it (for example with `rg` or
  `grep -n`) for the terms of a case. Read the parts this document needs before you start, and go back to
  it for every decision you are not sure of. It often writes the older short names (AUTH, DCT, FullAff,
  :modstr); your answer uses the release names listed under Output format.
- There are no lookup tools in this condition: use only the files listed here and what you know. Do not
  search the web and do not read anything outside this directory.

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
- Write the answer to `answer.txt` in this directory: every sentence, then the document-level
  relations, in the format above, nothing else. It is long; you may write it in parts (for example
  sentence by sentence, adding to the file), but at the end the file must hold the whole answer.
- Write the whole document: do not stop early, do not summarise, do not skip sentences.

## Input

Language: {lang_label}
Document: {doc_id} ({n} sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces.

{sentences}
