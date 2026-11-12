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
variable (re-entrancy: `:ARG0 s3p` above). Write an entity's full node (name, apposition) at its first occurrence in reading order; later mentions are re-entrancies.

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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. In Chinese documents write **no** `:wiki` at all. A named human is `individual-person`. A middle dot inside a
transliterated foreign name is kept as its own `:opN "·"`. A title or role noun before a name is `:ARG1-of (h / have-org-role-91
:ARG3 <role>)`; a role noun built from a verb + 人/者 is `(r / 人 :ARG0-of (v / verb-0N ...))` (`performance` for a completed act,
e.g. founding). A descriptive noun phrase in apposition to a name is `:ARG1-of (i / identity-91 :ARG2 <head noun with all its
modifiers>)` on the named entity. Decades (X年代) use `:era`. A periodical, tabloid or magazine name is `newspaper`, not `publication`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. A decade (X年代) is `:era`, never `:decade`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
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
| X holds title T in organization O | `have-org-role-91` | `:ARG1` X, `:ARG2` O, `:ARG3` T |
| X is the R (kin, friend) of Z | `have-rel-role-92` | `:ARG1` X, `:ARG2` Z, `:ARG3` R |
| X has quantity Q | `have-quant-91` | `:ARG1` X, `:ARG2` Q |
| cause, reason | `have-cause-91` / `:cause` | |

Role nouns are reified the same way: *the president of Russia* →
`(p / person :ARG1-of (h / have-org-role-91 :ARG2 (c / country ...) :ARG3 (p2 / president)))`;
*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `(b / but-91 :ARG1 ... :ARG2 ...)`.
  These frames take `:ARG1`/`:ARG2`, never `:op1`/`:op2`. A connective opening a sentence (不过, 但是, 然而, 因此) that relates it to an earlier sentence gets no frame; annotate the clause alone. A time word or adverbial of a clause attaches to that
  clause's event, never to the discourse frame;
- concession `:concession`, condition `:condition`, reason `:reason` (for 由于/因为 phrases giving the reason for a state, an action or a judgement), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.- Reified reason and purpose: when a reason marker is paired with a result marker (因为…于是/所以, 由于…而), or a clause has a
  marked purpose clause (为了, 以, 以便), use `(h / have-reason-91 :ARG1 <result event> :ARG2 <cause event> :aspect state)` and
  `(h2 / have-purpose-91 :ARG1 <main event> :ARG2 <purpose event> :aspect state)`, nesting have-purpose-91 inside have-reason-91
  when both occur. Both frames get `(author :full-affirmative h)` and no temporal parent. Keep the `:reason`/`:purpose` roles for
  unpaired phrases inside one clause.

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
  attached as `:mod` to the predicate it scopes over, not to a noun. Time adverbs (曾经, 曾, *once, formerly*) are
  `:temporal`, not `:mod`.
- A modifier that applies to each of several coordinated nouns is placed on each conjunct with the same variable
  (re-entrancy), not once on the `and` node.
- Fill only the arguments the syntax provides. Do not borrow a participant from elsewhere in the sentence for a
  noun compound or a nominal event; in a compound "N1-verb N2", the role is filled by the compound's own noun.
  The same holds for dropped subjects and objects of finite clauses (in coordination, contrast or a chain of clauses): do not
  add a re-entrancy to an earlier mention; leave the argument out. This also holds for purpose clauses, infinitive-like and
  trailing clauses (never fill their agent with an entity of the main clause) and for possessors: a word like 旗下 is a `:mod`
  concept, not a `:possessor` taken from elsewhere. A trailing clause that describes the object just introduced (a new entity and
  what it holds or does) is a relative clause: attach its event with `:ARGn-of` on that object. Do not add relations the text does not state (e.g. a
  `:part-of` the words do not express). Use only roles of the closed list; a partitive word (其中, *among them, of which*) is a
  `:mod` on the noun it modifies.
- Relative clause headed by an aspectual verb ("N that has stopped V-ing"): N is `:ARG1-of` (or `:ARG0-of`) the inner verb, and
  the aspectual verb is attached to the inner verb by `:ARG1-of`; N is not also an argument of the aspectual verb.
- Read the roleset for every role. For Chinese belong-type rolesets (X belongs to Y), the gold convention is: the thing that
  belongs = `:ARG0`, the owner = `:ARG1`, even where the PropBank role glosses seem to say the reverse. So "N that belongs to X"
  is `(n / N :ARG0-of (b / belong-verb :ARG1 X))`. Never assume possessum = `:ARG1`.
- Coordination with mixed separators: if the first two items are joined without 、 and the rest with 、, the first pair is its
  own nested `and` inside the outer `and`.
- "Known/famous for X" (…而闻名, 以…著称): the famous entity is the `:ARG1` of the fame predicate, attached as
  `:ARG1-of` on that noun, and the X clause is `:reason` of it, with that noun as its agent. When such a clause
  follows "A is a B", attach it inside the B noun, not as a separate conjunct.
- Role choice for noun modifiers: a country, city or place modifying a noun → `:place`; a channel or medium
  (TV, radio, network, print) → `:medium`; an edition, section or component of a whole → `:part-of` (not
  `:possessor`).
- When a component, edition or section noun modifies a named work through 的 ([X] 版 的 《N》), the component noun is the head
  and the work is its `:part-of`; modifiers of the component (colour, style) stay on it. A trailing relative clause on such an object attaches to the component noun.
- Change verbs with 由 X 改为/变为 Y: the original X is `:ARG1` and the result Y is `:ARG2`; never `:source`. When X and Y are components (layout, edition, format) of the subject, the subject is `:part-of` on X, not its own argument and not an inverse `:part`.
- A "verb + 量" quantity noun whose first part is a clear verb is split: `(q / 量 :quant-of (v / verb-01 :ARG1 <entity>))`, the
  owner of the quantity being the verb's `:ARG1` (not `:possessor`). An amount it reaches or falls to is
  `:ARG1-of (h / have-quant-91 :ARG2 <number> :unit <classifier>)` on the quantity noun, not a separate `thing` argument. Neither the inner verb nor `have-quant-91` gets `:aspect` or a modal link, and `have-quant-91` gets no temporal link. A measure noun (circulation, sales, price) at another time or value is not coreferent; corefer only its owner.
- A modifier that says how a process nominal is done (colour, style, method) is `:manner`, not `:mod`.
- Comparatives and superlatives use `have-degree-91`: *the most P X* → `(x / X :ARG1-of (h / have-degree-91
  :ARG2 (p / P) :ARG3 (m / most)))` (Chinese: `:ARG3 (m / 最)`); *more P than Y* adds `:ARG4 Y`. Use `:degree`
  only for plain intensifiers (very, too; 很, 非常, 太).
- When the degree word modifies a verb (*most rich in X*, 最富有X), that verb is the `:ARG2` of `have-degree-91` as an event
  with its own `:aspect` (`(r / verb-01 :ARG1 X :aspect state)`), temporal parent and modal parent; the head noun is `:ARG1`.
  Do not use `:ARG5` and give `have-degree-91` itself no modal link.
- A postposition phrase over a time-span noun (X 历史上, *in X's history*) is `:temporal (s / 上 :op1 (h / 历史))` on its head,
  with the country or place as `:place` of the history noun. The place rule holds for abstract nouns too.
- A property word or chengyu used attributively ("absurd content", X 的 Y with X a property) is a `:mod` concept,
  not an event: it gets no aspect and no temporal or modal links.

## 4. Attributes

### 4.1 Aspect (`:aspect`, on every event)

Decide in this order before using the table:
1. Is the event a routine or recurring practice of its subject (an organisation or periodical publishing,
   reporting, compiling, broadcasting)? → `habitual`. Only verbs of publishing or reporting; the capacity or content of a
   publication (contains articles, has N pages) is not habitual (`process` or `state`). This holds whatever the tense, and also under an
   aspectual verb (continue, stop).
2. Does an aspectual verb of stopping or completion taking an event complement (*has already stopped doing X*) describe a present condition? → `state`.
   An aspectual verb of continuation or ongoing action in the present (*continues to do X*, 继续) is `activity`.
   A lexical verb of ending with no event complement (close down, cease publication; 停刊, 倒闭), even with *already*, is `performance`.
   State verbs (have, own, belong, be; 有, 拥有, 是) stay `state` even with 过, 曾经 or a duration.
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

Also: a purpose or intended action is `activity`; a completed past event in a participle or relative clause
(left over, inherited) is `performance`, not `state`.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2). A negator fused into a verb (未经-type verbs: "without having undergone") gives no
  `:polarity`. The verb is `full-negative` in the modal layer. Events nested under it do not inherit the
  negation: an event nested under the fused-negation verb gets `partial-affirmative`, with `author` as its modal parent (not the negated verb). The concept of a fused-negation verb is the
  un-negated verb with its own PropBank sense and roles (未经 → the 经-type verb's sense, with `:ARG0`/`:ARG1`), never `<negated word>-00`;
  its aspect follows that verb (`process` for 经/经过-type verbs). A compound "[process noun] + procedure/method/system noun" is
  reified as identity: `(p / procedure-noun :ARG0-of (i / identity-91 :ARG1 <event>))`, not `:mod`.
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
  - fame or property states used as attributes inside a noun phrase (*famous X*; see the fame rule below);
  - property modifiers;
  - vague deictic time words (*now, currently, nowadays*, 现在, 目前, 当前).
- Precision counts as much as recall: when a link is not clear, leave it out.
- Time expressions: an absolute date in the past gets `(document-creation-time :before s1t)` (a future one `:after`);
  only a relative deictic one (*today, yesterday*, 今天) gets `(document-creation-time :depends-on s1t)`.
- An event in the clause of a date or time expression gets `(date :overlap event)`; use `:contained` only when the time
  expression is explicitly a span (during, within, 期间); a year or decade takes `:overlap`.
- Past narrative: the anchor event of each new sentence links to `document-creation-time :before`, not to the previous
  sentence's event. Link it to an earlier event only when the sentence explicitly continues from it (也/还 + 成/成为/变成, *also became*, *as a
  result*, 于是), and then with `:overlap` unless the order is stated.
- **Within a sentence, chain the events.** Pick one anchor event (usually the main eventive predicate) and link
  the other events of the sentence to it: `:overlap` for simultaneous states, `:contained` for a state or event
  inside its span, `:before`/`:after` for sequence. Only the anchor links to `document-creation-time` or to an
  earlier sentence's event. For the main event of a sentence describing the present situation, the gold data
  uses `(document-creation-time :depends-on e)`, not `:overlap`: a sentence about the current state (with currently/already, 目前/已经, or a present naming or labelling verb).
- **Aspectual verbs.** When an aspectual verb (stop, continue, begin; 停止, 继续, 开始) takes an event complement, the aspectual verb
  is the parent of the complement: `(aspectual :overlap inner)`. In a main clause the aspectual verb hangs on the sentence anchor like
  any other clause predicate; in a contrast or coordination it `:overlap`s the first clause's anchor event. Only when the aspectual verb
  is inside a relative clause is the inner event the anchor (e.g. `(document-creation-time :before inner)` for a past habit), with the
  aspectual verb `:overlap`ping it. Never use `:before`/`:after` between two clauses that both describe the present situation. Never
  give a second event of the sentence its own link to `document-creation-time`, except the relative-clause anchor just described.
- **"Famous for X" in a defining sentence.** The fame state gets no temporal parent of its own; it is the parent of the habitual
  relative-clause event: `(fame :contained habitual-event)`, and that event also keeps its own `document-creation-time` link. The reason
  event (X) hangs on the habitual event with `:overlap`, not on the fame state.
- Every node that carries `:aspect` gets a modal parent (normally `author :full-affirmative`). A relative-clause verb with an aspect
  ("N that belongs to X") also gets a temporal parent: `:overlap` with the event whose argument N is, or with the clause anchor.
  Copular and identity predicates get no temporal parent but do get a modal parent. An `identity-91` reifying an apposition inside a noun phrase gets no `:aspect` and no links at all. Only property words used as plain `:mod`
  (no aspect) get no links.
- A process nominal that is an argument of a verb takes that verb as its temporal parent with `:overlap`; do not leave it without a parent.
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :overlap s1e)`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent. A purpose event `:overlap`s its main event (never
  `:after`). A reason or cause event is before its result: `(result :before reason)`; a future marker inside a reason clause about
  past events is future relative to that past, not after the main event.
- A relative-clause or participle event that describes an earlier completed event (left over, inherited, built) is before the
  event whose argument it modifies: `(main :before rc-event)`.
- An event nominal inside a decomposed quantity noun (see 3.1) `:overlap`s the verb of its clause.
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
- Coreference only the discourse entities the text tracks (participants, the topic entity). A name used only as a modifier
  (a country name modifying a noun, a place in a `:place` role) is not linked across sentences.
- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words. When a word occurs more than once in a sentence (e.g. a common noun that also appears
inside a name), align each node to its own occurrence.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect`; negated events have `:polarity -`.
- Every event and time expression has a temporal parent; every event has a modal parent.
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.
- Channel nouns (TV, radio, network) modifying a noun are `:medium`; places are `:place`; no `:wiki` in Chinese.
- No borrowed participants: every re-entrancy is licensed by the syntax of that clause.


</instruction>

# The sentences
6	《 世界 新闻 周报 》 创刊 于 1979 年 。
7	创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。
8	黑白 印刷 也 成 了 该刊 的 特色 。
9	在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。
10	不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10
Words: 《 世界 新闻 周报 》 创刊 于 1979 年 。

# sentence level graph:
(s6c / 创刊-01
    :ARG0 (s6n / newspaper
        :name (s6n2 / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :temporal (s6d / date-entity
        :year 1979)
    :aspect performance)


# document level annotation:
(s6s0 / sentence
    :temporal ((document-creation-time :before s6d)
               (s6d :overlap s6c))
    :modal ((root :modal author)
            (author :full-affirmative s6c)))


################################################################################
# meta-info
# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
Words: 创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。

# sentence level graph:
(s7h / have-reason-91
    :ARG1 (s7h2 / have-purpose-91
        :ARG1 (s7c / 创立-01
            :ARG0 (s7p / individual-person
                :name (s7n / name
                    :op1 "格内洛索"
                    :op2 "·"
                    :op3 "波普")
                :ARG0-of (s7h3 / have-org-role-91
                    :ARG3 (s7r2 / 人
                        :ARG0-of (s7c2 / 创始-01
                            :aspect performance))))
            :ARG1 (s7b3 / 版面
                :mod (s7h5 / 黑白)
                :part-of (s7w / newspaper
                    :name (s7n4 / name
                        :op1 "《"
                        :op2 "世界"
                        :op3 "新闻"
                        :op4 "周报"
                        :op5 "》"))
                :ARG0-of (s7r / 容纳-01
                    :ARG1 (s7a / 文章
                        :mod (s7x / 那些)
                        :ARG0-of (s7f / 符合-01
                            :polarity -
                            :ARG1 (s7s / 标准
                                :possessor (s7e / newspaper
                                    :name (s7n3 / name
                                        :op1 "《"
                                        :op2 "国家"
                                        :op3 "询问"
                                        :op4 "报"
                                        :op5 "》")
                                    :mod (s7q / 旗下)
                                    :ARG1-of (s7i / identity-91
                                        :ARG2 (s7t / 小报
                                            :mod (s7g2 / 八卦)))
                                    :part s7b))
                            :aspect state))
                    :aspect state))
            :aspect performance)
        :ARG2 (s7y / 运用-01
            :ARG1 (s7m / 印刷机
                :mod (s7h6 / 黑白)
                :ARG1-of (s7l / 遗留-01
                    :aspect performance))
            :manner (s7c3 / 充分)
            :aspect activity)
        :aspect state)
    :ARG2 (s7g / 改为-01
        :ARG1 (s7b / 版面
            :mod (s7h4 / 黑白))
        :ARG2 (s7b2 / 版面
            :mod (s7c4 / 彩色))
        :aspect performance)
    :aspect state)


# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :before s7c)
               (s7c :before s7g)
               (s7c :overlap s7y)
               (s7y :before s7l)
               (s7c :overlap s7c2)
               (s7c :overlap s7r)
               (s7r :overlap s7f))
    :modal ((root :modal author)
            (author :full-affirmative s7h)
            (author :full-affirmative s7h2)
            (author :full-affirmative s7c)
            (author :full-affirmative s7c2)
            (author :full-affirmative s7g)
            (author :full-affirmative s7y)
            (author :full-affirmative s7l)
            (author :full-affirmative s7r)
            (author :full-negative s7f))
    :coref ((s6n :same-entity s7w)))


################################################################################
# meta-info
# :: snt8
Index: 1 2 3 4 5 6 7 8 9
Words: 黑白 印刷 也 成 了 该刊 的 特色 。

# sentence level graph:
(s8c / 成-01
    :ARG0 (s8y / 印刷-01
        :manner (s8h / 黑白)
        :aspect process)
    :ARG1 (s8t / 特色
        :possessor (s8x / 刊
            :mod (s8g / 该)))
    :mod (s8m / 也)
    :aspect performance)


# document level annotation:
(s8s0 / sentence
    :temporal ((s7c :overlap s8c)
               (s8c :overlap s8y))
    :modal ((root :modal author)
            (author :full-affirmative s8c)
            (author :full-affirmative s8y))
    :coref ((s7w :same-entity s8x)))


################################################################################
# meta-info
# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。

# sentence level graph:
(s9d / 达到-01
    :ARG0 (s9q / 量
        :quant-of (s9f / 发行-01
            :ARG1 (s9n / newspaper
                :name (s9n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :ARG1-of (s9h / have-quant-91
            :ARG2 1200000
            :unit (s9u / 份)))
    :temporal (s9da / date-entity
        :era 1980)
    :aspect performance)


# document level annotation:
(s9s0 / sentence
    :temporal ((document-creation-time :before s9da)
               (s9da :overlap s9d)
               (s9d :overlap s9f))
    :modal ((root :modal author)
            (author :full-affirmative s9d))
    :coref ((s8x :same-entity s9n)))


################################################################################
# meta-info
# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Words: 不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。

# sentence level graph:
(s10j / 跌-01
    :ARG0 (s10q / 量
        :quant-of (s10f / 发行-01
            :ARG1 (s10x / 刊
                :mod (s10g / 该)))
        :ARG1-of (s10h / have-quant-91
            :ARG2 83000
            :unit (s10u / 份)))
    :temporal (s10d / date-entity
        :year 2007)
    :mod (s10y / 已经)
    :aspect performance)


# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10d)
               (s10d :overlap s10j)
               (s10j :overlap s10f))
    :modal ((root :modal author)
            (author :full-affirmative s10j))
    :coref ((s9n :same-entity s10x)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10
Words: 《 世界 新闻 周报 》 创刊 于 1979 年 。

# sentence level graph:
(s6x / 创刊-01
    :ARG0 (s6n / newspaper
        :name (s6n2 / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :temporal (s6d / date-entity
        :year 1979)
    :aspect performance)


# document level annotation:
(s6s0 / sentence
    :temporal ((document-creation-time :before s6d)
               (s6d :overlap s6x))
    :modal ((root :modal author)
            (author :full-affirmative s6x)))


################################################################################
# meta-info
# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
Words: 创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。

# sentence level graph:
(s7h / have-reason-91
    :ARG1 (s7h2 / have-purpose-91
        :ARG1 (s7x13 / 创立-01
            :ARG0 (s7i3 / individual-person
                :name (s7n5 / name
                    :op1 "格内洛索"
                    :op2 "·"
                    :op3 "波普")
                :ARG1-of (s7h3 / have-org-role-91
                    :ARG3 (s7x22 / 人
                        :ARG0-of (s7x23 / 创始-00
                            :aspect performance))))
            :ARG1 (s7x14 / 版面
                :mod (s7x15 / 黑白)
                :part-of (s7n3 / newspaper
                    :name (s7n4 / name
                        :op1 "《"
                        :op2 "世界"
                        :op3 "新闻"
                        :op4 "周报"
                        :op5 "》"))
                :ARG0-of (s7x17 / 容纳-01
                    :ARG1 (s7x18 / 文章
                        :mod (s7x19 / 那些)
                        :ARG0-of (s7x20 / 符合-01
                            :ARG1 (s7x21 / 标准
                                :possessor s7n)
                            :aspect state
                            :polarity -))
                    :aspect process))
            :aspect performance)
        :ARG2 (s7x8 / 运用-01
            :ARG1 (s7x10 / 印刷机
                :mod (s7x11 / 黑白)
                :ARG1-of (s7x12 / 遗留-01
                    :aspect performance))
            :manner (s7x9 / 充分)
            :aspect activity)
        :aspect state)
    :ARG2 (s7x / 改为-01
        :ARG1 (s7x4 / 版面
            :part-of (s7n / newspaper
                :name (s7n2 / name
                    :op1 "《"
                    :op2 "国家"
                    :op3 "询问"
                    :op4 "报"
                    :op5 "》")
                :ARG1-of (s7i2 / identity-91
                    :ARG2 (s7x5 / 小报
                        :mod (s7x6 / 旗下)
                        :mod (s7x7 / 八卦))))
            :mod (s7x16 / 黑白))
        :ARG2 (s7x2 / 版面
            :mod (s7x3 / 彩色))
        :aspect performance)
    :aspect state)


# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :before s7x13)
               (s7x13 :overlap s7x23)
               (s7x13 :overlap s7x17)
               (s7x17 :overlap s7x20)
               (s7x13 :overlap s7x8)
               (s7x8 :before s7x12)
               (s7x13 :before s7x))
    :modal ((root :modal author)
            (author :full-affirmative s7x23)
            (author :full-negative s7x20)
            (author :full-affirmative s7x17)
            (author :full-affirmative s7x13)
            (author :full-affirmative s7x12)
            (author :full-affirmative s7x8)
            (author :full-affirmative s7h2)
            (author :full-affirmative s7x)
            (author :full-affirmative s7h))
    :coref ((s6n :same-entity s7n3)))


################################################################################
# meta-info
# :: snt8
Index: 1 2 3 4 5 6 7 8 9
Words: 黑白 印刷 也 成 了 该刊 的 特色 。

# sentence level graph:
(s8x / 成-01
    :ARG0 (s8x2 / 印刷-01
        :manner (s8x3 / 黑白)
        :aspect habitual)
    :ARG1 (s8x4 / 特色
        :possessor (s8x5 / 刊
            :mod (s8x6 / 该)))
    :mod (s8x7 / 也)
    :aspect performance)


# document level annotation:
(s8s0 / sentence
    :temporal ((s7x13 :overlap s8x)
               (s8x :overlap s8x2))
    :modal ((root :modal author)
            (author :full-affirmative s8x2)
            (author :full-affirmative s8x))
    :coref ((s7n3 :same-entity s8x5)))


################################################################################
# meta-info
# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。

# sentence level graph:
(s9x / 达到-01
    :ARG0 (s9x2 / 量
        :quant-of (s9x3 / 发行-01
            :ARG1 (s9n / newspaper
                :name (s9n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :ARG1-of (s9h / have-quant-91
            :ARG2 1200000
            :unit (s9x4 / 份)))
    :temporal (s9d / date-entity
        :era 1980)
    :aspect performance)


# document level annotation:
(s9s0 / sentence
    :temporal ((document-creation-time :before s9d)
               (s9d :overlap s9x)
               (s9x :overlap s9x3))
    :modal ((root :modal author)
            (author :full-affirmative s9x))
    :coref ((s8x5 :same-entity s9n)))


################################################################################
# meta-info
# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Words: 不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。

# sentence level graph:
(s10x / 跌-01
    :ARG0 (s10x2 / 量
        :quant-of (s10x3 / 发行-01
            :ARG1 (s10x4 / 刊
                :mod (s10x5 / 该)))
        :ARG1-of (s10h / have-quant-91
            :ARG2 83000
            :unit (s10x7 / 份)))
    :temporal (s10d / date-entity
        :year 2007)
    :mod (s10x6 / 已经)
    :aspect performance)


# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10d)
               (s10d :overlap s10x)
               (s10x :overlap s10x3))
    :modal ((root :modal author)
            (author :full-affirmative s10x))
    :coref ((s9n :same-entity s10x4)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 100 / P 100 / F 100
a_event_concept: R 100 / P 100 / F 100
a_entity_found: R 100 / P 100 / F 100
a_entity_concept: R 100 / P 100 / F 100
a_granularity: R 100 / P 100 / F 100
b_event_sense: R 93 / P 93 / F 93
c_aspect: R 86 / P 86 / F 86
c_polarity: R 100 / P 100 / F 100
c_other_attributes: R 100 / P 100 / F 100
d_core_args_event: R 100 / P 100 / F 100
d_core_args_abstract: R 89 / P 89 / F 89
d_peripheral_event: R 100 / P 100 / F 100
d_peripheral_entity: R 86 / P 79 / F 83
e_core_labels: R 96 / P 96 / F 96
e_peripheral_labels: R 100 / P 100 / F 100
f_name_tokens: R 100 / P 100 / F 100
g_reentrancy: R 0 / P 0 / F 0
h_temporal: R 100 / P 100 / F 100
i_modal: R 100 / P 100 / F 100
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
b_event_sense | wrong | s7x23: 创始 -> 创始-01 | 创始 -> 创始-01
c_aspect | wrong | s7x17:aspect: process -> state | process -> state
d_core_args_abstract | partial | s7h3: arg1 s7i3/individual-person; arg3 s7x22/人 -> arg0 s7i3/individual-person; arg3 s7x22/人 | arg1 s7i3/individual-person: predicted as arg0
d_peripheral_entity | extra | s7x21: - -> possessor s7n/newspaper | extra possessor s7n/newspaper
d_peripheral_entity | wrong | s7n: part s7x4/版面 -> mod s7x6/旗下 | missing part s7x4/版面; extra mod s7x6/旗下
d_peripheral_entity | partial | s7x5: mod s7x6/旗下; mod s7x7/八卦 -> mod s7x7/八卦 | missing mod s7x6/旗下
e_core_labels | wrong | s7h3 -arg1-> s7i3: arg1 -> arg0 | arg1 -> arg0
g_reentrancy | missing | s7x21/标准 -possessor-> s7n/newspaper: s7x21/标准 -possessor-> s7n/newspaper -> - | the prediction has the edge but not as a reentrancy
g_reentrancy | extra | s7e/newspaper -part-> s7b/版面: - -> s7e/newspaper -part-> s7b/版面 | gold has no such reentrancy
c_aspect | wrong | s8x2:aspect: habitual -> process | habitual -> process

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.