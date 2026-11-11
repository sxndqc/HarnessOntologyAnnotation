# Skill: the document-level relations of one sentence

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
- Do not guess when you can check: the meaning of a predicate is in PropBank: look it up with
  `propbank_lookup` (see Tools) whenever it matters for a relation (whether an event is a state, who its
  conceiver is).
- Before you answer, check that the relations cover every event and entity of this sentence that the
  guidelines ask for.

## Guidelines

{guideline}

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

## Tools

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Use it when the meaning of a predicate decides a relation.

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
