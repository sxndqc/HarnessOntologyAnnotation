# Review of the instruction: error patterns in this document, most costly first, and what to change

## 1. Temporal and modal links for nested content and for nouns treated as events (about 10 temporal units, 4 modal, 3 aspect)

**What went wrong**
- **Clause anchor.** One sentence was a coordination whose first conjunct was a topic noun (modified by a relative-clause verb and followed by a list of examples). The annotator made that noun the conjunct. So its anchor fell on the second clause, and the anchor's links were all wrong.
  - Gold makes the relative-clause verb the head of the conjunct, with the topic noun as its argument. That verb is then the anchor.
- **Content of a saying verb.** The content was an abstract predicate (`have-mod-91`) whose subject is an event nominal.
  - The annotator gave the `have-mod-91` a temporal parent.
  - It also hung the event nominal under the `have-mod-91`.
  - Gold gives the abstract predicate no temporal parent. The event under it attaches directly to the saying verb, and the parallel events of the sentence hang off that content event.
- **Event-like nouns that are not events.** Two nouns were annotated as events, each with a sense or `-00`, an aspect, a temporal triple and a modal triple. Gold makes them plain entity concepts:
  - an activity noun given as an item in an `:example` list;
  - a chengyu that is the value (`:ARG2`) of the purpose `identity-91`.

**Why**
- The "N 有 A、B…等" rule only says what to do when N has an outer role.
- 5.1 exempts only `identity-91` and `have-degree-91` from the temporal structure.
- Nothing says that list items or idioms in a naming or value slot are entities.

**Changes to the instruction**
- (a) When a topic noun with a listed `:example` stands as a clause or conjunct with no outer role, and it is modified by a relative-clause verb: make that verb the clause head (or conjunct) with the noun as its argument. That verb is the anchor.
- (b) An abstract predicate (`have-mod-91`, `have-place-91`, …) that is the complement of a saying or thinking verb gets a modal parent but no temporal parent. The events inside it take the reporting verb as their temporal parent, with `:overlap`.
- (c) An activity noun that is only an item in a topic or example list, and an idiom that fills the value slot of an abstract predicate, are entity concepts: no sense, no `:aspect`, no temporal or modal triple.

## 2. Names of fictional beings and celestial bodies (about 10 units across name tokens, entity concept, granularity and other attributes)

**What went wrong**
- **Names written as common nouns.** A fictional character's name made of ordinary words was annotated as a common noun with a `:mod`. A named alien was annotated with the category noun as the concept and `:name` holding only the rest.
  - Gold makes both `individual-person`. In the first mention it also puts the category word inside the name.
  - The wrong type spread to every check on those nodes. Most of the `c_other_attributes` precision loss comes from name ops sitting on the wrong node.
- **Celestial body.** "Earth" was written as a plain noun. It should have been `planet` + `:name`, which the instruction already requires.

**Why**
- The clause "a common category noun before a name is the concept, with `:name` for the rest" contradicts "any named being … is `individual-person`". The annotator followed the first.
- The celestial-body rule gives no Chinese example, so a word that looks like a common noun was not seen as a name.

**Changes to the instruction**
- A named being (character, alien, mascot) is always `individual-person`. Never make the category noun the concept.
- A character name made of common words (a "Bat-Boy" type name) is still a name, with every word as an `:op`.
- Say explicitly that 地球, 月球, 太阳 and similar words are names: `planet` / `star` + `:name`, even with no other naming marker.

## 3. A shortened repeat of a name in the same sentence (about 8 units: entity concept, granularity, peripheral roles, two reentrancy, three coref)

**What went wrong**
- A later bare head noun repeated the publication's full name in the same sentence. The annotator re-entered the publication's variable for it.
- Gold makes a new node for the noun, uses it (here as the `:part-of` target), and links it with `(name-node :same-entity new-node)`.

**Why**
- Section 1 ("a repeat with its own noun: see 5.3") says such a repeat is not a re-entrancy, but 5.3 says "within one sentence, coreference is a re-entrancy". The two rules conflict.

**Change to the instruction**
- Only pronouns and unexpressed mentions are re-entered.
- A mention with its own noun (a shortened name, a repeated head noun) gets its own node plus a `:same-entity` triple, even inside the same sentence.

## 4. Senses and role numbers (5 units: 2 sense errors on Chinese verbs, 2 role labels on one predicate, 1 more sense difference)

**What went wrong**
- **Wrong sense.** The annotator chose -01 twice where another sense fits:
  - a passive verb of accusing or claiming needs its "point out / claim" sense (-02 here);
  - a relationship verb ("X has a relationship with Y") needs its existential "entity exists with respect to ARG0" sense (-03 here), not possession (-01).
- **Wrong role numbers.** A "can be considered as" verb has roles `:ARG0` (thing described) and `:ARG1` (what it counts as). The annotator wrote `:ARG1` / `:ARG2` out of English habit.
- **Third difference: not a clear error.** One verb has only an `:ARG0` -01 frame in PropBank. Gold left it without a sense, so it scored as `-00` against the annotator's `-01`. The annotator's choice follows the instruction; do not change the rule for this.

**Why**
- The required lookup was not actually done.

**Change to the instruction**
- Restate the lookup as a must, with two typical traps:
  - 有 has several senses (possession, existence or relationship, inclusion of a list), so pick by the participants;
  - copular "count as" verbs (算是, 成为 type) number their roles from `:ARG0`.

## 5. Aspect of habitual and stative nominals (4 units)

**What went wrong**
- A periodical's reporting appeared as an event nominal ("its reports"). The annotator gave it `process`; gold has `habitual`. This happened twice.
- A "survive / exist" verb under "continue" got `activity`; gold has `state`.
- A generic ongoing activity nominal got `process`; gold has `activity`.

**Why**
- "Event nominal → `process`" competes with the institution-habitual rule, and the instruction does not say which one wins.

**Change to the instruction**
- The habitual rule for institutions and periodicals overrides the event-nominal default.
- Existence and survival verbs are `state`, also under "continue".
- An event nominal used as an ongoing generic activity (not a single occurrence) is `activity`.

## 6. Modal conceivers (about 4 units)

**What went wrong**
- **Unused `null-conceiver`.** The annotator wrote `(author :full-affirmative null-conceiver)` in every sentence, even where `null-conceiver` was never used.
  - **Change:** add this triple only when `null-conceiver` is actually a parent in that sentence.
- **Reported content.** Gold gives reported content both an author link and a speaker link. The annotator gave only the speaker link. Gold is not consistent here, so this is low priority; consider allowing both.
- **Agentless passive.** For an agentless passive accusation, gold uses an expressed entity as conceiver, not `null-conceiver`. This looks like a gold quirk; I would not encode it.

## 7. A locative postposition after a place noun (3 units)

**What went wrong**
- In "在 N 中" (in N), the annotator wrote `:place N`. Gold has a postposition node (`中 :op1 N`) filling the verb's location role from its frame (`:ARG1` here).

**Change to the instruction**
- Extend the 2.1 postposition rule from time nouns to place nouns: 中, 上, 里 after a place noun is a node with `:op1` N.
- That node fills the verb's location role if its frame has one; otherwise it is `:place`.

## 8. Smaller items

- **Possessive pronoun on an event nominal.** The annotator added a `:possessor` re-entrancy. Gold has nothing.
  - **Change:** extend 2.4 to say it adds no `:possessor` either.
- **Repeated adverb.** One adverb was annotated twice; gold attaches it to one predicate only.
  - **Change:** an adverb gets exactly one node, at the clause it appears in.
- **Shared time expression.** A date at the start of the sentence scopes over both clauses of a "but" sentence. Gold re-enters it as `:temporal` on the second clause too.
  - **Change:** say that a sentence-initial time expression is re-entered as `:temporal` on every coordinated clause it scopes over.

## Keep: what the annotator got right

- **Events:** events found and event concepts were perfect.
- **Pronouns:** `refer-person` and `refer-number` were perfect.
- **Clause linking:** concessive "虽然…不过" as `but-91` with an `and` `:ARG1`.
- **Purpose:** the copular 以 X 为目的 construction as `identity-91` with `:purpose-of`.
- **Lists:** `:example` lists closed with 等 as the last `:op`.
- **Roles and titles:** `have-rel-role-91` with `:place` for a title, and the appositive `identity-91` for a descriptor noun.
- **Reported speech:** `:quote` on reported content, and the speaker entity as modal conceiver.
- **Superlatives:** the superlative `implicit-argument` with `:unit`. Other gold sentences confirm `:ARG2` property / `:ARG3` degree for `have-degree-91`. The only gold sentence that differs looks idiosyncratic, so do not change that rule.
- **Temporal:** the date `:overlap` anchor pattern and the sequence `:after` in a `consecutive`.