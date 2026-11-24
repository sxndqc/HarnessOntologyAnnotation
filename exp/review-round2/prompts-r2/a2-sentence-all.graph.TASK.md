# Task: the sentence-level UMR graph of one sentence

Your job is the sentence-level graph of one sentence of a document, in Uniform Meaning Representation
(UMR). (A later step adds the sentence's document-level relations.) You find the sentence at the end,
under **Input**. Stay in this directory; Files lists what you need. The answer goes into `answer.txt` (see
Output format), and `notes/` is yours for notes.

**Accuracy is what matters here.** Experts annotated the same sentence by these guidelines, and your graph
is checked against theirs node by node and relation by relation: each concept, sense, role and attribute
value is counted. Work as carefully and for as long as that takes:

- The examples are the model to follow: a construction that an example shows is annotated the way that
  example annotates it.
- Start by reading the guidelines closely. Whenever a decision is uncertain, return to them: which concept
  and which sense, a numbered or a non-core role, abstract concepts and named entities, aspect, modal
  strength, polarity.
- Check instead of guessing: use the three tools (see Files): search the full guidelines with
  `tools/search_guidelines.py` whenever the abridged guidelines do not settle a case, look up every
  predicate in PropBank with `tools/propbank_lookup.py` before you choose its sense and numbered roles,
  and look up how the gold data annotates a construction, a word or a relation with
  `tools/search_annotations.py`. Look things up as often as you need: many lookups are expected.
- Check the graph against the guidelines one more time before you answer: a concept for every word that
  carries meaning, an aspect for every event, the right direction for every role.

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
- Write the answer to `answer.txt` in this directory: the two header lines and the graph of this sentence,
  in the format above, nothing else.

## Input

Language: {lang_label}
Document: {doc_id}, sentence {num} of {n}

The sentence: its number, a tab, then its words separated by spaces.

{line}
