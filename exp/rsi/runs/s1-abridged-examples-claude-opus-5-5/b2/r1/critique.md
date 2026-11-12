I ranked the errors by how many judged units they cost. Most of the loss comes from three things: sentence 7, the temporal anchoring of dates, and the measure noun 发行量.

## 1. A complex causal–purpose sentence was parsed too freely (sentence 7, about 35 units)
**Checks hit:** a_event_found/concept, a_entity, d_core_args, d_peripheral, f_name_tokens, all of g_reentrancy (0/0), and the coreference chain that depends on it.

What went wrong:
- **Clause-linking predicates were missing.** The sentence has the shape 因为 X，为 Y，于是 Z. Gold uses abstract predicates for this. The annotator put `:reason` and `:purpose` on 创立.
  - Gold: `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state) :ARG2 改为 :aspect state)`.
- **Inferred arguments were invented, against §3** ("Do not add arguments…"). All of these are extra in gold:
  - `运用 :ARG0 s7p`
  - `小报 :possessor s7p` (旗下 was read as a possessor)
  - `容纳 :ARG0 newspaper`
  - `have-org-role-92 :ARG2 《世界新闻周报》`
- **The wrong head was chosen.** 创立了黑白版面的《世界新闻周报》 means the founder created the black-and-white layout of the paper.
  - Gold: `创立 :ARG1 (版面 :mod 黑白 :part-of (newspaper 《世界新闻周报》) :ARG0-of (容纳-01 …))`.
  - In gold, 容纳 modifies 版面. It is not a purpose of 创立.
- **由 X 改为 Y was mis-roled.** The annotator gave `:ARG1 小报 :source 黑白版面`. Gold: `改为 :ARG1 (版面 :mod 黑白 :part-of 《国家询问报》) :ARG2 (版面 :mod 彩色)`.
- **An apposition was not split.** For 旗下的八卦小报《国家询问报》 the annotator put the name on 小报. Gold: `(newspaper :name 《国家询问报》 :ARG1-of (identity-91 :ARG2 (小报 :mod 旗下 :mod 八卦)))`.
- **A role noun was not decomposed.** For 创始人 gold has `individual-person :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance)))`, with no `:ARG2`.
- **The middle dot was dropped from the name.** 格内洛索·波普 should be `:op1 "格内洛索" :op2 "·" :op3 "波普"`.

**Instruction changes:**
- Add to §2.5: "When the reason, purpose or result is a whole clause (因为…于是…, 为…而/于是…), use the abstract predicates `have-reason-91` (`:ARG1` result, `:ARG2` reason) and `have-purpose-91` (`:ARG1` main event, `:ARG2` purpose) as the root. Each takes `:aspect state` and gets `(author :full-affirmative …)`."
- Add: "由 X 改为/变为 Y: X is `:ARG1`, Y is `:ARG2`; no `:source`."
- Add: "In `<common noun> + 《name》` apposition, the named entity is the head, and the common noun is `:ARG1-of (identity-91 :ARG2 noun)`. 旗下 is `:mod (旗下)`, not a possessor."
- Add: "In *V 了 Adj-N 的 《Name》* the object is the head noun (版面), with `:part-of` the named entity."
- Add: "A role noun built from a verb (创始人) is `人 :ARG0-of (<verb>-00/-01)` under `have-org-role-91 :ARG3`. Do not add an organization the text does not give."
- Make the existing rule louder: "Never re-use a participant from elsewhere in the sentence as an unexpressed agent or possessor; each re-entrancy needs a pronoun or an overt word."
- In §2.2, keep separator punctuation (·) as its own `:opN`.

## 2. Temporal anchoring of dates and in-sentence relations (h_temporal F 19%, about 16 units)
- **Absolute dates.** In sentences 6, 9 and 10 the annotator followed the instruction: `(root :depends-on s6d) (s6d :contained s6c)`. Gold has `(document-creation-time :before s6d) (s6d :overlap s6x)`. That is 6 units, and the instruction's rule is the cause. The other gold documents I checked also anchor events with `document-creation-time :before`.
  - **Change:** "A past absolute date: `(document-creation-time :before <date>)`, and the event of its clause `(<date> :overlap <event>)`. Do not use `root :depends-on` or `:contained`."
- **Cause and purpose.** The annotator wrote `创立 :after 运用/容纳` and `创立 :overlap 改为`. Gold has `创立 :overlap 运用`, `创立 :overlap 容纳` and `(创立 :before 改为)`, and also `(运用 :before 遗留)`.
  - **Change:** "A reason event comes before its result (`result :before reason`). A purpose clause is `:overlap` its main event. Replace 'a purpose is `:after`'. A resultative participle such as 遗留下来 is `performance` and comes before the event that uses it."
- **Event nominals.** The 发行 inside 发行量 needs `(达到 :overlap 发行)`. It got no parent because it had no node (see 3).
- **Cross-sentence anchoring.** In sentence 8 (黑白印刷也成了该刊的特色), the annotator wrote `document-creation-time :before 成`. Gold anchors it to the previous sentence: `(s7x13 :overlap s8x)`.
  - **Change:** "A sentence with no time expression that continues the previous sentence's episode hangs from that sentence's main event."

## 3. Measure nouns and quantities: 发行量 and 120万份 (sentences 9–10, about 20 units)
The annotator made 发行量 an entity with a `:possessor`. For the number it used `(thing :quant 1200000 :unit 份)` as `:ARG2`/`:ARG4`. Gold:
```
(达到-01 :ARG0 (量 :quant-of (发行-01 :ARG1 (newspaper …))
                 :ARG1-of (have-quant-91 :ARG2 1200000 :unit (份))) :aspect performance)
```
Sentence 10 is the same, with `跌-01 :ARG0 (量 …)` and `have-quant-91 :ARG2 83000`.

**Change:** add to §2.2: "A V+量 compound (发行量, 产量, 销量) is `量 :quant-of (V-01 :ARG1 <possessor>)`. The amount it reaches is `量 :ARG1-of (have-quant-91 :ARG2 <number> :unit <classifier>)`. It is not a separate `:ARG` of 达到/跌, and not `thing :quant`." The rule should also say that the event inside 发行量 needs temporal and modal parents.

## 4. Chinese PropBank roles misread from English frames (about 8 units)
- **成, 达到, 跌.** PropBank gives `成-01` ARG0 = theme and ARG1 = end result. It gives `达到-01` and `跌-01` ARG0 = theme. The annotator used `成 :ARG1 印刷 :ARG2 特色` (English *become*), `达到 :ARG1 发行量` and `跌 :ARG1`.
  - **Change:** "Take the role numbers from the Chinese roleset, not from the English equivalent. For change-of-state and amount verbs (成, 达到, 跌, 增至), the theme is usually `:ARG0`. Look it up with propbank_lookup."
- **黑白印刷.** Gold has `印刷 :manner 黑白 :aspect habitual`. The annotator had `:mod` and `process`.
  - **Change:** "An adjective describing how an event-noun's action is done is `:manner`. A recurring production activity is `habitual` (extend the 发行/报导 rule to 印刷)."

## 5. Coreference (j_coref F 40%)
- Most of the chain loss comes from item 1. The `s7w` node matched gold's 《国家询问报》 node, so every link to 《世界新闻周报》 was counted wrong.
- `(s6c :same-event s7c)` (创刊 vs 创立) is extra. The two have different verbs and different objects (the paper vs. its layout).
  - **Change:** "Do not link events expressed by different verbs unless the text makes them clearly identical."

## 6. Modal
- Gold has `(author :full-affirmative 运用/容纳)`. The annotator had `(创立 :unspecified …)`.
  - **Change:** "A purpose that the text presents as realized (the paper was founded to take these articles, and it did) is `author :full-affirmative`."
- The new `have-reason-91` and `have-purpose-91` nodes also need author full-affirmative.

## 7. Smaller items
- **该刊.** Gold has `(刊 :mod 该)`, not `newspaper`. Change: "A demonstrative + abbreviated noun keeps the word as its concept." There are 2 such units.
- **1980年代.** Gold has `date-entity :era 1980`, not `:decade`.
- **Sentence-initial 不过.** Gold has no `but-91` in sentence 10; the root is `跌-01`. Change: "A sentence-initial 不过/但是 that links to the previous sentence is not annotated in the graph."

## What the instruction should keep
These rules worked:
- the named-entity format with 《 》 as `:op`s and no `:wiki`;
- `performance` on completed main events;
- `已经 → :mod`;
- `:polarity -` with `full-negative` on 符合;
- PropBank senses (100%);
- `state` on 符合;
- the 周报/该刊 coreference chain across sentences 8–10;
- document format (100%);
- the "no `:subset-of` within a sentence" and "chain to closest mention" rules.