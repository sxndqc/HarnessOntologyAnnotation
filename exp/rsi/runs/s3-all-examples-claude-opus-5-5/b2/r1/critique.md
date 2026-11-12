Ranked by cost, most costly first. The main losses are the temporal checks (h_temporal F 39), the snt7 structure (d_core_args_abstract 0, g_reentrancy P 20), and the 发行量/target-number pattern in snt9 and snt10.

## 1. Temporal relations: the instruction teaches relation labels that the gold does not use (about 10 h_temporal units)

**The pattern.**
- **Date to event:** the annotator wrote `(s6d :contained s6x)`, `(s9d :contained s9x)` and `(s10d :contained s10x)`. The gold has `:overlap` in all three. The right parent was chosen each time, but the relation was wrong.
- **Purpose:** the annotator wrote `(s7x :after s7x12)` and `(s7x :after s7x17)`. The gold has `(s7x13 :overlap s7x8)` for 运用 and `(s7x13 :overlap s7x17)` for 容纳.
- **Reason:** the annotator wrote `(s7x :after s7x5)` for 改为. The gold has `(s7x13 :before s7x)`.
- **遗留下来:** the annotator wrote `(s7x12 :overlap s7x15)`. The gold has `(s7x8 :before s7x12)`, because the presses were left over before they were used.

**Why it happens.** The annotator followed the instruction exactly. Section 5.1 gives `(s1t :contained s1e)` as the model for a time expression, and it says "a purpose is `:after` its main event". Both rules are wrong for this gold. Nothing in the instruction covers reasons or relative participles.

**What to change.**
- Replace the date example with `(s6d :overlap s6x)`, and state the rule: "a date or period from the clause → `:overlap` its event".
- Replace the purpose rule with: "a purpose or reason clause → `:overlap` the main event, unless it is clearly earlier. In that case write `(main :before X)`."
- Add a rule for relative participles: "a participle describing an earlier state of a noun (遗留下来的, 留下的) → `(verb :before participle)`".

## 2. snt8 is anchored to the document creation time instead of the previous sentence's event (1 unit)

**The pattern.** For 黑白印刷也成了该刊的特色, the annotator wrote `(document-creation-time :before s8x)`. The gold has `(s7x13 :overlap s8x)`.

**Why it happens.** The instruction says: "Do not anchor it to an event of an earlier sentence unless a word (然后, 之后, 同时) marks that relation." Here 也 together with 成了 marks a result that continues the founding narrative of snt7.

**What to change.** Add 也 to the list of marker words. Also add: "a sentence describing the result or a feature of the event just narrated (成了…特色) → `(previous-main-event :overlap X)`".

## 3. The snt7 clause skeleton: :reason/:purpose roles instead of have-reason-91/have-purpose-91 (about 8 units)

**The pattern.** The sentence is built as 因为 X，为 Y，于是 Z. The annotator rooted it at 创立-01 and attached `:reason (改-01)`, `:purpose (运用-01)` and a second `:purpose (容纳-01)`. The gold is:
```
(s7h / have-reason-91
    :ARG1 (s7h2 / have-purpose-91 :ARG1 (创立-01 ...) :ARG2 (运用-01 ...) :aspect state)
    :ARG2 (改为-01 ...)
    :aspect state)
```
Each reified node also gets `(author :full-affirmative s7h)` and `(author :full-affirmative s7h2)`.

**What it cost.** have-reason-91 is missing, and so is its modal triple. have-purpose-91 was mismatched with have-org-role. d_core_args_abstract scored 0. There were also two extra peripheral units.

**Why it happens.** Section 2.5 maps 因为 to `:reason` and 为了 to `:purpose` only. Other gold Chinese sentences also reify 因为/由于…而 as have-reason-91 (for example 0005 snt12 and snt33).

**What to change.** Add: "When 因为/由于 … (于是/所以/而) or 为(了) … (于是) links whole clauses as the sentence's main structure, reify it.
- Reason: `have-reason-91` with `:ARG1` the result and `:ARG2` the cause.
- Purpose: `have-purpose-91` with `:ARG1` the main event and `:ARG2` the purpose.

Give both `:aspect state` and an author `full-affirmative` triple. Keep `:reason`/`:purpose` as roles only for phrase-level modifiers."

## 4. Invented re-entrancies and a misplaced relative clause (g_reentrancy P 20; about 6 more core and peripheral units)

**The pattern.**
- The annotator added `:possessor s7p` on 《国家询问报》 and `:ARG0 s7p` on 运用.
- It made the newspaper the `:ARG1` of 创立 and the `:ARG0` of 容纳.
- It attached 容纳 as a second `:purpose`.

In the gold, the object of 创立 is the black-and-white layout, and 容纳 is a relative clause on it:
```
:ARG1 (s7x14 / 版面 :mod (黑白)
        :part-of (s7n3 / newspaper :name ...)
        :ARG0-of (s7x17 / 容纳-01 :ARG1 (文章 ...) :aspect process))
```
The same holds for 将由黑白版面改为彩色版面: the gold has `改为-01 :ARG1 (版面 :mod 黑白 :part-of 《国家询问报》) :ARG2 (版面 :mod 彩色)`. The annotator instead used `:ARG1 newspaper` and `:source 版面`.

**Why it happens.** The instruction already says "Do not copy a subject or owner into another clause unless a word refers to it", but the annotator did not follow it. The instruction does say that a version or part of a publication is `:part-of`, but it never extends this to 版面 when it is the head of an X版面的Y phrase. The annotator read 黑白版面的《世界新闻周报》 as a modifier on the name.

**What to change.**
- Add the example "黑白版面的《世界新闻周报》 → `(版面 :mod 黑白 :part-of newspaper)`, which is the object of the verb".
- Add: "a clause after ， that says what the created or changed thing does (容纳…文章) is `:ARG0-of` that thing, with `:aspect process`, not a `:purpose`."
- Repeat the no-invented-arguments rule in the checklist.

## 5. Role nouns and appositives in snt7 (about 6 units)

**The pattern.**
- **创始人:** the annotator wrote `person :ARG1-of (have-org-role-92 :ARG2 newspaper :ARG3 创始人)`. The gold is:
  ```
  individual-person :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance)))
  ```
  The gold also has `(s7x13 :overlap s7x23)` and an author triple for 创始-00.
- **旗下的八卦小报《国家询问报》:** the gold has `newspaper :ARG1-of (identity-91 :ARG2 (小报 :mod 旗下 :mod 八卦))`. The annotator wrote `:mod 小报` and dropped 旗下.

**Why it happens.** The instruction shows only `person` together with have-org-role-92. The Chinese gold consistently uses `individual-person` for named people and pronouns (0005 snt12 and snt33). Nothing in the instruction covers appositives.

**What to change.**
- "A named person or personal pronoun is `individual-person`."
- "A ‑人 agent noun (创始人, 创办人) is `人 :ARG0-of (verb-00/01)`. The verb is an event with its own aspect, temporal triple and modal triple."
- "An appositive common noun before a name (旗下的八卦小报《X》) → `name-entity :ARG1-of (identity-91 :ARG2 noun)`, keeping all of the noun's modifiers (旗下 included)."
- "Keep a verb compound as written (改为-01, not 改-01 with a `:source`)."

## 6. 发行量 and the target number of 达到/跌至 (snt9 and snt10: about 14 units)

**The pattern.** The annotator wrote `(达到-01 :ARG0 (发行量 :possessor newspaper) :ARG1 (份 :quant 1200000))`. The gold is:
```
(s9x / 达到-01
    :ARG0 (s9x2 / 量
        :quant-of (s9x3 / 发行-01 :ARG1 (s9n / newspaper ...))
        :ARG1-of (s9h / have-quant-91 :ARG2 1200000 :unit (s9x4 / 份))))
```
The same structure applies in snt10 to 跌至 8万3千份: no `:ARG3`, but `have-quant-91 :ARG2 83000 :unit 份`. In the gold, 发行-01 gets `(main :overlap 发行)` but no modal triple.

**Why it happens.** The instruction has no rule for X量 compounds built on a verb, or for the target value of a change-of-quantity verb. Note that other gold documents sometimes keep 销量 or 铸造量 whole, so this decomposition reflects this document's gold practice.

**What to change.** Add: "发行量 (a verb + 量 measure of the entity's activity) → `量 :quant-of (发行-01 :ARG1 entity)`. The value reached (达到/跌至/增至 N 份) → `量 :ARG1-of (have-quant-91 :ARG2 N :unit 份)`, not a numbered argument of the verb. The inner 发行-01 gets `(main :overlap 发行)`." Also correct the classifier rule: a number that goes into have-quant-91 takes `:unit`, without `:quant` on the unit.

## 7. Smaller items

- **Unwanted but-91 in snt10.** 不过 at the start of a sentence, linking it to the previous sentence: the gold has no but-91, and 跌-01 is the root. The instruction's "but-91 (2.5)" example caused this extra node. Restrict but-91 to contrasts between clauses inside one sentence.
- **1980年代.** The gold writes `:era 1980`, not `:decade`. Add this as an example.
- **黑白印刷.** In 黑白印刷 the colour word modifies a verb, so it is `:manner`, not `:mod`. Add: "a modifier of an event noun used as a verb (黑白印刷) → `:manner`."
- **Aspect.**
  - A purpose verb (为充分运用) is `activity`.
  - A relative clause describing what the created thing does (容纳) is `process`.
  - 遗留下来的 is `performance`. The 已经…的 → `state` rule does not cover it.

  Add these to the aspect section.

## What to keep

These parts of the instruction worked and should stay unchanged:
- Name tokens with the 《 》 title marks: f_name_tokens scored 100.
- The `刊 :mod 该` treatment of common nouns and the coreference chain rules: j_coref_chain scored 100.
- 已经 as `:mod`.
- Polarity on 不符合, together with the `full-negative` modal triple: c_polarity scored 100.
- Event senses: b_event_sense scored 100.
- `(document-creation-time :before date)` for absolute past dates.
- `performance` on narrated past events.
- Root plus author `full-affirmative` modal triples: i_modal F 90.