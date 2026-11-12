Six changes, each aimed at a problem from the critique that will recur on other documents:

1. **Modal, `null-conceiver`.** The annotator wrote `(author :full-affirmative null-conceiver)` in every sentence. 5.2 now forbids that triple. `null-conceiver` may only be the parent of an event, and only when no node of the text can be the conceiver.
2. **Modal, agentless report verbs (被指, 据说).** The content events had two parents. Now the subject of the reported clause is the conceiver: for X 与 Y, the `and` node. The content events get no separate author triple.
3. **其中最X宗.** The annotator put the property under `:ARG2` with a sense and an aspect. For this pattern, have-degree-91 is now `:ARG1 (大) :ARG2 (最) :ARG5 (其中)`, and 大 is a bare concept with no sense, aspect or triples.
4. **Adverb nodes and a shared date.**
   - The "never drop adverbs" rule is narrowed: 仍/还 before 继续/保持/依然 gets no node, and neither does the 都 of 都以…为目的.
   - A sentence-initial date over a `but-91`/`and` root is now `:temporal` of each clause's event.
5. **Vague quantifiers.** 一些/许多/几 are `:quant`, not `:mod`.
6. **Speaker triple.** The 虽然…不过 example now shows the speaker triple on the 报导 of the 不过 clause.

To stay under the 30000-character limit, I shortened the entity-type list. I also dropped examples whose rules are already stated explicitly: title marks, but-91, 达到 quantity, 是…的 and 历史上.

```json
{"summary": "Modal: forbid author→null-conceiver triple; agentless report verbs (被指) take the reported clause's subject (and-node) as conceiver. 其中最X宗 → have-degree-91 :ARG1 大 :ARG2 最 :ARG5 其中 with bare 大. Narrow adverb rule (no 仍 before 继续, no 都 in 都以…为目的); sentence-initial date shared by but-91/and clauses. 一些 → :quant. Speaker triple on 报导 in 不过 clause. Trimmed redundant examples and type list for space.", "edits": [
{"op": "replace", "old": "Types: `person`,\n`country`, `city`, `organization`,\n`company`, `newspaper`, `publication`,\n`event`,\n`disease`, `product`, `spaceship`, ... (as in AMR).", "new": "Types as in AMR (`company`, `newspaper`, `spaceship`, ...)."},
{"op": "delete", "old": "- Title marks (2.2): 《世界新闻周报》 → `:name (n / name :op1 \"《\" :op2 \"世界\" :op3 \"新闻\" :op4 \"周报\" :op5 \"》\")`."},
{"op": "delete", "old": "- but-91 (2.5): X，不过Y (within one sentence) → `(b / but-91 :ARG1 X :ARG2 Y)`. A sentence starting with 不过 → no but-91; root = main verb (跌-01)."},
{"op": "delete", "old": "- Quantity (3): 发行量达到120万份 → `(d / 达到-01 :ARG0 (l / 量 :quant-of (f / 发行-01 :ARG1 n) :ARG1-of (h / have-quant-91 :ARG2 1200000 :unit (u / 份))))`."},
{"op": "delete", "old": "- 是…的 (2.3): 都是真实的 → `(h / have-mod-91 :ARG2 (t / 真实) :mod (d / 都) :aspect state)`."},
{"op": "delete", "old": "- 历史上 (4.2): 美国历史上 → `:temporal (s / 上 :op1 (h / 历史 ...))`."},
{"op": "replace", "old": "A conceiver that is not in the text is `null-conceiver`.", "new": "Never write `(author … null-conceiver)`; `null-conceiver` only parents an event when no text node can. Agentless 被指/据说: the conceiver is the reported clause's subject (X与Y → its `and`): `(author :full-affirmative and)` `(and :full-affirmative E)`, no author triple on E."},
{"op": "replace", "old": "and the head is `implicit-argument :unit 宗`.", "new": "and the head is `implicit-argument :unit 宗`; there have-degree-91 is `:ARG1 (大) :ARG2 (最) :ARG5 (其中)`, 大 bare, no aspect or triples."},
{"op": "replace", "old": "Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`).", "new": "Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`). Except: no node for 仍/还 before 继续/保持/依然, nor for 都 in 都以…为目的. A sentence-initial date over a `but-91`/`and` root is `:temporal` of each clause's event (re-used)."},
{"op": "replace", "old": "- 重复/经常 → `:frequency`;", "new": "- 一些/许多/几 → `:quant (一些)`, not `:mod`. 重复/经常 → `:frequency`;"},
{"op": "replace", "old": ":ARG2 (g / 博君一笑)))`.", "new": ":ARG2 (g / 博君一笑)))`; that 报导 also gets `(newspaper :full-affirmative 报导)`."},
{"op": "append", "text": "\n- Modal/degree/date (5.2, 3): 被指与X有关系 → `(author :full-affirmative a)` `(a :full-affirmative 有)`; 其中最大宗 → `(h / have-degree-91 :ARG1 (大) :ARG2 (最) :ARG5 (其中))`; 一些人物 → `人物 :quant (一些)`; 2007年…，不过仍继续 → `继续 :temporal d`, no 仍 node."}
]}
```