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
variable (re-entrancy: `:ARG0 s3p` above). Write an entity's full node (name, apposition, all modifiers) at its first mention in the order of the words of the sentence (text order, not graph order), even when that mention sits deeper in the graph; every other mention is a bare variable.

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
:ARG3 <role>)` (the holder is always `:ARG1`, never `:ARG0`); separately, a role noun built from a verb + 人/者 is `(r / 人 :ARG0-of (v / verb-0N ...))` (`performance` for a completed act,
e.g. founding). A descriptive noun phrase in apposition to a name is `:ARG1-of (i / identity-91 :ARG2 <head noun with all its
modifiers>)` on the named entity; modifiers written before the apposition noun (的-phrases, 旗下, property words) go on that noun, not on the entity. Decades (X年代) use `:era`. A periodical, tabloid or magazine name is `newspaper`, not `publication`. Types: `person`,
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
- Change verbs with 由 X 改为/变为 Y: the original X is `:ARG1` and the result Y is `:ARG2`; never `:source`. When X and Y are components (layout, edition, format) of the subject, the subject is `:part-of` on X, not its own argument and not an inverse `:part`, even when it also fills a role elsewhere (that role is then a re-entrancy).
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
   printing, issuing, reporting, broadcasting)? → `habitual`, also for a process nominal naming such a practice (e.g. subject of
   "is/became its feature"); this step precedes step 3. A verb of what a publication holds or carries (contains articles) is `process`. This holds whatever the tense, and also under an
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
11	2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了 《 世界 新闻 周报 》 的 发行 ， 不过 周报 的 网络版 仍 继续 生存 。
12	虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。
13	他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。
14	其中 最大宗 可 算是 外星人 地球 活动 。
15	美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
Words: 2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了 《 世界 新闻 周报 》 的 发行 ， 不过 周报 的 网络版 仍 继续 生存 。

# sentence level graph:
(s11b / but-91
    :ARG1 (s11x / 停止-01
        :temporal (s11d / date-entity
            :year 2007
            :month 7)
        :ARG0 (s11c / company
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司")
            :ARG1-of (s11i / identity-91
                :ARG2 (s11x2 / 母公司)))
        :ARG1 (s11x3 / 发行-01
            :ARG1 (s11w / newspaper
                :name (s11n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :aspect habitual)
        :aspect performance)
    :ARG2 (s11x4 / 继续-01
        :ARG1 (s11x5 / 生存-01
            :ARG0 (s11x6 / 网络版
                :part-of s11w)
            :aspect activity)
        :mod (s11x7 / 仍)
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11x)
               (s11x :overlap s11x3)
               (s11x :overlap s11x4)
               (s11x4 :overlap s11x5))
    :modal ((root :modal author)
            (author :full-affirmative s11x)
            (author :full-affirmative s11x3)
            (author :full-affirmative s11x4)
            (author :full-affirmative s11x5)))


################################################################################
# meta-info
# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。

# sentence level graph:
(s12b / but-91
    :ARG1 (s12x / 宣称-01
        :ARG0 (s12n / newspaper
            :name (s12n2 / name
                :op1 "《"
                :op2 "世界"
                :op3 "新闻"
                :op4 "周报"
                :op5 "》"))
        :ARG1 (s12x2 / 真实-01
            :ARG0 (s12x3 / 报导-01
                :ARG0 s12n
                :aspect habitual)
            :mod (s12x4 / 都)
            :aspect state)
        :medium (s12x5 / 标语
            :possessor s12n
            :ARG1-of (s12i / identity-91
                :ARG2 (s12x6 / 报导-01
                    :ARG0 s12n
                    :ARG1 (s12x7 / 事实)
                    :mod (s12x8 / 只)
                    :aspect habitual)
                :aspect state))
        :aspect activity)
    :ARG2 (s12h / have-purpose-91
        :ARG1 (s12x9 / 报导-01
            :quant (s12x10 / 大部分)
            :aspect habitual)
        :ARG2 (s12x11 / 博君一笑-00
            :aspect activity)
        :mod (s12x12 / 都)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
               (s12x :overlap s12x2)
               (s12x2 :overlap s12x3)
               (s12x :overlap s12x6)
               (s12x :overlap s12x9)
               (s12x9 :overlap s12x11))
    :modal ((root :modal author)
            (author :full-affirmative s12x)
            (author :full-affirmative s12n)
            (s12n :full-affirmative s12x2)
            (author :full-affirmative s12x3)
            (author :full-affirmative s12i)
            (author :full-affirmative s12x6)
            (author :full-affirmative s12h)
            (author :full-affirmative s12x9)
            (author :full-affirmative s12x11))
    :coref ((s11w :same-entity s12n)))


################################################################################
# meta-info
# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。

# sentence level graph:
(s13a / and
    :op1 (s13x / 有-07
        :ARG0 (s13x2 / 题材
            :ARG1-of (s13x3 / 报导-01
                :ARG0 (s13p / person
                    :refer-person 3rd
                    :refer-number plural)
                :frequency (s13x4 / 经常)
                :aspect habitual))
        :ARG1 (s13a2 / and
            :op1 (s13x5 / 外星人)
            :op2 (s13x6 / 航天员
                :mod (s13x7 / 古代))
            :op3 (s13x8 / 旅行-01
                :mod (s13x9 / 时间)
                :aspect process)
            :op4 (s13x10 / 大脚)
            :op5 (s13x11 / 欧帕兹)
            :mod (s13x12 / 等))
        :aspect state)
    :op2 (s13x13 / 创造-01
        :ARG0 s13p
        :ARG1 (s13x14 / 人物
            :quant (s13x15 / 一些)
            :ARG1-of (s13x17 / 出现-01
                :ARG0 (s13x18 / 新闻
                    :possessor s13p)
                :manner (s13x19 / 重复)
                :aspect habitual)
            :mod (s13x16 / 虚拟)
            :example (s13a3 / and
                :op1 (s13p2 / person
                    :name (s13n / name
                        :op1 "蝙蝠"
                        :op2 "男孩"))
                :op2 (s13x20 / 外星人
                    :name (s13n2 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod"))
                :mod (s13x21 / 等)))
        :mod (s13x22 / 甚至)
        :aspect performance))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13x)
               (s13x :overlap s13x3)
               (s13x :overlap s13x8)
               (s13x :overlap s13x13)
               (s13x13 :after s13x17))
    :modal ((root :modal author)
            (author :full-affirmative s13x)
            (author :full-affirmative s13x3)
            (author :full-affirmative s13x8)
            (author :full-affirmative s13x13)
            (author :full-affirmative s13x17))
    :coref ((s12n :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14x / 算是-01
    :ARG0 (s14x2 / 宗
        :mod (s14x5 / 其中)
        :ARG1-of (s14h / have-degree-91
            :ARG2 (s14x3 / 大)
            :ARG3 (s14x4 / 最)))
    :ARG1 (s14x6 / 活动-01
        :ARG0 (s14x7 / 外星人)
        :place (s14x8 / 地球)
        :aspect process)
    :modal-strength neutral-affirmative
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :depends-on s14x)
               (s14x :overlap s14x6))
    :modal ((root :modal author)
            (author :neutral-affirmative s14x)
            (author :full-affirmative s14x6)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15x / 指-02
    :ARG1 (s15a / and
        :op1 (s15x2 / 有-01
            :ARG0 (s15p / individual-person
                :name (s15n / name
                    :op1 "希拉里"
                    :op2 "·"
                    :op3 "克林顿")
                :ARG1-of (s15h / have-org-role-91
                    :ARG2 (s15c / country
                        :name (s15n2 / name
                            :op1 "美国"))
                    :ARG3 (s15x3 / 第一夫人)
                    :mod (s15x4 / 前)))
            :companion (s15x7 / 外星人
                :name (s15n3 / name
                    :op1 "P"
                    :op2 "'"
                    :op3 "Lod"))
            :ARG1 (s15x5 / 关系
                :mod (s15x6 / 暧昧))
            :aspect state)
        :op2 (s15x8 / 领养-01
            :ARG0 s15p
            :ARG1 (s15x9 / 宝宝
                :mod (s15x10 / 外星))
            :temporal (s15x11 / 后来)
            :mod (s15x12 / 还)
            :aspect performance))
    :mod (s15x13 / 就)
    :aspect performance)


# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15x)
               (s15x :overlap s15x2)
               (s15x2 :after s15x8))
    :modal ((root :modal author)
            (author :full-affirmative s15x)
            (s15x :full-affirmative s15x2)
            (s15x :full-affirmative s15x8))
    :coref ((s13x20 :same-entity s15x7)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt11
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
Words: 2007 年 7 月 ， 母公司 美国 媒体 公司 停止 了 《 世界 新闻 周报 》 的 发行 ， 不过 周报 的 网络版 仍 继续 生存 。

# sentence level graph:
(s11b / but-91
    :ARG1 (s11x / 停止-01
        :ARG0 (s11c / company
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司")
            :ARG1-of (s11i2 / identity-91
                :ARG2 (s11x6 / 公司
                    :mod (s11x7 / 母))))
        :ARG1 (s11x8 / 发行-01
            :ARG0 s11c
            :ARG1 (s11n2 / newspaper
                :name (s11n3 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :aspect process)
        :temporal (s11d / date-entity
            :year 2007
            :month 7)
        :aspect performance)
    :ARG2 (s11x2 / 继续-01
        :ARG0 (s11x4 / 网络版
            :part-of (s11x5 / 周报))
        :ARG1 (s11x3 / 生存-01
            :ARG0 s11x4
            :aspect state)
        :temporal s11d
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11x)
               (s11x :overlap s11x8)
               (s11x :overlap s11x2)
               (s11x2 :overlap s11x3))
    :modal ((root :modal author)
            (author :full-affirmative s11x8)
            (author :full-affirmative s11x)
            (author :full-affirmative s11x3)
            (author :full-affirmative s11x2))
    :coref ((s11n2 :same-entity s11x5)))


################################################################################
# meta-info
# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。

# sentence level graph:
(s12b / but-91
    :ARG1 (s12a / and
        :op1 (s12x / 宣称-01
            :ARG0 (s12n / newspaper
                :name (s12n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :ARG1 (s12h / have-mod-91
                :ARG1 (s12x4 / 报导-01
                    :aspect habitual)
                :ARG2 (s12x3 / 真实)
                :mod (s12x2 / 都)
                :aspect state
                :quote s12x)
            :aspect performance)
        :op2 (s12i3 / identity-91
            :ARG1 (s12x5 / 标语
                :possessor s12n)
            :ARG2 (s12x6 / 报导-01
                :ARG0 s12n
                :ARG1 (s12x8 / 事实)
                :mod (s12x7 / 只)
                :aspect habitual
                :quote s12i3)
            :aspect state))
    :ARG2 (s12i2 / identity-91
        :ARG1 (s12x9 / 目的
            :purpose-of (s12x10 / 报导-01
                :mod (s12x11 / 大部分)
                :aspect habitual))
        :ARG2 (s12x12 / 博君一笑)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
               (s12x :overlap s12x4)
               (s12x4 :overlap s12x6)
               (s12x4 :overlap s12x10))
    :modal ((root :modal author)
            (author :full-affirmative s12x4)
            (author :full-affirmative s12h)
            (author :full-affirmative s12x)
            (author :full-affirmative s12x6)
            (author :full-affirmative s12i3)
            (author :full-affirmative s12x10)
            (author :full-affirmative s12i2)
            (author :full-affirmative s12n)
            (s12n :full-affirmative s12h)
            (s12n :full-affirmative s12x6)
            (s12n :full-affirmative s12x10))
    :coref ((s11n2 :same-entity s12n)))


################################################################################
# meta-info
# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。

# sentence level graph:
(s13a / and
    :op1 (s13x2 / 报导-01
        :ARG0 (s13p / person
            :refer-number plural
            :refer-person 3rd)
        :ARG1 (s13x4 / 题材
            :example (s13a2 / and
                :op1 (s13x5 / 外星人)
                :op2 (s13x6 / 航天员
                    :mod (s13x11 / 古代))
                :op3 (s13x7 / 旅行
                    :mod (s13x12 / 时间))
                :op4 (s13x8 / 大脚)
                :op5 (s13x9 / 欧帕兹)
                :op6 (s13x10 / 等)))
        :frequency (s13x3 / 经常)
        :aspect habitual)
    :op2 (s13x / 创造-01
        :ARG0 s13p
        :ARG1 (s13x13 / 人物
            :mod (s13x14 / 虚拟)
            :quant (s13x15 / 一些)
            :ARG0-of (s13x16 / 出现-01
                :ARG1 (s13x18 / 中
                    :op1 (s13x19 / 新闻
                        :possessor s13p))
                :frequency (s13x17 / 重复)
                :aspect habitual)
            :example (s13a3 / and
                :op1 (s13i2 / individual-person
                    :name (s13n / name
                        :op1 "蝙蝠"
                        :op2 "男孩"))
                :op2 (s13i3 / individual-person
                    :name (s13n2 / name
                        :op1 "外星人"
                        :op2 "P"
                        :op3 "'"
                        :op4 "Lod"))
                :op3 (s13x20 / 等)))
        :aspect performance
        :mod (s13x21 / 甚至)))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13x2)
               (s13x2 :overlap s13x)
               (s13x :overlap s13x6))
    :modal ((root :modal author)
            (author :full-affirmative s13x2)
            (author :full-affirmative s13x16)
            (author :full-affirmative s13x))
    :coref ((s12n :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14x / 算是-01
    :ARG0 (s14i2 / implicit-argument
        :ARG1-of (s14h / have-degree-91
            :ARG1 (s14x3 / 大)
            :ARG2 (s14x4 / 最)
            :ARG5 (s14x5 / 其中))
        :unit (s14x2 / 宗))
    :ARG1 (s14x6 / 活动-01
        :ARG0 (s14x7 / 外星人)
        :place (s14p / planet
            :name (s14n / name
                :op1 "地球"))
        :aspect activity)
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :before s14x)
               (s14x :overlap s14x6))
    :modal ((root :modal author)
            (author :full-affirmative s14x6)
            (author :neutral-affirmative s14x)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15x / 指-02
    :ARG1 (s15c / consecutive
        :op1 (s15x3 / 有-03
            :ARG0 (s15a / and
                :op1 (s15i2 / individual-person
                    :name (s15n / name
                        :op1 "希拉里"
                        :op2 "·"
                        :op3 "克林顿")
                    :ARG1-of (s15h / have-rel-role-91
                        :ARG3 (s15x6 / 第一夫人
                            :mod (s15x7 / 前)
                            :place (s15c2 / country
                                :name (s15n2 / name
                                    :op1 "美国")))))
                :op2 (s15x11 / 外星人
                    :name (s15n4 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod")))
            :ARG1 (s15x4 / 关系
                :mod (s15x5 / 暧昧))
            :aspect state
            :quote s15x)
        :op2 (s15x2 / 领养-00
            :ARG0 s15i2
            :ARG1 (s15x9 / 宝宝
                :mod (s15x10 / 外星))
            :aspect performance
            :quote s15x))
    :aspect performance)


# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15x)
               (s15x :overlap s15x3)
               (s15x3 :after s15x2))
    :modal ((root :modal author)
            (s15a :full-affirmative s15x3)
            (s15a :full-affirmative s15x2)
            (author :full-affirmative s15x)
            (author :full-affirmative s15a)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 96 / P 100 / F 98
a_event_concept: R 91 / P 91 / F 91
a_entity_found: R 93 / P 96 / F 95
a_entity_concept: R 87 / P 87 / F 87
a_granularity: R 92 / P 92 / F 92
b_event_sense: R 89 / P 89 / F 89
c_aspect: R 78 / P 78 / F 78
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 100 / P 40 / F 57
d_core_args_event: R 63 / P 59 / F 61
d_core_args_abstract: R 47 / P 58 / F 52
d_peripheral_event: R 57 / P 36 / F 44
d_peripheral_entity: R 56 / P 50 / F 53
e_core_labels: R 87 / P 87 / F 87
e_peripheral_labels: R 92 / P 92 / F 92
f_name_tokens: R 88 / P 88 / F 88
g_reentrancy: R 42 / P 71 / F 53
h_temporal: R 65 / P 52 / F 58
i_modal: R 75 / P 69 / F 72
j_coref_chain: R 50 / P 40 / F 44
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_found | missing | s11x7: 母 -> - | no node in the prediction matches it
a_entity_concept | wrong | s11x6: 公司 -> 母公司 | 公司 -> 母公司
a_entity_concept | wrong | s11x5: 周报 -> 仍 | 周报 -> 仍
a_granularity | missing | «公司» 公司: «公司» 公司 -> «美国媒体公司» company | inside a wider predicted node
a_granularity | missing | «周报» 周报: «周报» 周报 -> «《世界新闻周报》» newspaper | inside a wider predicted node
a_granularity | extra | «美国媒体公司» company: «公司» 公司 -> «美国媒体公司» company | wider than the gold node
a_granularity | extra | «《世界新闻周报》» newspaper: «周报» 周报 -> «《世界新闻周报》» newspaper | wider than the gold node
c_aspect | wrong | s11x8:aspect: process -> habitual | process -> habitual
c_aspect | wrong | s11x3:aspect: state -> activity | state -> activity
d_core_args_event | partial | s11x2: arg0 s11x4/网络版; arg1 s11x3/生存-01 -> arg1 s11x3/生存-01 | missing arg0 s11x4/网络版
d_core_args_event | extra | s11x3: - -> arg0 s11x4/网络版 | extra arg0 s11x4/网络版
d_peripheral_event | extra | s11x2: - -> mod s11x5/周报 | extra mod s11x5/周报
d_peripheral_entity | missing | s11x6: mod s11x7/母 -> - | missing mod s11x7/母
d_peripheral_entity | missing | s11x5: part s11x4/网络版 -> - | missing part s11x4/网络版
g_reentrancy | missing | s11x2/继续-01 -temporal-> s11d/date-entity: s11x2/继续-01 -temporal-> s11d/date-entity -> - | the prediction has no such edge
g_reentrancy | missing | s11x3/生存-01 -arg0-> s11x4/网络版: s11x3/生存-01 -arg0-> s11x4/网络版 -> - | the prediction has the edge but not as a reentrancy
g_reentrancy | missing | s11x8/发行-01 -arg0-> s11c/company: s11x8/发行-01 -arg0-> s11c/company -> - | the prediction has no such edge
g_reentrancy | extra | s11w/newspaper -part-> s11x6/网络版: - -> s11w/newspaper -part-> s11x6/网络版 | gold has no such reentrancy
a_event_found | missing | s12i2: identity-91 -> - | no node in the prediction matches it
a_event_concept | wrong | s12h: have-mod -> have-purpose | have-mod -> have-purpose
a_entity_found | missing | s12x9: 目的 -> - | no node in the prediction matches it
a_entity_concept | wrong | s12a: and -> 都 | and -> 都
c_aspect | wrong | s12x:aspect: performance -> activity | performance -> activity
d_core_args_event | wrong | s12b: arg1 s12a/and; arg2 s12i2/identity-91 -> arg1 s12x/宣称-01; arg2 s12h/have-mod-91 | missing arg1 s12a/and; missing arg2 s12i2/identity-91; extra arg1 s12x/宣称-01; extra arg2 s12h/have-mod-91
d_core_args_event | partial | s12x: arg0 s12n/newspaper; arg1 s12h/have-mod-91 -> arg0 s12n/newspaper; arg1 s12x3/真实 | missing arg1 s12h/have-mod-91; extra arg1 s12x3/真实
d_core_args_abstract | partial | s12h: arg1 s12x4/报导-01; arg2 s12x3/真实 -> arg1 s12x4/报导-01; arg2 s12x12/博君一笑 | missing arg2 s12x3/真实; extra arg2 s12x12/博君一笑
d_peripheral_event | extra | s12x: - -> medium s12x5/标语 | extra medium s12x5/标语
d_peripheral_event | extra | s12x4: - -> quant s12x11/大部分 | extra quant s12x11/大部分
d_peripheral_event | missing | s12x10: mod s12x11/大部分; purpose s12x9/目的 -> - | missing mod s12x11/大部分; missing purpose s12x9/目的
d_peripheral_entity | extra | s12x3: - -> mod s12a/and | extra mod s12a/and
g_reentrancy | missing | s12h/have-mod-91 -quote-> s12x/宣称-01: s12h/have-mod-91 -quote-> s12x/宣称-01 -> - | the prediction has no such edge
g_reentrancy | missing | s12x6/报导-01 -quote-> s12i3/identity-91: s12x6/报导-01 -quote-> s12i3/identity-91 -> - | the prediction has no such edge
g_reentrancy | extra | s12x3/报导-01 -arg0-> s12n/newspaper: - -> s12x3/报导-01 -arg0-> s12n/newspaper | gold has no such reentrancy
a_entity_concept | wrong | s13x18: 中 -> 有 | 中 -> 有
a_entity_concept | wrong | s13i2: individual-person -> person | individual-person -> person
a_entity_concept | wrong | s13i3: individual-person -> name | individual-person -> name
a_granularity | missing | «P» individual-person/individual-person/person: «P» individual-person/individual-person/person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person/individual-person/person -> «P'Lod» 外星人 | wider than the gold node
c_other_attributes | extra | s13i3:op1: - -> p | gold has no :op1
c_other_attributes | extra | s13i3:op2: - -> ' | gold has no :op2
c_other_attributes | extra | s13i3:op3: - -> lod | gold has no :op3
d_core_args_event | wrong | s13x16: arg0 s13x13/人物; arg1 s13x18/中 -> arg0 s13x19/新闻; arg1 s13x13/人物 | arg0 s13x13/人物: predicted as arg1; missing arg1 s13x18/中; extra arg0 s13x19/新闻
d_peripheral_event | wrong | s13x16: frequency s13x17/重复 -> manner s13x17/重复 | frequency s13x17/重复: predicted as manner
d_peripheral_entity | missing | s13x4: example s13a2/and -> - | missing example s13a2/and
d_peripheral_entity | extra | s13a2: - -> mod s13x10/等 | extra mod s13x10/等
d_peripheral_entity | extra | s13a3: - -> mod s13x20/等 | extra mod s13x20/等
e_core_labels | wrong | s13x16 -arg0-> s13x13: arg0 -> arg1 | arg0 -> arg1
e_peripheral_labels | wrong | s13x16 -frequency-> s13x17: frequency -> manner | frequency -> manner
f_name_tokens | missing | s13i3: 外星人 p ' lod -> - | the prediction has no :name
f_name_tokens | extra | s13n2: - -> p ' lod | gold has no :name
a_entity_found | missing | s14i2: implicit-argument -> - | no node in the prediction matches it
a_entity_found | missing | s14p: planet -> - | no node in the prediction matches it
c_aspect | wrong | s14x6:aspect: activity -> process | activity -> process
d_core_args_event | partial | s14x: arg0 s14i2/implicit-argument; arg1 s14x6/活动-01 -> arg0 s14x2/宗; arg1 s14x6/活动-01 | missing arg0 s14i2/implicit-argument; extra arg0 s14x2/宗
d_core_args_abstract | wrong | s14h: arg1 s14i2/implicit-argument; arg1 s14x3/大; arg2 s14x4/最; arg5 s14x5/其中 -> arg1 s14x2/宗; arg2 s14x3/大; arg3 s14x4/最 | missing arg1 s14i2/implicit-argument; arg1 s14x3/大: predicted as arg2; arg2 s14x4/最: predicted as arg3; missing arg5 s14x5/其中; extra arg1 s14x2/宗
d_peripheral_event | wrong | s14x6: place s14p/planet -> place s14n/name | missing place s14p/planet; extra place s14n/name
d_peripheral_entity | extra | s14x2: - -> mod s14x5/其中 | extra mod s14x5/其中
e_core_labels | wrong | s14h -arg1-> s14x3: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s14h -arg2-> s14x4: arg2 -> arg3 | arg2 -> arg3
a_event_concept | wrong | s15h: have-rel-role -> 还 | have-rel-role -> 还
a_entity_found | extra | s15x11: - -> 后来 | matches no gold node
a_entity_found | extra | s15x13: - -> 就 | matches no gold node
a_entity_concept | wrong | s15c: consecutive -> have-org-role | consecutive -> have-org-role
a_granularity | missing | «P» individual-person: «P» individual-person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person -> «P'Lod» 外星人 | wider than the gold node
b_event_sense | wrong | s15x3: 有-03 -> 有-01 | 有-03 -> 有-01
b_event_sense | wrong | s15x2: 领养 -> 领养-01 | 领养 -> 领养-01
d_core_args_event | wrong | s15x: arg1 s15c/consecutive -> arg1 s15a/and | missing arg1 s15c/consecutive; extra arg1 s15a/and
d_core_args_event | partial | s15x3: arg0 s15a/and; arg1 s15x4/关系 -> arg0 s15i2/individual-person; arg1 s15x4/关系 | missing arg0 s15a/and; extra arg0 s15i2/individual-person
d_core_args_abstract | missing | s15h: arg1 s15i2/individual-person; arg3 s15x6/第一夫人 -> - | missing arg1 s15i2/individual-person; missing arg3 s15x6/第一夫人
d_peripheral_event | extra | s15x: - -> mod s15x13/就 (not in gold) | extra mod s15x13/就 (not in gold)
d_peripheral_event | extra | s15x2: - -> mod s15h/have-rel-role-91; temporal s15x11/后来 (not in gold) | extra mod s15h/have-rel-role-91; extra temporal s15x11/后来 (not in gold)
d_peripheral_entity | extra | s15c: - -> mod s15x7/前 | extra mod s15x7/前
d_peripheral_entity | missing | s15x6: mod s15x7/前; place s15c2/country -> - | missing mod s15x7/前; missing place s15c2/country
g_reentrancy | missing | s15x2/领养 -quote-> s15x/指-02: s15x2/领养 -quote-> s15x/指-02 -> - | the prediction has no such edge
g_reentrancy | missing | s15x3/有-03 -quote-> s15x/指-02: s15x3/有-03 -quote-> s15x/指-02 -> - | the prediction has no such edge
h_temporal | wrong | 报导-01 «报导» (snt12 s12x10 = pred s12x3): 报导-01 «报导» (snt12 s12x4 = pred s12x9) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12x3) -> 真实 «真实» (snt12 s12x3 = pred s12x2) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12x3) | right relation, wrong parent
h_temporal | extra | 博君一笑 «博君一笑» (snt12 s12x12 = pred s12x11): - -> 报导-01 «报导» (snt12 s12x4 = pred s12x9) :overlap 博君一笑 «博君一笑» (snt12 s12x12 = pred s12x11) | gold gives this node no temporal parent
h_temporal | extra | 真实 «真实» (snt12 s12x3 = pred s12x2): - -> 宣称-01 «宣称» (snt12 s12x = pred s12x) :overlap 真实 «真实» (snt12 s12x3 = pred s12x2) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt12 s12x6 = pred s12x6): 报导-01 «报导» (snt12 s12x4 = pred s12x9) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12x6) -> 宣称-01 «宣称» (snt12 s12x = pred s12x) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12x6) | right relation, wrong parent
h_temporal | wrong | 创造-01 «创造» (snt13 s13x = pred s13x13): 报导-01 «报导» (snt13 s13x2 = pred s13x3) :overlap 创造-01 «创造» (snt13 s13x = pred s13x13) -> 中 «中» (snt13 s13x18 = pred s13x) :overlap 创造-01 «创造» (snt13 s13x = pred s13x13) | right relation, wrong parent
h_temporal | extra | 出现-01 «出现» (snt13 s13x16 = pred s13x17): - -> 创造-01 «创造» (snt13 s13x = pred s13x13) :after 出现-01 «出现» (snt13 s13x16 = pred s13x17) | gold gives this node no temporal parent
h_temporal | extra | 中 «中» (snt13 s13x18 = pred s13x): - -> document-creation-time :before 中 «中» (snt13 s13x18 = pred s13x) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt13 s13x2 = pred s13x3): document-creation-time :before 报导-01 «报导» (snt13 s13x2 = pred s13x3) -> 中 «中» (snt13 s13x18 = pred s13x) :overlap 报导-01 «报导» (snt13 s13x2 = pred s13x3) | wrong parent and relation
h_temporal | missing | 航天员 «航天员» (snt13 s13x6 = pred s13x6): 创造-01 «创造» (snt13 s13x = pred s13x13) :overlap 航天员 «航天员» (snt13 s13x6 = pred s13x6) -> - | the prediction gives this node no temporal parent
h_temporal | extra | 旅行 «旅行» (snt13 s13x7 = pred s13x8): - -> 中 «中» (snt13 s13x18 = pred s13x) :overlap 旅行 «旅行» (snt13 s13x7 = pred s13x8) | gold gives this node no temporal parent
h_temporal | wrong | 算是-01 «算是» (snt14 s14x = pred s14x): document-creation-time :before 算是-01 «算是» (snt14 s14x = pred s14x) -> document-creation-time :depends-on 算是-01 «算是» (snt14 s14x = pred s14x) | right parent, wrong relation
i_modal | partial | have-mod-91 (snt12 s12h = pred s12h): author :full-affirmative have-mod-91 (snt12 s12h = pred s12h); newspaper (snt12 s12n = pred s12n) :full-affirmative have-mod-91 (snt12 s12h = pred s12h) -> author :full-affirmative have-mod-91 (snt12 s12h = pred s12h) | agrees on part of the relations
i_modal | missing | identity-91 (snt12 s12i2): author :full-affirmative identity-91 (snt12 s12i2) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | partial | 报导-01 «报导» (snt12 s12x10 = pred s12x3): author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x3); newspaper (snt12 s12n = pred s12n) :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x3) -> author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x3) | agrees on part of the relations
i_modal | extra | 博君一笑 «博君一笑» (snt12 s12x12 = pred s12x11): - -> author :full-affirmative 博君一笑 «博君一笑» (snt12 s12x12 = pred s12x11) | gold gives this node no modal parent
i_modal | extra | 真实 «真实» (snt12 s12x3 = pred s12x2): - -> newspaper (snt12 s12n = pred s12n) :full-affirmative 真实 «真实» (snt12 s12x3 = pred s12x2) | gold gives this node no modal parent
i_modal | partial | 报导-01 «报导» (snt12 s12x6 = pred s12x6): author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12x6); newspaper (snt12 s12n = pred s12n) :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12x6) -> author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12x6) | agrees on part of the relations
i_modal | extra | 中 «中» (snt13 s13x18 = pred s13x): - -> author :full-affirmative 中 «中» (snt13 s13x18 = pred s13x) | gold gives this node no modal parent
i_modal | extra | 旅行 «旅行» (snt13 s13x7 = pred s13x8): - -> author :full-affirmative 旅行 «旅行» (snt13 s13x7 = pred s13x8) | gold gives this node no modal parent
i_modal | missing | and (snt15 s15a = pred s15a): author :full-affirmative and (snt15 s15a = pred s15a) -> - | the prediction gives this node no modal parent
i_modal | wrong | 领养 «领养» (snt15 s15x2 = pred s15x8): and (snt15 s15a = pred s15a) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15x8) -> 指-02 «指» (snt15 s15x = pred s15x) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15x8) | right relation, wrong parent
i_modal | wrong | 有-03 «有» (snt15 s15x3 = pred s15x2): and (snt15 s15a = pred s15a) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15x2) -> 指-02 «指» (snt15 s15x = pred s15x) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15x2) | right relation, wrong parent
j_coref_chain | partial | newspaper (snt11 s11n2 = pred s11w): 周报 «周报» (snt11 s11x5 = pred s11x7); newspaper (snt12 s12n = pred s12n); person «P» (snt13 s13p = pred s13p) -> newspaper (snt12 s12n = pred s12n); person «P» (snt13 s13p = pred s13p) | not linked to: 周报 «周报» (snt11 s11x5 = pred s11x7)
j_coref_chain | missing | 周报 «周报» (snt11 s11x5 = pred s11x7): newspaper (snt11 s11n2 = pred s11w); newspaper (snt12 s12n = pred s12n); person «P» (snt13 s13p = pred s13p) -> - | the prediction links it to nothing
j_coref_chain | partial | newspaper (snt12 s12n = pred s12n): newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x7); person «P» (snt13 s13p = pred s13p) -> newspaper (snt11 s11n2 = pred s11w); person «P» (snt13 s13p = pred s13p) | not linked to: 周报 «周报» (snt11 s11x5 = pred s11x7)
j_coref_chain | extra | name (snt13 s13n2 = pred s13x20): - -> 外星人 «外星人» (snt15 s15x11 = pred s15x7) | gold links it to nothing
j_coref_chain | partial | person «P» (snt13 s13p = pred s13p): newspaper (snt12 s12n = pred s12n); newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x7) -> newspaper (snt12 s12n = pred s12n); newspaper (snt11 s11n2 = pred s11w) | not linked to: 周报 «周报» (snt11 s11x5 = pred s11x7)
j_coref_chain | extra | 外星人 «外星人» (snt15 s15x11 = pred s15x7): - -> name (snt13 s13n2 = pred s13x20) | gold links it to nothing

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.