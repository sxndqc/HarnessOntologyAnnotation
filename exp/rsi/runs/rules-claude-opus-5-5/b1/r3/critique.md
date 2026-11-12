Here are the error patterns, most costly first. Overall the annotation is strong: concepts, senses, entities, names, non-core roles and coreference all scored 100. Almost all the loss is in document-level temporal and modal links, plus one role-direction error.

## 1. Temporal links of secondary events: the instruction's own rules point the wrong way (h_temporal F 65; 6 units)

**a) Aspectual verb with an event complement, in the second clause of a contrast** (2 units wrong, and an `:after` link that gold doesn't have)
- What happened: the annotator made the inner (complement) event the anchor. It linked the aspectual verb to that inner event, and made the first clause's event `:after` the inner event.
- What gold does:
  - the first clause's event is the anchor;
  - the aspectual verb `:overlap`s that anchor;
  - the complement event is the child of the aspectual verb (`aspectual :overlap inner`).
- Why: the instruction says this ("the inner event is the anchor; the aspectual verb `:overlap`s the inner event"), and the annotator followed it.
- Change: rewrite the aspectual-verb rule:
  - The aspectual verb is the parent of its complement event, with `:overlap`.
  - The aspectual verb hangs on the sentence anchor like any other clause predicate. In a contrast or coordination, that is `:overlap` with the first clause's anchor.
  - Keep the "inner event is the anchor" reading only when the aspectual verb is inside a relative clause.
  - Never use `:before`/`:after` between clauses that both describe the present situation.

**b) Relative-clause states inside a noun phrase** (1 temporal unit and 1 modal unit missing)
- What happened: a relative-clause verb with its own `:aspect` (a "belongs to X" state modifying the object) got no temporal and no modal parent.
- What gold does: gives it `main-verb :overlap state` and `author :full-affirmative`.
- Why: the instruction's list of things that get no temporal parent includes "a relative-clause state". The annotator also carried that over to the modal layer.
- Change:
  - Delete "a relative-clause state" from that list.
  - Add: every node that carries `:aspect` gets a modal parent. It also gets a temporal parent, normally `:overlap` with the event it modifies or with the clause's anchor.
  - Only property words used as plain `:mod` (no aspect) get no links.

**c) "Famous for X" inside a defining "A is a B" sentence** (1 unit partial, 1 extra, 1 wrong parent)
- What gold does:
  - The fame state gets no temporal parent of its own. It is the parent of the relative-clause habitual event (`fame :contained habitual-event`), and that event also keeps `document-creation-time :before`.
  - The reason event (what the newspaper is famous for reporting) hangs on the habitual relative-clause event (`:overlap`), not on the fame state.
- What happened: the annotator made the fame state a child of the habitual event and the reason a child of the fame state.
- Change: state this pattern as a rule. The current text ("states or reasons that hang on it link to it") gives the opposite direction.

## 2. Modal parents (i_modal R 81; 3 units)

**a) Copular `identity-91` had no modal parent** (1 unit)
- Gold gives it `author :full-affirmative`, even though it has no temporal parent.
- Why: the instruction's "no temporal parent for copular predicates" was carried over to the modal layer.
- Change: add "Copular and identity predicates get no temporal parent but do get a modal parent (`author :full-affirmative`)."

**b) Event nested under a fused-negation verb** (1 unit, wrong parent)
- Gold's parent is `author :partial-affirmative`. The annotator used the negated verb as the parent.
- Why: the instruction gives the strength but not the parent.
- Change: add "Its parent is `author`, not the negated verb."

**c)** The relative-clause state in 1b (1 unit), fixed by the rule there.

## 3. Role direction of the belong-type roleset in a relative clause (d_core_args_event, e_core_labels, g_reentrancy; 4 units)
- What happened: in "N that belongs to X", the annotator made N `:ARG1-of` and X the `:ARG0`.
- What gold does: the owned thing N is `:ARG0-of`, and the owner X is `:ARG1`.
- Why: the PropBank role description of this roleset reads the other way round ("ARG1: entity belonging to arg0"). The annotator trusted PropBank over the vague warning in the instruction.
- Change: make the warning concrete.
  - "For Chinese belong-type rolesets (X belongs to Y), the gold convention is: the thing that belongs = `:ARG0`, the owner = `:ARG1`. Apply this even where the PropBank role glosses seem to say the reverse."
  - "So 'N that belongs to X' is `N :ARG0-of (belong :ARG1 X)`."

## 4. Aspect of "continue doing X" in the present (c_aspect; 1 unit)
- Gold uses `activity`; the annotator used `state`.
- Why: step 2 of the aspect order ("an aspectual verb taking an event complement that describes a present condition → state") is too broad.
- Change: limit step 2 to verbs of stopping or completion with "already" (these stay `state`). An aspectual verb of continuation or ongoing action in the present is `activity`.

## 5. Alignment of a word that occurs twice (a_granularity; 2 units)
- A common noun that also appears inside a name was matched to the name's span instead of to its own occurrence. This was probably an alignment slip.
- Change: add "When a word occurs more than once in a sentence, align each node to its own occurrence."

## What to keep
These worked and the instruction should keep the rules behind them:
- Title marks inside names, and newspaper as the type of a periodical.
- Classifier kept as `:unit`.
- `:place` for country modifiers and `:medium` for channel nouns.
- `:part-of` for an edition of a publication.
- `have-degree-91` with an eventive `:ARG2`.
- The postposition time-span `:temporal` with `:place` on the history noun.
- The fused-negation verb with `process` aspect and `full-negative`, and no `:polarity`.
- Process noun + procedure noun reified with `identity-91`.
- The nested `and` for mixed separators.
- Re-entrant shared modifiers on coordinated nouns.
- `habitual` for publishing and reporting.
- `document-creation-time :depends-on` for present-situation and naming sentences.
- The coreference chain to the closest earlier mention.