# Review of the annotation of the tabloid passage: what to change in the instruction

The costliest errors come from three things the instruction does not cover:
- **Quoted headlines** were parsed as clauses instead of being treated as titled works.
- **Chinese adjectives** were not treated as PropBank stative verbs.
- **Some connective and postposition rules** in the instruction disagree with gold.

The patterns are listed from most to least costly.

---

### 1. A quoted headline counted as an article was parsed as a clause (largest cost)
**Pattern.** A headline in 「 」 was the object of a publishing or reporting verb and was counted by a classifier (一篇). The annotator analysed the words inside the quotes as events. It created `implicit-argument` plus `:topic` event, inner verbs, inner country and person names, `:quote` edges, and modal and temporal triples for them. It also built coreference chains through the headline's inner nouns. The same happened with a headline placed in apposition after an article noun (新闻 「…」).

Gold treats each such headline as a **`publication` named entity**:
- one `:op` per token, with the opening and closing quotation marks and the internal punctuation each as its own `:op`;
- the classifier's `:quant 1 :unit 篇` goes on that publication node;
- when the headline follows an article noun, the noun takes `:ARG1-of (identity-91 :ARG2 publication)` with `:aspect state`, and that `identity-91` gets the author modal triple.

**Cost.** f_name_tokens (3 names missing). a_entity_concept (3 wrong). About 6 extra entity nodes. Several extra or wrong core-argument, `:topic` and `:purpose` units. Extra re-entrancies (`:quote`, re-entered agent). About 8 extra modal triples, about 4 extra temporal triples, and the whole extra coreference chain (j_coref precision 56).

**Why.** Section 2.2 gives the title-bracket rule only for 《 》. The quote rule in section 3 tells the annotator to parse any reported content as events. Nothing separates a headline used as a countable object from a reported clause.

**Change.** Add to 2.2:
> A headline or title in quotation marks (「 」, “ ”) that is counted by a classifier (一篇, 一则) or set in apposition to an article noun (新闻, 文章, 报导) names a work. Write it as `publication` + `:name`, with one `:op` per token, including the quotation marks and inner punctuation. Do not analyse its words: no events, no inner names, no `:quote`, no triples, no coreference into it. Put the classifier's `:quant`/`:unit` on the publication node. An article noun before it takes `:ARG1-of (identity-91 :ARG2 publication)` (state, author full-affirmative).
>
> Only a quoted clause directly after a verb of saying, with no classifier, is reported content (section 3).

### 2. Chinese adjectives were left as plain modifiers or put under `have-mod-91`
**Pattern.** Chinese property words (ridiculous, absurd, laughable, true, prominent) were handled in two wrong ways:
- in predicate position: `have-mod-91` with the adjective as a bare `:ARG2`;
- as attributive modifiers: `:mod` with no sense.

Gold makes each one an event with its PropBank sense (`-01`). Its only role is `:ARG0`, the thing described. It has `:aspect state`, an `:overlap` temporal parent, and `(author :full-affirmative)`. An attributive one is written `noun :ARG0-of (adj-01 :aspect state)`. A property of a noun that follows 的 (the absurdity of X) is `adj-01 :ARG0 X`, not `:possessor`.

**Cost.** b_event_sense (5). c_aspect (4 missing). d_core_args (3 missing `:ARG0`, plus the wrong `have-mod-91` abstract arguments). About 5 missing temporal triples and about 5 missing modal triples. Extra `:mod` and `:possessor` edges. 1 missing re-entrancy.

**Why.** Section 2.3 says "X is Adj (no frame) → have-mod-91" and lists "plain modifiers" as non-events. The annotator did not look up adjectives in PropBank, because the required lookup reads as being for verbs only. Chinese PropBank frames most adjectives as single-argument verbs (`荒唐-01`, `显著-01`, `真实-01`, `荒谬-01` and `可笑-01` all have `ARG0` = the entity described).

**Change.** Add to the required lookup:
> Look up every Chinese adjective, predicative or attributive, in PropBank. If it has a frame, it is an event `adj-01` whose `:ARG0` is the thing described (as an attribute: `noun :ARG0-of adj-01`). Give it `:aspect state`, `:overlap` with its governing event, and an author modal triple. Use `have-mod-91` only when the word has no frame.

### 3. Ability noun with a content verb, and the 有 sense
**Pattern.** For "has the ability to V", the annotator used `有-01` with `:purpose V`, and put V's modal under 有. Gold uses `有-06` (entity described / thing it has). The ability noun takes `:ARG1-of (identity-91 :ARG2 V :aspect state)`. V is `habitual`, and the modal triple is `(author :neutral-affirmative V)`.

**Change.**
> An ability, right or opportunity noun with a content verb (能力/机会/权利 + V) links the content as `noun :ARG1-of (identity-91 :ARG2 V)`, never as `:purpose`. Give V `habitual` when it states a general capacity. Its modal parent is the author with `neutral-affirmative`, not 有.

Also add 有-06 (an entity described as having a feature or capacity) to the 有 trap list.

### 4. Sense and lemma lookup was not followed (b_event_sense 61)
**Pattern.**
- `当-01` was used where the participants called for `当-02` (position holder / position).
- `指-01` was used where they called for `指-02` (point out / claim).
- The token 贴到 was cut down to 贴, even though `贴到-01` exists. Its roles are `ARG1` = the place and `ARG2` = the thing posted, so the annotator's arguments were swapped too.
- For `刊登-01`, `ARG1` is the location and `ARG2` is the thing published. The annotator swapped them as well.

**Why.** The instruction already requires looking up the whole token and comparing all senses, but the annotator applied it to only a few verbs.

**Change.** Keep the rule and make it stricter:
> Before writing any Chinese concept, write out the token's full roleset list. The `-01` sense is chosen only if its role descriptions fit. For posting and publishing verbs, check which number holds the location and which holds the item; they are often `ARG1` = location and `ARG2` = item.

Give 当-02 and 指-02 as examples of a later sense being the correct one.

### 5. Postposition time nodes, named events and 如 "for example"
**Pattern.**
- **Named event with 时.** For a year plus a famous event plus 时, the annotator built a `时` node with an event and a separate date. Gold writes one `event` named entity: `:name` holds the year, 年 and the event noun as `:op`s, it attaches as `:temporal` on the clause's verb, and it gets no date triple.
- **Clause with 时.** For a clause plus 时, gold attaches the clause's event directly as `:temporal` and makes no 时 node.
- **Sentence-initial 如.** The annotator ignored a sentence-initial 如 (for example). Gold reifies it as `(have-example-91 :ARG1 (implicit-predicate) :ARG2 main-event)`, with no aspect and no triples.

**Cost.** Wrong and extra concepts, a missing name, wrong `:temporal` attachments, and 3 or 4 temporal units.

**Change.**
- Limit the 时/中 postposition-node rule in 2.1 to bare time or period nouns. When the item before 时 is a verb or clause, the event itself is the `:temporal`.
- A specific named occasion (a year + election, a games) is `event` + `:name`, with all its tokens as `:op`s.
- Add the 如 / 例如 opening-a-sentence rule as described above.

### 6. Temporal structure of reported and coordinated clauses (h_temporal 47)
**Pattern.**
- **Anchor on a time in the content.** The annotator anchored the reporting verb to a date inside the reported material. Gold links it `(document-creation-time :before reporting verb)`.
- **Earlier event in a claim.** A claim that refers to an earlier event (with its own earlier year) should be `(claim-verb :before content)`. The annotator instead made the content `:overlap` its date.
- **Order of a means or reason clause.** A means or reason sub-event of that content is `:overlap` with it, not `:before`.
- **Coordinated conjuncts.** Gold chains each conjunct to the previous one, not every conjunct to the first.
- **Defunct subject.** In the concessive sentence, the subject no longer exists, so gold dates its state `:before` the document creation time. The annotator used `:overlap`. The instruction already has this rule; it was not followed.

**Change.**
- Anchor rule (1) applies only to a time expression of the main clause itself. A date inside reported content does not anchor the reporting verb.
- An event in reported content that happened earlier than the report is `:before` the reporting verb.
- Make the "something that no longer exists → past" rule explicit for properties of that entity (its content, its staff).

### 7. Purpose connective 为了 + clause
**Pattern.** The annotator followed the instruction: `have-purpose-91` with `:aspect state`, an author triple, no re-entered subject, and `讽刺` as `process`. Gold uses `have-reason-91`, gives it no aspect and no modal triple, and re-enters the subject as `:ARG0` of the purpose verb. The purpose verb is `performance`, since it was realised together with the main event.

**Change.**
- The reified clause-linking node gets no `:aspect` and no modal triple.
- A purpose clause with no subject of its own re-enters the main subject; this overrides the "do not re-enter into 为了" line.
- A purpose that was carried out takes the main event's aspect.
- Gold may prefer `have-reason-91` here. This rests on one sentence, so state it with care.

### 8. Modal parents in reported content
**Pattern.** Gold is not fully consistent here.
- In the coordinated reporting sentence, gold puts the **reporting verbs** under the publication as conceiver: `(author → publication)` and `(publication → each reporting verb)`. The content events go under the author.
- In later sentences, gold gives the pronoun or publication no modal triple at all.
- The annotator added `(author :full-affirmative entity)` plus content-under-entity in every sentence, and an `:unspecified` triple from a support verb to its complement. Gold gives that complement no modal parent.

**Change (low priority).** Do not add the speaker-as-conceiver structure when the "content" is a titled work (pattern 1). Do not treat ordinary transitive verbs (support, endorse) as complement-taking modal predicates.

### 9. Coreference target and generic nouns
**Pattern.**
- The annotator linked a later full-noun mention to the immediately preceding pronoun. Gold links pronouns and later mentions to the **nearest earlier full-noun mention** of the entity.
- The annotator chained a generic kind noun ("aliens") across sentences. Gold leaves it unlinked.

**Change.** In 5.3:
> Link each new mention to the closest earlier mention that is a noun or name, not a pronoun. Generic kind nouns (bare nouns naming a class, especially inside quoted or fictional content) get no coreference.

### 10. Smaller items
- **Single-token compounds.** Keep a single segmented token as one concept (墙上, 记者团). The modifier-split and postposition rules apply only to separate tokens.
- **Named legislative bodies.** A legislative chamber named as a location is `building`.
- **Event modifying a noun with 的.** An event noun modifying a content noun with 的 (a photo of a handshake) is `:mod`, not `:topic`.
- **Owning country.** A country that owns an institutional thing (its policy) is `:possessor`. Keep `:place` for location. The instruction's "X 的 N → :place" rule is too broad.
- **Domain noun.** A domain noun on a policy-type noun (foreign policy) is `:topic`.
- **Agent noun with a disposition verb.** In a V者 agent noun with a disposition verb (好事者), the verb is `state`, not `habitual`.
- **Complement of a support verb.** A position verb under a support verb gets no `:aspect`.
- **`:quote` placement.** Gold puts `:quote` on every event of the claimed content, including its reason sub-event. Do not put `:quote` on the content of a plain report verb whose object is a titled work.

---

### Keep these (they were scored correct)
- Event and entity detection, granularity, `:refer-*` values on pronouns, and the document format. These scored 100 or close to it.
- A pronoun for a publication becomes a pronoun node linked `:same-entity` to the publication.
- `该刊` is written `刊 :mod 该`, and 内容 / 编辑 are `:part-of` / `:possessor` of the publication.
- `but-91` for 虽然…但; V者 decomposition; `全 :mod`; classifier `:quant`/`:unit`; and the `复制人` split.
- Most aspects of completed past acts (`performance`), and `(document-creation-time :before main event)` anchoring for narrative sentences.