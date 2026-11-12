<!-- system -->
You review UMR annotations made with an instruction, and say what in the instruction should change.
<!-- user -->
An annotator (a model) annotated the sentences below in Uniform Meaning Representation (UMR), following the instruction below. A judge (umrjudge) then compared its annotation with the expert gold annotation, check by check (concepts, senses, roles, attributes, named entities, reentrancy, and the document-level temporal, modal and coreference relations).

Your task: find the error patterns that cost the most, explain why they happen given the instruction (a rule that is missing, unclear, wrong, or not followed), and say what to change in the instruction to fix them so that they do not recur on other documents. Order them by cost, most costly first. Say also what the annotator got right that the instruction should keep. For each problem give one or two concrete examples from these sentences: the words, what the annotation had, and the correct annotation fragment.

You may use the tools to check the guidelines (search_guidelines), PropBank (propbank_lookup) and how other gold annotations do a case (search_annotations).

# The instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.



## Guidelines

# UMR guidelines, abridged



## 1. What a UMR is

A UMR has two levels.

- **Sentence level**: one rooted, directed graph per sentence in PENMAN notation, adapted from AMR:
  concepts (events, entities, abstract concepts), the relations between them (participant roles and
  non-participant roles) and attributes (aspect, polarity, mode, quantity, person and number, degree).
- **Document level**: three kinds of relations between the nodes of the sentence graphs, across sentences:
  **temporal** dependencies, **modal** dependencies, and **coreference**.



**Variables.** Every node of sentence N has a variable starting with `s` + N (`s3d`, `s3p`, `s3d2`), all
different within the document. A node that fills two roles is written once and then referred to by its
variable (re-entrancy).

## 2. Concepts

### 2.1 Events

An event is a process or a state that is **predicated**, or a process used to **refer or modify**:

- verbs used as predicates (`deny-01`, Chinese `拥有-01`);
- event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events, with their PropBank sense (活动-01);
- participles and relative-clause verbs (*the man who left*: `(p / person :ARG0-of (l / leave-11))`);
- predicated states: adjectives and nouns in predicate position (*he is tall*, 他很高) — through the
  abstract predicates of 2.3 when there is no lexical verb.

Not events: entity nouns, property words used as plain modifiers (*a tall man*: `:mod (t / tall)`),
auxiliaries and modal verbs (*will, can, must*; 会, 能, 可以, 应该 — they affect `:aspect` and modal
strength, they are not nodes), light verbs (*make a decision* → `decide-01`; 进行访问 → `访问-01`),
the copula (*be*, 是) — it becomes one of the abstract predicates.

**Chinese adjectives are verbs.** Look up every adjective, predicate or modifier: if CPB has it (荒唐, 荒谬, 可笑, 真实, 显著), it is `<word>-01` with `:ARG0` = the thing described, `:aspect state`, a temporal parent (`:overlap` its governing event) and `(author :full-affirmative …)`; as a modifier it is `:ARG0-of` (显著位置 → `(位置 :ARG0-of (显著-01 :aspect state))`). V+者 → `(者 :ARG0-of (V-00 :aspect state))`. `have-mod-91`/`:mod` only for words not in CPB (黑白, 八卦).

**Concept names.** An English event is its PropBank roleset (`deny-01`, `look-up-05`). A Chinese event is the
Chinese word as written with its Chinese PropBank sense (`拥有-01`, `执行-01`); a Chinese predicate that is not
in PropBank is `<word>-00` — look the verb up first; many verbs that look rare have a sense (停刊-01). Keep compound verbs whole (称为 → `称为-01`, not `称-01`). Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :wiki "Russia" :name (n / name :op1 "Russia"))`: an entity-type concept, an optional `:wiki`
(the Wikipedia title, or `-` when there is none), and `:name` with one `:opN` per word of the name.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. A middle dot in a transliterated name is its own `:opN` (格内洛索·波普 → `:op1 "格内洛索" :op2 "·" :op3 "波普"`).
In Chinese names keep the title brackets 《 》 as their own `:opN` (《世界新闻周报》 → `:op1 "《" :op2 "世界" ... :opN "》"`). Do not add `:wiki` in Chinese documents. A headline or article title in 「 」 (一篇「…」, 新闻「…」) is `(publication :name (name :op1 "「" … :opN "」"))`, one `:opN` per word, punctuation included, with `:quant 1 :unit (篇)` after 一篇; no inner events, no `:quote`, no modal or temporal triples; after a common noun: `(新闻 :ARG1-of (identity-91 :ARG2 (publication …)))`. A named event with a year (2000年总统大选) is `(event :name (name :op1 "2000" :op2 "年" :op3 "总统大选"))`, not a date-entity; a following 时 adds no node. A named institution is one name (美国参议院 → `(building :name (name :op1 "美国" :op2 "参议院"))`). A country or place name that modifies a noun (美国小报) is `:place`, not `:mod`. Do not corefer a repeated country name that is only such a modifier. In Chinese documents a named human is `individual-person`, not `person` (`(individual-person :name (name :op1 "格内洛索" :op2 "·" :op3 "波普"))`); keep `person` for pronouns and unnamed people. Types as in AMR (`country`, `city`, `organization`, `company`, `newspaper`, `publication`, `building`, `event`, `planet` (地球), ...).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
a classifier is kept as the unit too, including 个, 份, 款, 本 (一份小报 → `小报 :quant 1 :unit (份)`).
A V+量 compound (发行量, 产量, 销量) is `(量 :quant-of (V-01 :ARG1 <whose>))`; the inner V-01 gets **no** `:aspect` and **no** modal triple; it only gets the temporal triple `(<governing verb> :overlap V)`. The amount it reaches is `量 :ARG1-of (have-quant-91 :ARG2 <number> :unit (<classifier>))`, not a separate `:ARG` of 达到/跌 and not `thing :quant`. A decade (1980年代) is `date-entity :era 1980`.

### 2.3 Abstract predicates (non-verbal clauses)

| construction | concept | roles |
|---|---|---|
| X is Y (identity, equation) | `identity-91` | `:ARG1` X, `:ARG2` Y |
| X is Adj / X has property | `have-mod-91` | `:ARG1` theme, `:ARG2` property |
| X is in/at place | `have-place-91` | `:ARG1` theme, `:ARG2` place |
| X has Y (possession) | `have-91` | `:ARG1` possessor, `:ARG2` possessum |
| Y belongs to X | `belong-91` | `:ARG1` possessum, `:ARG2` possessor |
| there is X (in L) | `exist-91` | `:ARG1` location, `:ARG2` theme |
| X is a member of category Y | `have-role-91` | `:ARG1` X, `:ARG3` category |
| X holds title T in organization O | `have-org-role-92` | `:ARG1` X, `:ARG2` O, `:ARG3` T |
| X is the R (kin, friend) of Z | `have-rel-role-92` | `:ARG1` X, `:ARG2` Z, `:ARG3` R |
| X has quantity Q | `have-quant-91` | `:ARG1` X, `:ARG2` Q |
| cause, reason | `have-cause-91` / `:cause` | |

Role nouns are reified the same way: *the president of Russia* →
`(p / person :ARG1-of (h / have-org-role-92 :ARG2 (c / country ...) :ARG3 (p2 / president)))`;
*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.

When the text has a lexical verb that is in Chinese PropBank (属, 拥有), use that verb with its frame's roles instead of `belong-91` / `have-91`. Superlatives and comparatives (最, 更, *most, more*) use `(have-degree-91 :ARG1 X :ARG2 <property> :ARG3 (最))`, not `:degree`. `have-degree-91` gets no `:aspect`. A root `identity-91` / `have-*-91` (the sentence's main predicate) takes `:aspect state`; an `identity-91` inside a noun phrase (程序 :ARG0-of identity-91) takes none. A frame such as 历史上 / 在…上 is `:temporal (上 :op1 (历史))` on the noun, not an `:ARG4` of `have-degree-91`.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference. A 他们/它/其 standing for an organization or publication named in the same sentence is no new node: reuse its variable; a possessive 他们的 before an event noun adds no `:ARG0`. In a later sentence the pronoun is its own node, coreferred to the named entity, not to an earlier pronoun.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过, 可是) `but-91` when it links two clauses of the same sentence; a sentence-initial 不过/但是 that links to the previous sentence is not annotated (the root is the clause's verb);
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) and 以…而 → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) with no second connective → `:concession`; 虽然 X，不过/但是 Y → `(but-91 :ARG1 X :ARG2 Y)`. 后来/然后 linking two clauses → `(consecutive :op1 X :op2 Y)`, no node for 后来. 以 X 为目的 → `(identity-91 :ARG1 (目的 :purpose-of <event>) :ARG2 X)` (X a plain concept), not have-purpose-91. A parenthetical 'N：quote' → `(identity-91 :ARG1 N :ARG2 <content>)`, joined to its clause by `and`; a quoted slogan's identity-91 takes `:aspect state` and its inner event `:quote` that identity-91.
- When whole clauses are linked by paired connectives (因为 X，于是/所以 Z; 为 Y，于是 …), use abstract predicates as the root: `have-reason-91` (`:ARG1` result, `:ARG2` reason) and `have-purpose-91` (`:ARG1` main event, `:ARG2` purpose), nested when both occur: `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用) :ARG2 改为)`. Each takes `:aspect state`, no temporal parent, and `(author :full-affirmative …)`. 以…而 inside a clause stays `:reason`.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span. A fixed four-character idiom is one concept. A pair of coordinated nouns written together (奇闻轶事) is split: `(and :op1 (奇闻) :op2 (轶事))`.

## 3. Relations

**Participant roles** (Stage 1): the numbered roles of the predicate's roleset, `:ARG0` (agent, causer,
experiencer as initiator), `:ARG1` (patient, theme), `:ARG2`–`:ARG5` as the roleset defines them. Use the
inverse `:ARGn-of` for a relative clause or a participant nominal: 卖菜的人 → `(p / person :ARG0-of (m /
卖-01 :ARG1 (c / 菜)))`.

**Non-participant roles** (closed list, the frequent ones): `:mod` (property, demonstrative, typifying
modifier), `:possessor`, `:part` / `:part-of`, `:topic`, `:temporal` (time expression or event),
`:place`, `:direction`, `:path`, `:goal`, `:source`, `:start`, `:manner`, `:instrument`, `:cause`,
`:reason`, `:purpose`, `:condition`, `:concession`, `:duration`, `:frequency`, `:extent`, `:degree`,
`:quant`, `:unit`, `:ord`, `:range`, `:age`, `:medium`, `:companion`, `:beneficiary`, `:example`,
`:subset-of`, `:name`, `:wiki`, `:opN`, `:vocative`, `:polite`, `:other-role` (when none fits).

- Chinese adverbs are concepts, not only aspect cues. 已经, 都 and 其中 → `:mod (<word>)`; 也 only as the sole adverb of a simple clause; no node for 甚至, 还, 就, 仍 beside 继续, or 都 in 都以…为目的; 靠 X V → `V :reason X`, no 靠 node; 曾经 → `:temporal (曾经)`. A medium (电视, 网络) is `:medium`.
- A modifier shared by coordinated nouns goes on each conjunct by reentrancy, never on the `and` node.
- Do not add arguments (agents, possessors, organizations) that the text does not express. Never re-use a participant from elsewhere in the sentence as an unexpressed agent or possessor: every re-entrancy needs a pronoun or an overt word. Exception: the overt subject of a control or aspectual verb (继续, 停止, 开始, 想, 打算) is also `:ARG0` of the embedded event or nominal (它停止了它的发行 → 发行 `:ARG0` 它). 旗下 is `:mod (旗下)`, not a possessor. Do not fill the subject of a later clause with an entity from an earlier clause (…，不过仍继续发行网络版: 发行 has no `:ARG0`).
- An edition, version or part of a publication or organization (纸本, 网络版, 分部), or its content or article (内容, 一篇新闻), takes `:part-of` its whole, not `:possessor` — but only when the whole is written with it (《…》的纸本). A bare 网络版 gets no `:part-of`.
- For an intransitive Chinese verb such as 停刊-01 (or a `-00` verb not in PropBank), the sole participant is `:ARG0`.
- When an event noun names what the head noun is (查证程序: the procedure is the verification), use `(程序 :ARG0-of (identity-91 :ARG1 (查证-01)))`, not `:mod`.
- In 'X 是 … Y，以 … 而 V' the second predicate modifies Y: `Y :ARG1-of (V :reason ...)`. Do not add a coordinating `and`.
- Apposition `<common noun> + 《name》` (八卦小报《国家询问报》): the named entity is the head, and the common noun hangs from it by `:ARG1-of (identity-91 :ARG2 (<noun> :mod …))`. Likewise a role noun before an organization name (母公司美国媒体公司): `company` with the name `:ARG1-of (identity-91 :ARG2 (公司 :mod (母)))`.
- In V 了 Adj-N 的《Name》 the object is the head noun with `:part-of` the named entity (创立了黑白版面的《…》 → `创立 :ARG1 (版面 :mod (黑白) :part-of (newspaper …))`); a relative clause before it (容纳…的) modifies that noun.
- 由 X 改为/变为 Y: X is `:ARG1`, Y is `:ARG2`; no `:source`. In `<Whole> 由 X 改为 Y`, when X and Y are parts or features of the subject (版面, 颜色, 名称), 改为 has **no** `:ARG0`: the subject is `:part-of` on X (`改为 :ARG1 (版面 :part-of <newspaper> :mod (黑白)) :ARG2 (版面 :mod (彩色))`).
- Build a repeated entity in full (name, apposition, modifiers) at its first mention in the graph (first in reading order), and refer to it at later exact repeats in the same sentence by its bare variable (`:possessor s7n`). A shortened repeat (周报 after 《世界新闻周报》) is its own node `(周报)` with an in-sentence `:same-entity` triple. A sentence-initial date shared by both clauses of 不过/但 is `:temporal` of both main events.
- A role noun built from a verb (创始人) is `(person :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance))))`, with no `:ARG2` unless the organization is written with it.
- Take the sense and role numbers of every Chinese predicate from its CPB roleset, never from English (当-02 position holder; 当选 `:ARG0` electee; 刊登, 贴到, 登: `:ARG1` location, `:ARG2` thing published, no `:place`): for change-of-state and amount verbs (成-01, 达到-01, 跌-01, 增至) the theme is `:ARG0` (成-01 `:ARG0` theme, `:ARG1` result). Look it up.
- An adjective saying how an event noun's action is done is `:manner` (黑白印刷 → `印刷 :manner (黑白)`).
- '<noun> 有 A、B…等' and 如 A、B 等 → `<noun> :example (and :op1 A :op2 B :op3 (等))`; 有 is no event; 等 is always the last `:opN`. Nouns in such lists are entities (时间旅行 → `(旅行 :mod (时间))`). 重复/经常 → `:frequency`; 在 N 中 → `(中 :op1 N)` (出现 `:ARG1`); 大部分 → `:mod`.
- X 与 Y 有关系 → `(有-03 :ARG0 (and :op1 X :op2 Y) :ARG1 (关系 …))`, no `:companion`. 被指 → `指-02`. Look up the whole compound first (称为-01; 算是-01: `:ARG0` thing described, `:ARG1` what it counts as). 其中最 + Adj with no head noun → `implicit-argument :ARG1-of (have-degree-91 :ARG1 (Adj) :ARG2 (最) :ARG5 (其中))`, classifier (宗) as `:unit`.
- A common noun directly before a name (外星人 P'Lod) in running text is no apposition: `(外星人 :name (name …))`, no identity-91; in a 如 A、B 等 list each character is `individual-person` named with all its written words, descriptor included, and is not coreferred with the narrative mention. 母公司 → `(公司 :mod (母))`. 前 → `:mod (前)` on the role noun; 第一夫人 → `have-rel-role-91 :ARG3 (第一夫人 :place (country …))`.
- A demonstrative + abbreviated noun keeps the word as its concept (该刊 → `(刊 :mod (该))`, not `newspaper`).

Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. The
top node of reported or claimed content (宣称, 指, a slogan) **must** also carry `:quote <reporting event>`.

## 4. Attributes

### 4.1 Aspect (`:aspect`, on every event)

Use the coarse values:

| value | use for |
|---|---|
| `state` | states: non-verbal predicates (2.3), *be, have, know, want, like, believe*, 是, 有, 在, 知道, 喜欢, 认为 |
| `habitual` | an event that happens usually or repeatedly (*he walks to work*, 经常, 每天) |
| `activity` | an ongoing process with no evidence of an end (*is running*, 正在, 着; a present-tense process; most generic statements of what is done) |
| `endeavor` | a process that ended without reaching its result (*worked on it for a week*, stop doing) |
| `performance` | a process that ended and reached its result: completed past events (*denied*, *was arrested*, 了, 过) |
| `process` | an event nominal, or a process whose type cannot be told (*the meeting*, 探索 as a noun) |

Aspect cues: a publication's or institution's own recurring verbs (发行, 报导, 综合, 印刷) used as predicates are `habitual`, even with 了, unless one occasion or article is given (time clause, 一篇, one headline → `performance`); this cue does not extend to other verbs. A relative clause describing what a newly founded thing was designed to do (容纳…文章的版面) is `process`. A purpose event (为/为了 X, `have-purpose-91 :ARG2`, `:purpose`) is `activity`, not `performance`, even when it is modally full-affirmative. 已经 + 停止 or another end verb is `state` only inside a relative clause that describes an entity (已经停止发行的小报); as the main predicate, 已经 + an end verb (已经停刊) is `performance`. Passive naming (被称为) and a past claim (宣称) are `performance`. Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂. An event nominal that is the object of 停止/开始 (它的发行) is `process` (no habitual). 生存, 存在 → `state`; an ongoing activity noun (活动) → `activity`. A negated event (未, 没) never gets `performance`; use `process` when its type cannot be told.



### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2). Exception: 未经 X / 没有经过 X → `经-01` with no `:polarity`; the negation is only the modal triple `(author :full-negative 经)`.
- `:mode imperative` (commands, 请, 别), `:mode interrogative` (questions; the questioned argument is
  `amr-unknown`, a yes/no question gets `:polarity amr-unknown`), `:mode expressive` (interjections).
- `:degree` for intensifiers and downtoners (*very, too, most*; 很, 非常, 太, 最) as a concept:
  `:degree (v / very)`.
- `:quant` for numbers and quantifiers (`:quant 3`, `:quant (a / all)`).

## 5. Document level

The document-level annotation of sentence N is one graph `(sNs0 / sentence ...)` with up to three lists of
`(parent :relation child)` triples. The triples of sentence N have at least one node of sentence N; the
other end can be a node of an earlier sentence or a constant.

### 5.1 Temporal (`:temporal`)

A dependency structure: each event and each time expression gets **one reference time** as its parent, and
the relation says where the **child** is relative to the **parent**:

- `:before` (child before parent), `:after` (child after parent), `:overlap` (child and parent overlap),
  `:contained` (child inside parent), `:contains`, `:depends-on` (between time nodes).
- Constants: `document-creation-time`, `past-reference`, `present-reference`, `future-reference`, `root`.
- Time expressions first: a past absolute date (*1998*, 1980年代) is `(document-creation-time :before <date>)` (never `root :depends-on`); a relative one (*today, yesterday*,
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`; a vague one
  (*nowadays*) on `past-reference` / `present-reference` / `future-reference` (for 目前/现在 see the rule below).
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :overlap s1e)`, not `:contained`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent. A purpose event is `:overlap` its main event (`(创立 :overlap 运用)`). A reason comes before its result: `(<reason> :before <result>)` (因为 X，于是 Z → `(X :before Z)`). A resultative participle (遗留下来) comes before the event that uses it (`(运用 :before 遗留)`).
- A sentence with no time expression that continues the previous sentence's episode hangs its main event from that sentence's main event (`(s7x :overlap s8x)`); but a sentence that judges or sums up the earlier text (算是, 其中最…) is `(document-creation-time :before X)` in a past narrative.
- Reported content (宣称, 指, 说): its first event is `(<report> :overlap X)`; other content events and later clauses hang from X, not from the report. 后来 Y after X → `(X :after Y)`. A clause with 仍/继续 contrasting with a past event → `:overlap`, never `:after`.
- Anchor only the **main event** of a sentence to `document-creation-time` (or to a time expression of its clause). Attach every other event of the sentence to that main event or to a nearby event, usually `:overlap` (`:contained` if it lies inside it, `:before`/`:after` when the order is clear). Events inside relative clauses, modifiers and event nominals also need a parent, normally their governing event with `:overlap`. Leave no event without a temporal parent.
- Copular abstract predicates (`identity-91`, `have-mod-91`, `have-*-91`) normally get **no** temporal parent.
- A relative time word such as 目前 or 现在 is a `:temporal` node in the graph but gets **no** temporal parent of its own. Link the main event of its clause to `document-creation-time` with `:depends-on` (`(document-creation-time :depends-on <main event>)`), then chain the other events from that main event with `:overlap`.
- 曾经 and 已经 are graph nodes only: they get no temporal parent and no event hangs from them. A past event marked with 曾经 or 过 is `(document-creation-time :before <event>)`; chain the sentence's other events from it with `:overlap`.
- The main event of a naming or reputation clause (被称为, 被誉为) is `(document-creation-time :depends-on <event>)`, as with 目前.
- When the root is an abstract predicate (`identity-91`, `have-mod-91`), anchor to `document-creation-time` the first event inside it (usually a relative-clause event such as 发行) and hang every other event from that event: an end verb (停止) `:overlap`; a reputation or state holding within it (闻名) `:contained`; a co-occurring activity (报导) `:overlap`. Never anchor more than one event of a sentence to `document-creation-time`.
- An event that modifies a noun hangs from the event whose argument that noun is (查证 inside 程序, the argument of 经 → `(经 :overlap 查证)`), not from the sentence's first event.

### 5.2 Modal (`:modal`)

A dependency structure of conceivers and events: `(conceiver :strength event)`, starting with
`(root :modal author)` in every sentence that has events.

- Strength = the conceiver's certainty that the event happens or holds: `full-affirmative` (plain
  assertion, *will*), `partial-affirmative` (*probably, must, should*, 应该, 可能性大, 一定 as inference),
  `neutral-affirmative` (*may, might, perhaps, can*, 可能, 也许, 或许, desire/hope), `neutral-negative`,
  `partial-negative`, `full-negative` (negated: *not, never, deny*, 没, 不), `unspecified`.
- Every event the author asserts: `(author :full-affirmative s1e)`.
- 可/能/可以 before a predicate (可算是) make it `neutral-affirmative` from the author.
- The root abstract predicate (`identity-91`, `have-mod-91`, ...) of an asserted sentence also gets `(author :full-affirmative …)`, although it gets no temporal parent.
- Reported speech or thought: `(author :full-affirmative s9p)` for the speaker node, and each content event gets **both** `(author :full-affirmative X)` and `(s9p :full-affirmative X)`. The conceiver is the speaker's entity node, not the reporting verb; with no written speaker (被指) use the whole subject node of the first content event (the `and` if coordinated). The top content node (with `:quote`, even an abstract predicate) gets both `author` and conceiver triples.
- Connectives (`but-91`, `and`, `consecutive`) get no modal triple.
- An event under a modal or complement-taking predicate (*want, try, plan, decide, hope*, 想, 希望, 打算,
  决定, 需要): the predicate is asserted by the author, the complement has the predicate as parent with
  `unspecified` (or the strength the predicate implies): `(author :full-affirmative s3w)`
  `(s3w :unspecified s3g)`.
- A conceiver that is not in the text is `null-conceiver`. A purpose the text presents as realized (founded to hold such articles, and it did) is `(author :full-affirmative <purpose>)`, not `unspecified` under the main event. An event nominal naming a usual procedure (一般的…程序) under a negated event is `(author :partial-affirmative <nominal>)`. Purpose and condition clauses may use the
  constants `purpose` and `have-condition` as parents of their events.
- In the sentence graph, write the strength of an event that is not `full-affirmative` from the author as
  `:modal-strength <value>` too (the scorers move it to the document level).

### 5.3 Coreference (`:coref`)

- `(earlier :same-entity later)`: two mentions of the same entity — a pronoun and its antecedent, a repeated
  name, a definite description. Link each mention to its closest earlier mention, earlier one first;
  link entity nodes, never `name` nodes.
- `(earlier :same-event later)`: two mentions of the same event.
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Within one sentence, coreference is a re-entrancy (one variable), except a shortened name repeat (see 3).
- Link two mentions only when they pick out the same individual or the same single event. Do not link two mentions of the same verb with different arguments, times or polarity (发行 of the print edition vs 发行 of the online edition). Do not link noun phrases with the same head but different restrictors (许多内容 vs 荒诞不经的内容). Never put a `:subset-of` triple inside one sentence or from a 其中 phrase. Do not link events expressed by different verbs (创刊 vs 创立) unless the text makes them clearly identical. When in doubt, leave the link out; chains like 周报 / 该周报 / 《…周报》 are what gold annotates.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.



## Examples

- Temporal chain (5.1): 目前…停刊，不过仍继续发行网络版 → `(document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`; 目前 has no temporal parent.
- Copular root (5.1): 是…已经停止发行的小报，以报导…而闻名 → `(document-creation-time :before 发行) (发行 :overlap 停止) (闻名 :contained 发行) (发行 :overlap 报导)`; modal `(author :full-affirmative identity-91)`.

- Aspect (4.1): main predicate 纸本已经停刊 → `(停刊-01 :ARG0 (纸本 …) :aspect performance)`; 继续发行网络版 → bare `(网络版)`, no `:part-of`.
- 曾经 + 过 (4.1, 5.1): 也曾经短暂的拥有过一个节目 → `(拥有-01 :temporal (曾经) :aspect state)`, `(document-creation-time :before 拥有) (拥有 :overlap …)`; 曾经 has no temporal parent.
- Negation (4.2): 都未经一般的新闻查证程序 → `(经-01 :mod (都) :aspect process)` without `:polarity`; modal `(author :full-negative 经) (author :partial-affirmative 查证)`.






- Clause links (2.5): 因为 X，为 Y，于是 Z → `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state) :ARG2 改为 :aspect state)`; temporal `(创立 :overlap 运用) (创立 :before 改为)`.

- 改为 (3): 小报《…》将由黑白版面改为彩色版面 …不符合《…》标准 → `(改为-01 :ARG1 (版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 …))) :mod (黑白)) :ARG2 (版面 :mod (彩色)))`, no `:ARG0`; later `(标准 :possessor s7n)`.

- Roles (3): 黑白印刷也成了该刊的特色 → `(成-01 :ARG0 (印刷-01 :manner (黑白) :aspect habitual) :ARG1 (特色 :poss… (刊 :mod (该))))`; temporal from previous sentence's main event.

- Aspect (4.1): 为充分运用… → `运用 :aspect activity`; 容纳…文章的版面 → `(版面 :ARG0-of (容纳-01 … :aspect process))`.



- 虽然…不过 (2.5): → `(but-91 :ARG1 (and :op1 宣称 :op2 (identity-91 :ARG1 标语 :ARG2 报导)) :ARG2 (identity-91 :ARG1 (目的 :purpose-of 报导) :ARG2 (博君一笑)))`; no modal triple on but-91/and.
- Quote (5.2): 宣称其报导都是真实的 → `(have-mod-91 :quote s12x …)`, `(author :full-affirmative have-mod-91) (s12n :full-affirmative have-mod-91)`, likewise each content 报导; slogan → `(identity-91 :aspect state)`.
- 被指 (5.1): 被指与X有暧昧关系，后来领养 → `(consecutive :op1 (有-03 :quote 指) :op2 (领养 :quote 指))`, `(指 :overlap 有) (有 :after 领养)`, conceiver = the `and` subject.


- Pronoun (2.4): 他们的报导…他们的标语 → `(报导-01 :aspect habitual)`, `(标语 :possessor s12n)`; next sentence 他们 → `(s12n :same-entity s13p)`.
- 算是 (3): 其中最大宗可算是…活动 → `(算是-01 :ARG0 (implicit-argument :ARG1-of (have-degree-91 :ARG1 (大) :ARG2 (最) :ARG5 (其中)) :unit (宗)) :ARG1 (活动-01 …))`, `(author :neutral-affirmative 算是) (document-creation-time :before 算是)`.

- Title (2.2): 刊登一篇「苏联复制…」 → `(刊登-01 :ARG2 (publication :name (name :op1 "「" :op2 "苏联" … "」") :quant 1 :unit (篇)))`, no events inside.
- Adjective (2.1): 内容虽然荒唐 → `(荒唐-01 :ARG0 (内容 :part-of 周报) :aspect state)`.
- Report (5.1, 5.2): 指柯林顿1992年靠外星人背书当选 → `(当选-01 :ARG0 柯林顿 :reason (背书-00 :ARG0 外星人))`, `(指 :before 当选)`, `(刊 :full-affirmative 指) (author :full-affirmative 当选)`.

</instruction>

# The sentences
16	2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。
17	不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。
18	如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。
19	为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。
20	该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt16
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
Words: 2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。

# sentence level graph:
(s16a / and
    :op1 (s16b / 报导-01
        :ARG0 (s16k / 刊
            :mod (s16k2 / 该))
        :ARG1 (s16p / publication
            :name (s16n / name
                :op1 "「"
                :op2 "外星人"
                :op3 "支持"
                :op4 "布什"
                :op5 "当"
                :op6 "总统"
                :op7 "」"))
        :temporal (s16e / event
            :name (s16n2 / name
                :op1 "2000"
                :op2 "年"
                :op3 "总统大选"))
        :aspect performance)
    :op2 (s16z / 注销-01
        :ARG0 s16k
        :ARG1 (s16x / 照片
            :mod (s16h / 合成)
            :topic (s16w / 握手-01
                :ARG0 (s16s / 双方)
                :aspect performance))
        :temporal s16e
        :aspect performance)
    :op3 (s16c / 指-02
        :ARG0 s16k
        :ARG1 (s16d / 当选-01
            :ARG0 (s16l / individual-person
                :name (s16n3 / name
                    :op1 "柯林顿"))
            :reason (s16y / 背书-00
                :ARG0 (s16w2 / 外星人)
                :aspect performance)
            :temporal (s16t / date-entity
                :year 1992)
            :mod (s16m / 也)
            :quote s16c
            :aspect performance)
        :temporal s16e
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16e)
               (s16e :overlap s16b)
               (s16b :overlap s16z)
               (s16b :overlap s16c)
               (s16z :before s16w)
               (document-creation-time :before s16t)
               (s16t :overlap s16d)
               (s16d :before s16y))
    :modal ((root :modal author)
            (author :full-affirmative s16b)
            (author :full-affirmative s16z)
            (author :full-affirmative s16w)
            (author :full-affirmative s16c)
            (s16k :full-affirmative s16c)
            (author :full-affirmative s16d)
            (s16k :full-affirmative s16d)
            (author :full-affirmative s16y)
            (s16k :full-affirmative s16y)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17a / but-91
    :ARG1 (s17h / 荒唐-01
        :ARG0 (s17c / 内容
            :part-of (s17z / 周报))
        :aspect state)
    :ARG2 (s17y / 有-01
        :ARG0 (s17b / 编辑
            :possessor s17z)
        :ARG1 (s17n / 能力
            :topic (s17d / 点出-00
                :ARG0 s17b
                :ARG1 (s17a2 / and
                    :op1 (s17h2 / 荒谬-01
                        :ARG0 (s17x / 新闻
                            :ARG0-of (s17r / 真实-01
                                :aspect state))
                        :aspect state)
                    :op2 (s17k / 可笑-01
                        :ARG0 s17x
                        :aspect state))
                :place (s17t / 标题)
                :modal-strength neutral-affirmative
                :aspect habitual))
        :mod (s17m / 也)
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17y)
               (s17y :overlap s17h)
               (s17y :overlap s17d)
               (s17d :overlap s17r)
               (s17d :overlap s17h2)
               (s17d :overlap s17k))
    :modal ((root :modal author)
            (author :full-affirmative s17h)
            (author :full-affirmative s17y)
            (author :neutral-affirmative s17d)
            (author :full-affirmative s17r)
            (author :full-affirmative s17h2)
            (author :full-affirmative s17k))
    :coref ((s16k :same-entity s17z)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18k / 刊登-01
    :ARG0 (s18t / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s18w / 位置
        :ARG0-of (s18x / 显著-01
            :aspect state))
    :ARG2 (s18p / publication
        :name (s18n / name
            :op1 "「"
            :op2 "苏联"
            :op3 "复制"
            :op4 "一万个"
            :op5 "希特勒"
            :op6 "」")
        :quant 1
        :unit (s18u / 篇))
    :temporal (s18z / 争论-01
        :ARG0 (s18q / 全世界)
        :ARG1 (s18r / 问题
            :mod (s18d / 道德)
            :topic (s18f / 复制人))
        :aspect activity)
    :aspect performance)


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18z)
               (s18z :overlap s18k)
               (s18k :overlap s18x))
    :modal ((root :modal author)
            (author :full-affirmative s18k)
            (author :full-affirmative s18z)
            (author :full-affirmative s18x))
    :coref ((s17z :same-entity s18t)))


################################################################################
# meta-info
# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。

# sentence level graph:
(s19b / 报导-01
    :ARG0 (s19p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s19q / publication
        :name (s19n / name
            :op1 "「"
            :op2 "美国"
            :op3 "买通"
            :op4 "外星人"
            :op5 "去"
            :op6 "追杀"
            :op7 "宾拉登"
            :op8 "」")
        :quant 1
        :unit (s19u / 篇))
    :purpose (s19f / 讽刺-01
        :ARG0 s19p
        :ARG1 (s19z / 政策
            :mod (s19w / 外交)
            :possessor (s19c / country
                :name (s19n2 / name
                    :op1 "美国")))
        :aspect activity)
    :mod (s19m / 也)
    :aspect performance)


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19b)
               (s19b :overlap s19f))
    :modal ((root :modal author)
            (author :full-affirmative s19b)
            (author :full-affirmative s19f))
    :coref ((s17z :same-entity s19p)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20t / 贴到-01
    :ARG0 (s20z / 者
        :ARG0-of (s20h / 好事-00
            :aspect state))
    :ARG1 (s20q / 墙
        :possessor (s20j / 记者团
            :possessor (s20b / building
                :name (s20n2 / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :ARG2 (s20x / 新闻
        :part-of (s20k / 刊
            :mod (s20k2 / 该))
        :quant 1
        :unit (s20u / 篇)
        :ARG1-of (s20i / identity-91
            :ARG2 (s20p / publication
                :name (s20n / name
                    :op1 "「"
                    :op2 "12"
                    :op3 "位"
                    :op4 "美国"
                    :op5 "参议员"
                    :op6 "是"
                    :op7 "外星人"
                    :op8 "！"
                    :op9 "」"))))
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20t)
               (s20t :overlap s20h))
    :modal ((root :modal author)
            (author :full-affirmative s20t)
            (author :full-affirmative s20h))
    :coref ((s19p :same-entity s20k)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt16
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
Words: 2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。

# sentence level graph:
(s16a / and
    :op1 (s16x / 报导-01
        :ARG0 (s16x4 / 刊
            :mod (s16x5 / 该))
        :ARG1 (s16x6 / 支持-01
            :ARG0 (s16x7 / 外星人)
            :ARG1 (s16x8 / 当-02
                :ARG0 (s16i2 / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16x9 / 总统))
            :aspect state)
        :quote s16x
        :temporal (s16e / event
            :name (s16n3 / name
                :op1 "2000"
                :op2 "年"
                :op3 "总统大选"))
        :aspect performance)
    :op2 (s16x2 / 注销-00
        :ARG0 s16x4
        :ARG1 (s16x10 / 照片
            :ARG1-of (s16x11 / 合成-01
                :aspect performance)
            :mod (s16x12 / 握手-01
                :ARG0 (s16x13 / 双方)
                :aspect process))
        :aspect performance)
    :op3 (s16x3 / 指-02
        :ARG0 s16x4
        :ARG1 (s16x14 / 当选-01
            :ARG0 (s16i3 / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :reason (s16x15 / 背书-00
                :ARG0 (s16x16 / 外星人)
                :aspect performance
                :quote s16x3)
            :temporal (s16d / date-entity
                :year 1992)
            :aspect performance
            :quote s16x3)
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16x)
               (s16x :overlap s16x6)
               (s16x6 :overlap s16x8)
               (s16x :overlap s16x2)
               (s16x2 :overlap s16x11)
               (s16x11 :overlap s16x12)
               (s16x2 :overlap s16x3)
               (s16x3 :before s16x14)
               (s16x14 :overlap s16x15))
    :modal ((root :modal author)
            (author :full-affirmative s16x6)
            (author :full-affirmative s16x4)
            (s16x4 :full-affirmative s16x)
            (author :full-affirmative s16x11)
            (author :full-affirmative s16x12)
            (s16x4 :full-affirmative s16x2)
            (author :full-affirmative s16x15)
            (author :full-affirmative s16x14)
            (s16x4 :full-affirmative s16x3)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17x / 荒唐-01
        :ARG0 (s17x3 / 内容
            :part-of (s17x4 / 周报))
        :aspect state)
    :ARG2 (s17x2 / 有-06
        :ARG0 (s17x5 / 编辑
            :possessor s17x4)
        :ARG1 (s17x6 / 能力
            :ARG1-of (s17i2 / identity-91
                :ARG2 (s17x7 / 点出-01
                    :ARG0 s17x5
                    :ARG1 (s17a / and
                        :op1 (s17x8 / 荒谬-01
                            :ARG0 (s17x10 / 新闻
                                :ARG0-of (s17x11 / 真实-01
                                    :aspect state))
                            :aspect state)
                        :op2 (s17x9 / 可笑-01
                            :ARG0 s17x10
                            :aspect state))
                    :place (s17x12 / 标题)
                    :aspect habitual)
                :aspect state))
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17x)
               (s17x :overlap s17x2)
               (s17x2 :overlap s17x7)
               (s17x7 :overlap s17x8)
               (s17x8 :overlap s17x11)
               (s17x7 :overlap s17x9))
    :modal ((root :modal author)
            (author :full-affirmative s17x)
            (author :full-affirmative s17x11)
            (author :full-affirmative s17x8)
            (author :full-affirmative s17x9)
            (author :neutral-affirmative s17x7)
            (author :full-affirmative s17i2)
            (author :full-affirmative s17x2))
    :coref ((s16x4 :same-entity s17x4)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18h / have-example-91
    :ARG1 (s18i2 / implicit-predicate)
    :ARG2 (s18x / 刊登-01
        :ARG0 (s18t / thing
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s18x2 / 位置
            :ARG0-of (s18x3 / 显著-01
                :aspect state))
        :ARG2 (s18p / publication
            :name (s18n / name
                :op1 "「"
                :op2 "苏联"
                :op3 "复制"
                :op4 "一万个"
                :op5 "希特勒"
                :op6 "」")
            :unit (s18x4 / 篇)
            :quant 1)
        :temporal (s18x5 / 争论-01
            :ARG0 (s18x6 / 世界
                :mod (s18x7 / 全))
            :ARG1 (s18x8 / 问题
                :mod (s18x9 / 道德)
                :topic (s18x10 / 人
                    :ARG1-of (s18x11 / 复制-01
                        :aspect process)))
            :aspect activity)
        :aspect performance))


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18x)
               (s18x :overlap s18x3)
               (s18x :overlap s18x5))
    :modal ((root :modal author)
            (author :full-affirmative s18x3)
            (author :full-affirmative s18x11)
            (author :full-affirmative s18x5)
            (author :full-affirmative s18x))
    :coref ((s17x4 :same-entity s18t)))


################################################################################
# meta-info
# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。

# sentence level graph:
(s19h / have-reason-91
    :ARG1 (s19x / 报导-01
        :ARG0 (s19p / person
            :refer-number plural
            :refer-person 3rd)
        :ARG1 (s19p2 / publication
            :name (s19n / name
                :op1 "「"
                :op2 "美国"
                :op3 "买通"
                :op4 "外星人"
                :op5 "去"
                :op6 "追杀"
                :op7 "宾拉登"
                :op8 "」")
            :unit (s19x7 / 篇)
            :quant 1)
        :mod (s19x3 / 也
            :unit (s19x4 / 篇)
            :quant 1)
        :aspect performance)
    :ARG2 (s19x2 / 讽刺-01
        :ARG0 s19p
        :ARG1 (s19x5 / 政策
            :topic (s19x6 / 外交)
            :possessor (s19c / country
                :name (s19n2 / name
                    :op1 "美国")))
        :aspect performance))


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19x)
               (s19x :overlap s19x2))
    :modal ((root :modal author)
            (author :full-affirmative s19x)
            (author :full-affirmative s19x2))
    :coref ((s17x4 :same-entity s19p)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20x / 贴到-01
    :ARG0 (s20x2 / 者
        :ARG0-of (s20x3 / 好事-00
            :aspect state))
    :ARG1 (s20x4 / 墙上
        :place-of (s20x5 / 记者团
            :place (s20b / building
                :name (s20n / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :ARG2 (s20x6 / 新闻
        :unit (s20x7 / 篇)
        :quant 1
        :part-of (s20x8 / 刊
            :mod (s20x9 / 该))
        :ARG1-of (s20i2 / identity-91
            :ARG2 (s20p / publication
                :name (s20n2 / name
                    :op1 "「"
                    :op2 "12"
                    :op3 "位"
                    :op4 "美国"
                    :op5 "参议员"
                    :op6 "是"
                    :op7 "外星人"
                    :op8 "！"
                    :op9 "」"))
            :aspect state))
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20x)
               (s20x :overlap s20x3))
    :modal ((root :modal author)
            (author :full-affirmative s20x3)
            (author :full-affirmative s20i2)
            (author :full-affirmative s20x))
    :coref ((s17x4 :same-entity s20x8)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 89 / P 100 / F 94
a_event_concept: R 88 / P 88 / F 88
a_entity_found: R 89 / P 100 / F 94
a_entity_concept: R 90 / P 90 / F 90
a_granularity: R 90 / P 96 / F 92
b_event_sense: R 81 / P 81 / F 81
c_aspect: R 74 / P 89 / F 81
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 80 / P 36 / F 50
d_core_args_event: R 86 / P 100 / F 93
d_core_args_abstract: R 50 / P 100 / F 67
d_peripheral_event: R 80 / P 67 / F 73
d_peripheral_entity: R 61 / P 61 / F 61
e_core_labels: R 97 / P 97 / F 97
e_peripheral_labels: R 83 / P 83 / F 83
f_name_tokens: R 100 / P 88 / F 93
g_reentrancy: R 78 / P 78 / F 78
h_temporal: R 41 / P 43 / F 42
i_modal: R 63 / P 82 / F 72
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_event_concept | wrong | s16x6: 支持 -> publication | 支持 -> publication
a_event_concept | wrong | s16x8: 当 -> 也 | 当 -> 也
a_entity_found | missing | s16i2: individual-person -> - | no node in the prediction matches it
a_entity_found | missing | s16x9: 总统 -> - | no node in the prediction matches it
a_entity_concept | wrong | s16x7: 外星人 -> name | 外星人 -> name
a_granularity | missing | «外星人» 外星人/外星人: «外星人» 外星人/外星人 -> «「外星人支持布什当总统」» publication | inside a wider predicted node
a_granularity | missing | «支持» 支持-01: «支持» 支持-01 -> «「外星人支持布什当总统」» publication | inside a wider predicted node
a_granularity | missing | «当» 当-02: «当» 当-02 -> «「外星人支持布什当总统」» publication | inside a wider predicted node
a_granularity | missing | «总统» 总统: «总统» 总统 -> «「外星人支持布什当总统」» publication | inside a wider predicted node
a_granularity | extra | «「外星人支持布什当总统」» publication: «外星人» 外星人/外星人; «支持» 支持-01; «当» 当-02; «总统» 总统 -> «「外星人支持布什当总统」» publication | one predicted node for 4 gold nodes
b_event_sense | wrong | s16x2: 注销 -> 注销-01 | 注销 -> 注销-01
b_event_sense | wrong | s16x11: 合成-01 -> 合成 | 合成-01 -> 合成
c_aspect | missing | s16x6:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s16x11:aspect: performance -> - | the prediction has no :aspect
c_aspect | wrong | s16x12:aspect: process -> performance | process -> performance
c_other_attributes | extra | s16x7:op1: - -> 「 | gold has no :op1
c_other_attributes | extra | s16x7:op2: - -> 外星人 | gold has no :op2
c_other_attributes | extra | s16x7:op3: - -> 支持 | gold has no :op3
c_other_attributes | extra | s16x7:op4: - -> 布什 | gold has no :op4
c_other_attributes | extra | s16x7:op5: - -> 当 | gold has no :op5
c_other_attributes | extra | s16x7:op6: - -> 总统 | gold has no :op6
c_other_attributes | extra | s16x7:op7: - -> 」 | gold has no :op7
d_core_args_event | missing | s16x6: arg0 s16x7/外星人; arg1 s16x8/当-02 -> - | missing arg0 s16x7/外星人; missing arg1 s16x8/当-02
d_core_args_event | missing | s16x8: arg0 s16i2/individual-person; arg1 s16x9/总统 -> - | missing arg0 s16i2/individual-person; missing arg1 s16x9/总统
d_core_args_event | missing | s16x11: arg1 s16x10/照片 -> - | missing arg1 s16x10/照片
d_peripheral_event | partial | s16x14: temporal s16d/date-entity -> mod s16x8/当-02; temporal s16d/date-entity | extra mod s16x8/当-02
d_peripheral_entity | wrong | s16x10: mod s16x12/握手-01 -> mod s16x11/合成-01; topic s16x12/握手-01 | mod s16x12/握手-01: predicted as topic; extra mod s16x11/合成-01
e_core_labels | wrong | s16x6 -arg0-> s16x7: arg0 -> name | arg0 -> name
e_peripheral_labels | wrong | s16x10 -mod-> s16x12: mod -> topic | mod -> topic
f_name_tokens | extra | s16x6: - -> 「 外星人 支持 布什 当 总统 」 | gold has no :name
g_reentrancy | missing | s16x/报导-01 -quote-> s16x/报导-01: s16x/报导-01 -quote-> s16x/报导-01 -> - | the prediction has no such edge
g_reentrancy | missing | s16x15/背书 -quote-> s16x3/指-02: s16x15/背书 -quote-> s16x3/指-02 -> - | the prediction has no such edge
g_reentrancy | extra | s16z/注销-01 -temporal-> s16e/event: - -> s16z/注销-01 -temporal-> s16e/event | gold has no such reentrancy
g_reentrancy | extra | s16c/指-02 -temporal-> s16e/event: - -> s16c/指-02 -temporal-> s16e/event | gold has no such reentrancy
a_event_concept | wrong | s17i2: identity -> 也 | identity -> 也
b_event_sense | wrong | s17x2: 有-06 -> 有-01 | 有-06 -> 有-01
b_event_sense | wrong | s17x7: 点出-01 -> 点出 | 点出-01 -> 点出
c_aspect | missing | s17i2:aspect: state -> - | the prediction has no :aspect
d_core_args_abstract | missing | s17i2: arg1 s17x6/能力; arg2 s17x7/点出-01 -> - | missing arg1 s17x6/能力; missing arg2 s17x7/点出-01
d_peripheral_event | extra | s17x2: - -> mod s17i2/identity-91 | extra mod s17i2/identity-91
d_peripheral_entity | extra | s17x6: - -> topic s17x7/点出-01 | extra topic s17x7/点出-01
a_event_found | missing | s18h: have-example-91 -> - | no node in the prediction matches it
a_event_found | missing | s18x11: 复制-01 -> - | no node in the prediction matches it
a_entity_found | missing | s18i2: implicit-predicate -> - | no node in the prediction matches it
a_entity_found | missing | s18x7: 全 -> - | no node in the prediction matches it
a_entity_concept | wrong | s18x6: 世界 -> 全世界 | 世界 -> 全世界
a_entity_concept | wrong | s18x10: 人 -> 复制人 | 人 -> 复制人
a_granularity | missing | «复制» 复制-01: «复制» 复制-01 -> «「苏联复制一万个希特勒」» publication | inside a wider predicted node
a_granularity | extra | «「苏联复制一万个希特勒」» publication: «复制» 复制-01 -> «「苏联复制一万个希特勒」» publication | wider than the gold node
d_peripheral_entity | missing | s18x6: mod s18x7/全 -> - | missing mod s18x7/全
a_event_found | missing | s19h: have-reason-91 -> - | no node in the prediction matches it
a_entity_found | missing | s19x4: 篇 -> - | no node in the prediction matches it
c_aspect | wrong | s19x2:aspect: performance -> activity | performance -> activity
c_other_attributes | missing | s19x3:quant: 1 -> - | the prediction has no :quant
d_peripheral_event | partial | s19x: mod s19x3/也 -> mod s19x3/也; purpose s19x2/讽刺-01 | extra purpose s19x2/讽刺-01
d_peripheral_entity | missing | s19x3: unit s19x4/篇 -> - | missing unit s19x4/篇
d_peripheral_entity | partial | s19x5: possessor s19c/country; topic s19x6/外交 -> mod s19x6/外交; possessor s19c/country | topic s19x6/外交: predicted as mod
e_peripheral_labels | wrong | s19x5 -topic-> s19x6: topic -> mod | topic -> mod
a_entity_concept | wrong | s20x4: 墙上 -> 墙 | 墙上 -> 墙
c_aspect | missing | s20i2:aspect: state -> - | the prediction has no :aspect
d_peripheral_entity | extra | s20x4: - -> possessor s20x5/记者团 | extra possessor s20x5/记者团
d_peripheral_entity | wrong | s20x5: place s20b/building; place s20x4/墙上 -> possessor s20b/building | place s20b/building: predicted as possessor; missing place s20x4/墙上
e_peripheral_labels | wrong | s20x5 -place-> s20b: place -> possessor | place -> possessor
h_temporal | extra | date-entity (snt16 s16d = pred s16t): - -> document-creation-time :before date-entity (snt16 s16d = pred s16t) | gold gives this node no temporal parent
h_temporal | extra | event (snt16 s16e = pred s16e): - -> document-creation-time :before event (snt16 s16e = pred s16e) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): document-creation-time :before 报导-01 «报导» (snt16 s16x = pred s16b) -> event (snt16 s16e = pred s16e) :overlap 报导-01 «报导» (snt16 s16x = pred s16b) | wrong parent and relation
h_temporal | missing | 合成-01 «合成» (snt16 s16x11 = pred s16h): 注销 «注销» (snt16 s16x2 = pred s16z) :overlap 合成-01 «合成» (snt16 s16x11 = pred s16h) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 握手-01 «握手» (snt16 s16x12 = pred s16w): 合成-01 «合成» (snt16 s16x11 = pred s16h) :overlap 握手-01 «握手» (snt16 s16x12 = pred s16w) -> 注销 «注销» (snt16 s16x2 = pred s16z) :before 握手-01 «握手» (snt16 s16x12 = pred s16w) | wrong parent and relation
h_temporal | wrong | 当选-01 «当选» (snt16 s16x14 = pred s16d): 指-02 «指» (snt16 s16x3 = pred s16c) :before 当选-01 «当选» (snt16 s16x14 = pred s16d) -> date-entity (snt16 s16d = pred s16t) :overlap 当选-01 «当选» (snt16 s16x14 = pred s16d) | wrong parent and relation
h_temporal | wrong | 背书 «背书» (snt16 s16x15 = pred s16y): 当选-01 «当选» (snt16 s16x14 = pred s16d) :overlap 背书 «背书» (snt16 s16x15 = pred s16y) -> 当选-01 «当选» (snt16 s16x14 = pred s16d) :before 背书 «背书» (snt16 s16x15 = pred s16y) | right parent, wrong relation
h_temporal | wrong | 指-02 «指» (snt16 s16x3 = pred s16c): 注销 «注销» (snt16 s16x2 = pred s16z) :overlap 指-02 «指» (snt16 s16x3 = pred s16c) -> 报导-01 «报导» (snt16 s16x = pred s16b) :overlap 指-02 «指» (snt16 s16x3 = pred s16c) | right relation, wrong parent
h_temporal | missing | 支持-01 «支持» (snt16 s16x6 = pred s16p): 报导-01 «报导» (snt16 s16x = pred s16b) :overlap 支持-01 «支持» (snt16 s16x6 = pred s16p) -> - | the prediction gives this node no temporal parent
h_temporal | missing | 当-02 «当» (snt16 s16x8 = pred s16m): 支持-01 «支持» (snt16 s16x6 = pred s16p) :overlap 当-02 «当» (snt16 s16x8 = pred s16m) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 荒唐-01 «荒唐» (snt17 s17x = pred s17h): document-creation-time :before 荒唐-01 «荒唐» (snt17 s17x = pred s17h) -> 有-06 «有» (snt17 s17x2 = pred s17y) :overlap 荒唐-01 «荒唐» (snt17 s17x = pred s17h) | wrong parent and relation
h_temporal | wrong | 真实-01 «真实» (snt17 s17x11 = pred s17r): 荒谬-01 «荒谬» (snt17 s17x8 = pred s17h2) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17r) -> 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17r) | right relation, wrong parent
h_temporal | wrong | 有-06 «有» (snt17 s17x2 = pred s17y): 荒唐-01 «荒唐» (snt17 s17x = pred s17h) :overlap 有-06 «有» (snt17 s17x2 = pred s17y) -> document-creation-time :before 有-06 «有» (snt17 s17x2 = pred s17y) | wrong parent and relation
h_temporal | wrong | 刊登-01 «刊登» (snt18 s18x = pred s18k): document-creation-time :before 刊登-01 «刊登» (snt18 s18x = pred s18k) -> 争论-01 «争论» (snt18 s18x5 = pred s18z) :overlap 刊登-01 «刊登» (snt18 s18x = pred s18k) | wrong parent and relation
h_temporal | wrong | 争论-01 «争论» (snt18 s18x5 = pred s18z): 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 争论-01 «争论» (snt18 s18x5 = pred s18z) -> document-creation-time :before 争论-01 «争论» (snt18 s18x5 = pred s18z) | wrong parent and relation
i_modal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) -> author :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) | right relation, wrong parent
i_modal | missing | 合成-01 «合成» (snt16 s16x11 = pred s16h): author :full-affirmative 合成-01 «合成» (snt16 s16x11 = pred s16h) -> - | the prediction gives this node no modal parent
i_modal | partial | 当选-01 «当选» (snt16 s16x14 = pred s16d): author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16d) -> author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16d); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16d) | agrees on part of the relations
i_modal | partial | 背书 «背书» (snt16 s16x15 = pred s16y): author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16y) -> author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16y); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16y) | agrees on part of the relations
i_modal | wrong | 注销 «注销» (snt16 s16x2 = pred s16z): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16z) -> author :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16z) | right relation, wrong parent
i_modal | partial | 指-02 «指» (snt16 s16x3 = pred s16c): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16c) -> author :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16c); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16c) | agrees on part of the relations
i_modal | missing | 刊 «该刊» (snt16 s16x4 = pred s16k): author :full-affirmative 刊 «该刊» (snt16 s16x4 = pred s16k) -> - | the prediction gives this node no modal parent
i_modal | missing | 支持-01 «支持» (snt16 s16x6 = pred s16p): author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16p) -> - | the prediction gives this node no modal parent
i_modal | missing | identity-91 (snt17 s17i2 = pred s17m): author :full-affirmative identity-91 (snt17 s17i2 = pred s17m) -> - | the prediction gives this node no modal parent
i_modal | missing | 复制-01 «复制» (snt18 s18x11): author :full-affirmative 复制-01 «复制» (snt18 s18x11) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | missing | identity-91 (snt20 s20i2 = pred s20i): author :full-affirmative identity-91 (snt20 s20i2 = pred s20i) -> - | the prediction gives this node no modal parent

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.