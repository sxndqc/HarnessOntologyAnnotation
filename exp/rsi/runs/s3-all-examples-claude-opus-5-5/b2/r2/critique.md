Across these five sentences the annotation matches gold on almost every check. Event and entity concepts, core roles, role labels, name tokens, coreference and format all score 100. The losses come from five patterns. Four of them come straight from the instruction: one rule is too broad, two rules are missing, and two examples are wrong.

## 1. `:aspect state` and a modal triple on -91/-92 nodes inside a noun phrase (8 units, the costliest)
**Cost:** c_aspect 4 extra and i_modal 4 extra. The nodes are have-org-role-91 s7h3, identity-91 s7i (the appositive), and have-quant-91 s9h and s10h.

**Example:**
- 创始人 格内洛索·波普: the annotation had `(s7h3 / have-org-role-91 :ARG3 (s7r / 人 …) :aspect state)` plus `(author :full-affirmative s7h3)`.
- Gold has `(s7h3 / have-org-role-91 :ARG3 (s7x22 / 人 …))`, with no aspect and no modal triple.
- 发行量达到120万份: the annotation had `(s9h / have-quant-91 :ARG2 1200000 :unit (s9u / 份) :aspect state)` plus `(author :full-affirmative s9h)`. Gold has the same node with neither.

**Why:** the annotator followed the instruction. Section 4.1 says "`identity-91` and the other -91/-92 predicates are events too: give them `:aspect state` and a modal triple". That holds only for -91 nodes that are clause-level predicates. In this document those are have-reason-91 and have-purpose-91, which gold does annotate this way. Other gold documents follow the same split: a clause-level `identity-91` ("X 为 Y") has `:aspect state`, but an appositive `:ARG1-of (identity-91 :ARG2 名模)` and `have-org-role-91` have no aspect.

**Change:** replace the 4.1 bullet with something like:
> "A -91/-92 node that is the predicate of a clause (X 是 Y as the main or a conjoined clause, have-reason-91, have-purpose-91) gets `:aspect state` and `(author :full-affirmative X)`, and no temporal triple. A -91/-92 node *inside a noun phrase* gets no `:aspect`, no temporal triple and no modal triple. That covers an appositive `:ARG1-of (identity-91 …)`, `have-org-role-91`/`have-rel-role-92` that reify a role noun, and `have-quant-91` under 量."

Also fix the examples that contradict this:
- Remove "identity-91 → `:aspect state`" from the aspect example, or limit it to clause-level use.
- In the 创始人 example, state that have-org-role-91 has no aspect.

## 2. `:aspect habitual` on 发行-01 under 量 (2 units)
**Cost:** c_aspect 2 extra (s9f and s10f).

**Example:** 该刊发行量: the annotation had `(s10f / 发行-01 :ARG1 (s10k / 刊 …) :aspect habitual)`. Gold has `(s10x3 / 发行-01 :ARG1 (s10x4 / 刊 …))`, with no `:aspect`.

**Why:** the 量 rule says the inner 发行-01 "gets `(main :overlap 发行)` but no modal triple". It says nothing about aspect. Meanwhile the general rule "publishing 发行 … is habitual" applies.

**Change:** extend the rule to say: "The inner 发行-01 under `量 :quant-of` has **no `:aspect`** and no modal triple. Its only document-level relation is `(main :overlap 发行)`." Keep the temporal triple: the annotator got it right in both sentences.

## 3. 黑白印刷 annotated as an entity with no sense (4 units)
**Cost:** b_event_sense 1, c_aspect 1 missing, h_temporal 1 missing, i_modal 1 missing.

**Example:** 黑白印刷也成了该刊的特色: the annotation had `:ARG0 (s8y / 印刷 :manner (s8h / 黑白))` and no triples for it.

Gold has:
```
:ARG0 (s8x2 / 印刷-01 :manner (s8x3 / 黑白) :aspect habitual)
```
plus `(s8x :overlap s8x2)` and `(author :full-affirmative s8x2)`.

**Why:** the instruction's own example is wrong. It reads "Manner (3): 黑白印刷 → `(y / 印刷 :manner (h / 黑白))`", and the annotator copied it exactly. The rule beside it ("A modifier of an event noun … is `:manner`") calls 印刷 an event noun, but the example drops the sense.

**Change:** correct the example to `(y / 印刷-01 :manner (h / 黑白) :aspect habitual)`, with `(成 :overlap 印刷)` and `(author :full-affirmative 印刷)`. Then add a general line: "An event noun that is the subject or object of a verb (印刷 as the thing that 成了特色) keeps its PropBank sense and gets aspect, a temporal parent and a modal parent. A paper's ongoing practice is `habitual`."

## 4. A recurring named entity defined at its second mention, and its part relation inverted (4 units)
**Cost:** g_reentrancy 1 missing and 1 extra, d_peripheral_entity 1 missing and 1 extra.

**Example:** 《国家询问报》 appears twice in sentence 7: first as the paper whose 版面 is changed (将由黑白版面改为彩色版面), then as the owner of the 标准. The annotation defined the full named entity under `标准 :possessor (s7z2 / newspaper :part s7b3 :name … :ARG1-of (identity-91 …))` and pointed back to the 改为 版面 with `:part`.

Gold defines the entity at its first textual mention and reuses the variable later:
```
:ARG2 (s7x / 改为-01
    :ARG1 (s7x4 / 版面
        :part-of (s7n / newspaper :name (…"国家" "询问" "报"…)
                      :ARG1-of (s7i2 / identity-91 :ARG2 (s7x5 / 小报 :mod 旗下 :mod 八卦)))
        :mod (s7x16 / 黑白)) …)
… (s7x21 / 标准 :possessor s7n)
```

**Why:** the annotator also missed that 旗下的八卦小报《国家询问报》将由黑白版面改为… means the paper's 版面 changes. That 版面 is `:part-of` the paper, written on the 版面, as the existing rule "X版面的《Y》 / Y的X版面 … `:part-of` the publication" says. The PENMAN serialization puts `:ARG1` (创立) before `:ARG2` (改为), so the annotator wrote the entity out in full at the place that comes first in the graph. That was its later word mention.

**Change:** add two rules.
- "When an entity is mentioned twice in one sentence, write its full node (name, appositive, modifiers) where it is mentioned **first in the text**, and use the bare variable at the later mention (`标准 :possessor s7n`), even if the later mention comes earlier in the graph."
- "A 版面 or edition that belongs to a paper is always `版面 :part-of paper`, written on the 版面. Never write `paper :part 版面`."

## 5. A node for the preposition 至 before a date (2 units)
**Cost:** a_entity_found 1 extra, d_peripheral_event 1 partial.

**Example:** 至2007年: the annotation had `:temporal (s10z / 至 :op1 (s10d / date-entity :year 2007))`. Gold has `:temporal (s10d / date-entity :year 2007)`.

**Why:** the annotator likely extended the 美国历史上 → `(上 :op1 历史)` example to a preposition. Nothing in the instruction says that 在/至/到/于 + a date gets no node. The annotator did handle 在1980年代 and 于1979年 correctly.

**Change:** add "A preposition before a time (在, 于, 至, 到, 从 … 年) gets no node. The date-entity is the `:temporal` itself. The 上 of 历史上 is the only exception shown."

## What the instruction should keep
These rules produced correct annotations here and should stay:
- **Reified skeleton:** the have-reason-91 / have-purpose-91 skeleton, with aspect and modal on both.
- **Sentence 7 rules:** the 版面 `:part-of` 《世界新闻周报》 plus `:ARG0-of 容纳-01 :aspect process`, the appositive `identity-91 :ARG2 小报 :mod 旗下 :mod 八卦`, and `人 :ARG0-of 创始-00`. Also the procedure for 改为-01 with `:ARG1`/`:ARG2`.
- **Quantity:** `量 :quant-of 发行-01` with `have-quant-91 :ARG2 N :unit 份`.
- **Names and common nouns:** title marks as name tokens, no `:wiki`, `individual-person`, and 该刊 → `刊 :mod 该` rather than a newspaper type.
- **Adverbs and connectives:** 已经 and 也 as `:mod`, no node for sentence-initial 不过, and `:era 1980`.
- **Temporal anchoring:** a date anchored to `document-creation-time` and then `(date :overlap main)`, `(prev-main :overlap 成)` for 也成了, and purpose/reason/participle anchoring all matched gold (h_temporal precision 100).
- **Coreference:** the chain linking each mention to its closest earlier mention (j_coref_chain 100).