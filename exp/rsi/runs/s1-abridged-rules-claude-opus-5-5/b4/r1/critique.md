# Review of the UMR annotation of sentences 16–20: costly error patterns and changes to the instruction

The patterns are ordered by cost, highest first. Counts are approximate units from umrjudge.

## 1. Property words were left as plain modifiers or wrapped in `have-mod-91` (about 35 units, the largest cost)

**What went wrong.** Chinese adjectives and stative words should be events, but the annotator left them out. This covers:
- a predicative adjective in a concessive clause;
- adjectives in "X 与 Y" coordinations under a verb;
- attributive adjectives on nouns, such as "real news", "prominent position" and "composite photo";
- the stative part of an agent compound.

The gold makes each of them a `<word>-01` event with `:aspect state`. The described noun is `:ARG0` of the event (written `:ARG0-of` when the word modifies the noun). Each event also gets `(parent :overlap e)` and `(author :full-affirmative e)`.

The annotator instead used `have-mod-91` (wrong concept, wrong arguments, and a wrong anchor for the sentence), `:mod`, or `:possessor`. This shows up in b_event_sense, c_aspect, d_core_args, h_temporal and i_modal. Another gold document (an attributive adjective done as `:ARG0-of 特别-01 :aspect state`) confirms the practice.

**Why.** Section 2.1 lists "property words used as plain modifiers" as not events. Section 2.3 says to use `have-mod-91` for "X is Adj". Both are English-centred rules.

**Change.** Add a Chinese rule: a Chinese adjective or stative word that has a PropBank frame is always an event, whether it is a predicate or an attributive modifier (with or without 的).
- Predicate: `(e / Adj-01 :ARG0 theme :aspect state)`.
- Attributive: `(n / noun :ARG0-of (e / Adj-01 :aspect state))`.
- In both cases, use the role number the roleset gives; it is often `:ARG0`.
- It gets temporal `:overlap` with its governing event and `(author :full-affirmative e)`.
- Use `have-mod-91` only when the property word has no frame.
- Keep the "not events" clause only for non-frame modifiers, such as demonstratives, plain nouns and sense-less words.

## 2. A quoted headline was annotated as an inner clause instead of as a named work (about 25 units)

**What went wrong.** An article title in 「 」 brackets was the object of a publishing or reporting verb, counted with an article classifier ("一篇 「…」") or placed after "新闻". The annotator parsed its content into events, countries, persons and `:quote` links, plus an `implicit-argument` head. This produced many extra nodes, modal and temporal triples, and reentrancies.

The gold makes the title `publication :name` with every word as an `:opN`, the brackets included, and `:quant 1 :unit 篇` on that node. When an article noun is present, the gold links them as `(noun :ARG1-of (identity-91 :ARG2 publication-name))`. The title's content gets no events and no modal or temporal triples.

**Why.** Section 2.2 gives the bracket rule only for 《 》. Nothing distinguishes a quoted title from quoted reported content.

**Change.** Add this rule: a quoted string that names an article or headline is a named `publication`, and its whole text, brackets and punctuation included, is split into `:op`s. Treat it this way when it is:
- counted with an article classifier (篇, 则);
- in apposition to an article noun; or
- the object of a publishing verb.

No inner structure is built for it. Keep the clause analysis plus `:quote` only when the quotation is the direct content of a verb of saying or reporting and has no article classifier or article noun.

## 3. The wrong sense, the wrong frame roles, or a split compound verb (about 15 units)

**What went wrong.**
- A verb of claiming was given the "refer to" sense instead of the "point out / claim" sense.
- A verb of holding a position was given its first sense instead of the position-holder sense.
- 有 + ability was given `有-01` instead of the sense for an entity described as having something.
- A V到 token that has its own frame was cut back to the bare verb. PropBank has 贴到-01 (ARG1 is the place, ARG2 is the thing posted).
- A verb + directional complement written as two tokens was not merged, although PropBank has the compound (点出-01).
- For publishing verbs, the frame's location role is `:ARG1` and the published item is `:ARG2`. The annotator used `:place` and `:ARG1`.
- The subject of "be elected" took `:ARG1` instead of the frame's `:ARG0`.

**Why.** The lookup rule exists in the instruction but was not applied fully. It also does not cover verb + complement written as separate tokens.

**Change.** Strengthen step 1 of the Chinese role-numbering rule:
- Always look up V+complement tokens (V到, V出, V上) as a whole before falling back to the bare verb.
- When the complement is a separate token, also look up the joined form, and if it has a frame, make it one concept aligned to both tokens.
- Add an explicit check: for publishing and posting verbs, the location is a numbered argument, not `:place`.
- Restate that roles are always copied from the chosen sense, including for change-of-state and election verbs.

## 4. Specific reports by a periodical were marked `habitual` (about 6 units)

**What went wrong.** Specific reporting, publishing and deleting acts, each about one particular article or event, were marked `habitual` because of the rule on "repeated activity of an institution". The gold uses `performance`.

**Change.** Narrow that rule. `habitual` applies only to the generic, regular activity of a periodical (what it publishes or covers in general). A single act tied to one specific item or occasion is `performance` when it is completed, even when the agent is a publication.

## 5. Focus and additive adverbs became nodes (about 7 units)

**What went wrong.** The annotator made nodes for "even" (甚至) and for an additive 还 linking coordinated clauses. In sentences 16–17 the gold had no node for 也. The instruction's "adverbs are nodes" rule caused this.

**Change.** Add to the no-node list (where 就 and 便 already are):
- 甚至 / *even*;
- 还 and 也 when they only link a clause to a preceding clause or sentence.

Keep 也 or 还 as `:mod` only when it scopes over an argument inside one clause. Gold practice on 也 is inconsistent: sentence 19 keeps one, so this split is a judgement call.

## 6. A means verb was kept as its own event (about 5 units)

**What went wrong.** In "靠 X 而/to achieve Y", the annotator made 靠 an event with `:manner`. The gold drops 靠 and makes X the `:reason` of Y. X's event carries `:quote` from the reporting verb, like the main content.

**Change.** Add a rule: a reliance or means verb introducing the cause of a result (靠, 凭, 借) gets no node. Its object event is `:reason` of the result event.

## 7. Compounds and word-internal structure were not split (about 6 units)

**What went wrong.** Three kinds of compound were kept whole:
- a V+人 compound for a kind of entity;
- 全 + noun;
- a V+者 agent compound outside a role construction.

The gold splits them as follows:
- V+人 → `人 :ARG1-of V-01 :aspect process`;
- 全 + noun → noun `:mod 全`;
- V+者 → `者 :ARG0-of V-0x`.

**Change.** Make the agent-noun decomposition of section 2.3 general, so it applies wherever the noun occurs. Extend it to V+人 patient compounds (written `:ARG1-of`). Split 全/各 + noun into noun `:mod`.

## 8. Purpose clause details (about 4 units)

**What went wrong.** The gold reified a 为了 clause with `have-reason-91` (not `have-purpose-91`). It gave that node no `:aspect` and no modal triple, and it re-entered the main subject as `:ARG0` of the purpose verb.

**Change.**
- Write no `:aspect` on the reified reason or purpose node, and no modal triple for it.
- When the main clause's agent is clearly the agent of the purpose verb, re-enter it there. This revises "do not re-enter into 为/为了 clauses".
- Check gold practice on which concept to use; this case shows `have-reason-91`.

## 9. Smaller structural cases (about 10 units)

- **Named event.** A named event with its year (a year + election type) is `event :name` with all words as `:op`s. It is not a 时 node plus a `date-entity`.
- **Example sentences.** A sentence opening with 如 (*for example*) that illustrates the previous sentence is rooted in `have-example-91 :ARG1 implicit-predicate :ARG2 main-event`.
- **Edge choices.**
  - The content of a publication is `:part-of` it, not `:possessor`. Extend the "Parts and media" rule to content and articles.
  - An event noun modifying a noun with 的 is `:mod`, not `:topic`.
  - A domain noun before 政策 is `:topic`.
  - A named building or institution containing a group is `:place` of that group; use `building` for a legislature's seat.

## 10. Modal triples on entities

**What went wrong.** The annotator added `(author :full-affirmative <entity or pronoun>)` even when the entity was only a pseudo-conceiver of title content.

**Change.** Add a conceiver entity triple only when that entity really parents reported content (not a named title).

**Caveat.** In sentence 16 the gold put the publication as conceiver of its own reporting acts and the author as conceiver of the content. That contradicts section 5.2, so do not rewrite the rule from this one case.

## Keep these

- Person and number attributes on pronouns (100%).
- Coreference linking a pronoun to the publication entity.
- Re-entering a shared agent across coordinated verbs.
- `but-91` for 虽然…但.
- `:quant` and `:unit` for classifiers, including 1.
- The past-time anchoring of matrix events.
- `(reporting-verb :before content)` for an earlier reported event.
- The granularity rules and document format (both 100%).