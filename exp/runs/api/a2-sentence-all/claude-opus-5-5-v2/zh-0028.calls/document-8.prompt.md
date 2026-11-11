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
- Do not guess when you can check: use the tools (see Tools): search the full guidelines with
  `search_guidelines` for the rules of temporal, modal and coreference relations, look up how the gold
  data annotates such relations with `search_annotations` (e.g. `:same-entity`, `:depends-on`,
  `:full-affirmative`), and look a predicate up with `propbank_lookup` whenever its meaning matters for a
  relation. Call them as often as you need.
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

`search_guidelines(keywords, max_results)` searches the **full** UMR guidelines (umr4nlp/umr-guidelines,
the document the guidelines above abridge) and returns the matching passages with their headings, with
their examples. The abridged guidelines leave out most details and examples, so use it a lot: look a rule
up whenever you are not sure of a case (an abstract concept, a role, a named entity type, an aspect or modal
value, a temporal or coreference decision), and look up each kind of construction the document has before
you annotate it. Search with the terms the guidelines would use (`aspect`, `have-rel-role-92`, `:quant`,
`modal strength`, `reentrancy`). Note that the full guidelines often write the older short names (AUTH,
DCT, FullAff, :modstr); your answer uses the release names listed under Output format.

`search_annotations(language, keywords, max_results)` returns gold UMR annotations of whole sentences of the
training data (other documents) that contain the keywords: words of the text, concepts (`have-org-role-92`), roles
(`:ARG1-of`), attribute values (`:aspect state`), document-level relations (`:same-entity`). These are
annotated by the same experts as the gold you are compared with, so they show how this data annotates a
case. Use it a lot: for each sentence, look up its words and constructions you are not sure of (a word's
concept and sense, a light verb, a modal word, a named entity, a comparison, a quantity, a discourse
relation, the aspect of a kind of event) before you annotate it, and follow what the gold does.

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Use it when the meaning of a predicate decides a relation.

<!-- user -->
## Input

Language: zh
Document: zh-0028, sentence 8 of 12

The previous sentences (at most five; number, tab, words):

3	能够 在 拨接 电脑 设备 之 余 ， 还 能够 方便 用户 进行 PS3 、 Xbox360 、 蓝光机 等等 设备 的 连接 。

4	这 就 是 三星 B560 ， 你 值得 拥有 !

5	方形 机身 和 方形 的 底座 设计 ， 笔挺 的 立姿 ， 有点 像 大师 打座 的 气势 。

6	它 有 三 个 接口 ， 分别 为 电源 、 HDMI 、 VGA 。

7	高清 的 HDMI 接口 成为 现在 市场 的 主流 ， 很 有 可能 HDMI 就 是 2012 的 一 个 趋势 ， 同时 还 保留 有 VGA 的 接口 ， 让 消费者 在 不同 需求 上 得到 满足 。

Their graphs:

# ::snt 3
# sentence level graph:
(s3f / 方便-01
    :ARG0 (s3t / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s3u / 用户)
    :ARG2 (s3l / 连接-01
        :ARG0 s3u
        :ARG1 (s3s / 设备
            :example (s3a / and
                :op1 (s3p / product
                    :name (s3n / name :op1 "PS3"))
                :op2 (s3p2 / product
                    :name (s3n2 / name :op1 "Xbox360"))
                :op3 (s3b / 蓝光机)
                :op4 (s3e / et-cetera)))
        :aspect state)
    :temporal (s3b2 / 拨接-01
        :ARG0 s3t
        :ARG1 (s3s2 / 设备
            :mod (s3d / 电脑))
        :aspect state
        :modal-strength neutral-affirmative)
    :mod (s3h / 还)
    :aspect state
    :modal-strength neutral-affirmative)

# ::snt 4
# sentence level graph:
(s4a / and
    :op1 (s4i / identity-91
        :ARG1 (s4t / thing
            :mod (s4z / 这))
        :ARG2 (s4p / product
            :wiki "-"
            :name (s4n / name :op1 "三星" :op2 "B560"))
        :mod (s4j / 就)
        :aspect state)
    :op2 (s4z2 / 值得-01
        :ARG1 (s4y / 拥有-01
            :ARG0 (s4p2 / person
                :refer-person 2nd
                :refer-number singular)
            :ARG1 s4p
            :aspect state
            :modal-strength neutral-affirmative)
        :aspect state))

I read the sentence as "The square-body and square-base design and the upright posture look a little like the aura of a master sitting in meditation." The main predicate is 像-01 ("resemble"): its `:ARG0` is the thing being described (the design and the posture, joined with `and`) and its `:ARG1` is what it looks like (气势, "aura"). 有点 ("somewhat") is `:degree`, following a gold example with the same 有点 像 pattern.

Three choices are uncertain:
- **打座:** The sentence writes 打座, which is not in PropBank, so it is 打座-00. PropBank has the standard spelling 打坐 as 打坐-01, and the gold may use that instead.
- **设计 ("design"):** I treated it as an event noun, 设计-01 with `:aspect process`. The gold may instead treat it as a plain noun.
- **方形 and 笔挺:** Both are plain `:mod` modifiers here, not separate events.

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
            :aspect activity))
    :degree (s5y / 有点)
    :aspect state)

# ::snt 6
# sentence level graph:
(s6h / have-91
    :ARG1 (s6p / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG2 (s6x / 接口
        :quant 3
        :unit (s6x2 / 个)
        :ARG1-of (s6i / identity-91
            :ARG2 (s6a / and
                :op1 (s6x3 / 电源)
                :op2 (s6x4 / HDMI)
                :op3 (s6x5 / VGA))
            :mod (s6x6 / 分别-01)
            :aspect state))
    :aspect state)

I read the sentence as three linked clauses, joined by `and`:
1. HDMI is now the market's mainstream.
2. HDMI is very likely to be a 2012 trend.
3. VGA ports are kept too, so consumers' different needs are met.

The senses come from Chinese PropBank. Five choices were judgement calls rather than checked rules:
- **很有可能 ("very likely")**: I put it on the second clause as `:modal-strength partial-affirmative` with no node of its own. A gold search for 很有可能 found nothing, and the gold examples of 可能 were not the same construction.
- **Satisfying needs**: I treated 得到满足 ("get satisfied") as plain `满足-01`, with the consumers as the ones satisfied (`:ARG2`) and their needs as `:ARG1`.
- **HDMI and VGA**: I annotated both as named entities of type `product`. I did not check this type in the guidelines or the gold data.
- **成为 ("become")**: I gave it `:aspect state`, reading "has become the mainstream now" as a current state.
- **Dropped words**: 就, 很 and 一个 have no node of their own; 同时 ("at the same time") is kept as a `:temporal`.

# ::snt 7
# sentence level graph:
(s7a / and
    :op1 (s7c / 成为-01
        :ARG0 (s7j / 接口
            :mod (s7g / 高清)
            :mod (s7p / product
                :name (s7n / name :op1 "HDMI")))
        :ARG1 (s7z / 主流
            :poss (s7s / 市场))
        :temporal (s7x / 现在)
        :aspect state)
    :op2 (s7i / identity-91
        :ARG1 (s7p2 / product
            :name (s7n2 / name :op1 "HDMI"))
        :ARG2 (s7q / 趋势
            :quant 1
            :temporal (s7d / date-entity :year 2012))
        :aspect state
        :modal-strength partial-affirmative)
    :op3 (s7b / 保留-01
        :ARG1 (s7j2 / 接口
            :mod (s7p3 / product
                :name (s7n3 / name :op1 "VGA")))
        :mod (s7h / 还)
        :temporal (s7t / 同时)
        :aspect state
        :purpose (s7r / 让-02
            :ARG1 (s7k / 消费者)
            :ARG2 (s7m / 满足-01
                :ARG1 (s7x2 / 需求-01
                    :ARG0 s7k
                    :mod (s7y / 不同)
                    :aspect state)
                :ARG2 s7k
                :aspect performance)
            :aspect performance)))

This sentence:

8	福韵 B560 系列 的 诠释 有 ： “ 福运 ” 、 “ 幸福 ” 、 和 拥有 贵族 的 “ 韵 ” 味 。

Its graph:

我把句子分析为：「福韵 B560 系列的诠释」是一个事件名词，它通过「有」引出三项内容。

1. **「有」**：用 **有-07**，这个义项在 PropBank 里的意思是「ARG0 包含 ARG1 里的这些项」。这里的 ARG0 是「诠释」，ARG1 是后面列出的几项。体（aspect）标为 `state`。
2. **「诠释」**：用 **诠释-01**，它的 ARG1 是这个系列。因为它是事件名词，所以体标为 `process`。
3. **「福韵 B560 系列」**：处理成一个以 `系列` 为中心的节点，用 `:mod` 连到一个命名实体 `product`，名称为「福韵」「B560」。用 `product` 这个类型是我的判断，没有在标注数据里核对过。
4. **三项内容**：用 `and` 并列：「福运」「幸福」，以及 **拥有-01**（ARG1 为「韵味」，`:mod` 为「贵族」）。「拥有」在这里表达的是一种状态，所以体标为 `state`。

有一处不太确定：原文把「韵」加了引号，「韵」和「味」是两个分开的词。我还是把它们合成一个概念 `韵味`，所以这个节点可能无法和单个词对齐。

# ::snt 8
# sentence level graph:
(s8x / 有-07
    :ARG0 (s8x2 / 诠释-01
        :ARG1 (s8x3 / 系列
            :mod (s8p / product
                :name (s8n / name :op1 "福韵" :op2 "B560")))
        :aspect process)
    :ARG1 (s8a / and
        :op1 (s8x4 / 福运)
        :op2 (s8x5 / 幸福)
        :op3 (s8x6 / 拥有-01
            :ARG1 (s8x7 / 韵味
                :mod (s8x8 / 贵族))
            :aspect state))
    :aspect state)
