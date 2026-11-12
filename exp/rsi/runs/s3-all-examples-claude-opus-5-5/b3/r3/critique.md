The annotation is already close to gold. Concepts, aspect, refer attributes, name tokens, coreference and format all scored 100. Most of the lost points are in the document-level modal annotation (F 82) and in a few rules that the instruction states wrongly or does not state. Here they are by cost, most costly first.

## 1. Modal: a `null-conceiver` triple is added everywhere, and the speaker is wrong for 被指 (i_modal, about 5 units)

**What happened.**
- Every sentence starts with `(author :full-affirmative null-conceiver)`. Gold never has this triple (1 extra unit).
- In snt15, 被指 ("is said to") has no named speaker. The annotator gave the content two parents, `null-conceiver` and `author`. Gold uses the people the claim is about, the `and` node, as conceiver.
  - Annotation: `(null-conceiver :full-affirmative s15y)` `(author :full-affirmative s15y)` and the same for 领养.
  - Gold: `(author :full-affirmative s15a)` `(s15a :full-affirmative s15x3)` `(s15a :full-affirmative s15x2)`.
  - Cost: 3 units (two "wrong parent", one "missing").

**Why.** Section 5.2 says "A conceiver that is not in the text is `null-conceiver`". It does not say that `null-conceiver` gets no triple of its own. It also does not say what to do when the content of a speech verb would get both a speaker parent and an author parent. The annotator therefore declared `null-conceiver` in every sentence and gave the content events two parents.

**Change.** Add to 5.2:
- "Never write `(author :full-affirmative null-conceiver)`. Introduce `null-conceiver` only as the parent of an event, and only when no node of the text can serve as conceiver."
- "Passive report verbs with no agent (被指, 被称, 据说): the conceiver of the content is the subject phrase of the reported clause (for X 与 Y 有关系, the `and` of X and Y). Write `(author :full-affirmative and-node)` and `(and-node :full-affirmative each content event)`. The content events get no separate `author` triple."

## 2. have-degree-91 for 最大宗 headed by `implicit-argument` (e_core_labels and d_core_args_abstract 2 units each, plus 1 temporal and 1 modal unit)

**What happened.**
- Annotation: `(s14h / have-degree-91 :ARG2 (s14d / 大-01 :aspect state) :ARG3 (s14z / 最) :ARG5 其中)`, plus the triples `(s14x :overlap s14d)` and `(author :full-affirmative s14d)`.
- Gold: `(s14h / have-degree-91 :ARG1 (s14x3 / 大) :ARG2 (s14x4 / 最) :ARG5 (s14x5 / 其中))`. Here 大 is a bare concept with no sense, no aspect, and no temporal or modal triple.

**Why.** Section 4.2 and the 最富创意 example tell the annotator to put the property under `:ARG2` with a sense and an aspect. The annotator followed that faithfully. The rule is right when the head is a real noun (报纸) and the property is a verb phrase (富创意). It is wrong for the 其中最X宗 pattern, where the head is `implicit-argument`.

**Change.** Extend the 其中最大宗 bullet in section 3 with: "Here the bare adjective is `:ARG1 (大)` with no sense or aspect, the degree word is `:ARG2 (最)`, and 其中 is `:ARG5`. 大 gets no temporal or modal triple." Also add the full fragment to the Examples.

## 3. 仍 / 都 nodes and the date shared across a 不过 contrast (snt11–12: about 4 units)

**What happened.**
- 仍 got its own node, `:mod (s11r / 仍)` on 继续. 继续 already says "still", so gold has no 仍 node. This cost 1 unit in a_entity_found and 1 in d_peripheral_event.
- In 都以博君一笑为目的, the annotator added `:mod (s12d2 / 都)` to identity-91. Gold has no node for this 都, although it keeps the 都 of 都是真实 (1 unit).
- 继续 lacks `:temporal s11d`. In gold, the date 2007年7月 at the start of the sentence scopes both clauses of the `but-91` (1 g_reentrancy unit).

**Why.** Section 3 says "已经, 都, 也, 仍, 还 → a `:mod` node … Never drop them." That is an over-broad rule. The instruction also has no rule about a sentence-initial date covering coordinated or contrasted clauses.

**Change.**
- Narrow the adverb rule: "仍/还 before 继续, 保持 or 依然 is redundant: no node. 都 gets a node only in X都是Adj; in 都以…为目的 it gets none."
- Add: "A date at the head of a sentence whose root is `but-91` or `and` is `:temporal` of each clause's event, re-used by its variable."

## 4. 一些 is `:quant`, not `:mod` (e_peripheral_labels 1 unit, d_peripheral_entity 1 partial)

**What happened.**
- Annotation: `(s13w / 人物 :mod (s13y / 一些) …)`.
- Gold: `(s13x13 / 人物 :quant (s13x15 / 一些) …)`.

**Change.** Add to 2.2: "Vague quantifiers (一些, 一点, 许多, 几) are `:quant (一些)`, not `:mod`."

## 5. A speaker triple is missing on the content events of the 不过 clause (snt12, 1 partial)

**What happened.** The 报导 of 大部分的报导都以博君一笑为目的 (s12x8) needs `(s12n :full-affirmative s12x8)` in addition to its author triple. The rule is already in 5.2 ("the events of a following clause that goes on about what was claimed"), but the annotator applied it only inside the 宣称 clause.

**Change.** Make it concrete in the 虽然…不过 example: "the 报导 under 目的 also gets `(newspaper :full-affirmative 报导)`."

## 6. Small items not worth an instruction change

- **领养 sense (1 unit).** Gold has `领养-00`, but PropBank does have `领养-01`, so the annotator's `领养-01` is right by the instruction. Keep the "look up PropBank" rule.
- **出现 / 航天员 temporal (2 units).** Gold gives the habitual relative clause 出现 no temporal parent, and gives the entity 航天员 one. That looks like a gold error, so do not change the rule.
- **Granularity (about 6 units).** These come from how the named-entity type nodes (company 美国媒体公司, newspaper 《世界新闻周报》, P'Lod) were aligned against gold's narrower spans. The annotation is not the problem here. At most, add: "for an appositive pair (母公司 + name), align the common noun to its own word and the type node only to the name words."

## What to keep

These rules worked and should stay as written:
- The reified 虽然…不过 → `but-91` skeleton, with `:quote` on each content conjunct, never on the `and`.
- The 以X为目的 → `identity-91` rule.
- `量`, `版面`, `have-rel-role-91` for 前第一夫人, and `individual-person` for names listed as examples (蝙蝠男孩, 外星人P'Lod).
- `外星人 :name` for P'Lod in snt15, and the title-mark name tokens.
- The `consecutive` rule for 后来…还, with `(有 :after 领养)`.
- The aspect rules: habitual for reporting, process for 发行 under 停止, state for 生存.
- The anchoring rules: past anchoring of the main event, and the date as parent with `:overlap`.
- The coreference rules: a repeated 周报 gets its own node linked by `:same-entity`, and 他们 is a `person` linked to the paper.