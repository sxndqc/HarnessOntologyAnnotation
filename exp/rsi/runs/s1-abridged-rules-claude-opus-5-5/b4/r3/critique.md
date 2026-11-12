Below are the error patterns, most costly first. Unit counts are approximate. They come from the judge's list of units it did not count as correct.

---

### 1. Reported speech by a publication: modal parents, temporal chaining and `:quote` (about 15 units: i_modal 7, h_temporal 5, g_reentrancy 3, j_coref 2)

There are three separate problems.

**a. Modal parent of the reporting verbs versus their content.**
- **Gold:** when an expressed organization or publication reports, claims or retracts something, the gold makes that entity the conceiver of its own reporting acts (`entity :full-affirmative report-verb`). The reported content events sit directly under `author`.
- **Annotator:** it did the reverse (`author → report-verb`, `entity → content`). That is what the instruction literally says in 5.2.
- The gold pattern goes against the general guidelines and may not be consistent across documents. Before rewriting 5.2, check more gold documents (search_annotations with `:full-affirmative` + a publication speaker).
- If the pattern holds, add this rule: *"When an expressed organization or publication is the agent of a series of reporting acts, that entity is the modal parent of the reporting events; their content events are under `author`; an argument clause nested inside the content (e.g. *someone becomes X*) gets no modal triple."*

**b. Temporal chaining in coordination and inside content.** Three rules to add:
- In a multi-clause `and`, each later conjunct `:overlap`s the conjunct just before it (a chain), not the first conjunct.
- An event nominal or modifier inside a noun phrase that is under another modifier event takes that nearer event as its parent, not the clause verb.
- A means or support event introduced by 靠/凭 (*by means of X*) `:overlap`s the event it enables, not `:before`.
- Also: a date expression that appears only inside reported content gets no temporal triple at all. The instruction says the anchor must not link to such a date, but it doesn't say the date itself gets no triple.

**c. `:quote` and coreference in content.**
- `:quote` goes on every event of the reported content, including subordinate reason or means events inside it, not only the top content event.
- Two mentions of a generic kind noun (a bare plural class such as *aliens* used generically) in different clauses are separate nodes with **no** `:same-entity` link. Add this to 5.3. It also stops the core-argument mix-up that a coref link causes when nodes are matched.

### 2. Demonstrative + noun written as one token (该X, 此X, 本X) (about 9 units: a_entity_concept 4, d_peripheral 2, plus knock-on temporal and peripheral errors from bad node matching)

- **Error:** the annotator kept the token as one entity concept.
- **Gold:** splits it into the noun with the demonstrative as `:mod` (`(k / 刊 :mod (g / 该))`).
- **Cause:** 2.6 says to split "free head noun + modifier" compounds, but only gives a noun-noun example. Demonstratives are listed under "not events" and look as if they get no node at all.
- **Fix:** add *"A demonstrative + noun token (该/此/本/这 + noun) is split: noun `:mod` demonstrative. Coref links the noun node."*

### 3. Frames and role numbers not taken from the whole token (about 10 units: event concept 2, sense 2, core labels 4, core args 2)

- **Verb + complement tokens.** The annotator cut such tokens (V出, V到) down to the bare verb even though the whole token has its own frame. The instruction already says to look up the whole token, so this rule was not followed. Strengthen it: *"Check V+complement tokens (V出, V到, V上, V成) as a whole first; use the bare verb only if the whole token is not in PropBank."*
- **Publishing and posting verbs.** In these frames the place is often `:ARG1` and the thing published or posted is `:ARG2`. The annotator used the English order (thing = `:ARG1`). The current sentence ("usually make the place … a numbered argument") is too vague. Replace it with: *"For publishing/posting verbs, copy the role numbers from the frame. Typically ARG1 = location/medium and ARG2 = entity published or posted."*
- **Sense choice for common polysemous verbs.** The annotator defaulted to -01 again:
  - a "serve as / hold a position" verb should be the position-holder sense;
  - a "point out / claim" verb used for a saying should be the claim sense, not the "refer to" sense.
  
  Add: *"For a verb of saying, pick the claim/assert sense. For 'serve as [title]', pick the position-holder sense."*
- Don't chase the gold's -00 on verbs that do have a PropBank frame. It doesn't generalize.

### 4. Role noun with a possessive pronoun or owner (其编辑, *its editors*) (about 6 units: extra event and entity, core args, 4 reentrancies)

- **Error:** the annotator built `person :ARG1-of have-org-role-91 :ARG2 org :ARG3 editor`.
- **Gold:** keeps the noun itself, with the owner as `:possessor`, and re-enters that noun as the agent of later verbs.
- **Fix:** limit reification to role nouns that appear with a person's name or in an explicit title construction. Add *"A role or occupation noun with only a possessor (its/其 X, the paper's X) is the noun itself + `:possessor`, not a reified role."*

### 5. A 为了 purpose clause before the main clause (about 6 units)

- **Concept:** the gold used `have-reason-91` for 为了 + clause. Check other gold before changing the concept.
- **Aspect and modal:** the reified node had no `:aspect` and no modal triple. Change 2.5: the reified reason/purpose node gets **no `:aspect`** and **no modal triple**.
- **Purpose verb:** the purpose verb is `performance` when the main act that serves the purpose is completed (not `process`). It re-enters the shared subject as `:ARG0`. This reverses the current "do not re-enter the subject into 为/为了-purpose clauses" rule for the case where the purpose clause comes before the main clause and shares its subject.

### 6. Concessive and contrast anchoring, and stance verbs (about 4 units)

- **But-91 anchor:** when the root is `but-91`/`contrast-91`, its `:ARG1` is the anchor and `:ARG2` `:overlap`s it, as with the first conjunct of `and`.
- **Tense:** descriptions of a publication or institution that the document treats as past are `:before` the document creation time. The rule already exists (the past rule in 5.1), but it was not applied to the anchor.
- **`identity-91` aspect:** under 能力/机会 the `identity-91` gets `:aspect state`. Make this an explicit exception to "nested abstract predicates get no aspect".
- **Stance verbs:** support, oppose or favour as a stance (*X supports Y doing Z*) is `state`, not `activity`. Add these to the stative list in 4.1.

### 7. 时 after a named occasion (about 3 units)

- **Error:** the annotator built a 时 node with `:op1` the named event and gave it a date triple. It then became the anchor's parent.
- **Fix:** add to 2.1: *"After a named occasion (event + `:name`), 时 gets no node; the event is the `:temporal` of the verb directly; the verb anchors to the document creation time."*

### 8. Smaller patterns (1–3 units each)

- **Sentence-initial 如 / 例如 / *for example*:** this introduces an example of the preceding statement. Use `(h / have-example-91 :ARG1 (i / implicit-predicate) :ARG2 main-event)` as the root.
- **Event nouns that classify a noun:** an event noun classifying a noun (*a photo of a handshake*, the *X 的 photo* type) is `:mod`, not `:topic`.
- **Country with 的 on what it has or does:** X 的 N, where N is something the country owns or produces (policy, army), is `:possessor`. Restrict the `:place` rule to place names modifying a noun directly, without 的. A field noun before the head (外交政策) is `:topic`.
- **Agent nouns from a trait word:** an agent noun built from a character-trait word (好事者 type) is `state`, not `habitual`.
- **Legislature named as a location:** a named legislature used as the location of something is a `building` + `:name`. The group inside it is `:place` building. A locative noun (墙上) is linked with `:place-of` to the group, not `:possessor`.
- **Words inside a compound:** an inner verb of a decomposed V+人 compound gets a modal triple but no temporal parent.

### What to keep (these scored well)

- Publication headlines as `publication` + `:name`, with quote marks as `:op`s and `:quant`/`:unit` from the classifier.
- The appositive `identity-91` for an article noun followed by its headline.
- The `:part-of` rule linking an article to its publication.
- The 能力 + V → `identity-91` rule, with V `habitual` and author neutral-affirmative.
- The V+人 / 者 decomposition.
- `:refer-person` / `:refer-number` on pronouns, and treating a pronoun for a publication as a new node with `:same-entity` to the publication.
- `but-91` for 虽然…但.
- Named occasions as `event` + `:name`.

Abstract-predicate core arguments, the refer attributes and the other attributes all scored 100.