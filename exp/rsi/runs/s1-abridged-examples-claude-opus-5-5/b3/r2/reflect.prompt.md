<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29600). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

# The current instruction
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

# The critique (training batch 3: chinese_umr-0001, sentences 11-15; AnCast++ comprehensive 76.9)
<critique>
Below are the error patterns, most costly first. For each one: the cost, why it happened, and what to change in the instruction.

## 1. 他们 standing for the newspaper became a new `person` node
**Cost:** the biggest single loss. It accounts for most of j_coref_chain (F 13) and adds 2 units each in a_entity_found, g_reentrancy and d_core_args, plus temporal and modal parents tied to that node.

**Examples:**
- snt12 他们的报导 / 他们的标语
  - Annotation: a new `(s12p / person :refer-person 3rd :refer-number plural)`, used as `:ARG0` of 报导 and as `:possessor` of 标语.
  - Gold: no `:ARG0` on the first 报导 (`(s12x4 / 报导-01 :aspect habitual)`), and `(s12x5 / 标语 :possessor s12n)`, where s12n is the 《世界新闻周报》 node.
- snt13 他们经常报导
  - Annotation: `(s12p :same-entity s13p)`.
  - Gold: `(s12n :same-entity s13p)`. The chain runs from the newspaper to the pronoun.

**Why:** Section 2.4 says a pronoun is always `person`/`thing` with person and number. Nothing says what to do when 他们/它 refers back to an organisation or publication.

**Change:** add to 2.4 and 5.3:
- "When 他们/它/其 refers to an organisation or publication already mentioned in the same sentence, do not make a new node. Use that entity's variable (`标语 :possessor s12n`). A possessive 他们的 in front of an event noun adds no `:ARG0`."
- "In a later sentence the pronoun is its own `person` node, but its coreference goes to the named entity (`(s12n :same-entity s13p)`), not to an earlier pronoun node."

## 2. 其中最大宗可算是外星人地球活动 (snt14): roles, modal strength and tense all wrong
**Cost:** about 14 units across d_core_args (event and abstract), e_core_labels ×3, a_entity, b_event_sense, i_modal, h_temporal and j_coref_subset.

**What went wrong:**
- **算是 roles.** The annotation had `算是 :ARG1 thing :ARG2 活动`. PropBank 算是-01 has `ARG0` = the entity described and `ARG1` = what it counts as.
  - Gold: `(算是-01 :ARG0 (implicit-argument :ARG1-of (have-degree-91 :ARG1 (大) :ARG2 (最) :ARG5 (其中)) :unit (宗)) :ARG1 (活动-01 …))`.
- **Modal strength.** 可 was ignored, giving `(author :full-affirmative s14x)`. Gold has `(author :neutral-affirmative s14x)`.
- **Temporal relation.** The annotation had `(document-creation-time :overlap s14x)`. Gold has `:before`.
- **Sense.** 活动 was written with no sense. Gold has `活动-01`; it is in PropBank.
- **Extra subset link.** The annotation added `(s14t :subset-of s13t)`. Gold has no such triple.

**Why:**
- The rule that modal verbs "are not nodes" was followed, but the second half, that they change modal strength, was not applied to 可.
- Rule 2.3 tells the annotator to look up lexical verbs, but the annotator did not check 算是's role numbers.
- The 5.1 rule "a sentence that sums up the earlier text is anchored to document-creation-time" gives no relation, so the annotator picked `:overlap`.
- Section 2.1 tells the annotator to annotate event nominals as events, but does not say they still take their PropBank sense.

**Change:**
- In 5.2, add: "可/能/可以 before a predicate (可算是) make that predicate `neutral-affirmative` from the author."
- In 5.1, change the summing-up rule to: "…is `(document-creation-time :before X)` in a past-tense narrative document."
- In 3, add: "算是-01: `:ARG0` = the thing described, `:ARG1` = what it counts as."
- Add: "其中最 + noun with no head noun → `implicit-argument` with `have-degree-91 :ARG1 <adj> :ARG2 (最) :ARG5 (其中)`; a classifier such as 宗 is `:unit`."
- In 2.1, add: "an event nominal that has a PropBank frame takes its sense (活动-01)."
- In 5.3, add: "No `:subset-of` link from a 其中 phrase."

## 3. 母公司美国媒体公司 and the short 周报 mention (snt11)
**Cost:** about 12 units across a_entity_found, a_granularity ×4, d_core_args, d_core_args_abstract, f_name_tokens, g_reentrancy ×3 and j_coref.

**What went wrong:**
- **The company.** The annotation had `(公司 :mod 母 :name "美国" "媒体" "公司")`.
  - Gold: `(s11c / company :name … :ARG1-of (identity-91 :ARG2 (公司 :mod (母))))`.
- **The short mention 周报.** 周报的网络版 was written `:part-of s11n`, a re-entrancy to the full 《世界新闻周报》 node.
  - Gold: a separate `(s11x5 / 周报)` node, plus `(s11n2 :same-entity s11x5)` in the coreference list.
- **Missing `:ARG0` on 发行.** Gold has `发行 :ARG0 s11c`. The instruction's own control rule (它停止了它的发行 → 发行 `:ARG0` 它) covers this, but the annotator did not apply it.
- **Shared date.** Gold has `继续 :temporal s11d`: the sentence-initial date also scopes the second clause.

**Why:**
- The apposition rule in 3 only covers common noun + 《name》, so a role noun before an organisation name was merged into it.
- The "refer to it by its bare variable" rule in 3 and "within one sentence, coreference is a re-entrancy" in 5.3 directly caused the 周报 merge.

**Change:**
- Extend the apposition rule: "<role noun> + <organisation name> (母公司美国媒体公司) → entity-type node (`company`) with the name, plus `:ARG1-of (identity-91 :ARG2 <role noun>)`."
- Qualify the re-entrancy rule: "A shortened repeat of a name (周报 after 《世界新闻周报》) is its own node with the bare word as its concept, linked by an in-sentence `:same-entity` triple. Use re-entrancy only for pronouns and for exact repeats."
- Add: "A sentence-initial date shared by both clauses of 不过/但 goes on both main events as `:temporal`."
- Restate the control rule next to 停止/开始 + 的 + event noun.

## 4. Modal and temporal structure of reported content (snt12, snt15)
**Cost:** about 9 units: i_modal ×7 and h_temporal ×2.

**snt12:**
- **Conceiver on the wrong node.** The annotator gave the conceiver triple to the inner 报导 (`s12n :full-affirmative s12r`).
  - Gold puts it on the top node of the quoted content, `(s12n :full-affirmative s12h)` (the have-mod-91).
  - Gold also adds `(author :full-affirmative s12h)`, plus `(s12n :full-affirmative …)` on the slogan's 报导 and on the 大部分的报导 clause.
- **Slogan identity-91.** It needs `:aspect state`, and its 报导 needs `:quote s12i3`.
- **Temporal parents.** The other content events should hang from the first content event, `(s12x4 :overlap s12x6) (s12x4 :overlap s12x10)`, not from 宣称. The instruction already says this; the annotator did not follow it.

**snt15:**
- **Conceiver of 被指.** Gold's conceiver is the coordinated subject `s15a` (the `and` node), with `(author :full-affirmative s15a)`. The annotator used Hillary alone (s15p).

**Change:**
- In 5.2: "The conceiver triples go on the top node of the content: the node that carries `:quote`, even an abstract predicate. Give that node both `author` and conceiver triples."
- "For 被指 the conceiver is the whole subject node of the content's first event (the `and` node when it is coordinated)."
- "A quoted slogan is `identity-91 :aspect state`, and its inner event carries `:quote` that identity-91."
- "宣称 as a past claim is `performance`, not `activity`."

## 5. Named fictional characters in a 如…等 list (snt13)
**Cost:** about 9 units: f_name_tokens ×3, a_entity_concept ×2, a_granularity, c_other_attributes ×3 (the main reason its precision is 40), plus an extra coreference link.

**What went wrong:**
- 蝙蝠男孩 was written `(男孩 :mod 蝙蝠)`. Gold has `(individual-person :name (name :op1 "蝙蝠" :op2 "男孩"))`.
- 外星人P'Lod was written `(外星人 :name "P" "'" "Lod")`. Gold has `(individual-person :name (name :op1 "外星人" :op2 "P" :op3 "'" :op4 "Lod"))`.

**Why:** The instruction's own rule "外星人 P'Lod is no apposition: (外星人 :name …)" fits gold in snt15 but not in this list. Gold is not consistent here.

**Change:** limit that rule: "In a list of example characters (如 A、B 等), each character is `individual-person` with the whole written name, the descriptor included (`:op1 "外星人" :op2 "P" …`). Use `(外星人 :name …)` only in running narrative." Also: "Do not corefer mentions whose node types differ in this way unless the text makes them the same." Gold does not link snt13's P'Lod to snt15's.

## 6. Extra adverb nodes
**Cost:** about 6 units across a_entity_found, d_peripheral_event and a_event_concept.

**What went wrong:**
- snt15: 就 and 还 (后来还领养) were added as `:mod`.
- snt12: the 都 of 都以…为目的 was added as `:mod`.
- snt11: 仍 was added as `:mod`.

Gold omits all of these. Gold does keep the 都 in 都是真实的 and 甚至.

**Change:** narrow the adverb list in 3: "Focus particles 就 and additive 还 after 后来 are not annotated. 仍 next to 继续 is redundant and gets no node. Keep 都 only when it quantifies the subject of a copular predicate."

## 7. Smaller problems
- **出现's location (snt13).** 在他们的新闻中 was written as `:place`. Gold uses a numbered argument: `出现 :ARG1 (中 :op1 新闻)`. Change: "A location role in a 出现/在…中 frame is a numbered argument; look up the frame." (PropBank lists the location as ARG0, but gold uses ARG1.)
- **Temporal parent in snt13.** `(s13c :after s13x)` was extra. Events inside a relative clause on the created object should be `:overlap`, or follow gold.

## What to keep
- Event detection (a_event_found 100) and person/number attributes (c_refer 100).
- The clause-level structures: `but-91` with `and`, `identity-91` with `目的 :purpose-of`, `consecutive` with `:quote` on both content events, and `:example (and … (等))` lists.
- The control re-entrancy for 继续生存.
- `individual-person` plus `have-rel-role-91 :ARG3 (第一夫人 :mod 前 :place country)`.
- The date chain `(document-creation-time :before date)(date :overlap 停止)` and `(有 :after 领养)`.
- 领养-01: PropBank has this sense. Gold's 领养-00 is a gold slip, so do not change the "look the verb up first" rule.
</critique>

# Earlier edits
- batch 1, reflection 1 (10/10 edits applied): Fix temporal chaining (anchor one main event, chain others with :overlap, no parent for copular -91 predicates, relative time words depend on DCT); Chinese classifiers as :unit; adverbs as :mod nodes; Chinese name brackets, no wiki, :place/:medium; aspect cues (habitual institutional activity, 已经+stop = state, 被称为 = performance); :reason for 因为/由于/以…而; 不过/可是 → but-91; distribute modifiers over con -> AnCast++ comp 84.8 on the batch, kept
- batch 1, reflection 2 (9/9 edits applied): Fix the 目前 temporal rule and its wrong example; add copular-root anchoring and governing-event rules; restrain coreference; narrow the 已经+end-verb state cue; add role rules (:part-of for editions, ARG0 for intransitive -00 verbs, no borrowed subjects, identity-91 for event-noun heads); keep compound verbs whole, 历史上 as :temporal, no aspect on have-degree-91; modal triple for root abstract predicat -> AnCast++ comp 94.6 on the batch, kept
- batch 1, reflection 3 (9/9 edits applied): Fix 曾经 temporal handling and stative aspect with 过; no :polarity on 未经 and no performance for negated events; 停刊-01 not -00; :part-of only with an expressed whole; :aspect state on root abstract predicates; :depends-on for naming clauses; partial-affirmative for usual-procedure nominals under negation; update examples. -> AnCast++ comp 100.0 on the batch, kept
- batch 2, reflection 1 (13/13 edits applied): Fix date anchoring (DCT :before date, date :overlap event), reason/purpose temporal order, cross-sentence anchoring; add have-reason-91/have-purpose-91 for paired clause connectives; apposition with identity-91, 由X改为Y roles, part-of objects, role nouns, 量 measure nouns with have-quant-91, middle dot in names, :era for 年代, 该刊; stronger no-invented-arguments rule; Chinese PropBank role numbering for -> AnCast++ comp 95.7 on the batch, kept
- batch 2, reflection 2 (7/7 edits applied): Fix 由X改为Y with a topic subject (:part-of on X, no :ARG0) and the full-build-at-first-mention re-entrancy rule; V+量 inner verb gets no aspect/modal; purpose events are activity, habitual cue narrowed (relative clause of founded thing = process); named humans are individual-person in Chinese; update examples and checklist. -> AnCast++ comp 100.0 on the batch, kept
- batch 2, reflection 3 (2/2 edits applied): Resolve the contradictory re-entrancy rule: build a repeated entity in full at its first mention in the sentence's word order, even when that branch is written later in PENMAN (e.g. under have-reason-91 :ARG2); annotate the 改为 example accordingly. -> AnCast++ comp 98.9 on the batch, not kept (the best was 100.0)
- batch 3, reflection 1 (17/17 edits applied): Add rules for reported-content temporal/modal/:quote, contrast overlap, summary sentences anchored to DCT, 虽然…不过 but-91, 以X为目的, parenthetical slogans, consecutive for 后来, control-verb re-entrancy exception, connectives without modal, 有/如…等 :example lists, :frequency, 有-03 relationships, 指-02/算是-01, title-before-name, planet, 母公司 split, 前 :mod, aspect of nominal under 停止 and 生存; trim redundant exam -> AnCast++ comp 76.9 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.