<!-- system -->
You review UMR annotations made with an instruction, and say what in the instruction should change.
<!-- user -->
An annotator (a model) annotated the sentences below in Uniform Meaning Representation (UMR), following the instruction below. A judge (umrjudge) then compared its annotation with the expert gold annotation, check by check (concepts, senses, roles, attributes, named entities, reentrancy, and the document-level temporal, modal and coreference relations).

Your task: find the error patterns that cost the most, explain why they happen given the instruction (a rule that is missing, unclear, wrong, or not followed), and say what to change in the instruction to fix them so that they do not recur on other documents. Order them by cost, most costly first. Say also what the annotator got right that the instruction should keep. Give your advice as general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences; describe each case by its kind (e.g. a verb of saying with a clause object, a noun modified by a measure phrase).

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
- Do not guess when you can check: use the three tools (see Tools): search the full guidelines with
  `search_guidelines` whenever the guidelines above do not settle a case, look up every predicate in
  PropBank with `propbank_lookup` before you choose its sense and numbered roles, and look up how the gold
  data annotates a construction, a word or a relation with `search_annotations`. Call them as often as you
  need: many calls are expected.
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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a numeral + measure word or classifier keeps the classifier as the unit,
ordinary classifiers included (个, 本, 只, 位, 份, 面): 三杯水 → `水 :quant 3 :unit 杯`, 一本书 → `书 :quant 1 :unit (s / 本)`.
A demonstrative + classifier (这个, 那份) also keeps the classifier as `:unit`.
The title marks of a work or publication name (《 and 》) are part of the name: `:op1 "《"`, then the words, then a last `:opN "》"`.

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
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `(b / but-91 :ARG1 ... :ARG2 ...)`.
  These frames take `:ARG1`/`:ARG2`, never `:op1`/`:op2`. A time word or adverbial of a clause attaches to that
  clause's event, never to the discourse frame;
- concession `:concession`, condition `:condition`, reason `:reason` (for 由于/因为 phrases giving the reason for a state, an action or a judgement), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; *in order to* (为了)
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

### 3.1 Attachment rules (frequent errors)

- Every adverb that carries meaning (*already, still, also, all/both*; 已经, 仍, 也, 都, 均) gets its own node,
  attached as `:mod` to the predicate it scopes over, not to a noun.
- A modifier that applies to each of several coordinated nouns is placed on each conjunct with the same variable
  (re-entrancy), not once on the `and` node.
- Fill only the arguments the syntax provides. Do not borrow a participant from elsewhere in the sentence for a
  noun compound or a nominal event; in a compound "N1-verb N2", the role is filled by the compound's own noun.
- "Known/famous for X" (…而闻名, 以…著称): the famous entity is the `:ARG1` of the fame predicate, attached as
  `:ARG1-of` on that noun, and the X clause is `:reason` of it, with that noun as its agent. When such a clause
  follows "A is a B", attach it inside the B noun, not as a separate conjunct.
- Role choice for noun modifiers: a country, city or place modifying a noun → `:place`; a channel or medium
  (TV, radio, network, print) → `:medium`; an edition, section or component of a whole → `:part-of` (not
  `:possessor`).
- Comparatives and superlatives use `have-degree-91`: *the most P X* → `(x / X :ARG1-of (h / have-degree-91
  :ARG2 (p / P) :ARG3 (m / most)))` (Chinese: `:ARG3 (m / 最)`); *more P than Y* adds `:ARG4 Y`. Use `:degree`
  only for plain intensifiers (very, too; 很, 非常, 太).
- A property word or chengyu used attributively ("absurd content", X 的 Y with X a property) is a `:mod` concept,
  not an event: it gets no aspect and no temporal or modal links.

## 4. Attributes

### 4.1 Aspect (`:aspect`, on every event)

Decide in this order before using the table:
1. Is the event a routine or recurring practice of its subject (an organisation or periodical publishing,
   reporting, compiling, broadcasting)? → `habitual`. This holds whatever the tense, and also under an
   aspectual verb (continue, stop).
2. Does a completive or aspectual predicate (*has already stopped, has ended*) describe a present condition? → `state`.
3. Is the event a process noun, including the object of a light or experiential verb (经, 经过, 进行, undergo)? → `process`.
4. Is it a verb of naming or labelling (*is called X*, 被称为)? → `performance`.

Otherwise use the coarse values:

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
  then negative (5.2). A negator fused into a verb (未经-type verbs: "without having undergone") gives no
  `:polarity`. The verb is `full-negative` in the modal layer. Events nested under it do not inherit the
  negation; check the gold data for their strength.
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
- **Which nodes get a temporal parent.** Only real eventive predicates and specific time expressions. Do NOT
  give a temporal parent to:
  - copular or identity predicates (`identity-91`, `have-role-91` of a defining "A is a B" sentence);
  - states used as attributes inside a noun phrase (*famous X*, a relative-clause state);
  - property modifiers;
  - vague deictic time words (*now, currently, nowadays*, 现在, 目前, 当前).
- Precision counts as much as recall: when a link is not clear, leave it out.
- Time expressions: an absolute date (*1998*) depends on `root`; a relative one (*today, yesterday*,
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`.
- **Within a sentence, chain the events.** Pick one anchor event (usually the main eventive predicate) and link
  the other events of the sentence to it: `:overlap` for simultaneous states, `:contained` for a state or event
  inside its span, `:before`/`:after` for sequence. Only the anchor links to `document-creation-time` or to an
  earlier sentence's event. For the main event of a sentence describing the present situation, the gold data
  often uses `(document-creation-time :depends-on e)`; check with `search_annotations`.
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
- `(earlier :same-event later)`: two mentions of the same event instance, with the same participants. Two
  different events of similar meaning (e.g. two different kinds of stopping) are not linked.
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
    :ARG1 (s1p / publication
        :wiki "Weekly_World_News"
        :name (s1n / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :ARG2 (s1x / 小报
        :quant 1
        :unit (s1x2 / 份)
        :ARG1-of (s1x3 / 停止-01
            :ARG1 (s1x4 / 发行-01
                :ARG1 s1x
                :aspect habitual)
            :mod (s1x5 / 已经)
            :aspect state)
        :place (s1c / country
            :wiki "United_States"
            :name (s1n2 / name
                :op1 "美国"))
        :mod (s1x6 / 超市)
        :ARG1-of (s1x7 / 闻名-01
            :reason (s1x8 / 报导-01
                :ARG0 s1x
                :ARG1 (s1a / and
                    :op1 (s1x9 / 奇闻)
                    :op2 (s1x10 / 轶事)
                    :op3 (s1x11 / 传奇
                        :mod (s1x12 / 都会))
                    :op4 (s1x13 / 新闻
                        :mod (s1x14 / 恶搞)))
                :aspect habitual)
            :aspect state))
    :aspect state)


# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1x3)
               (s1x3 :before s1x4)
               (document-creation-time :before s1x8))
    :modal ((root :modal author)
            (author :full-affirmative s1i)
            (author :full-affirmative s1x3)
            (author :full-affirmative s1x4)
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
                :mod s2x6)
            :subset s2x9)
        :aspect habitual)
    :op2 (s2x8 / 未经-00
        :ARG1 (s2x9 / 内容
            :quant (s2x10 / 许多))
        :ARG2 (s2x11 / 程序
            :mod (s2x12 / 一般)
            :mod (s2x13 / 查证-01
                :ARG1 (s2x14 / 新闻)
                :aspect process))
        :mod (s2x15 / 都)
        :aspect state))


# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2x)
               (s2x :overlap s2x8))
    :modal ((root :modal author)
            (author :full-affirmative s2x)
            (author :full-negative s2x8)
            (author :full-affirmative s2x13))
    :coref ((s1p :same-entity s2x2)))


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
        :mod (s3x6 / 电视)
        :ARG1-of (s3x7 / 属-02
            :ARG0 s3x2
            :aspect state))
    :mod (s3x8 / 也)
    :mod (s3x9 / 曾经)
    :duration (s3x10 / 短暂)
    :aspect performance)


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
    :ARG1 (s4x / 停刊-01
        :ARG0 (s4x2 / 纸本
            :part-of (s4p / publication
                :wiki "Weekly_World_News"
                :name (s4n / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :mod (s4x3 / 已经)
        :temporal (s4x4 / 目前)
        :aspect state)
    :ARG2 (s4x5 / 继续-01
        :ARG1 (s4x6 / 发行-01
            :ARG0 s4p
            :ARG1 (s4x7 / 网络版
                :part-of s4p)
            :aspect habitual)
        :mod (s4x8 / 仍)
        :aspect activity))


# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :overlap s4x)
               (s4x :overlap s4x5)
               (s4x5 :overlap s4x6))
    :modal ((root :modal author)
            (author :full-affirmative s4x)
            (author :full-affirmative s4x5)
            (author :full-affirmative s4x6))
    :coref ((s3x2 :same-entity s4p)))


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
            :ARG2 (s5x5 / 创意)
            :ARG3 (s5x6 / 最)
            :ARG5 (s5x7 / 历史
                :mod (s5c / country
                    :wiki "United_States"
                    :name (s5n / name
                        :op1 "美国")))))
    :reason (s5x8 / 内容
        :mod (s5x9 / 荒诞不经)
        :possessor s5x2)
    :aspect performance)


# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :overlap s5x))
    :modal ((root :modal author)
            (author :full-affirmative s5x)
            (author :full-affirmative s5h))
    :coref ((s4p :same-entity s5x2)
            (s1c :same-entity s5c)))



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
a_event_found: R 89 / P 100 / F 94
a_event_concept: R 94 / P 94 / F 94
a_entity_found: R 94 / P 100 / F 97
a_entity_concept: R 96 / P 96 / F 96
a_granularity: R 98 / P 98 / F 98
b_event_sense: R 100 / P 100 / F 100
c_aspect: R 79 / P 79 / F 79
c_other_attributes: R 100 / P 100 / F 100
d_core_args_event: R 75 / P 81 / F 78
d_core_args_abstract: R 70 / P 70 / F 70
d_peripheral_event: R 90 / P 90 / F 90
d_peripheral_entity: R 74 / P 79 / F 77
e_core_labels: R 86 / P 86 / F 86
e_peripheral_labels: R 88 / P 88 / F 88
f_name_tokens: R 100 / P 100 / F 100
f_wiki: R – / P 0 / F 0
g_reentrancy: R 80 / P 44 / F 57
h_temporal: R 46 / P 55 / F 50
i_modal: R 88 / P 88 / F 88
j_coref_chain: R 100 / P 71 / F 83
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_found | missing | s1a2: and -> - | no node in the prediction matches it
a_entity_concept | wrong | s1n: newspaper -> publication | newspaper -> publication
a_granularity | missing | «新闻» 新闻: «新闻» 新闻 -> «《世界新闻周报》» publication | inside a wider predicted node
a_granularity | extra | «《世界新闻周报》» publication: «新闻» 新闻 -> «《世界新闻周报》» publication | wider than the gold node
d_core_args_event | missing | s1x3: arg1 s1x/小报 -> - | missing arg1 s1x/小报
d_core_args_event | partial | s1x4: arg1 s1x3/发行-01 -> arg1 s1x/小报; arg1 s1x3/发行-01 | extra arg1 s1x/小报
f_wiki | extra | s1n:wiki: - -> weekly_world_news | gold has no :wiki
f_wiki | extra | s1c:wiki: - -> united_states | gold has no :wiki
g_reentrancy | extra | s1x4/发行-01 -arg1-> s1x/小报: - -> s1x4/发行-01 -arg1-> s1x/小报 | gold has no such reentrancy
a_event_found | missing | s2i2: identity-91 -> - | no node in the prediction matches it
a_event_concept | wrong | s2x8: 经 -> 未经 | 经 -> 未经
a_entity_found | missing | s2x11: 其中 -> - | no node in the prediction matches it
c_aspect | wrong | s2x8:aspect: process -> state | process -> state
d_core_args_event | wrong | s2x8: arg0 s2x9/内容; arg1 s2x12/程序 -> arg1 s2x9/内容; arg2 s2x12/程序 | arg0 s2x9/内容: predicted as arg1; arg1 s2x12/程序: predicted as arg2
d_peripheral_entity | partial | s2x9: mod s2x11/其中; quant s2x10/许多 -> quant s2x10/许多 | missing mod s2x11/其中
d_peripheral_entity | partial | s2x12: mod s2x15/一般 -> mod s2x13/查证-01; mod s2x15/一般 | extra mod s2x13/查证-01
e_core_labels | wrong | s2x8 -arg0-> s2x9: arg0 -> arg1 | arg0 -> arg1
e_core_labels | wrong | s2x8 -arg1-> s2x12: arg1 -> arg2 | arg1 -> arg2
g_reentrancy | extra | s2a2/and -subset-> s2x9/内容: - -> s2a2/and -subset-> s2x9/内容 | gold has no such reentrancy
c_aspect | wrong | s3x:aspect: state -> performance | state -> performance
d_core_args_event | wrong | s3x6: arg0 s3x4/节目 -> arg1 s3x4/节目 | arg0 s3x4/节目: predicted as arg1
d_peripheral_event | partial | s3x: duration s3x10/短暂; mod s3x8/也; temporal s3x9/曾经 -> duration s3x10/短暂; mod s3x8/也; mod s3x9/曾经 | temporal s3x9/曾经: predicted as mod
d_peripheral_entity | partial | s3x4: medium s3x5/电视; unit s3x7/个 -> mod s3x5/电视; unit s3x7/个 | medium s3x5/电视: predicted as mod
e_core_labels | wrong | s3x6 -arg0-> s3x4: arg0 -> arg1 | arg0 -> arg1
e_peripheral_labels | wrong | s3x -temporal-> s3x9: temporal -> mod | temporal -> mod
e_peripheral_labels | wrong | s3x4 -medium-> s3x5: medium -> mod | medium -> mod
g_reentrancy | missing | s3x6/属-02 -arg1-> s3x2/周报: s3x6/属-02 -arg1-> s3x2/周报 -> - | the prediction has no such edge
g_reentrancy | extra | s3x7/属-02 -arg0-> s3x2/周报: - -> s3x7/属-02 -arg0-> s3x2/周报 | gold has no such reentrancy
a_entity_concept | wrong | s4n: newspaper -> publication | newspaper -> publication
c_aspect | wrong | s4x:aspect: performance -> state | performance -> state
f_wiki | extra | s4n:wiki: - -> weekly_world_news | gold has no :wiki
g_reentrancy | extra | s4p/publication -part-> s4x7/网络版: - -> s4p/publication -part-> s4x7/网络版 | gold has no such reentrancy
g_reentrancy | extra | s4x6/发行-01 -arg0-> s4p/publication: - -> s4x6/发行-01 -arg0-> s4p/publication | gold has no such reentrancy
a_event_found | missing | s5x5: 富-01 -> - | no node in the prediction matches it
a_entity_found | missing | s5x8: 上 -> - | no node in the prediction matches it
d_core_args_abstract | partial | s5h: arg1 s5x4/报纸; arg2 s5x5/富-01; arg3 s5x7/最 -> arg1 s5x4/报纸; arg2 s5x6/创意; arg3 s5x7/最; arg5 s5x9/历史 | missing arg2 s5x5/富-01; extra arg2 s5x6/创意; extra arg5 s5x9/历史
d_peripheral_entity | missing | s5x4: temporal s5x8/上 -> - | missing temporal s5x8/上
d_peripheral_entity | wrong | s5x9: place s5c/country -> mod s5c/country | place s5c/country: predicted as mod
e_peripheral_labels | wrong | s5x9 -place-> s5c: place -> mod | place -> mod
f_wiki | extra | s5c:wiki: - -> united_states | gold has no :wiki
h_temporal | wrong | 发行-01 «发行» (snt1 s1x3 = pred s1x4): document-creation-time :before 发行-01 «发行» (snt1 s1x3 = pred s1x4); 闻名-01 «闻名» (snt1 s1x7 = pred s1x7) :contained 发行-01 «发行» (snt1 s1x3 = pred s1x4) -> 停止-01 «停止» (snt1 s1x4 = pred s1x3) :before 发行-01 «发行» (snt1 s1x3 = pred s1x4) | wrong parent and relation
h_temporal | wrong | 停止-01 «停止» (snt1 s1x4 = pred s1x3): 发行-01 «发行» (snt1 s1x3 = pred s1x4) :overlap 停止-01 «停止» (snt1 s1x4 = pred s1x3) -> document-creation-time :before 停止-01 «停止» (snt1 s1x4 = pred s1x3) | wrong parent and relation
h_temporal | wrong | 报导-01 «报导» (snt1 s1x8 = pred s1x8): 发行-01 «发行» (snt1 s1x3 = pred s1x4) :overlap 报导-01 «报导» (snt1 s1x8 = pred s1x8) -> document-creation-time :before 报导-01 «报导» (snt1 s1x8 = pred s1x8) | wrong parent and relation
h_temporal | missing | 查证-01 «查证» (snt2 s2x13 = pred s2x13): 经-01 «未经» (snt2 s2x8 = pred s2x8) :overlap 查证-01 «查证» (snt2 s2x13 = pred s2x13) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 停刊-01 «停刊» (snt4 s4x = pred s4x): document-creation-time :depends-on 停刊-01 «停刊» (snt4 s4x = pred s4x) -> document-creation-time :overlap 停刊-01 «停刊» (snt4 s4x = pred s4x) | right parent, wrong relation
h_temporal | wrong | 称为-01 «称为» (snt5 s5x = pred s5x): document-creation-time :depends-on 称为-01 «称为» (snt5 s5x = pred s5x) -> document-creation-time :overlap 称为-01 «称为» (snt5 s5x = pred s5x) | right parent, wrong relation
h_temporal | missing | 富-01 «最富» (snt5 s5x5): 称为-01 «称为» (snt5 s5x = pred s5x) :overlap 富-01 «最富» (snt5 s5x5) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | wrong | 查证-01 «查证» (snt2 s2x13 = pred s2x13): author :partial-affirmative 查证-01 «查证» (snt2 s2x13 = pred s2x13) -> author :full-affirmative 查证-01 «查证» (snt2 s2x13 = pred s2x13) | right parent, wrong relation
i_modal | extra | have-degree-91 (snt5 s5h = pred s5h): - -> author :full-affirmative have-degree-91 (snt5 s5h = pred s5h) | gold gives this node no modal parent
i_modal | missing | 富-01 «最富» (snt5 s5x5): author :full-affirmative 富-01 «最富» (snt5 s5x5) -> - | the prediction has no node for it (its sentence graph lacks it)
j_coref_chain | extra | country (snt1 s1c = pred s1c): - -> country (snt5 s5c = pred s5c) | gold links it to nothing
j_coref_chain | extra | country (snt5 s5c = pred s5c): - -> country (snt1 s1c = pred s1c) | gold links it to nothing

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.