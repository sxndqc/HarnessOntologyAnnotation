The costliest losses were temporal links (F 47), aspect (F 60), re-entrancy (F 18) and peripheral roles (F 33/48). Next came smaller structural slips in classifiers, name tokens, discourse frames and degree. Senses (100), document format (100), modal (91) and event detection (97) were strong. Some gold choices below are quirky, so where the gold data shows a pattern I describe the pattern rather than claim it is the guideline rule.

## 1. Temporal links: an anchor for every node, all hung on the document time (h_temporal, about 11 units, P 41)
**What went wrong:**
- **Too many anchors.** Every event and every time expression got a temporal parent. That included:
  - the copular identity predicate at the root of a defining sentence;
  - a "famous for" state;
  - a property word in a modifier;
  - a vague time word like "currently".

  Gold gives none of these a temporal parent.
- **Wrong parents inside a sentence.** Gold chains the events to each other. The publishing event is the parent, the "stopped" state overlaps it, and the "famous" state is `:contained` in it. The annotator instead hung several events on the document-creation-time, or on the time word.
- **Wrong relation.** For the main event of a present-situation sentence, gold uses `(document-creation-time :depends-on event)`; the annotator used `:overlap`.

**Why:** Section 5.1 says that every event and time expression gets a parent and that vague time words depend on past/present-reference. Nothing tells the annotator to limit links, so it over-generates.

**Change to the instruction:**
- Give temporal parents only to real eventive predicates, not to copular or identity predicates, plain states used as attributes, or property modifiers.
- Do not give vague deictic time words ("now", "currently") a parent of their own.
- Within a sentence, pick one anchor event and link the other events to it (`:overlap` / `:contained`), not each one to the document time.
- Link the anchor event to the document time.
- Precision matters as much as recall: leave out a link when unsure.

## 2. Aspect of recurring and resultative events (c_aspect, 8 units, F 60)
**What went wrong:**
- **Recurring activities.** An organisation's or periodical's regular activity (publishing, compiling content, continuing to publish) was marked endeavor, performance or activity. Gold marks it habitual, even when it is in the past or under an aspectual verb such as "continue" or "stop".
- **Resulting condition.** "Has already stopped", used to describe the current condition, was marked performance; gold marks it state.
- **Negated process noun.** A process named by a noun after a negated "undergo" verb was marked performance; gold marks it process.
- **Passive naming.** A passive verb of naming ("is called X") was marked state; gold marks it performance.

**Why:** Table 4.1 points to "completed past → performance" and "ongoing → activity" without asking first whether the event is a recurring routine.

**Change to the instruction:** Add a decision order:
1. Is the event a routine or recurring practice of its subject (publishing, reporting, compiling)? Then it is habitual, whatever the tense or aspectual verb.
2. Does an aspectual or completive predicate ("already stopped", "has ended") describe a present condition? Then it is state.
3. Is the event a process noun, including the object of a light or experiential verb? Then it is process.
4. Is it a verb of naming or labelling? Then it is performance.

## 3. Modifiers and arguments attached to the wrong node (d_peripheral, g_reentrancy, about 12 units)
**What went wrong:**
- **Adverbs dropped.** Content adverbs ("already", the scope adverb "all/both") had no node or sat on the noun. Gold puts them as `:mod` on the predicate.
- **Shared modifiers on a coordination.** Adjectives that modify both conjuncts were put once on the `and` node. Gold puts them on each conjunct and re-uses the same variable (re-entrancy).
- **Arguments filled from context.** The annotator added a participant to a noun compound that has an event modifier ("X-verification procedure") by taking it from the context. The compound's own noun is the argument.
- **"Famous for X" clauses.** The annotator made such a clause a separate `and` conjunct with a `:manner` role. Gold attaches "famous" to the noun it describes as `:ARG1-of` and makes the X clause a `:reason`. The X clause's agent is that noun, not the subject's name node.

**Change to the instruction:**
- Every adverb that carries meaning gets a node. Attach it with `:mod` to the predicate it scopes over, not to a noun.
- A modifier distributed over coordinated nouns goes on each conjunct, as a re-entrancy.
- Fill only the arguments the syntax provides; do not borrow them from elsewhere in the sentence.
- For "known/famous for X" (以…而闻名): the famous thing is `:ARG1`, and X is `:reason`.
- When a "known for" clause follows "A is a B", attach it inside the B noun.

## 4. Non-core role labels (e_peripheral, d_peripheral_entity, about 7 units)
**What went wrong:**
- A country modifying a noun ("American tabloid", "American history") got `:mod`; gold uses `:place`.
- A medium noun on a programme ("TV programme") got `:mod`; gold uses `:medium`.
- A part of a whole ("print edition of the paper") got `:possessor`; gold uses `:part-of`.
- A causal phrase (由于) got `:cause`; gold uses `:reason`.

**Change to the instruction:**
- A country or place word modifying a noun → `:place`.
- A channel or medium noun → `:medium`.
- An edition, section or component of a whole → `:part-of`.
- Use `:reason` for 由于/因为 phrases that give a reason for a state or a judgement. Section 2.5 currently says `:cause`; fix it.

## 5. Classifiers and measure words (c_other_attributes, a_entity, 5 units)
**What went wrong:** The annotator dropped ordinary classifiers, following the instruction. Gold keeps them: `:quant 1 :unit (份/个)`. Gold data does this consistently (个, 面, 只, 位).

**Change to the instruction:** Replace the rule "an ordinary classifier is dropped" with this: numeral + classifier → `:quant N :unit (classifier)`. Keep a demonstrative + classifier as `:unit` as well.

## 6. Named-entity tokens (f_name_tokens, 2 units, plus a mismatch on the classifier node)
**What went wrong:** In the gold, the book-title marks 《 》 are their own `:op`s of the name. The annotator left them out.

**Change to the instruction:** Include the title brackets as the first and last `:opN` of a work or publication name.

## 7. Superlatives and degree (a_event, d_core, 3 units)
**What went wrong:** "The most creative X" was written as `:degree (most)` with the noun as `:ARG0`. Gold uses `(X :ARG1-of (have-degree-91 :ARG2 property :ARG3 最))`. A property word in an attributive clause ("absurd content") should be a plain `:mod`, not an event with aspect, temporal and modal links. That extra event cost 3 more units.

**Change to the instruction:**
- Comparatives and superlatives use `have-degree-91`. Keep `:degree` only for plain intensifiers such as "very".
- State the existing rule more forcefully: an attributive property word, including a chengyu, is a `:mod` concept, not an event.

## 8. Discourse-frame roles (e_core_labels, 2 units)
**What went wrong:** `but-91` and `contrast-91` take `:ARG1` and `:ARG2`. The annotator used `:op1` and `:op2`, and also put a clause-level time word on the frame instead of on the clause it modifies.

**Change to the instruction:** Say this explicitly in 2.5, and require time adverbials to attach to the event they modify, never to the discourse node.

## 9. Over-linking coreference and negation (j_coref, c_polarity, i_modal, about 5 units)
**What went wrong:**
- **Coreference.** The annotator linked two different cessation events as `:same-event`: stopping publication and ceasing print. Gold does not link them.
- **"Not undergone" (未经).** The annotator put `:polarity -` on the event. Gold keeps it as full-negative in the modal layer without `:polarity`. It also gives the embedded process noun partial-affirmative strength, not full-negative.

**Change to the instruction:**
- Use `:same-event` only when the mentions are clearly the same event instance with the same participants.
- A negator fused into a verb (未经) is recorded as modal full-negative on that verb. The negation does not automatically pass to the events nested under it.

## Keep these
- **Senses.** Looking up every predicate in PropBank gave a perfect sense score. One caveat: on the possessive 属 the annotator's argument order followed PropBank, but gold reverses it. Where they conflict, check gold usage.
- **Entity coreference.** Linking each mention of the same entity to its closest earlier mention was all correct (recall 100).
- **Modal links.** `(root :modal author)` followed by author full-affirmative for asserted events worked well (F 91).
- **Name handling.** The type + name structure, Chinese word-level `:op`s, `identity-91` for "A is a B", and a `but-91` root for 不过 were all right.
- **Document format.** The document-level format was perfect.