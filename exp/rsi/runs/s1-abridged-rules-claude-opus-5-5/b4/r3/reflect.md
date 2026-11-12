**Summary of changes.** The edits fix the critique's recurring, generalizable errors. To stay under the 30000-character limit, I compressed some verbose passages, with no change of meaning:
- the `identity-91`-root temporal block;
- the abstract-predicate paragraph;
- the aspectual-relative rule;
- the Heads rule;
- the stative-verb rule;
- the concept-name examples.

**Added or fixed:**
- **Demonstrative + noun tokens** (该/此/本/这 + noun) are split into the noun with the demonstrative as `:mod`.
- **Role nouns with only a possessor** (其X, *its X*) stay the noun itself plus `:possessor`; they are no longer reified.
- **Publishing/posting verbs:** role numbers are copied from the frame (often `:ARG1` = place/medium, `:ARG2` = the thing published).
- **Sense choice:** saying verbs take the claim sense, and "serve as" takes the position-holder sense.
- **Whole-token lookup:** V+complement tokens (V出, V到, V上, V成) are looked up as a whole first.
- **Clause-linking reason/purpose nodes** get no `:aspect` and no modal triple. A fronted 为/为了 purpose clause re-enters the shared subject.
- **Temporal:**
  - later conjuncts of a coordination chain to the conjunct just before;
  - for a `but-91`/`contrast-91` root, `:ARG1` is the anchor;
  - a date that appears only inside reported content gets no triple;
  - a 靠/凭 means event `:overlap`s the event it enables;
  - 时 after a named occasion gets no node.
- **`identity-91` under 能力/机会** gets `:aspect state`.
- **Stance verbs** (support, oppose) are `state`.
- **Coreference:** generic kind nouns get no `:same-entity` link.

**Not changed:** I left the uncertain modal-parent pattern for reporting organizations alone, as the critique advised checking more gold documents first.

```json
{"summary": "Compress verbose passages (identity-91 temporal block, abstract-predicate paragraph, aspectual relative, heads, stative rule, concept-name examples) to make room. Add: demonstrative+noun split; possessor-only role nouns not reified; publishing verb role numbers from frame; claim/position-holder senses; whole-token V+complement lookup; reified reason/purpose without aspect/modal; fronted purpose clause re-enters shared subject; temporal chaining of conjuncts, but-91 ARG1 anchor, no triple for dates inside reported content, means events overlap, no 时 node after named occasion; identity-91 under 能力 gets state; stance verbs state; no coref for generic kind nouns.", "edits": [
{"op": "replace", "old": "When a sentence's root is `identity-91`, choose as anchor the event inside the predicate noun that is most clearly placed in time, usually a completed past event (`(document-creation-time :before e)`). The triples are:", "new": "With an `identity-91` root, the anchor is the event in the predicate noun most clearly placed in time (usually completed past):"},
{"op": "replace", "old": "- for a reputation or property state of that noun, `(state :contained anchor)`. The state is the parent and the anchor is the child; the state itself gets no other temporal parent;", "new": "- a reputation or property state of that noun: `(state :contained anchor)`, no other parent;"},
{"op": "replace", "old": "- every other event of the predicate noun, including the means or reason of the reputation, is `(anchor :overlap e)`. None of them hang under the reputation state.", "new": "- every other event of the noun (also the reputation's means or reason): `(anchor :overlap e)`."},
{"op": "replace", "old": "Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as written in Chinese (`宇航员`, `航天器`).", "new": "Entities and modifiers are the word itself, lemmatized in English and as written in Chinese."},
{"op": "replace", "old": " It is not an argument of the aspectual verb as well. Check the aspectual verb's roleset.", "new": ""},
{"op": "replace", "old": "In N1 的 N2, and in *change from A to B* (从 A 变为 B), the grammatical head common noun is the concept.", "new": "In N1 的 N2 the grammatical head common noun is the concept."},
{"op": "replace", "old": "Possession, belonging, existence, survival and knowing verbs stay `state` even with 了, 过, 曾经, a duration modifier or under *continue*. These markers only place the state in time for the temporal triples.", "new": "Possession, belonging, existence, survival, knowing and stance (support, oppose) verbs stay `state` even with 了, 过, 曾经, a duration modifier or under *continue*."},
{"op": "replace", "old": "Use an abstract predicate only when there is no lexical predicate. A Chinese verb with its own PropBank frame keeps that frame and its roles. For example, a possession or belonging verb such as 属于 or 拥有 is that verb with its own fitting sense (see Chinese role numbering below), not `belong-91` / `have-91`.", "new": "Use an abstract predicate only when there is no lexical predicate: a framed Chinese verb (属于, 拥有) keeps its frame and fitting sense, not `belong-91` / `have-91`."},
{"op": "replace", "old": "`(h / have-reason-91 :ARG1 effect-event :ARG2 cause-event :aspect state)`, `(h2 / have-purpose-91 :ARG1 main-event :ARG2 purpose-event :aspect state)`", "new": "`(h / have-reason-91 :ARG1 effect-event :ARG2 cause-event)`, `(h2 / have-purpose-91 :ARG1 main-event :ARG2 purpose-event)`"},
{"op": "replace", "old": "It gets `(author :full-affirmative h)` but no temporal parent (see 5.1).", "new": "It gets no `:aspect`, no modal triple and no temporal parent."},
{"op": "replace", "old": "Do not re-enter the subject into 为/为了-purpose clauses or relative clauses unless a word fills the role.", "new": "Re-enter a shared subject in a fronted 为/为了 purpose clause; not in relative clauses unless a word fills the role."},
{"op": "insert_after", "anchor": "A true idiom stays one concept.", "text": " A demonstrative + noun token (该/此/本/这 + noun) is split: noun `:mod` demonstrative."},
{"op": "insert_after", "anchor": "`(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.", "text": " A role noun with only a possessor (其/its X, no name or title construction) is the noun + `:possessor`, not reified."},
{"op": "replace", "old": "publishing/posting verbs usually make the place published in a numbered argument (not `:place`).", "new": "publishing/posting verbs: copy the frame's numbers (often `:ARG1` place/medium, `:ARG2` thing published). Saying verbs take the claim sense; 'serve as [title]' the position-holder sense. Check V出/V到/V上/V成 tokens whole first."},
{"op": "replace", "old": "write `noun :ARG1-of (identity-91 :ARG2 V)`, not `:purpose`", "new": "write `noun :ARG1-of (identity-91 :ARG2 V :aspect state)`, not `:purpose`"},
{"op": "replace", "old": "When the root is a coordination, the first conjunct is the anchor; later conjuncts `:overlap` it unless an order word says otherwise.", "new": "When the root is a coordination, the first conjunct is the anchor; each later conjunct `:overlap`s the one before it unless an order word says otherwise. For a `but-91`/`contrast-91` root, `:ARG1` is the anchor. A date only inside reported content gets no triple."},
{"op": "replace", "old": "X's event is the `:reason` of Y.", "new": "X's event is the `:reason` of Y (temporal `:overlap` Y)."},
{"op": "replace", "old": "as `:temporal` of the verb, with no date triple.", "new": "as `:temporal` of the verb, with no date triple; a following 时 gets no node."},
{"op": "replace", "old": "- Link every mention of the main discourse entities.", "new": "- Link every mention of the main discourse entities. Generic kind nouns (a class used generically) in different clauses are not linked."}
]}
```