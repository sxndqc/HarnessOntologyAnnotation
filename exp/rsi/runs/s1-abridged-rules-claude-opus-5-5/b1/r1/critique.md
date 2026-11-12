# Review of the instruction: error patterns in the five-sentence Chinese document, most costly first

## 1. Temporal links: every event is anchored to the document creation time (h_temporal F 30; about 13 units)

**What went wrong**
- Almost every event got its own `document-creation-time :before/:overlap` link, including:
  - events in a relative clause,
  - the second clause of a coordination,
  - a "known for" clause,
  - a negated clause.
- In gold, the sentence's main event gets one link to the document creation time. The other events in the sentence hang off that main event or a sister event with `:overlap` (or `:contained`).
- Gold also differs in three other ways:
  - It gives no temporal parent to a copular state (`identity-91`) or to a vague time word like "currently". The annotator added `present-reference :depends-on` for the time word.
  - For a sentence whose main event is a present-relevant change or naming, gold uses `document-creation-time :depends-on <event>`.
  - It always links an event nominal inside a negated predicate, a relative-clause verb, and a possession verb inside a modifier. The annotator left these with no parent.

**Why it happens:** The instruction's rule (1) time expression, (2) earlier event, (3) document creation time puts the document creation time ahead of other events in the same sentence. It also says "annotate event–event relations only when they are clear", which pushes the annotator away from same-sentence links.

**What to change:** Add this rule:
- Pick one temporal anchor per sentence: the matrix event, linked to the document creation time or a time expression.
- Every other event in the sentence takes that anchor or the event it modifies as its parent. Use `:overlap` unless the order is explicit.
- This covers subordinate, relative, complement, coordinated, cause/reason, nominal and negated events.
- Every event node, including one inside a noun-phrase modifier, must get a parent.
- Do not give a vague present-time adverb its own `depends-on` triple.
- Leave a pure copular identity state out of the temporal structure. It still belongs in the modal structure.

## 2. Function words and classifiers are dropped (a_entity_found R 85, part of d_peripheral; about 10 units)

**What went wrong**
- Gold keeps these as nodes:
  - aspectual or temporal adverbs ("already" as `:mod`, "once/formerly" as `:temporal`);
  - the "all" adverb, as `:mod` on the event;
  - "among them", as `:mod` on the noun;
  - a locative postposition after a time noun, as a `:temporal` node with `:op1`.
- Gold also keeps "one + classifier" as `:quant 1` plus `:unit <classifier>`, even for ordinary classifiers like 个 and 份.

**Why it happens:** The instruction says outright that ordinary classifiers are dropped. That contradicts the gold. It also lists auxiliaries as non-nodes, and the annotator extended that to aspectual adverbs.

**What to change:**
- Replace the classifier rule: a numeral + classifier is `:quant N` plus `:unit <classifier>`, and `:quant 1` is written too.
- State that adverbs are nodes:
  - aspect/time adverbs (already, once, still, all, also) become `:mod`, or `:temporal` for past-time adverbs;
  - a partitive "among them" becomes `:mod`.
- Only modal auxiliaries are dropped.

## 3. Arguments attached to the wrong node, and implicit arguments added (g_reentrancy F 15, d_core_args_event F 64; about 12 units)

**What went wrong**
- **Relative clause with an aspectual verb.** In a pattern like "stopped publishing" modifying a noun, the annotator made the head noun the argument of the outer verb and also of the inner verb. Gold makes the head noun `:ARG1-of` the inner verb only. The aspectual verb then takes the inner event: inner event `:ARG1-of` the aspectual verb.
- **Implicit participants.** The annotator added participants the text does not express:
  - an agent of a publishing event;
  - a possessor of a derived product;
  - the subject of a negated "undergo".

  Gold leaves them out. Re-entrancy precision was 12 %.
- **Clause describing the predicate noun.** The clause "known for X-ing" comes after a copular sentence and describes the predicate noun. Gold attaches it under that noun as `:ARG1-of`. The annotator made it a top-level `and` conjunct with re-entrant subjects.
- **Shared modifiers.** In "various strange A and B", gold copies the modifiers onto each conjunct by re-entrancy. The annotator put them on the `and` node and also added a spurious `:subset`.

**What to change:** Add these rules:
- Do not add an unexpressed argument just because the roleset has a slot. Re-enter a node only when the text expresses the participant.
- For a head noun modified by an aspectual verb plus a verb, the noun is the argument of the innermost verb.
- A modifier shared by coordinated nouns goes on each conjunct (re-entrancy), not on the coordinator.
- A clause that keeps describing a copular predicate noun attaches to that noun.

## 4. Aspect (c_aspect F 60; 5 units)

**What went wrong**
- Recurring publishing activity, and what a periodical regularly contains: gold `habitual`. The annotator used `process`, `performance` or `activity`.
- "Already" + stop, describing a current result: gold `state`.
- A negated "undergo" with a nominal object: gold `process`.
- A passive "is called/regarded as": gold `performance`.

**What to change:** Add these rules:
- Activities of an institution that repeat (publishing, broadcasting, reporting, collecting content) are `habitual`, even with a completion marker.
- "already + cease/stop" describing the current situation is `state`.
- A naming or evaluation passive is `performance`.

## 5. Concept choices (a_event_concept and core labels; about 8 units)

**What went wrong**
- **Lexical verb vs abstract predicate.** A Chinese possession/belonging verb with a PropBank frame should keep that lexical frame (holder as `ARG0`, owner as `ARG1`) instead of `belong-91`.
- **Concessive "but".** 不过 and similar words take `but-91`, not `contrast-91`.
- **Superlatives.** "most + property" is `have-degree-91`: the noun is `:ARG1`, the property event is `:ARG2`, and the degree word is `:ARG3`. Do not use `:degree` on the property verb.
- **Reason words.** 由于 and the frame 以…而 go to `:reason`. The instruction's "因为/由于 → :cause" is wrong for this data.
- **Coordinated compound noun.** A four-character compound made of two coordinated nouns is split into `and` with two ops. An idiom stays one concept.
- **Part-of and medium.** A physical edition of a publication is `:part-of` it, not `:possessor`. A medium noun ("TV") modifying a program is `:medium`.
- **Ceasing publication.** A verb of ceasing publication takes the publication as `ARG0`. Check the roleset.

**What to change:** Add these points to sections 2.3 and 2.5:
- Prefer the Chinese PropBank verb over an abstract `-91` predicate whenever a frame exists.
- Add 不过 to the list of words that take `but-91`.
- Add a `have-degree-91` row to the abstract-predicate table.
- Change 由于 to `:reason`.
- Split coordinated noun compounds into `and`.

## 6. Named entities (f_name_tokens F 50, f_wiki 0, place labels; about 7 units)

**What went wrong**
- Gold includes the title brackets 《 》 as their own `:op`s.
- Gold has no `:wiki`.
- A country name modifying a noun or "history" is `:place`, not `:mod`.

**What to change:**
- Do not write `:wiki` for this data.
- For titled works, keep the bracket tokens as the first and last `:op`.
- A country/location name modifying a common noun is `:place`.

## 7. Coreference precision (j_coref_chain P 71; 2 units)

**What went wrong:** The annotator linked a country name that appears as a modifier in two sentences. Gold links only the main discourse entity.

**What to change:** Do not build chains for incidental place names that are only modifiers. Do link every mention of the main entities.

## Minor: polarity on a negated event
The annotator put `:polarity -` on the negated event. Gold has no polarity there but still marks the event `full-negative` in the modal structure. This cost one unit; leave the rule as it is.

## What to keep
- **Modal annotation (F 94):** `root → author → full-affirmative`, and `full-negative` for negated events.
- **Senses (100):** the sense choices and the habit of looking up rolesets.
- **Abstract predicates:** core roles of the abstract predicates (100).
- **Document format (100).**
- **Coreference recall (100):** linking each mention to the closest earlier one.
- **Basic graph shape:** event-nominal aspect `process`, relative clauses as `:ARGn-of`, and the overall structure of the sentence graphs.