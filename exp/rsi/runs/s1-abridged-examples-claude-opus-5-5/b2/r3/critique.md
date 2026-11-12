The annotation matches gold on every check except two, and both come from one wrong decision in sentence 7. The other 19 checks are at 100%.

## Problem 1: in sentence 7, the repeated entity was written out in full at the wrong mention (the only cost)

**Cost:** 4 units in total.
- **d_peripheral_entity** dropped to F 91, with 2 units lost: one extra `标准 :possessor` edge and one missing `newspaper :part 版面` edge.
- **g_reentrancy** dropped to R 0 / P 0, with 2 units lost: gold's one re-entrancy was missing and the annotation had an extra one instead.

**What happened.** 《国家询问报》 appears twice in sentence 7:
- first in the 因为 clause (旗下的八卦小报《国家询问报》将由黑白版面改为彩色版面, words 6–14);
- again near the end (不符合《国家询问报》标准, words 48–52).

The annotator wrote the full node (the name plus the apposition `identity-91 :ARG2 (小报 :mod 旗下 :mod 八卦)`) under 标准, the later mention. It then pointed back to it from 改为:

```
:ARG1 (s7h2 / have-purpose-91 :ARG1 (s7x / 创立-01 ...
        (s7s / 标准 :possessor (s7n / newspaper :name (...) :ARG1-of (s7id / identity-91 :ARG2 (s7k / 小报 ...))))
...
:ARG2 (s7g / 改为-01 :ARG1 (s7v / 版面 :part-of s7n ...))
```

Gold writes it in full at the first mention in reading order, under 改为, and 标准 points back to it:

```
:ARG2 (s7x / 改为-01
    :ARG1 (s7x4 / 版面
        :part-of (s7n / newspaper :name (s7n2 / name :op1 "《" :op2 "国家" :op3 "询问" :op4 "报" :op5 "》")
                    :ARG1-of (s7i2 / identity-91 :ARG2 (s7x5 / 小报 :mod (s7x6 / 旗下) :mod (s7x7 / 八卦))))
        :mod (s7x16 / 黑白)) ...)
...
(s7x21 / 标准 :possessor s7n)
```

**Why it happens.** The instruction's rule is self-contradictory in exactly this situation: "Build a repeated entity in full … at its first mention in the graph (first in reading order)". Because of `have-reason-91`, the 创立 branch (`:ARG1`) is written before the 改为 branch (`:ARG2`) in the PENMAN graph, even though the 改为 clause comes first in the text. So "first in the graph" points to 标准 and "first in reading order" points to 改为. The annotator chose graph order. The 改为 example in the instruction does show the gold pattern (`改为 :ARG1 (版面 :part-of (s7n / newspaper … identity-91 …))`, later `(标准 :possessor s7n)`), but it doesn't say this holds even when the 改为 branch is written last.

**Change to the instruction.** In section 3, replace the rule with something like:

> Build a repeated entity in full (name, apposition, modifiers) at the mention that comes **first in the sentence's word order**, even when that mention's branch is written later in the PENMAN graph (for example under `have-reason-91 :ARG2`). Every other mention, including ones in branches written earlier in the graph, is the bare variable. So in 因为《X》将由…改为…，…于是创立…，容纳不符合《X》标准的文章, the full node goes under 改为 (`版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 …))`) and 标准 gets `:possessor s7n`.

Also add the same note to the 改为 example: "although 改为 is `:ARG2` of `have-reason-91` and is written last, it holds the full node."

## What to keep

Everything else matched gold exactly, and these rules should stay as written:
- **Clause structure:** `have-reason-91` / `have-purpose-91` nesting with `:aspect state` and full-affirmative modals; the purpose event 运用 as `activity`; 遗留 ordered before 运用 (`:before`); 改为 with no `:ARG0` and the subject attached through `:part-of`.
- **Entities and words:** the apposition pattern with `identity-91`; `individual-person` with the middle dot as its own `:opN`; the 创始人 → `have-org-role-91` + `创始-00` pattern; 该刊 → `(刊 :mod (该))`; 黑白印刷 with `:manner` and `habitual`; 成-01 taking the theme as `:ARG0`.
- **V+量 compounds:** 发行量 built as `量 :quant-of 发行-01 :ARG1-of have-quant-91`, with no aspect or modal triple on 发行 and only `(达到 :overlap 发行)` as its temporal link.
- **Time and adverbs:** dates as `(document-creation-time :before date)` then `(date :overlap event)`, including `:era 1980`; 已经 as `:mod`; sentence 8 hanging from the previous sentence's main event.
- **Modal and coreference:** the 未经/不符合 negation handled as `:polarity -` with `full-negative`; coreference chained across sentences to the nearest earlier mention (周报 → 该刊 → 《…周报》 → 该刊), with no extra links.