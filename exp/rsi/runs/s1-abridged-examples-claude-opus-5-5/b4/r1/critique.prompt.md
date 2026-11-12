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

**Make the annotation as correct as you can**: it is compared node by node and relation by relation with an expert gold annotation. Check every decision against the guidelines, follow the examples, and check each graph (concepts, aspect, role direction, document-level coverage) before moving on.

## Guidelines

# UMR guidelines, abridged

UMR 0.9 abridged, for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data.

## 1. What a UMR is

A UMR has two levels.

- **Sentence level**: one rooted, directed graph per sentence in PENMAN notation, adapted from AMR:
  concepts (events, entities, abstract concepts), the relations between them (participant roles and
  non-participant roles) and attributes (aspect, polarity, mode, quantity, person and number, degree).
- **Document level**: three kinds of relations between the nodes of the sentence graphs, across sentences:
  **temporal** dependencies, **modal** dependencies, and **coreference**.

```
He denied any wrongdoing.

(s3d / deny-01
    :ARG0 (s3p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s3d2 / do-02
        :ARG0 s3p
        :ARG1 (s3t / thing
            :mod (s3a / any)
            :ARG1-of (s3w / wrong-02))
        :aspect process)
    :aspect performance)

(s3s0 / sentence
    :temporal ((document-creation-time :before s3d)
               (s3d :before s3d2))
    :modal ((root :modal author)
            (author :full-affirmative s3p)
            (s3p :full-affirmative s3d)
            (s3d :unspecified s3d2))
    :coref ((s2p :same-entity s3p)))
```

**Variables.** Every node of sentence N has a variable starting with `s` + N (`s3d`, `s3p`, `s3d2`), all
different within the document. A node that fills two roles is written once and then referred to by its
variable (re-entrancy: `:ARG0 s3p` above).

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

**Concept names.** An English event is its PropBank roleset (`deny-01`, `look-up-05`). A Chinese event is the
Chinese word as written with its Chinese PropBank sense (`拥有-01`, `执行-01`); a Chinese predicate that is not
in PropBank is `<word>-00` — look the verb up first; many verbs that look rare have a sense (停刊-01). Keep compound verbs whole (称为 → `称为-01`, not `称-01`). Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :wiki "Russia" :name (n / name :op1 "Russia"))`: an entity-type concept, an optional `:wiki`
(the Wikipedia title, or `-` when there is none), and `:name` with one `:opN` per word of the name.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. A middle dot in a transliterated name is its own `:opN` (格内洛索·波普 → `:op1 "格内洛索" :op2 "·" :op3 "波普"`).
In Chinese names keep the title brackets 《 》 as their own `:opN` (《世界新闻周报》 → `:op1 "《" :op2 "世界" ... :opN "》"`). Do not add `:wiki` in Chinese documents. A country or place name that modifies a noun (美国小报) is `:place`, not `:mod`. Do not corefer a repeated country name that is only such a modifier. In Chinese documents a named human is `individual-person`, not `person` (`(individual-person :name (name :op1 "格内洛索" :op2 "·" :op3 "波普"))`); keep `person` for pronouns and unnamed people. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, `planet` (地球), ... (as in AMR).

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

- Chinese adverbs are concepts, not only aspect cues. 已经, 都, 也, 甚至, 还 and 其中 → `:mod (<word>)`, but no node for 就, for 还 after 后来, for 仍 beside 继续, or for 都 in 都以…为目的; 曾经 → `:temporal (曾经)`. A medium (电视, 网络) is `:medium`.
- A modifier shared by coordinated nouns goes on each conjunct by reentrancy, never on the `and` node.
- Do not add arguments (agents, possessors, organizations) that the text does not express. Never re-use a participant from elsewhere in the sentence as an unexpressed agent or possessor: every re-entrancy needs a pronoun or an overt word. Exception: the overt subject of a control or aspectual verb (继续, 停止, 开始, 想, 打算) is also `:ARG0` of the embedded event or nominal (它停止了它的发行 → 发行 `:ARG0` 它). 旗下 is `:mod (旗下)`, not a possessor. Do not fill the subject of a later clause with an entity from an earlier clause (…，不过仍继续发行网络版: 发行 has no `:ARG0`).
- An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor` — but only when the whole is written with it (《…》的纸本). A bare 网络版 gets no `:part-of`.
- For an intransitive Chinese verb such as 停刊-01 (or a `-00` verb not in PropBank), the sole participant is `:ARG0`.
- When an event noun names what the head noun is (查证程序: the procedure is the verification), use `(程序 :ARG0-of (identity-91 :ARG1 (查证-01)))`, not `:mod`.
- In 'X 是 … Y，以 … 而 V' the second predicate modifies Y: `Y :ARG1-of (V :reason ...)`. Do not add a coordinating `and`.
- Apposition `<common noun> + 《name》` (八卦小报《国家询问报》): the named entity is the head, and the common noun hangs from it by `:ARG1-of (identity-91 :ARG2 (<noun> :mod …))`. Likewise a role noun before an organization name (母公司美国媒体公司): `company` with the name `:ARG1-of (identity-91 :ARG2 (公司 :mod (母)))`.
- In V 了 Adj-N 的《Name》 the object is the head noun with `:part-of` the named entity (创立了黑白版面的《…》 → `创立 :ARG1 (版面 :mod (黑白) :part-of (newspaper …))`); a relative clause before it (容纳…的) modifies that noun.
- 由 X 改为/变为 Y: X is `:ARG1`, Y is `:ARG2`; no `:source`. In `<Whole> 由 X 改为 Y`, when X and Y are parts or features of the subject (版面, 颜色, 名称), 改为 has **no** `:ARG0`: the subject is `:part-of` on X (`改为 :ARG1 (版面 :part-of <newspaper> :mod (黑白)) :ARG2 (版面 :mod (彩色))`).
- Build a repeated entity in full (name, apposition, modifiers) at its first mention in the graph (first in reading order), and refer to it at later exact repeats in the same sentence by its bare variable (`:possessor s7n`). A shortened repeat (周报 after 《世界新闻周报》) is its own node `(周报)` with an in-sentence `:same-entity` triple. A sentence-initial date shared by both clauses of 不过/但 is `:temporal` of both main events.
- A role noun built from a verb (创始人) is `(person :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance))))`, with no `:ARG2` unless the organization is written with it.
- Take role numbers from the Chinese roleset, not from the English equivalent: for change-of-state and amount verbs (成-01, 达到-01, 跌-01, 增至) the theme is `:ARG0` (成-01 `:ARG0` theme, `:ARG1` result). Look it up.
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

Aspect cues: a publication's or institution's own recurring verbs (发行, 报导, 综合, 印刷) used as predicates are `habitual`, even with 了; this cue does not extend to other verbs. A relative clause describing what a newly founded thing was designed to do (容纳…文章的版面) is `process`. A purpose event (为/为了 X, `have-purpose-91 :ARG2`, `:purpose`) is `activity`, not `performance`, even when it is modally full-affirmative. 已经 + 停止 or another end verb is `state` only inside a relative clause that describes an entity (已经停止发行的小报); as the main predicate, 已经 + an end verb (已经停刊) is `performance`. Passive naming (被称为) and a past claim (宣称) are `performance`. Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂. An event nominal that is the object of 停止/开始 (它的发行) is `process` (no habitual). 生存, 存在 → `state`; an ongoing activity noun (活动) → `activity`. A negated event (未, 没) never gets `performance`; use `process` when its type cannot be told.



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
- Degree (2.3): 美国历史上最…的报纸 → `(报纸 :temporal (上 :op1 (历史 :place (country …))))`, `have-degree-91` without aspect; 称为 → `称为-01`.


- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`.


- Clause links (2.5): 因为 X，为 Y，于是 Z → `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state) :ARG2 改为 :aspect state)`; temporal `(创立 :overlap 运用) (创立 :before 改为)`.
- Apposition (3): 旗下的八卦小报《国家询问报》 → `(newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 :mod (旗下) :mod (八卦))))`.
- 改为 (3): 小报《…》将由黑白版面改为彩色版面 …不符合《…》标准 → `(改为-01 :ARG1 (版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 …))) :mod (黑白)) :ARG2 (版面 :mod (彩色)))`, no `:ARG0`; later `(标准 :possessor s7n)`.
- Measure noun (2.2): 发行量达到120万份 → `(达到-01 :ARG0 (量 :quant-of (发行-01 :ARG1 …) :ARG1-of (have-quant-91 :ARG2 1200000 :unit (份))) :aspect performance)`, `(达到 :overlap 发行)`.
- Roles (3): 黑白印刷也成了该刊的特色 → `(成-01 :ARG0 (印刷-01 :manner (黑白) :aspect habitual) :ARG1 (特色 :poss… (刊 :mod (该))))`; temporal from previous sentence's main event.

- Aspect (4.1): 为充分运用… → `运用 :aspect activity`; 容纳…文章的版面 → `(版面 :ARG0-of (容纳-01 … :aspect process))`.
- Named person (2.2): 格内洛索·波普 → `(individual-person :name (name :op1 "格内洛索" :op2 "·" :op3 "波普"))`.

- Control (3): 网络版继续生存 → `(继续-01 :ARG0 s11n :ARG1 (生存-01 :ARG0 s11n :aspect state))`; temporal `(停止 :overlap 继续)`.
- 虽然…不过 (2.5): → `(but-91 :ARG1 (and :op1 宣称 :op2 (identity-91 :ARG1 标语 :ARG2 报导)) :ARG2 (identity-91 :ARG1 (目的 :purpose-of 报导) :ARG2 (博君一笑)))`; no modal triple on but-91/and.
- Quote (5.2): 宣称其报导都是真实的 → `(have-mod-91 :quote s12x …)`, `(author :full-affirmative have-mod-91) (s12n :full-affirmative have-mod-91)`, likewise each content 报导; slogan → `(identity-91 :aspect state)`.
- 被指 (5.1): 被指与X有暧昧关系，后来领养 → `(consecutive :op1 (有-03 :quote 指) :op2 (领养 :quote 指))`, `(指 :overlap 有) (有 :after 领养)`, conceiver = the `and` subject.
- List (3): 题材有A、B等 → `(题材 :example (and :op1 A :op2 B :op3 (等)))`; 重复出现 → `:frequency (重复)`.

- Pronoun (2.4): 他们的报导…他们的标语 → `(报导-01 :aspect habitual)`, `(标语 :possessor s12n)`; next sentence 他们 → `(s12n :same-entity s13p)`.
- 算是 (3): 其中最大宗可算是…活动 → `(算是-01 :ARG0 (implicit-argument :ARG1-of (have-degree-91 :ARG1 (大) :ARG2 (最) :ARG5 (其中)) :unit (宗)) :ARG1 (活动-01 …))`, `(author :neutral-affirmative 算是) (document-creation-time :before 算是)`.
- Apposition (3): 母公司美国媒体公司 → `(company :name … :ARG1-of (identity-91 :ARG2 (公司 :mod (母))))`; later 周报的网络版 → `(网络版 :part-of (s11x5 / 周报))` + `(s11n2 :same-entity s11x5)`.
- List names (3): 如蝙蝠男孩、外星人P'Lod等 → `(individual-person :name (name :op1 "蝙蝠" :op2 "男孩"))`, `(individual-person :name (name :op1 "外星人" :op2 "P" :op3 "'" :op4 "Lod"))`.

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
    :op1 (s16r / 报导-01
        :ARG0 (s16k / 刊
            :mod (s16g / 该))
        :ARG1 (s16z / 支持-01
            :ARG0 (s16w / 外星人)
            :ARG1 (s16d2 / 当-01
                :ARG0 (s16p / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16z2 / 总统)
                :aspect state)
            :quote s16r
            :aspect state)
        :temporal (s16s / 时
            :op1 (s16x / 总统大选
                :temporal (s16d / date-entity
                    :year 2000)))
        :aspect habitual)
    :op2 (s16c / 注销-01
        :ARG0 s16k
        :ARG1 (s16p2 / 照片
            :ARG1-of (s16h / 合成-01
                :aspect performance)
            :topic (s16w2 / 握手-01
                :ARG0 (s16f / 双方)
                :aspect performance))
        :mod (s16h2 / 还)
        :aspect performance)
    :op3 (s16i / 指-02
        :ARG0 s16k
        :ARG1 (s16e / 当选-01
            :ARG1 (s16p3 / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :manner (s16o / 靠-01
                :ARG0 s16p3
                :ARG1 (s16b / 背书-01
                    :ARG0 (s16w3 / 外星人)
                    :aspect performance)
                :aspect state)
            :temporal (s16d3 / date-entity
                :year 1992)
            :mod (s16y / 也)
            :quote s16i
            :aspect performance)
        :mod (s16s2 / 甚至)
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16d)
               (s16d :overlap s16r)
               (s16r :overlap s16z)
               (s16z :overlap s16d2)
               (s16r :overlap s16c)
               (s16c :before s16h)
               (s16h :overlap s16w2)
               (s16r :overlap s16i)
               (document-creation-time :before s16d3)
               (s16d3 :overlap s16e)
               (s16e :overlap s16o)
               (s16o :overlap s16b))
    :modal ((root :modal author)
            (author :full-affirmative s16r)
            (author :full-affirmative s16c)
            (author :full-affirmative s16i)
            (author :full-affirmative s16h)
            (author :full-affirmative s16w2)
            (author :full-affirmative s16k)
            (author :full-affirmative s16z)
            (s16k :full-affirmative s16z)
            (author :full-affirmative s16d2)
            (s16k :full-affirmative s16d2)
            (author :full-affirmative s16e)
            (s16k :full-affirmative s16e)
            (author :full-affirmative s16o)
            (s16k :full-affirmative s16o)
            (author :full-affirmative s16b)
            (s16k :full-affirmative s16b)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17h / have-mod-91
        :ARG1 (s17c / 内容
            :possessor (s17x / 周报))
        :ARG2 (s17t / 荒唐)
        :aspect state)
    :ARG2 (s17y / 有-01
        :ARG0 (s17e / 编辑
            :possessor s17x)
        :ARG1 (s17n / 能力
            :topic (s17d / 点出-01
                :ARG0 s17e
                :ARG1 (s17a / and
                    :op1 (s17m / 荒谬
                        :possessor (s17w / 新闻
                            :mod (s17z / 真实)))
                    :op2 (s17k / 可笑
                        :possessor s17w))
                :place (s17l / 标题)
                :modal-strength neutral-affirmative
                :aspect activity))
        :mod (s17g / 也)
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :overlap s17y)
               (s17y :overlap s17d))
    :modal ((root :modal author)
            (author :full-affirmative s17h)
            (author :full-affirmative s17y)
            (s17y :neutral-affirmative s17d))
    :coref ((s16k :same-entity s17x)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18k / 刊登-01
    :ARG0 (s18p / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s18f / 复制-01
        :ARG0 (s18c / country
            :name (s18n / name
                :op1 "苏联"))
        :ARG1 (s18h / individual-person
            :name (s18n2 / name
                :op1 "希特勒")
            :quant 10000
            :unit (s18g / 个))
        :quote s18k
        :aspect performance)
    :place (s18w / 位置
        :mod (s18x / 显著))
    :temporal (s18s / 时
        :op1 (s18z / 争论-01
            :ARG0 (s18j / 世界
                :mod (s18q / 全))
            :ARG1 (s18e / 问题
                :mod (s18d / 道德)
                :topic (s18r / 复制人))
            :aspect activity))
    :aspect performance)


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18k)
               (s18k :overlap s18z)
               (s18k :overlap s18f))
    :modal ((root :modal author)
            (author :full-affirmative s18k)
            (author :full-affirmative s18z)
            (author :full-affirmative s18p)
            (author :full-affirmative s18f)
            (s18p :full-affirmative s18f))
    :coref ((s17x :same-entity s18p)))


################################################################################
# meta-info
# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。

# sentence level graph:
(s19r / 报导-01
    :ARG0 (s19p / person
        :refer-person 3rd
        :refer-number plural)
    :ARG1 (s19m / 买通-01
        :ARG0 (s19c / country
            :name (s19n / name
                :op1 "美国"))
        :ARG1 (s19w / 外星人)
        :purpose (s19z / 追杀-01
            :ARG0 s19w
            :ARG1 (s19b / individual-person
                :name (s19n2 / name
                    :op1 "宾拉登"))
            :aspect activity)
        :quote s19r
        :aspect performance)
    :purpose (s19f / 讽刺-01
        :ARG0 s19p
        :ARG1 (s19e / 政策
            :mod (s19d / 外交)
            :possessor s19c)
        :aspect activity)
    :mod (s19y / 也)
    :aspect habitual)


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19r)
               (s19r :overlap s19f)
               (s19r :overlap s19m)
               (s19m :overlap s19z))
    :modal ((root :modal author)
            (author :full-affirmative s19r)
            (author :full-affirmative s19f)
            (author :full-affirmative s19p)
            (author :full-affirmative s19m)
            (s19p :full-affirmative s19m)
            (author :full-affirmative s19z)
            (s19p :full-affirmative s19z))
    :coref ((s18p :same-entity s19p)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20t / 贴到-01
    :ARG0 (s20h / 好事者)
    :ARG1 (s20x / 新闻
        :quant 1
        :unit (s20u / 篇)
        :possessor (s20k / 刊
            :mod (s20g / 该))
        :topic (s20i / identity-91
            :ARG1 (s20s / 参议员
                :quant 12
                :unit (s20u2 / 位)
                :place (s20c / country
                    :name (s20n / name
                        :op1 "美国")))
            :ARG2 (s20w / 外星人)
            :aspect state))
    :ARG2 (s20q / 墙上
        :possessor (s20j / 记者团
            :mod (s20e / 参议院
                :place s20c)))
    :mod (s20m / 甚至)
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20t))
    :modal ((root :modal author)
            (author :full-affirmative s20t)
            (author :full-affirmative s20k)
            (author :full-affirmative s20i)
            (s20k :full-affirmative s20i))
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
a_event_found: R 100 / P 97 / F 98
a_event_concept: R 86 / P 86 / F 86
a_entity_found: R 100 / P 87 / F 93
a_entity_concept: R 76 / P 76 / F 76
a_granularity: R 100 / P 100 / F 100
b_event_sense: R 61 / P 61 / F 61
c_aspect: R 50 / P 60 / F 55
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 40 / P 40 / F 40
d_core_args_event: R 57 / P 73 / F 64
d_core_args_abstract: R 8 / P 11 / F 10
d_peripheral_event: R 57 / P 28 / F 38
d_peripheral_entity: R 32 / P 27 / F 29
e_core_labels: R 81 / P 81 / F 81
e_peripheral_labels: R 77 / P 77 / F 77
f_name_tokens: R 38 / P 43 / F 40
g_reentrancy: R 67 / P 43 / F 52
h_temporal: R 45 / P 45 / F 45
i_modal: R 54 / P 52 / F 53
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_event_found | extra | s16o: - -> 靠-01 | matches no gold node
a_entity_found | extra | s16d: - -> date-entity | matches no gold node
a_entity_found | extra | s16h2: - -> 还 | matches no gold node
a_entity_found | extra | s16y: - -> 也 | matches no gold node
a_entity_found | extra | s16s2: - -> 甚至 | matches no gold node
a_entity_concept | wrong | s16e: event -> 时 | event -> 时
b_event_sense | wrong | s16x8: 当-02 -> 当-01 | 当-02 -> 当-01
b_event_sense | wrong | s16x2: 注销 -> 注销-01 | 注销 -> 注销-01
b_event_sense | wrong | s16x15: 背书 -> 背书-01 | 背书 -> 背书-01
c_aspect | wrong | s16x:aspect: performance -> habitual | performance -> habitual
c_aspect | extra | s16x8:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s16x12:aspect: process -> performance | process -> performance
d_core_args_event | wrong | s16x14: arg0 s16i3/individual-person -> arg1 s16i3/individual-person | arg0 s16i3/individual-person: predicted as arg1
d_peripheral_event | extra | s16x2: - -> mod s16h2/还 (not in gold) | extra mod s16h2/还 (not in gold)
d_peripheral_event | extra | s16x3: - -> mod s16s2/甚至 (not in gold) | extra mod s16s2/甚至 (not in gold)
d_peripheral_event | partial | s16x14: temporal s16d/date-entity -> manner s16o/靠-01 (not in gold); mod s16y/也 (not in gold); temporal s16d/date-entity | extra manner s16o/靠-01 (not in gold); extra mod s16y/也 (not in gold)
d_peripheral_entity | wrong | s16x10: mod s16x12/握手-01 -> topic s16x12/握手-01 | mod s16x12/握手-01: predicted as topic
e_core_labels | wrong | s16x14 -arg0-> s16i3: arg0 -> arg1 | arg0 -> arg1
e_peripheral_labels | wrong | s16x10 -mod-> s16x12: mod -> topic | mod -> topic
f_name_tokens | missing | s16e: 2000 年 总统大选 -> - | the prediction has no :name
g_reentrancy | missing | s16x/报导-01 -quote-> s16x/报导-01: s16x/报导-01 -quote-> s16x/报导-01 -> - | the prediction has no such edge
g_reentrancy | missing | s16x15/背书 -quote-> s16x3/指-02: s16x15/背书 -quote-> s16x3/指-02 -> - | the prediction has no such edge
g_reentrancy | extra | s16o/靠-01 -arg0-> s16p3/individual-person: - -> s16o/靠-01 -arg0-> s16p3/individual-person | gold has no such reentrancy
g_reentrancy | extra | s16z/支持-01 -quote-> s16r/报导-01: - -> s16z/支持-01 -quote-> s16r/报导-01 | gold has no such reentrancy
a_event_concept | wrong | s17i2: identity -> have-mod | identity -> have-mod
a_entity_found | extra | s17g: - -> 也 | matches no gold node
b_event_sense | wrong | s17x: 荒唐-01 -> 荒唐 | 荒唐-01 -> 荒唐
b_event_sense | wrong | s17x2: 有-06 -> 有-01 | 有-06 -> 有-01
b_event_sense | wrong | s17x8: 荒谬-01 -> 荒谬 | 荒谬-01 -> 荒谬
b_event_sense | wrong | s17x11: 真实-01 -> 真实 | 真实-01 -> 真实
b_event_sense | wrong | s17x9: 可笑-01 -> 可笑 | 可笑-01 -> 可笑
c_aspect | missing | s17x:aspect: state -> - | the prediction has no :aspect
c_aspect | wrong | s17x7:aspect: habitual -> activity | habitual -> activity
c_aspect | missing | s17x8:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x11:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x9:aspect: state -> - | the prediction has no :aspect
d_core_args_event | partial | s17b: arg1 s17x/荒唐-01; arg2 s17x2/有-06 -> arg1 s17i2/identity-91; arg2 s17x2/有-06 | missing arg1 s17x/荒唐-01; extra arg1 s17i2/identity-91
d_core_args_event | missing | s17x: arg0 s17x3/内容 -> - | missing arg0 s17x3/内容
d_core_args_event | missing | s17x8: arg0 s17x10/新闻 -> - | missing arg0 s17x10/新闻
d_core_args_event | missing | s17x11: arg0 s17x10/新闻 -> - | missing arg0 s17x10/新闻
d_core_args_abstract | wrong | s17i2: arg1 s17x6/能力; arg2 s17x7/点出-01 -> arg1 s17x3/内容; arg2 s17x/荒唐-01 | missing arg1 s17x6/能力; missing arg2 s17x7/点出-01; extra arg1 s17x3/内容; extra arg2 s17x/荒唐-01
d_peripheral_event | extra | s17x2: - -> mod s17g/也 (not in gold) | extra mod s17g/也 (not in gold)
d_peripheral_event | extra | s17x8: - -> possessor s17x10/新闻 | extra possessor s17x10/新闻
d_peripheral_entity | extra | s17x3: - -> possessor s17x4/周报 | extra possessor s17x4/周报
d_peripheral_entity | missing | s17x4: part s17x3/内容 -> - | missing part s17x3/内容
d_peripheral_entity | extra | s17x6: - -> topic s17x7/点出-01 | extra topic s17x7/点出-01
d_peripheral_entity | extra | s17x10: - -> mod s17x11/真实-01 | extra mod s17x11/真实-01
e_core_labels | wrong | s17x8 -arg0-> s17x10: arg0 -> possessor | arg0 -> possessor
g_reentrancy | missing | s17x9/可笑-01 -arg0-> s17x10/新闻: s17x9/可笑-01 -arg0-> s17x10/新闻 -> - | the prediction has no such edge
g_reentrancy | extra | s17k/可笑 -possessor-> s17w/新闻: - -> s17k/可笑 -possessor-> s17w/新闻 | gold has no such reentrancy
a_event_concept | wrong | s18h: have-example -> 时 | have-example -> 时
a_entity_concept | wrong | s18i2: implicit-predicate -> name | implicit-predicate -> name
a_entity_concept | wrong | s18p: publication -> individual-person | publication -> individual-person
a_entity_concept | wrong | s18x4: 篇 -> country | 篇 -> country
a_entity_concept | wrong | s18x10: 人 -> 复制人 | 人 -> 复制人
b_event_sense | wrong | s18x3: 显著-01 -> 显著 | 显著-01 -> 显著
c_aspect | missing | s18x3:aspect: state -> - | the prediction has no :aspect
c_aspect | wrong | s18x11:aspect: process -> performance | process -> performance
c_other_attributes | extra | s18i2:op1: - -> 希特勒 | gold has no :op1
c_other_attributes | wrong | s18p:quant: 1 -> 10000 | 1 -> 10000
d_core_args_event | partial | s18x: arg0 s18t/thing; arg1 s18x2/位置; arg2 s18p/publication -> arg0 s18t/thing; arg1 s18x11/复制-01 | missing arg1 s18x2/位置; missing arg2 s18p/publication; extra arg1 s18x11/复制-01
d_core_args_event | missing | s18x3: arg0 s18x2/位置 -> - | missing arg0 s18x2/位置
d_core_args_event | wrong | s18x11: arg1 s18x10/人 -> arg0 s18x4/篇; arg1 s18p/publication | missing arg1 s18x10/人; extra arg0 s18x4/篇; extra arg1 s18p/publication
d_core_args_abstract | missing | s18h: arg1 s18i2/implicit-predicate; arg2 s18x/刊登-01 -> - | missing arg1 s18i2/implicit-predicate; missing arg2 s18x/刊登-01
d_peripheral_event | wrong | s18x: temporal s18x5/争论-01 -> place s18x2/位置; temporal s18h/have-example-91 | missing temporal s18x5/争论-01; extra place s18x2/位置; extra temporal s18h/have-example-91
d_peripheral_entity | extra | s18x2: - -> mod s18x3/显著-01 | extra mod s18x3/显著-01
d_peripheral_entity | wrong | s18p: unit s18x4/篇 -> unit s18n/name | missing unit s18x4/篇; extra unit s18n/name
e_core_labels | wrong | s18x -arg1-> s18x2: arg1 -> place | arg1 -> place
f_name_tokens | wrong | s18p: 「 苏联 复制 一万个 希特勒 」 -> 希特勒 | 「 苏联 复制 一万个 希特勒 」 -> 希特勒
f_name_tokens | extra | s18x4: - -> 苏联 | gold has no :name
g_reentrancy | extra | s18f/复制-01 -quote-> s18k/刊登-01: - -> s18f/复制-01 -quote-> s18k/刊登-01 | gold has no such reentrancy
a_event_concept | wrong | s19h: have-reason -> 买通 | have-reason -> 买通
a_entity_concept | wrong | s19p2: publication -> 追杀 | publication -> 追杀
a_entity_concept | wrong | s19x7: 篇 -> individual-person | 篇 -> individual-person
a_entity_concept | wrong | s19x4: 篇 -> name | 篇 -> name
c_aspect | extra | s19h:aspect: - -> performance | gold has no :aspect
c_aspect | wrong | s19x:aspect: performance -> habitual | performance -> habitual
c_aspect | wrong | s19x2:aspect: performance -> activity | performance -> activity
c_other_attributes | missing | s19p2:quant: 1 -> - | the prediction has no :quant
c_other_attributes | missing | s19x3:quant: 1 -> - | the prediction has no :quant
c_other_attributes | extra | s19x4:op1: - -> 宾拉登 | gold has no :op1
d_core_args_event | partial | s19x: arg0 s19p/person; arg1 s19p2/publication -> arg0 s19p/person; arg1 s19h/have-reason-91 | missing arg1 s19p2/publication; extra arg1 s19h/have-reason-91
d_core_args_abstract | wrong | s19h: arg1 s19x/报导-01; arg2 s19x2/讽刺-01 -> arg0 s19c/country; arg1 s19n/name | missing arg1 s19x/报导-01; missing arg2 s19x2/讽刺-01; extra arg0 s19c/country; extra arg1 s19n/name
d_peripheral_event | partial | s19x: mod s19x3/也 -> mod s19x3/也; purpose s19x2/讽刺-01 | extra purpose s19x2/讽刺-01
d_peripheral_entity | missing | s19p2: unit s19x7/篇 -> - | missing unit s19x7/篇
d_peripheral_entity | missing | s19x3: unit s19x4/篇 -> - | missing unit s19x4/篇
d_peripheral_entity | wrong | s19x5: possessor s19c/country; topic s19x6/外交 -> mod s19x6/外交 | missing possessor s19c/country; topic s19x6/外交: predicted as mod
e_peripheral_labels | wrong | s19p2 -unit-> s19x7: unit -> arg1 | unit -> arg1
e_peripheral_labels | wrong | s19x5 -topic-> s19x6: topic -> mod | topic -> mod
f_name_tokens | missing | s19p2: 「 美国 买通 外星人 去 追杀 宾拉登 」 -> - | the prediction has no :name
f_name_tokens | extra | s19x7: - -> 宾拉登 | gold has no :name
g_reentrancy | extra | s19m/买通-01 -quote-> s19r/报导-01: - -> s19m/买通-01 -quote-> s19r/报导-01 | gold has no such reentrancy
g_reentrancy | extra | s19z/追杀-01 -arg0-> s19w/外星人: - -> s19z/追杀-01 -arg0-> s19w/外星人 | gold has no such reentrancy
g_reentrancy | extra | s19e/政策 -possessor-> s19c/country: - -> s19e/政策 -possessor-> s19c/country | gold has no such reentrancy
a_event_concept | wrong | s20x3: 好事 -> 甚至 | 好事 -> 甚至
a_entity_found | extra | s20u2: - -> 位 | matches no gold node
a_entity_found | extra | s20e: - -> 参议院 | matches no gold node
a_entity_concept | wrong | s20x2: 者 -> 好事者 | 者 -> 好事者
a_entity_concept | wrong | s20b: building -> country | building -> country
a_entity_concept | wrong | s20p: publication -> 外星人 | publication -> 外星人
c_aspect | missing | s20x3:aspect: state -> - | the prediction has no :aspect
d_core_args_event | partial | s20x: arg0 s20x2/者; arg1 s20x4/墙上; arg2 s20x6/新闻 -> arg0 s20x2/者; arg1 s20x6/新闻; arg2 s20x4/墙上 | arg1 s20x4/墙上: predicted as arg2; arg2 s20x6/新闻: predicted as arg1
d_core_args_event | missing | s20x3: arg0 s20x2/者 -> - | missing arg0 s20x2/者
d_core_args_abstract | partial | s20i2: arg1 s20x6/新闻; arg2 s20p/publication -> arg1 s20n2/name; arg2 s20p/publication | missing arg1 s20x6/新闻; extra arg1 s20n2/name
d_peripheral_event | extra | s20x: - -> mod s20x3/好事 | extra mod s20x3/好事
d_peripheral_entity | extra | s20x4: - -> possessor s20x5/记者团 | extra possessor s20x5/记者团
d_peripheral_entity | wrong | s20x5: place s20b/building; place s20x4/墙上 -> mod s20e/参议院 (not in gold) | missing place s20b/building; missing place s20x4/墙上; extra mod s20e/参议院 (not in gold)
d_peripheral_entity | partial | s20x6: unit s20x7/篇 -> possessor s20x8/刊; topic s20i2/identity-91; unit s20x7/篇 | extra possessor s20x8/刊; extra topic s20i2/identity-91
d_peripheral_entity | partial | s20x8: mod s20x9/该; part s20x6/新闻 -> mod s20x9/该 | missing part s20x6/新闻
e_core_labels | wrong | s20x -arg1-> s20x4: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s20x -arg2-> s20x6: arg2 -> arg1 | arg2 -> arg1
f_name_tokens | wrong | s20b: 美国 参议院 -> 美国 | 美国 参议院 -> 美国
f_name_tokens | missing | s20p: 「 12 位 美国 参议员 是 外星人 ！ 」 -> - | the prediction has no :name
g_reentrancy | extra | s20e/参议院 -place-> s20c/country: - -> s20e/参议院 -place-> s20c/country | gold has no such reentrancy
h_temporal | extra | ?date-entity (snt16 s16d): - -> document-creation-time :before ?date-entity (snt16 s16d) | a predicted node that matches nothing in gold
h_temporal | extra | ?靠-01 «靠» (snt16 s16o): - -> 当选-01 «当选» (snt16 s16x14 = pred s16e) :overlap ?靠-01 «靠» (snt16 s16o) | a predicted node that matches nothing in gold
h_temporal | extra | date-entity (snt16 s16d = pred s16d3): - -> document-creation-time :before date-entity (snt16 s16d = pred s16d3) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt16 s16x = pred s16r): document-creation-time :before 报导-01 «报导» (snt16 s16x = pred s16r) -> ?date-entity (snt16 s16d) :overlap 报导-01 «报导» (snt16 s16x = pred s16r) | wrong parent and relation
h_temporal | wrong | 合成-01 «合成» (snt16 s16x11 = pred s16h): 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 合成-01 «合成» (snt16 s16x11 = pred s16h) -> 注销 «注销» (snt16 s16x2 = pred s16c) :before 合成-01 «合成» (snt16 s16x11 = pred s16h) | right parent, wrong relation
h_temporal | wrong | 当选-01 «当选» (snt16 s16x14 = pred s16e): 指-02 «指» (snt16 s16x3 = pred s16i) :before 当选-01 «当选» (snt16 s16x14 = pred s16e) -> date-entity (snt16 s16d = pred s16d3) :overlap 当选-01 «当选» (snt16 s16x14 = pred s16e) | wrong parent and relation
h_temporal | wrong | 背书 «背书» (snt16 s16x15 = pred s16b): 当选-01 «当选» (snt16 s16x14 = pred s16e) :overlap 背书 «背书» (snt16 s16x15 = pred s16b) -> ?靠-01 «靠» (snt16 s16o) :overlap 背书 «背书» (snt16 s16x15 = pred s16b) | right relation, wrong parent
h_temporal | wrong | 指-02 «指» (snt16 s16x3 = pred s16i): 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 指-02 «指» (snt16 s16x3 = pred s16i) -> 报导-01 «报导» (snt16 s16x = pred s16r) :overlap 指-02 «指» (snt16 s16x3 = pred s16i) | right relation, wrong parent
h_temporal | missing | 荒唐-01 «荒唐» (snt17 s17x = pred s17t): document-creation-time :before 荒唐-01 «荒唐» (snt17 s17x = pred s17t) -> - | the prediction gives this node no temporal parent
h_temporal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17z): 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17z) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 有-06 «有» (snt17 s17x2 = pred s17y): 荒唐-01 «荒唐» (snt17 s17x = pred s17t) :overlap 有-06 «有» (snt17 s17x2 = pred s17y) -> document-creation-time :overlap 有-06 «有» (snt17 s17x2 = pred s17y) | right relation, wrong parent
h_temporal | missing | 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m): 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) -> - | the prediction gives this node no temporal parent
h_temporal | missing | 可笑-01 «可笑» (snt17 s17x9 = pred s17k): 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 可笑-01 «可笑» (snt17 s17x9 = pred s17k) -> - | the prediction gives this node no temporal parent
h_temporal | extra | 复制-01 «复制» (snt18 s18x11 = pred s18f): - -> 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 复制-01 «复制» (snt18 s18x11 = pred s18f) | gold gives this node no temporal parent
h_temporal | missing | 显著-01 «显著» (snt18 s18x3 = pred s18x): 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 显著-01 «显著» (snt18 s18x3 = pred s18x) -> - | the prediction gives this node no temporal parent
h_temporal | extra | have-reason-91 (snt19 s19h = pred s19m): - -> 报导-01 «报导» (snt19 s19x = pred s19r) :overlap have-reason-91 (snt19 s19h = pred s19m) | gold gives this node no temporal parent
h_temporal | extra | publication (snt19 s19p2 = pred s19z): - -> have-reason-91 (snt19 s19h = pred s19m) :overlap publication (snt19 s19p2 = pred s19z) | gold gives this node no temporal parent
h_temporal | missing | 好事 «好事者» (snt20 s20x3 = pred s20m): 贴到-01 «贴到» (snt20 s20x = pred s20t) :overlap 好事 «好事者» (snt20 s20x3 = pred s20m) -> - | the prediction gives this node no temporal parent
i_modal | extra | ?靠-01 «靠» (snt16 s16o): - -> author :full-affirmative ?靠-01 «靠» (snt16 s16o); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative ?靠-01 «靠» (snt16 s16o) | a predicted node that matches nothing in gold
i_modal | wrong | 报导-01 «报导» (snt16 s16x = pred s16r): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16r) -> author :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16r) | right relation, wrong parent
i_modal | partial | 当选-01 «当选» (snt16 s16x14 = pred s16e): author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16e) -> author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16e); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16e) | agrees on part of the relations
i_modal | partial | 背书 «背书» (snt16 s16x15 = pred s16b): author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16b) -> author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16b); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16b) | agrees on part of the relations
i_modal | wrong | 注销 «注销» (snt16 s16x2 = pred s16c): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16c) -> author :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16c) | right relation, wrong parent
i_modal | wrong | 指-02 «指» (snt16 s16x3 = pred s16i): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16i) -> author :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16i) | right relation, wrong parent
i_modal | partial | 支持-01 «支持» (snt16 s16x6 = pred s16z): author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z) -> author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z) | agrees on part of the relations
i_modal | extra | 当-02 «当» (snt16 s16x8 = pred s16d2): - -> author :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16d2); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16d2) | gold gives this node no modal parent
i_modal | missing | 荒唐-01 «荒唐» (snt17 s17x = pred s17t): author :full-affirmative 荒唐-01 «荒唐» (snt17 s17x = pred s17t) -> - | the prediction gives this node no modal parent
i_modal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17z): author :full-affirmative 真实-01 «真实» (snt17 s17x11 = pred s17z) -> - | the prediction gives this node no modal parent
i_modal | partial | 点出-01 «点» (snt17 s17x7 = pred s17d): author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) [from the sentence-graph modal-strength] -> author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) [from the sentence-graph modal-strength]; 有-06 «有» (snt17 s17x2 = pred s17y) :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) | agrees on part of the relations
i_modal | missing | 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m): author :full-affirmative 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) -> - | the prediction gives this node no modal parent
i_modal | missing | 可笑-01 «可笑» (snt17 s17x9 = pred s17k): author :full-affirmative 可笑-01 «可笑» (snt17 s17x9 = pred s17k) -> - | the prediction gives this node no modal parent
i_modal | extra | thing (snt18 s18t = pred s18p): - -> author :full-affirmative thing (snt18 s18t = pred s18p) | gold gives this node no modal parent
i_modal | partial | 复制-01 «复制» (snt18 s18x11 = pred s18f): author :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18f) -> author :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18f); thing (snt18 s18t = pred s18p) :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18f) | agrees on part of the relations
i_modal | missing | 显著-01 «显著» (snt18 s18x3 = pred s18x): author :full-affirmative 显著-01 «显著» (snt18 s18x3 = pred s18x) -> - | the prediction gives this node no modal parent
i_modal | extra | have-reason-91 (snt19 s19h = pred s19m): - -> author :full-affirmative have-reason-91 (snt19 s19h = pred s19m); person (snt19 s19p = pred s19p) :full-affirmative have-reason-91 (snt19 s19h = pred s19m) | gold gives this node no modal parent
i_modal | extra | person (snt19 s19p = pred s19p): - -> author :full-affirmative person (snt19 s19p = pred s19p) | gold gives this node no modal parent
i_modal | extra | publication (snt19 s19p2 = pred s19z): - -> author :full-affirmative publication (snt19 s19p2 = pred s19z); person (snt19 s19p = pred s19p) :full-affirmative publication (snt19 s19p2 = pred s19z) | gold gives this node no modal parent
i_modal | partial | identity-91 (snt20 s20i2 = pred s20i): author :full-affirmative identity-91 (snt20 s20i2 = pred s20i) -> author :full-affirmative identity-91 (snt20 s20i2 = pred s20i); 刊 «该刊» (snt20 s20x8 = pred s20k) :full-affirmative identity-91 (snt20 s20i2 = pred s20i) | agrees on part of the relations
i_modal | missing | 好事 «好事者» (snt20 s20x3 = pred s20m): author :full-affirmative 好事 «好事者» (snt20 s20x3 = pred s20m) -> - | the prediction gives this node no modal parent
i_modal | extra | 刊 «该刊» (snt20 s20x8 = pred s20k): - -> author :full-affirmative 刊 «该刊» (snt20 s20x8 = pred s20k) | gold gives this node no modal parent

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.