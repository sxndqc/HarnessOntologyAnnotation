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

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value
and document-level relation counts. Take the time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.
- Follow the examples: when a sentence has a construction an example shows, annotate it the way the
  example does.
- Before you go on to the next sentence, check the graph against the guidelines once more: every word
  that carries meaning has its concept, every event its aspect, every role the right direction; and at
  the end check that the document-level relations cover every event and entity the guidelines ask for.

## Guidelines

# UMR guidelines, abridged

A short version of the UMR 0.9 specification (`umr_guidelines.md` in this folder, umr4nlp/umr-guidelines),
for annotating Chinese and English at Stage 1 (numbered PropBank roles). Where the full guideline uses the older short names (`AUTH`, `DCT`,
`FullAff`, `:modstr`, `:ref-person`, `Performance`), this version uses the names of the UMR release data
(`author`, `document-creation-time`, `full-affirmative`, `:modal-strength`, `:refer-person`, `performance`).

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
- event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events;
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
recoverable may be added as such a node (aligned to no word) and linked by coreference.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过, 可是) `but-91` when it links two clauses of the same sentence; a sentence-initial 不过/但是 that links to the previous sentence is not annotated (the root is the clause's verb);
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) and 以…而 → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) with no second connective → `:concession`; 虽然 X，不过/但是 Y → `(but-91 :ARG1 X :ARG2 Y)`. 后来/然后 linking two clauses → `(consecutive :op1 X :op2 Y)`, no node for 后来. 以 X 为目的 → `(identity-91 :ARG1 (目的 :purpose-of <event>) :ARG2 X)` (X a plain concept), not have-purpose-91. A parenthetical 'N：quote' → `(identity-91 :ARG1 N :ARG2 <content>)`, joined to its clause by `and`.
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

- Chinese adverbs are concepts, not only aspect cues. 已经, 都, 也, 仍, 还 and 其中 → `:mod (<word>)`; 曾经 → `:temporal (曾经)`. A medium (电视, 网络) is `:medium`.
- A modifier shared by coordinated nouns goes on each conjunct by reentrancy, never on the `and` node.
- Do not add arguments (agents, possessors, organizations) that the text does not express. Never re-use a participant from elsewhere in the sentence as an unexpressed agent or possessor: every re-entrancy needs a pronoun or an overt word. Exception: the overt subject of a control or aspectual verb (继续, 停止, 开始, 想, 打算) is also `:ARG0` of the embedded event or nominal (它停止了它的发行 → 发行 `:ARG0` 它). 旗下 is `:mod (旗下)`, not a possessor. Do not fill the subject of a later clause with an entity from an earlier clause (…，不过仍继续发行网络版: 发行 has no `:ARG0`).
- An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor` — but only when the whole is written with it (《…》的纸本). A bare 网络版 gets no `:part-of`.
- For an intransitive Chinese verb such as 停刊-01 (or a `-00` verb not in PropBank), the sole participant is `:ARG0`.
- When an event noun names what the head noun is (查证程序: the procedure is the verification), use `(程序 :ARG0-of (identity-91 :ARG1 (查证-01)))`, not `:mod`.
- In 'X 是 … Y，以 … 而 V' the second predicate modifies Y: `Y :ARG1-of (V :reason ...)`. Do not add a coordinating `and`.
- Apposition `<common noun> + 《name》` (八卦小报《国家询问报》): the named entity is the head, and the common noun hangs from it by `:ARG1-of (identity-91 :ARG2 (<noun> :mod …))`.
- In V 了 Adj-N 的《Name》 the object is the head noun with `:part-of` the named entity (创立了黑白版面的《…》 → `创立 :ARG1 (版面 :mod (黑白) :part-of (newspaper …))`); a relative clause before it (容纳…的) modifies that noun.
- 由 X 改为/变为 Y: X is `:ARG1`, Y is `:ARG2`; no `:source`. In `<Whole> 由 X 改为 Y`, when X and Y are parts or features of the subject (版面, 颜色, 名称), 改为 has **no** `:ARG0`: the subject is `:part-of` on X (`改为 :ARG1 (版面 :part-of <newspaper> :mod (黑白)) :ARG2 (版面 :mod (彩色))`).
- Build a repeated entity in full (name, apposition, modifiers) at its first mention in the graph (first in reading order), and refer to it at later mentions in the same sentence by its bare variable (`:possessor s7n`).
- A role noun built from a verb (创始人) is `(person :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance))))`, with no `:ARG2` unless the organization is written with it.
- Take role numbers from the Chinese roleset, not from the English equivalent: for change-of-state and amount verbs (成-01, 达到-01, 跌-01, 增至) the theme is `:ARG0` (成-01 `:ARG0` theme, `:ARG1` result). Look it up.
- An adjective saying how an event noun's action is done is `:manner` (黑白印刷 → `印刷 :manner (黑白)`).
- '<noun> 有 A、B…等' and 如 A、B 等 → `<noun> :example (and :op1 A :op2 B :op3 (等))`; 有 is no event; 等 is always the last `:opN`. Nouns in such lists are entities (时间旅行 → `(旅行 :mod (时间))`). 重复/经常 → `:frequency`; 在 N 中 → `(中 :op1 N)`; 大部分 → `:mod`.
- X 与 Y 有关系 → `(有-03 :ARG0 (and :op1 X :op2 Y) :ARG1 (关系 …))`, no `:companion`. 被指 → `指-02`. Look up the whole compound first (算是-01, 称为-01).
- A common noun directly before a name (外星人 P'Lod) is no apposition: `(外星人 :name (name …))`, no identity-91. 母公司 → `(公司 :mod (母))`. 前 → `:mod (前)` on the role noun; 第一夫人 → `have-rel-role-91 :ARG3 (第一夫人 :place (country …))`.
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

Aspect cues: a publication's or institution's own recurring verbs (发行, 报导, 综合, 印刷) used as predicates are `habitual`, even with 了; this cue does not extend to other verbs. A relative clause describing what a newly founded thing was designed to do (容纳…文章的版面) is `process`. A purpose event (为/为了 X, `have-purpose-91 :ARG2`, `:purpose`) is `activity`, not `performance`, even when it is modally full-affirmative. 已经 + 停止 or another end verb is `state` only inside a relative clause that describes an entity (已经停止发行的小报); as the main predicate, 已经 + an end verb (已经停刊) is `performance`. Passive naming (被称为) is `performance`. Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂. An event nominal that is the object of 停止/开始 (它的发行) is `process` (no habitual). 生存, 存在 → `state`; an ongoing activity noun (活动) → `activity`. A negated event (未, 没) never gets `performance`; use `process` when its type cannot be told.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

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
- A sentence with no time expression that continues the previous sentence's episode hangs its main event from that sentence's main event (`(s7x :overlap s8x)`); but a sentence that judges or sums up the earlier text (算是, 其中最…) is anchored to `document-creation-time` itself.
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
- The root abstract predicate (`identity-91`, `have-mod-91`, ...) of an asserted sentence also gets `(author :full-affirmative …)`, although it gets no temporal parent.
- Reported speech or thought: `(author :full-affirmative s9p)` for the speaker node, and each content event gets **both** `(author :full-affirmative X)` and `(s9p :full-affirmative X)`. The conceiver is the speaker's entity node, not the reporting verb; with no written speaker (被指) use the passive subject.
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
- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.
- Link two mentions only when they pick out the same individual or the same single event. Do not link two mentions of the same verb with different arguments, times or polarity (发行 of the print edition vs 发行 of the online edition). Do not link noun phrases with the same head but different restrictors (许多内容 vs 荒诞不经的内容). Never put a `:subset-of` triple inside one sentence. Do not link events expressed by different verbs (创刊 vs 创立) unless the text makes them clearly identical. When in doubt, leave the link out; chains like 周报 / 该周报 / 《…周报》 are what gold annotates.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect`; negated events have `:polarity -`.
- Every event and time expression has a temporal parent; every event has a modal parent (except the inner verb of a V+量 compound, which has only a temporal parent).
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.

## Examples

- Temporal chain (5.1): 目前…停刊，不过仍继续发行网络版 → `(document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`; 目前 has no temporal parent.
- Copular root (5.1): 是…已经停止发行的小报，以报导…而闻名 → `(document-creation-time :before 发行) (发行 :overlap 停止) (闻名 :contained 发行) (发行 :overlap 报导)`; modal `(author :full-affirmative identity-91)`.
- Coref (5.3): 发行 (print, stopped) vs 发行 (online edition, continuing) → no `:same-event`.
- Aspect (4.1): main predicate 纸本已经停刊 → `(停刊-01 :ARG0 (纸本 …) :aspect performance)`; 继续发行网络版 → bare `(网络版)`, no `:part-of`.
- 曾经 + 过 (4.1, 5.1): 也曾经短暂的拥有过一个节目 → `(拥有-01 :temporal (曾经) :aspect state)`, `(document-creation-time :before 拥有) (拥有 :overlap …)`; 曾经 has no temporal parent.
- Negation (4.2): 都未经一般的新闻查证程序 → `(经-01 :mod (都) :aspect process)` without `:polarity`; modal `(author :full-negative 经) (author :partial-affirmative 查证)`.
- Degree (2.3): 美国历史上最…的报纸 → `(报纸 :temporal (上 :op1 (历史 :place (country …))))`, `have-degree-91` without aspect; 称为 → `称为-01`.
- Adverb (3): 已经停止 → `(停止-01 :mod (已经) :aspect state)`; 曾经 → `:temporal (曾经)`.
- Name (2.2): 美国…小报 → `(小报 :place (country :name (name :op1 "美国")))`, with no `:wiki`.
- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`.

- Date (5.1): 1980年代…改为 → `(document-creation-time :before s9d) (s9d :overlap s9x)`, `(date-entity :era 1980)`.
- Clause links (2.5): 因为 X，为 Y，于是 Z → `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state) :ARG2 改为 :aspect state)`; temporal `(创立 :overlap 运用) (创立 :before 改为)`.
- Apposition (3): 旗下的八卦小报《国家询问报》 → `(newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 :mod (旗下) :mod (八卦))))`.
- 改为 (3): 小报《…》将由黑白版面改为彩色版面 …不符合《…》标准 → `(改为-01 :ARG1 (版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 …))) :mod (黑白)) :ARG2 (版面 :mod (彩色)))`, no `:ARG0`; later `(标准 :possessor s7n)`.
- Measure noun (2.2): 发行量达到120万份 → `(达到-01 :ARG0 (量 :quant-of (发行-01 :ARG1 …) :ARG1-of (have-quant-91 :ARG2 1200000 :unit (份))) :aspect performance)`, `(达到 :overlap 发行)`.
- Roles (3): 黑白印刷也成了该刊的特色 → `(成-01 :ARG0 (印刷-01 :manner (黑白) :aspect habitual) :ARG1 (特色 :poss… (刊 :mod (该))))`; temporal from previous sentence's main event.

- Aspect (4.1): 为充分运用… → `运用 :aspect activity`; 容纳…文章的版面 → `(版面 :ARG0-of (容纳-01 … :aspect process))`.
- Named person (2.2): 格内洛索·波普 → `(individual-person :name (name :op1 "格内洛索" :op2 "·" :op3 "波普"))`.

- Control (3): 网络版继续生存 → `(继续-01 :ARG0 s11n :ARG1 (生存-01 :ARG0 s11n :aspect state))`; temporal `(停止 :overlap 继续)`.
- 虽然…不过 (2.5): → `(but-91 :ARG1 (and :op1 宣称 :op2 (identity-91 :ARG1 标语 :ARG2 报导)) :ARG2 (identity-91 :ARG1 (目的 :purpose-of 报导) :ARG2 (博君一笑)))`; no modal triple on but-91/and.
- Quote (5.2): 宣称其报导都是真实的 → `(have-mod-91 :quote s12x …)`, `(author :full-affirmative 报导) (s12n :full-affirmative 报导)`.
- 被指 (5.1): 被指与X有暧昧关系，后来领养 → `(consecutive :op1 (有-03 :quote 指) :op2 (领养 :quote 指))`, `(指 :overlap 有) (有 :after 领养)`, conceiver = passive subject.
- List (3): 题材有A、B等 → `(题材 :example (and :op1 A :op2 B :op3 (等)))`; 重复出现 → `:frequency (重复)`.

</instruction>

# The sentences
11	2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了 《 世界 新闻 周报 》 的 发行 ， 不过 周报 的 网络版 仍 继续 生存 。
12	虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。
13	他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。
14	其中 最大宗 可 算是 外星人 地球 活动 。
15	美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
Words: 2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了 《 世界 新闻 周报 》 的 发行 ， 不过 周报 的 网络版 仍 继续 生存 。

# sentence level graph:
(s11b / but-91
    :ARG1 (s11x / 停止-01
        :temporal (s11d / date-entity
            :year 2007
            :month 7)
        :ARG0 (s11c / 公司
            :mod (s11m / 母)
            :name (s11n2 / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司"))
        :ARG1 (s11x2 / 发行-01
            :ARG1 (s11n / newspaper
                :name (s11n3 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :aspect process)
        :aspect performance)
    :ARG2 (s11x3 / 继续-01
        :ARG0 (s11w / 网络版
            :part-of s11n)
        :ARG1 (s11x4 / 生存-01
            :ARG0 s11w
            :aspect state)
        :mod (s11r / 仍)
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11x)
               (s11x :overlap s11x2)
               (s11x :overlap s11x3)
               (s11x3 :overlap s11x4))
    :modal ((root :modal author)
            (author :full-affirmative s11x)
            (author :full-affirmative s11x2)
            (author :full-affirmative s11x3)
            (author :full-affirmative s11x4)))


################################################################################
# meta-info
# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。

# sentence level graph:
(s12b / but-91
    :ARG1 (s12a / and
        :op1 (s12x / 宣称-01
            :ARG0 (s12n / newspaper
                :name (s12n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :ARG1 (s12h / have-mod-91
                :quote s12x
                :ARG1 (s12r / 报导-01
                    :ARG0 (s12p / person
                        :refer-person 3rd
                        :refer-number plural)
                    :aspect habitual)
                :ARG2 (s12t / 真实)
                :mod (s12d / 都)
                :aspect state)
            :aspect activity)
        :op2 (s12i / identity-91
            :ARG1 (s12s / 标语
                :possessor s12p)
            :ARG2 (s12r2 / 报导-01
                :ARG1 (s12f / 事实)
                :mod (s12o / 只)
                :ARG0 s12n
                :aspect habitual)))
    :ARG2 (s12i2 / identity-91
        :ARG1 (s12g / 目的
            :purpose-of (s12r3 / 报导-01
                :mod (s12m / 大部分)
                :aspect habitual))
        :ARG2 (s12y / 博君一笑)
        :mod (s12d2 / 都)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
               (s12x :overlap s12r)
               (s12x :overlap s12r2)
               (s12x :overlap s12r3))
    :modal ((root :modal author)
            (author :full-affirmative s12x)
            (author :full-affirmative s12n)
            (author :full-affirmative s12r)
            (s12n :full-affirmative s12r)
            (author :full-affirmative s12i)
            (author :full-affirmative s12r2)
            (author :full-affirmative s12i2)
            (author :full-affirmative s12r3))
    :coref ((s11n :same-entity s12n)))


################################################################################
# meta-info
# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。

# sentence level graph:
(s13a / and
    :op1 (s13t / 题材
        :ARG1-of (s13r / 报导-01
            :ARG0 (s13p / person
                :refer-person 3rd
                :refer-number plural)
            :frequency (s13f / 经常)
            :aspect habitual)
        :example (s13a2 / and
            :op1 (s13w / 外星人)
            :op2 (s13h / 航天员
                :mod (s13g / 古代))
            :op3 (s13l / 旅行
                :mod (s13s / 时间))
            :op4 (s13b / 大脚)
            :op5 (s13o / 欧帕兹)
            :op6 (s13d / 等)))
    :op2 (s13c / 创造-01
        :ARG0 s13p
        :mod (s13e / 甚至)
        :ARG1 (s13y / 人物
            :mod (s13v / 虚拟)
            :quant (s13k / 一些)
            :ARG0-of (s13x / 出现-01
                :place (s13z / 中
                    :op1 (s13n / 新闻
                        :possessor s13p))
                :frequency (s13q / 重复)
                :aspect habitual)
            :example (s13a3 / and
                :op1 (s13m / 男孩
                    :mod (s13bt / 蝙蝠))
                :op2 (s13al / 外星人
                    :name (s13nn / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod"))
                :op3 (s13d2 / 等)))
        :aspect performance))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13r)
               (s13r :overlap s13c)
               (s13c :after s13x))
    :modal ((root :modal author)
            (author :full-affirmative s13r)
            (author :full-affirmative s13c)
            (author :full-affirmative s13x))
    :coref ((s12p :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14x / 算是-01
    :ARG1 (s14t / thing
        :mod (s14q / 其中)
        :ARG1-of (s14h / have-degree-91
            :ARG2 (s14b / 大宗)
            :ARG3 (s14z / 最)))
    :ARG2 (s14a / 活动
        :ARG0 (s14w / 外星人)
        :place (s14e / planet
            :name (s14n / name
                :op1 "地球"))
        :aspect activity)
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :overlap s14x)
               (s14x :overlap s14a))
    :modal ((root :modal author)
            (author :full-affirmative s14x)
            (author :full-affirmative s14a))
    :coref ((s14t :subset-of s13t)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15x / 指-02
    :ARG1 (s15c / consecutive
        :op1 (s15y / 有-03
            :ARG0 (s15a / and
                :op1 (s15p / individual-person
                    :name (s15n / name
                        :op1 "希拉里"
                        :op2 "·"
                        :op3 "克林顿")
                    :ARG1-of (s15r / have-rel-role-91
                        :ARG3 (s15f / 第一夫人
                            :mod (s15q / 前)
                            :place (s15k / country
                                :name (s15n3 / name
                                    :op1 "美国")))))
                :op2 (s15w / 外星人
                    :name (s15n2 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod")))
            :ARG1 (s15g / 关系
                :mod (s15m / 暧昧))
            :quote s15x
            :aspect state)
        :op2 (s15l / 领养-01
            :ARG0 s15p
            :ARG1 (s15b / 宝宝
                :mod (s15e / 外星))
            :mod (s15h / 还)
            :quote s15x
            :aspect performance))
    :mod (s15j / 就)
    :aspect performance)


# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15x)
               (s15x :overlap s15y)
               (s15y :after s15l))
    :modal ((root :modal author)
            (author :full-affirmative s15x)
            (author :full-affirmative s15p)
            (author :full-affirmative s15y)
            (s15p :full-affirmative s15y)
            (author :full-affirmative s15l)
            (s15p :full-affirmative s15l))
    :coref ((s13al :same-entity s15w)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
Words: 2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了 《 世界 新闻 周报 》 的 发行 ， 不过 周报 的 网络版 仍 继续 生存 。

# sentence level graph:
(s11b / but-91
    :ARG1 (s11x / 停止-01
        :ARG0 (s11c / company
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司")
            :ARG1-of (s11i2 / identity-91
                :ARG2 (s11x6 / 公司
                    :mod (s11x7 / 母))))
        :ARG1 (s11x8 / 发行-01
            :ARG0 s11c
            :ARG1 (s11n2 / newspaper
                :name (s11n3 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :aspect process)
        :temporal (s11d / date-entity
            :year 2007
            :month 7)
        :aspect performance)
    :ARG2 (s11x2 / 继续-01
        :ARG0 (s11x4 / 网络版
            :part-of (s11x5 / 周报))
        :ARG1 (s11x3 / 生存-01
            :ARG0 s11x4
            :aspect state)
        :temporal s11d
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11x)
               (s11x :overlap s11x8)
               (s11x :overlap s11x2)
               (s11x2 :overlap s11x3))
    :modal ((root :modal author)
            (author :full-affirmative s11x8)
            (author :full-affirmative s11x)
            (author :full-affirmative s11x3)
            (author :full-affirmative s11x2))
    :coref ((s11n2 :same-entity s11x5)))


################################################################################
# meta-info
# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。

# sentence level graph:
(s12b / but-91
    :ARG1 (s12a / and
        :op1 (s12x / 宣称-01
            :ARG0 (s12n / newspaper
                :name (s12n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :ARG1 (s12h / have-mod-91
                :ARG1 (s12x4 / 报导-01
                    :aspect habitual)
                :ARG2 (s12x3 / 真实)
                :mod (s12x2 / 都)
                :aspect state
                :quote s12x)
            :aspect performance)
        :op2 (s12i3 / identity-91
            :ARG1 (s12x5 / 标语
                :possessor s12n)
            :ARG2 (s12x6 / 报导-01
                :ARG0 s12n
                :ARG1 (s12x8 / 事实)
                :mod (s12x7 / 只)
                :aspect habitual
                :quote s12i3)
            :aspect state))
    :ARG2 (s12i2 / identity-91
        :ARG1 (s12x9 / 目的
            :purpose-of (s12x10 / 报导-01
                :mod (s12x11 / 大部分)
                :aspect habitual))
        :ARG2 (s12x12 / 博君一笑)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
               (s12x :overlap s12x4)
               (s12x4 :overlap s12x6)
               (s12x4 :overlap s12x10))
    :modal ((root :modal author)
            (author :full-affirmative s12x4)
            (author :full-affirmative s12h)
            (author :full-affirmative s12x)
            (author :full-affirmative s12x6)
            (author :full-affirmative s12i3)
            (author :full-affirmative s12x10)
            (author :full-affirmative s12i2)
            (author :full-affirmative s12n)
            (s12n :full-affirmative s12h)
            (s12n :full-affirmative s12x6)
            (s12n :full-affirmative s12x10))
    :coref ((s11n2 :same-entity s12n)))


################################################################################
# meta-info
# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。

# sentence level graph:
(s13a / and
    :op1 (s13x2 / 报导-01
        :ARG0 (s13p / person
            :refer-number plural
            :refer-person 3rd)
        :ARG1 (s13x4 / 题材
            :example (s13a2 / and
                :op1 (s13x5 / 外星人)
                :op2 (s13x6 / 航天员
                    :mod (s13x11 / 古代))
                :op3 (s13x7 / 旅行
                    :mod (s13x12 / 时间))
                :op4 (s13x8 / 大脚)
                :op5 (s13x9 / 欧帕兹)
                :op6 (s13x10 / 等)))
        :frequency (s13x3 / 经常)
        :aspect habitual)
    :op2 (s13x / 创造-01
        :ARG0 s13p
        :ARG1 (s13x13 / 人物
            :mod (s13x14 / 虚拟)
            :quant (s13x15 / 一些)
            :ARG0-of (s13x16 / 出现-01
                :ARG1 (s13x18 / 中
                    :op1 (s13x19 / 新闻
                        :possessor s13p))
                :frequency (s13x17 / 重复)
                :aspect habitual)
            :example (s13a3 / and
                :op1 (s13i2 / individual-person
                    :name (s13n / name
                        :op1 "蝙蝠"
                        :op2 "男孩"))
                :op2 (s13i3 / individual-person
                    :name (s13n2 / name
                        :op1 "外星人"
                        :op2 "P"
                        :op3 "'"
                        :op4 "Lod"))
                :op3 (s13x20 / 等)))
        :aspect performance
        :mod (s13x21 / 甚至)))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13x2)
               (s13x2 :overlap s13x)
               (s13x :overlap s13x6))
    :modal ((root :modal author)
            (author :full-affirmative s13x2)
            (author :full-affirmative s13x16)
            (author :full-affirmative s13x))
    :coref ((s12n :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14x / 算是-01
    :ARG0 (s14i2 / implicit-argument
        :ARG1-of (s14h / have-degree-91
            :ARG1 (s14x3 / 大)
            :ARG2 (s14x4 / 最)
            :ARG5 (s14x5 / 其中))
        :unit (s14x2 / 宗))
    :ARG1 (s14x6 / 活动-01
        :ARG0 (s14x7 / 外星人)
        :place (s14p / planet
            :name (s14n / name
                :op1 "地球"))
        :aspect activity)
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :before s14x)
               (s14x :overlap s14x6))
    :modal ((root :modal author)
            (author :full-affirmative s14x6)
            (author :neutral-affirmative s14x)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15x / 指-02
    :ARG1 (s15c / consecutive
        :op1 (s15x3 / 有-03
            :ARG0 (s15a / and
                :op1 (s15i2 / individual-person
                    :name (s15n / name
                        :op1 "希拉里"
                        :op2 "·"
                        :op3 "克林顿")
                    :ARG1-of (s15h / have-rel-role-91
                        :ARG3 (s15x6 / 第一夫人
                            :mod (s15x7 / 前)
                            :place (s15c2 / country
                                :name (s15n2 / name
                                    :op1 "美国")))))
                :op2 (s15x11 / 外星人
                    :name (s15n4 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod")))
            :ARG1 (s15x4 / 关系
                :mod (s15x5 / 暧昧))
            :aspect state
            :quote s15x)
        :op2 (s15x2 / 领养-00
            :ARG0 s15i2
            :ARG1 (s15x9 / 宝宝
                :mod (s15x10 / 外星))
            :aspect performance
            :quote s15x))
    :aspect performance)


# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15x)
               (s15x :overlap s15x3)
               (s15x3 :after s15x2))
    :modal ((root :modal author)
            (s15a :full-affirmative s15x3)
            (s15a :full-affirmative s15x2)
            (author :full-affirmative s15x)
            (author :full-affirmative s15a)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 100 / P 100 / F 100
a_event_concept: R 96 / P 96 / F 96
a_entity_found: R 95 / P 93 / F 94
a_entity_concept: R 93 / P 93 / F 93
a_granularity: R 93 / P 93 / F 93
b_event_sense: R 89 / P 89 / F 89
c_aspect: R 89 / P 94 / F 92
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 100 / P 40 / F 57
d_core_args_event: R 86 / P 80 / F 83
d_core_args_abstract: R 67 / P 80 / F 73
d_peripheral_event: R 93 / P 65 / F 76
d_peripheral_entity: R 100 / P 89 / F 94
e_core_labels: R 88 / P 88 / F 88
e_peripheral_labels: R 100 / P 100 / F 100
f_name_tokens: R 75 / P 75 / F 75
g_reentrancy: R 67 / P 80 / F 73
h_temporal: R 76 / P 76 / F 76
i_modal: R 70 / P 74 / F 72
j_coref_chain: R 17 / P 11 / F 13
j_coref_subset: R – / P 0 / F 0
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_event_concept | wrong | s11i2: identity -> 仍 | identity -> 仍
a_entity_found | missing | s11c: company -> - | no node in the prediction matches it
a_entity_found | missing | s11x5: 周报 -> - | no node in the prediction matches it
a_granularity | missing | «公司» 公司: «公司» 公司 -> «美国媒体公司» 公司 | inside a wider predicted node
a_granularity | missing | «周报» 周报: «周报» 周报 -> «《世界新闻周报》» newspaper | inside a wider predicted node
a_granularity | extra | «美国媒体公司» 公司: «公司» 公司 -> «美国媒体公司» 公司 | wider than the gold node
a_granularity | extra | «《世界新闻周报》» newspaper: «周报» 周报 -> «《世界新闻周报》» newspaper | wider than the gold node
d_core_args_event | partial | s11x: arg0 s11c/company; arg1 s11x8/发行-01 -> arg0 s11x6/公司; arg1 s11x8/发行-01 | missing arg0 s11c/company; extra arg0 s11x6/公司
d_core_args_abstract | missing | s11i2: arg1 s11c/company; arg2 s11x6/公司 -> - | missing arg1 s11c/company; missing arg2 s11x6/公司
d_peripheral_event | extra | s11x2: - -> mod s11i2/identity-91 | extra mod s11i2/identity-91
f_name_tokens | extra | s11x6: - -> 美国 媒体 公司 | gold has no :name
g_reentrancy | missing | s11x2/继续-01 -temporal-> s11d/date-entity: s11x2/继续-01 -temporal-> s11d/date-entity -> - | the prediction has no such edge
g_reentrancy | missing | s11x8/发行-01 -arg0-> s11c/company: s11x8/发行-01 -arg0-> s11c/company -> - | an end of the edge has no match in the prediction
g_reentrancy | extra | s11n/newspaper -part-> s11w/网络版: - -> s11n/newspaper -part-> s11w/网络版 | gold has no such reentrancy
a_entity_found | extra | s12p: - -> person | matches no gold node
a_entity_found | extra | s12d2: - -> 都 | matches no gold node
c_aspect | wrong | s12x:aspect: performance -> activity | performance -> activity
c_aspect | missing | s12i3:aspect: state -> - | the prediction has no :aspect
d_core_args_event | extra | s12x4: - -> arg0 s12p/person (not in gold) | extra arg0 s12p/person (not in gold)
g_reentrancy | missing | s12x5/标语 -possessor-> s12n/newspaper: s12x5/标语 -possessor-> s12n/newspaper -> - | the prediction has no such edge
g_reentrancy | missing | s12x6/报导-01 -quote-> s12i3/identity-91: s12x6/报导-01 -quote-> s12i3/identity-91 -> - | the prediction has no such edge
g_reentrancy | extra | s12s/标语 -possessor-> s12p/person: - -> s12s/标语 -possessor-> s12p/person | gold has no such reentrancy
a_entity_concept | wrong | s13i2: individual-person -> name | individual-person -> name
a_entity_concept | wrong | s13i3: individual-person -> 蝙蝠 | individual-person -> 蝙蝠
a_granularity | missing | «P» individual-person/individual-person/person: «P» individual-person/individual-person/person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person/individual-person/person -> «P'Lod» 外星人 | wider than the gold node
c_other_attributes | extra | s13i2:op1: - -> p | gold has no :op1
c_other_attributes | extra | s13i2:op2: - -> ' | gold has no :op2
c_other_attributes | extra | s13i2:op3: - -> lod | gold has no :op3
d_core_args_event | partial | s13x16: arg0 s13x13/人物; arg1 s13x18/中 -> arg0 s13x13/人物 | missing arg1 s13x18/中
d_peripheral_event | partial | s13x16: frequency s13x17/重复 -> frequency s13x17/重复; place s13x18/中 | extra place s13x18/中
e_core_labels | wrong | s13x16 -arg1-> s13x18: arg1 -> place | arg1 -> place
f_name_tokens | missing | s13i2: 蝙蝠 男孩 -> - | the prediction has no :name
f_name_tokens | missing | s13i3: 外星人 p ' lod -> - | the prediction has no :name
f_name_tokens | extra | s13n2: - -> p ' lod | gold has no :name
a_entity_found | missing | s14i2: implicit-argument -> - | no node in the prediction matches it
a_entity_concept | wrong | s14x3: 大 -> 大宗 | 大 -> 大宗
a_entity_concept | wrong | s14x2: 宗 -> thing | 宗 -> thing
b_event_sense | wrong | s14x6: 活动-01 -> 活动 | 活动-01 -> 活动
d_core_args_event | wrong | s14x: arg0 s14i2/implicit-argument; arg1 s14x6/活动-01 -> arg1 s14x2/宗; arg2 s14x6/活动-01 | missing arg0 s14i2/implicit-argument; arg1 s14x6/活动-01: predicted as arg2; extra arg1 s14x2/宗
d_core_args_abstract | wrong | s14h: arg1 s14i2/implicit-argument; arg1 s14x3/大; arg2 s14x4/最; arg5 s14x5/其中 -> arg1 s14x2/宗; arg2 s14x3/大; arg3 s14x4/最 | missing arg1 s14i2/implicit-argument; arg1 s14x3/大: predicted as arg2; arg2 s14x4/最: predicted as arg3; missing arg5 s14x5/其中; extra arg1 s14x2/宗
d_peripheral_entity | extra | s14x2: - -> mod s14x5/其中 | extra mod s14x5/其中
e_core_labels | wrong | s14x -arg1-> s14x6: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s14h -arg1-> s14x3: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s14h -arg2-> s14x4: arg2 -> arg3 | arg2 -> arg3
a_entity_found | extra | s15h: - -> 还 | matches no gold node
a_entity_found | extra | s15j: - -> 就 | matches no gold node
a_granularity | missing | «P» individual-person: «P» individual-person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person -> «P'Lod» 外星人 | wider than the gold node
b_event_sense | wrong | s15x2: 领养 -> 领养-01 | 领养 -> 领养-01
d_peripheral_event | extra | s15x: - -> mod s15j/就 (not in gold) | extra mod s15j/就 (not in gold)
d_peripheral_event | extra | s15x2: - -> mod s15h/还 (not in gold) | extra mod s15h/还 (not in gold)
h_temporal | wrong | 报导-01 «报导» (snt12 s12x10 = pred s12r3): 报导-01 «报导» (snt12 s12x4 = pred s12r) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12r3) -> 宣称-01 «宣称» (snt12 s12x = pred s12x) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12r3) | right relation, wrong parent
h_temporal | wrong | 报导-01 «报导» (snt12 s12x6 = pred s12r2): 报导-01 «报导» (snt12 s12x4 = pred s12r) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12r2) -> 宣称-01 «宣称» (snt12 s12x = pred s12x) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12r2) | right relation, wrong parent
h_temporal | extra | 出现-01 «出现» (snt13 s13x16 = pred s13x): - -> 创造-01 «创造» (snt13 s13x = pred s13c) :after 出现-01 «出现» (snt13 s13x16 = pred s13x) | gold gives this node no temporal parent
h_temporal | missing | 航天员 «航天员» (snt13 s13x6 = pred s13h): 创造-01 «创造» (snt13 s13x = pred s13c) :overlap 航天员 «航天员» (snt13 s13x6 = pred s13h) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 算是-01 «算是» (snt14 s14x = pred s14x): document-creation-time :before 算是-01 «算是» (snt14 s14x = pred s14x) -> document-creation-time :overlap 算是-01 «算是» (snt14 s14x = pred s14x) | right parent, wrong relation
i_modal | missing | have-mod-91 (snt12 s12h = pred s12h): author :full-affirmative have-mod-91 (snt12 s12h = pred s12h); newspaper (snt12 s12n = pred s12n) :full-affirmative have-mod-91 (snt12 s12h = pred s12h) -> - | the prediction gives this node no modal parent
i_modal | partial | 报导-01 «报导» (snt12 s12x10 = pred s12r3): author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12r3); newspaper (snt12 s12n = pred s12n) :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12r3) -> author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12r3) | agrees on part of the relations
i_modal | partial | 报导-01 «报导» (snt12 s12x4 = pred s12r): author :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12r) -> author :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12r); newspaper (snt12 s12n = pred s12n) :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12r) | agrees on part of the relations
i_modal | partial | 报导-01 «报导» (snt12 s12x6 = pred s12r2): author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12r2); newspaper (snt12 s12n = pred s12n) :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12r2) -> author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12r2) | agrees on part of the relations
i_modal | wrong | 算是-01 «算是» (snt14 s14x = pred s14x): author :neutral-affirmative 算是-01 «算是» (snt14 s14x = pred s14x) -> author :full-affirmative 算是-01 «算是» (snt14 s14x = pred s14x) | right parent, wrong relation
i_modal | missing | and (snt15 s15a = pred s15a): author :full-affirmative and (snt15 s15a = pred s15a) -> - | the prediction gives this node no modal parent
i_modal | extra | individual-person «P» (snt15 s15i2 = pred s15p): - -> author :full-affirmative individual-person «P» (snt15 s15i2 = pred s15p) | gold gives this node no modal parent
i_modal | wrong | 领养 «领养» (snt15 s15x2 = pred s15l): and (snt15 s15a = pred s15a) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) -> author :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l); individual-person «P» (snt15 s15i2 = pred s15p) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) | right relation, wrong parent
i_modal | wrong | 有-03 «有» (snt15 s15x3 = pred s15y): and (snt15 s15a = pred s15a) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) -> author :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y); individual-person «P» (snt15 s15i2 = pred s15p) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) | right relation, wrong parent
j_coref_chain | partial | newspaper (snt11 s11n2 = pred s11n): 周报 «周报» (snt11 s11x5); newspaper (snt12 s12n = pred s12n); person «P» (snt13 s13p = pred s13p) -> newspaper (snt12 s12n = pred s12n) | not linked to: 周报 «周报» (snt11 s11x5); person «P» (snt13 s13p = pred s13p)
j_coref_chain | missing | 周报 «周报» (snt11 s11x5): newspaper (snt11 s11n2 = pred s11n); newspaper (snt12 s12n = pred s12n); person «P» (snt13 s13p = pred s13p) -> - | the prediction has no node for it (its sentence graph lacks it)
j_coref_chain | extra | ?person (snt12 s12p): - -> person «P» (snt13 s13p = pred s13p) | a predicted node that matches nothing in gold
j_coref_chain | partial | newspaper (snt12 s12n = pred s12n): newspaper (snt11 s11n2 = pred s11n); 周报 «周报» (snt11 s11x5); person «P» (snt13 s13p = pred s13p) -> newspaper (snt11 s11n2 = pred s11n) | not linked to: 周报 «周报» (snt11 s11x5); person «P» (snt13 s13p = pred s13p)
j_coref_chain | extra | name (snt13 s13n2 = pred s13al): - -> 外星人 «外星人» (snt15 s15x11 = pred s15w) | gold links it to nothing
j_coref_chain | wrong | person «P» (snt13 s13p = pred s13p): newspaper (snt12 s12n = pred s12n); newspaper (snt11 s11n2 = pred s11n); 周报 «周报» (snt11 s11x5) -> ?person (snt12 s12p) | linked to another chain than gold's
j_coref_chain | extra | 外星人 «外星人» (snt15 s15x11 = pred s15w): - -> name (snt13 s13n2 = pred s13al) | gold links it to nothing
j_coref_subset | extra | 宗 «最大宗» (snt14 s14x2 = pred s14t) :subset-of 题材 «题材» (snt13 s13x4 = pred s13t): - -> 宗 «最大宗» (snt14 s14x2 = pred s14t) :subset-of 题材 «题材» (snt13 s13x4 = pred s13t)

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.