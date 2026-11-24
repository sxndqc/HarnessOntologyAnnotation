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
- Check instead of guessing: use the three tools (see Files): search the full guidelines with
  `tools/search_guidelines.py` whenever the abridged guidelines do not settle a case, look up every
  predicate in PropBank with `tools/propbank_lookup.py` before you choose its sense and numbered roles,
  and look up how the gold data annotates a construction, a word or a relation with
  `tools/search_annotations.py`. Look things up as often as you need: many lookups are expected.
- Finish each sentence with one more check of its graph against the guidelines before moving on: a concept
  for every word that carries meaning, an aspect for every event, the right direction for every role. When
  the document is done, make sure the document-level relations cover every event and entity the guidelines
  ask for.

## Files

- `guidelines/umr_guidelines_abridged.md`: the UMR guidelines, abridged (about 14,000 characters). Read
  all of it before you start.
- `tools/`: commands (run them in the shell, from this directory):

`python3 tools/search_guidelines.py KEYWORD [KEYWORD ...] [--max N]` searches the full UMR guidelines and
prints the matching passages with their headings (at most N, 1-10, default 3). Search with the terms the
guidelines would use (`aspect`, `have-rel-role-92`, `:quant`, "modal strength", `reentrancy`), and look up
each kind of construction the document has before you annotate it.

`python3 tools/propbank_lookup.py --language {lang} LEMMA [LEMMA ...]` prints the PropBank rolesets of up
to 20 lemmas: each roleset's id, its numbered roles and its examples. Look up every predicate (verbs, and
nouns and adjectives that take arguments); compare the rolesets' meanings and examples with the sentence
and take the one that fits. Give all lemmas of a sentence in one call.

`python3 tools/search_annotations.py --language {lang} KEYWORD [KEYWORD ...] [--max N]` prints gold UMR
annotations of whole training sentences (other documents) that contain the keywords (at most N, 1-10,
default 3): words of the text, concepts (`have-org-role-92`), roles (`:ARG1-of`), attribute values
(`:aspect state`), document-level relations (`:same-entity`). They are annotated by the same experts as
the gold you are compared with: for each sentence, look up the words and constructions you are not sure
of before you annotate it, and follow what the gold does.

- Use only this directory: the files listed here and the commands in `tools/`. Do not search the web and
  do not read anything outside this directory (the tools read their own data).

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
