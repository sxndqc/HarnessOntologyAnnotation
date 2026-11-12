<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 19541). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. The title marks 《 》 around a publication's name are name tokens: they are the first and last `:opN`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
a numeral + classifier phrase is kept too, also with 一 (一份, 一个, 三本书 → `书 :quant 3 :unit (b / 本)`). Check with `search_annotations` when unsure.

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
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91`. Both take `:ARG1` and `:ARG2`, never `:opN`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; 以 X 而 Y (*known for X*) → Y `:reason` X. When such a clause describes a noun (e.g. the predicate noun of a 是 sentence), attach it inside that noun as `:ARG1-of`, not as a new conjunct; *in order to* (为了)
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

Frequent choices:
- A country or region modifying a noun (美国小报, *a US paper*) → `:place`, not `:mod`.
- A channel or medium (电视, 网络, *TV*) → `:medium`.
- A version, edition or part of a publication or thing (X的纸本) → `:part-of`, not `:possessor`.
- Adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs such as 目前 → `:temporal` on that event. Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`).
- A modifier shared by coordinated nouns goes on each conjunct, as one node re-used by re-entrancy, not on the `and` node.
- Add an implicit or re-entrant argument only when the text expresses it.
- Check the PropBank argument order: for 属-02 the thing owned is `:ARG0` and the owner `:ARG1`.

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

- A typical or repeated activity of a person or institution (publishing 发行, broadcasting, selling, collecting stories 综合) is `habitual`. This holds even without a frequency word, and even with 了, when the clause describes what the entity does in general.
- 已经 + a change-of-state verb used as a modifier (已经停止发行的小报) is `state`: it is the entity's resulting condition.
- A passive naming or evaluation (被称为, 被誉为) is `performance`.
- 未经 (*without having undergone*) is `process`.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2).
- `:mode imperative` (commands, 请, 别), `:mode interrogative` (questions; the questioned argument is
  `amr-unknown`, a yes/no question gets `:polarity amr-unknown`), `:mode expressive` (interjections).
- A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91`. Its roles are `:ARG1` the entity, `:ARG2` the property, and `:ARG3` the degree (最/更, `most`/`more`).
- An adjectival chengyu before 的 (荒诞不经的内容) is a `:mod`, not an event.
- `:degree` is only for intensifiers and downtoners (*very, too*; 很, 非常, 太), as a concept:
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
  (*nowadays*, 现在, 目前) is also anchored to now: `(document-creation-time :depends-on s4t)`, then its event `(s4t :overlap s4e)`. Use `past-reference` / `present-reference` / `future-reference` only for vague times not tied to the moment of writing.
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :contained s1e)`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent; a purpose is `:after` its main event.
- Annotate event–event relations only when they are clear.
- Give no temporal parent to a copular predicate (`identity-91` for 是) or to a property used as a modifier.
- Within a sentence, anchor the dependent events (relative clauses, the 以…而 result, a second conjunct) to the sentence's main anchoring event, not each to `document-creation-time`. Example: `(document-creation-time :before s1f)`, then `(s1f :overlap s1s)` and `(s1k :contained s1f)`.

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
- `(earlier :same-event later)`: two mentions of the same event. Use it only when the participants are the same. *The paper stopped publishing* and *its print edition stopped* are different events.
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

- Classifier (2.2): 一份小报 → `(x / 小报 :quant 1 :unit (u / 份))`.
- Title marks (2.2): 《世界新闻周报》 → `:name (n / name :op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》")`.
- but-91 (2.5): 不过… → `(b / but-91 :ARG1 ... :ARG2 ...)`.
- 以…而闻名 (2.5): a tabloid known for its reports → `(x / 小报 :ARG1-of (k / 闻名-01 :reason (r / 报导-01 :ARG0 x)))`.
- 由于 (2.5): 由于…内容 → `:reason (c / 内容 ...)`.
- Roles (3): 美国小报 → `:place (c / country ...)`; 电视节目 → `(p / 节目 :medium (t / 电视))`; 都经过 → `(j / 经-01 :mod (d / 都))`.
- Shared modifier (3): 奇怪的新闻与专栏 → `(a / and :op1 (n / 新闻 :mod (q / 奇怪)) :op2 (z / 专栏 :mod q))`.
- 属 (3): 属自己的节目 → `(p / 节目 :ARG0-of (s / 属-02 :ARG1 x))`.
- Aspect (4.1): 发行 (a paper's publishing) → `:aspect habitual`; 已经停止发行的 → 停止 `:aspect state`; 被称为 → `:aspect performance`.
- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.
- 历史上 (4.2): 美国历史上 → `:temporal (s / 上 :op1 (h / 历史 ...))`.
- Temporal (5.1): 目前停刊 → `(document-creation-time :depends-on s4t)` `(s4t :overlap s4e)`; no temporal triple for `identity-91`.

</instruction>

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 82.1)
<critique>
# Review of the annotation of the 5-sentence 《世界新闻周报》 document: error patterns, causes, and changes to the instruction

The annotator did most of the sentence-level work well; the losses are at the document level and in a few repeated habits. The checks that lost the most were temporal (F 35), reentrancy (precision 56), aspect (F 83), core arguments of events (F 90), coreference precision (71), and wiki and polarity (precision 0). The problems are listed below from most to least costly.

---

## 1. Temporal anchoring (h_temporal F 35: 7 of about 10 gold events wrong, missing or extra; plus one k_doc_format error)

There are four sub-patterns.

**a) Triple direction reversed, giving a node two parents (snt 1).** The annotator wrote `(document-creation-time :before s1f)` and also `(s1b :contained s1f)`. The second triple makes 报导 the *parent* of 发行, so 发行 ends up with two parents (the k_doc_format error). 报导 and 闻名 were also given the wrong roles.
- Gold: `(document-creation-time :before s1x3) (s1x3 :overlap s1x4 停止) (s1x3 :overlap s1x8 报导) (s1x7 闻名 :contained s1x3)`
- Cause: section 5.1 says "parent first, child second", but its example `(s1k :contained s1f)` has the anchoring event in the *child* slot. That contradicts the rule just before it. The annotator copied the shape and put the wrong event in it.
- Fix: state in bold that **the first element of a triple is the parent and every event has exactly one parent**. Replace the example with the full snt-1 pattern: "the main event 发行 → DCT; 停止 and 报导 → `(发行 :overlap X)`."

**b) Dependent events sent to DCT, or left without a parent.**
- snt 1: `(document-creation-time :overlap s1t)` for 停止. The rule "anchor dependents to the main event" already says this should be `(s1f :overlap s1t)`; the annotator did not follow it.
- snt 2: 查证-01 had no parent. Gold: `(s2x8 :overlap s2x13)`.
- snt 5: 富-01 inside have-degree-91 had no parent. Gold: `(s5x :overlap s5x5)`.
- Cause: the line "Give no temporal parent to … a property used as a modifier" was over-applied to *event concepts that carry `:aspect`*.
- Fix: "Every node with a PropBank sense and an `:aspect` (including 富-01 under have-degree-91 and 查证-01 inside a noun) gets a temporal parent, normally `(main-event :overlap X)`. Only plain `:mod` words with no sense, and identity-91, get none."

**c) A cross-sentence anchor used where gold uses DCT (snt 2).** The annotator wrote `(s1f :overlap s2z)`. Gold has `(document-creation-time :before s2x)`.
- Fix: "Anchor each sentence's main event to `document-creation-time` unless the text marks a relation to an earlier event (然后, 之后, 同时 …)."

**d) The rule for 目前 and similar time words is wrong for this data (snt 4, and snt 5 by analogy).** The instruction's own example `(document-creation-time :depends-on s4t)(s4t :overlap s4e)` cost three units: the parent of 停刊, the parent of 继续, and an extra parent for 目前.
- Gold gives 目前 no temporal node at all. It writes `(document-creation-time :depends-on s4x)` on the main event and `(s4x :overlap s4x2)` for the second conjunct.
- Snt 5 gold likewise has `(document-creation-time :depends-on s5x)`.
- Fix: rewrite the 目前 example and rule as: "Vague present adverbs (目前, 现在) stay `:temporal` in the graph, but at the document level the main event attaches directly: `(document-creation-time :depends-on <main event>)`. The other events of the sentence go `(main :overlap X)`. Do not give the adverb its own triple."

---

## 2. Implicit arguments and extra re-entrancies (g_reentrancy precision 56, 4 extra; d_core_args_event 3 units; d_peripheral_entity 2)

**Snt 1, 已经停止发行的小报.** The annotator wrote `小报 :ARG0-of (停止-01 :ARG1 (发行-01 :ARG1 s1x))`. Gold nests it as a chain of relative clauses:
```
(s1x / 小报 :ARG1-of (s1x3 / 发行-01
                     :ARG1-of (s1x4 / 停止-01 :mod (已经) :aspect state)
                     :aspect habitual))
```

**Snt 4.** The annotator added `发行-01 :ARG0 s4n` and `网络版 :part-of s4n`. Neither is in the text, and gold has neither: it has `(s4x6 / 发行-01 :ARG1 (s4x7 / 网络版))`. The ":part-of for a version or edition" rule was applied with no written X的.

**Snt 2, 其中.** The annotator rendered it as `and :part s2c`. Gold has `内容 :mod (其中)`. Building it as a part relation also broke the `:ARG0` of 经-01 (one missing core argument, one extra re-entrancy).

**Why:** the instruction does say "Add an implicit or re-entrant argument only when the text expresses it", but it is a one-line bullet, and the examples (以…而闻名 with `:ARG0 x`, 属自己 with `:ARG1 x`) push towards re-entrancy.

**Changes to the instruction:**
- Add the 已经停止发行的小报 structure above as an example. State: "for V1+V2的N (停止发行的), N attaches to the inner verb (`:ARG1-of 发行`) and the outer verb takes the inner verb as `:ARG1-of`."
- Add: "Use `:part-of` only when the owner is written in the phrase (X的纸本). 网络版 alone gets no owner. Do not copy a subject into a second clause unless a word (自己, 其, a pronoun) refers to it."
- Add: "其中 → `:mod (其中)` on the noun it introduces."

---

## 3. Aspect (c_aspect F 83: 3 units)

**identity-91 had no `:aspect` (snt 1).** Gold has `:aspect state`. It also gets `(author :full-affirmative s1i2)`, which the annotator also missed (an i_modal unit). The cause is that the line "no temporal parent for identity-91" was read as "not an event".
- Fix: "identity-91 and the other -91 predicates carry `:aspect state` and a modal triple. Only the temporal triple is left out."

**曾经…拥有过 annotated `performance`; gold has `state`.** The 了/过 → performance rule overrode the lexical state verb.
- Fix: "Stative verbs (拥有, 有, 是, 在, 属) stay `state` even with 过 / 曾经 / 了."

**已经停刊 as a main predicate annotated `state`; gold has `performance`.** The annotator stretched the rule "已经 + change-of-state verb as a modifier is state" to a main clause.
- Fix: add "When the 已经 + change-of-state verb is the main predicate (纸本已经停刊), use `performance`. `state` applies only to the 的-modifier."

---

## 4. `:wiki` added (f_wiki: 4 extra, precision 0)

The annotator added `:wiki "Weekly_World_News"` (twice) and `:wiki "United_States"` (twice). Gold has none. In other Chinese gold data, `:wiki` appears only in about two sentences, and in a non-standard form there.

Fix: replace "an optional `:wiki`" with "**Do not add `:wiki`** in Chinese documents."

---

## 5. Coreference over-linking (j_coref_chain precision 71: 2 units)

The annotator linked the 美国 of snt 1 and the 美国 of snt 5 with `(s1c :same-entity s5u)`. Gold links only the main participant chain (周报 / newspaper across all five sentences), which the annotator got fully right.

Fix: "Link the document's participant chains. Do not link a country or place name that is used only as a modifier (`:place` of 小报, of 历史) to another such mention."

---

## 6. Smaller items

**Coordination grouping (snt 1).** Gold groups 奇闻轶事, written without 、, as an inner `and`: `(and :op1 (and :op1 奇闻 :op2 轶事) :op2 传奇 :op3 新闻)`. The annotator made a flat four-way `and`, which cost one missing entity node.
- Fix: "Nouns run together without 、 form their own inner `and`; 、 separates the outer conjuncts."

**Polarity on 未经 and the modal strength of 查证 (snt 2).** Gold gives 经-01 no `:polarity` but does mark it full-negative at the document level. It also gives 查证 `partial-affirmative`. Other Chinese gold data does use `:polarity -` for 未, so this looks like a quirk of this one gold document. I would **not** change the polarity rule.

**The 查证 structure (snt 2).** Gold wraps 查证 in `程序 :ARG0-of (identity-91 :ARG1 查证)`. The annotator's `:mod 查证-01` is a reasonable alternative. Leave this alone, or at most add the gold pattern as an example of "a 程序/过程 that is the event" (程序 :ARG0-of identity-91 :ARG1 event).

---

## What to keep (these worked)

- **Senses and concepts:** event, concept and sense checks were all at 100. Keep the instruction to look up each predicate in PropBank, and the `<word>-00` fallback.
- **Example-driven rules:** these were all reproduced exactly and scored fully:
  - title marks as name tokens;
  - the classifier as `:quant 1 :unit 份/个`;
  - `:place` for 美国小报;
  - `:medium 电视`;
  - `:part-of` in 纸本;
  - the shared modifier re-used across 新闻 and 专栏;
  - the 属-02 argument order;
  - the 以…而闻名 → `:reason` structure;
  - the 由于 → `:reason` noun;
  - have-degree-91 for 最富创意;
  - 历史上 as `:temporal (上 :op1 历史)`;
  - `but-91` with `:ARG1`/`:ARG2`;
  - 已经, 都, 也, 仍 as `:mod` on the event.
- **Aspect values:** habitual for 发行, 综合 and 报导; process for 未经/查证; performance for 被称为; activity for 继续; state for the modifier 停止. Keep these rules.
- **Modal and coreference basics:** `(root :modal author)` plus author full-affirmative, full-negative for the negated event, and the 周报 coreference chain across sentences. Keep these.
</critique>

# Earlier edits
- batch 1, reflection 1 (11/11 edits applied): Fix classifier rule (keep 一份/一个 as :quant+:unit), title marks as name tokens, but-91 :ARG1/:ARG2, 由于→:reason, 以X而Y→:reason, non-core role rules (:place for countries, :medium, :part-of, adverbs as :mod, shared modifiers on conjuncts, no invented arguments, 属 argument order), habitual/state/performance aspect rules, have-degree-91 for superlatives and chengyu as :mod, temporal rules (no parent for  -> AnCast++ comp 82.1 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.