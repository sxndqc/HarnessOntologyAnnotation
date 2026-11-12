# Review of the UMR annotation of the 《世界新闻周报》 document (5 sentences), with changes for the instruction

Problems are ordered by cost, most costly first. I did not use the tools for this review. Each judgement below rests on the gold annotation and the judge's unit list.

## 1. Aspect of publishing and "already stopped" events (c_aspect F 60; 6 wrong units)
**What went wrong:**
- **发行 is a habitual event.** 发行 in snt1 was annotated `endeavor` and in snt4 `activity`; gold has `habitual` both times. Publishing a newspaper is a repeated event.
- 综合 (snt2, "the weekly brings together all kinds of stories") was annotated `performance`, apparently triggered by 了. Gold has `habitual`, because it describes what the paper regularly does.
- **已经停止 is a resulting state.** 已经停止 (snt1) was annotated `performance`; gold has `state`. As a relative-clause modifier, "already stopped" describes the paper's current condition.
- 未经 (snt2) was annotated `performance`; gold has `process`.
- 被称为 (snt5) was annotated `state`; gold has `performance`. It is a completed act of naming.

**Why it happens:** the aspect table maps 了/past to `performance` and present-tense processes to `activity`. It never says that a characteristic, repeated activity of an institution is `habitual` even without 经常 or 每天.

**Change:**
- Add to 4.1: "Typical or repeated activities of a person or institution (publishing, broadcasting, selling, collecting content) are `habitual` even without a frequency word, and even with 了 when the clause describes what the entity does in general."
- Add: "已经 + change-of-state verb used as a modifier (已经停止发行的小报) is `state`."
- Add: "A passive naming or evaluation (被称为, 被誉为) is `performance`."

## 2. Temporal over-annotation and wrong anchors (h_temporal F 47; about 11 units)
**What went wrong:**
- **States and descriptions were each attached to the document creation time.** Gold gives no temporal parent to the copular `identity-91` (snt1), to the time word 目前 (snt4) or to a modifier-like state (荒诞不经, snt5). The annotator added `(document-creation-time :overlap s1i)`, `(present-reference :depends-on s4x2)` and `(s5x :overlap s5x10)`.
- **Same-sentence events were not chained to the clause's main event.** In snt1 gold anchors the other events on 发行:
  - `(document-creation-time :before s1x3)`
  - `(s1x3 :overlap s1x4)` (发行 → 停止)
  - `(s1x7 :contained s1x3)` (闻名 inside the publishing period)
  - `(s1x3 :overlap s1x8)`

  The annotator instead did `(s1x3 :after s1x4)` (停止 after 发行) and `document-creation-time :overlap 闻名`.
- In snt4 gold uses `(document-creation-time :depends-on s4x)` and then `(s4x :overlap s4x2)`. The annotator used 目前 as the parent of both clauses.

**Change to 5.1:**
- "Do not give a temporal parent to a copular/identity predicate or to a property used as a modifier."
- "Within a sentence, anchor the dependent events (relative clauses, the 以…而 result, the second conjunct) to the sentence's main anchoring event rather than each to the document creation time."
- "A vague time word like 目前 is a `:temporal` modifier of the event and needs no `present-reference` triple."

## 3. Non-core role choice and attachment (d_peripheral_event F 33, d_peripheral_entity F 48, e_peripheral_labels; about 20 units)
**What went wrong:**
- **Country modifiers.** 美国小报 and 美国历史 were given `:mod country`; gold uses `:place (s1c / country …)`.
- 电视节目 was given `:mod`; gold uses `:medium (s3x5 / 电视)`.
- 《世界新闻周报》的纸本 was given `:possessor`; gold uses `:part-of`.
- **以…而闻名.** The annotator built a separate `and :op2 闻名 :manner 报导`. Gold makes it a relative modifier of the tabloid, with 报导 as the reason: `:ARG1-of (s1x7 / 闻名-01 :reason (s1x8 / 报导-01 :ARG0 s1x …))`.
- **由于 → :reason.** 由于 was annotated `:cause`; gold uses `:reason (s5x10 / 内容 …)`.
- **Adverbs.** 已经 (snt1 and snt4) got no node at all; gold keeps it as `:mod` on the event.
- 都 was put on the noun 内容; gold puts `:mod (s2x16 / 都)` on 经-01.
- 目前 was put on `but-91`; gold puts it on 停刊-01.

**Change:**
- In 2.5, change "because (因为, 由于) → :cause" to `:reason`. Add "以 X 而 Y (known for X) → Y `:reason` X".
- In section 3, add short rules:
  - A country or region modifying a noun → `:place`.
  - The channel or medium (电视, 网络) → `:medium`.
  - A version or part of a publication → `:part-of`.
  - Adverbs 已经, 都, 仍, 也 → `:mod` nodes on the event they modify, never dropped and never moved onto a noun or onto the discourse connective.
- Add: "A 以…而闻名 / 而 clause modifying the subject of a copular sentence attaches inside the predicate noun, not as a new conjunct."

## 4. Classifiers with 一 (a_entity_found, c_other_attributes; about 6 units)
**What went wrong:** 一份 and 一个 were dropped. Gold has `:quant 1 :unit (s1x5 / 份)` and `:quant 1 :unit (s3x7 / 个)`.

**Why it happens:** the instruction itself is wrong here. It says "an ordinary classifier (个, 本, 只, 位) is dropped".

**Change:** rewrite the classifier rule in 2.2: "A numeral + classifier phrase (一份, 一个, 三本) is kept: `:quant N :unit (x / <classifier>)`."

## 5. Name tokens with book-title marks (f_name_tokens F 50; 4 units in all)
**What went wrong:** 《世界新闻周报》 was annotated `:op1 "世界" :op2 "新闻" :op3 "周报"`. Gold includes the marks: `:op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》"`. This failed in snt1 and snt4 (2 name units), and it also caused 2 granularity units.

**Change:** add to 2.2: "In Chinese, the title marks 《 》 around a publication's name are name tokens: include them as the first and last `:opN`."

## 6. Superlatives and chengyu modifiers (a_event_found, d_core_args; about 5 units)
**What went wrong:**
- 最富创意 was annotated `富-01 :degree 最`, with `:ARG0` 报纸. Gold has:
  ```
  (s5x4 / 报纸 :ARG1-of (s5h / have-degree-91 :ARG2 (s5x5 / 富-01 :ARG1 (s5x6 / 创意)) :ARG3 (s5x7 / 最)))
  ```
- 荒诞不经的内容 was made an event (`荒诞不经-01`, which then got temporal and modal triples). Gold has `:mod (s5x11 / 荒诞不经)`.
- 美国历史上 lost the 上 node. Gold has `:temporal (s5x8 / 上 :op1 (s5x9 / 历史 …))`.

**Change:**
- In 4.2, replace "`:degree` for … most, 最" with: "A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91` (`:ARG1` the entity, `:ARG2` the property, `:ARG3` 最/更 or `most`/`more`). Only intensifiers (很, 非常, 太) are `:degree`."
- Add: "An adjectival chengyu before 的 is a `:mod`, not an event."

## 7. Connective roles (e_core_labels; 2 units)
**What went wrong:** 不过 was annotated `but-91 :op1/:op2`; gold uses `:ARG1`/`:ARG2`.

**Change:** in 2.5, state "`but-91` and `contrast-91` take `:ARG1` and `:ARG2`, not `:opN`".

## 8. Distributive modifiers and argument direction (g_reentrancy F 18)
**What went wrong:**
- 各式各样奇怪的新闻与专栏: the annotator put the adjectives on the `and` node. Gold puts `:mod` on each conjunct and re-uses the same nodes (re-entrancy).
- 属自己的节目: the annotator had `属-02 :ARG0 周报 :ARG1 节目`. Gold reverses it: `节目 :ARG0-of (属-02 :ARG1 s3x2)`. The annotator apparently did not follow the PropBank argument structure.
- Extra implicit arguments were added: `发行 :ARG0 newspaper` (snt4) and `查证 :ARG1 内容` (snt2). Gold leaves them out; in 查证 the ARG1 is 新闻.

**Change:**
- "A modifier shared by coordinated nouns goes on each conjunct (re-entrancy), not on the `and` node."
- "Add a re-entrant argument only when the text expresses it."
- "Check the PropBank argument order for belong-type verbs (属): the thing owned is ARG0, the owner ARG1."

## 9. Smaller issues
- **Coreference across 停止 and 停刊.** The annotator linked them with `:same-event` (2 extra units). They are different events: the whole paper stopped publishing in snt1, but only the print edition stopped in snt4. Add: "Link `:same-event` only when the participants are the same."
- **未经 and 查证.** The annotator put `:polarity -` on 经 and gave 查证 `full-negative`. Gold has no polarity node on 经 and gives 查证 `partial-affirmative`. This is low cost (2 units) and gold is not fully consistent here, so it does not justify a rule change.

## What to keep
- **Senses:** event senses scored 100%.
- **Concepts:** event and entity detection and concept choice were 94–97%, and Chinese words were used as concepts throughout.
- **Structure:** `identity-91` for 是 and the and/but structure for the second sentence and the 不过 sentence were right.
- **Modal:** author `full-affirmative` triples were right (modal F 91).
- **Coreference:** the entity chain 周报 → 周报 → newspaper → 周报 across all sentences was correct (recall 100%).
- **Format:** the document-level format was perfect.

The instruction's push to look things up in PropBank and the gold data should stay. It would also have caught items 4 and 8.