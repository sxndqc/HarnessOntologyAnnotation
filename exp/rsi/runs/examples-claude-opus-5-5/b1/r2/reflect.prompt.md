<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format and the tools' descriptions are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 19384). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. The title marks 《 》 around a publication's name are name tokens: include them as the first and last `:opN`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
an ordinary classifier is kept as the unit too: a numeral + classifier phrase (一份, 一个, 三本) → `:quant N :unit (x / <classifier>)` (三本书 → `书 :quant 3 :unit (b / 本)`; 一份小报 → `小报 :quant 1 :unit (f / 份)`).

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
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91` — `but-91` and `contrast-91` take `:ARG1` and `:ARG2`, never `:opN`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; 以 X 而 Y (*known for X*) → Y `:reason` X; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span. An adjectival chengyu modifying a noun (荒诞不经的内容) is a `:mod` concept, not an event (no aspect, no temporal or modal triples).

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
- A country or region modifying a noun (美国小报) → `:place (c / country ...)`, not `:mod`.
- The channel or medium (电视节目, 网络) → `:medium`.
- A version or part of a publication or object (X的纸本) → `:part-of`, not `:possessor`.
- Adverbs 已经, 都, 也, 仍, 还 are kept as `:mod` nodes on the event they modify. Never drop them, and never move them onto a noun or a discourse connective. A time word like 目前 likewise goes on the event it modifies.
- A relative clause or a 以…而 clause describing a noun attaches inside that noun (`:ARGn-of`), not as a new `and` conjunct.
- A modifier shared by coordinated nouns goes on each conjunct, not on the `and` node.
- Add a re-entrant or implicit argument only when the text expresses it.
- Always check the PropBank argument order: for 属-02 the thing that belongs is ARG0 and the owner is ARG1.

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

- Characteristic or repeated activities of a person or institution (publishing 发行, broadcasting, selling, compiling content 综合) are `habitual` even without a frequency word, and even with 了 when the clause describes what the entity does in general.
- 已经 + a change-of-state verb used as a modifier (已经停止发行的小报) is `state`: it describes a current condition.
- A passive act of naming or evaluation (被称为, 被誉为) is `performance`.
- 未经 (*without having undergone*) is `process`.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2).
- `:mode imperative` (commands, 请, 别), `:mode interrogative` (questions; the questioned argument is
  `amr-unknown`, a yes/no question gets `:polarity amr-unknown`), `:mode expressive` (interjections).
- A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91` (`:ARG1` the entity, `:ARG2` the property, `:ARG3` 最/更 or `most`/`more`).
- `:degree` only for intensifiers and downtoners (*very, too*; 很, 非常, 太) as a concept:
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
  (*nowadays*, 现在, 目前) is a `:temporal` modifier of its event in the graph. It gets no triple of its own: anchor the event instead (e.g. to `document-creation-time`).
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :contained s1e)`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent; a purpose is `:after` its main event.
- Annotate event–event relations only when they are clear.
- Do not give a temporal parent to a copular/identity predicate (`identity-91`) or to a property used as a modifier.
- Within a sentence, anchor the main event to `document-creation-time`, and anchor the dependent events (relative clauses, 以…而 reasons, related states) to that main event, not each to `document-creation-time`.

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
- `(earlier :same-event later)`: two mentions of the same event — only when the participants are the same. Stopping a whole paper and stopping only its print edition are different events.
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

- Classifier (2.2): 一份小报 → `(x / 小报 :quant 1 :unit (f / 份))`.
- Title marks (2.2): 《世界新闻周报》 → `:name (n / name :op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》")`.
- Aspect (4.1):
  - 发行 for a newspaper → `:aspect habitual`.
  - 已经停止发行的 (modifier) → `停止-01 :aspect state :mod (y / 已经)`.
  - 被称为 → `:aspect performance`.
- Roles (3):
  - 美国小报 → `小报 :place (c / country ...)`.
  - 电视节目 → `节目 :medium (t / 电视)`.
  - 周报的纸本 → `纸本 :part-of 周报`.
- 以…而闻名 (2.5, 3): 以报导…而闻名的小报 → `小报 :ARG1-of (w / 闻名-01 :reason (b / 报导-01 :ARG0 小报 ...))`.
- Reason (2.5): 由于…内容 → `:reason (n / 内容 ...)`.
- but-91 (2.5): 不过 → `(b / but-91 :ARG1 ... :ARG2 ...)`.
- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.
- Chengyu (2.6): 荒诞不经的内容 → `内容 :mod (h / 荒诞不经)`.
- Belong-type verb (3): 属自己的节目 → `节目 :ARG0-of (s / 属-02 :ARG1 周报)`.
- Temporal (5.1): main event 发行 → `(document-creation-time :before s1x3)` `(s1x3 :overlap s1x4)` `(s1x7 :contained s1x3)`. No triple for `identity-91`.

</instruction>

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 81.5)
<critique>
# Review of the annotator's UMR for the 《世界新闻周报》 document: costly error patterns and instruction changes

The annotator was strong on concepts and senses: event concepts 100, senses 100, name tokens 100, other attributes 100. Most of the loss is in five places:
- temporal: F 56
- reentrancy: F 50
- peripheral roles on entities: F 74
- coreference chains: precision 71
- core arguments: F 88–90

The patterns are below, most costly first.

---

## 1. Temporal parents: dependent events anchored to the wrong node (h_temporal, 7 units wrong, partial or extra)

**What went wrong**
- **Sentence 1, 停止.** The annotation had `(document-creation-time :overlap s1x4)`. Gold anchors it to the main event: `(s1x3 :overlap s1x4)`.
- **Sentence 1, 闻名.** The annotation had `(s1x5 :overlap s1x7)`. Gold has `(s1x7 :contained s1x3)`. This is exactly the instruction's own example, and it was not followed.
- **Sentence 4, 继续.** The annotation had `(document-creation-time :overlap s4x4)`. Gold has `(s4x :overlap s4x2)`: the second conjunct of `but-91` hangs on the first.
- **Sentence 2, 综合.** The annotation had `(s1x5 :overlap s2x)`, anchoring it to the previous sentence's event. Gold has `(document-creation-time :before s2x)`.
- **Sentences 4 and 5.** For 停刊 (sentence 4) and 称为 (sentence 5), gold writes `(document-creation-time :depends-on X)`. The annotation used `:before`. This looks like a gold convention for the main event of these sentences. It is less certain to generalise, so mention it only as what the gold data does.

**Why it happens**
- The rule "anchor dependent events to the main event" is stated, but it is not tied to the cases where it applies: a 已经-state modifier, the conjuncts of `but-91` or `and`, a `:reason` event.
- Nothing says that each sentence's main event anchors to `document-creation-time` and not to an event in an earlier sentence. The general rule (2) "an event before it that is a clear reference time" invited the cross-sentence anchoring.

**Change to the instruction.** Add to 5.1:
> "Each sentence's main (root-most) event anchors to `document-creation-time`. Do not anchor it to an event of an earlier sentence unless the text explicitly sequences them (然后, after that). Every other event in the sentence takes an event of the **same sentence** as its parent:
> - modifier states (已经停止) → `(main :overlap x)`;
> - the second conjunct of `and`/`but-91` → `(first :overlap second)`;
> - a 闻名-type state whose reason is the main event → `(state :contained main)`."

Then repeat the sentence 1 example triples verbatim as a mandatory pattern.

## 2. Arguments and reentrancies the text does not express (g_reentrancy: 3 extra; core args: 2 wrong)

**What went wrong**
- **Sentence 1, 已经停止发行的小报.** The annotation had `小报 :ARG0-of (停止-01 :ARG1 (发行-01 :ARG0 小报))`. Gold has:
  `(s1x / 小报 :ARG1-of (s1x3 / 发行-01 :ARG1-of (s1x4 / 停止-01 :mod (s1x6 / 已经) :aspect state) :aspect habitual))`
  The noun is the thing *published* (ARG1 of 发行). The stopping is predicated of the publishing, not done by the paper.
- **Sentence 4, 不过仍继续发行网络版.** The annotation added `:ARG0 s4p` on both 继续-01 and 发行-01. Gold leaves the subject out:
  `(s4x2 / 继续-01 :ARG1 (s4x6 / 发行-01 :ARG1 (s4x7 / 网络版)))`

**Why it happens.** "Add a re-entrant or implicit argument only when the text expresses it" is a single line, and the annotator overrode it with world knowledge. The instruction's own aspect example (`停止-01 ... :mod 已经`) shows no structure, so the annotator invented the ARG0 chain.

**Change to the instruction.**
- Give the full structure for the 已经停止发行的小报 example: "noun modified by [停止 + V]: noun `:ARG1-of` V, V `:ARG1-of` 停止."
- Add: "Do not fill a Chinese zero subject of a second clause (仍继续发行…) by re-entrancy. Leave the role out."

## 3. A modifier shared by coordinated nouns put on the `and` node, and an invented `:subset` (d_peripheral_entity: 6 units; g_reentrancy: 2 missing)

**What went wrong.** For 各式各样奇怪的新闻与专栏 the annotation had:

`(and :op1 新闻 :op2 专栏 :mod 各式各样 :mod 奇怪 :subset s2x9)`

Gold has:

`(s2a2 / and :op1 (s2x4 / 新闻 :mod (s2x6 / 各式各样) :mod (s2x7 / 奇怪)) :op2 (s2x5 / 专栏 :mod s2x6 :mod s2x7))`

The rule about shared modifiers is already in the instruction, and it was not followed. `:subset` is not a UMR role at all. 其中 should be `内容 :mod (s2x11 / 其中)`.

**Change to the instruction.**
- Add the 各式各样奇怪的新闻与专栏 fragment above as an example. It shows that the second conjunct uses re-entrant variables.
- Add: "其中 (among them) → `:mod (其中)` on the noun. Use only roles from the closed list; there is no `:subset`."

## 4. Negation with 未经, and the modal strength of what it scopes over (c_polarity: 1 extra; i_modal: 1 wrong; core args: 1)

**What went wrong.** Gold annotates 未经 as `经-01 :aspect process` **without** `:polarity -`. The negation is carried only by `(author :full-negative s2x8)`. The embedded event 查证 gets `(author :partial-affirmative s2x13)` in gold. The annotator gave it full-negative.

**Change to the instruction.** Extend the existing 未经 line in 4.1:
> "未经 → `经-01`, no `:polarity` in the graph, `(author :full-negative 经)`. An event nominal inside its object (查证) is `(author :partial-affirmative x)`."

**A related gold idiom.** In 新闻查证程序 a procedure noun is named by an event. Gold has `程序 :ARG0-of (identity-91 :ARG1 (查证-01 ...))`. The annotation had `程序 :mod 查证-01`. Add this as an example.

## 5. `identity-91` is not given aspect or modal (c_aspect: 1; i_modal: 1)

**What went wrong.** The instruction says to give `identity-91` no temporal triple. The annotator stretched this to no aspect and no modal triple. Gold has `:aspect state` and `(author :full-affirmative s1i2)`.

**Change to the instruction.** Write in 4.1 and 5.1:
> "`identity-91` and the other abstract predicates take `:aspect state` and a modal triple. Only the **temporal** triple is left out."

## 6. Event coreference across different editions (j_coref_chain: 2 extra)

**What went wrong.** The annotation had `(s1x5 :same-entity s4x5)`, linking 发行 of the paper (sentence 1) with 发行 of the 网络版 (sentence 4). The participants differ, and it used `:same-entity` for events. The instruction's warning covers only 停止.

**Change to the instruction.**
> "A repeated habitual verb with a different object (publishing the paper vs. publishing the online edition) is not `:same-event`. Never use `:same-entity` between events."

## 7. Smaller role and structure errors

- **Coordinated two-noun compounds** (a_entity_found: 2; a_entity_concept: 1). For 奇闻轶事 the annotation had one concept. Gold nests an `and` inside the outer `and`: `(s1a2 / and :op1 (奇闻) :op2 (轶事))`. Add: "a four-character string made of two coordinated nouns, not a chengyu, splits into a nested `and`."
- **"In X's history" with a superlative** (d_peripheral_entity, d_core_args_abstract, e_peripheral_labels). For 美国历史上最… the annotation had `have-degree-91 :ARG5 (历史 :possessor 美国)`. Gold has `报纸 :temporal (s5x8 / 上 :op1 (历史 :place (country 美国)))`. Add this as an example. A country on an abstract noun is `:place`, consistent with the existing 美国小报 rule.
- **曾经** (e_peripheral_labels: 1). The annotation had `:mod`. Gold has `:temporal (曾经)`. Add 曾经 next to 目前 as a `:temporal` modifier. It does not belong with 已经, 都 and 也, which are `:mod`.

## What to keep

These examples and rules worked and produced exact matches:
- the 《》 name tokens;
- 一份 / 一个 as `:quant` + `:unit`;
- 以…而闻名 as `:ARG1-of 闻名 :reason 报导`;
- `but-91 :ARG1/:ARG2`;
- the `have-degree-91` superlative;
- the chengyu as `:mod`;
- 属-02 argument order;
- `:part-of` for 纸本;
- `:medium` for 电视;
- the aspect rules (habitual 发行 and 综合, state for 已经停止, performance for 被称为, process for 未经);
- pronoun and coreference chaining of the newspaper entity.

Keep all of these unchanged, and add the new cases above in the same example-driven style, since the annotator follows concrete fragments far more reliably than general rules.
</critique>

# Earlier edits
- batch 1, reflection 1 (12/12 edits applied): Fix aspect (habitual institutional activities, 已经+stop state, 被称为 performance), temporal (no parent for identity/modifier states, chain to main event, no triple for vague time words), non-core roles (:reason for 由于/以而, :place for countries, :medium, :part-of, adverbs as :mod on event), classifier rule (keep :quant 1 :unit 份), title marks as name tokens, superlative have-degree-91, chengyu :mod, bu -> AnCast++ comp 81.5 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.