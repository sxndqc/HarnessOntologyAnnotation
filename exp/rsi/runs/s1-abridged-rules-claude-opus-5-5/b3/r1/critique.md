The costliest problems are three Chinese constructions the instruction does not cover, or covers wrongly: a two-sided concession, a purpose stated with a noun (以 X 为 目的), and a list after "topics include". Each one breaks the graph's skeleton, and the temporal and modal errors follow from that. Next come reported speech and some missing argument re-entries, then a set of smaller rules about senses, names, coreference and adverbs.

## 1. Clause skeleton: concession, purpose stated with a noun, and lists after "include" (~35 units)
**Checks hit:** event and entity found, core arguments (event and abstract), peripheral roles, temporal (6 of the errors), modal (5).

**What went wrong:**
- **虽然…不过/但是 with both connectives.** The annotator used `:concession` (rule 2.5 says 虽然 → `:concession`). Gold uses `but-91`, with the concessive clause(s) as `:ARG1` and the main clause as `:ARG2`. A parenthetical clause added to the first part becomes a second conjunct under `and`, not a role of the claim verb.
- **以 X 为 目的.** The annotator applied the `have-purpose-91` rule (meant for 为/为了 + clause) and dropped the noun 目的. Gold keeps the noun: `(identity-91 :ARG1 (目的 :purpose-of event) :ARG2 X)`. The quantifier (大部分) goes on the event as `:mod`.
- **"The topics/contents include A, B, C 等".** The annotator made 有 the root, with the list as its argument. Gold drops the copular 有: the topic noun is the argument of the reporting verb, and the list hangs under it as `:example`. 等 is the last `:opN` of the list `and`, not a `:mod`.
- **The anchor follows the skeleton.** Because the skeleton was wrong, the anchor was wrong too, and so were most of the temporal and modal triples of those two sentences.

**Changes to the instruction:**
- In 2.5: "When the concessive clause (虽然/尽管) is answered by 但/但是/不过/却 in the main clause, use `(but-91 :ARG1 concessive :ARG2 main)`. Use `:concession` only when there is no adversative word."
- "以 X 为 目的/目标/宗旨 is a copular frame. Keep the noun: `(identity-91 :ARG1 (目的 :purpose-of E) :ARG2 X :aspect state)`. `have-purpose-91` is only for 为/为了 + clause."
- "N 有 A、B…等 where N is a topic, content or category noun listing its members: no 有/`have-91` node. Use `N :example (and :op1 A … :opk 等)`."
- "等 / *etc.* closing a list is its last `:opN`."
- "A clause in parentheses that restates or exemplifies the previous one is a conjunct under `and`. It is not `:medium` and not `:ARG1-of identity-91` on a noun."

## 2. Reported speech: `:quote`, the speaker's arguments, sense choice, and modal strength (~15 units)
**Checks hit:** reentrancy (4 missing `:quote`), sense, modal, core arguments.

**What went wrong:**
- **Wrong sense.** A passive "is alleged to" verb (被指) was given the "refer to" sense. Its "point out / claim" sense was the right one; the lookup did not compare the senses.
- **No `:quote` edges.** Gold marks each reported clause with `:quote <reporting verb>`, also when the content is not in quotation marks (claims, allegations, slogans). The annotator wrote none.
- **Content treated as a complement of a modal predicate.** The annotator gave the content `:unspecified` from the reporting verb. Gold has the content `full-affirmative` from a conceiver, and the conceiver itself gets `(author :full-affirmative conceiver)`.
- **Arguments re-entered in the wrong places.** The annotator re-entered the speaker as `:ARG0` of the reported events. Yet it left out the claim verb's own `:ARG0`, the newspaper.

**Changes to the instruction:**
- Turn the `:quote` remark in §3 into a rule: "Every content clause of a verb of saying, claiming, alleging or sloganeering gets `:quote <that verb>`."
- In 5.2: "Verbs of saying or claiming are not modal predicates. Their content is `full-affirmative` from the speaker, or from the conceiver the clause names if the speaker is unexpressed. Never use `unspecified` for them."
- "A one-time claim or statement is `performance`, even by a periodical. The habitual rule is only for publishing, reporting and covering."

## 3. Shared subjects of aspectual and nominalized verbs (~8 units)
**Checks hit:** core arguments, reentrancy, aspect.

**What went wrong:**
- **继续/停止 + verb.** 继续-01 has `:ARG0` (agent) and `:ARG1` (thing that continues). Gold puts the subject as `:ARG0` of the aspectual verb and re-enters it as `:ARG0` of the inner verb. The annotator left it only on the inner verb.
- **Stopping a nominal event (停止 X 的发行).** The stopper is also the doer of the nominal event. Gold re-enters it; the annotator did not.
- **Aspect of a nominal object.** That nominal event is `process` in gold. The annotator wrote `habitual`, because of the periodical rule.

**Changes to the instruction:**
- "With an aspectual verb (停止, 继续, 开始), the subject fills the aspectual verb's agent role from its roleset. It is also re-entered as the subject of the governed verb or nominal."
- "An event nominal that is the object of an aspectual verb is `process`. This overrides the periodical-habitual rule."
- Also qualify the existing relative-clause rule ("the noun is an argument of the inner verb only"): it holds only when the roleset lacks an agent role.

## 4. A repeated mention inside the same sentence, and compound nouns (~10 units)
**Checks hit:** granularity (4), entity concept, coreference chain (3 partial plus 1 missing).

**What went wrong:**
- **Shortened repeat of a name.** A shortened repeat of a name already given in the sentence (a bare common noun after the full title) gets its own node in gold, linked by a `:coref` triple even within the sentence. The annotator re-entered the named node, as the instruction told it to.
- **Head + modifier compounds.** 母公司 should be `公司 :mod 母`.

**Changes to the instruction:**
- "A mention written out again with its own word (a shortened name, a common noun) gets its own node, plus `(earlier :same-entity later)` even within the sentence. Re-entrancy is only for unexpressed or shared arguments and pronoun-less repeats."
- "Split head + modifier compounds whose head is a free noun (X公司, X版 where X is a modifier): `head :mod X`."

## 5. Superlatives, a missing head noun, and the whole-token lookup (~10 units)
**Checks hit:** concept, core arguments, core labels.

**What went wrong:**
- **Whole token cut short.** 算是 has its own frame (`:ARG0` the thing described, `:ARG1` what it counts as). The annotator cut it to 算, against lookup step 1.
- **Missing head noun.** In "最大 + classifier" the head noun is missing. Gold writes `implicit-argument :unit <classifier>` and makes it the argument.
- **其中 as comparison set.** In a superlative, 其中 is `:ARG5`. The instruction's "partitive 其中 is `:mod`" rule misled the annotator here.
- **Modal of the inner event.** Under a hedged copular verb (可 → `neutral-affirmative` on the verb, which the annotator got right), the inner event is still `full-affirmative` from the author, not from the copular verb.

**Changes to the instruction:**
- Add an example of an aspectual or evaluative verb + 是 (算是, 就是) that has its own frame, to stop the cut.
- "Quantifier/classifier + superlative with no head noun: `(implicit-argument :unit <classifier> :ARG1-of (have-degree-91 …))`."
- "In a superlative, 其中 / 在…中 is `:ARG5`. The `:mod` rule for 其中 is only for non-comparative partitives."
- "An event inside a hedged copula's complement keeps `(author :full-affirmative e)`."

## 6. Discourse adverbs, comitative 与, and role nouns (~12 units)
**Checks hit:** extra entities, concept, sense, core arguments.

**What went wrong:**
- **Sequence adverbs.** 后来/然后/接着 linking two clauses should be `(consecutive :op1 first :op2 later)`. The annotator kept 后来 as a `:temporal` node, plus a past-reference triple, and kept 还 as `:mod`.
- **Focus particle 就.** Gold gives it no node.
- **"A 与 B 有 relation".** Both participants form an `and` that is the subject. B is not `:companion`. The sense must also be chosen by its role description; the annotator again defaulted to -01.
- **Kinship-type titles (第一夫人, wife).** These are `have-rel-role-91`, not `have-org-role-91`. The country goes as `:place` on the role noun, not as `:ARG2`.

**Changes to the instruction:**
- Add to 2.5: "A sequence adverb between two clauses gives `consecutive` (or `after`/`before`) with the clauses as `:op1`/`:op2`. The adverb itself and the additive 还 under it get no node."
- "Discourse/focus particles 就, 便 get no node."
- "A 与/和/跟 B + symmetric predicate (have a relation, meet, marry): `(and :op1 A :op2 B)` fills the subject role."
- "Spouse titles (第一夫人, wife) are `have-rel-role-91`. A modifying country is `:place` on the role noun."

## 7. Named characters and planets, and over-linking coreference (~12 units)
**Checks hit:** name tokens, other attributes (precision 40), entity concept, coreference precision (29).

**What went wrong:**
- **Named fictional characters.** Gold treats them as `individual-person`, with any descriptor word that is part of the name inside the name ("外星人 P'Lod" → `:op1 "外星人"`). The annotator used `person`, or the kind noun as the type.
- **地球.** It should be `planet :name`.
- **Over-linked coreference.** The annotator linked generic kind nouns (aliens as a topic, then as a class) across sentences.

**Changes to the instruction:**
- "Any named individual being, including fictional characters and aliens, is `individual-person`. A descriptor written as part of the name is an `:op`."
- "Celestial bodies are `planet`/`star` + `:name`."
- "Do not link generic or kind-level mentions of a class (bare nouns in a topic list, generic subjects) by `:coref`."

## 8. Smaller rules (~6 units)
- **Locatives and frequency adverbs.** "在 N 中 + appear/exist": the postposition node `(中 :op1 N)` is the verb's location argument (`:ARG1`), not `:place`. So the postposition rule in 2.1 applies to space too, not only to time nouns. 重复/反复/经常 are `:frequency`, not `:mod`.
- **Kind modifiers on a compound topic noun.** In 时间旅行 as a list item, the noun is an entity with `:mod`. It is not an event, so it gets no aspect or document-level triples.
- **A time adverb shared by coordinated clauses.** 仍 contrasting with an earlier date gets no node. Re-enter the date as `:temporal` on the second clause.

## What to keep
- Named-entity format: Chinese name tokens split, title brackets as their own `:op`s, the middle dot as its own `:op`.
- Date entities and the anchoring of a dated sentence on its date, with `:overlap`.
- Pronoun person and number (`c_refer` 100%).
- The `but-91` structure for a contrast with 不过 between clauses.
- The appositive `identity-91` for 母公司-type descriptors.
- `have-mod-91` for a claimed property.
- Event-nominal and relative-clause attachment (`:ARG0-of`).
- `neutral-affirmative` for 可.
- The document format (`k_doc_format` 100%).