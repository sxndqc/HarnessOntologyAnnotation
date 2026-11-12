<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29176). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

# The current instruction
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

# The critique (training batch 4: chinese_umr-0001, sentences 16-20; AnCast++ comprehensive 77.3)
<critique>
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
</critique>

# Earlier edits
- batch 1, reflection 1 (10/10 edits applied): Fix temporal chaining (anchor one main event, chain others with :overlap, no parent for copular -91 predicates, relative time words depend on DCT); Chinese classifiers as :unit; adverbs as :mod nodes; Chinese name brackets, no wiki, :place/:medium; aspect cues (habitual institutional activity, 已经+stop = state, 被称为 = performance); :reason for 因为/由于/以…而; 不过/可是 → but-91; distribute modifiers over con -> AnCast++ comp 84.8 on the batch, kept
- batch 1, reflection 2 (9/9 edits applied): Fix the 目前 temporal rule and its wrong example; add copular-root anchoring and governing-event rules; restrain coreference; narrow the 已经+end-verb state cue; add role rules (:part-of for editions, ARG0 for intransitive -00 verbs, no borrowed subjects, identity-91 for event-noun heads); keep compound verbs whole, 历史上 as :temporal, no aspect on have-degree-91; modal triple for root abstract predicat -> AnCast++ comp 94.6 on the batch, kept
- batch 1, reflection 3 (9/9 edits applied): Fix 曾经 temporal handling and stative aspect with 过; no :polarity on 未经 and no performance for negated events; 停刊-01 not -00; :part-of only with an expressed whole; :aspect state on root abstract predicates; :depends-on for naming clauses; partial-affirmative for usual-procedure nominals under negation; update examples. -> AnCast++ comp 100.0 on the batch, kept
- batch 2, reflection 1 (13/13 edits applied): Fix date anchoring (DCT :before date, date :overlap event), reason/purpose temporal order, cross-sentence anchoring; add have-reason-91/have-purpose-91 for paired clause connectives; apposition with identity-91, 由X改为Y roles, part-of objects, role nouns, 量 measure nouns with have-quant-91, middle dot in names, :era for 年代, 该刊; stronger no-invented-arguments rule; Chinese PropBank role numbering for -> AnCast++ comp 95.7 on the batch, kept
- batch 2, reflection 2 (7/7 edits applied): Fix 由X改为Y with a topic subject (:part-of on X, no :ARG0) and the full-build-at-first-mention re-entrancy rule; V+量 inner verb gets no aspect/modal; purpose events are activity, habitual cue narrowed (relative clause of founded thing = process); named humans are individual-person in Chinese; update examples and checklist. -> AnCast++ comp 100.0 on the batch, kept
- batch 2, reflection 3 (2/2 edits applied): Resolve the contradictory re-entrancy rule: build a repeated entity in full at its first mention in the sentence's word order, even when that branch is written later in PENMAN (e.g. under have-reason-91 :ARG2); annotate the 改为 example accordingly. -> AnCast++ comp 98.9 on the batch, not kept (the best was 100.0)
- batch 3, reflection 1 (17/17 edits applied): Add rules for reported-content temporal/modal/:quote, contrast overlap, summary sentences anchored to DCT, 虽然…不过 but-91, 以X为目的, parenthetical slogans, consecutive for 后来, control-verb re-entrancy exception, connectives without modal, 有/如…等 :example lists, :frequency, 有-03 relationships, 指-02/算是-01, title-before-name, planet, 母公司 split, 前 :mod, aspect of nominal under 停止 and 生存; trim redundant exam -> AnCast++ comp 76.9 on the batch, kept
- batch 3, reflection 2 (26/26 edits applied): Freed space (shorter preamble/abridgement note, removed checklist and redundant examples), then fixed: org/publication pronouns reuse the entity variable and corefer to the named entity; 算是-01 roles, implicit-argument for 其中最, 可 = neutral-affirmative, summary sentences DCT :before, event nominal senses, no subset-of from 其中; role-noun + org name apposition, shortened name repeat as own node with i -> AnCast++ comp 97.5 on the batch, kept
- batch 3, reflection 3 (11/12 edits applied): Fix reported-content modal triples (only :quote nodes get author+speaker; nested events author only; 被指/据说 content events conceiver only), add slogan-verb :ARG0 re-entrancy exception, add explicit alignment cases for short repeats/母公司/外星人, update examples; free space by trimming preamble and redundant text. -> AnCast++ comp 96.5 on the batch, not kept (the best was 97.5)
- batch 4, reflection 1 (21/25 edits applied): Free space (drop sample graph, preamble, long type list, redundant examples); add rules for 「」 titles as publication names, named events with year, Chinese CPB adjectives as stative -01 verbs, general CPB roleset lookup (刊登/贴到 roles), fewer adverb nodes and 靠 as :reason, narrowed habitual cue, 为了-initial have-reason-91, nominal modifiers as :mod process, temporal chaining for coordinated/connectiv -> AnCast++ comp 77.3 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.