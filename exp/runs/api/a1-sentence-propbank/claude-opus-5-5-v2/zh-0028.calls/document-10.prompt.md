<!-- system -->
# Skill: the document-level relations of one sentence

You add the UMR document-level relations (temporal, modal, coreference) of one sentence of a document.
Every sentence of the document already has its sentence-level graph. Under **Input** at the end you get
this sentence and the sentences before it (at most five) with their graphs.

**Make the annotation as correct as you can.** It is compared, relation by relation, with an expert gold
annotation made by these guidelines, so every temporal, modal and coreference relation counts. Take the
time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: which events and entities get which relations, their reference times, conceivers and
  modal strengths, and which nodes corefer.
- Follow the examples: when the sentence has a case an example shows, annotate it the way the example
  does.
- Do not guess when you can check: the meaning of a predicate is in PropBank: look it up with
  `propbank_lookup` (see Tools) whenever it matters for a relation (whether an event is a state, who its
  conceiver is).
- Before you answer, check that the relations cover every event and entity of this sentence that the
  guidelines ask for.

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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
an ordinary classifier (个, 本, 只, 位) is dropped (三本书 → `书 :quant 3`).

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

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而) `but-91`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:cause`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span.

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
- Annotate event–event relations only when they are clear.

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


## Output format

Write plain text only (no JSON, no commentary): the document-level relations of this sentence (number N)
in one graph, for example for sentence 2:

    # document level relations:
    (d / document
        :temporal ((s1t :before s2t)
                   (document-creation-time :overlap s2s))
        :modal ((root :modal author)
                (author :full-affirmative s2t)
                (author :full-affirmative s2s))
        :coref ((s1p :same-entity s2p)))

- The relations of this sentence are those in which a node of sentence N takes part: with a constant
  (`author`, `root`, `document-creation-time`, `past-reference`, `present-reference`,
  `future-reference`, `null-conceiver`), with another node of sentence N, or with a node of one of the
  previous sentences given (for example coreference with an earlier mention, or an event of this sentence
  ordered after an event of the previous one). Do not repeat relations among the previous sentences only.
- `(parent :relation child)` triples, grouped under `:temporal`, `:modal`, `:coref`; each end is a
  variable of the graphs given, exactly as written there, or a constant.
- Use the names of the UMR release data: `author` (not AUTH), `document-creation-time` (not DCT),
  `full-affirmative`, ..., `unspecified` (not FullAff, ...).
- If the sentence has no document-level relation, write the graph with empty groups: `(d / document)`.

## Tools

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Use it when the meaning of a predicate decides a relation.

<!-- user -->
## Input

Language: zh
Document: zh-0028, sentence 10 of 12

The previous sentences (at most five; number, tab, words):

5	方形 机身 和 方形 的 底座 设计 ， 笔挺 的 立姿 ， 有点 像 大师 打座 的 气势 。

6	它 有 三 个 接口 ， 分别 为 电源 、 HDMI 、 VGA 。

7	高清 的 HDMI 接口 成为 现在 市场 的 主流 ， 很 有 可能 HDMI 就 是 2012 的 一 个 趋势 ， 同时 还 保留 有 VGA 的 接口 ， 让 消费者 在 不同 需求 上 得到 满足 。

8	福韵 B560 系列 的 诠释 有 ： “ 福运 ” 、 “ 幸福 ” 、 和 拥有 贵族 的 “ 韵 ” 味 。

9	左右上角 的 两 条 龙 设计 的 毫 无 瑕疵 ， 机身 背后 写 有 一 个 大大 的 “ 福 ” 字 ， 并且 拥有 古代 龙纹 图案 ， 这些 都 有 浓郁 的 中国 元素 。

Their graphs:

# ::snt 5
# sentence level graph:
(s5x / 像-01
    :ARG0 (s5a / and
        :op1 (s5s / 设计-01
            :ARG1 (s5a2 / and
                :op1 (s5j / 机身
                    :mod (s5f / 方形))
                :op2 (s5d / 底座
                    :mod (s5f2 / 方形)))
            :aspect process)
        :op2 (s5l / 立姿
            :mod (s5b / 笔挺)))
    :ARG1 (s5q / 气势
        :mod (s5d2 / 打座-00
            :ARG0 (s5m / 大师)
            :aspect process))
    :degree (s5y / 有点)
    :aspect state)

# ::snt 6
# sentence level graph:
(s6a / and
    :op1 (s6y / 有-01
        :ARG0 (s6t / thing
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s6j / 接口
            :quant 3)
        :aspect state)
    :op2 (s6w / 为-01
        :ARG0 s6j
        :ARG1 (s6a2 / and
            :op1 (s6d / 电源)
            :op2 (s6h / HDMI)
            :op3 (s6v / VGA))
        :manner (s6f / 分别)
        :aspect state))

I based this on two PropBank lookups:
- **有 (has):** I chose `有-01` (owner and thing owned). "它" (it) is the owner and is a third-person singular `thing`. The three ports are `接口 :quant 3`. The classifier 个 is left out.
- **为 (are, namely):** I chose `为-01` (a thing and what it is said to be). Its `:ARG0` points back to the same ports node, and its `:ARG1` is an `and` of the three items: 电源 (power), HDMI and VGA.

Some choices were judgement calls and could differ from the expert annotation:
- **Joining the clauses:** there is no conjunction, so I linked them with a top-level `and`. Another option would be to attach the second clause to the ports with `:ARG0-of`.
- **分别 (respectively):** I attached it to `为-01` as `:manner`. It could also be a plain `:mod`.
- **Aspect:** both events are `state`, since one is owning and the other says what the ports are.

# ::snt 7
# sentence level graph:
(s7a / and
    :op1 (s7c / 成为-01
        :ARG0 (s7j / 接口
            :mod (s7g / 高清)
            :mod (s7p / product
                :name (s7n / name :op1 "HDMI")))
        :ARG1 (s7z / 主流
            :mod (s7s / 市场
                :temporal (s7x / 现在)))
        :aspect state)
    :op2 (s7i / identity-91
        :ARG1 s7p
        :ARG2 (s7q / 趋势
            :temporal (s7d / date-entity :year 2012))
        :aspect state
        :modal-strength partial-affirmative)
    :op3 (s7b / 保留-01
        :ARG0 s7p
        :ARG1 (s7j2 / 接口
            :mod (s7p2 / product
                :name (s7n2 / name :op1 "VGA")))
        :mod (s7h / 还)
        :temporal (s7t / 同时)
        :purpose (s7r / 让-02
            :ARG1 (s7k / 消费者)
            :ARG2 (s7e / 得到-01
                :ARG0 s7k
                :ARG1 (s7m / 满足-01
                    :ARG2 (s7x2 / 需求-01
                        :ARG0 s7k
                        :mod (s7y / 不同)
                        :aspect state)
                    :aspect process)
                :aspect activity)
            :aspect activity)
        :aspect state))

<br>

I think 很有可能 ("very likely") counts as probable, not merely possible. So the `identity-91` (HDMI 就是 2012 的趋势) gets `:modal-strength partial-affirmative`.

A few other calls you may want to check:
- **Copula:** I treated 是 as a copula and wrote it as `identity-91`, as the guidelines say for "X is Y", not as PropBank `是-01`.
- **Named entities:** HDMI and VGA are both written as `product` named entities. The type and the missing `:wiki` are my guesses.
- **Subject of 保留:** the sentence doesn't say what keeps the VGA port. I made it HDMI (`:ARG0 s7p`), but this is the least certain choice in the graph.
- **得到满足:** I wrote it as `得到-01` ("obtain") taking `满足-01` ("satisfy") as its `:ARG1`, with the consumers' needs as what is satisfied. PropBank's `满足-01` puts the thing satisfied in `:ARG2`, as in its example "满足……需求". I attached 在不同需求上 there, though the expert may have tied it to the consumers or to 得到.
- **Purpose:** the 让 clause is a `:purpose` of 保留.
- **Aspect:** 成为 and 保留有 are `state`, describing the current market. 让 and 得到 are `activity`.

# ::snt 8
# sentence level graph:
(s8y / 有-07
    :ARG0 (s8q / 诠释-01
        :ARG1 (s8x / 系列
            :mod (s8p / product
                :wiki -
                :name (s8n / name :op1 "福韵" :op2 "B560")))
        :aspect process)
    :ARG1 (s8a / and
        :op1 (s8f / 福运)
        :op2 (s8h / 幸福-01
            :aspect state)
        :op3 (s8o / 拥有-01
            :ARG0 s8x
            :ARG1 (s8w / 味
                :mod (s8r / 韵)
                :mod (s8g / 贵族))
            :aspect state))
    :aspect state)

I treated "福韵 B560" as a product name and "系列" (series) as the head noun modified by that product. Other choices I made:

- **有-07**: I chose this "includes" sense for 有, with ARG0 the content being described and ARG1 the items listed.
- **诠释-01**: Here it is a noun meaning "the interpretation", so it is a process. Its ARG1 is the series.
- **福运**: I wrote this as a plain entity concept, not an event.
- **幸福-01**: I treated this as a state. It has no argument because PropBank's only role for it, ARG0 (the one who is happy), isn't stated in the sentence.
- **拥有-01**: I made the series its owner. What is owned is 味 (flavor), with 韵 (charm) and 贵族 (noble) as modifiers.

Two points could reasonably go another way: whether 幸福 should be a plain noun rather than an event, and whether "系列" belongs inside the name.

# ::snt 9
# sentence level graph:
(s9a / and
    :op1 (s9s / 设计-01
        :ARG1 (s9l / 龙
            :quant 2
            :place (s9j / 上角
                :mod (s9z / 左右)))
        :manner (s9w / 无-01
            :ARG1 (s9x / 瑕疵)
            :degree (s9h / 毫)
            :aspect state)
        :aspect performance)
    :op2 (s9x2 / 写-01
        :ARG1 (s9z2 / 字
            :mod (s9f / 福)
            :mod (s9d / 大大)
            :quant 1)
        :ARG2 (s9b / 背后
            :part-of (s9j2 / 机身))
        :aspect state)
    :op3 (s9y / 拥有-01
        :ARG0 s9j2
        :ARG1 (s9t / 图案
            :mod (s9l2 / 龙纹)
            :mod (s9g / 古代))
        :aspect state)
    :op4 (s9y2 / 有-01
        :ARG0 (s9t2 / thing
            :mod (s9z3 / 这些)
            :mod (s9d2 / 都)
            :refer-number plural)
        :ARG1 (s9e / 元素
            :mod (s9c / country
                :wiki "China"
                :name (s9n / name :op1 "中国"))
            :mod (s9n2 / 浓郁))
        :aspect state))

I annotated the sentence as an `and` of four clauses, all on the plane's design. There is no conjunction for this `and` in the sentence, so it is aligned to no word. I checked every predicate in PropBank: 设计, 无, 写, 有, 拥有 and 浓郁. 瑕疵 is not in PropBank, so it is a plain noun.

These choices could reasonably have gone another way:
- **设计得毫无瑕疵**: I used `设计-01` with `:manner (无-01 :ARG1 瑕疵 :degree 毫)`. The other way to do it was to drop `无-01` and put `:polarity -` on 瑕疵.
- **Aspect of 设计**: I chose `performance` (the design is finished). `state` is also possible, since the clause describes how the plane looks.
- **拥有**: The subject is left out in the sentence. I took it to be the plane body (机身) and reused that node as `:ARG0`.
- **这些**: I made it a separate `thing` node marked plural. The gold may instead point it back to the three earlier clauses.
- **有**: I used `有-01` (possession). `有-06` ("entity owned by / exists with respect to") also fits.
- **浓郁**: I treated it as a plain modifier (`:mod`) of 元素, not as the predicate `浓郁-01`, because here it describes the noun rather than being predicated.
- **"福" 字**: 福 is a `:mod` of 字, with `:quant 1` for 一个.

This sentence:

10	金黄色 的 B560 系列 看 起来 更 符合 龙年 的 韵味 ， 背部 的 福 字 也 更加 现眼 . 。

Its graph:

# ::snt 10
# sentence level graph:
(s10a / and
    :op1 (s10k / 看-05
        :ARG0 (s10x / 系列
            :name (s10n / name :op1 "B560")
            :mod (s10j / 金黄色))
        :ARG1 (s10f / 符合-01
            :ARG0 s10x
            :ARG1 (s10y / 韵味
                :possessor (s10l / 龙年))
            :degree (s10g / 更)
            :aspect state)
        :aspect state)
    :op2 (s10m / 现眼-00
        :ARG1 (s10z / 字
            :mod (s10u / 福)
            :place (s10b / 背部
                :part-of s10x))
        :mod (s10e / 也)
        :degree (s10h / 更加)
        :aspect state))

I treated 现眼 as written as the predicate. It is not in Chinese PropBank, so I named it `现眼-00`. It is probably a typo for 显眼 ("eye-catching"), which is in PropBank as `显眼-01` and takes `:ARG0` for its theme. If the gold annotation fixes the typo, that node would be `显眼-01` with `:ARG0` instead.

Other choices that could go either way:
- **看起来:** I used `看-05` ("look/appear"), which in PropBank only has an `:ARG0`. I put 符合 under it as `:ARG1` anyway, so that "fits the Year of the Dragon" is shown as what the series appears to do.
- **B560 系列:** I annotated it as the concept 系列 with the name "B560", not as a named-entity type like `product`.
- **龙年:** I left it as a plain concept that possesses 韵味, not as a `date-entity`.
- **背部:** I treated 背部 ("the back") as the place of the character and linked it as part of the B560 series.
