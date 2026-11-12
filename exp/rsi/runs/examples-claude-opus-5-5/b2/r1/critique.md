Below are the error patterns, most costly first. Each cost is the number of judge units involved. "Gold" is the expert annotation.

## 1. Time-anchoring rules for dates and connected events go against gold (h_temporal F 19, 13 of about 16 units lost)

**Explicit dates (6 units in sentences 6, 9 and 10).** The instruction tells the annotator to hang an absolute date on `root` and to put the event `:contained` in the date. The annotator did exactly that every time. Gold does something else every time:
- *创刊于1979年*:
  - annotator: `(root :depends-on s6d) (s6d :contained s6c)`
  - gold: `(document-creation-time :before s6d) (s6d :overlap s6x)`
- Sentences 9 and 10 (1980年代, 2007年) follow the same pattern.

**Fix:** replace the rule. A past date in the text → `(document-creation-time :before date)`. The event of that date → `(date :overlap event)`. Remove "absolute date depends on root" and "`(s1t :contained s1e)`".

**Purpose and reason clauses in sentence 7 (4 units).**
- *为充分运用* and *容纳*: the annotator wrote `(s7c :before s7y)` and `(s7c :before s7r)`. Gold has `(s7x13 :overlap s7x8)` and `(s7x13 :overlap s7x17)`. The instruction's line "a purpose is `:after` its main event" (which the annotator turned into `:before`) is wrong for gold. The fix is purpose → `:overlap`.
- The reason *改为* happened before the founding. The annotator wrote `(s7c :after s7g)`. Gold has `(s7x13 :before s7x)`. Since the relation says where the child is relative to the parent, an earlier cause is `:before`. Add a worked example for this.
- *遗留下来的印刷机*: gold has `(运用 :before 遗留)`, and 遗留 is `performance`, not `state`.

**A sentence that continues the previous one (1 unit).** *黑白印刷也成了该刊的特色* continues the founding story. Gold anchors it as `(s7x13 :overlap s8x)`. The annotator used `document-creation-time :before`, following the rule that the main event must never anchor to an earlier sentence.

**Fix:** loosen that rule. When a sentence continues the narrative of the previous one (也, 于是, or a result of the event just told), anchor its main event to that earlier event.

## 2. Reason and purpose clauses written as roles instead of `have-reason-91` / `have-purpose-91` (about 12 units: a_event, d_core_args_abstract, aspect, modal)

In *因为 X，为 Y，于是 Z*, the annotator used `:reason` and `:purpose` on 创立. Gold reifies them as a nested structure:

```
(s7h / have-reason-91
    :ARG1 (s7h2 / have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state)
    :ARG2 改为
    :aspect state)
```

Both predicates are asserted: `(author :full-affirmative s7h)` and `(author :full-affirmative s7h2)`. The Chinese gold corpus does this regularly (the 于海 sentences: 因为…而, 所以). The instruction's §2.5 only offers `:reason` / `:purpose`, so the annotator never considered the reified form.

A related point: the annotator gave 运用 the modal parent `purpose`, which the judge rejects as an unknown constant (k_doc_format). Gold has `(author :full-affirmative s7x8)`.

**Fixes:**
- When a clause-level 因为/由于 … (于是/所以) or 为(了) links two full clauses, use `have-reason-91` (`:ARG1` result, `:ARG2` cause) and `have-purpose-91` (`:ARG1` main event, `:ARG2` purpose), each with `:aspect state` and a full-affirmative modal triple.
- Keep `:reason` only for phrase-level 由于 + noun.
- Delete the `purpose` / `have-condition` constants from §5.2.

## 3. 发行量 / quantity constructions (about 14 units in sentences 9–10)

The annotator treated 发行量 as a single entity with `:possessor` and wrote `份 :quant N`. Gold splits it and reifies the amount:

```
(s9x2 / 量
    :quant-of (s9x3 / 发行-01 :ARG1 (s9n / newspaper ...))
    :ARG1-of (s9h / have-quant-91 :ARG2 1200000 :unit (s9x4 / 份)))
```

The hidden event 发行 then needs a temporal triple: `(s9x :overlap s9x3)`. The instruction's classifier rule (`:quant N :unit`) pushed the annotator toward `份 :quant`. It also caused the wrong `:ARG3` on 跌-01 and the false coreference chain from 发行量 to 发行量 (j_coref precision).

**Fix:** add a rule for V+量 nouns (发行量, 销量, 产量): `量 :quant-of V-01`. A number reached or dropped to (达到/跌至 N 份) goes on 量 as `:ARG1-of (have-quant-91 :ARG2 N :unit 份)`, not as an argument of the verb. A quantity measured at different times is not the same entity.

## 4. Sentence 7 entity structure (about 15 units: entity concept, core args, reentrancy)

**黑白版面的《世界新闻周报》.** Gold's argument of 创立 is the edition, not the paper:

```
(s7x14 / 版面 :mod 黑白 :part-of (newspaper ...))
```

That 版面 is also the `:ARG0` of 容纳. The annotator made the newspaper the argument and hung 版面 as a `:mod`. In the same way, gold's *改为* has `:ARG1 (版面 :mod 黑白 :part-of 《国家询问报》)`, not the newspaper plus `:source`.

**Fix:** "X 版面/版 of a publication" → `版面 :part-of publication`. This extends the existing 纸本 rule, so state it generally for edition and format nouns.

**创始人.** Gold has:

```
(individual-person :name ...
    :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance))))
```

The annotator wrote `person :ARG0-of have-org-role-92 :ARG2 newspaper`. The role is wrong (`:ARG0` instead of `:ARG1`), and so is the `:ARG2`.

Also, the Chinese gold uses `individual-person` for named people (confirmed in other documents). The instruction's type list says `person`, so add `individual-person` for named humans in Chinese.

**旗下的八卦小报《国家询问报》.** This is an appositive. Gold:

```
newspaper :ARG1-of (identity-91 :ARG2 (小报 :mod 旗下 :mod 八卦))
```

The annotator dropped 小报 and 旗下 and invented `:possessor s7p`.

**Fix:** add a rule for appositive common noun + name: `identity-91 :ARG2`.

**Invented re-entrancies (g_reentrancy P 20).** The annotator added `:ARG0 s7p` on 运用 and `:possessor s7p`, among others. The instruction already says to add re-entrancy only when the text expresses it. Extend that from Chinese zero subjects to purpose clauses and possessors.

## 5. A common noun for a publication typed as `newspaper` (2 units)

The annotator typed *该刊* as `newspaper`. Gold has `(刊 :mod 该)`. The newspaper / magazine typing in §2.2 is for named entities only.

**Fix:** say that unnamed mentions keep the Chinese word as the concept.

## 6. Smaller items

- **Sentence-initial 不过 (1 or 2 units).** Here 不过 links to the previous sentence, so there is no first conjunct inside the sentence. Gold drops it, and 跌-01 is the root. The annotator built a `but-91` with only an `:ARG2`. **Fix:** use `but-91` only when both conjuncts are inside the sentence.
- **1980年代 (1 unit).** Gold has `:era 1980`, not `:decade`. Add this as an example.
- **黑白印刷 (1 unit).** A modifier of an event noun that tells how it is done is `:manner`, not `:mod`.
- **容纳 aspect (1 unit).** Gold has `process`, not `habitual`. The rule "a characteristic activity of an institution is habitual" was over-applied to a purpose or relative-clause event. Limit it to main predications.
- **运用 aspect (1 unit).** Gold has `activity`, not `process`.

## What to keep

These rules worked and should stay:
- Title-mark name tokens with `newspaper` typing and no `:wiki` (f_name_tokens 100).
- Sense choice from PropBank (b_event_sense 100).
- Polarity on 不符合, with `full-negative` in the modal triple.
- 已经 / 也 kept as `:mod` on the event.
- Performance aspect for completed past events.
- `(root :modal author)` plus author full-affirmative for asserted events.
- Cross-sentence `:same-entity` chains for the newspaper, linking entity nodes only and closest earlier mention first. Coref recall was 100.