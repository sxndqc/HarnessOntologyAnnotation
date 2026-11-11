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
Document: zh-0028, sentence 7 of 12

The previous sentences (at most five; number, tab, words):

2	而且 它 还 配备 了 D-Sub （ VGA ） ， HDMI 两 种 接口 ，

3	能够 在 拨接 电脑 设备 之 余 ， 还 能够 方便 用户 进行 PS3 、 Xbox360 、 蓝光机 等等 设备 的 连接 。

4	这 就 是 三星 B560 ， 你 值得 拥有 !

5	方形 机身 和 方形 的 底座 设计 ， 笔挺 的 立姿 ， 有点 像 大师 打座 的 气势 。

6	它 有 三 个 接口 ， 分别 为 电源 、 HDMI 、 VGA 。

Their graphs:

# ::snt 2
# sentence level graph:
(s2a / and
    :op2 (s2p / 配备-01
        :ARG2 (s2t / thing
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s2j / 接口
            :quant 2
            :mod (s2a2 / and
                :op1 (s2x / product
                    :wiki -
                    :name (s2n / name :op1 "D-Sub" :op2 "VGA"))
                :op2 (s2x2 / product
                    :wiki "HDMI"
                    :name (s2n2 / name :op1 "HDMI"))))
        :mod (s2h / 还)
        :aspect state))

I treated 配备 as `配备-01`, sense "equip". 它 ("it") fills `:ARG2`, the thing that gets equipped, and the interfaces fill `:ARG1`. PropBank's own example for this word is set up the same way: the satellite (这颗卫星上) is `ARG2` and the equipment is `ARG1`.

A few choices could easily differ from the gold annotation:
- **而且 ("moreover"):** I made it an `and` with only `:op2`, so the sentence links back to the previous one. Gold might instead put a `:mod` on `配备-01`.
- **The two interfaces:** I wrote one `接口` node with `:quant 2` (the classifier 种 is dropped). The two named products hang under it through `:mod` and `and`. That `:mod` link is my own choice. Gold might use two separate `接口` nodes joined by `and`.
- **D-Sub (VGA):** I made it a single name with two words, `"D-Sub"` and `"VGA"`, and gave it no wiki title (`-`). VGA could also be read as a second name for the same port, written in brackets.
- **Aspect:** I gave `state`, because "it comes equipped with" describes a property of the device even though 了 is there. `performance` is the other possible reading.

# ::snt 3
# sentence level graph:
(s3a / and
    :op1 (s3b / 拨接-01
        :ARG0 (s3t / thing
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s3s / 设备
            :mod (s3d / 电脑))
        :modal-strength neutral-affirmative
        :aspect habitual)
    :op2 (s3f / 方便-01
        :ARG0 s3t
        :ARG1 (s3u / 用户)
        :ARG2 (s3l / 连接-01
            :ARG0 s3u
            :ARG1 (s3s2 / 设备
                :example (s3a2 / and
                    :op1 (s3p / product
                        :wiki "PlayStation_3"
                        :name (s3n / name :op1 "PS3"))
                    :op2 (s3p2 / product
                        :wiki "Xbox_360"
                        :name (s3n2 / name :op1 "Xbox360"))
                    :op3 (s3g / 蓝光机))
                :mod (s3e / 等等))
            :aspect habitual)
        :mod (s3h / 还)
        :modal-strength neutral-affirmative
        :aspect habitual))

# ::snt 4
# sentence level graph:
(s4a / and
    :op1 (s4i / identity-91
        :ARG1 (s4t / thing
            :mod (s4z / 这))
        :ARG2 (s4p / product
            :wiki -
            :name (s4n / name :op1 "三星" :op2 "B560"))
        :aspect state)
    :op2 (s4z2 / 值得-01
        :ARG0 s4p
        :ARG1 (s4y / 拥有-01
            :ARG0 (s4p2 / person
                :refer-person 2nd
                :refer-number singular)
            :ARG1 s4p
            :aspect state)
        :aspect state))

I treated the two clauses as `and`. The first, 这就是三星B560, is an identity: "this" is the Samsung B560. I left 就 out because it only adds emphasis. In the second, 你值得拥有, PropBank's 值得-01 has ARG0 as what makes something worthwhile, so the phone is its ARG0 and the owning (拥有-01) is its ARG1. "You" owns it (ARG0) and the phone, which the sentence doesn't repeat, is also what is owned (ARG1).

A few calls are judgement rather than certain:
- **Product name:** I made the phone a single `product` named "三星" "B560" and did not add Samsung as a separate company.
- **Strength of 拥有:** Owning is only presented as worthwhile, not asserted. Its strength would be set under 值得 at the document level, so I didn't add a `:modal-strength` to it here.
- **Joining the clauses:** The gold annotation might link them with something other than `and`, for example `multi-sentence`.

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

This sentence:

7	高清 的 HDMI 接口 成为 现在 市场 的 主流 ， 很 有 可能 HDMI 就 是 2012 的 一 个 趋势 ， 同时 还 保留 有 VGA 的 接口 ， 让 消费者 在 不同 需求 上 得到 满足 。

Its graph:

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
