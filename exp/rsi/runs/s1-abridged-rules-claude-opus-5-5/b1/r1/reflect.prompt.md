<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 15598). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

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

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 55.7)
<critique>
# Review of the instruction: error patterns in the five-sentence Chinese document, most costly first

## 1. Temporal links: every event is anchored to the document creation time (h_temporal F 30; about 13 units)

**What went wrong**
- Almost every event got its own `document-creation-time :before/:overlap` link, including:
  - events in a relative clause,
  - the second clause of a coordination,
  - a "known for" clause,
  - a negated clause.
- In gold, the sentence's main event gets one link to the document creation time. The other events in the sentence hang off that main event or a sister event with `:overlap` (or `:contained`).
- Gold also differs in three other ways:
  - It gives no temporal parent to a copular state (`identity-91`) or to a vague time word like "currently". The annotator added `present-reference :depends-on` for the time word.
  - For a sentence whose main event is a present-relevant change or naming, gold uses `document-creation-time :depends-on <event>`.
  - It always links an event nominal inside a negated predicate, a relative-clause verb, and a possession verb inside a modifier. The annotator left these with no parent.

**Why it happens:** The instruction's rule (1) time expression, (2) earlier event, (3) document creation time puts the document creation time ahead of other events in the same sentence. It also says "annotate event–event relations only when they are clear", which pushes the annotator away from same-sentence links.

**What to change:** Add this rule:
- Pick one temporal anchor per sentence: the matrix event, linked to the document creation time or a time expression.
- Every other event in the sentence takes that anchor or the event it modifies as its parent. Use `:overlap` unless the order is explicit.
- This covers subordinate, relative, complement, coordinated, cause/reason, nominal and negated events.
- Every event node, including one inside a noun-phrase modifier, must get a parent.
- Do not give a vague present-time adverb its own `depends-on` triple.
- Leave a pure copular identity state out of the temporal structure. It still belongs in the modal structure.

## 2. Function words and classifiers are dropped (a_entity_found R 85, part of d_peripheral; about 10 units)

**What went wrong**
- Gold keeps these as nodes:
  - aspectual or temporal adverbs ("already" as `:mod`, "once/formerly" as `:temporal`);
  - the "all" adverb, as `:mod` on the event;
  - "among them", as `:mod` on the noun;
  - a locative postposition after a time noun, as a `:temporal` node with `:op1`.
- Gold also keeps "one + classifier" as `:quant 1` plus `:unit <classifier>`, even for ordinary classifiers like 个 and 份.

**Why it happens:** The instruction says outright that ordinary classifiers are dropped. That contradicts the gold. It also lists auxiliaries as non-nodes, and the annotator extended that to aspectual adverbs.

**What to change:**
- Replace the classifier rule: a numeral + classifier is `:quant N` plus `:unit <classifier>`, and `:quant 1` is written too.
- State that adverbs are nodes:
  - aspect/time adverbs (already, once, still, all, also) become `:mod`, or `:temporal` for past-time adverbs;
  - a partitive "among them" becomes `:mod`.
- Only modal auxiliaries are dropped.

## 3. Arguments attached to the wrong node, and implicit arguments added (g_reentrancy F 15, d_core_args_event F 64; about 12 units)

**What went wrong**
- **Relative clause with an aspectual verb.** In a pattern like "stopped publishing" modifying a noun, the annotator made the head noun the argument of the outer verb and also of the inner verb. Gold makes the head noun `:ARG1-of` the inner verb only. The aspectual verb then takes the inner event: inner event `:ARG1-of` the aspectual verb.
- **Implicit participants.** The annotator added participants the text does not express:
  - an agent of a publishing event;
  - a possessor of a derived product;
  - the subject of a negated "undergo".

  Gold leaves them out. Re-entrancy precision was 12 %.
- **Clause describing the predicate noun.** The clause "known for X-ing" comes after a copular sentence and describes the predicate noun. Gold attaches it under that noun as `:ARG1-of`. The annotator made it a top-level `and` conjunct with re-entrant subjects.
- **Shared modifiers.** In "various strange A and B", gold copies the modifiers onto each conjunct by re-entrancy. The annotator put them on the `and` node and also added a spurious `:subset`.

**What to change:** Add these rules:
- Do not add an unexpressed argument just because the roleset has a slot. Re-enter a node only when the text expresses the participant.
- For a head noun modified by an aspectual verb plus a verb, the noun is the argument of the innermost verb.
- A modifier shared by coordinated nouns goes on each conjunct (re-entrancy), not on the coordinator.
- A clause that keeps describing a copular predicate noun attaches to that noun.

## 4. Aspect (c_aspect F 60; 5 units)

**What went wrong**
- Recurring publishing activity, and what a periodical regularly contains: gold `habitual`. The annotator used `process`, `performance` or `activity`.
- "Already" + stop, describing a current result: gold `state`.
- A negated "undergo" with a nominal object: gold `process`.
- A passive "is called/regarded as": gold `performance`.

**What to change:** Add these rules:
- Activities of an institution that repeat (publishing, broadcasting, reporting, collecting content) are `habitual`, even with a completion marker.
- "already + cease/stop" describing the current situation is `state`.
- A naming or evaluation passive is `performance`.

## 5. Concept choices (a_event_concept and core labels; about 8 units)

**What went wrong**
- **Lexical verb vs abstract predicate.** A Chinese possession/belonging verb with a PropBank frame should keep that lexical frame (holder as `ARG0`, owner as `ARG1`) instead of `belong-91`.
- **Concessive "but".** 不过 and similar words take `but-91`, not `contrast-91`.
- **Superlatives.** "most + property" is `have-degree-91`: the noun is `:ARG1`, the property event is `:ARG2`, and the degree word is `:ARG3`. Do not use `:degree` on the property verb.
- **Reason words.** 由于 and the frame 以…而 go to `:reason`. The instruction's "因为/由于 → :cause" is wrong for this data.
- **Coordinated compound noun.** A four-character compound made of two coordinated nouns is split into `and` with two ops. An idiom stays one concept.
- **Part-of and medium.** A physical edition of a publication is `:part-of` it, not `:possessor`. A medium noun ("TV") modifying a program is `:medium`.
- **Ceasing publication.** A verb of ceasing publication takes the publication as `ARG0`. Check the roleset.

**What to change:** Add these points to sections 2.3 and 2.5:
- Prefer the Chinese PropBank verb over an abstract `-91` predicate whenever a frame exists.
- Add 不过 to the list of words that take `but-91`.
- Add a `have-degree-91` row to the abstract-predicate table.
- Change 由于 to `:reason`.
- Split coordinated noun compounds into `and`.

## 6. Named entities (f_name_tokens F 50, f_wiki 0, place labels; about 7 units)

**What went wrong**
- Gold includes the title brackets 《 》 as their own `:op`s.
- Gold has no `:wiki`.
- A country name modifying a noun or "history" is `:place`, not `:mod`.

**What to change:**
- Do not write `:wiki` for this data.
- For titled works, keep the bracket tokens as the first and last `:op`.
- A country/location name modifying a common noun is `:place`.

## 7. Coreference precision (j_coref_chain P 71; 2 units)

**What went wrong:** The annotator linked a country name that appears as a modifier in two sentences. Gold links only the main discourse entity.

**What to change:** Do not build chains for incidental place names that are only modifiers. Do link every mention of the main entities.

## Minor: polarity on a negated event
The annotator put `:polarity -` on the negated event. Gold has no polarity there but still marks the event `full-negative` in the modal structure. This cost one unit; leave the rule as it is.

## What to keep
- **Modal annotation (F 94):** `root → author → full-affirmative`, and `full-negative` for negated events.
- **Senses (100):** the sense choices and the habit of looking up rolesets.
- **Abstract predicates:** core roles of the abstract predicates (100).
- **Document format (100).**
- **Coreference recall (100):** linking each mention to the closest earlier one.
- **Basic graph shape:** event-nominal aspect `process`, relative clauses as `:ARGn-of`, and the overall structure of the sentence graphs.
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