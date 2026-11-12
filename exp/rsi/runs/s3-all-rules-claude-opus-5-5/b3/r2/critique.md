The costliest losses come from how entities and pronouns are tracked and linked: coreference scored F 13, re-entrancy F 44, temporal F 63 and modal F 72. Concepts, aspect and attributes were mostly correct. The problems below are ordered by cost.

## 1. Pronouns and repeated mentions: wrong node, so the coreference chain breaks
**Cost:** coreference R 17 / P 11 (6 of 6 chain units wrong). Also one extra entity, an extra `:ARG0`, an extra possessor re-entrancy, a missing possessor re-entrancy, plus 2 wrong concepts and 4 granularity units.

**What happened:**
- A 3rd-plural pronoun ("their reports", "their slogan") referred to the named periodical in the same sentence. The annotator made a new `person` node for it.
  - Gold re-uses the periodical's variable as the possessor.
  - Gold leaves out the possessive participant of the nominal event ("their reports") entirely.
- The next sentence's "they" was then linked to that bogus `person`, so the whole periodical chain fell apart.
- In the other direction, a shortened second mention of a name (the bare head noun of a periodical's title, used as the whole of a later part-of phrase in the same sentence) was collapsed into the full name's variable. Gold gives it its own node and a `:coref` triple inside the sentence.

**Why:** Rule 5.3 says "within one sentence, coreference is a re-entrancy" without separating pronouns from repeated nouns. Rule 2.4 says every pronoun is a new `person`/`thing` node.

**Change:**
- A pronoun whose antecedent is in the same sentence (including an organisation or publication referred to by 他们 or *they*) gets no node of its own. Re-use the antecedent's variable.
- A possessive pronoun on a nominal event does not become that event's `:ARG0`.
- A pronoun across sentences is a new node linked to the antecedent entity (here, the organisation), not to another pronoun node.
- A word that repeats a name or noun overtly (a short name, a bare head noun) always gets its own node. If it refers to an entity already in the same sentence, add a `:coref` `:same-entity` triple. Re-entrancy is only for pronouns and dropped or controlled arguments.

## 2. "虽然 … 不过/但是" in one sentence
**Cost:** a wrong root, the two missing `:ARG1`/`:ARG2` links, and the knock-on effects on temporal and modal parents.

**What happened:** The annotator used `:concession` on the main clause. With both markers in the same sentence, gold uses `but-91` with `:ARG1` = the 虽然 clause(s) and `:ARG2` = the 不过 clause. It also put an extra `:mod` 都 on the root; gold has no such node.

**Why:** Rule 2.5 maps 虽然 to `:concession` and says nothing about the paired form.

**Change:** When a concessive marker (虽然, 尽管, *although*) is followed by 但是/不过/却 in the same sentence, use `but-91 :ARG1 <concessive clause> :ARG2 <main clause>`. Keep `:concession` for unpaired 虽然.

## 3. `:quote` on reported content is skipped
**Cost:** 5 missing re-entrancy edges.

**What happened:** Every top node of reported content needs `:quote` pointing to the reporting verb. This covers each conjunct of a reported consecutive or `and` chain, and the content of a quoted slogan inside an `identity-91` (there the `:quote` points to that `identity-91`). The annotator added none of these.

**Why:** Rule 3 calls `:quote` something "the UMR release data also marks", which sounds optional.

**Change:** Make it mandatory. Every top event of reported or quoted content (including passive "被指/被称", "is said to"), and each of its conjuncts, gets `:quote <reporting event>`. The content of a quoted slogan gets `:quote` on the frame that introduces it.

## 4. Rules already in the instruction but not applied
**Cost:** 3 missing re-entrancy edges (in a 3-of-6 re-entrancy total).

**What happened:**
- **Control with an event nominal:** the subject of 停止 was not re-entered as `:ARG0` of its nominal complement.
- **Shared time expression:** a date scoping over both halves of a `but-91` was not attached to the second clause too.
- **Consecutive chain with one subject:** in a 后来 chain whose clauses share a subject, gold re-enters that subject as the `:ARG0` of the later verb. Gold also gives the 还 in "后来还" no node. The annotator did neither, which follows the instruction's ban on dropped-subject re-entrancy.

**Change:**
- Put the first two rules in the checklist so they are applied.
- Add an exception to the no-borrowing rule: in a `consecutive` (后来) chain, a dropped subject of the later clause re-enters the first clause's subject.
- 还/也 directly after 后来 gets no node.

## 5. Frequency adverbs and location postpositions
**Cost:** 2 wrong peripheral labels, and the peripheral-event check scored F 50.

**What happened:** 经常 and 重复 should be `:frequency`. The annotator used `:mod` and `:manner`.

**Change:** Add a rule: frequency adverbs (经常, 常常, 往往, 重复, 屡次; *often, repeatedly*) → `:frequency`. Also note that 3.1 makes time adverbs `:temporal`; frequency adverbs are their own class.

**Locations:**
- "在 N 中/上/里" should be a postposition concept: `(中 :op1 N)`. The annotator dropped the postposition.
- For appearance and existence verbs whose roleset has a location argument (出现), the location is a numbered argument, not `:place`.

**Change:** Extend the 上 rule (in 3.1) to every location postposition: (`中`/`上`/`里` `:op1 N`). Tell the annotator to check the roleset for a location argument before using `:place`.
- Note that gold here gave the theme `:ARG0` and the location `:ARG1`, the reverse of the PropBank glosses. Flag this verb class like the belong-type note: follow gold practice, not the glosses.

## 6. Named characters and a noun before a name
**Cost:** 2 wrong concepts, 2 granularity units, 2 name-token units, 1 extra `identity-91`, and an extra cross-sentence coreference.

**What happened:** Named fictional characters were typed `person`; they should be `individual-person`. A category noun written right before a name (alien + name) was reified as an `identity-91` apposition. Gold either puts the noun inside the name or uses it as the entity's type concept.

**Change:**
- Every named individual, fictional or not, is `individual-person` unless a category noun right before the name serves as its type.
- A bare category noun right before a name (no 的, no title) is not an apposition: use it as the type concept, or as the first `:op` of the name.
- Reserve `identity-91` for descriptive noun phrases.

## 7. Temporal anchor and its parents in multi-clause sentences
**Cost:** about 8 temporal units.

**What happened:**
- **Anchor choice:** In a two-clause `and`, gold anchors on the first clause's event and hangs the second on it with `:overlap`. The annotator anchored on the later verb.
- **Reported clause:** The reported event links to the saying verb. A `have-mod-91` or `identity-91` that frames it gets no temporal parent. Later reported or habitual events `:overlap` that first content event, not the saying verb.
- **Habitual relative clause:** A habitual relative-clause verb on an object got a temporal link; gold gives it none.

**Change:**
- In coordination, the anchor is the first conjunct's main event.
- Abstract predicates (`have-mod-91`, `identity-91`) never get a temporal parent, even inside reported content. Their eventive argument takes the matrix verb as parent.

## 8. Modal parents of reported content
**Cost:** about 7 modal units.

**What happened:**
- In the sentence with a slogan and a concessive, gold gives the speaker as a modal parent for the main reported event and the slogan's event. For the main claim's `have-mod-91` and the slogan's event, gold also adds an `author :full-affirmative` link.
- The slogan's `identity-91` has only `author` as parent.

**Change:** Keep speaker → content. Add `author` as a second parent for the content of a claim the author reports and then contrasts. Give the frame (`identity-91`) of a parenthetical quotation `author` as its parent.

## 9. Word-level concept choices
**Cost:** a few units each.

- **Fixed word vs. its first character:** For a word in PropBank as a whole (e.g. *X-是*), use that roleset, not the roleset of its first character. Look up the full word first.
- **Classifier in an adjective:** In a compound like 最大宗, the classifier is a `:unit` and the property is the adjective alone. The degree frame takes the property as `:ARG1` and the degree word as `:ARG2`, and 其中 goes on it as `:ARG5`. Gold's unusual role order here is a convention worth stating.
- **Unnamed omitted head:** An omitted head noun is `implicit-argument`, not `thing`.
- **Named celestial bodies:** These are named entities (`planet`, …).
- **Bound modifiers in compounds:** A bound modifier glued to a noun (母公司) is split into head + `:mod` when gold splits it, as for other modifier + head compounds.
- **Activity, not process:** A verb-nominal used as a predicate argument and describing an ongoing activity got `process`; gold uses `activity`.

## What the instruction should keep
These parts worked and should stay as they are:
- Chinese name splitting and title marks in names; `newspaper` as the periodical type.
- `have-rel-role-91` for first lady, with `:place` and `前` as `:mod`.
- `identity-91` with `目的 :purpose-of` for a purpose stated as a noun.
- `:example` (with 等 as the last `:op`) for "N 有 A、B等".
- The `but-91` with `:part-of` for an edition noun.
- Habitual aspect for publishing and reporting.
- `performance` for completed speech acts.
- The date `:overlap` and `document-creation-time :before` pattern.
- The modal frame: speaker as parent for reported content, `neutral-affirmative` for 可.

Person, number and other attributes and the document format scored 100. Concept, sense and aspect choices were at 88–95.