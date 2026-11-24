# Task: the sentence-level UMR graph of one sentence

You annotate one sentence of a document in Uniform Meaning Representation (UMR): its sentence-level graph.
(Its document-level relations are added later, in another step.) The sentence is under **Input** at the
end. Work in this directory only; the files you need are listed under Files. Write the answer to `answer.txt` (see Output format). You may keep notes in `notes/`.

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role and attribute
value counts. Take the time this needs:

- Read the guidelines carefully before you start, and go back to them for every decision you are
  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity.
- Follow the examples: when the sentence has a construction an example shows, annotate it the way the
  example does.
- Do not guess when you can check: use the three tools (see Files): search the full guidelines with
  `tools/search_guidelines.py` whenever the abridged guidelines do not settle a case, look up every
  predicate in PropBank with `tools/propbank_lookup.py` before you choose its sense and numbered roles,
  and look up how the gold data annotates a construction, a word or a relation with
  `tools/search_annotations.py`. Look things up as often as you need: many lookups are expected.
- Before you answer, check the graph against the guidelines once more: every word that carries meaning
  has its concept, every event its aspect, every role the right direction.

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
