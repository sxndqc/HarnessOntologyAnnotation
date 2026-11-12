<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 27979). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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
- Do not guess when you can check: the answer to almost every question is in the guidelines above and
  their examples; look it up there rather than answer from memory.
- Before you go on to the next sentence, check the graph against the guidelines once more: every word
  that carries meaning has its concept, every event its aspect, every role the right direction; and at
  the end check that the document-level relations cover every event and entity the guidelines ask for.

## Guidelines

# UMR guidelines, abridged

A short version of the UMR 0.9 specification (`umr_guidelines.md` in this folder, umr4nlp/umr-guidelines),
for annotating Chinese and English at Stage 1 (numbered PropBank roles). It keeps what an annotator needs for
most sentences and leaves out the typological material, the fine-grained lattices, the field-linguistics
sections and most of the examples. Where the full guideline uses the older short names (`AUTH`, `DCT`,
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
`disease`, `product`, `spaceship`, ... (as in AMR).

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
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.
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
- Do not add arguments (agents, possessors, organizations) that the text does not express. Never re-use a participant from elsewhere in the sentence as an unexpressed agent or possessor: every re-entrancy needs a pronoun or an overt word. 旗下 is `:mod (旗下)`, not a possessor. Do not fill the subject of a later clause with an entity from an earlier clause (…，不过仍继续发行网络版: 发行 has no `:ARG0`).
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
- A demonstrative + abbreviated noun keeps the word as its concept (该刊 → `(刊 :mod (该))`, not `newspaper`).

Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. The
UMR release data also marks it with `:quote <reporting event>` when the content is a quotation.

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

Aspect cues: a publication's or institution's own recurring verbs (发行, 报导, 综合, 印刷) used as predicates are `habitual`, even with 了; this cue does not extend to other verbs. A relative clause describing what a newly founded thing was designed to do (容纳…文章的版面) is `process`. A purpose event (为/为了 X, `have-purpose-91 :ARG2`, `:purpose`) is `activity`, not `performance`, even when it is modally full-affirmative. 已经 + 停止 or another end verb is `state` only inside a relative clause that describes an entity (已经停止发行的小报); as the main predicate, 已经 + an end verb (已经停刊) is `performance`. Passive naming (被称为) is `performance`. Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂. A negated event (未, 没) never gets `performance`; use `process` when its type cannot be told.

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
- A sentence with no time expression that continues the previous sentence's episode hangs its main event from that sentence's main event (`(s7x :overlap s8x)`), not from `document-creation-time`.
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
- Reported speech or thought: the author is certain of the speaker, the speaker of the content:
  `(author :full-affirmative s9p)` `(s9p :full-affirmative s9s3)`, where `s9p` is the speaker (a person
  node, or an event used as conceiver).
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
- Root copula (2.3): 是…小报 → `(identity-91 :ARG1 … :ARG2 … :aspect state)`.
- Naming (5.1): 被称为… → `(document-creation-time :depends-on 称为)`.
- Degree (2.3): 美国历史上最…的报纸 → `(报纸 :temporal (上 :op1 (历史 :place (country …))))`, `have-degree-91` without aspect; 称为 → `称为-01`.
- Classifier (2.2): 一个节目 → `(节目 :quant 1 :unit (个))`.
- Adverb (3): 已经停止 → `(停止-01 :mod (已经) :aspect state)`; 曾经 → `:temporal (曾经)`.
- Name (2.2): 美国…小报 → `(小报 :place (country :name (name :op1 "美国")))`, with no `:wiki`.
- Reason (2.5): 以报导…而闻名 → `(闻名-01 :reason (报导-01 ...))`.
- Lexical verb (2.3): 节目属周报 → `(属-02 :ARG0 节目 :ARG1 周报)`, not `belong-91`.
- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`.

- Date (5.1): 1980年代…改为 → `(document-creation-time :before s9d) (s9d :overlap s9x)`, `(date-entity :era 1980)`.
- Clause links (2.5): 因为 X，为 Y，于是 Z → `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state) :ARG2 改为 :aspect state)`; temporal `(创立 :overlap 运用) (创立 :before 改为)`.
- Apposition (3): 旗下的八卦小报《国家询问报》 → `(newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 :mod (旗下) :mod (八卦))))`.
- 改为 (3): 小报《…》将由黑白版面改为彩色版面 …不符合《…》标准 → `(改为-01 :ARG1 (版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 …))) :mod (黑白)) :ARG2 (版面 :mod (彩色)))`, no `:ARG0`; later `(标准 :possessor s7n)`.
- Measure noun (2.2): 发行量达到120万份 → `(达到-01 :ARG0 (量 :quant-of (发行-01 :ARG1 …) :ARG1-of (have-quant-91 :ARG2 1200000 :unit (份))) :aspect performance)`, `(达到 :overlap 发行)`.
- Roles (3): 黑白印刷也成了该刊的特色 → `(成-01 :ARG0 (印刷-01 :manner (黑白) :aspect habitual) :ARG1 (特色 :poss… (刊 :mod (该))))`; temporal from previous sentence's main event.

- Aspect (4.1): 为充分运用… → `运用 :aspect activity`; 容纳…文章的版面 → `(版面 :ARG0-of (容纳-01 … :aspect process))`.
- V+量 (2.2): 发行量 → `(量 :quant-of (发行-01 :ARG1 …))` with no `:aspect` and no modal triple; only `(达到 :overlap 发行)`.
- Named person (2.2): 格内洛索·波普 → `(individual-person :name (name :op1 "格内洛索" :op2 "·" :op3 "波普"))`.

</instruction>

# The critique (training batch 2: chinese_umr-0001, sentences 6-10; AnCast++ comprehensive 100.0)
<critique>
The annotation matches gold on every check except two, and both come from one wrong decision in sentence 7. The other 19 checks are at 100%.

## Problem 1: in sentence 7, the repeated entity was written out in full at the wrong mention (the only cost)

**Cost:** 4 units in total.
- **d_peripheral_entity** dropped to F 91, with 2 units lost: one extra `标准 :possessor` edge and one missing `newspaper :part 版面` edge.
- **g_reentrancy** dropped to R 0 / P 0, with 2 units lost: gold's one re-entrancy was missing and the annotation had an extra one instead.

**What happened.** 《国家询问报》 appears twice in sentence 7:
- first in the 因为 clause (旗下的八卦小报《国家询问报》将由黑白版面改为彩色版面, words 6–14);
- again near the end (不符合《国家询问报》标准, words 48–52).

The annotator wrote the full node (the name plus the apposition `identity-91 :ARG2 (小报 :mod 旗下 :mod 八卦)`) under 标准, the later mention. It then pointed back to it from 改为:

```
:ARG1 (s7h2 / have-purpose-91 :ARG1 (s7x / 创立-01 ...
        (s7s / 标准 :possessor (s7n / newspaper :name (...) :ARG1-of (s7id / identity-91 :ARG2 (s7k / 小报 ...))))
...
:ARG2 (s7g / 改为-01 :ARG1 (s7v / 版面 :part-of s7n ...))
```

Gold writes it in full at the first mention in reading order, under 改为, and 标准 points back to it:

```
:ARG2 (s7x / 改为-01
    :ARG1 (s7x4 / 版面
        :part-of (s7n / newspaper :name (s7n2 / name :op1 "《" :op2 "国家" :op3 "询问" :op4 "报" :op5 "》")
                    :ARG1-of (s7i2 / identity-91 :ARG2 (s7x5 / 小报 :mod (s7x6 / 旗下) :mod (s7x7 / 八卦))))
        :mod (s7x16 / 黑白)) ...)
...
(s7x21 / 标准 :possessor s7n)
```

**Why it happens.** The instruction's rule is self-contradictory in exactly this situation: "Build a repeated entity in full … at its first mention in the graph (first in reading order)". Because of `have-reason-91`, the 创立 branch (`:ARG1`) is written before the 改为 branch (`:ARG2`) in the PENMAN graph, even though the 改为 clause comes first in the text. So "first in the graph" points to 标准 and "first in reading order" points to 改为. The annotator chose graph order. The 改为 example in the instruction does show the gold pattern (`改为 :ARG1 (版面 :part-of (s7n / newspaper … identity-91 …))`, later `(标准 :possessor s7n)`), but it doesn't say this holds even when the 改为 branch is written last.

**Change to the instruction.** In section 3, replace the rule with something like:

> Build a repeated entity in full (name, apposition, modifiers) at the mention that comes **first in the sentence's word order**, even when that mention's branch is written later in the PENMAN graph (for example under `have-reason-91 :ARG2`). Every other mention, including ones in branches written earlier in the graph, is the bare variable. So in 因为《X》将由…改为…，…于是创立…，容纳不符合《X》标准的文章, the full node goes under 改为 (`版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 …))`) and 标准 gets `:possessor s7n`.

Also add the same note to the 改为 example: "although 改为 is `:ARG2` of `have-reason-91` and is written last, it holds the full node."

## What to keep

Everything else matched gold exactly, and these rules should stay as written:
- **Clause structure:** `have-reason-91` / `have-purpose-91` nesting with `:aspect state` and full-affirmative modals; the purpose event 运用 as `activity`; 遗留 ordered before 运用 (`:before`); 改为 with no `:ARG0` and the subject attached through `:part-of`.
- **Entities and words:** the apposition pattern with `identity-91`; `individual-person` with the middle dot as its own `:opN`; the 创始人 → `have-org-role-91` + `创始-00` pattern; 该刊 → `(刊 :mod (该))`; 黑白印刷 with `:manner` and `habitual`; 成-01 taking the theme as `:ARG0`.
- **V+量 compounds:** 发行量 built as `量 :quant-of 发行-01 :ARG1-of have-quant-91`, with no aspect or modal triple on 发行 and only `(达到 :overlap 发行)` as its temporal link.
- **Time and adverbs:** dates as `(document-creation-time :before date)` then `(date :overlap event)`, including `:era 1980`; 已经 as `:mod`; sentence 8 hanging from the previous sentence's main event.
- **Modal and coreference:** the 未经/不符合 negation handled as `:polarity -` with `full-negative`; coreference chained across sentences to the nearest earlier mention (周报 → 该刊 → 《…周报》 → 该刊), with no extra links.
</critique>

# Earlier edits
- batch 1, reflection 1 (10/10 edits applied): Fix temporal chaining (anchor one main event, chain others with :overlap, no parent for copular -91 predicates, relative time words depend on DCT); Chinese classifiers as :unit; adverbs as :mod nodes; Chinese name brackets, no wiki, :place/:medium; aspect cues (habitual institutional activity, 已经+stop = state, 被称为 = performance); :reason for 因为/由于/以…而; 不过/可是 → but-91; distribute modifiers over con -> AnCast++ comp 84.8 on the batch, kept
- batch 1, reflection 2 (9/9 edits applied): Fix the 目前 temporal rule and its wrong example; add copular-root anchoring and governing-event rules; restrain coreference; narrow the 已经+end-verb state cue; add role rules (:part-of for editions, ARG0 for intransitive -00 verbs, no borrowed subjects, identity-91 for event-noun heads); keep compound verbs whole, 历史上 as :temporal, no aspect on have-degree-91; modal triple for root abstract predicat -> AnCast++ comp 94.6 on the batch, kept
- batch 1, reflection 3 (9/9 edits applied): Fix 曾经 temporal handling and stative aspect with 过; no :polarity on 未经 and no performance for negated events; 停刊-01 not -00; :part-of only with an expressed whole; :aspect state on root abstract predicates; :depends-on for naming clauses; partial-affirmative for usual-procedure nominals under negation; update examples. -> AnCast++ comp 100.0 on the batch, kept
- batch 2, reflection 1 (13/13 edits applied): Fix date anchoring (DCT :before date, date :overlap event), reason/purpose temporal order, cross-sentence anchoring; add have-reason-91/have-purpose-91 for paired clause connectives; apposition with identity-91, 由X改为Y roles, part-of objects, role nouns, 量 measure nouns with have-quant-91, middle dot in names, :era for 年代, 该刊; stronger no-invented-arguments rule; Chinese PropBank role numbering for -> AnCast++ comp 95.7 on the batch, kept
- batch 2, reflection 2 (7/7 edits applied): Fix 由X改为Y with a topic subject (:part-of on X, no :ARG0) and the full-build-at-first-mention re-entrancy rule; V+量 inner verb gets no aspect/modal; purpose events are activity, habitual cue narrowed (relative clause of founded thing = process); named humans are individual-person in Chinese; update examples and checklist. -> AnCast++ comp 100.0 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.