<!-- system -->
You review UMR annotations made with an instruction, and say what in the instruction should change.
<!-- user -->
An annotator (a model) annotated the sentences below in Uniform Meaning Representation (UMR), following the instruction below. A judge (umrjudge) then compared its annotation with the expert gold annotation, check by check (concepts, senses, roles, attributes, named entities, reentrancy, and the document-level temporal, modal and coreference relations).

Your task: find the error patterns that cost the most, explain why they happen given the instruction (a rule that is missing, unclear, wrong, or not followed), and say what to change in the instruction to fix them so that they do not recur on other documents. Order them by cost, most costly first. Say also what the annotator got right that the instruction should keep. Give your advice as general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences; describe each case by its kind (e.g. a verb of saying with a clause object, a noun modified by a measure phrase).

You may use the tools to check the guidelines (search_guidelines), PropBank (propbank_lookup) and how other gold annotations do a case (search_annotations).

# The instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document (under **Input**, one sentence per line) in Uniform Meaning Representation (UMR):
every sentence's graph, then the document-level temporal, modal and coreference relations. It is compared node by
node and relation by relation with an expert gold annotation made by these guidelines; every concept, sense, role,
attribute and relation counts.

- Follow the guidelines and their examples. When they do not settle a case, use `search_guidelines`; look up every
  predicate with `propbank_lookup` before choosing its sense and roles; check gold constructions with
  `search_annotations`. Many calls are expected.


## Guidelines

# UMR guidelines, abridged



## 1. What a UMR is

A UMR has one graph per sentence (PENMAN, adapted from AMR) and document-level temporal, modal and coreference relations.

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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. In Chinese documents write **no** `:wiki` at all. A named human or character, fictional too, is `individual-person`. A bare category noun right before a name (no 的, no title) is the type concept, not an apposition. A middle dot inside a
transliterated foreign name is kept as its own `:opN "·"`. A title or role noun before a name is `:ARG1-of (h / have-org-role-91
:ARG3 <role>)` (the holder is always `:ARG1`, never `:ARG0`); separately, a role noun built from a verb + 人/者 is `(r / 人 :ARG0-of (v / verb-0N ...))` (`performance` for a completed act,
e.g. founding). A descriptive noun phrase in apposition to a name is `:ARG1-of (i / identity-91 :ARG2 <head noun with all its
modifiers>)` on the named entity; modifiers written before the apposition noun (的-phrases, 旗下, property words) go on that noun, not on the entity. A periodical, tabloid or magazine name is `newspaper`, not `publication`. Types as in AMR (`country`, `city`, `organization`, `company`, `planet`, `spaceship`, ...).

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

X 是 Adj (的) / X 都是 Adj: `have-mod-91 :ARG1 X :ARG2 Adj` (adverb as `:mod` of have-mod-91), never an `Adj-01` event. A title held through marriage (first lady) is `have-rel-role-91 :ARG3 <title>`, country `:place` and former `:mod` on the title.

Role nouns are reified the same way: *the president of Russia* →
`(p / person :ARG1-of (h / have-org-role-91 :ARG2 (c / country ...) :ARG3 (p2 / president)))`;
*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. An omitted head noun is `implicit-argument`, not `thing`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`; 等/*etc.* closing a list is its last `:opN`. "N 有 A、B…等" listing examples of N → `:example (and …)` on N, no 有 node; "A 与 B 有 <relation noun>" → `有-03 :ARG0 (and A B) :ARG1 <noun>`, never `:companion`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `(b / but-91 :ARG1 ... :ARG2 ...)`.
  These frames take `:ARG1`/`:ARG2`, never `:op1`/`:op2`. A connective opening a sentence (不过, 但是, 然而, 因此) that relates it to an earlier sentence gets no frame; annotate the clause alone. A time word or adverbial of a clause attaches to that
  clause's event, never to the discourse frame;
- concession `:concession`, condition `:condition`, reason `:reason` (for 由于/因为 phrases giving the reason for a state, an action or a judgement), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`. With 但是/不过/却 later in the same sentence, 虽然/尽管 gives `but-91 :ARG1 <concessive clause(s)> :ARG2 <main clause>` instead.- Reified reason and purpose: when a reason marker is paired with a result marker (因为…于是/所以, 由于…而), or a clause has a
  marked purpose clause (为了, 以, 以便), use `(h / have-reason-91 :ARG1 <result event> :ARG2 <cause event> :aspect state)` and
  `(h2 / have-purpose-91 :ARG1 <main event> :ARG2 <purpose event> :aspect state)`, nesting have-purpose-91 inside have-reason-91
  when both occur. Both frames get `(author :full-affirmative h)` and no temporal parent. Keep the `:reason`/`:purpose` roles for
  unpaired phrases inside one clause.
- A purpose stated as a noun (以 Y 为目的/目标) is `(i / identity-91 :ARG1 (m / 目的 :purpose-of <event>) :ARG2 Y)`; Y is a plain concept without aspect or links.
- A parenthetical or colon restatement (slogan, gloss) is its own `identity-91 :ARG1 <noun> :ARG2 <content>` clause joined to the previous clause by `and`, never `:medium`/`:mod`.
- 后来/*later, then* joining two predicates → `(c / consecutive :op1 … :op2 …)`, no node for 后来. nor for 还/也 right after it; a dropped subject of the later clause re-enters the first clause's subject. Discourse 就/便 outside a condition gets no node.

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

Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. The reported content's top event, and each of its conjuncts, always gets `:quote <reporting event>` (also passive 被指/被称); a quoted slogan's content gets `:quote` on its framing node.

### 3.1 Attachment rules (frequent errors)

- Every adverb that carries meaning (*already, still, also, all/both*; 已经, 仍, 也, 都, 均) gets its own node,
  attached as `:mod` to the predicate it scopes over, not to a noun. Time adverbs (曾经, 曾, *once, formerly*) are
  `:temporal`, not `:mod`. Frequency adverbs (经常, 常常, 往往, 重复; *often, repeatedly*) are `:frequency`.
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
- Exception (control): the subject of an aspectual or control verb (继续, 停止, 开始) is its `:ARG0` and re-enters as `:ARG0` of its event complement, event nominals included. A time expression scoping over both clauses of a but-91/contrast attaches to both clause events.
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
  with the country or place as `:place` of the history noun. The place rule holds for abstract nouns too. Every location postposition likewise: 在 N 中/上/里 → `(z / 中 :op1 N)`. Check the roleset for a location argument (出现-type) before using `:place`.
- A property word or chengyu used attributively ("absurd content", X 的 Y with X a property) is a `:mod` concept,
  not an event: it gets no aspect and no temporal or modal links.

## 4. Attributes

### 4.1 Aspect (`:aspect`, on every event)

Decide in this order before using the table:
1. Is the event a routine or recurring practice of its subject (an organisation or periodical publishing,
   printing, issuing, reporting, broadcasting)? → `habitual`, also for a process nominal naming such a practice (but an event-nominal complement of an aspectual verb such as 停止 is `process`) (e.g. subject of
   "is/became its feature"); this step precedes step 3. A verb of what a publication holds or carries (contains articles) is `process`. This holds whatever the tense, and also under an
   aspectual verb (continue, stop).
2. Does an aspectual verb of stopping or completion taking an event complement (*has already stopped doing X*) describe a present condition? → `state`.
   An aspectual verb of continuation or ongoing action in the present (*continues to do X*, 继续) is `activity`.
   A lexical verb of ending with no event complement (close down, cease publication; 停刊, 倒闭), even with *already*, is `performance`.
   State verbs (have, own, belong, be, exist, survive; 有, 拥有, 是, 存在, 生存) stay `state` even with 过, 曾经 or a duration.
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

Also: a completed past speech act (claim, announce; 宣称) is `performance`; a purpose or intended action is `activity`; a completed past event in a participle or relative clause
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
  - copular or identity predicates (`identity-91`, `have-mod-91`, `have-role-91` of a defining "A is a B" sentence), also inside reported content; their eventive argument takes the matrix verb as parent;
  - fame or property states used as attributes inside a noun phrase (*famous X*; see the fame rule below);
  - property modifiers;
  - vague deictic time words (*now, currently, nowadays*, 现在, 目前, 当前).
- Time expressions: an absolute date in the past gets `(document-creation-time :before s1t)` (a future one `:after`);
  only a relative deictic one (*today, yesterday*, 今天) gets `(document-creation-time :depends-on s1t)`.
- An event in the clause of a date or time expression gets `(date :overlap event)`; use `:contained` only when the time
  expression is explicitly a span (during, within, 期间); a year or decade takes `:overlap`.
- Past narrative: the anchor event of each new sentence links to `document-creation-time :before`, not to the previous
  sentence's event. Link it to an earlier event only when the sentence explicitly continues from it (也/还 + 成/成为/变成, *also became*, *as a
  result*, 于是), and then with `:overlap` unless the order is stated.
- **Within a sentence, chain the events.** Pick one anchor event (the main eventive predicate; in a coordination, the first conjunct's) and link
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
  node, or an event used as conceiver). Every event of the reported content, including an appended slogan or quotation and later clauses still reporting it, takes the speaker as modal parent; the content's top node carries `:quote <saying verb>`.
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
- Within one sentence, a pronoun (also 他们/*they* for an organisation or publication) or a dropped argument re-uses its antecedent's variable, no own node; a possessive pronoun on an event nominal is omitted. An overt repeated name or noun (short name, bare head noun) gets its own node plus a `:same-entity` triple. A later sentence's pronoun links to the antecedent entity.

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
- Same-sentence pronouns are re-entrancies, repeated nouns own nodes + `:coref`; control subjects re-enter nominal complements; a time over both halves of but-91 attaches to both.
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
        :ARG0 (s11c / company
            :ARG1-of (s11i / identity-91
                :ARG2 (s11x2 / 母公司))
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司"))
        :ARG1 (s11x3 / 发行-01
            :ARG1 (s11w / newspaper
                :name (s11n2 / name
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
    :ARG2 (s11x4 / 继续-01
        :ARG0 (s11x5 / 网络版
            :part-of (s11x6 / 周报))
        :ARG1 (s11x7 / 生存-01
            :ARG0 s11x5
            :aspect activity)
        :mod (s11x8 / 仍)
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11x)
               (s11x :overlap s11x3)
               (s11x :after s11x4)
               (s11x4 :overlap s11x7))
    :modal ((root :modal author)
            (author :full-affirmative s11x)
            (author :full-affirmative s11x3)
            (author :full-affirmative s11x4)
            (author :full-affirmative s11x7))
    :coref ((s11w :same-entity s11x6)))


################################################################################
# meta-info
# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。

# sentence level graph:
(s12b / but-91
    :ARG1 (s12a / and
        :op1 (s12x / 宣称-01
            :ARG0 (s12w / newspaper
                :name (s12n / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :ARG1 (s12h / have-mod-91
                :ARG1 (s12x2 / 报导-01
                    :aspect habitual)
                :ARG2 (s12x3 / 真实)
                :quote s12x
                :aspect state)
            :aspect performance)
        :op2 (s12i / identity-91
            :ARG1 (s12x5 / 标语
                :possessor s12w)
            :ARG2 (s12x6 / 报导-01
                :ARG0 (s12w2 / newspaper
                    :name (s12n2 / name
                        :op1 "世界"
                        :op2 "新闻"
                        :op3 "周报"))
                :ARG1 (s12x7 / 事实)
                :mod (s12x8 / 只)
                :aspect habitual)
            :aspect state))
    :ARG2 (s12i2 / identity-91
        :ARG1 (s12m / 目的
            :purpose-of (s12x9 / 报导-01
                :quant (s12x10 / 大部分)
                :aspect habitual))
        :ARG2 (s12x11 / 博君一笑)
        :mod (s12x12 / 都)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
               (s12x :overlap s12x2)
               (s12x :overlap s12x6)
               (s12x :overlap s12x9))
    :modal ((root :modal author)
            (author :full-affirmative s12x)
            (author :full-affirmative s12w)
            (s12w :full-affirmative s12h)
            (s12w :full-affirmative s12x2)
            (author :full-affirmative s12i)
            (author :full-affirmative s12x6)
            (author :full-affirmative s12i2)
            (author :full-affirmative s12x9))
    :coref ((s11x6 :same-entity s12w)
            (s12w :same-entity s12w2)))


################################################################################
# meta-info
# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。

# sentence level graph:
(s13a / and
    :op1 (s13x / 题材
        :ARG1-of (s13x2 / 报导-01
            :ARG0 (s13p / person
                :refer-person 3rd
                :refer-number plural)
            :frequency (s13x3 / 经常)
            :aspect habitual)
        :example (s13a2 / and
            :op1 (s13x4 / 外星人)
            :op2 (s13x5 / 航天员
                :mod (s13x6 / 古代))
            :op3 (s13x7 / 旅行
                :mod (s13x8 / 时间))
            :op4 (s13x9 / 大脚)
            :op5 (s13x10 / 欧帕兹)
            :op6 (s13x11 / 等)))
    :op2 (s13x12 / 创造-01
        :ARG0 s13p
        :ARG1 (s13x13 / 人物
            :quant (s13x15 / 一些)
            :ARG1-of (s13x16 / 出现-01
                :ARG0 (s13x17 / 中
                    :op1 (s13x18 / 新闻
                        :possessor s13p))
                :frequency (s13x19 / 重复)
                :aspect habitual)
            :mod (s13x14 / 虚拟)
            :example (s13a3 / and
                :op1 (s13p2 / individual-person
                    :name (s13n / name
                        :op1 "蝙蝠"
                        :op2 "男孩"))
                :op2 (s13x20 / 外星人
                    :name (s13n2 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod"))
                :op3 (s13x21 / 等)))
        :mod (s13x22 / 甚至)
        :aspect performance))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13x2)
               (s13x2 :overlap s13x12)
               (s13x12 :overlap s13x16))
    :modal ((root :modal author)
            (author :full-affirmative s13x2)
            (author :full-affirmative s13x12)
            (author :full-affirmative s13x16))
    :coref ((s12w2 :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14s / 算是-01
    :ARG0 (s14x / 最大宗
        :mod (s14x2 / 其中))
    :ARG1 (s14x3 / 活动-01
        :ARG0 (s14x4 / 外星人)
        :place (s14x5 / 地球)
        :aspect process)
    :modal-strength neutral-affirmative
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :overlap s14s)
               (s14s :overlap s14x3))
    :modal ((root :modal author)
            (author :neutral-affirmative s14s)
            (author :full-affirmative s14x3))
    :coref ((s13x4 :same-entity s14x4)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15z / 指-02
    :ARG1 (s15c / consecutive
        :op1 (s15y / 有-03
            :ARG0 (s15a / and
                :op1 (s15p / individual-person
                    :ARG1-of (s15h / have-rel-role-91
                        :ARG3 (s15x / 第一夫人
                            :place (s15c2 / country
                                :name (s15n2 / name
                                    :op1 "美国"))
                            :mod (s15x2 / 前)))
                    :name (s15n / name
                        :op1 "希拉里"
                        :op2 "·"
                        :op3 "克林顿"))
                :op2 (s15x3 / 外星人
                    :name (s15n3 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod")))
            :ARG1 (s15x4 / 关系
                :mod (s15x5 / 暧昧))
            :quote s15z
            :aspect state)
        :op2 (s15l / 领养-01
            :ARG0 s15p
            :ARG1 (s15x6 / 宝宝
                :mod (s15x7 / 外星))
            :quote s15z
            :aspect performance))
    :aspect performance)


# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15z)
               (s15z :overlap s15y)
               (s15y :after s15l))
    :modal ((root :modal author)
            (author :full-affirmative s15z)
            (s15z :full-affirmative s15y)
            (s15z :full-affirmative s15l))
    :coref ((s13x20 :same-entity s15x3)))



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
a_event_concept: R 100 / P 100 / F 100
a_entity_found: R 93 / P 98 / F 96
a_entity_concept: R 93 / P 93 / F 93
a_granularity: R 93 / P 93 / F 93
b_event_sense: R 94 / P 94 / F 94
c_aspect: R 89 / P 89 / F 89
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 100 / P 40 / F 57
d_core_args_event: R 86 / P 86 / F 86
d_core_args_abstract: R 100 / P 100 / F 100
d_peripheral_event: R 76 / P 67 / F 71
d_peripheral_entity: R 89 / P 89 / F 89
e_core_labels: R 94 / P 94 / F 94
e_peripheral_labels: R 94 / P 94 / F 94
f_name_tokens: R 88 / P 88 / F 88
g_reentrancy: R 67 / P 100 / F 80
h_temporal: R 71 / P 71 / F 71
i_modal: R 75 / P 79 / F 77
j_coref_chain: R 75 / P 33 / F 46
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_concept | wrong | s11x6: 公司 -> 母公司 | 公司 -> 母公司
a_entity_concept | wrong | s11x7: 母 -> 仍 | 母 -> 仍
a_granularity | missing | «公司» 公司: «公司» 公司 -> «美国媒体公司» company | inside a wider predicted node
a_granularity | missing | «周报» 周报: «周报» 周报 -> «《世界新闻周报》» newspaper | inside a wider predicted node
a_granularity | extra | «美国媒体公司» company: «公司» 公司 -> «美国媒体公司» company | wider than the gold node
a_granularity | extra | «《世界新闻周报》» newspaper: «周报» 周报 -> «《世界新闻周报》» newspaper | wider than the gold node
c_aspect | wrong | s11x3:aspect: state -> activity | state -> activity
d_peripheral_event | extra | s11x2: - -> mod s11x7/母 | extra mod s11x7/母
d_peripheral_entity | missing | s11x6: mod s11x7/母 -> - | missing mod s11x7/母
g_reentrancy | missing | s11x2/继续-01 -temporal-> s11d/date-entity: s11x2/继续-01 -temporal-> s11d/date-entity -> - | the prediction has no such edge
g_reentrancy | missing | s11x8/发行-01 -arg0-> s11c/company: s11x8/发行-01 -arg0-> s11c/company -> - | the prediction has no such edge
a_entity_found | extra | s12w2: - -> newspaper | matches no gold node
d_core_args_event | partial | s12x6: arg1 s12x8/事实 -> arg0 s12w2/newspaper (not in gold); arg1 s12x8/事实 | extra arg0 s12w2/newspaper (not in gold)
d_peripheral_event | partial | s12x10: mod s12x11/大部分; purpose s12x9/目的 -> purpose s12x9/目的; quant s12x11/大部分 | mod s12x11/大部分: predicted as quant
e_peripheral_labels | wrong | s12x10 -mod-> s12x11: mod -> quant | mod -> quant
g_reentrancy | missing | s12x6/报导-01 -arg0-> s12n/newspaper: s12x6/报导-01 -arg0-> s12n/newspaper -> - | the prediction has no such edge
g_reentrancy | missing | s12x6/报导-01 -quote-> s12i3/identity-91: s12x6/报导-01 -quote-> s12i3/identity-91 -> - | the prediction has no such edge
a_entity_concept | wrong | s13i3: individual-person -> name | individual-person -> name
a_granularity | missing | «P» individual-person/individual-person/person: «P» individual-person/individual-person/person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person/individual-person/person -> «P'Lod» 外星人 | wider than the gold node
c_other_attributes | extra | s13i3:op1: - -> p | gold has no :op1
c_other_attributes | extra | s13i3:op2: - -> ' | gold has no :op2
c_other_attributes | extra | s13i3:op3: - -> lod | gold has no :op3
d_core_args_event | wrong | s13x16: arg0 s13x13/人物; arg1 s13x18/中 -> arg0 s13x18/中; arg1 s13x13/人物 | arg0 s13x13/人物: predicted as arg1; arg1 s13x18/中: predicted as arg0
e_core_labels | wrong | s13x16 -arg0-> s13x13: arg0 -> arg1 | arg0 -> arg1
e_core_labels | wrong | s13x16 -arg1-> s13x18: arg1 -> arg0 | arg1 -> arg0
f_name_tokens | missing | s13i3: 外星人 p ' lod -> - | the prediction has no :name
f_name_tokens | extra | s13n2: - -> p ' lod | gold has no :name
a_event_found | missing | s14h: have-degree-91 -> - | no node in the prediction matches it
a_entity_found | missing | s14i2: implicit-argument -> - | no node in the prediction matches it
a_entity_found | missing | s14x3: 大 -> - | no node in the prediction matches it
a_entity_found | missing | s14x4: 最 -> - | no node in the prediction matches it
a_entity_found | missing | s14p: planet -> - | no node in the prediction matches it
a_entity_concept | wrong | s14x2: 宗 -> 最大宗 | 宗 -> 最大宗
c_aspect | wrong | s14x6:aspect: activity -> process | activity -> process
d_core_args_event | partial | s14x: arg0 s14i2/implicit-argument; arg1 s14x6/活动-01 -> arg0 s14x2/宗; arg1 s14x6/活动-01 | missing arg0 s14i2/implicit-argument; extra arg0 s14x2/宗
d_peripheral_event | wrong | s14x6: place s14p/planet -> place s14n/name | missing place s14p/planet; extra place s14n/name
d_peripheral_entity | extra | s14x2: - -> mod s14x5/其中 | extra mod s14x5/其中
a_granularity | missing | «P» individual-person: «P» individual-person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person -> «P'Lod» 外星人 | wider than the gold node
b_event_sense | wrong | s15x2: 领养 -> 领养-01 | 领养 -> 领养-01
h_temporal | wrong | 继续-01 «继续» (snt11 s11x2 = pred s11x4): 停止-01 «停止» (snt11 s11x = pred s11x) :overlap 继续-01 «继续» (snt11 s11x2 = pred s11x4) -> 停止-01 «停止» (snt11 s11x = pred s11x) :after 继续-01 «继续» (snt11 s11x2 = pred s11x4) | right parent, wrong relation
h_temporal | wrong | 报导-01 «报导» (snt12 s12x10 = pred s12x9): 报导-01 «报导» (snt12 s12x4 = pred s12x2) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12x9) -> 宣称-01 «宣称» (snt12 s12x = pred s12x) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12x9) | right relation, wrong parent
h_temporal | wrong | 报导-01 «报导» (snt12 s12x6 = pred s12x6): 报导-01 «报导» (snt12 s12x4 = pred s12x2) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12x6) -> 宣称-01 «宣称» (snt12 s12x = pred s12x) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12x6) | right relation, wrong parent
h_temporal | extra | 出现-01 «出现» (snt13 s13x16 = pred s13x16): - -> 创造-01 «创造» (snt13 s13x = pred s13x12) :overlap 出现-01 «出现» (snt13 s13x16 = pred s13x16) | gold gives this node no temporal parent
h_temporal | missing | 航天员 «航天员» (snt13 s13x6 = pred s13x5): 创造-01 «创造» (snt13 s13x = pred s13x12) :overlap 航天员 «航天员» (snt13 s13x6 = pred s13x5) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 算是-01 «算是» (snt14 s14x = pred s14s): document-creation-time :before 算是-01 «算是» (snt14 s14x = pred s14s) -> document-creation-time :overlap 算是-01 «算是» (snt14 s14x = pred s14s) | right parent, wrong relation
i_modal | partial | have-mod-91 (snt12 s12h = pred s12h): author :full-affirmative have-mod-91 (snt12 s12h = pred s12h); newspaper (snt12 s12n = pred s12w) :full-affirmative have-mod-91 (snt12 s12h = pred s12h) -> newspaper (snt12 s12n = pred s12w) :full-affirmative have-mod-91 (snt12 s12h = pred s12h) | agrees on part of the relations
i_modal | partial | 报导-01 «报导» (snt12 s12x10 = pred s12x9): author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x9); newspaper (snt12 s12n = pred s12w) :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x9) -> author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x9) | agrees on part of the relations
i_modal | wrong | 报导-01 «报导» (snt12 s12x4 = pred s12x2): author :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12x2) -> newspaper (snt12 s12n = pred s12w) :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12x2) | right relation, wrong parent
i_modal | partial | 报导-01 «报导» (snt12 s12x6 = pred s12x6): author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12x6); newspaper (snt12 s12n = pred s12w) :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12x6) -> author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12x6) | agrees on part of the relations
i_modal | missing | and (snt15 s15a = pred s15a): author :full-affirmative and (snt15 s15a = pred s15a) -> - | the prediction gives this node no modal parent
i_modal | wrong | 领养 «领养» (snt15 s15x2 = pred s15l): and (snt15 s15a = pred s15a) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) -> 指-02 «指» (snt15 s15x = pred s15z) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) | right relation, wrong parent
i_modal | wrong | 有-03 «有» (snt15 s15x3 = pred s15y): and (snt15 s15a = pred s15a) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) -> 指-02 «指» (snt15 s15x = pred s15z) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) | right relation, wrong parent
j_coref_chain | partial | newspaper (snt11 s11n2 = pred s11w): 周报 «周报» (snt11 s11x5 = pred s11x6); newspaper (snt12 s12n = pred s12w); person «P» (snt13 s13p = pred s13p) -> 周报 «周报» (snt11 s11x5 = pred s11x6); ?newspaper «世界 新闻 周报» (snt12 s12w2); newspaper (snt12 s12n = pred s12w); person «P» (snt13 s13p = pred s13p) | wrongly linked to: ?newspaper «世界 新闻 周报» (snt12 s12w2)
j_coref_chain | partial | 周报 «周报» (snt11 s11x5 = pred s11x6): newspaper (snt11 s11n2 = pred s11w); newspaper (snt12 s12n = pred s12w); person «P» (snt13 s13p = pred s13p) -> newspaper (snt11 s11n2 = pred s11w); ?newspaper «世界 新闻 周报» (snt12 s12w2); newspaper (snt12 s12n = pred s12w); person «P» (snt13 s13p = pred s13p) | wrongly linked to: ?newspaper «世界 新闻 周报» (snt12 s12w2)
j_coref_chain | extra | ?newspaper «世界 新闻 周报» (snt12 s12w2): - -> newspaper (snt12 s12n = pred s12w); newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x6); person «P» (snt13 s13p = pred s13p) | a predicted node that matches nothing in gold
j_coref_chain | partial | newspaper (snt12 s12n = pred s12w): newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x6); person «P» (snt13 s13p = pred s13p) -> ?newspaper «世界 新闻 周报» (snt12 s12w2); newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x6); person «P» (snt13 s13p = pred s13p) | wrongly linked to: ?newspaper «世界 新闻 周报» (snt12 s12w2)
j_coref_chain | extra | name (snt13 s13n2 = pred s13x20): - -> 外星人 «外星人» (snt15 s15x11 = pred s15x3) | gold links it to nothing
j_coref_chain | partial | person «P» (snt13 s13p = pred s13p): newspaper (snt12 s12n = pred s12w); newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x6) -> ?newspaper «世界 新闻 周报» (snt12 s12w2); newspaper (snt12 s12n = pred s12w); newspaper (snt11 s11n2 = pred s11w); 周报 «周报» (snt11 s11x5 = pred s11x6) | wrongly linked to: ?newspaper «世界 新闻 周报» (snt12 s12w2)
j_coref_chain | extra | 外星人 «外星人» (snt13 s13x5 = pred s13x4): - -> 外星人 «外星人» (snt14 s14x7 = pred s14x4) | gold links it to nothing
j_coref_chain | extra | 外星人 «外星人» (snt14 s14x7 = pred s14x4): - -> 外星人 «外星人» (snt13 s13x5 = pred s13x4) | gold links it to nothing
j_coref_chain | extra | 外星人 «外星人» (snt15 s15x11 = pred s15x3): - -> name (snt13 s13n2 = pred s13x20) | gold links it to nothing

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.