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
every sentence's graph, then the document-level temporal, modal and coreference relations.

- Follow the guidelines and their examples. When they do not settle a case, use `search_guidelines`; look up every
  predicate with `propbank_lookup` before choosing its sense and roles; check gold constructions with
  `search_annotations`. Many calls are expected.


## Guidelines

# UMR guidelines, abridged



## 1. What a UMR is

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

- predicate verbs, event nominals with process meaning (会议, 比赛), participles and relative-clause verbs;
- predicated states: adjectives and nouns in predicate position (*he is tall*, 他很高) — through the
  abstract predicates of 2.3 when there is no lexical verb.

Not events: entity nouns, modifier words with no roleset (see 3.1),
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
modifiers>)` on the named entity; modifiers written before the apposition noun (的-phrases, 旗下, property words) go on that noun, not on the entity. A periodical, tabloid or magazine name is `newspaper`, not `publication`.

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. A decade (X年代) is `:era`, never `:decade`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a numeral + measure word or classifier keeps the classifier as the unit,
ordinary classifiers included (个, 本, 只, 位, 份, 面): 三杯水 → `水 :quant 3 :unit 杯`, 一本书 → `书 :quant 1 :unit (s / 本)`.
A demonstrative + classifier (这个, 那份) also keeps the classifier as `:unit`.
The title marks of a work or publication name (《 and 》) are part of the name: `:op1 "《"`, then the words, then a last `:opN "》"`. A 「」/“” article or headline title used with a classifier or next to an article/news noun is a name too: `(p / publication :quant N :unit <classifier> :name (n / name :op1 "「" … :opN "」"))`, every word and mark an `:opN`; nothing inside it is analysed. A named event with a year in its name is `(e / event :name (n / name :op1 "<year>" :op2 "年" …))`, no links.

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
  add a re-entrancy to an earlier mention; leave the argument out. This also holds for infinitive-like and
  trailing clauses (never fill their agent with an entity of the main clause) and for possessors: a word like 旗下 is a `:mod`
  concept, not a `:possessor` taken from elsewhere. A trailing clause that describes the object just introduced (a new entity and
  what it holds or does) is a relative clause: attach its event with `:ARGn-of` on that object. Do not add relations the text does not state (e.g. a
  `:part-of` the words do not express). Use only roles of the closed list; a partitive word (其中, *among them, of which*) is a
  `:mod` on the noun it modifies, unless a superlative follows (then `:ARG5`, see have-degree-91).
- Exception (control): the subject of an aspectual or control verb (继续, 停止, 开始) is its `:ARG0` and re-enters as `:ARG0` of its event complement, event nominals included. A time expression over (or opening) a but-91/contrast attaches to both clause events; a still/continue second clause `:overlap`s the first, never `:after`.
- Relative clause headed by an aspectual verb ("N that has stopped V-ing"): N is `:ARGn-of` the inner verb, which is `:ARG1-of` the aspectual verb; N is not its argument.
- Read the roleset for every role. For Chinese belong-type rolesets (X belongs to Y), the gold convention is: the thing that
  belongs = `:ARG0`, the owner = `:ARG1`, even where the PropBank role glosses seem to say the reverse. So "N that belongs to X"
  is `(n / N :ARG0-of (b / belong-verb :ARG1 X))`. Never assume possessum = `:ARG1`.
- "Known/famous for X" (…而闻名, 以…著称): the famous entity is the `:ARG1` of the fame predicate, attached as
  `:ARG1-of` on that noun, and the X clause is `:reason` of it, with that noun as its agent. When such a clause
  follows "A is a B", attach it inside the B noun, not as a separate conjunct.
- Role choice for noun modifiers: a country, city or place modifying a noun → `:place`; a channel or medium
  (TV, radio, network, print) → `:medium`; an edition, section or component of a whole, or an article of a publication → `:part-of` (not `:possessor`).
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
  Give `have-degree-91` itself no modal link. With no head noun (其中 最 Adj + classifier): `(i / implicit-argument :unit <classifier> :ARG1-of (h / have-degree-91 :ARG1 (a / Adj) :ARG2 (m / 最) :ARG5 (q / 其中)))`.
- A postposition phrase over a time-span noun (X 历史上, *in X's history*) is `:temporal (s / 上 :op1 (h / 历史))` on its head,
  with the country or place as `:place` of the history noun. The place rule holds for abstract nouns too. Every location postposition likewise: 在 N 中/上/里 → `(z / 中 :op1 N)`. Appearance verbs (出现-type): the appearing entity is `:ARG0`, the 在 N 中 location `:ARG1` (gold convention).
- An attributive modifier (X 的 Y) that has a PropBank roleset (check it) is an event: a property predicate `(y / Y :ARG0-of (x / X-01 :aspect state))` (the role its roleset gives the described entity), a producing verb `:ARG1-of … :aspect performance`; it `:overlap`s the clause event, author modal parent. An event nominal modifying a noun is `:mod` with `process` aspect. A word with no roleset (relational or distinguishing word, chengyu) is a `:mod` concept,
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
   State verbs (have, own, belong, be, exist, survive; 有, 拥有, 是, 存在, 生存) stay `state` even with 过, 曾经, a duration, or under 继续/仍.
3. Is the event a process noun, including the object of a light or experiential verb (经, 经过, 进行, undergo)? → `process` (but an activity noun complementing a judging verb, 算/是-type, is `activity`).
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
  `:polarity`; the verb is `full-negative` (modal) and an event nested under it gets `(author :partial-affirmative e)`. The concept of a fused-negation verb is the
  un-negated verb with its own PropBank sense and roles (未经 → the 经-type verb's sense, with `:ARG0`/`:ARG1`), never `<negated word>-00`;
  its aspect follows that verb (`process` for 经/经过-type verbs). A compound "[process noun] + procedure/method/system noun" is
  reified as identity: `(p / procedure-noun :ARG0-of (i / identity-91 :ARG1 <event>))`, not `:mod`.
- `:mode imperative` (commands, 请, 别), `:mode interrogative` (questions; the questioned argument is
  `amr-unknown`, a yes/no question gets `:polarity amr-unknown`), `:mode expressive` (interjections).
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
- **Fame in a defining sentence.** The fame state has no temporal parent; it is the parent of the habitual RC event `(fame :contained e)`, which keeps its own DCT link; the reason event `:overlap`s e.
- Every node that carries `:aspect` gets a modal parent (normally `author :full-affirmative`). A relative-clause verb with an aspect
  ("N that belongs to X") also gets a temporal parent: `:overlap` with the event whose argument N is, or with the clause anchor.
  Copular and identity predicates get no temporal parent but do get a modal parent. An `identity-91` reifying an apposition inside a noun phrase gets no `:aspect` and no links at all. Only property words used as plain `:mod`
  (no aspect) get no links.
- A process nominal that is an argument of a verb takes that verb as its temporal parent with `:overlap`; do not leave it without a parent.
- Then every event: (1) a time expression of its clause; else (2) a clear earlier reference event; else (3) `document-creation-time` (`:before` past, `:overlap` present state, `:after` future; Chinese: decide from context, 了, 过, 将, 会).
- An event in a complement clause takes its matrix event as parent. Clauses restating or qualifying a report's content take the content's main event as parent, not the reporting verb. A purpose event `:overlap`s its main event (never
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
- Reported speech or thought: `(author :full-affirmative s9p)` for the speaker; every predicate of the content (also an appended slogan and later clauses about that source's reports) gets both `(author :full-affirmative e)` and `(s9p :full-affirmative e)`; event nominals that are arguments inside the content get author only. The content's top node carries `:quote <saying verb>`. A passive reporting verb with no speaker (被指): the conceiver is the content's subject node, with `(author :full-affirmative <subject>)`; never the reporting event.
- An event under a modal or complement-taking predicate (*want, try, plan, decide, hope*, 想, 希望, 打算,
  决定, 需要): the predicate is asserted by the author, the complement has the predicate as parent with
  `unspecified` (or the strength the predicate implies): `(author :full-affirmative s3w)`
  `(s3w :unspecified s3g)`.
- A conceiver that is not in the text is `null-conceiver`. Purpose and condition clauses may use the
  constants `purpose` and `have-condition` as parents of their events.
- In the sentence graph, write the strength of an event that is not `full-affirmative` from the author as
  `:modal-strength <value>` too.

### 5.3 Coreference (`:coref`)

- `(earlier :same-entity later)`: two mentions of the same entity — a pronoun and its antecedent, a repeated
  name, a definite description. Link each mention to its closest earlier mention, earlier one first;
  link entity nodes, never `name` nodes.
- `(earlier :same-event later)`: two mentions of the same event instance, with the same participants. Two
  different events of similar meaning (e.g. two different kinds of stopping) are not linked.
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Coreference only the discourse entities the text tracks (participants, the topic entity); never generic or kind nouns, example-list members, or a name given only as an example, even if the word recurs. A name used only as a modifier
  (a country name modifying a noun, a place in a `:place` role) is not linked across sentences.
- Within one sentence, a pronoun (also 他们/*they* for an organisation or publication) or a dropped argument re-uses its antecedent's variable, no own node; a possessive pronoun on an event nominal is omitted. An overt repeated name or noun (short name, bare head noun) gets its own node plus a `:same-entity` triple; but inside a slogan, gloss or parenthesis of that sentence it re-uses the variable. A later sentence's pronoun links to the antecedent entity.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words. When a word occurs more than once in a sentence (e.g. a common noun that also appears
inside a name), align each node to its own occurrence.

## 7. Checklist

- Balanced parentheses; unique `s<N>` variables; every event has `:aspect`, a temporal and a modal parent.
- Compounds split (prefix + noun, verb + 人/者); 「」 titles are unanalysed names.
- Same-sentence pronouns are re-entrancies, repeated nouns own nodes + `:coref`; control subjects re-enter nominal complements; a time over both halves of but-91 attaches to both.



</instruction>

# The sentences
16	2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。
17	不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。
18	如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。
19	为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。
20	该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt16
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
Words: 2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。

# sentence level graph:
(s16a / and
    :op1 (s16x / 报导-01
        :temporal (s16x4 / 时
            :op1 (s16x5 / 总统大选
                :temporal (s16d / date-entity
                    :year 2000)))
        :ARG0 (s16x2 / 刊
            :mod (s16x3 / 该))
        :ARG1 (s16x6 / 支持-01
            :ARG0 (s16x7 / 外星人)
            :ARG1 (s16x8 / 当-02
                :ARG0 (s16p / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16x9 / 总统)
                :aspect state)
            :quote s16x
            :aspect state)
        :aspect performance)
    :op2 (s16x10 / 注销-01
        :temporal s16x4
        :ARG0 s16x2
        :mod (s16x11 / 还)
        :ARG1 (s16x12 / 照片
            :mod (s16x13 / 握手-01
                :ARG0 (s16x14 / 双方)
                :aspect process)
            :ARG1-of (s16x15 / 合成-01
                :aspect performance))
        :aspect performance)
    :op3 (s16x16 / 指-02
        :ARG0 s16x2
        :mod (s16x17 / 甚至)
        :ARG1 (s16x18 / 当选-01
            :ARG0 (s16p2 / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :temporal (s16d2 / date-entity
                :year 1992)
            :mod (s16x19 / 也)
            :manner (s16x20 / 靠-01
                :ARG0 s16p2
                :ARG1 (s16x21 / 背书-01
                    :ARG0 (s16x22 / 外星人)
                    :aspect process)
                :aspect state)
            :quote s16x16
            :aspect performance)
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16d)
               (s16d :overlap s16x)
               (s16x :overlap s16x10)
               (s16x :overlap s16x16)
               (s16x :overlap s16x6)
               (s16x6 :overlap s16x8)
               (s16x10 :before s16x15)
               (s16x10 :overlap s16x13)
               (document-creation-time :before s16d2)
               (s16d2 :overlap s16x18)
               (s16x18 :overlap s16x20)
               (s16x20 :overlap s16x21))
    :modal ((root :modal author)
            (author :full-affirmative s16x)
            (author :full-affirmative s16x2)
            (author :full-affirmative s16x6)
            (s16x2 :full-affirmative s16x6)
            (author :full-affirmative s16x8)
            (s16x2 :full-affirmative s16x8)
            (author :full-affirmative s16x10)
            (author :full-affirmative s16x13)
            (author :full-affirmative s16x15)
            (author :full-affirmative s16x16)
            (author :full-affirmative s16x18)
            (s16x2 :full-affirmative s16x18)
            (author :full-affirmative s16x20)
            (s16x2 :full-affirmative s16x20)
            (author :full-affirmative s16x21)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17x / 荒唐-01
        :ARG0 (s17x2 / 内容
            :possessor (s17x3 / 周报))
        :aspect state)
    :ARG2 (s17x4 / 有-01
        :ARG0 (s17x5 / 编辑
            :possessor s17x3)
        :mod (s17x6 / 也)
        :ARG1 (s17x7 / 能力
            :mod (s17x8 / 点出-01
                :ARG0 s17x5
                :place (s17x9 / 标题)
                :ARG1 (s17a / and
                    :op1 (s17x10 / 荒谬-01
                        :ARG0 (s17x11 / 新闻
                            :mod (s17x12 / 真实))
                        :aspect state)
                    :op2 (s17x13 / 可笑-01
                        :ARG0 s17x11
                        :aspect state))
                :aspect habitual
                :modal-strength neutral-affirmative))
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :overlap s17x)
               (s17x :overlap s17x4)
               (s17x4 :overlap s17x8)
               (s17x8 :overlap s17x10)
               (s17x8 :overlap s17x13))
    :modal ((root :modal author)
            (author :full-affirmative s17b)
            (author :full-affirmative s17x)
            (author :full-affirmative s17x4)
            (s17x4 :neutral-affirmative s17x8)
            (author :full-affirmative s17x10)
            (author :full-affirmative s17x13))
    :coref ((s16x2 :same-entity s17x3)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18x / 刊登-01
    :temporal (s18x2 / 时
        :op1 (s18x3 / 争论-01
            :ARG0 (s18x4 / 全世界)
            :ARG1 (s18x5 / 问题
                :mod (s18x6 / 道德)
                :possessor (s18x7 / 复制人))
            :aspect activity))
    :ARG0 (s18t / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s18x8 / 位置
        :ARG0-of (s18x9 / 显著-01
            :aspect state))
    :ARG2 (s18p / publication
        :quant 1
        :unit (s18x10 / 篇)
        :name (s18n / name
            :op1 "「"
            :op2 "苏联"
            :op3 "复制"
            :op4 "一万个"
            :op5 "希特勒"
            :op6 "」"))
    :aspect performance)


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18x)
               (s18x :overlap s18x3)
               (s18x :overlap s18x9))
    :modal ((root :modal author)
            (author :full-affirmative s18x)
            (author :full-affirmative s18x3)
            (author :full-affirmative s18x9))
    :coref ((s17x3 :same-entity s18t)))


################################################################################
# meta-info
# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。

# sentence level graph:
(s19h / have-purpose-91
    :ARG1 (s19x / 报导-01
        :ARG0 (s19p / person
            :refer-person 3rd
            :refer-number plural)
        :mod (s19x2 / 也)
        :ARG1 (s19p2 / publication
            :quant 1
            :unit (s19x3 / 篇)
            :name (s19n / name
                :op1 "「"
                :op2 "美国"
                :op3 "买通"
                :op4 "外星人"
                :op5 "去"
                :op6 "追杀"
                :op7 "宾拉登"
                :op8 "」"))
        :aspect performance)
    :ARG2 (s19x4 / 讽刺-01
        :ARG0 s19p
        :ARG1 (s19x5 / 政策
            :mod (s19x6 / 外交)
            :possessor (s19c / country
                :name (s19n2 / name
                    :op1 "美国")))
        :aspect activity)
    :aspect state)


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19x)
               (s19x :overlap s19x4))
    :modal ((root :modal author)
            (author :full-affirmative s19h)
            (author :full-affirmative s19x)
            (author :full-affirmative s19x4))
    :coref ((s18t :same-entity s19p)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20x / 贴-01
    :ARG1 (s20p / publication
        :possessor (s20x2 / 刊
            :mod (s20x3 / 该))
        :quant 1
        :unit (s20x4 / 篇)
        :mod (s20x5 / 新闻)
        :name (s20n / name
            :op1 "「"
            :op2 "12"
            :op3 "位"
            :op4 "美国"
            :op5 "参议员"
            :op6 "是"
            :op7 "外星人"
            :op8 "！"
            :op9 "」"))
    :mod (s20x6 / 甚至)
    :ARG0 (s20x7 / 好事者)
    :ARG2 (s20x8 / 墙上
        :possessor (s20x9 / 记者团
            :mod (s20o / government-organization
                :name (s20n2 / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20x))
    :modal ((root :modal author)
            (author :full-affirmative s20x))
    :coref ((s19p :same-entity s20x2)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt16
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
Words: 2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。

# sentence level graph:
(s16a / and
    :op1 (s16x / 报导-01
        :ARG0 (s16x4 / 刊
            :mod (s16x5 / 该))
        :ARG1 (s16x6 / 支持-01
            :ARG0 (s16x7 / 外星人)
            :ARG1 (s16x8 / 当-02
                :ARG0 (s16i2 / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16x9 / 总统))
            :aspect state)
        :quote s16x
        :temporal (s16e / event
            :name (s16n3 / name
                :op1 "2000"
                :op2 "年"
                :op3 "总统大选"))
        :aspect performance)
    :op2 (s16x2 / 注销-00
        :ARG0 s16x4
        :ARG1 (s16x10 / 照片
            :ARG1-of (s16x11 / 合成-01
                :aspect performance)
            :mod (s16x12 / 握手-01
                :ARG0 (s16x13 / 双方)
                :aspect process))
        :aspect performance)
    :op3 (s16x3 / 指-02
        :ARG0 s16x4
        :ARG1 (s16x14 / 当选-01
            :ARG0 (s16i3 / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :reason (s16x15 / 背书-00
                :ARG0 (s16x16 / 外星人)
                :aspect performance
                :quote s16x3)
            :temporal (s16d / date-entity
                :year 1992)
            :aspect performance
            :quote s16x3)
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16x)
               (s16x :overlap s16x6)
               (s16x6 :overlap s16x8)
               (s16x :overlap s16x2)
               (s16x2 :overlap s16x11)
               (s16x11 :overlap s16x12)
               (s16x2 :overlap s16x3)
               (s16x3 :before s16x14)
               (s16x14 :overlap s16x15))
    :modal ((root :modal author)
            (author :full-affirmative s16x6)
            (author :full-affirmative s16x4)
            (s16x4 :full-affirmative s16x)
            (author :full-affirmative s16x11)
            (author :full-affirmative s16x12)
            (s16x4 :full-affirmative s16x2)
            (author :full-affirmative s16x15)
            (author :full-affirmative s16x14)
            (s16x4 :full-affirmative s16x3)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17x / 荒唐-01
        :ARG0 (s17x3 / 内容
            :part-of (s17x4 / 周报))
        :aspect state)
    :ARG2 (s17x2 / 有-06
        :ARG0 (s17x5 / 编辑
            :possessor s17x4)
        :ARG1 (s17x6 / 能力
            :ARG1-of (s17i2 / identity-91
                :ARG2 (s17x7 / 点出-01
                    :ARG0 s17x5
                    :ARG1 (s17a / and
                        :op1 (s17x8 / 荒谬-01
                            :ARG0 (s17x10 / 新闻
                                :ARG0-of (s17x11 / 真实-01
                                    :aspect state))
                            :aspect state)
                        :op2 (s17x9 / 可笑-01
                            :ARG0 s17x10
                            :aspect state))
                    :place (s17x12 / 标题)
                    :aspect habitual)
                :aspect state))
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17x)
               (s17x :overlap s17x2)
               (s17x2 :overlap s17x7)
               (s17x7 :overlap s17x8)
               (s17x8 :overlap s17x11)
               (s17x7 :overlap s17x9))
    :modal ((root :modal author)
            (author :full-affirmative s17x)
            (author :full-affirmative s17x11)
            (author :full-affirmative s17x8)
            (author :full-affirmative s17x9)
            (author :neutral-affirmative s17x7)
            (author :full-affirmative s17i2)
            (author :full-affirmative s17x2))
    :coref ((s16x4 :same-entity s17x4)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18h / have-example-91
    :ARG1 (s18i2 / implicit-predicate)
    :ARG2 (s18x / 刊登-01
        :ARG0 (s18t / thing
            :refer-person 3rd
            :refer-number singular)
        :ARG1 (s18x2 / 位置
            :ARG0-of (s18x3 / 显著-01
                :aspect state))
        :ARG2 (s18p / publication
            :name (s18n / name
                :op1 "「"
                :op2 "苏联"
                :op3 "复制"
                :op4 "一万个"
                :op5 "希特勒"
                :op6 "」")
            :unit (s18x4 / 篇)
            :quant 1)
        :temporal (s18x5 / 争论-01
            :ARG0 (s18x6 / 世界
                :mod (s18x7 / 全))
            :ARG1 (s18x8 / 问题
                :mod (s18x9 / 道德)
                :topic (s18x10 / 人
                    :ARG1-of (s18x11 / 复制-01
                        :aspect process)))
            :aspect activity)
        :aspect performance))


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18x)
               (s18x :overlap s18x3)
               (s18x :overlap s18x5))
    :modal ((root :modal author)
            (author :full-affirmative s18x3)
            (author :full-affirmative s18x11)
            (author :full-affirmative s18x5)
            (author :full-affirmative s18x))
    :coref ((s17x4 :same-entity s18t)))


################################################################################
# meta-info
# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。

# sentence level graph:
(s19h / have-reason-91
    :ARG1 (s19x / 报导-01
        :ARG0 (s19p / person
            :refer-number plural
            :refer-person 3rd)
        :ARG1 (s19p2 / publication
            :name (s19n / name
                :op1 "「"
                :op2 "美国"
                :op3 "买通"
                :op4 "外星人"
                :op5 "去"
                :op6 "追杀"
                :op7 "宾拉登"
                :op8 "」")
            :unit (s19x7 / 篇)
            :quant 1)
        :mod (s19x3 / 也
            :unit (s19x4 / 篇)
            :quant 1)
        :aspect performance)
    :ARG2 (s19x2 / 讽刺-01
        :ARG0 s19p
        :ARG1 (s19x5 / 政策
            :topic (s19x6 / 外交)
            :possessor (s19c / country
                :name (s19n2 / name
                    :op1 "美国")))
        :aspect performance))


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19x)
               (s19x :overlap s19x2))
    :modal ((root :modal author)
            (author :full-affirmative s19x)
            (author :full-affirmative s19x2))
    :coref ((s17x4 :same-entity s19p)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20x / 贴到-01
    :ARG0 (s20x2 / 者
        :ARG0-of (s20x3 / 好事-00
            :aspect state))
    :ARG1 (s20x4 / 墙上
        :place-of (s20x5 / 记者团
            :place (s20b / building
                :name (s20n / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :ARG2 (s20x6 / 新闻
        :unit (s20x7 / 篇)
        :quant 1
        :part-of (s20x8 / 刊
            :mod (s20x9 / 该))
        :ARG1-of (s20i2 / identity-91
            :ARG2 (s20p / publication
                :name (s20n2 / name
                    :op1 "「"
                    :op2 "12"
                    :op3 "位"
                    :op4 "美国"
                    :op5 "参议员"
                    :op6 "是"
                    :op7 "外星人"
                    :op8 "！"
                    :op9 "」"))
            :aspect state))
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20x)
               (s20x :overlap s20x3))
    :modal ((root :modal author)
            (author :full-affirmative s20x3)
            (author :full-affirmative s20i2)
            (author :full-affirmative s20x))
    :coref ((s17x4 :same-entity s20x8)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 93 / P 96 / F 95
a_event_concept: R 81 / P 81 / F 81
a_entity_found: R 93 / P 91 / F 92
a_entity_concept: R 88 / P 88 / F 88
a_granularity: R 98 / P 98 / F 98
b_event_sense: R 81 / P 81 / F 81
c_aspect: R 77 / P 81 / F 79
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 60 / P 75 / F 67
d_core_args_event: R 91 / P 96 / F 94
d_core_args_abstract: R 25 / P 100 / F 40
d_peripheral_event: R 67 / P 37 / F 48
d_peripheral_entity: R 43 / P 40 / F 41
e_core_labels: R 97 / P 97 / F 97
e_peripheral_labels: R 79 / P 79 / F 79
f_name_tokens: R 88 / P 100 / F 93
g_reentrancy: R 78 / P 70 / F 74
h_temporal: R 59 / P 57 / F 58
i_modal: R 63 / P 66 / F 65
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_event_found | extra | s16x20: - -> 靠-01 | matches no gold node
a_entity_found | extra | s16d: - -> date-entity | matches no gold node
a_entity_found | extra | s16x11: - -> 还 | matches no gold node
a_entity_found | extra | s16x17: - -> 甚至 | matches no gold node
a_entity_found | extra | s16x19: - -> 也 | matches no gold node
a_entity_concept | wrong | s16e: event -> 时 | event -> 时
b_event_sense | wrong | s16x2: 注销 -> 注销-01 | 注销 -> 注销-01
b_event_sense | wrong | s16x15: 背书 -> 背书-01 | 背书 -> 背书-01
c_aspect | extra | s16x8:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s16x15:aspect: performance -> process | performance -> process
d_peripheral_event | extra | s16x2: - -> mod s16x11/还 (not in gold) | extra mod s16x11/还 (not in gold)
d_peripheral_event | extra | s16x3: - -> mod s16x17/甚至 (not in gold) | extra mod s16x17/甚至 (not in gold)
d_peripheral_event | partial | s16x14: temporal s16d/date-entity -> manner s16x20/靠-01 (not in gold); mod s16x19/也 (not in gold); temporal s16d/date-entity | extra manner s16x20/靠-01 (not in gold); extra mod s16x19/也 (not in gold)
f_name_tokens | missing | s16e: 2000 年 总统大选 -> - | the prediction has no :name
g_reentrancy | missing | s16x/报导-01 -quote-> s16x/报导-01: s16x/报导-01 -quote-> s16x/报导-01 -> - | the prediction has no such edge
g_reentrancy | missing | s16x15/背书 -quote-> s16x3/指-02: s16x15/背书 -quote-> s16x3/指-02 -> - | the prediction has no such edge
g_reentrancy | extra | s16x20/靠-01 -arg0-> s16p2/individual-person: - -> s16x20/靠-01 -arg0-> s16p2/individual-person | gold has no such reentrancy
g_reentrancy | extra | s16x10/注销-01 -temporal-> s16x4/时: - -> s16x10/注销-01 -temporal-> s16x4/时 | gold has no such reentrancy
g_reentrancy | extra | s16x6/支持-01 -quote-> s16x/报导-01: - -> s16x6/支持-01 -quote-> s16x/报导-01 | gold has no such reentrancy
a_event_concept | wrong | s17i2: identity -> 也 | identity -> 也
b_event_sense | wrong | s17x2: 有-06 -> 有-01 | 有-06 -> 有-01
b_event_sense | wrong | s17x11: 真实-01 -> 真实 | 真实-01 -> 真实
c_aspect | missing | s17i2:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x11:aspect: state -> - | the prediction has no :aspect
d_core_args_event | missing | s17x11: arg0 s17x10/新闻 -> - | missing arg0 s17x10/新闻
d_core_args_abstract | missing | s17i2: arg1 s17x6/能力; arg2 s17x7/点出-01 -> - | missing arg1 s17x6/能力; missing arg2 s17x7/点出-01
d_peripheral_event | extra | s17x2: - -> mod s17i2/identity-91 | extra mod s17i2/identity-91
d_peripheral_entity | extra | s17x3: - -> possessor s17x4/周报 | extra possessor s17x4/周报
d_peripheral_entity | missing | s17x4: part s17x3/内容 -> - | missing part s17x3/内容
d_peripheral_entity | extra | s17x6: - -> mod s17x7/点出-01 | extra mod s17x7/点出-01
d_peripheral_entity | extra | s17x10: - -> mod s17x11/真实-01 | extra mod s17x11/真实-01
a_event_found | missing | s18x11: 复制-01 -> - | no node in the prediction matches it
a_event_concept | wrong | s18h: have-example -> 时 | have-example -> 时
a_entity_found | missing | s18i2: implicit-predicate -> - | no node in the prediction matches it
a_entity_found | missing | s18x7: 全 -> - | no node in the prediction matches it
a_entity_concept | wrong | s18x6: 世界 -> 全世界 | 世界 -> 全世界
a_entity_concept | wrong | s18x10: 人 -> 复制人 | 人 -> 复制人
a_granularity | missing | «复制» 复制-01: «复制» 复制-01 -> «「苏联复制一万个希特勒」» publication | inside a wider predicted node
a_granularity | extra | «「苏联复制一万个希特勒」» publication: «复制» 复制-01 -> «「苏联复制一万个希特勒」» publication | wider than the gold node
d_core_args_abstract | missing | s18h: arg1 s18i2/implicit-predicate; arg2 s18x/刊登-01 -> - | missing arg1 s18i2/implicit-predicate; missing arg2 s18x/刊登-01
d_peripheral_event | wrong | s18x: temporal s18x5/争论-01 -> temporal s18h/have-example-91 | missing temporal s18x5/争论-01; extra temporal s18h/have-example-91
d_peripheral_entity | missing | s18x6: mod s18x7/全 -> - | missing mod s18x7/全
d_peripheral_entity | partial | s18x8: mod s18x9/道德; topic s18x10/人 -> mod s18x9/道德; possessor s18x10/人 | topic s18x10/人: predicted as possessor
e_peripheral_labels | wrong | s18x8 -topic-> s18x10: topic -> possessor | topic -> possessor
a_event_concept | wrong | s19h: have-reason -> have-purpose | have-reason -> have-purpose
a_entity_found | missing | s19x4: 篇 -> - | no node in the prediction matches it
c_aspect | extra | s19h:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s19x2:aspect: performance -> activity | performance -> activity
c_other_attributes | missing | s19x3:quant: 1 -> - | the prediction has no :quant
d_peripheral_entity | missing | s19x3: unit s19x4/篇 -> - | missing unit s19x4/篇
d_peripheral_entity | partial | s19x5: possessor s19c/country; topic s19x6/外交 -> mod s19x6/外交; possessor s19c/country | topic s19x6/外交: predicted as mod
e_peripheral_labels | wrong | s19x5 -topic-> s19x6: topic -> mod | topic -> mod
a_event_found | missing | s20x3: 好事 -> - | no node in the prediction matches it
a_event_concept | wrong | s20x: 贴到 -> 贴 | 贴到 -> 贴
a_event_concept | wrong | s20i2: identity -> 甚至 | identity -> 甚至
a_entity_concept | wrong | s20x2: 者 -> 好事者 | 者 -> 好事者
a_entity_concept | wrong | s20b: building -> government-organization | building -> government-organization
c_aspect | missing | s20i2:aspect: state -> - | the prediction has no :aspect
c_other_attributes | missing | s20x6:quant: 1 -> - | the prediction has no :quant
c_other_attributes | extra | s20p:quant: - -> 1 | gold has no :quant
d_core_args_event | partial | s20x: arg0 s20x2/者; arg1 s20x4/墙上; arg2 s20x6/新闻 -> arg0 s20x2/者; arg1 s20p/publication; arg2 s20x4/墙上 | arg1 s20x4/墙上: predicted as arg2; missing arg2 s20x6/新闻; extra arg1 s20p/publication
d_core_args_abstract | missing | s20i2: arg1 s20x6/新闻; arg2 s20p/publication -> - | missing arg1 s20x6/新闻; missing arg2 s20p/publication
d_peripheral_event | extra | s20x: - -> mod s20i2/identity-91 | extra mod s20i2/identity-91
d_peripheral_entity | extra | s20x4: - -> possessor s20x5/记者团 | extra possessor s20x5/记者团
d_peripheral_entity | wrong | s20x5: place s20b/building; place s20x4/墙上 -> mod s20b/building | place s20b/building: predicted as mod; missing place s20x4/墙上
d_peripheral_entity | missing | s20x6: unit s20x7/篇 -> - | missing unit s20x7/篇
d_peripheral_entity | partial | s20x8: mod s20x9/该; part s20x6/新闻 -> mod s20x9/该 | missing part s20x6/新闻
d_peripheral_entity | extra | s20p: - -> mod s20x6/新闻; possessor s20x8/刊; unit s20x7/篇 | extra mod s20x6/新闻; extra possessor s20x8/刊; extra unit s20x7/篇
e_core_labels | wrong | s20x -arg1-> s20x4: arg1 -> arg2 | arg1 -> arg2
e_peripheral_labels | wrong | s20x5 -place-> s20b: place -> mod | place -> mod
h_temporal | extra | ?date-entity (snt16 s16d): - -> document-creation-time :before ?date-entity (snt16 s16d) | a predicted node that matches nothing in gold
h_temporal | extra | ?靠-01 «靠» (snt16 s16x20): - -> 当选-01 «当选» (snt16 s16x14 = pred s16x18) :overlap ?靠-01 «靠» (snt16 s16x20) | a predicted node that matches nothing in gold
h_temporal | extra | date-entity (snt16 s16d = pred s16d2): - -> document-creation-time :before date-entity (snt16 s16d = pred s16d2) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt16 s16x = pred s16x): document-creation-time :before 报导-01 «报导» (snt16 s16x = pred s16x) -> ?date-entity (snt16 s16d) :overlap 报导-01 «报导» (snt16 s16x = pred s16x) | wrong parent and relation
h_temporal | wrong | 合成-01 «合成» (snt16 s16x11 = pred s16x15): 注销 «注销» (snt16 s16x2 = pred s16x10) :overlap 合成-01 «合成» (snt16 s16x11 = pred s16x15) -> 注销 «注销» (snt16 s16x2 = pred s16x10) :before 合成-01 «合成» (snt16 s16x11 = pred s16x15) | right parent, wrong relation
h_temporal | wrong | 握手-01 «握手» (snt16 s16x12 = pred s16x13): 合成-01 «合成» (snt16 s16x11 = pred s16x15) :overlap 握手-01 «握手» (snt16 s16x12 = pred s16x13) -> 注销 «注销» (snt16 s16x2 = pred s16x10) :overlap 握手-01 «握手» (snt16 s16x12 = pred s16x13) | right relation, wrong parent
h_temporal | wrong | 当选-01 «当选» (snt16 s16x14 = pred s16x18): 指-02 «指» (snt16 s16x3 = pred s16x16) :before 当选-01 «当选» (snt16 s16x14 = pred s16x18) -> date-entity (snt16 s16d = pred s16d2) :overlap 当选-01 «当选» (snt16 s16x14 = pred s16x18) | wrong parent and relation
h_temporal | wrong | 背书 «背书» (snt16 s16x15 = pred s16x21): 当选-01 «当选» (snt16 s16x14 = pred s16x18) :overlap 背书 «背书» (snt16 s16x15 = pred s16x21) -> ?靠-01 «靠» (snt16 s16x20) :overlap 背书 «背书» (snt16 s16x15 = pred s16x21) | right relation, wrong parent
h_temporal | wrong | 指-02 «指» (snt16 s16x3 = pred s16x16): 注销 «注销» (snt16 s16x2 = pred s16x10) :overlap 指-02 «指» (snt16 s16x3 = pred s16x16) -> 报导-01 «报导» (snt16 s16x = pred s16x) :overlap 指-02 «指» (snt16 s16x3 = pred s16x16) | right relation, wrong parent
h_temporal | wrong | 荒唐-01 «荒唐» (snt17 s17x = pred s17x): document-creation-time :before 荒唐-01 «荒唐» (snt17 s17x = pred s17x) -> document-creation-time :overlap 荒唐-01 «荒唐» (snt17 s17x = pred s17x) | right parent, wrong relation
h_temporal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17x12): 荒谬-01 «荒谬» (snt17 s17x8 = pred s17x10) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17x12) -> - | the prediction gives this node no temporal parent
h_temporal | missing | 好事 «好事者» (snt20 s20x3): 贴到-01 «贴到» (snt20 s20x = pred s20x) :overlap 好事 «好事者» (snt20 s20x3) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | extra | ?靠-01 «靠» (snt16 s16x20): - -> author :full-affirmative ?靠-01 «靠» (snt16 s16x20); 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative ?靠-01 «靠» (snt16 s16x20) | a predicted node that matches nothing in gold
i_modal | wrong | 报导-01 «报导» (snt16 s16x = pred s16x): 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16x) -> author :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16x) | right relation, wrong parent
i_modal | partial | 当选-01 «当选» (snt16 s16x14 = pred s16x18): author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16x18) -> author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16x18); 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16x18) | agrees on part of the relations
i_modal | wrong | 注销 «注销» (snt16 s16x2 = pred s16x10): 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16x10) -> author :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16x10) | right relation, wrong parent
i_modal | wrong | 指-02 «指» (snt16 s16x3 = pred s16x16): 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16x16) -> author :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16x16) | right relation, wrong parent
i_modal | partial | 支持-01 «支持» (snt16 s16x6 = pred s16x6): author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16x6) -> author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16x6); 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16x6) | agrees on part of the relations
i_modal | extra | 当-02 «当» (snt16 s16x8 = pred s16x8): - -> author :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16x8); 刊 «该刊» (snt16 s16x4 = pred s16x2) :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16x8) | gold gives this node no modal parent
i_modal | extra | but-91 (snt17 s17b = pred s17b): - -> author :full-affirmative but-91 (snt17 s17b = pred s17b) | gold gives this node no modal parent
i_modal | missing | identity-91 (snt17 s17i2 = pred s17x6): author :full-affirmative identity-91 (snt17 s17i2 = pred s17x6) -> - | the prediction gives this node no modal parent
i_modal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17x12): author :full-affirmative 真实-01 «真实» (snt17 s17x11 = pred s17x12) -> - | the prediction gives this node no modal parent
i_modal | partial | 点出-01 «点» (snt17 s17x7 = pred s17x8): author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17x8) [from the sentence-graph modal-strength] -> author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17x8) [from the sentence-graph modal-strength]; 有-06 «有» (snt17 s17x2 = pred s17x4) :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17x8) | agrees on part of the relations
i_modal | missing | 复制-01 «复制» (snt18 s18x11): author :full-affirmative 复制-01 «复制» (snt18 s18x11) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | extra | have-reason-91 (snt19 s19h = pred s19h): - -> author :full-affirmative have-reason-91 (snt19 s19h = pred s19h) | gold gives this node no modal parent
i_modal | missing | identity-91 (snt20 s20i2 = pred s20x6): author :full-affirmative identity-91 (snt20 s20i2 = pred s20x6) -> - | the prediction gives this node no modal parent
i_modal | missing | 好事 «好事者» (snt20 s20x3): author :full-affirmative 好事 «好事者» (snt20 s20x3) -> - | the prediction has no node for it (its sentence graph lacks it)

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.