<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 15877). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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


</instruction>

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 57.0)
<critique>
# Review of the UMR annotation of the 《世界新闻周报》 document (5 sentences), with changes for the instruction

Problems are ordered by cost, most costly first. I did not use the tools for this review. Each judgement below rests on the gold annotation and the judge's unit list.

## 1. Aspect of publishing and "already stopped" events (c_aspect F 60; 6 wrong units)
**What went wrong:**
- **发行 is a habitual event.** 发行 in snt1 was annotated `endeavor` and in snt4 `activity`; gold has `habitual` both times. Publishing a newspaper is a repeated event.
- 综合 (snt2, "the weekly brings together all kinds of stories") was annotated `performance`, apparently triggered by 了. Gold has `habitual`, because it describes what the paper regularly does.
- **已经停止 is a resulting state.** 已经停止 (snt1) was annotated `performance`; gold has `state`. As a relative-clause modifier, "already stopped" describes the paper's current condition.
- 未经 (snt2) was annotated `performance`; gold has `process`.
- 被称为 (snt5) was annotated `state`; gold has `performance`. It is a completed act of naming.

**Why it happens:** the aspect table maps 了/past to `performance` and present-tense processes to `activity`. It never says that a characteristic, repeated activity of an institution is `habitual` even without 经常 or 每天.

**Change:**
- Add to 4.1: "Typical or repeated activities of a person or institution (publishing, broadcasting, selling, collecting content) are `habitual` even without a frequency word, and even with 了 when the clause describes what the entity does in general."
- Add: "已经 + change-of-state verb used as a modifier (已经停止发行的小报) is `state`."
- Add: "A passive naming or evaluation (被称为, 被誉为) is `performance`."

## 2. Temporal over-annotation and wrong anchors (h_temporal F 47; about 11 units)
**What went wrong:**
- **States and descriptions were each attached to the document creation time.** Gold gives no temporal parent to the copular `identity-91` (snt1), to the time word 目前 (snt4) or to a modifier-like state (荒诞不经, snt5). The annotator added `(document-creation-time :overlap s1i)`, `(present-reference :depends-on s4x2)` and `(s5x :overlap s5x10)`.
- **Same-sentence events were not chained to the clause's main event.** In snt1 gold anchors the other events on 发行:
  - `(document-creation-time :before s1x3)`
  - `(s1x3 :overlap s1x4)` (发行 → 停止)
  - `(s1x7 :contained s1x3)` (闻名 inside the publishing period)
  - `(s1x3 :overlap s1x8)`

  The annotator instead did `(s1x3 :after s1x4)` (停止 after 发行) and `document-creation-time :overlap 闻名`.
- In snt4 gold uses `(document-creation-time :depends-on s4x)` and then `(s4x :overlap s4x2)`. The annotator used 目前 as the parent of both clauses.

**Change to 5.1:**
- "Do not give a temporal parent to a copular/identity predicate or to a property used as a modifier."
- "Within a sentence, anchor the dependent events (relative clauses, the 以…而 result, the second conjunct) to the sentence's main anchoring event rather than each to the document creation time."
- "A vague time word like 目前 is a `:temporal` modifier of the event and needs no `present-reference` triple."

## 3. Non-core role choice and attachment (d_peripheral_event F 33, d_peripheral_entity F 48, e_peripheral_labels; about 20 units)
**What went wrong:**
- **Country modifiers.** 美国小报 and 美国历史 were given `:mod country`; gold uses `:place (s1c / country …)`.
- 电视节目 was given `:mod`; gold uses `:medium (s3x5 / 电视)`.
- 《世界新闻周报》的纸本 was given `:possessor`; gold uses `:part-of`.
- **以…而闻名.** The annotator built a separate `and :op2 闻名 :manner 报导`. Gold makes it a relative modifier of the tabloid, with 报导 as the reason: `:ARG1-of (s1x7 / 闻名-01 :reason (s1x8 / 报导-01 :ARG0 s1x …))`.
- **由于 → :reason.** 由于 was annotated `:cause`; gold uses `:reason (s5x10 / 内容 …)`.
- **Adverbs.** 已经 (snt1 and snt4) got no node at all; gold keeps it as `:mod` on the event.
- 都 was put on the noun 内容; gold puts `:mod (s2x16 / 都)` on 经-01.
- 目前 was put on `but-91`; gold puts it on 停刊-01.

**Change:**
- In 2.5, change "because (因为, 由于) → :cause" to `:reason`. Add "以 X 而 Y (known for X) → Y `:reason` X".
- In section 3, add short rules:
  - A country or region modifying a noun → `:place`.
  - The channel or medium (电视, 网络) → `:medium`.
  - A version or part of a publication → `:part-of`.
  - Adverbs 已经, 都, 仍, 也 → `:mod` nodes on the event they modify, never dropped and never moved onto a noun or onto the discourse connective.
- Add: "A 以…而闻名 / 而 clause modifying the subject of a copular sentence attaches inside the predicate noun, not as a new conjunct."

## 4. Classifiers with 一 (a_entity_found, c_other_attributes; about 6 units)
**What went wrong:** 一份 and 一个 were dropped. Gold has `:quant 1 :unit (s1x5 / 份)` and `:quant 1 :unit (s3x7 / 个)`.

**Why it happens:** the instruction itself is wrong here. It says "an ordinary classifier (个, 本, 只, 位) is dropped".

**Change:** rewrite the classifier rule in 2.2: "A numeral + classifier phrase (一份, 一个, 三本) is kept: `:quant N :unit (x / <classifier>)`."

## 5. Name tokens with book-title marks (f_name_tokens F 50; 4 units in all)
**What went wrong:** 《世界新闻周报》 was annotated `:op1 "世界" :op2 "新闻" :op3 "周报"`. Gold includes the marks: `:op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》"`. This failed in snt1 and snt4 (2 name units), and it also caused 2 granularity units.

**Change:** add to 2.2: "In Chinese, the title marks 《 》 around a publication's name are name tokens: include them as the first and last `:opN`."

## 6. Superlatives and chengyu modifiers (a_event_found, d_core_args; about 5 units)
**What went wrong:**
- 最富创意 was annotated `富-01 :degree 最`, with `:ARG0` 报纸. Gold has:
  ```
  (s5x4 / 报纸 :ARG1-of (s5h / have-degree-91 :ARG2 (s5x5 / 富-01 :ARG1 (s5x6 / 创意)) :ARG3 (s5x7 / 最)))
  ```
- 荒诞不经的内容 was made an event (`荒诞不经-01`, which then got temporal and modal triples). Gold has `:mod (s5x11 / 荒诞不经)`.
- 美国历史上 lost the 上 node. Gold has `:temporal (s5x8 / 上 :op1 (s5x9 / 历史 …))`.

**Change:**
- In 4.2, replace "`:degree` for … most, 最" with: "A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91` (`:ARG1` the entity, `:ARG2` the property, `:ARG3` 最/更 or `most`/`more`). Only intensifiers (很, 非常, 太) are `:degree`."
- Add: "An adjectival chengyu before 的 is a `:mod`, not an event."

## 7. Connective roles (e_core_labels; 2 units)
**What went wrong:** 不过 was annotated `but-91 :op1/:op2`; gold uses `:ARG1`/`:ARG2`.

**Change:** in 2.5, state "`but-91` and `contrast-91` take `:ARG1` and `:ARG2`, not `:opN`".

## 8. Distributive modifiers and argument direction (g_reentrancy F 18)
**What went wrong:**
- 各式各样奇怪的新闻与专栏: the annotator put the adjectives on the `and` node. Gold puts `:mod` on each conjunct and re-uses the same nodes (re-entrancy).
- 属自己的节目: the annotator had `属-02 :ARG0 周报 :ARG1 节目`. Gold reverses it: `节目 :ARG0-of (属-02 :ARG1 s3x2)`. The annotator apparently did not follow the PropBank argument structure.
- Extra implicit arguments were added: `发行 :ARG0 newspaper` (snt4) and `查证 :ARG1 内容` (snt2). Gold leaves them out; in 查证 the ARG1 is 新闻.

**Change:**
- "A modifier shared by coordinated nouns goes on each conjunct (re-entrancy), not on the `and` node."
- "Add a re-entrant argument only when the text expresses it."
- "Check the PropBank argument order for belong-type verbs (属): the thing owned is ARG0, the owner ARG1."

## 9. Smaller issues
- **Coreference across 停止 and 停刊.** The annotator linked them with `:same-event` (2 extra units). They are different events: the whole paper stopped publishing in snt1, but only the print edition stopped in snt4. Add: "Link `:same-event` only when the participants are the same."
- **未经 and 查证.** The annotator put `:polarity -` on 经 and gave 查证 `full-negative`. Gold has no polarity node on 经 and gives 查证 `partial-affirmative`. This is low cost (2 units) and gold is not fully consistent here, so it does not justify a rule change.

## What to keep
- **Senses:** event senses scored 100%.
- **Concepts:** event and entity detection and concept choice were 94–97%, and Chinese words were used as concepts throughout.
- **Structure:** `identity-91` for 是 and the and/but structure for the second sentence and the 不过 sentence were right.
- **Modal:** author `full-affirmative` triples were right (modal F 91).
- **Coreference:** the entity chain 周报 → 周报 → newspaper → 周报 across all sentences was correct (recall 100%).
- **Format:** the document-level format was perfect.

The instruction's push to look things up in PropBank and the gold data should stay. It would also have caught items 4 and 8.
</critique>

# Earlier edits
(none: the first edit)

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.