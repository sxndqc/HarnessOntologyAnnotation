# What to change in the instruction, from the review of sentences 16–20

## Summary

Most of the lost points come from three things:
- The annotator parsed the quoted headlines 「…」 as events.
- It did not treat Chinese adjectives as stative verbs.
- It guessed rolesets instead of looking them up.

After those come four rules in the instruction that gold did not follow here: the habitual aspect for 报导, the `:mod` nodes for adverbs, the overlap rule for reported content, and the rule that every report has both an author and a speaker conceiver. Coreference (100), refer attributes (100), the doc format (100) and how fine-grained the concepts were (100) are already right.

---

## 1. Quoted article titles 「…」 parsed as clauses (most costly)

**Cost.** This hits most checks in sentences 18, 19 and 20:
- entity concepts: publication → individual-person / 追杀 / 外星人, and 篇 → country / name;
- name tokens: 3 names missing or wrong;
- `:quant`/`:unit`: 1 → 10000, and the 篇 unit missing twice;
- core arguments of 刊登, 报导 and 贴到;
- reentrancy: about 4 extra (`:quote`, 追杀 `:ARG0`);
- about 10 extra modal and temporal triples on content events that gold does not have.

**Examples.**
- 刊登一篇「苏联复制一万个希特勒」
  - Annotation: `:ARG1 (复制-01 :ARG0 (country 苏联) :ARG1 (individual-person 希特勒 :quant 10000) :quote s18k)`.
  - Gold: `:ARG2 (publication :name (name :op1 "「" :op2 "苏联" :op3 "复制" :op4 "一万个" :op5 "希特勒" :op6 "」") :quant 1 :unit (篇))`.
- 一篇新闻「12位美国参议员是外星人！」
  - Annotation: `新闻 :topic (identity-91 :ARG1 参议员 :ARG2 外星人)`.
  - Gold: `(新闻 :quant 1 :unit (篇) :ARG1-of (identity-91 :ARG2 (publication :name (name :op1 "「" … :op8 "！" :op9 "」"))))`.

**Why it happens.** The instruction only covers 《》 titles, and its rule on reported speech ("top node … must carry `:quote`", "each content event gets both author and conceiver triples") pushes the annotator to break every quote down into events.

**Change.** Add this to 2.2:
> A quoted headline or article title in 「 」 that names a piece of writing (after 一篇/篇, or in apposition to 新闻/文章) is `(publication :name (name :op1 "「" … :opN "」"))`, with one `:opN` per word, brackets and punctuation included. Put `:quant 1 :unit (篇)` on it. It has no inner events, no `:quote`, and no modal or temporal triples. When a common noun stands before it (新闻「…」), use `(新闻 :ARG1-of (identity-91 :ARG2 (publication …)))`.

Then limit the `:quote` and double-conceiver rule to the content of real reporting verbs (宣称, 指, 说, and 报导 + a clause with no 篇).

## 2. Chinese adjectives turned into `have-mod-91` or `:mod` instead of stative verbs

**Cost.**
- event senses: 荒唐, 荒谬, 可笑, 真实, 显著, 好事 — 6 wrong;
- aspect: 6 missing;
- core arguments: `:ARG0` missing on 荒唐, 荒谬, 可笑, 真实 and 好事;
- `d_core_args_abstract` (F 10): the made-up `have-mod-91`;
- about 8 missing temporal triples and about 6 missing modal triples.

**Examples.**
- 周报内容虽然荒唐
  - Annotation: `(have-mod-91 :ARG1 内容 :ARG2 (荒唐))`.
  - Gold: `(荒唐-01 :ARG0 (内容 :part-of 周报) :aspect state)`.
- 真实新闻的荒谬与可笑
  - Annotation: `(荒谬 :possessor (新闻 :mod (真实)))`.
  - Gold: `(荒谬-01 :ARG0 (新闻 :ARG0-of (真实-01 :aspect state)) :aspect state)`, and 可笑-01 the same way.
- 显著位置
  - Gold: `(位置 :ARG0-of (显著-01 :aspect state))`.
- 好事者
  - Gold: `(者 :ARG0-of (好事-00 :aspect state))`.

**Why it happens.** Section 2.1 says adjectives in predicate position go "through the abstract predicates of 2.3", and "a tall man" → `:mod`. Both are English rules. In Chinese PropBank these words are verbs: 荒唐-01, 真实-01 and 显著-01 each have a single role, "ARG0: entity described".

**Change.** Add this to 2.1:
> In Chinese, look up every adjective, whether it is a predicate or a modifier. If it is in PropBank (荒唐, 真实, 显著, 可笑, 荒谬), it is an event `<word>-01` with `:ARG0` = the thing described, `:aspect state`, a temporal parent (`:overlap` its governing event) and `(author :full-affirmative …)`.
> - As a modifier it is `:ARG0-of`.
> - Keep `have-mod-91` and `:mod` for words that are not in PropBank, and for colour or style words already covered (黑白, 八卦).
> - A noun formed as V+者 is `(者 :ARG0-of (V-00))`.

## 3. Rolesets and role numbers guessed, not looked up

**Cost.** Senses and core labels:
- 当-01 should be 当-02 ("position holder");
- 有-01 should be 有-06;
- 当选 `:ARG1` should be `:ARG0` (electee);
- 刊登: the annotation has `:ARG1` = the content and `:place` 位置; in PropBank `ARG1` is the location and `ARG2` the entity published;
- 贴到: the annotation has `:ARG1` 新闻 and `:ARG2` 墙上; in PropBank `ARG1` is the place and `ARG2` the entity posted.

**Gold fragments.**
- `(刊登-01 :ARG0 它 :ARG1 (位置 …) :ARG2 (publication …))`
- `(贴到-01 :ARG0 者 :ARG1 (墙上 …) :ARG2 (新闻 …))`

**Why it happens.** The instruction gives the "look it up" rule only for change-of-state verbs, so the annotator copied English argument patterns.

**Change.** Make the rule general:
> For every Chinese predicate, take the sense and the role numbers from its CPB roleset. For publishing or posting verbs (刊登, 贴到, 登), `:ARG1` is the location (在 X / 到 X) and `:ARG2` is the thing published. Do not use `:place` for a numbered location argument.

## 4. Temporal structure of sentence 16 and of the copular/contrast root in sentence 17

**Cost.** h_temporal is at 45; about 12 triples are wrong.

**Errors and fixes.**
- **2000年总统大选时.** The annotation built `时 :op1 (总统大选 :temporal date-entity)` and anchored 报导 to that date. Gold has `(event :name (name :op1 "2000" :op2 "年" :op3 "总统大选"))` and `(document-creation-time :before 报导)`.
  - Rule: a named recurring event with a year (2000年总统大选, 1998年世界杯) is a named `event`, not a date-entity. The bare frame 时 adds no node.
- **Reported content that happened before the report.** 指 … 柯林顿1992年…当选: gold has `(指 :before 当选)`, and the annotation has `(1992 :overlap 当选)`.
  - Amend the rule "reported content → `:overlap`": when the content is clearly earlier than the report (an earlier year, 过), use `(report :before content)`. A date inside reported content gets no temporal parent of its own.
- **Coordinated clauses.** Gold chains each conjunct from the one before it: `(报导 :overlap 注销) (注销 :overlap 指)`. The annotation hung every conjunct from the first one.
  - Say this explicitly: for clauses joined by `and` or 还, chain each from the previous conjunct.
- **Past narrative.** In sentence 17 the annotation has `(document-creation-time :overlap 有)`. Gold has `(document-creation-time :before 荒唐) (荒唐 :overlap 有)`.
  - Under `but-91` or another connective root, anchor the first clause's event to `document-creation-time` (`:before` in a past narrative) and chain the second from it.
- **Completed events in modifiers.** 注销 → 合成 should be `:overlap`, not `:before`. Only a clear resultative participle gets `:before`.

## 5. Aspect rules that over-generalize

**Cost.** c_aspect is at 55; about 7 units.

**Errors and fixes.**
- **报导 marked habitual** (sentences 16 and 19) because of the rule "a publication's own recurring verbs … are habitual even with 了". Gold has `performance` for one specific report (2000年…报导「…」, 报导了一篇).
  - Restrict the rule: it is habitual only when no single occasion or single article is given. With a time clause, 一篇, or one specific headline, the verb is `performance`.
- **讽刺 marked activity** under the rule "purpose = activity". Gold has `performance` here. Its root is `(have-reason-91 :ARG1 报导 :ARG2 讽刺)`, with no `:aspect`, and it gets no temporal or modal triple. The `:purpose` choice also cost the concept and the abstract arguments.
  - Add: a sentence-initial 为了 X，Y about an act that was done is `have-reason-91` (`:ARG1` Y, `:ARG2` X), and X takes Y's aspect.
- **Event nominal modifying a noun.** 握手的合成照片 should be `(照片 :mod (握手-01 :aspect process))`, not `:topic` and not performance.
  - Add: an event nominal that modifies a noun is `:mod` with `process`.
- **复制人** should be `(人 :ARG1-of (复制-01 :aspect process))`, not a single entity 复制人.
- **点出 under 有能力** is `habitual` (a general ability), not `activity`. 当 inside a complement (支持 X 当总统) gets no aspect.

## 6. Extra adverb and light-verb nodes

**Cost.** Entity_found precision went down because of 还, 也 ×2, 甚至 ×2 and 靠-01, plus extra peripheral edges, the 靠 reentrancy, and the temporal and modal triples on 靠.

**Why it happens.** Section 3 tells the annotator to make 也, 还 and 甚至 into `:mod` nodes. Gold has no node for 甚至 (sentences 16 and 20), for additive 还 (sentence 16), or for 也 (sentences 16 and 17). It kept 也 only in sentence 19.

**Change.**
- Remove 甚至 and additive 还 (还 + V = "also") from the `:mod` list. Keep 已经, 都 and 其中, and make 也 a node only when it is the sole adverb of a simple clause.
- Add: 靠 X (V) means "by virtue of X". It is `V :reason X`, with no 靠 node. Gold here: `(当选-01 :ARG0 柯林顿 :reason (背书-00 :ARG0 外星人) :temporal 1992)`.

## 7. Modal conceivers for reports

**Cost.** i_modal is at 53.
- Gold makes the publication the conceiver of its own acts: `(s16x4 :full-affirmative 报导/注销/指)`. Their content events get only `(author :full-affirmative …)`.
- The annotation gave author → 报导 and added a second, 刊 conceiver triple to each content event.
- It also gave `(author :full-affirmative <entity>)` to pronoun and publication nodes in sentences 18, 19 and 20, which have no reported content (or whose content is now a publication name).

**Change.** Add:
> When a publication or person is the subject of a reporting act, write `(author :full-affirmative <subject>)` and `(<subject> :full-affirmative <reporting event>)`. Give content events only the author triple.
>
> Add an `(author :full-affirmative <entity>)` triple only when that entity is a conceiver of some event.

## 8. Smaller structural rules

- **Content and articles of a publication are `:part-of` it.** 周报内容 → `(内容 :part-of 周报)` and 该刊的一篇新闻 → `(新闻 :part-of (刊 :mod 该))`, not `:possessor`. Extend the 纸本/网络版 rule to these.
- **A named institution is one name.** 美国参议院 is `(building :name (name :op1 "美国" :op2 "参议院"))`, not country + `:place`. 记者团 attaches to it with `:place`, and 墙上 relates to 记者团 with `:place-of`.
- **A noun whose content is an event.** 有能力点出… → `(能力 :ARG1-of (identity-91 :ARG2 (点出-01 …) :aspect state))`, like the 查证程序 rule, not `:topic`.
- **Sentence-initial 如 ("for example").** It is `(have-example-91 :ARG1 (implicit-predicate) :ARG2 <main event>)`.
- **外交政策.** It is `(政策 :topic (外交))`.

## What the instruction should keep

- Pronoun nodes with refer-person and refer-number, and coreferring each later pronoun to the publication (chain F 100).
- `该刊 → (刊 :mod (该))`.
- Chinese named people as `individual-person`.
- Every event of each sentence found (event_found 98), and granularity at 100.
- `(author :neutral-affirmative 点出)` for an event under 有能力.
- `争论 :aspect activity` under 在…时.
- Anchoring past main events with `document-creation-time :before`.