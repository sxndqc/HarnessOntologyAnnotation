<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 19360). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

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

Only modal auxiliaries are dropped. Adverbs are nodes:
- aspectual and scope adverbs (*already, still, also, all*; 已经, 仍, 也, 都) are `:mod` on the event;
- past-time adverbs (*once, formerly*; 曾, 曾经) are `:temporal`;
- a partitive like 其中 (*among them*) is `:mod` on the noun;
- a locative postposition after a time noun (X 时, X 中, X 以来) is a `:temporal` node with the time noun as `:op1`.

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

Use an abstract predicate only when there is no lexical predicate. A Chinese verb with its own PropBank frame keeps that frame and its roles. For example, a possession or belonging verb such as 属于 or 拥有 is `属于-01` / `拥有-01`, not `belong-91` / `have-91`. Do not use `:degree` on a property verb for a superlative; use `have-degree-91`.

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

A compound made of two coordinated nouns (AB where A and B are parallel nouns, e.g. a four-character N1N2 meaning *N1 and N2*) is split: `(a / and :op1 N1 :op2 N2)`. A true idiom stays one concept.

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
- **Unexpressed participants.** Do not fill a roleset slot with a participant the text does not express. Re-enter a node only when the text itself expresses that participant in that role.
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
- **already + stop/cease** (已经停止…) describing the current situation is `state`.
- **A naming or evaluation passive** (*is called / is regarded as*, 被称为, 被誉为) is `performance`.
- **A negated event with a nominal event object** (没有经过X) is `process`.

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
- Every event node must get exactly one temporal parent. The only exception is a pure copular identity state (`identity-91`), which is left out of the temporal structure; it still gets its modal parent.

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
- Every event has `:aspect`; negated events have `:polarity -`.
- Every event and time expression has a temporal parent; every event has a modal parent.
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.


</instruction>

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 78.4)
<critique>
The costliest error is the temporal structure (about 11 units). Next come superlatives built on a property verb (about 9 units) and Chinese verbs whose argument numbers or sense were assumed rather than checked in PropBank (about 7 units). Most other checks were already strong.

## 1. Temporal anchors and constants (h_temporal F 43, about 11 units)

What went wrong, by kind:

**(a) Copular identity sentence with events inside the predicate noun.**
- The annotator anchored on the "known for" state, linking it to document creation time with `:overlap`. It also ordered the "stopped" event `:before` the event it stops, even though the order of a stop and the event it stops was not stated.
- Gold anchors on the past event inside the predicate noun (`DCT :before`). Every other event of the sentence hangs off that anchor: the reputation state is `:contained` in it, and the rest are `:overlap`.
- **Why:** rule 5.1 says "the anchor is the matrix event". When the matrix is `identity-91`, which has no temporal link, the rule does not say what replaces it.
- **Change:** "When the root is `identity-91`, choose as anchor the event in the predicate noun that is most clearly placed in time, usually a completed past event. The reputation or property states are then `:contained` in it, and everything else is `:overlap`. An aspectual verb (stop, begin) and the event it governs are `:overlap`, never `:before`/`:after`."

**(b) Past-time adverbs (曾经 type).**
- The annotator made the adverb a time expression (`past-reference :depends-on adv`, then `adv :contained event`).
- Gold gives the adverb no temporal triple and uses `document-creation-time :before event`.
- **Change:** "Past-time adverbs (once, formerly, 曾, 曾经) stay `:temporal` nodes in the graph but are not reference times. Give them no temporal triple, and link the event directly as `(document-creation-time :before e)`." Do the same as the instruction already does for vague present adverbs.

**(c) Events whose result holds now** (a termination already done, as in 已经 + a termination verb; a naming/evaluation passive).
- Gold uses `(document-creation-time :depends-on e)`. The annotator used `:overlap` and `:before`.
- **Change:** add this case to 5.1: a completed event whose result describes the present situation (a status reached, a name or evaluation given) is linked as `(document-creation-time :depends-on e)`.

**(d) `have-degree-91`.** The annotator gave it a temporal parent, a modal parent and `:aspect state`. Gold gives it none of these, consistently across documents. It is the same kind of exception as `identity-91`; see item 4.

## 2. Superlative of a property verb, and "history 上" (about 9 units)

**What went wrong:**
- For "most + property verb + noun object" (最富创意 type), the annotator dropped the verb and put the noun as `:ARG2` of `have-degree-91`.
- It also made the scope phrase "in X's history" (X 历史上) an `:ARG5` comparison set and dropped the postposition.

**What gold does:**
- `:ARG2` is the property verb as an event (`富-01 :ARG1 创意`, `:aspect state`).
- The scope phrase is a `:temporal` node for 上 with the time noun as `:op1`, attached to the head noun.

**What it cost:** a missing event, its aspect, temporal and modal links, the missing 上 node, and three wrong `have-degree-91` arguments.

**Why:** 2.3 says to use `have-degree-91` but not what fills `:ARG2` when the property is a verb with an object. The locative-postposition rule lists 时/中/以来 only.

**Changes:**
- "In a superlative or comparative, `:ARG2` is the property word itself. If it is a verb with its own object (rich in X, full of X), keep the verb as an event concept with its object, and put that verb under `:ARG2`."
- "Use `:ARG5` only for an explicit comparison set (among N, of all N). A scope like 'in history' (X 上, X 以来) is a `:temporal` (or `:range`) postposition node with the noun as `:op1`."
- Extend the postposition list to 上 after time or period nouns (历史上).

## 3. Chinese verbs: argument numbering and sense guessed from English (about 7 units)

**What went wrong:**
- A "belonging" verb in a relative clause got sense -01 with `:ARG1` = the thing and `:ARG2` = the owner. In PropBank, -02 is the belonging sense, with `:ARG0` = the owner and `:ARG1` = the thing that belongs.
  - In gold, the program is `:ARG0-of` the verb, and the newspaper (the 自己 referent) is re-entered as its `:ARG1`.
- A "cease publication" verb has only `:ARG0` in PropBank (the publication). The annotator used `:ARG1`.

**Why:** the instruction warns against abstract predicates, which is why the verb was right, but it never says the Chinese PropBank roleset decides the numbering. The annotator then fell back on English habits (theme = `:ARG1`).

**Change:** "For every Chinese predicate, look up its frames. Choose the sense whose role descriptions fit, and use exactly the numbered roles that roleset defines. Many Chinese intransitive and change-of-state verbs have only `:ARG0`. Do not default the theme to `:ARG1`."

## 4. Attributes on abstract predicates (3 units)

**What went wrong:**
- `identity-91` had no `:aspect`, but gold has `:aspect state`.
- `have-degree-91` was given `:aspect state`, but gold gives it no aspect, and also no temporal or modal parent.

**Change** (state both together):
- "`identity-91` gets `:aspect state` and a modal parent, but no temporal parent."
- "`have-degree-91` gets no `:aspect`, no temporal parent and no modal parent. The event under its `:ARG2`, if any, gets all of these."

## 5. Coreference of an incidental place name (j_coref precision 71, 2 units)

The annotator linked a country name that appears only as a `:place` modifier in two sentences, which the instruction already forbids. The rule was not followed.

**Change:** add it to the final checklist as well: "Before writing `:coref`, drop every pair where both mentions are only `:place`/`:mod` modifiers."

## 6. Smaller patterns (1–2 units each)

- **Shared subject in a purpose or means frame** (以 X 而 Y, "known for doing X"): gold re-enters the subject of Y as `:ARG0` of X. The instruction's "unexpressed participants" rule made the annotator leave it out.
  - **Change:** "A subject shared through a control or serial frame counts as expressed; re-enter it."
- **Negation fused into a verb word** (未经 type): gold puts no `:polarity -` on the graph, only `full-negative` at the document level.
  - **Change:** add this as an exception to "negated events have `:polarity -`".
- **Noun + event-nominal modifier meaning "a procedure that is X"**: gold uses `程序 :ARG0-of (identity-91 :ARG1 event)`, not `:mod event`.
- **Termination verb with 已经:** the rule "already + stop/cease → `state`" was over-applied. Gold restricts it to the aspectual verb that governs another event (stop doing X). A lexical termination verb (ceased publication) with 已经 is `performance`. Narrow the rule to say so.
- **A list whose first item is a fixed pair of parallel nouns:** gold nests the pair as its own `and` inside the outer `and`. Say this in 2.6.
- **Event nominal inside a negated clause:** gold gives it author-level `partial-affirmative`, not `(negated event :unspecified x)`. This is a minor point and probably not worth a rule.

## What to keep

The instruction already produced these correctly, so keep the rules behind them:
- Named entities, including title brackets as their own `:op`s.
- `:quant 1` with `:unit` for a classifier.
- `:place` for a country modifying a noun.
- Shared modifiers re-entered on each conjunct.
- `:medium` for a TV program and `:part-of` for a print edition.
- 由于 → `:reason`; 但/不过 → `but-91`.
- `habitual` for a periodical's publishing and contents.
- `performance` for a naming passive; `state` for 已经停止.
- `:mod` for 已经/仍/也/都 and `:temporal` for 曾经 in the graph.
- Main-entity coreference chains, and the format of the document-level annotation.

All of these scored at or near 100.
</critique>

# Earlier edits
- batch 1, reflection 1 (15/15 edits applied): Temporal: one anchor per sentence, other events hang off it with :overlap, every event gets a parent, no depends-on for vague present adverbs, copular identity left out. Classifiers become :quant+:unit (also 1); adverbs are nodes. No implicit arguments. Attachment rules for aspectual-verb relatives, shared modifiers, describing clauses, part-of and medium. Aspect rules for habitual, already+stop a -> AnCast++ comp 78.4 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.