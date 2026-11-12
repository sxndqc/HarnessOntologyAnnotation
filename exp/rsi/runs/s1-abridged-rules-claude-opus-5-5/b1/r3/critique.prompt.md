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

Only modal auxiliaries are dropped. Adverbs are nodes:
- aspectual and scope adverbs (*already, still, also, all*; 已经, 仍, 也, 都) are `:mod` on the event;
- past-time adverbs (*once, formerly*; 曾, 曾经) are `:temporal` (in the graph only; they get no temporal triple, see 5.1);
- a partitive like 其中 (*among them*) is `:mod` on the noun;
- a locative postposition after a time or period noun (X 时, X 中, X 以来, X 上 as in *in the history of ...*) is a `:temporal` node for the postposition with the noun as `:op1`, attached to the word it scopes over (often the head noun).

**Concept names.** An English event is its PropBank roleset (`deny-01`, `look-up-05`). A Chinese event is the
Chinese word as written with its Chinese PropBank sense (`拥有-01`, `执行-01`); a Chinese predicate that is not
in PropBank is `<word>-00`. Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :name (n / name :op1 "Russia"))`: an entity-type concept and `:name` with one `:opN` per word of the name.

- Do not write `:wiki`.
- For a titled work in title brackets 《 》, the brackets are their own first and last `:op`s.
- A country or place name modifying a common noun (X 的历史, an X company) is `:place`, not `:mod`.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a numeral + classifier or measure word gives `:quant N` plus `:unit <classifier>` on the noun, for real measure words and ordinary classifiers (个, 本, 份, 位) alike, and also when the number is 1 (一个X → `X :quant 1 :unit 个`).

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
| X is the most/more Adj (superlative, comparative) | `have-degree-91` | `:ARG1` X, `:ARG2` property, `:ARG3` degree word (`most`, `more`), `:ARG5` set compared to |
| cause, reason | `have-cause-91` / `:cause` | |

Role nouns are reified the same way: *the president of Russia* →
`(p / person :ARG1-of (h / have-org-role-92 :ARG2 (c / country ...) :ARG3 (p2 / president)))`;
*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.

Use an abstract predicate only when there is no lexical predicate. A Chinese verb with its own PropBank frame keeps that frame and its roles. For example, a possession or belonging verb such as 属于 or 拥有 is `属于-01` / `拥有-01`, not `belong-91` / `have-91`. Do not use `:degree` on a property verb for a superlative; use `have-degree-91`. Its `:ARG2` is the property word itself. If the property is a verb with its own object (*rich in X, full of X*, 富X, 充满X), keep that verb as an event with its object (`(r / V-01 :ARG1 X :aspect state)`) and put it under `:ARG2`; do not drop the verb or put the object noun there. Use `:ARG5` only for an explicit comparison set (*among N, of all N*, 在…中); a scope like *in history* is a `:temporal` postposition node (2.1), not `:ARG5`.

**Chinese role numbering.** For every Chinese predicate, look up its Chinese PropBank frames. Choose the sense whose role descriptions fit (the belonging/membership sense of a verb is often not -01), and use exactly the numbered roles that roleset defines. Many Chinese intransitive and change-of-state verbs have only `:ARG0` (the thing that ceases, changes or acts). Do not default the theme to `:ARG1` by English habit.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. Do not add nodes for Chinese zero subjects or objects or for other unexpressed participants: leave the role out.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为) → `:cause`; 由于 and the frame 以…而 → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span.

A compound made of two coordinated nouns (AB where A and B are parallel nouns, e.g. a four-character N1N2 meaning *N1 and N2*) is split: `(a / and :op1 N1 :op2 N2)`. A true idiom stays one concept. When such a parallel-noun pair is one item of a longer list, nest it as its own `and` inside the outer `and`.

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

Attachment rules:
- **Unexpressed participants.** Do not fill a roleset slot with a participant the text does not express. Re-enter a node only when the text itself expresses that participant in that role. A subject shared through a control, serial or purpose/means frame (以 X 而 Y, *known for doing X*, *try to X*) counts as expressed: re-enter it as the subject of the embedded verb too.
- **Aspectual verb in a relative clause.** When a head noun is modified by an aspectual verb plus another verb (*the X that stopped/began doing Y*), the noun is an argument of the inner verb only: `(x / X :ARG1-of (p / V-01 :ARG1-of (s / stop-01)))`. It is not an argument of the aspectual verb as well. Check the aspectual verb's roleset.
- **Shared modifiers.** A modifier shared by coordinated nouns (*various A and B*) goes on each conjunct by re-entrancy, not on the `and` node. Do not add `:subset` there.
- **Describing clauses.** A clause that goes on describing the predicate noun of a copular sentence (*X is a Y, known for Z*) attaches under that noun, e.g. as `:ARG1-of`. It is not a separate top-level conjunct.
- **Parts and media.** A physical edition or part of a publication is `:part-of` it, not `:possessor`. A medium noun (TV, 网络) modifying a program or product is `:medium`.

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

Further aspect rules:
- **Repeated activity of an institution or periodical** (publishing, broadcasting, reporting, what it regularly contains or covers) is `habitual`, even with 了 or other completion marking.
- **already + an aspectual stop verb governing another event** (已经停止 doing X) describing the current situation is `state`. A lexical termination verb with no governed event (a publication ceased, an organization dissolved) is `performance`, even with 已经.
- **Abstract predicates:** `identity-91` gets `:aspect state`; `have-degree-91` gets no `:aspect` (the event under its `:ARG2` does).
- **A naming or evaluation passive** (*is called / is regarded as*, 被称为, 被誉为) is `performance`.
- **A negated event with a nominal event object** (没有经过X) is `process`.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2). Exception: when the negation is fused into one verb word (未经 type), write no `:polarity -`; mark only `full-negative` at the document level.
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
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`; a vague past or future one on `past-reference` / `future-reference`. A vague present adverb (*currently, nowadays*, 现在, 目前) gets no temporal triple of its own.
- Then pick **one anchor per sentence**: the matrix (main) event. Only the anchor is linked to the outside: (1) to a time expression of its clause, if there is one (`(s1t :contained s1e)`); else (2) to an event of an earlier sentence that is a clear reference time (`(s2c :before s3a)`); else (3) to
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- Every other event of the sentence takes the anchor, or the event or entity-modifying event it depends on, as its parent. Use `:overlap` unless the order is explicit (`:before`/`:after`; a purpose is `:after` its main event). This covers:
  - subordinate, complement, coordinated and cause/reason clauses;
  - relative-clause verbs and event nominals;
  - negated events;
  - events inside noun-phrase modifiers.
  Do not give these their own `document-creation-time` link.
- Past-time adverbs (*once, formerly*, 曾, 曾经) are not reference times: give them no triple and link their event directly, `(document-creation-time :before e)`.
- A completed event whose result describes the present situation (a status reached, a name or evaluation given: a naming/evaluation passive, 已经 + a completed change) is linked as `(document-creation-time :depends-on e)`.
- An aspectual verb (*stop, begin, continue*) and the event it governs are `:overlap`, never `:before`/`:after`.
- Every event node must get exactly one temporal parent. Two exceptions:
  - `identity-91` is left out of the temporal structure but still gets its modal parent. When a sentence's root is `identity-91`, choose as anchor the event inside the predicate noun that is most clearly placed in time, usually a completed past event (`(document-creation-time :before e)`). Reputation or property states of that noun are `:contained` in the anchor, and the other events are `:overlap` under it.
  - `have-degree-91` gets no temporal parent and no modal parent. The event under its `:ARG2` does get them.

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
- Link every mention of the main discourse entities. Do not build chains for incidental place names or other entities that occur only as modifiers (`:place`, `:mod`) in different sentences.
- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect` (`have-degree-91` excepted); negated events have `:polarity -` (fused negation verbs excepted).
- Every Chinese predicate uses the sense and numbered roles of its own PropBank roleset.
- Before writing `:coref`, drop every pair where both mentions are only `:place`/`:mod` modifiers.
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
        :name (s1n / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :ARG2 (s1x / 小报
        :quant 1
        :unit (s1u / 份)
        :place (s1c / country
            :name (s1n2 / name
                :op1 "美国"))
        :mod (s1c2 / 超市)
        :ARG1-of (s1f / 发行-01
            :ARG1-of (s1t / 停止-01
                :mod (s1y / 已经)
                :aspect state)
            :aspect habitual)
        :ARG1-of (s1w / 闻名-01
            :reason (s1b / 报导-01
                :ARG0 s1x
                :ARG1 (s1a / and
                    :op1 (s1a2 / and
                        :op1 (s1q / 奇闻)
                        :op2 (s1y2 / 轶事))
                    :op2 (s1c3 / 传奇
                        :mod (s1d / 都会))
                    :op3 (s1x2 / 新闻
                        :mod (s1e / 恶搞)))
                :aspect habitual)
            :aspect state))
    :aspect state)


# document level annotation:
(s1s0 / sentence
    :temporal ((document-creation-time :before s1f)
               (s1f :overlap s1t)
               (s1f :contained s1w)
               (s1w :overlap s1b))
    :modal ((root :modal author)
            (author :full-affirmative s1i)
            (author :full-affirmative s1f)
            (author :full-affirmative s1t)
            (author :full-affirmative s1w)
            (author :full-affirmative s1b)))


################################################################################
# meta-info
# :: snt2
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
Words: 该 周报 综合 了 各式各样 奇怪 的 新闻 与 专栏 ， 其中 许多 内容 都 未经 一般 的 新闻 查证 程序 。

# sentence level graph:
(s2a / and
    :op1 (s2z / 综合-01
        :ARG0 (s2p / 周报
            :mod (s2g / 该))
        :ARG1 (s2a2 / and
            :op1 (s2x / 新闻
                :mod (s2s / 各式各样)
                :mod (s2q / 奇怪))
            :op2 (s2l / 专栏
                :mod s2s
                :mod s2q))
        :aspect habitual)
    :op2 (s2w / 未经-00
        :ARG0 (s2n / 内容
            :quant (s2x2 / 许多)
            :mod (s2q2 / 其中))
        :ARG1 (s2c / 程序
            :mod (s2y / 一般)
            :mod (s2c2 / 查证-01
                :ARG1 (s2x3 / 新闻)
                :aspect process))
        :mod (s2d / 都)
        :modal-strength full-negative
        :aspect process))


# document level annotation:
(s2s0 / sentence
    :temporal ((document-creation-time :before s2z)
               (s2z :overlap s2w)
               (s2w :overlap s2c2))
    :modal ((root :modal author)
            (author :full-affirmative s2z)
            (author :full-negative s2w)
            (author :full-affirmative s2c2))
    :coref ((s1p :same-entity s2p)))


################################################################################
# meta-info
# :: snt3
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 该 周报 也 曾经 短暂 的 拥有 过 一个 属 自己 的 电视 节目 。

# sentence level graph:
(s3y / 拥有-01
    :ARG0 (s3z / 周报
        :mod (s3g / 该))
    :ARG1 (s3j / 节目
        :quant 1
        :unit (s3u / 个)
        :medium (s3d2 / 电视)
        :ARG1-of (s3s / 属-01
            :ARG2 s3z
            :aspect state))
    :mod (s3y2 / 也)
    :temporal (s3c / 曾经)
    :duration (s3d / 短暂)
    :aspect performance)


# document level annotation:
(s3s0 / sentence
    :temporal ((document-creation-time :before s3y)
               (s3y :overlap s3s))
    :modal ((root :modal author)
            (author :full-affirmative s3y)
            (author :full-affirmative s3s))
    :coref ((s2p :same-entity s3z)))


################################################################################
# meta-info
# :: snt4
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Words: 目前 《 世界 新闻 周报 》 的 纸本 已经 停刊 ， 不过 仍 继续 发行 网络版 。

# sentence level graph:
(s4b / but-91
    :ARG1 (s4t / 停刊-01
        :ARG0 (s4z / 纸本
            :part-of (s4p / publication
                :name (s4n / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :mod (s4y / 已经)
        :temporal (s4m / 目前)
        :aspect performance)
    :ARG2 (s4j / 继续-01
        :ARG1 (s4f / 发行-01
            :ARG1 (s4w / 网络版
                :part-of s4p)
            :aspect habitual)
        :mod (s4r / 仍)
        :aspect activity))


# document level annotation:
(s4s0 / sentence
    :temporal ((document-creation-time :depends-on s4t)
               (s4t :overlap s4j)
               (s4j :overlap s4f))
    :modal ((root :modal author)
            (author :full-affirmative s4t)
            (author :full-affirmative s4j)
            (author :full-affirmative s4f))
    :coref ((s3z :same-entity s4p)))


################################################################################
# meta-info
# :: snt5
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Words: 由于 其 荒诞不经 的 内容 ， 该 周报 被 称为 美国 历史 上 最富 创意 的 报纸 。

# sentence level graph:
(s5c / 称-01
    :ARG1 (s5z / 周报
        :mod (s5g / 该))
    :ARG2 (s5b / 报纸
        :ARG1-of (s5h / have-degree-91
            :ARG2 (s5f / 富-01
                :ARG1 (s5y / 创意)
                :aspect state)
            :ARG3 (s5m / 最))
        :temporal (s5s / 上
            :op1 (s5l / 历史
                :place (s5c2 / country
                    :name (s5n / name
                        :op1 "美国")))))
    :reason (s5n2 / 内容
        :possessor s5z
        :mod (s5h2 / 荒诞不经))
    :aspect performance)


# document level annotation:
(s5s0 / sentence
    :temporal ((document-creation-time :depends-on s5c)
               (s5c :overlap s5f))
    :modal ((root :modal author)
            (author :full-affirmative s5c)
            (author :full-affirmative s5f))
    :coref ((s4p :same-entity s5z)))



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
a_event_concept: R 88 / P 88 / F 88
a_entity_found: R 100 / P 100 / F 100
a_entity_concept: R 96 / P 96 / F 96
a_granularity: R 98 / P 98 / F 98
b_event_sense: R 92 / P 92 / F 92
c_aspect: R 93 / P 93 / F 93
c_other_attributes: R 100 / P 100 / F 100
d_core_args_event: R 93 / P 93 / F 93
d_core_args_abstract: R 100 / P 100 / F 100
d_peripheral_event: R 100 / P 100 / F 100
d_peripheral_entity: R 96 / P 96 / F 96
e_core_labels: R 96 / P 96 / F 96
e_peripheral_labels: R 100 / P 100 / F 100
f_name_tokens: R 100 / P 100 / F 100
g_reentrancy: R 80 / P 67 / F 73
h_temporal: R 88 / P 82 / F 85
i_modal: R 94 / P 94 / F 94
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_concept | wrong | s1n: newspaper -> publication | newspaper -> publication
a_granularity | missing | «新闻» 新闻: «新闻» 新闻 -> «《世界新闻周报》» publication | inside a wider predicted node
a_granularity | extra | «《世界新闻周报》» publication: «新闻» 新闻 -> «《世界新闻周报》» publication | wider than the gold node
a_event_found | missing | s2i2: identity-91 -> - | no node in the prediction matches it
a_event_concept | wrong | s2x8: 经 -> 未经 | 经 -> 未经
d_peripheral_entity | partial | s2x12: mod s2x15/一般 -> mod s2x13/查证-01; mod s2x15/一般 | extra mod s2x13/查证-01
b_event_sense | wrong | s3x6: 属-02 -> 属-01 | 属-02 -> 属-01
c_aspect | wrong | s3x:aspect: state -> performance | state -> performance
d_core_args_event | wrong | s3x6: arg0 s3x4/节目 -> arg1 s3x4/节目 | arg0 s3x4/节目: predicted as arg1
e_core_labels | wrong | s3x6 -arg0-> s3x4: arg0 -> arg1 | arg0 -> arg1
g_reentrancy | missing | s3x6/属-02 -arg1-> s3x2/周报: s3x6/属-02 -arg1-> s3x2/周报 -> - | the prediction has no such edge
g_reentrancy | extra | s3s/属-01 -arg2-> s3z/周报: - -> s3s/属-01 -arg2-> s3z/周报 | gold has no such reentrancy
a_entity_concept | wrong | s4n: newspaper -> publication | newspaper -> publication
g_reentrancy | extra | s4p/publication -part-> s4w/网络版: - -> s4p/publication -part-> s4w/网络版 | gold has no such reentrancy
a_event_concept | wrong | s5x: 称为 -> 称 | 称为 -> 称
h_temporal | partial | 发行-01 «发行» (snt1 s1x3 = pred s1f): document-creation-time :before 发行-01 «发行» (snt1 s1x3 = pred s1f); 闻名-01 «闻名» (snt1 s1x7 = pred s1w) :contained 发行-01 «发行» (snt1 s1x3 = pred s1f) -> document-creation-time :before 发行-01 «发行» (snt1 s1x3 = pred s1f) | agrees on part of the relations
h_temporal | extra | 闻名-01 «闻名» (snt1 s1x7 = pred s1w): - -> 发行-01 «发行» (snt1 s1x3 = pred s1f) :contained 闻名-01 «闻名» (snt1 s1x7 = pred s1w) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt1 s1x8 = pred s1b): 发行-01 «发行» (snt1 s1x3 = pred s1f) :overlap 报导-01 «报导» (snt1 s1x8 = pred s1b) -> 闻名-01 «闻名» (snt1 s1x7 = pred s1w) :overlap 报导-01 «报导» (snt1 s1x8 = pred s1b) | right relation, wrong parent
i_modal | wrong | 查证-01 «查证» (snt2 s2x13 = pred s2c2): author :partial-affirmative 查证-01 «查证» (snt2 s2x13 = pred s2c2) -> author :full-affirmative 查证-01 «查证» (snt2 s2x13 = pred s2c2) | right parent, wrong relation

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.