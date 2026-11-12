<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29921). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

# The current instruction
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

# The critique (training batch 4: chinese_umr-0001, sentences 16-20; AnCast++ comprehensive 48.7)
<critique>
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

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.