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
in PropBank is `<word>-00`. Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :wiki "Russia" :name (n / name :op1 "Russia"))`: an entity-type concept, an optional `:wiki`
(the Wikipedia title, or `-` when there is none), and `:name` with one `:opN` per word of the name.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`.
In Chinese names keep the title brackets 《 》 as their own `:opN` (《世界新闻周报》 → `:op1 "《" :op2 "世界" ... :opN "》"`). Do not add `:wiki` in Chinese documents. A country or place name that modifies a noun (美国小报) is `:place`, not `:mod`. Do not corefer a repeated country name that is only such a modifier. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
a classifier is kept as the unit too, including 个, 份, 款, 本 (一份小报 → `小报 :quant 1 :unit (份)`).

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

When the text has a lexical verb that is in Chinese PropBank (属, 拥有), use that verb with its frame's roles instead of `belong-91` / `have-91`. Superlatives and comparatives (最, 更, *most, more*) use `(have-degree-91 :ARG1 X :ARG2 <property> :ARG3 (最))`, not `:degree`.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过, 可是) `but-91`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) and 以…而 → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.

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
- Do not add arguments (agents, possessors) that the text does not express or clearly imply.
- In 'X 是 … Y，以 … 而 V' the second predicate modifies Y: `Y :ARG1-of (V :reason ...)`. Do not add a coordinating `and`.

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

Aspect cues: recurring activities of a publication or institution (发行, 报导, 综合) are `habitual`, even with 了. 已经 + 停止 or another end verb used to describe an entity is `state` (the resulting state). Passive naming (被称为) is `performance`.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2).
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
- Time expressions first: an absolute date (*1998*) depends on `root`; a relative one (*today, yesterday*,
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`; a vague one
  (*nowadays*, 现在) on `past-reference` / `present-reference` / `future-reference`.
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :contained s1e)`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent; a purpose is `:after` its main event.
- Anchor only the **main event** of a sentence to `document-creation-time` (or to a time expression of its clause). Attach every other event of the sentence to that main event or to a nearby event, usually `:overlap` (`:contained` if it lies inside it, `:before`/`:after` when the order is clear). Events inside relative clauses, modifiers and event nominals also need a parent, normally their governing event with `:overlap`. Leave no event without a temporal parent.
- Copular abstract predicates (`identity-91`, `have-mod-91`, `have-*-91`) normally get **no** temporal parent.
- A relative time word such as 目前 or 现在 is a time node attached as `(document-creation-time :depends-on <node>)`. Do not attach it to `present-reference`. Then chain the events from it with `:overlap`.

### 5.2 Modal (`:modal`)

A dependency structure of conceivers and events: `(conceiver :strength event)`, starting with
`(root :modal author)` in every sentence that has events.

- Strength = the conceiver's certainty that the event happens or holds: `full-affirmative` (plain
  assertion, *will*), `partial-affirmative` (*probably, must, should*, 应该, 可能性大, 一定 as inference),
  `neutral-affirmative` (*may, might, perhaps, can*, 可能, 也许, 或许, desire/hope), `neutral-negative`,
  `partial-negative`, `full-negative` (negated: *not, never, deny*, 没, 不), `unspecified`.
- Every event the author asserts: `(author :full-affirmative s1e)`.
- Reported speech or thought: the author is certain of the speaker, the speaker of the content:
  `(author :full-affirmative s9p)` `(s9p :full-affirmative s9s3)`, where `s9p` is the speaker (a person
  node, or an event used as conceiver).
- An event under a modal or complement-taking predicate (*want, try, plan, decide, hope*, 想, 希望, 打算,
  决定, 需要): the predicate is asserted by the author, the complement has the predicate as parent with
  `unspecified` (or the strength the predicate implies): `(author :full-affirmative s3w)`
  `(s3w :unspecified s3g)`.
- A conceiver that is not in the text is `null-conceiver`. Purpose and condition clauses may use the
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

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect`; negated events have `:polarity -`.
- Every event and time expression has a temporal parent; every event has a modal parent.
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.

## Examples

- Temporal chain (5.1): 目前…发行…网络版 → `(document-creation-time :depends-on s4x) (s4x :overlap s4x2) (s4x2 :overlap s4x6)`. The other events of a sentence hang from its main event: `(document-creation-time :before s1x3) (s1x3 :overlap s1x4)`.
- Classifier (2.2): 一个节目 → `(节目 :quant 1 :unit (个))`.
- Adverb (3): 已经停止 → `(停止-01 :mod (已经) :aspect state)`; 曾经 → `:temporal (曾经)`.
- Name (2.2): 美国…小报 → `(小报 :place (country :name (name :op1 "美国")))`, with no `:wiki`.
- Reason (2.5): 以报导…而闻名 → `(闻名-01 :reason (报导-01 ...))`.
- Lexical verb (2.3): 节目属周报 → `(属-02 :ARG0 节目 :ARG1 周报)`, not `belong-91`.
- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`.

</instruction>

# The sentences
1	《 世界 新闻 周报 》 是 一份 已经 停止 发行 的 美国 超市 小报 ， 以 报导 奇闻 轶事 、 都 会 传奇 、 恶搞 新闻 而 闻名 。
2	该 周报 综合 了 各式各样 奇怪 的 新闻 与 专栏 ， 其中 许多 内容 都 未经 一般 的 新闻 查证 程序 。
3	该 周报 也 曾经 短暂 的 拥有 过 一个 属 自己 的 电视 节目 。
4	目前 《 世界 新闻 周报 》 的 纸本 已经 停刊 ， 不过 仍 继续 发行 网络版 。
5	由于 其 荒诞不经 的 内容 ， 该 周报 被 称为 美国 历史 上 最富 创意 的 报纸 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 《 世界 新闻 周报 》 是 一份 已经 停止 发行 的 美国 超市 小报 ， 以 报导 奇闻 轶事 、 都 会 传奇 、 恶搞 新闻 而 闻名 。

# sentence level graph:
(s1i / identity-91
    :ARG1 (s1n / newspaper
        :name (s1n2 / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :ARG2 (s1x / 小报
        :quant 1
        :unit (s1x2 / 份)
        :mod (s1x3 / 超市)
        :place (s1c / country
            :name (s1c2 / name
                :op1 "美国"))
        :ARG1-of (s1x4 / 发行-01
            :ARG1-of (s1x5 / 停止-01
                :mod (s1x6 / 已经)
                :aspect state)
            :aspect habitual)
        :ARG1-of (s1x7 / 闻名-01
            :reason (s1x8 / 报导-01
                :ARG0 s1x
                :ARG1 (s1a / and
                    :op1 (s1a2 / and
                        :op1 (s1x9 / 奇闻)
                        :op2 (s1x10 / 轶事))
                    :op2 (s1x11 / 传奇
                        :mod (s1x12 / 都会))
                    :op3 (s1x13 / 新闻
                        :mod (s1x14 / 恶搞)))
                :aspect habitual)
            :aspect state))
    :aspect state)


# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :overlap s1x5)
               (s1x5 :after s1x4)
               (document-creation-time :overlap s1x7)
               (s1x7 :overlap s1x8))
    :modal ((root :modal author)
            (author :full-affirmative s1x4)
            (author :full-affirmative s1x5)
            (author :full-affirmative s1x7)
            (author :full-affirmative s1x8)))


################################################################################
# meta-info
# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
Words: 该 周报 综合 了 各式各样 奇怪 的 新闻 与 专栏 ， 其中 许多 内容 都 未经 一般 的 新闻 查证 程序 。

# sentence level graph:
(s2a / and
    :op1 (s2x / 综合-01
        :ARG0 (s2x2 / 周报
            :mod (s2x3 / 该))
        :ARG1 (s2a2 / and
            :op1 (s2x4 / 新闻
                :mod (s2x5 / 各式各样)
                :mod (s2x6 / 奇怪))
            :op2 (s2x7 / 专栏
                :mod s2x5
                :mod s2x6))
        :aspect habitual)
    :op2 (s2x8 / 经-01
        :polarity -
        :ARG0 (s2x9 / 内容
            :quant (s2x10 / 许多)
            :mod (s2x11 / 其中))
        :ARG1 (s2x12 / 程序
            :mod (s2x13 / 查证-01
                :ARG1 (s2x14 / 新闻)
                :aspect process)
            :mod (s2x15 / 一般))
        :mod (s2x16 / 都)
        :aspect performance
        :modal-strength full-negative))


# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2x)
               (s2x :overlap s2x8)
               (s2x :overlap s2x13))
    :modal ((root :modal author)
            (author :full-affirmative s2x)
            (author :full-negative s2x8)
            (author :full-affirmative s2x13))
    :coref ((s1n :same-entity s2x2)
            (s2x9 :subset-of s2a2)))


################################################################################
# meta-info
# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 该 周报 也 曾经 短暂 的 拥有 过 一个 属 自己 的 电视 节目 。

# sentence level graph:
(s3x / 拥有-01
    :ARG0 (s3x2 / 周报
        :mod (s3x3 / 该))
    :ARG1 (s3x4 / 节目
        :quant 1
        :unit (s3x5 / 个)
        :medium (s3x6 / 电视)
        :ARG0-of (s3x7 / 属-02
            :ARG1 s3x2
            :aspect state))
    :mod (s3x8 / 也)
    :temporal (s3x9 / 曾经)
    :duration (s3x10 / 短暂)
    :aspect state)


# document level annotation:
(s3s0 / sentence
    :temporal ((document-creation-time :before s3x)
               (s3x :overlap s3x7))
    :modal ((root :modal author)
            (author :full-affirmative s3x)
            (author :full-affirmative s3x7))
    :coref ((s2x2 :same-entity s3x2)))


################################################################################
# meta-info
# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Words: 目前 《 世界 新闻 周报 》 的 纸本 已经 停刊 ， 不过 仍 继续 发行 网络版 。

# sentence level graph:
(s4b / but-91
    :ARG1 (s4x2 / 停刊-01
        :ARG1 (s4x3 / 纸本
            :possessor (s4n / newspaper
                :name (s4n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :mod (s4x4 / 已经)
        :temporal (s4x / 目前)
        :aspect state)
    :ARG2 (s4x5 / 继续-01
        :ARG1 (s4x6 / 发行-01
            :ARG0 s4n
            :ARG1 (s4x7 / 网络版)
            :aspect habitual)
        :mod (s4x8 / 仍)
        :aspect activity))


# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :depends-on s4x)
               (s4x :overlap s4x2)
               (s4x2 :overlap s4x5)
               (s4x5 :overlap s4x6))
    :modal ((root :modal author)
            (author :full-affirmative s4x2)
            (author :full-affirmative s4x5)
            (author :full-affirmative s4x6))
    :coref ((s3x2 :same-entity s4n)
            (s1x4 :same-event s4x6)))


################################################################################
# meta-info
# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Words: 由于 其 荒诞不经 的 内容 ， 该 周报 被 称为 美国 历史 上 最富 创意 的 报纸 。

# sentence level graph:
(s5x / 称-01
    :ARG1 (s5x2 / 周报
        :mod (s5x3 / 该))
    :ARG2 (s5x4 / 报纸
        :ARG1-of (s5h / have-degree-91
            :ARG2 (s5x5 / 富-01
                :ARG1 (s5x6 / 创意)
                :aspect state)
            :ARG3 (s5x7 / 最)
            :ARG4 (s5x8 / 历史
                :place (s5c / country
                    :name (s5c2 / name
                        :op1 "美国")))
            :aspect state))
    :reason (s5x9 / 内容
        :possessor s5x2
        :mod (s5x10 / 荒诞不经))
    :aspect performance)


# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :before s5x)
               (s5x :overlap s5x5))
    :modal ((root :modal author)
            (author :full-affirmative s5x)
            (author :full-affirmative s5x5))
    :coref ((s4n :same-entity s5x2)
            (s2x9 :same-entity s5x9)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt1
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Words: 《 世界 新闻 周报 》 是 一份 已经 停止 发行 的 美国 超市 小报 ， 以 报导 奇闻 轶事 、 都 会 传奇 、 恶搞 新闻 而 闻名 。

# sentence level graph:
(s1i2 / identity-91
    :ARG1 (s1n / newspaper
        :name (s1n2 / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :ARG2 (s1x / 小报
        :mod (s1x2 / 超市)
        :place (s1c / country
            :name (s1n3 / name
                :op1 "美国"))
        :ARG1-of (s1x3 / 发行-01
            :ARG1-of (s1x4 / 停止-01
                :mod (s1x6 / 已经)
                :aspect state)
            :aspect habitual)
        :quant 1
        :unit (s1x5 / 份)
        :ARG1-of (s1x7 / 闻名-01
            :reason (s1x8 / 报导-01
                :ARG0 s1x
                :ARG1 (s1a / and
                    :op1 (s1a2 / and
                        :op1 (s1x9 / 奇闻)
                        :op2 (s1x10 / 轶事))
                    :op2 (s1x11 / 传奇
                        :mod (s1x13 / 都会))
                    :op3 (s1x12 / 新闻
                        :mod (s1x14 / 恶搞)))
                :aspect habitual)
            :aspect state))
    :aspect state)


# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1x3)
               (s1x3 :overlap s1x4)
               (s1x7 :contained s1x3)
               (s1x3 :overlap s1x8))
    :modal ((root :modal author)
            (author :full-affirmative s1x4)
            (author :full-affirmative s1x3)
            (author :full-affirmative s1x8)
            (author :full-affirmative s1x7)
            (author :full-affirmative s1i2)))


################################################################################
# meta-info
# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
Words: 该 周报 综合 了 各式各样 奇怪 的 新闻 与 专栏 ， 其中 许多 内容 都 未经 一般 的 新闻 查证 程序 。

# sentence level graph:
(s2a / and
    :op1 (s2x / 综合-01
        :ARG0 (s2x2 / 周报
            :mod (s2x3 / 该))
        :ARG1 (s2a2 / and
            :op1 (s2x4 / 新闻
                :mod (s2x6 / 各式各样)
                :mod (s2x7 / 奇怪))
            :op2 (s2x5 / 专栏
                :mod s2x6
                :mod s2x7))
        :aspect habitual)
    :op2 (s2x8 / 经-01
        :ARG0 (s2x9 / 内容
            :quant (s2x10 / 许多)
            :mod (s2x11 / 其中))
        :ARG1 (s2x12 / 程序
            :ARG0-of (s2i2 / identity-91
                :ARG1 (s2x13 / 查证-01
                    :ARG1 (s2x14 / 新闻)
                    :aspect process))
            :mod (s2x15 / 一般))
        :mod (s2x16 / 都)
        :aspect process))


# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2x)
               (s2x :overlap s2x8)
               (s2x8 :overlap s2x13))
    :modal ((root :modal author)
            (author :full-affirmative s2x)
            (author :partial-affirmative s2x13)
            (author :full-negative s2x8))
    :coref ((s1n :same-entity s2x2)))


################################################################################
# meta-info
# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 该 周报 也 曾经 短暂 的 拥有 过 一个 属 自己 的 电视 节目 。

# sentence level graph:
(s3x / 拥有-01
    :ARG0 (s3x2 / 周报
        :mod (s3x3 / 该))
    :ARG1 (s3x4 / 节目
        :medium (s3x5 / 电视)
        :ARG0-of (s3x6 / 属-02
            :ARG1 s3x2
            :aspect state)
        :quant 1
        :unit (s3x7 / 个))
    :mod (s3x8 / 也)
    :temporal (s3x9 / 曾经)
    :duration (s3x10 / 短暂)
    :aspect state)


# document level annotation:
(s3s0 / sentence
    :temporal ((document-creation-time :before s3x)
               (s3x :overlap s3x6))
    :modal ((root :modal author)
            (author :full-affirmative s3x6)
            (author :full-affirmative s3x))
    :coref ((s2x2 :same-entity s3x2)))


################################################################################
# meta-info
# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Words: 目前 《 世界 新闻 周报 》 的 纸本 已经 停刊 ， 不过 仍 继续 发行 网络版 。

# sentence level graph:
(s4b / but-91
    :ARG1 (s4x / 停刊-01
        :ARG0 (s4x5 / 纸本
            :part-of (s4n / newspaper
                :name (s4n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :temporal (s4x3 / 目前)
        :mod (s4x4 / 已经)
        :aspect performance)
    :ARG2 (s4x2 / 继续-01
        :ARG1 (s4x6 / 发行-01
            :ARG1 (s4x7 / 网络版)
            :aspect habitual)
        :mod (s4x8 / 仍)
        :aspect activity))


# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :depends-on s4x)
               (s4x :overlap s4x2)
               (s4x2 :overlap s4x6))
    :modal ((root :modal author)
            (author :full-affirmative s4x)
            (author :full-affirmative s4x6)
            (author :full-affirmative s4x2))
    :coref ((s3x2 :same-entity s4n)))


################################################################################
# meta-info
# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Words: 由于 其 荒诞不经 的 内容 ， 该 周报 被 称为 美国 历史 上 最富 创意 的 报纸 。

# sentence level graph:
(s5x / 称为-01
    :ARG1 (s5x2 / 周报
        :mod (s5x3 / 该))
    :ARG2 (s5x4 / 报纸
        :ARG1-of (s5h / have-degree-91
            :ARG2 (s5x5 / 富-01
                :ARG1 (s5x6 / 创意)
                :aspect state)
            :ARG3 (s5x7 / 最))
        :temporal (s5x8 / 上
            :op1 (s5x9 / 历史
                :place (s5c / country
                    :name (s5n / name
                        :op1 "美国")))))
    :reason (s5x10 / 内容
        :possessor s5x2
        :mod (s5x11 / 荒诞不经))
    :aspect performance)


# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :depends-on s5x)
               (s5x :overlap s5x5))
    :modal ((root :modal author)
            (author :full-affirmative s5x5)
            (author :full-affirmative s5x))
    :coref ((s4n :same-entity s5x2)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 94 / P 100 / F 97
a_event_concept: R 94 / P 94 / F 94
a_entity_found: R 98 / P 100 / F 99
a_entity_concept: R 100 / P 100 / F 100
a_granularity: R 98 / P 98 / F 98
b_event_sense: R 100 / P 100 / F 100
c_aspect: R 87 / P 81 / F 84
c_polarity: R – / P 0 / F 0
c_other_attributes: R 100 / P 100 / F 100
d_core_args_event: R 93 / P 93 / F 93
d_core_args_abstract: R 88 / P 88 / F 88
d_peripheral_event: R 100 / P 100 / F 100
d_peripheral_entity: R 82 / P 88 / F 85
e_core_labels: R 96 / P 96 / F 96
e_peripheral_labels: R 100 / P 100 / F 100
f_name_tokens: R 100 / P 100 / F 100
g_reentrancy: R 100 / P 83 / F 91
h_temporal: R 54 / P 47 / F 50
i_modal: R 88 / P 93 / F 90
j_coref_chain: R 100 / P 56 / F 71
j_coref_subset: R – / P 0 / F 0
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_granularity | missing | «新闻» 新闻: «新闻» 新闻 -> «《世界新闻周报》» newspaper | inside a wider predicted node
a_granularity | extra | «《世界新闻周报》» newspaper: «新闻» 新闻 -> «《世界新闻周报》» newspaper | wider than the gold node
a_event_found | missing | s2i2: identity-91 -> - | no node in the prediction matches it
c_aspect | wrong | s2x8:aspect: process -> performance | process -> performance
c_polarity | extra | s2x8:polarity: - -> - | gold has no :polarity
d_peripheral_entity | partial | s2x12: mod s2x15/一般 -> mod s2x13/查证-01; mod s2x15/一般 | extra mod s2x13/查证-01
c_aspect | wrong | s4x:aspect: performance -> state | performance -> state
d_core_args_event | wrong | s4x: arg0 s4x5/纸本 -> arg1 s4x5/纸本 | arg0 s4x5/纸本: predicted as arg1
d_peripheral_entity | extra | s4x5: - -> possessor s4n/newspaper | extra possessor s4n/newspaper
d_peripheral_entity | missing | s4n: part s4x5/纸本 -> - | missing part s4x5/纸本
e_core_labels | wrong | s4x -arg0-> s4x5: arg0 -> arg1 | arg0 -> arg1
g_reentrancy | extra | s4x6/发行-01 -arg0-> s4n/newspaper: - -> s4x6/发行-01 -arg0-> s4n/newspaper | gold has no such reentrancy
a_event_concept | wrong | s5x: 称为 -> 称 | 称为 -> 称
a_entity_found | missing | s5x8: 上 -> - | no node in the prediction matches it
c_aspect | extra | s5h:aspect: - -> state | gold has no :aspect
d_core_args_abstract | partial | s5h: arg1 s5x4/报纸; arg2 s5x5/富-01; arg3 s5x7/最 -> arg1 s5x4/报纸; arg2 s5x5/富-01; arg3 s5x7/最; arg4 s5x9/历史 | extra arg4 s5x9/历史
d_peripheral_entity | missing | s5x4: temporal s5x8/上 -> - | missing temporal s5x8/上
h_temporal | wrong | 发行-01 «发行» (snt1 s1x3 = pred s1x4): document-creation-time :before 发行-01 «发行» (snt1 s1x3 = pred s1x4); 闻名-01 «闻名» (snt1 s1x7 = pred s1x7) :contained 发行-01 «发行» (snt1 s1x3 = pred s1x4) -> 停止-01 «停止» (snt1 s1x4 = pred s1x5) :after 发行-01 «发行» (snt1 s1x3 = pred s1x4) | wrong parent and relation
h_temporal | wrong | 停止-01 «停止» (snt1 s1x4 = pred s1x5): 发行-01 «发行» (snt1 s1x3 = pred s1x4) :overlap 停止-01 «停止» (snt1 s1x4 = pred s1x5) -> document-creation-time :overlap 停止-01 «停止» (snt1 s1x4 = pred s1x5) | right relation, wrong parent
h_temporal | extra | 闻名-01 «闻名» (snt1 s1x7 = pred s1x7): - -> document-creation-time :overlap 闻名-01 «闻名» (snt1 s1x7 = pred s1x7) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt1 s1x8 = pred s1x8): 发行-01 «发行» (snt1 s1x3 = pred s1x4) :overlap 报导-01 «报导» (snt1 s1x8 = pred s1x8) -> 闻名-01 «闻名» (snt1 s1x7 = pred s1x7) :overlap 报导-01 «报导» (snt1 s1x8 = pred s1x8) | right relation, wrong parent
h_temporal | wrong | 查证-01 «查证» (snt2 s2x13 = pred s2x13): 经-01 «未经» (snt2 s2x8 = pred s2x8) :overlap 查证-01 «查证» (snt2 s2x13 = pred s2x13) -> 综合-01 «综合» (snt2 s2x = pred s2x) :overlap 查证-01 «查证» (snt2 s2x13 = pred s2x13) | right relation, wrong parent
h_temporal | wrong | 停刊-01 «停刊» (snt4 s4x = pred s4x2): document-creation-time :depends-on 停刊-01 «停刊» (snt4 s4x = pred s4x2) -> 目前 «目前» (snt4 s4x3 = pred s4x) :overlap 停刊-01 «停刊» (snt4 s4x = pred s4x2) | wrong parent and relation
h_temporal | extra | 目前 «目前» (snt4 s4x3 = pred s4x): - -> document-creation-time :depends-on 目前 «目前» (snt4 s4x3 = pred s4x) | gold gives this node no temporal parent
h_temporal | wrong | 称为-01 «称为» (snt5 s5x = pred s5x): document-creation-time :depends-on 称为-01 «称为» (snt5 s5x = pred s5x) -> document-creation-time :before 称为-01 «称为» (snt5 s5x = pred s5x) | right parent, wrong relation
i_modal | missing | identity-91 (snt1 s1i2 = pred s1i): author :full-affirmative identity-91 (snt1 s1i2 = pred s1i) -> - | the prediction gives this node no modal parent
i_modal | wrong | 查证-01 «查证» (snt2 s2x13 = pred s2x13): author :partial-affirmative 查证-01 «查证» (snt2 s2x13 = pred s2x13) -> author :full-affirmative 查证-01 «查证» (snt2 s2x13 = pred s2x13) | right parent, wrong relation
j_coref_chain | extra | 发行-01 «发行» (snt1 s1x3 = pred s1x4): - -> 发行-01 «发行» (snt4 s4x6 = pred s4x6) | gold links it to nothing
j_coref_chain | extra | 内容 «内容» (snt2 s2x9 = pred s2x9): - -> 内容 «内容» (snt5 s5x10 = pred s5x9) | gold links it to nothing
j_coref_chain | extra | 发行-01 «发行» (snt4 s4x6 = pred s4x6): - -> 发行-01 «发行» (snt1 s1x3 = pred s1x4) | gold links it to nothing
j_coref_chain | extra | 内容 «内容» (snt5 s5x10 = pred s5x9): - -> 内容 «内容» (snt2 s2x9 = pred s2x9) | gold links it to nothing
j_coref_subset | extra | 内容 «内容» (snt2 s2x9 = pred s2x9) :subset-of and (snt2 s2a2 = pred s2a2): - -> 内容 «内容» (snt2 s2x9 = pred s2x9) :subset-of and (snt2 s2a2 = pred s2a2)

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.