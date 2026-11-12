# Review of the annotation of the 5-sentence 《世界新闻周报》 document: error patterns, causes, and changes to the instruction

The annotator did most of the sentence-level work well; the losses are at the document level and in a few repeated habits. The checks that lost the most were temporal (F 35), reentrancy (precision 56), aspect (F 83), core arguments of events (F 90), coreference precision (71), and wiki and polarity (precision 0). The problems are listed below from most to least costly.

---

## 1. Temporal anchoring (h_temporal F 35: 7 of about 10 gold events wrong, missing or extra; plus one k_doc_format error)

There are four sub-patterns.

**a) Triple direction reversed, giving a node two parents (snt 1).** The annotator wrote `(document-creation-time :before s1f)` and also `(s1b :contained s1f)`. The second triple makes 报导 the *parent* of 发行, so 发行 ends up with two parents (the k_doc_format error). 报导 and 闻名 were also given the wrong roles.
- Gold: `(document-creation-time :before s1x3) (s1x3 :overlap s1x4 停止) (s1x3 :overlap s1x8 报导) (s1x7 闻名 :contained s1x3)`
- Cause: section 5.1 says "parent first, child second", but its example `(s1k :contained s1f)` has the anchoring event in the *child* slot. That contradicts the rule just before it. The annotator copied the shape and put the wrong event in it.
- Fix: state in bold that **the first element of a triple is the parent and every event has exactly one parent**. Replace the example with the full snt-1 pattern: "the main event 发行 → DCT; 停止 and 报导 → `(发行 :overlap X)`."

**b) Dependent events sent to DCT, or left without a parent.**
- snt 1: `(document-creation-time :overlap s1t)` for 停止. The rule "anchor dependents to the main event" already says this should be `(s1f :overlap s1t)`; the annotator did not follow it.
- snt 2: 查证-01 had no parent. Gold: `(s2x8 :overlap s2x13)`.
- snt 5: 富-01 inside have-degree-91 had no parent. Gold: `(s5x :overlap s5x5)`.
- Cause: the line "Give no temporal parent to … a property used as a modifier" was over-applied to *event concepts that carry `:aspect`*.
- Fix: "Every node with a PropBank sense and an `:aspect` (including 富-01 under have-degree-91 and 查证-01 inside a noun) gets a temporal parent, normally `(main-event :overlap X)`. Only plain `:mod` words with no sense, and identity-91, get none."

**c) A cross-sentence anchor used where gold uses DCT (snt 2).** The annotator wrote `(s1f :overlap s2z)`. Gold has `(document-creation-time :before s2x)`.
- Fix: "Anchor each sentence's main event to `document-creation-time` unless the text marks a relation to an earlier event (然后, 之后, 同时 …)."

**d) The rule for 目前 and similar time words is wrong for this data (snt 4, and snt 5 by analogy).** The instruction's own example `(document-creation-time :depends-on s4t)(s4t :overlap s4e)` cost three units: the parent of 停刊, the parent of 继续, and an extra parent for 目前.
- Gold gives 目前 no temporal node at all. It writes `(document-creation-time :depends-on s4x)` on the main event and `(s4x :overlap s4x2)` for the second conjunct.
- Snt 5 gold likewise has `(document-creation-time :depends-on s5x)`.
- Fix: rewrite the 目前 example and rule as: "Vague present adverbs (目前, 现在) stay `:temporal` in the graph, but at the document level the main event attaches directly: `(document-creation-time :depends-on <main event>)`. The other events of the sentence go `(main :overlap X)`. Do not give the adverb its own triple."

---

## 2. Implicit arguments and extra re-entrancies (g_reentrancy precision 56, 4 extra; d_core_args_event 3 units; d_peripheral_entity 2)

**Snt 1, 已经停止发行的小报.** The annotator wrote `小报 :ARG0-of (停止-01 :ARG1 (发行-01 :ARG1 s1x))`. Gold nests it as a chain of relative clauses:
```
(s1x / 小报 :ARG1-of (s1x3 / 发行-01
                     :ARG1-of (s1x4 / 停止-01 :mod (已经) :aspect state)
                     :aspect habitual))
```

**Snt 4.** The annotator added `发行-01 :ARG0 s4n` and `网络版 :part-of s4n`. Neither is in the text, and gold has neither: it has `(s4x6 / 发行-01 :ARG1 (s4x7 / 网络版))`. The ":part-of for a version or edition" rule was applied with no written X的.

**Snt 2, 其中.** The annotator rendered it as `and :part s2c`. Gold has `内容 :mod (其中)`. Building it as a part relation also broke the `:ARG0` of 经-01 (one missing core argument, one extra re-entrancy).

**Why:** the instruction does say "Add an implicit or re-entrant argument only when the text expresses it", but it is a one-line bullet, and the examples (以…而闻名 with `:ARG0 x`, 属自己 with `:ARG1 x`) push towards re-entrancy.

**Changes to the instruction:**
- Add the 已经停止发行的小报 structure above as an example. State: "for V1+V2的N (停止发行的), N attaches to the inner verb (`:ARG1-of 发行`) and the outer verb takes the inner verb as `:ARG1-of`."
- Add: "Use `:part-of` only when the owner is written in the phrase (X的纸本). 网络版 alone gets no owner. Do not copy a subject into a second clause unless a word (自己, 其, a pronoun) refers to it."
- Add: "其中 → `:mod (其中)` on the noun it introduces."

---

## 3. Aspect (c_aspect F 83: 3 units)

**identity-91 had no `:aspect` (snt 1).** Gold has `:aspect state`. It also gets `(author :full-affirmative s1i2)`, which the annotator also missed (an i_modal unit). The cause is that the line "no temporal parent for identity-91" was read as "not an event".
- Fix: "identity-91 and the other -91 predicates carry `:aspect state` and a modal triple. Only the temporal triple is left out."

**曾经…拥有过 annotated `performance`; gold has `state`.** The 了/过 → performance rule overrode the lexical state verb.
- Fix: "Stative verbs (拥有, 有, 是, 在, 属) stay `state` even with 过 / 曾经 / 了."

**已经停刊 as a main predicate annotated `state`; gold has `performance`.** The annotator stretched the rule "已经 + change-of-state verb as a modifier is state" to a main clause.
- Fix: add "When the 已经 + change-of-state verb is the main predicate (纸本已经停刊), use `performance`. `state` applies only to the 的-modifier."

---

## 4. `:wiki` added (f_wiki: 4 extra, precision 0)

The annotator added `:wiki "Weekly_World_News"` (twice) and `:wiki "United_States"` (twice). Gold has none. In other Chinese gold data, `:wiki` appears only in about two sentences, and in a non-standard form there.

Fix: replace "an optional `:wiki`" with "**Do not add `:wiki`** in Chinese documents."

---

## 5. Coreference over-linking (j_coref_chain precision 71: 2 units)

The annotator linked the 美国 of snt 1 and the 美国 of snt 5 with `(s1c :same-entity s5u)`. Gold links only the main participant chain (周报 / newspaper across all five sentences), which the annotator got fully right.

Fix: "Link the document's participant chains. Do not link a country or place name that is used only as a modifier (`:place` of 小报, of 历史) to another such mention."

---

## 6. Smaller items

**Coordination grouping (snt 1).** Gold groups 奇闻轶事, written without 、, as an inner `and`: `(and :op1 (and :op1 奇闻 :op2 轶事) :op2 传奇 :op3 新闻)`. The annotator made a flat four-way `and`, which cost one missing entity node.
- Fix: "Nouns run together without 、 form their own inner `and`; 、 separates the outer conjuncts."

**Polarity on 未经 and the modal strength of 查证 (snt 2).** Gold gives 经-01 no `:polarity` but does mark it full-negative at the document level. It also gives 查证 `partial-affirmative`. Other Chinese gold data does use `:polarity -` for 未, so this looks like a quirk of this one gold document. I would **not** change the polarity rule.

**The 查证 structure (snt 2).** Gold wraps 查证 in `程序 :ARG0-of (identity-91 :ARG1 查证)`. The annotator's `:mod 查证-01` is a reasonable alternative. Leave this alone, or at most add the gold pattern as an example of "a 程序/过程 that is the event" (程序 :ARG0-of identity-91 :ARG1 event).

---

## What to keep (these worked)

- **Senses and concepts:** event, concept and sense checks were all at 100. Keep the instruction to look up each predicate in PropBank, and the `<word>-00` fallback.
- **Example-driven rules:** these were all reproduced exactly and scored fully:
  - title marks as name tokens;
  - the classifier as `:quant 1 :unit 份/个`;
  - `:place` for 美国小报;
  - `:medium 电视`;
  - `:part-of` in 纸本;
  - the shared modifier re-used across 新闻 and 专栏;
  - the 属-02 argument order;
  - the 以…而闻名 → `:reason` structure;
  - the 由于 → `:reason` noun;
  - have-degree-91 for 最富创意;
  - 历史上 as `:temporal (上 :op1 历史)`;
  - `but-91` with `:ARG1`/`:ARG2`;
  - 已经, 都, 也, 仍 as `:mod` on the event.
- **Aspect values:** habitual for 发行, 综合 and 报导; process for 未经/查证; performance for 被称为; activity for 继续; state for the modifier 停止. Keep these rules.
- **Modal and coreference basics:** `(root :modal author)` plus author full-affirmative, full-negative for the negated event, and the 周报 coreference chain across sentences. Keep these.