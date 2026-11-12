# Review of the UMR annotation of the 《世界新闻周报》 document (5 sentences)

The annotation is close to gold. Concepts, entities, core and non-core roles, names and coreference all score 100. Every lost unit comes from a few narrow rules, and three of those mistakes were caused by the instruction itself (its wording or its own examples). The problems are listed from most to least costly.

## 1. 曾经 is treated as a time expression, and 拥有 gets the wrong aspect (3 units: 2 h_temporal, 1 c_aspect)

**Example (snt3, 该周报也曾经短暂的拥有过一个…节目):**
- **Annotation had:** `(past-reference :depends-on s3t)`, `(s3t :contained s3x)` and `拥有-01 … :aspect performance`.
- **Gold has:** `(document-creation-time :before s3x)`, `(s3x :overlap s3x6)` and `拥有-01 … :aspect state`. 曾经 gets no temporal parent.

**Why it happens:**
- The instruction says 曾经 → `:temporal (曾经)` in the graph. Section 5.1 then says "time expressions first … a vague one on past-reference". So the annotator gave 曾经 a parent and hung the event from it.
- 4.1 lists 过 as a cue for `performance`. The rule "拥有/有 is a state" is not stated strongly enough to override 过.

**Change:**
- In 5.1, put 曾经 next to 目前/现在: "曾经, 目前, 现在, 已经 are graph nodes only. They get no temporal parent, and no event hangs from them. A past event marked with 曾经 or 过 is `(document-creation-time :before <event>)`."
- In 4.1, add: "Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂."

## 2. 未经 gets `:polarity -` and `performance` (2 units: c_polarity, c_aspect)

**Example (snt2, 许多内容都未经…查证程序):**
- **Annotation had:** `(经-01 :polarity - … :aspect performance)`.
- **Gold has:** `(s2x8 / 经-01 :ARG0 … :ARG1 … :mod (都) :aspect process)`. The negation appears only at the document level, as `(author :full-negative s2x8)`.

**Why it happens:** Section 4.2 tells the annotator to put `:polarity -` on every concept negated by 未. Gold expresses this negation only through modal strength. A negated event never happened, so it cannot be a completed `performance`.

**Change:**
- Add: "未经 X / 没有经过 X → `经-01` with no `:polarity`. The negation goes only into the modal triple `(author :full-negative 经)`."
- Add: "A negated event (未, 没) never gets `performance`. Use `process` when its type cannot be told."

Keep the `full-negative` modal triple: the annotator got it right.

## 3. Wrong sense 停刊-00 (1 unit: b_event_sense)

**Example (snt4):**
- **Annotation had:** `停刊-00`.
- **Gold has:** `(s4x / 停刊-01 :ARG0 (纸本 …))`.

**Why it happens:** The instruction is wrong. Section 3 calls 停刊 "an intransitive Chinese verb not in PropBank", and the Aspect example in Examples writes `停刊-00`. Chinese PropBank does have `停刊-01` (ARG0 = the publication that stops circulation).

**Change:**
- Rewrite the rule as: "For an intransitive verb such as 停刊-01, the sole participant is `:ARG0`."
- Change the example to `停刊-01`.
- Add: "Look the verb up before using `-00`."

## 4. `:part-of` is added to an edition whose whole is not stated (1 unit: g_reentrancy)

**Example (snt4, 继续发行网络版):**
- **Annotation had:** `(s4x5 / 网络版 :part-of s4n)`.
- **Gold has:** `(s4x7 / 网络版)`.

**Why it happens:** Section 3 says an edition "takes `:part-of` its whole". The annotator applied this even though the whole is only implied. That also clashes with the instruction's own rule against adding arguments the text does not express.

**Change:** "An edition takes `:part-of` its whole only when the whole is written with it (《…》的纸本). A bare 网络版 gets no `:part-of`."

## 5. No `:aspect state` on the root abstract predicate (1 unit: c_aspect)

**Example (snt1):**
- **Annotation had:** `(s1i / identity-91 :ARG1 … :ARG2 …)`.
- **Gold has:** `(s1i2 / identity-91 … :aspect state)`.

**Why it happens:** The instruction only says that `have-degree-91` gets no aspect. It says nothing about `identity-91` as the root. Gold gives the root copular predicate `:aspect state`, but not an `identity-91` embedded under a noun (snt2: 程序 :ARG0-of identity-91, which has no aspect).

**Change:** "A root `identity-91` or `have-*-91` takes `:aspect state`. An `identity-91` inside a noun phrase (程序 :ARG0-of identity-91) and `have-degree-91` take none."

## 6. 被称为 is anchored with `:before` instead of `:depends-on` (1 unit: h_temporal)

**Example (snt5):**
- **Annotation had:** `(document-creation-time :before s5x)`.
- **Gold has:** `(document-creation-time :depends-on s5x)`.

**Why it happens:** The instruction gives `:depends-on` only for clauses with 目前/现在. A passive naming or reputation (被称为) is a judgement that still holds at the time of writing, and gold treats it the same way.

**Change:** "The main event of a naming or reputation clause (被称为, 被誉为) is `(document-creation-time :depends-on <event>)`, as with 目前."

## 7. Event nominal of a usual procedure gets the wrong modal strength (1 unit: i_modal)

**Example (snt2, 一般的新闻查证程序):**
- **Annotation had:** `(author :full-affirmative s2x14)`.
- **Gold has:** `(author :partial-affirmative s2x13)`.

**Why it happens:** No rule covers a generic or typical event nominal (一般的…查证) inside a negated event.

**Change (worth only one unit, so keep it narrow):** "An event nominal naming a usual procedure (一般的…程序) that sits under a negated event is `partial-affirmative` from the author."

## What to keep
- **Snt1 copular-root temporal pattern:** `DCT :before 发行`, `发行 :overlap 停止`, `闻名 :contained 发行`, `发行 :overlap 报导`. It matches gold exactly. The k_doc_format "two parents" flag on 发行 is in gold too, so do not change this pattern.
- **Snt4 temporal chain:** `目前` with `:depends-on` and the `:overlap` chain matched gold.
- **Rules that matched gold exactly:** classifiers as `:unit`, title brackets as `:opN`, no `:wiki`, country as `:place`, `:temporal (上 :op1 (历史))`, `have-degree-91` with no aspect, `属-02`, `称为-01`, `:reason` for 以…而, and the `identity-91` for 查证程序.
- **Other rules that matched gold:** 已经 → `state` inside a relative clause, `but-91`, and conservative coreference (the 周报 chain only, no link between the two 发行 events). Coreference scored 100.

The a_granularity miss (新闻 inside the newspaper's name) is a scorer artifact and needs no change.