The annotation is strong overall: event senses 100, name tokens 100, coreference chains 100, document format 100. Most of what was lost comes from one reported clause in sentence 16, from missing shared subjects, and from a few rules where the instruction disagrees with the gold. Here they are, most costly first.

## 1. Inner structure of a 报导「…」 clause (snt16): about 9 units
**Checks hit:** d_core_args ×2, e_core_labels ×1, g_reentrancy (3 extra), c_aspect ×1, i_modal ×1.

In 「外星人 支持 布什 当 总统」 the annotator wrote:
- `支持-01 :ARG1 布什 :ARG2 (当-02 :ARG0 布什 :quote 报导 :aspect performance)`;
- a `:quote s16b` on 支持 as well;
- `(author :full-affirmative 当)`.

The gold is:
```
(报导-01 :ARG1 (支持-01 :ARG0 (外星人) :ARG1 (当-02 :ARG0 (individual-person :name 布什) :ARG1 (总统)) :aspect state) :quote s16x …)
```
- 当 has no `:aspect` and no modal triple.
- Neither content event has `:quote`. The gold puts `:quote` on 报导 itself, pointing to itself.

**Why it happened:**
- The instruction never says to take role numbers from the CPB frame for this case. PropBank 支持-01 has only ARG0 and ARG1, so "支持 X 当 Y" must be `:ARG1 (当 :ARG0 X)`. The annotator gave it an English-style ARG1 + ARG2.
- Rule 2.2 says "each event `:quote <report>`" for a 「…」 object of a reporting verb. That is what produced the extra `:quote` edges. The gold applies `:quote` per event only to 指 content, not to 报导「…」.

**Change:**
- Add: "支持/帮助/让 X V: X is the `:ARG0` of V, and the whole V-clause is `:ARG1` of 支持. 支持-01 has no `:ARG2`. Look the frame up."
- Add: "An event embedded as a complement inside another content event (当 under 支持) gets no `:aspect` and no modal triple."
- Revise 2.2 for 报导「…」: put `:quote` on the 报导 node itself (as the gold does) and none on the content events. Keep per-event `:quote 指` for 指/宣称 content.

## 2. Shared subject left out of a controlled or purpose event: 4 units
**Checks hit:** g_reentrancy missing ×2, d_core_args.

- **有能力点出:** the annotator gave `点出-01` no `:ARG0`. Gold: `点出-01 :ARG0 s17x5 (编辑)`.
- **为了讽刺…，他们…报导:** the annotator gave `讽刺-01` no `:ARG0`. Gold: `讽刺-01 :ARG0 s19p (他们)`.

**Why:** the instruction says "Never re-use a participant … as an unexpressed agent", and its exception lists only 继续/停止/开始/想/打算.

**Change:** extend that exception to 有能力/有资格 + V (the 有-06 subject is the V's `:ARG0`) and to a 为了/为 purpose clause whose subject is the main clause's subject.

## 3. Sentence-initial 为了 X，Y (snt19): about 5 units
**Checks hit:** a_event_found, d_peripheral, c_aspect, a_entity_found ×2.

- The annotator wrote `报导 :purpose (讽刺 :aspect activity)`.
- Gold: `(have-reason-91 :ARG1 (报导-01 … :mod (也)) :ARG2 (讽刺-01 :ARG0 他们 :aspect performance))`, with no `:aspect` or modal triple on have-reason-91. The 也 node was also missed.

**Why:**
- Rule 2.5 maps 为了 → `:purpose` and reserves have-*-91 roots for paired connectives.
- Rule 4.1 forces purpose events to `activity`.

**Change:**
- Add: "A clause-initial 为了 X，Y with a completed main event → `(have-reason-91 :ARG1 Y :ARG2 X)`."
- Add: "A purpose that the completed main event achieves (satirizing by reporting) is `performance`."
- Restate: 也 → `:mod (也)` whenever it is the clause's only adverb, even when a 为了 clause comes before it.
- (The gold's `:quant`/`:unit` on 也 looks like noise; don't copy it.)

## 4. Repeated generic noun reused by re-entrancy (snt16): 3 units
The annotator wrote `背书-00 :ARG0 s16x`, reusing the first 外星人. Gold makes a new node: `(背书-00 :ARG0 (s16x16 / 外星人))`.

**Why:** rule 3 says "refer to it at later exact repeats in the same sentence by its bare variable."

**Change:** limit that rule to named or specific referents. A bare kind noun (外星人, 人) that is repeated in a different clause gets its own node.

## 5. Abstract-predicate defaults applied to have-example-91 (snt18): 2 units
The annotator gave `have-example-91` `:aspect state` and `(author :full-affirmative s18h)`. Gold has neither.

**Change:** "have-example-91 (如 + example) gets no `:aspect`, no temporal parent and no modal triple; its `:ARG2` event is anchored as the main event."

## 6. Aspect and temporal links of noun-modifying events: 3 units
- **复制人 (generic kind):** the annotator had `复制-01 :aspect performance` plus `(争论 :overlap 复制)`. Gold: `:aspect process` and no temporal parent.
- **合成照片:** the annotator had `(注销 :before 合成)`. Gold: `(注销 :overlap 合成)`. The "resultative participle comes before" rule was over-extended from 遗留下来.

**Change:**
- Add: "V+N naming a kind (复制人) → V `:aspect process`, no temporal parent."
- Add: "A V+N for a specific object (合成照片) → `performance` and `:overlap` its governing event. Use `:before` only for an explicit 下来/出来 resultative."

## 7. Smaller items: 1 unit each
- **墙上:** the annotator wrote `墙`. Gold keeps `墙上` as written. Add: a locative noun that is the place argument of a verb (贴到 墙上) keeps 上 in the concept. Only frames like 历史上/在…上 get split into `(上 :op1 …)`.
- **可笑's temporal parent (snt17):** the annotator used `荒谬 :overlap 可笑`. Gold: `点出 :overlap 可笑`. The "each `:opN` hangs from `:opN-1`" rule should apply to coordinated clauses only. Adjective conjuncts inside an argument hang from the governing event.

## What to keep
These rules produced exactly the gold and should stay as written:
- **Headline titles:** `publication` with 「」 tokens, `:quant 1 :unit (篇)`.
- **新闻 + title:** `新闻 :ARG1-of (identity-91 :ARG2 publication :aspect state)`, with an author modal triple and no temporal parent.
- **有能力 V:** `有-06` + `能力 :ARG1-of identity-91`, the V `habitual` and `neutral-affirmative`.
- **指 reports:** 指-02 with `:quote` on its content, `(指 :before 当选)`, and the speaker 刊 as conceiver of 报导, 注销 and 指.
- **Adjectives and V+者 forms:** 荒唐-01, 显著-01 and 好事-00 for 好事者.
- **Coordinated adjectives:** `and` of 荒谬-01 and 可笑-01, sharing 新闻.
- **Pronoun nodes** and the coreference chain of 周报/它/他们/该刊.
- **Institution names:** `building` for 美国参议院 plus the `:place-of` structure.
- **Named-event dates:** `event :name` for 2000年总统大选.