# Review of the UMR annotation of sentences 16–20: costly error patterns and changes to the instruction

The annotation is strong overall. Named entities, name tokens, `refer` attributes, coreference chains and document format all scored 100. Event and entity detection were at about 97, and core arguments of events at 98. The losses are in the temporal (F 76) and modal (F 74) relations, core arguments of abstract predicates (67) and reentrancy (67). They come from about seven patterns, listed below by cost. In several of them the annotator did what the instruction says, so the instruction itself has to change.

---

## 1. Conceivers of a publication's reports (snt16): about 7 modal units

**Cost:** 7 modal units. 报导, 注销 and 指 had the wrong parent; 支持, 当选 and 背书 were partial; 当-02 had an extra triple.

**What happened.** The instruction says "the content events of a claim get both (author …) and (speaker …)", and the annotator followed it:
- `(author :full-affirmative s16b)`, `(s16k :full-affirmative s16s)`, `(s16k :full-affirmative s16x2)` …

The gold does it the other way round. The paper is the conceiver of its own acts, and the reported content hangs only on the author:
```
(author :full-affirmative s16x4)          ; 该刊
(s16x4 :full-affirmative s16x)            ; 报导
(s16x4 :full-affirmative s16x2)           ; 注销
(s16x4 :full-affirmative s16x3)           ; 指
(author :full-affirmative s16x6)          ; 支持 (content) – author only
(author :full-affirmative s16x14) (author :full-affirmative s16x15)
```

**Why.** The rule in 5.2 is wrong for this document's convention.

**Change.** Replace the sentence "The content events of a claim … get both (author …) and (speaker …)" with this:

> When a publication or person is the subject of reporting or claiming verbs (报导, 指, 注销, 宣称), write `(author :full-affirmative SPEAKER)` and `(SPEAKER :full-affirmative V)` for each of those verbs, with no author triple on them. Each event of the reported content gets only `(author :full-affirmative X)`.

Also add a related rule:

> A verb that is the complement of a content verb (当 in 支持布什当总统) gets no `:aspect` and no modal triple. Its only triple is `(content-verb :overlap X)`.

---

## 2. A headline next to a common noun (snt20, 该刊的一篇新闻「…」): about 6 units

**Cost:** about 6 units: one core argument of the event, the identity-91 core arguments (abstract), 2 core labels, aspect and modal.

**What the annotator had.** Following the 旗下小报《X》 rule, the publication was the head:
```
:ARG2 (s20p / publication :name … :ARG1-of (s20i / identity-91 :ARG2 (s20x / 新闻 …)))
```
It added no aspect and no modal triple, as the instruction says for a -91 node inside a noun phrase.

**Gold:**
```
:ARG2 (s20x6 / 新闻 :quant 1 :unit (篇) :part-of (刊 :mod 该)
        :ARG1-of (s20i2 / identity-91 :ARG2 (s20p / publication :name …) :aspect state))
```
with `(author :full-affirmative s20i2)`.

**Change.** Add to 2.2/3:

> A 「headline」 in apposition after a common noun (新闻, 报导, 文章) is the reverse of the 小报《X》 case. The common noun is the head and the argument of the verb, with its 一篇 and 该刊 on it. It is `:ARG1-of (identity-91 :ARG2 publication :aspect state)`. This identity-91 gets `(author :full-affirmative i)` but no temporal triple.

This is an exception to the rule "a -91 node inside a noun phrase gets no aspect and no modal triple", and that rule should say so.

---

## 3. 为了 X，S 也 V (snt19): about 6 units

**Cost:**
- Concept: annotator had `have-purpose-91`; gold has `have-reason-91`.
- Extra `:aspect state` and an extra `(author :full-affirmative s19h)`.
- 讽刺: aspect `activity`, gold `performance`.
- Missing `:ARG0 s19p` on 讽刺.
- 美国的外交政策 was `:place`; gold has `:possessor`.

**Why.** The instruction itself requires each of these errors:
- "Purpose: have-purpose-91 … :aspect state and (author …)"
- "A purpose verb (为充分运用) is activity"
- "no subject copied onto a purpose verb"
- "A country … modifying a noun → :place"

**Gold fragment:**
```
(s19h / have-reason-91
   :ARG1 (报导-01 :ARG0 (s19p / person …) …)
   :ARG2 (讽刺-01 :ARG0 s19p :ARG1 (政策 :topic 外交 :possessor (country "美国")) :aspect performance))
```
No aspect and no modal triple on s19h.

**Changes.**
1. A sentence-initial 为了 X followed by a clause (without 因为/于是) → `have-reason-91 :ARG1 main :ARG2 X`, with no aspect, no temporal triple and no modal triple. The X verb is then:
   - `performance` when the main verb is completed (了);
   - re-entered with the main subject as its `:ARG0`.
2. Restrict the "no subject copied onto a purpose verb" rule to phrase-level `:purpose`.
3. Restrict the `:place` rule to a country placed directly before the noun (美国小报). X**的**N (美国的外交政策) → `:possessor`.

---

## 4. Temporal parents of events inside nouns and arguments: 6 units

| words | annotation | gold |
|---|---|---|
| 合成的照片 | `(s16x :before s16h)` | `(注销 :overlap 合成)` |
| 双方握手的…照片 | `(s16x :before s16w2)` | `(合成 :overlap 握手)`: chained to the other modifier of the same noun |
| 靠外星人背书当选 | `(当选 :before 背书)` | `(当选 :overlap 背书)` |
| 真实新闻 (新闻 is ARG0 of 荒谬) | `(点出 :overlap 真实)` | `(荒谬 :overlap 真实)` |
| 点出 [荒谬 与 可笑] | `(荒谬 :overlap 可笑)` | `(点出 :overlap 可笑)` |
| 复制人 | `(争论 :overlap 复制)` | no temporal triple |

**Why.**
- The participle rule "(V :before participle)" and "reason → :before (usual case)" pushed the annotator to `:before`.
- The rule "In (and :op1 A :op2 B), B's parent is A" was applied to an `and` inside an argument.
- The existing rule "an event inside a noun takes the event whose argument contains it" was not followed for 真实.

**Changes.**
1. Modifier events of a noun (合成的, 握手的) take `:overlap`. The first one takes the governing verb as parent, and each further one takes the previous modifier.
2. Keep `:before` only for 遗留下来的/留下的 types.
3. A `:reason` event nested in a reported clause (靠 X) → `:overlap`.
4. The chaining rule for `and` applies only to clause-level conjuncts. Conjuncts of an `and` that is an argument each take the verb governing the `and`.
5. Restate, with 真实新闻 as the example, that the parent is the predicate whose argument directly contains the noun.
6. 复制-01 in 复制人 gets the author triple but no temporal triple.

---

## 5. Reentrancy and stray nodes in snt16: about 6 units

**a. The time clause was re-used on each conjunct (2 extra reentrancies).** The annotator added `:temporal s16e` on 注销 and on 指, following "a sentence-initial date over an and root is :temporal of each clause's event". Gold puts the event-name time (2000年总统大选时) only on the first conjunct.

**Change:** re-use only for a `date-entity`. A `X时` / `event :name` time goes on the first conjunct only.

**b. :quote on nested content events (1 missing).** Gold also has `:quote s16x3` on 背书, which sits inside 当选.

**Change:** ":quote goes on every event inside the reported content, including `:reason`/`:condition` events nested in it."

**c. 也 inside reported content (2 units).** In 指柯林顿1992年也靠外星人背书当选, the annotator gave 也 a `:mod` node. Gold has no node.

**Change:** add to the exceptions: "也/还 inside a reported or embedded clause gets no node. Keep 也 only on the main verb of a stand-alone sentence (他们也报导了)."

**d. Aspect of an event-noun modifier.** 握手-01 under 照片 was `performance`; gold has `process`. Fix the instruction's example to `照片 :mod (握手-01 :aspect process)`.

---

## 6. Sentence-initial 如 / 例如 (snt18): 3 units

**Cost:** 3 units. The have-example-91 node is missing, the implicit-predicate node is missing, and there is a granularity mismatch.

**What happened.** The instruction has no rule for this. The annotator made 刊登 the root. Gold (and chinese_umr-0014 snt13, 例如…):
```
(s18h / have-example-91 :ARG1 (implicit-predicate) :ARG2 (s18x / 刊登-01 …))
```
with no aspect and no document-level triples on have-example-91. The main event keeps `(document-creation-time :before 刊登)`.

**Change.** Add this rule to 2.5.

---

## 7. Modal strength of an ability complement (snt17): 1 unit

**What happened.** 有能力 … 点出 had `(author :full-affirmative s17d)`. Gold has `(author :neutral-affirmative s17x7)`.

**Change.** In the 有能力 rule, add: "the VP under 能力 gets `(author :neutral-affirmative V)` (ability = *can*)." Keep the author triples on 有-06 and identity-91.

---

## Gold quirks not to chase
- **注销-00:** PropBank has 注销-01, which the annotator used correctly.
- **`:quant 1 :unit 篇` on 也** in snt19: this is a misplacement in the gold.
- **`:quote s16x` on 报导 itself:** a self-loop.

Do not add rules for any of these.

---

## What to keep
- **Named entities:** event, building and publication names with every mark as an `:opN`. 一篇 is `:quant 1 :unit 篇`, with no inner triples.
- **Nouns and modifiers:**
  - 好事者 → `者 :ARG0-of 好事-00 :aspect state`
  - 复制人 → `人 :ARG1-of 复制-01 :aspect process`
  - 真实新闻 → `新闻 :ARG0-of 真实-01`
  - 显著位置 → `位置 :ARG0-of 显著-01`
  - `墙上 :place-of 记者团`
  - `内容 :part-of 周报`
  - `编辑 :possessor` (其)
- **Clause structures:**
  - `but-91` for 虽然…但
  - `有-06 + 能力 :ARG1-of identity-91 :ARG2 VP`
  - 当选 `:reason` 背书 for 靠
- **Pronouns and coreference:**
  - 它 → `thing`, 他们 → `person` plural
  - all coreference links to the paper (scored 100)
- **Temporal anchors:**
  - Main events anchored `(document-creation-time :before X)`.
  - Clause-level conjuncts chained by `:overlap` (报导 → 注销 → 指 matched the gold).