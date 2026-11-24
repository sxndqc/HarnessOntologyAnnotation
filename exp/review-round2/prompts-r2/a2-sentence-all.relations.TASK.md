# Task: the document-level relations of one sentence

Your job is to add the UMR document-level relations (temporal, modal, coreference) of one sentence of a
document. The sentence-level graphs of all sentences are already there. At the end, under **Input**, you
find this sentence and up to five sentences that precede it, each with its graph. Stay in this directory;
Files lists what you need. The answer goes into `answer.txt` (see Output format), and `notes/` is yours
for notes.

**Accuracy is what matters here.** Experts annotated the same document by these guidelines, and your
relations are checked against theirs one by one: each temporal, modal and coreference relation is counted.
Work as carefully and for as long as that takes:

- The examples are the model to follow: a case that an example shows is annotated the way that example
  annotates it.
- Start by reading the guidelines closely. Whenever a decision is uncertain, return to them: which events
  and entities take which relations, their reference times, conceivers and modal strengths, and which
  nodes corefer.
- Check instead of guessing: use the tools (see Files): search the full guidelines with
  `tools/search_guidelines.py` for the rules of temporal, modal and coreference relations, look up how the
  gold data annotates such relations with `tools/search_annotations.py` (e.g. `:same-entity`,
  `:depends-on`, `:full-affirmative`), and look a predicate up with `tools/propbank_lookup.py` whenever
  its meaning matters for a relation. Look things up as often as you need.
- Before you answer, make sure the relations cover every event and entity of this sentence that the
  guidelines ask for.

## Files

- `guidelines/umr_guidelines_abridged.md`: the UMR guidelines, abridged (about 14,000 characters). Read
  all of it before you start.
- `tools/`: commands (run them in the shell, from this directory):

`python3 tools/search_guidelines.py KEYWORD [KEYWORD ...] [--max N]` searches the full UMR guidelines and
prints the matching passages with their headings (at most N, 1-10, default 3). Search with the terms the
guidelines would use (`aspect`, `have-rel-role-92`, `:quant`, "modal strength", `reentrancy`), and look up
each kind of construction the document has before you annotate it.

`python3 tools/search_annotations.py --language {lang} KEYWORD [KEYWORD ...] [--max N]` prints gold UMR
annotations of whole training sentences (other documents) that contain the keywords (at most N, 1-10,
default 3): words of the text, concepts (`have-org-role-92`), roles (`:ARG1-of`), attribute values
(`:aspect state`), document-level relations (`:same-entity`). They are annotated by the same experts as
the gold you are compared with: for each sentence, look up the words and constructions you are not sure
of before you annotate it, and follow what the gold does.

`python3 tools/propbank_lookup.py --language {lang} LEMMA [LEMMA ...]` prints the PropBank rolesets of up
to 20 lemmas: each roleset's id, its numbered roles and its examples. Use it when the meaning of a
predicate decides a relation.

- Use only this directory: the files listed here and the commands in `tools/`. Do not search the web and
  do not read anything outside this directory (the tools read their own data).

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
- Write the answer to `answer.txt` in this directory: the `# document level relations:` line and the
  graph, in the format above, nothing else.

## Input

Language: {lang_label}
Document: {doc_id}, sentence {num} of {n}

The previous sentences (at most five; number, tab, words):

{prev_lines}

Their graphs:

{prev_graphs}

This sentence:

{line}

Its graph:

{graph}
