# Review of the instruction: UMR of a whole Chinese document (five sentences)

Costs are counts of the judge's unit verdicts listed above, grouped by error pattern, most costly first. A few gold choices look like noise; the last section names them so the instruction does not chase them.

## 1. Clause structure of copular, purpose and parenthetical constructions (about 20 units: core args event/abstract, peripheral, concepts, temporal, modal)

**What happened**
- **"X 以 Y 为目的" ("X takes Y as its purpose").** The annotator used `have-purpose-91`. Gold uses `identity-91 :ARG1 (目的 :purpose-of <event X>) :ARG2 Y`: the purpose noun is a node, and Y is a plain concept with no aspect or links.
- **A parenthetical restatement ("(their slogan: '…')").** The annotator attached it to the reporting verb as `:medium`. Gold makes it its own clause, `identity-91 :ARG1 <slogan noun> :ARG2 <content event>`, and joins it to the preceding clause with `and`.
- **"X 是 Adj 的" / "X 都是 Adj" ("X is Adj", "X are all Adj") in a claim.** The annotator turned the property word into an event (`Adj-01`). Gold uses `have-mod-91 :ARG1 X :ARG2 Adj`, with the adverb as `:mod` on `have-mod-91`.

**Why it happens.** Section 2.5 tells the annotator to use `have-purpose-91` whenever there is a "marked purpose", so 以…为目的 got caught by it. Nothing in the instruction covers parentheticals. Table 2.3 lists `have-mod-91`, but nothing says the 是…的 frame with a property word belongs to it.

**What to change**
- Limit `have-purpose-91` to purpose clauses (为了, 以便). When the purpose is stated as a noun (以 Y 为目的/目标, "its aim is Y"), use `identity-91`, with the purpose noun carrying `:purpose-of <event>` and Y as `:ARG2`.
- Add: a parenthetical or colon restatement of a sentence element is a separate `identity-91` clause, coordinated with `and`. It is not a `:medium` or `:mod` of the verb.
- Add: in "X 是 Adj (的)" the property word is the `:ARG2` of `have-mod-91`, not a verb sense.

## 2. List-introducing and relational 有 ("has"; about 12 units)

**What happened**
- **"The topics they often report include A, B, C 等".** The annotator built `有-07(topics, list)`. Gold drops 有: the reporting event is the predicate, and the list is `:example` on the topic noun.
- **"A 与 B 有 关系" ("A has a relationship with B").** The annotator wrote `有-01` with B as `:companion`. Gold uses `有-03` with `:ARG0 (and A B)`.
- **等 ("etc.").** The annotator put it as `:mod` on the `and` node. Gold makes it the last `:opN` of the list (twice in this document).

**What to change**
- "N 有 A、B…等" listing examples of a category noun → `:example (and …)` on N. The noun's own clause supplies the predicate.
- "A 与/和 B 有 <relation noun>" → `有-03 :ARG0 (and A B) :ARG1 <noun>`. The 与-partner is a co-argument, never `:companion`.
- 等 / *etc.* closing a list is the final `:opN` of the `and`.

## 3. Shared subjects of aspectual and control verbs, and re-entrant times (about 8 units: reentrancy, core args)

**What happened**
- **Missing control re-entrancies.** Gold gives 继续 ("continue") `:ARG0 <subject>`, and its complement re-enters the same subject. Gold also gives the event nominal under 停止 ("stop") the stopper as `:ARG0`. The annotator left all of these out.
- **Missing re-entrant date.** Gold repeats the clause date as `:temporal` on the second conjunct of `but-91`. The annotator gave the date to the first clause only.

**Why it happens.** The rule "never borrow a participant" in 3.1 is worded so absolutely that the annotator applied it to control verbs as well.

**What to change.** Add an exception to the no-borrowing rule:
- With an aspectual or control verb (继续, 停止, 开始; *continue, stop*), the subject is that verb's `:ARG0` and also re-enters as `:ARG0` of its event complement, including an event nominal that is the complement.
- A time expression that scopes over both clauses of a `but-91` / contrast is attached to both clause events (re-entrancy).

## 4. Aspect (7 units)

**What happened**
- **Event nominal under 停止.** Gold has `process`. The annotator gave `habitual`, as the instruction's step 1 demands.
- **"Survive / exist" verbs.** Gold has `state`; the annotator gave `activity`.
- **Past claim verb (宣称, "claim").** Gold has `performance`; the annotator gave `activity`.
- **Verbal noun used as a predicate's argument (活动, "activity").** Gold has `activity`; the annotator gave `process`.

**What to change**
- In step 1, exclude event nominals that are the complement of an aspectual verb: these are `process`.
- Add existence and survival verbs (生存, 存在, *survive, exist*) to the `state` list.
- A completed past speech act (claim, announce, say) is `performance`.

## 5. Compounds and repeated bare mentions inside a sentence (about 8 units: concept, granularity, coref)

**What happened**
- **Compound noun.** Gold splits a modifier-plus-head compound (a kinship or rank prefix + head noun) into `head :mod prefix`. The annotator kept it as one word.
- **Bare repetition of a name in the same sentence.** Gold gives it its own node (the bare noun) and a `:same-entity` triple. The annotator used a re-entrancy and missed the coref chain (3 coref units).

**What to change**
- Split a compound whose first morpheme is a separable modifier, such as 母-/父-/子- + organisation noun.
- A later short-form mention of a named entity in the same sentence (a bare head noun repeating part of the name) gets its own node with the bare word as concept, plus a `:coref :same-entity` triple. This is an exception to the "within a sentence, use a re-entrancy" rule in 5.3, which applies to pronouns and zero arguments.

## 6. Named entities of fictional or non-human characters, and planets (about 8 units)

**What happened**
- **Named fictional characters.** Gold types them `individual-person`. When a common noun is part of how the character is named (a species word before a proper name), gold puts it in the name as the first `:op`.
- **Planet names.** Gold makes a planet name a named entity of type `planet`. The annotator used the bare noun.

**What to change**
- Named characters, human or not, are `individual-person`.
- Earth, Mars and similar names are `planet` named entities.

## 7. Titles of spouses, sentence adverbs and sequence (about 10 units)

**What happened**
- **First-lady type title.** Gold uses `have-rel-role-91 :ARG3 <title>`, with the country as `:place` on the title noun and "former" as `:mod` on the title. The annotator used `have-org-role-91`.
- **后来 ("later") with 还 ("also").** Gold reifies the sequence as `consecutive :op1 … :op2 …` and makes no separate nodes for the time word.
- **就.** The emphatic or discourse 就 got no node in gold.

**What to change**
- A role defined by marriage or relation (first lady, wife of the president) → `have-rel-role-91`, with the country as `:place` of the role noun and "former" as `:mod` of the role noun.
- Two coordinated predicates linked by 后来 / *then / later* → `consecutive`, with no node for 后来.
- Discourse 就 / 便 in a non-conditional sentence gets no node. Keep the rule that meaningful adverbs (也, 都, 仍) get nodes.

## 8. Modal layer of reported content (about 9 units)

**What happened**
- **Nodes that should not be in the modal layer.** Gold gives no modal parent to plain concepts inside identity clauses (the purpose content, a locative 中 ("in"), a non-event nominal). The annotator gave them modal parents.
- **Who conceives the claim's content.** For the content of a claim, gold makes the claimer the conceiver of every embedded event, including those in the quoted slogan and the later clause about the reports. The annotator put most of these under `author`.
- **Missing `:quote`.** Gold adds `:quote <reporting event>` on the content of reported speech. The annotator never did (4 reentrancy units).

**What to change**
- Under a saying verb, every event of the reported content, including events in an appended slogan or quotation, has the speaker as modal parent. The content's top node also carries `:quote <saying verb>`, and this is to be applied consistently.
- No modal or temporal links for nodes without `:aspect`.

## 9. Temporal over-linking (about 10 units)

**What happened**
- **Links to nodes without aspect.** The annotator linked plain concepts (purpose content, list items such as a travel noun, a locative node).
- **Extra `:after` relation.** It added a link to a habitual relative-clause event (relative clause → creation verb) that gold leaves out.
- **Wrong parents.** It hung reported events on the wrong anchor: gold chains them on the first habitual reporting event, not on the claim verb or on a property word.

**What to change**
- Repeat in 5.1: no temporal parent for any node without `:aspect`.
- Leave out the links between habitual relative-clause events and past performances.
- Under a claim, the embedded habitual event is the local anchor for the other habitual events of the sentence.

## What the annotator got right, which the instruction should keep
- Named entities of works with 《》 kept as name tokens, and no `:wiki` in Chinese.
- Pronoun person and number (`c_refer` was 100%).
- The format of the document level (100%).
- Date `:overlap` anchoring, and the chaining of an aspectual verb to its complement.
- The coref chain from a named periodical to a later pronoun.
- `but-91` with `:ARG1`/`:ARG2` and the modal strength of 可 ("can") as `neutral-affirmative`.
- Superlative modifiers placed on the right noun, and `:frequency` for 经常 ("often").

## Gold choices not to chase
These look like gold noise, so the instruction should not be bent to match them:
- **出现 roles.** Gold reverses the PropBank roles (PropBank says `:ARG0` = location, `:ARG1` = theme). The annotator followed PropBank.
- **领养 sense.** Gold uses `领养-00` although PropBank has `领养-01`.
- **`have-degree-91` roles.** In the headless superlative 其中最大宗 ("the largest of which"), gold numbers the roles differently from the instruction's convention. The only point worth adding: a headless superlative takes an `implicit-argument` head with the classifier as `:unit`, and the partitive 其中 is that superlative's `:ARG5`.