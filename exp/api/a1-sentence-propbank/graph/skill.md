# Skill: the sentence-level UMR graph of one sentence

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
- Do not guess when you can check: look up every predicate in PropBank with `propbank_lookup` (see Tools)
  before you choose its sense and numbered roles. Call it as often as you need.
- Before you answer, check the graph against the guidelines once more: every word that carries meaning
  has its concept, every event its aspect, every role the right direction.

## Guidelines

{guideline}

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

## Tools

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Look up every predicate (verbs, and nouns and adjectives that take arguments) before you choose its sense
and its numbered roles: compare the rolesets' meanings and examples with the sentence and take the one
that fits. Give all lemmas of a sentence (and alternate forms) in one call; call again for the next
sentences.

## Input

Language: {lang}
Document: {doc_id}, sentence {num} of {n}

The sentence: its number, a tab, then its words separated by spaces.

{line}
