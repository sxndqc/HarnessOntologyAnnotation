# Review of the 《世界新闻周报》 annotation: what in the instruction should change

The annotator found every event, sense, numbered role, peripheral role, name token and re-entrancy correctly (all 100). The losses come from seven patterns. Five come straight from the wording of the instruction, and the instruction itself causes two of the largest. They are listed below with the costliest first.

---

## 1. Modal triples and `:aspect` on connective and embedded abstract nodes (6 units: i_modal ×4, c_aspect ×2)

**What happened**
- **Modal triples on connectives.** The annotator wrote `(author :full-affirmative X)` for:
  - `and` (s2a, snt 2)
  - `but-91` (s4b, snt 4)
- **Modal triples on abstract predicates that only modify a noun.** It also wrote that triple for:
  - `identity-91` under 程序 (s2i, snt 2)
  - `have-degree-91` under 报纸 (s5h, snt 5)
- **Aspect on the same embedded predicates.** It gave `:aspect state` to s2i and s5h.

Gold:
```
(s2x12 / 程序 :ARG0-of (s2i2 / identity-91 :ARG1 (s2x13 / 查证-01 ...)))   ; no :aspect, no modal triple
(s5x4 / 报纸 :ARG1-of (s5h / have-degree-91 :ARG2 ... :ARG3 (s5x7 / 最)))   ; no :aspect, no modal triple
```
Gold's modal lists for snt 2 and snt 4 contain no triple for `and` or `but-91`.

By contrast, the identity-91 at the root of snt 1 (the copula 是) does get `:aspect state` and `(author :full-affirmative s1i2)` in gold.

**Why it happened.** Two lines of the instruction cause this:
- §4.1 says *"identity-91 and the other abstract predicates take :aspect state and a modal triple."* The example for 新闻查证程序 repeats this.
- §5.2 says "every event the author asserts" gets a triple, and gives no exception for connectives.

The annotator followed these lines exactly.

**Change.** Replace the §4.1 bullet and add a line to §5.2:
> An abstract predicate gets `:aspect state` and a modal triple **only when it is the predicate of a clause** (the copula 是 → root `identity-91`). An abstract predicate that only reifies a noun modifier — `identity-91` under `:ARG0-of` of a noun (查证程序), `have-degree-91` for a superlative or comparative modifier (最富创意的报纸) — gets **no** `:aspect`, no modal triple and no temporal triple.
> Discourse connective nodes (`and`, `or`, `but-91`, `contrast-91`) get no modal triple. Only their conjuncts do.

Fix the 程序 example to match: `(i / identity-91 :ARG1 (c / 查证-01 …))` with no aspect.

## 2. `publication` instead of `newspaper` for the paper's name (4 units: a_entity_concept ×2, a_granularity ×2)

**What happened.** In snt 1 and snt 4 the annotator wrote `(s1p / publication :name ...)`. Gold has `(s1n / newspaper :name (s1n2 / name :op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》"))`. The granularity misses come with the same node: the predicted node was aligned to the whole name, while gold's node is matched to the word 新闻.

**Why it happened.** §2.2 explains title marks with the words "a publication's name", and the type list has no rule for choosing between `newspaper`, `magazine` and `publication`.

**Change.** Add to §2.2:
> A newspaper, weekly or tabloid (报, 周报, 日报, 小报) is `newspaper`; a magazine is `magazine`; use `publication` only when the kind is unknown.

Reword the title-mark example as "《世界新闻周报》 → `(n / newspaper :name ...)`".

## 3. `:wiki` added to named entities (3 units: f_wiki P 0)

**What happened.** The annotator added `:wiki "Weekly_World_News"` (snt 1 and snt 4) and `:wiki "United_States"` (snt 1 and snt 5). The Chinese gold has no `:wiki` anywhere.

**Why it happened.** §2.2 calls `:wiki` "optional" and shows it in the model entity `(c / country :wiki "Russia" ...)`, so the annotator took it as expected.

**Change.**
> The Chinese release data has no `:wiki`. Do not add `:wiki` to Chinese named entities.

Remove `:wiki` from the §2.2 example, or mark it "English only".

## 4. Temporal anchoring (3 units: h_temporal 77)

**a. The 报导 event in the 以…而闻名 clause got the wrong parent (1 unit).** The annotator wrote `(s1w :overlap s1b)`, with 闻名 as parent. Gold has `(s1x3 :overlap s1x8)`: 报导 anchors to the main event 发行. Both are habitual activities of the tabloid; 闻名 is only a state that results from them.

**Why.** The rule "relative clauses and complements → their governing event" led the annotator to take 闻名 as the governor.

**Change.** Add to §5.1:
> In 以 X 而闻名, the reason event X takes the clause's main event as parent: `(main :overlap X)`, not `(闻名 :overlap X)`.

**b. Main events whose result holds at present (2 units).** The annotator wrote `(document-creation-time :before s4t)` for 目前…已经停刊 and `(document-creation-time :before s5c)` for 被称为. Gold has `(document-creation-time :depends-on s4x)` and `(document-creation-time :depends-on s5x)`.

**Why.** §5.1 gives only `:before`, `:overlap` and `:after` for anchoring an event to the document creation time.

**Change.** Add to §5.1:
> A main event that is a completed change whose result holds now (目前……已经 V, a current label 被称为/被誉为) anchors as `(document-creation-time :depends-on e)`. Plain past events (snt 1–3 here) keep `:before`.

## 5. Coreference between repeated country modifiers (2 units: j_coref_chain P 71)

**What happened.** The annotator wrote `(s1c :same-entity s5c3)` linking 美国 in snt 1 and snt 5. Gold links only the chain of the newspaper itself.

**Change.** Add to §5.3:
> Link the document's discourse participants: names, pronouns, 该/其 descriptions. Do not link repeated mentions of a country or place that only serves as a modifier (`:place` of a noun, `历史 :place 美国`).

## 6. Two temporal parents for one event (1 unit: k_doc_format)

**What happened.** s1x3 has two parents: `(document-creation-time :before s1x3)` and `(s1w :contained s1x3)`. Gold has the same two triples, so the temporal check still counted both as correct. The format check penalizes it anyway.

**Why.** The instruction's own temporal example (§5.1 and Examples) gives this pair.

**Change.** Keep it, because it matches gold. Add a note that this pattern for 闻名 is the one allowed exception to "one parent per event".

---

## What to keep

These rules worked and should stay unchanged:
- Classifier as unit: `:quant 1 :unit 份/个`.
- Title marks as `:op1`/`:opN` name tokens.
- The 已经停止发行 pattern, with `停止-01 :aspect state`.
- 发行 and 综合 as `habitual`.
- 未经 → `经-01 :aspect process`, with the negation only in the modal triple `(author :full-negative 经-01)` and `:partial-affirmative` on 查证.
- Shared modifiers repeated on each conjunct of `and`.
- `其中` as `:mod`, `曾经` as `:temporal`, `短暂` as `:duration`.
- `属-02` with the program as ARG0 and the paper as ARG1.
- `纸本 :part-of` the newspaper.
- `but-91` with `:ARG1`/`:ARG2`, and its second conjunct anchored with `:overlap`.
- No filled zero subject for 继续发行.
- The superlative with `:temporal (上 :op1 (历史 :place 美国))`.
- The reason 内容 with `:possessor` re-entrancy.
- Main events of snt 2 and snt 3 anchored to the document creation time, not to an earlier sentence.
- The newspaper's coreference chain linked to the closest earlier mention.