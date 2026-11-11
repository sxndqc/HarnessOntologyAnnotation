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

Language: en
Document: en-0008, sentence 7 of 9

The previous sentences (at most five; number, tab, words):

2	Pope is the American businessman who was convicted last week on spying charges and sentenced to 20 years in a Russian prison .

3	He denied any wrongdoing .

4	Russian President Vladimir Putin pardoned him for health reasons .

5	Pope was flown to the U.S. military base at Ramstein , Germany .

6	He will spend the next several days at the medical center there before he returns home with his wife Sherry .

Their graphs:

# ::snt 2
# sentence level graph:
(s2i / identity-91
    :ARG1 (s2p / person
        :wiki "Edmond_Pope"
        :name (s2n / name
            :op1 "Pope"))
    :ARG2 (s2b / businessman
        :mod (s2n2 / nationality
            :wiki "United_States"
            :name (s2n3 / name
                :op1 "American"))
        :ARG1-of (s2c / convict-01
            :ARG2 (s2c2 / charge-05
                :ARG1 s2b
                :ARG2 (s2s / spy-01
                    :ARG0 s2b
                    :aspect process)
                :aspect process)
            :temporal (s2w / week
                :mod (s2l / last))
            :aspect performance)
        :ARG1-of (s2s2 / sentence-01
            :ARG2 (s2p2 / prison
                :mod (s2c3 / country
                    :wiki "Russia"
                    :name (s2n4 / name
                        :op1 "Russian"))
                :duration (s2t / temporal-quantity
                    :quant 20
                    :unit (s2y / year)))
            :ARG3 s2s
            :aspect performance))
    :aspect state)

# ::snt 3
# sentence level graph:
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

# ::snt 4
# sentence level graph:
(s4p / pardon-01
    :ARG0 (s4p2 / person
        :wiki "Vladimir_Putin"
        :name (s4n / name
            :op1 "Vladimir"
            :op2 "Putin")
        :ARG1-of (s4h / have-org-role-92
            :ARG2 (s4c / country
                :wiki "Russia"
                :name (s4n2 / name
                    :op1 "Russia"))
            :ARG3 (s4p3 / president)))
    :ARG1 (s4p4 / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1-of (s4c2 / cause-01
        :ARG0 (s4r / reason
            :mod (s4h2 / health)))
    :aspect performance)

# ::snt 5
# sentence level graph:
(s5f / fly-01
    :ARG1 (s5p / person
        :name (s5n / name :op1 "Pope"))
    :goal (s5b / base
        :mod (s5m / military)
        :possessor (s5c / country
            :name (s5n2 / name :op1 "U.S.")
            :wiki "United_States")
        :place (s5c2 / city
            :name (s5n3 / name :op1 "Ramstein")
            :place (s5c3 / country
                :name (s5n4 / name :op1 "Germany")
                :wiki "Germany")))
    :aspect performance)

# ::snt 6
# sentence level graph:
(s6s / spend-02
    :ARG0 (s6p / person
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s6t / temporal-quantity
        :quant (s6s2 / several)
        :unit (s6d / day
            :mod (s6n / next)))
    :temporal (s6b / before
        :op2 (s6r / return-01
            :ARG1 s6p
            :ARG4 (s6h / home)
            :companion (s6p2 / person
                :wiki -
                :name (s6n2 / name
                    :op1 "Sherry")
                :ARG1-of (s6h2 / have-rel-role-92
                    :ARG2 s6p
                    :ARG3 (s6w / wife)
                    :aspect state))
            :aspect performance))
    :place (s6c / center
        :mod (s6m / medical)
        :place (s6t2 / there))
    :aspect state)

This sentence:

7	Pope was in remission from a rare form of bone cancer when he was arrested in Russia.

Its graph:

# ::snt 7
# sentence level graph:
(s7h / have-mod-91
    :ARG1 (s7p / person
        :name (s7n / name :op1 "Pope"))
    :ARG2 (s7r / remission-02
        :ARG1 (s7d / disease
            :wiki "Bone_cancer"
            :name (s7n2 / name :op1 "bone" :op2 "cancer")
            :mod (s7f / form
                :mod (s7r2 / rare)))
        :aspect state)
    :temporal (s7a / arrest-01
        :ARG1 s7p
        :place (s7c / country
            :wiki "Russia"
            :name (s7n3 / name :op1 "Russia"))
        :aspect performance)
    :aspect state)
