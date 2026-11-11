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
- Do not guess when you can check: use the three tools (see Tools): search the full guidelines with
  `search_guidelines` whenever the guidelines above do not settle a case, look up every predicate in
  PropBank with `propbank_lookup` before you choose its sense and numbered roles, and look up how the gold
  data annotates a construction, a word or a relation with `search_annotations`. Call them as often as you
  need: many calls are expected.
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

`search_guidelines(keywords, max_results)` searches the **full** UMR guidelines (umr4nlp/umr-guidelines,
the document the guidelines above abridge) and returns the matching passages with their headings, with
their examples. The abridged guidelines leave out most details and examples, so use it a lot: look a rule
up whenever you are not sure of a case (an abstract concept, a role, a named entity type, an aspect or modal
value, a temporal or coreference decision), and look up each kind of construction the document has before
you annotate it. Search with the terms the guidelines would use (`aspect`, `have-rel-role-92`, `:quant`,
`modal strength`, `reentrancy`). Note that the full guidelines often write the older short names (AUTH,
DCT, FullAff, :modstr); your answer uses the release names listed under Output format.

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Look up every predicate (verbs, and nouns and adjectives that take arguments) before you choose its sense
and its numbered roles: compare the rolesets' meanings and examples with the sentence and take the one
that fits. Give all lemmas of a sentence (and alternate forms) in one call; call again for the next
sentences.

`search_annotations(language, keywords, max_results)` returns gold UMR annotations of whole sentences of the
training data (other documents) that contain the keywords: words of the text, concepts (`have-org-role-92`), roles
(`:ARG1-of`), attribute values (`:aspect state`), document-level relations (`:same-entity`). These are
annotated by the same experts as the gold you are compared with, so they show how this data annotates a
case. Use it a lot: for each sentence, look up its words and constructions you are not sure of (a word's
concept and sense, a light verb, a modal word, a named entity, a comparison, a quantity, a discourse
relation, the aspect of a kind of event) before you annotate it, and follow what the gold does.

## Input

Language: {lang}
Document: {doc_id}, sentence {num} of {n}

The sentence: its number, a tab, then its words separated by spaces.

{line}
