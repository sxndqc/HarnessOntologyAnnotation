# Review of the UMR annotation of sentences 16–20: costly error patterns and changes to the instruction

The structural checks scored well: refer attributes 100, the coreference chain 100, document format 100, core labels 97. The cost comes from five places:
- **One misapplied title rule** in sentence 16. It is the main cause of other_attributes P 36, name tokens, granularity, event concepts and core arguments.
- **Temporal anchoring** (h_temporal F 42), where the rules contradict each other.
- **Reported-speech modal and `:quote`.** The instruction's own rule text contradicts its example here.
- **Missing aspect, modal and arguments on `identity-91`.**
- **Senses that were never looked up.**

## 1. 「…」 directly after a reporting verb was annotated as a publication title (most costly)

**Cost.** This one decision cost about 25 units:
- 7 extra `:opN` (that is why other_attributes precision is 36);
- name_tokens 1 extra;
- granularity 5;
- event_concept 2, entity_found 2, entity_concept 1;
- core args 4 missing (支持 `:ARG0/:ARG1`, 当 `:ARG0/:ARG1`);
- aspect 1;
- temporal 2 missing (支持, 当);
- modal 1 missing (支持).

**What happened.** For 该刊报导「外星人支持布什当总统」 the annotator produced `报导-01 :ARG1 (publication :name (name :op1 "「" :op2 "外星人" … :op7 "」"))`.

The gold builds the clause:
```
:ARG1 (支持-01 :ARG0 (外星人) :ARG1 (当-02 :ARG0 (individual-person :name (name :op1 "布什")) :ARG1 (总统)) :aspect state)
```
with temporal `(报导 :overlap 支持) (支持 :overlap 当)` and modal `(author :full-affirmative 支持)`.

**Why.** Rule 2.2 says "A headline or article title in 「 」 … is `publication` … no inner events". Its triggers are only examples in parentheses (一篇「…」, 新闻「…」), so the annotator applied it to every 「」. The title rule is right where a counted article noun is present: sentences 18, 19 and 20 were all correct and should stay that way.

**Change.** Make the trigger explicit: 「…」 is a `publication` only when 一篇 / 篇 or an article noun (新闻, 文章, 标题) comes right before it. When 「…」 is the direct object of a reporting verb (报导, 说, 称, 指) with no such noun, it is reported content:
- annotate it as a clause, with full events and arguments;
- its events get `:aspect`, temporal parent `(<report> :overlap X)` and modal triples;
- its top event carries `:quote <report>`.

## 2. Temporal anchoring: time phrases, 时-clauses, report content and clause chains

**Cost.** About 14 temporal units (R 41 / P 43), plus 2 extra reentrancies.

**a. Named events and dates were used as reference times.**
- The annotator wrote `(document-creation-time :before s16e)` and `(s16e :overlap 报导)` for 2000年总统大选时, and `(DCT :before 1992) (1992 :overlap 当选)`.
- Gold gives the named event and the date **no** temporal parent, and has `(document-creation-time :before 报导)` and `(指 :before 当选)`.
- The instruction's own example already says `(指 :before 当选)`, but the general "time expression first" rule overrode it.

Change: "A named event used as a time phrase (`event :name …` + 时) is not a temporal node; anchor the main event to `document-creation-time`. In reported content, the report rule wins over a date inside the content: the date gets no parent, and the content event hangs from the report (`:before` when the content is earlier, as with 1992 vs 2000)."

**b. A 时-clause event was made the parent of the main event.**
- Sentence 18 (如全世界在争论…时，它…刊登): the annotator had `(DCT :before 争论) (争论 :overlap 刊登)`.
- Gold has `(DCT :before 刊登) (刊登 :overlap 争论)`.

Change: "The event of a 时 / 当…时 clause is the child: `(<main> :overlap <时-event>)`. Only the main event goes to `document-creation-time`."

**c. A shared time phrase was copied onto every conjunct of `and`.** The annotator put `:temporal s16e` on 注销 and 指 as well (2 extra reentrancies). The 不过/但 rule was over-applied. Change: "In `and`-coordination the time phrase stays on the first conjunct only."

**d. Each conjunct hangs from the preceding one, not from the first.**
- Gold has `(报导 :overlap 注销) (注销 :overlap 指)`; the annotator had 报导 → 指.
- Change: chain `:opN` from `:opN-1`.

**e. A 靠 / reason event got `:before`.**
- 靠外星人背书当选: the annotator had `(当选 :before 背书)`; gold has `(当选 :overlap 背书)`.
- Change: in "靠 X V", X is `:reason`, but temporally `(V :overlap X)`. The rule "a reason comes before its result" applies only to 因为/由于 clauses.

**f. Modifier events got the wrong relation or no parent.**
- 握手的合成照片: gold chains `(注销 :overlap 合成) (合成 :overlap 握手)`. The annotator had `(注销 :before 握手)` and gave 合成 no node at all.
- Sentence 17: 真实 modifies 新闻, which is the argument of 荒谬, so gold has `(荒谬 :overlap 真实)`. The annotator hung it from 点出.
- The existing rule ("hangs from the event whose argument that noun is") was not followed. Repeat it in the examples with 真实新闻的荒谬.

**g. With `but-91` the first clause was not anchored.**
- Sentence 17: gold has `(DCT :before 荒唐) (荒唐 :overlap 有)`; the annotator anchored 有.
- Change: "Under `but-91` / `contrast-91`, anchor the `:ARG1` clause's event and hang the `:ARG2` event from it with `:overlap`."

## 3. Reported speech: modal conceivers and `:quote`

**Cost.** 6 modal units, plus 2 reentrancy units (`:quote`).

**What happened.**
- In sentence 16 the annotator gave 报导, 注销 and 指 the parent `author`. Gold has `(s16x4/刊 :full-affirmative 报导 / 注销 / 指)` and `(author :full-affirmative 刊)`.
- It also added `(刊 :full-affirmative 当选)` and `(刊 :full-affirmative 背书)`. Gold gives the content events `author` only.

**Why.** Rule 5.2 says the content gets "both" author and speaker triples. The instruction's own example says the opposite: `(刊 :full-affirmative 指) (author :full-affirmative 当选)`. The annotator followed the rule text. It also skipped "`(author :full-affirmative s9p)` for the speaker node", which cost the missing 刊 unit.

**Change.** Rewrite 5.2 to match the example:
- `(author :full-affirmative <speaker>)`;
- `(<speaker> :full-affirmative <reporting event>)` for every event the speaker performs in that sentence (报导, 注销, 指);
- content events get `(author :full-affirmative X)`.

For `:quote`, gold puts it on every event of the content (当选 **and** 背书 `:quote 指`). Change "the top node … must carry `:quote`" to "every event of the reported content carries `:quote <report>`".

## 4. `identity-91` inside a noun phrase got no aspect, no modal triple, or was replaced by `:topic`

**Cost.** About 8 units: aspect 2, modal 2, core_args_abstract 2, event_concept 1, peripheral 1.

**What happened.**
- In sentence 20, 新闻 `:ARG1-of (identity-91 :ARG2 publication)` was correct but had no `:aspect`. Gold adds `:aspect state` and `(author :full-affirmative identity-91)`.
- In sentence 17 the annotator wrote 能力 `:topic` 点出. Gold has `(能力 :ARG1-of (identity-91 :ARG2 (点出-01 …) :aspect state))`, with `(author :full-affirmative identity-91)`.

**Why.** Rule 2.3 says that an `identity-91` inside a noun phrase "takes none", and 5.1/5.2 give the root `identity-91` a modal triple only. The annotator followed this rule, so the rule itself is too broad.

**Change.**
- An `identity-91` that equates a noun with a title or a content (新闻「…」, 能力 + V) takes `:aspect state` and `(author :full-affirmative …)`. It still gets no temporal parent.
- Keep "no aspect" only for the 程序 / 查证 kind.
- Add: "能力/资格 + V → `(能力 :ARG1-of (identity-91 :ARG2 V))`, not `:topic`."

## 5. Senses and modifier events: no PropBank lookup

**Cost.** event_sense 5, plus related aspect, modal and argument units, about 10 in total.

**What happened.**
- 点出: the annotator wrote `点出-00`, but CPB has `点出-01` (ARG0 agent, ARG1 theme).
- 有能力: the annotator wrote `有-01`. Gold has `有-06` ("ARG1 entity owned by / exist with respect to arg0").
- 合成照片: the annotator wrote `:mod (合成)`. Gold has `(照片 :ARG1-of (合成-01 :aspect performance))`, with `(注销 :overlap 合成)` and `(author :full-affirmative 合成)`. CPB has 合成-01.
- 握手的照片: the annotator wrote `:topic 握手 :aspect performance`. Gold has `:mod (握手-01 :aspect process)`.
- 注销: gold uses `注销-00`, because CPB 注销-01 ("cancel") does not fit the meaning "posted/published" here.

**Change.**
- Extend the "Chinese adjectives are verbs" rule to participial and verbal modifiers: a verb before 的 or a bare verb + N (合成照片) → `N :ARG1-of (V-01 :aspect performance)` when the noun is the result or patient.
- An event noun in 的 before a noun (握手的照片) → `:mod (V-01 :aspect process)`.
- Ability or possession of an abstract quality (有能力) → `有-06`.
- If the CPB sense does not match the meaning in context, use `-00`.
- Repeat the instruction "look up every predicate, including V+出/V+到 compounds".

## 6. Smaller patterns, each worth adding as one line

- **如 introducing an example sentence** (sentence 18, 3 units: event_found, entity_found, plus the missing 全 node). Add: `(have-example-91 :ARG1 (implicit-predicate) :ARG2 <main event>)` as the root.
- **全世界, 复制人.** Gold splits them: `(世界 :mod (全))`, and `(人 :ARG1-of (复制-01 :aspect process))` with `(author :full-affirmative 复制)`. Add: "a compound V+N noun where N is the patient (复制人) → `N :ARG1-of V`; 全+N → `N :mod (全)`."
- **Sentence-initial 为了 X，Y** (sentence 19). Gold uses `(have-reason-91 :ARG1 报导 :ARG2 讽刺)` with 讽刺 `:aspect performance`, not `:purpose` with `activity`. This contradicts the instruction's 为了 → `:purpose` / activity rule. It is one sentence, so treat it with caution. A clause-initial 为了 that fronts a whole clause could be handled like the paired-connective rule (an abstract-predicate root). If you adopt that, its aspect follows the realized event (`performance`), not `activity`.
- **外交政策.** Gold has `政策 :topic (外交)`, not `:mod`.
- **Locative noun with an institution name** (sentence 20, 美国参议院记者团的墙上). Gold has `(墙上 :place-of (记者团 :place (building …)))`. Keep the locative word whole (墙上). Extend "a country name modifying a noun is `:place`" to institution names, and do not use `:possessor` for them.

## What the annotator got right and the instruction should keep

- **Publication titles after 一篇** (sentences 18, 19, 20): `publication :name` with brackets as `:opN`, `:quant 1 :unit (篇)`. Also the 新闻 `:ARG1-of identity-91 :ARG2 publication` apposition.
- **The 该刊 → `(刊 :mod (该))` rule.**
- **`:part-of`** for 周报内容 and for 该刊的新闻.
- **Pronoun handling:** 它 → `thing`, 他们 → `person` plural. The coreference chain (each mention linked back to a 刊 / 周报 mention) scored 100.
- **`but-91` for 虽然…但.**
- **CPB adjectives as events:** 荒唐-01, 荒谬-01, 可笑-01, `显著-01 :ARG0-of`, 真实-01.
- **好事者** → `(者 :ARG0-of (好事-00 :aspect state))`.
- **指-02 / 当选-01 / 背书-00** with `:reason` (the 靠 rule), and the 1992 date-entity.
- **Modality:** `neutral-affirmative` for 点出 under 有能力.
- **Document format:** all correct.