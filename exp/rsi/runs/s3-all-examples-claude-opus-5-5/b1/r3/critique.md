# Review of the UMR annotation of the《世界新闻周报》 document: error patterns and instruction changes

The annotation is close to gold. Senses, name tokens, re-entrancy, coreference chains and document format all score 100. The losses come from a few patterns, listed below with the most costly first.

---

## 1. The compound 新闻查证程序 was flattened into `:mod`s (about 8 units)

**Cost:** a_event_concept, a_entity_found, a_granularity ×2, d_core_args_abstract ×2, d_core_args_event, d_peripheral_entity. The same node also caused one h_temporal error and one i_modal error.

**Example (snt 2, 一般的新闻查证程序):**
- The annotation had `(s2c2 / 程序 :mod (s2y / 一般) :mod (s2x2 / 新闻) :mod (s2c / 查证-01))`.
- Gold has:
  ```
  (s2x12 / 程序
      :ARG0-of (s2i2 / identity-91
          :ARG1 (s2x13 / 查证-01 :ARG1 (s2x14 / 新闻) :aspect process))
      :mod (s2x15 / 一般))
  ```
- In the document level, gold anchors 查证 to the event of its own clause, `(s2x8 :overlap s2x13)`. The annotation anchored it to the main event 综合 (s2z). Gold also gives 查证 the modal strength `author :partial-affirmative`; the annotation had full-affirmative.

**Why it happens:** The instruction has no rule for a noun–verb–noun compound (N1 V N2), where N2 is a procedure, method or process and V is an event that names it. The rule "event inside a noun → `(main-event :overlap X)`" also sends the annotator to the sentence's main event, when the event that holds the noun is the right parent.

**Change:** Add these rules to section 3 and section 5.1:
- "In N1 + V + N2, when N2 (程序, 过程, 制度, 方式, 手续) is the procedure that V names: annotate `N2 :ARG0-of (identity-91 :ARG1 V)`. N1 is the object of V (`V :ARG1 N1`), not a `:mod` of N2. Example: 新闻查证程序 → `(程序 :ARG0-of (i / identity-91 :ARG1 (查 / 查证-01 :ARG1 (新闻))))`."
- In 5.1, replace "normally `(main-event :overlap X)`" with: "an event inside a noun takes as parent the event whose argument contains it (未经…查证程序 → `(经-01 :overlap 查证-01)`), not the sentence's main event."

## 2. The definite description 该周报 was typed as `newspaper` (3 units)

**Cost:** a_entity_concept in snt 2, 3 and 5.

**Example:** the annotation had `(s2p / newspaper :mod (s2g / 该))`; gold has `(s2x2 / 周报 :mod (s2x3 / 该))`. The same happens with s3p and s5p.

**Why it happens:** The annotator applied the English entity type of the named mention《世界新闻周报》 to every later mention of it. The instruction says to use English "for entity types", but it does not say this applies only to named entities.

**Change:** Add to section 2.1/2.2: "Use an English entity type (`newspaper`, `person`, `country`) only for a node with `:name`, or for a pronoun. A common-noun mention, even one that refers back to a named entity (该周报, 这家公司), is the Chinese word itself (`周报`) with its `:mod (该)`. Coreference links it to the named mention."

## 3. Gold gives have-degree-91 no aspect, no temporal parent and no modal parent (3 units)

**Cost:** c_aspect extra, h_temporal extra, i_modal extra.

**Example (snt 5, 最富创意的报纸):**
- The annotation had `(s5h / have-degree-91 ... :aspect state)` with the triples `(s5c :overlap s5h)` and `(author :full-affirmative s5h)`.
- Gold has `(s5h / have-degree-91 :ARG2 (富-01 … :aspect state) :ARG3 (最))`, with no `:aspect` and no document-level triples. Only 富-01 gets `(s5x :overlap s5x5)` and `(author :full-affirmative s5x5)`.

**Why it happens:** The instruction tells the annotator to give "identity-91 and the other -91/-92 predicates" `:aspect state` and a modal triple. That holds for identity-91, but gold treats have-degree-91 differently.

**Change:** Add an exception: "have-degree-91 gets no `:aspect`, no temporal triple and no modal triple. The property under its `:ARG2` (富-01) carries the aspect, the temporal triple and the modal triple." Fix the superlative example in the instruction to match.

## 4. The temporal relations of 闻名 and 称为 do not match gold (3 units)

**Cost:** h_temporal: snt 1 extra + partial, snt 5 wrong.

**Example, snt 1 (以…而闻名):**
- The annotation had `(s1f :overlap s1w)`.
- Gold has `(s1x7 :contained s1x3)`: the reputation state 闻名 is the parent, and the publishing event 发行 lies inside it.
- The instruction's own example ("anchor … the 以…而 result … to the main anchoring event") led the annotator to the wrong triple.

**Example, snt 5 (被称为):**
- The annotation had `(document-creation-time :before s5c)`; gold has `(document-creation-time :depends-on s5x)`.
- The instruction contradicts itself. Section 5.1 says both "The sentence's main event attaches directly: `(document-creation-time :depends-on …)`" and "Anchor each sentence's main event to document-creation-time (`:before` if past)". Gold uses `:before` for clearly past events (snt 1–3: 停止发行, 综合了, 曾经拥有过). It uses `:depends-on` for main events that are still current or that evaluate the entity (snt 4 with 目前, snt 5 with 被称为).

**Change:**
- Make the 5.1 rule explicit: "`:before` when the main event is clearly past (了, 过, 曾经, 已经停止). `:depends-on` when it is a current state, or a naming or evaluation that still holds (目前…, 被称为, 被誉为)."
- Replace the 以…而 part of the dependents example with: "以 X 而闻名: the reputation state is the parent of the habitual event, `(闻名 :contained 发行)`. 闻名 itself gets no parent."

## 5. 曾经 was annotated as `:mod` instead of `:temporal` (2 units)

**Cost:** d_peripheral_event, e_peripheral_labels.

**Example:** in 曾经…拥有过, the annotation had `:mod (s3c / 曾经)`; gold has `:temporal (s3x9 / 曾经)`.

**Why it happens:** The instruction's adverb list puts 已经, 都, 也, 仍, 还 under `:mod` and names only 目前 under `:temporal`. 曾经 is not mentioned, so the annotator treated it like 已经.

**Change:** Write: "Time adverbs 目前, 曾经, 现在, 当时 → `:temporal`. Aspectual and scalar adverbs 已经, 都, 也, 仍, 还 → `:mod`."

## 6. 未经 was given `:polarity -` (1 unit)

**Example:** the annotation had `(s2j / 经-01 :polarity - …)`. Gold has no `:polarity` on 经-01 and marks the negation only as `(author :full-negative s2x8)`.

**Change:** Add to the 未经 rule: "未经 → `经-01`, `:aspect process`, no `:polarity -`. The negation is only the modal triple `(author :full-negative …)`." The annotator's full-negative triple was correct and should stay.

---

## What the instruction should keep

These rules all reproduced gold exactly. Keep them as they are:
- **Snt 1:** title-mark name tokens, the classifier `:quant 1 :unit 份`, `:place` for 美国, the V1V2的N chain (发行 `habitual` / 停止 `state` with `:mod 已经`), 以…而闻名 as `:reason`, and the inner `and` for 奇闻轶事.
- **Snt 2:** the shared modifiers re-used across conjuncts.
- **Snt 3:** the 属-02 argument order, `:medium 电视`, and `state` aspect for 拥有过.
- **Snt 4:** but-91, 纸本 `:part-of` the newspaper, no owner on 网络版, and the 目前 sentence's document-level temporal triples.
- **Snt 5:** 由于 → `:reason`, 历史上 → `:temporal (上 :op1 历史)`, and 被称为 → `performance`.
- **Document level:** the coreference chain linked to the closest earlier mention, and the identity-91 handling (aspect `state`, modal triple, no temporal triple).