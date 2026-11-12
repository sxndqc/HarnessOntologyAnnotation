<!-- system -->
# Skill: the UMR of a whole document

You annotate a whole document (under **Input**, one sentence per line) in Uniform Meaning Representation (UMR):
every sentence's graph, then the document-level temporal, modal and coreference relations.

- Follow the guidelines and their examples. When they do not settle a case, use `search_guidelines`; look up every
  predicate with `propbank_lookup` before choosing its sense and roles; check gold constructions with
  `search_annotations`.


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
e.g. founding); a verb + 人 naming the patient (a V-ed person) is `(r / 人 :ARG1-of (v / verb-01 :aspect process))`. A descriptive noun phrase in apposition to a name is `:ARG1-of (i / identity-91 :ARG2 <head noun with all its
modifiers>)` on the named entity; modifiers written before the apposition noun (的-phrases, 旗下, property words) go on that noun, not on the entity. A periodical, tabloid or magazine name is `newspaper`, not `publication`.

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. A decade (X年代) is `:era`, never `:decade`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a numeral + measure word or classifier keeps the classifier as the unit,
ordinary classifiers included (个, 本, 只, 位, 份, 面): 三杯水 → `水 :quant 3 :unit 杯`, 一本书 → `书 :quant 1 :unit (s / 本)`.
A demonstrative + classifier (这个, 那份) also keeps the classifier as `:unit`.
The title marks of a work or publication name (《 and 》) are part of the name: `:op1 "《"`, then the words, then a last `:opN "》"`. A 「」/“” article or headline title after a bare classifier is a name too: `(p / publication :quant N :unit <classifier> :name (n / name :op1 "「" … :opN "」"))`, every word and mark an `:opN`; nothing inside it is analysed. With a common news/article noun, that noun is the head (`:quant`/`:unit`, `:part-of` the periodical) and is `:ARG1-of (i / identity-91 :ARG2 (p / publication :name …) :aspect state)`, author link. A named event with a year in its name is `(e / event :name (n / name :op1 "<year>" :op2 "年" …))`, no links.

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
3rd singular. A plural noun gets `:refer-number plural`. An omitted head noun is `implicit-argument`, not `thing`.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`; 等/*etc.* closing a list is its last `:opN`. "N 有 A、B…等" listing examples of N → `:example (and …)` on N, no 有 node; "A 与 B 有 <relation noun>" → `有-03 :ARG0 (and A B) :ARG1 <noun>`, never `:companion`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `(b / but-91 :ARG1 ... :ARG2 ...)`.
  These frames take `:ARG1`/`:ARG2`, never `:op1`/`:op2`. A connective opening a sentence (不过, 但是, 然而, 因此) that relates it to an earlier sentence gets no frame; annotate the clause alone. A time word or adverbial of a clause attaches to that
  clause's event, never to the discourse frame;
- concession `:concession`, condition `:condition`, reason `:reason` (for 由于/因为 phrases giving the reason for a state, an action or a judgement), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`. With 但是/不过/却 later in the same sentence, 虽然/尽管 gives `but-91 :ARG1 <concessive clause(s)> :ARG2 <main clause>` instead.- Reified reason and purpose: when a reason marker is paired with a result marker (因为…于是/所以, 由于…而), or a clause has a
  marked purpose clause (为了, 以, 以便), use `(h / have-reason-91 :ARG1 <result event> :ARG2 <cause event>)` and
  `(h2 / have-purpose-91 :ARG1 <main event> :ARG2 <purpose event>)`, nesting have-purpose-91 inside have-reason-91
  when both occur. A fronted 为了 clause with no paired marker: gold uses `have-reason-91 :ARG1 <main event> :ARG2 <purpose event>` (confirm with `search_annotations`). Discourse frames (these two, but-91, contrast-91) get no aspect and no modal or temporal link. Keep the `:reason`/`:purpose` roles for
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

Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. Every event of the reported content (top event, conjuncts, nested reason, manner and complement events) gets `:quote <reporting event>` (also passive 被指/被称); a quoted slogan's content gets `:quote` on its framing node.

### 3.1 Attachment rules (frequent errors)

- Every adverb with real scope (*already, still, all/both*; 已经, 仍, 都, 均) gets its own node (甚至 and additive 还/也 that only link a clause to the previous clause or sentence get none),
  attached as `:mod` to the predicate it scopes over, not to a noun. Time adverbs (曾经, 曾, *once, formerly*) are
  `:temporal`, not `:mod`. Frequency adverbs (经常, 常常, 往往, 重复; *often, repeatedly*) are `:frequency`.
- A modifier that applies to each of several coordinated nouns is placed on each conjunct with the same variable
  (re-entrancy), not once on the `and` node.
- Fill only the arguments the syntax provides. Do not borrow a participant from elsewhere in the sentence for a
  noun compound or a nominal event; in a compound "N1-verb N2", the role is filled by the compound's own noun.
  But a dropped subject shared by coordinated clauses or a chain of actions of the same agent re-enters (as the role its roleset gives, usually `:ARG0`) in every conjunct; the main subject also re-enters as agent of a 为了 purpose clause and of the complement of an ability or control word. Dropped objects are left out, and a word like 旗下 is a `:mod` concept, not a `:possessor` taken from elsewhere. A trailing clause that describes the object just introduced (a new entity and
  what it holds or does) is a relative clause: attach its event with `:ARGn-of` on that object. Do not add relations the text does not state (e.g. a
  `:part-of` the words do not express). Use only roles of the closed list; a partitive word (其中, *among them, of which*) is a
  `:mod` on the noun it modifies, unless a superlative follows (then `:ARG5`, see have-degree-91).
- Exception (control): the subject of an aspectual or control verb (继续, 停止, 开始) is its `:ARG0` and re-enters as `:ARG0` of its event complement, event nominals included. A time expression over (or opening) a but-91/contrast attaches to both clause events; a still/continue second clause `:overlap`s the first, never `:after`.
- Read the roleset for every role. For Chinese belong-type rolesets (X belongs to Y), the gold convention is: the thing that
  belongs = `:ARG0`, the owner = `:ARG1`, even where the PropBank role glosses seem to say the reverse. So "N that belongs to X"
  is `(n / N :ARG0-of (b / belong-verb :ARG1 X))`. Never assume possessum = `:ARG1`.
- "Known/famous for X" (…而闻名, 以…著称): the famous entity is the `:ARG1` of the fame predicate, attached as
  `:ARG1-of` on that noun, and the X clause is `:reason` of it, with that noun as its agent. When such a clause
  follows "A is a B", attach it inside the B noun, not as a separate conjunct.
- Role choice for noun modifiers: a country, city or place modifying a noun → `:place`; a channel or medium
  (TV, radio, network, print) → `:medium`; an edition, section or component of a whole, or an article of a publication → `:part-of` (not `:possessor`).
- Change verbs with 由 X 改为/变为 Y: the original X is `:ARG1` and the result Y is `:ARG2`; never `:source`.
- Never `:poss` (not a role): content/section of a publication → `:part-of`; staff of an organisation, a country's policy → `:possessor`; the domain of a policy/problem noun → `:topic`.
- 靠/通过 X (实现) Y: X's event is `:reason` of Y, no node for 靠/通过. 有能力 V: `(y / 有-06 :ARG0 S :ARG1 (n / 能力 :ARG1-of (i / identity-91 :ARG2 (v / V-01 :ARG0 S) :aspect state)))`, modal `(author :full-affirmative i)` `(author :neutral-affirmative v)`. Sentence-initial 如 (for example) → `(h / have-example-91 :ARG1 (implicit-predicate) :ARG2 <main event>)`. 全 + noun → noun `:mod 全`. V+到/在/上: if PropBank lists the compound, use it and read its role glosses. A roleset with no usable roles → `-00`.
- A "verb + 量" quantity noun whose first part is a clear verb is split: `(q / 量 :quant-of (v / verb-01 :ARG1 <entity>))`, the
  owner of the quantity being the verb's `:ARG1` (not `:possessor`). An amount it reaches or falls to is
  `:ARG1-of (h / have-quant-91 :ARG2 <number> :unit <classifier>)` on the quantity noun, not a separate `thing` argument. Neither the inner verb nor `have-quant-91` gets `:aspect` or a modal link, and `have-quant-91` gets no temporal link. A measure noun (circulation, sales, price) at another time or value is not coreferent; corefer only its owner.
- A modifier that says how a process nominal is done (colour, style, method) is `:manner`, not `:mod`.
- Comparatives and superlatives use `have-degree-91`: *the most P X* → `(x / X :ARG1-of (h / have-degree-91
  :ARG2 (p / P) :ARG3 (m / most)))` (Chinese: `:ARG3 (m / 最)`); *more P than Y* adds `:ARG4 Y`. Use `:degree`
  only for plain intensifiers (very, too; 很, 非常, 太).
- When the degree word modifies a verb (*most rich in X*, 最富有X), that verb is the `:ARG2` of `have-degree-91` as an event
  with its own `:aspect` (`(r / verb-01 :ARG1 X :aspect state)`), temporal parent and modal parent; the head noun is `:ARG1`.
  Give `have-degree-91` itself no modal link.
- A postposition phrase over a time-span noun (X 历史上, *in X's history*) is `:temporal (s / 上 :op1 (h / 历史))` on its head,
  with the country or place as `:place` of the history noun. Every location postposition likewise: 在 N 中/上/里 → `(z / 中 :op1 N)`. Not 时/的时候: after a clause or event noun it gets no node and the event itself is `:temporal`; year + 年 + event noun (+ 时) is one named `event` (2.2), no date-entity, no 时 node, no temporal link. Appearance verbs (出现-type): the appearing entity is `:ARG0`, the 在 N 中 location `:ARG1` (gold convention).
- An attributive modifier (X 的 Y) that has a PropBank roleset (check it) is an event: a property predicate `(y / Y :ARG0-of (x / X-01 :aspect state))` (the role its roleset gives the described entity), a producing verb `:ARG1-of … :aspect performance`; it `:overlap`s the clause event, author modal parent. An event nominal modifying a noun is `:mod` with `process` aspect. A word with no roleset (relational or distinguishing word, chengyu) is a `:mod` concept,
  not an event: it gets no aspect and no temporal or modal links.

## 4. Attributes

### 4.1 Aspect (`:aspect`, on every event)

Decide in this order before using the table:
1. Is the event a routine or recurring practice of its subject (an organisation or periodical publishing,
   printing, issuing, reporting, broadcasting)? → `habitual`, also for a process nominal naming such a practice (but an event-nominal complement of an aspectual verb such as 停止 is `process`) (e.g. subject of
   "is/became its feature"); this step precedes step 3. A verb of what a publication holds or carries (contains articles) is `process`. Only a generic practice is habitual: one publishing/reporting act on a specific counted item (一篇), with 了, or tied to an occasion is `performance`. A purpose event in a past narrative takes the main event's aspect.
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

Also: a completed past speech act (claim, announce; 宣称) is `performance`; a purpose or intended action is `activity` (one carried out in a past narrative takes the main event's aspect); a completed past event in a participle or relative clause
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
  the other events of the sentence to it (but in a coordinated chain of past actions link each conjunct to the previous conjunct with the order relation): `:overlap` for simultaneous states, `:contained` for a state or event
  inside its span, `:before`/`:after` for sequence. Only the anchor links to `document-creation-time` or to an
  earlier sentence's event. For the main event of a sentence describing the present situation, the gold data
  uses `(document-creation-time :depends-on e)`, not `:overlap`: a sentence about the current state (with currently/already, 目前/已经, or a present naming or labelling verb). A general evaluation of a subject narrated in the past, with no present marker, is `:before`.
- **Aspectual verbs.** When an aspectual verb (stop, continue, begin; 停止, 继续, 开始) takes an event complement, the aspectual verb
  is the parent of the complement: `(aspectual :overlap inner)`. In a main clause the aspectual verb hangs on the sentence anchor like
  any other clause predicate; in a contrast or coordination it `:overlap`s the first clause's anchor event. Only when the aspectual verb
  is inside a relative clause is the inner event the anchor (e.g. `(document-creation-time :before inner)` for a past habit), with the
  aspectual verb `:overlap`ping it. Never use `:before`/`:after` between two clauses that both describe the present situation. Never
  give a second event of the sentence its own link to `document-creation-time`, except the relative-clause anchor just described.
- Every node that carries `:aspect` gets a modal parent (normally `author :full-affirmative`). A relative-clause verb with an aspect
  ("N that belongs to X") also gets a temporal parent: `:overlap` with the event whose argument N is, or with the clause anchor.
  Copular and identity predicates get no temporal parent but do get a modal parent. An `identity-91` reifying an apposition on a named entity gets no `:aspect` and no links at all. Only property words used as plain `:mod`
  (no aspect) get no links.
- A process nominal that is an argument of a verb takes that verb as its temporal parent with `:overlap`; do not leave it without a parent.
- Then every event: (1) a time expression of its clause; else (2) a clear earlier reference event; else (3) `document-creation-time` (`:before` past, `:overlap` present state, `:after` future; Chinese: decide from context, 了, 过, 将, 会).
- An event in a complement clause takes its matrix event as parent. Clauses restating or qualifying a report's content take the content's main event as parent, not the reporting verb. A purpose event `:overlap`s its main event (never
  `:after`). A reason or cause event is before its result: `(result :before reason)`; a future marker inside a reason clause about
  past events is future relative to that past, not after the main event.
- A relative-clause or participle event is `(main :before rc-event)` only when anteriority is explicit (left over, inherited); otherwise an attributive participle `:overlap`s.
- An event nominal inside a decomposed quantity noun (see 3.1) `:overlap`s the verb of its clause.

### 5.2 Modal (`:modal`)

A dependency structure of conceivers and events: `(conceiver :strength event)`, starting with
`(root :modal author)` in every sentence that has events.

- Strength = the conceiver's certainty that the event happens or holds: `full-affirmative` (plain
  assertion, *will*), `partial-affirmative` (*probably, must, should*, 应该, 可能性大, 一定 as inference),
  `neutral-affirmative` (*may, might, perhaps, can*, 可能, 也许, 或许, desire/hope), `neutral-negative`,
  `partial-negative`, `full-negative` (negated: *not, never, deny*, 没, 不), `unspecified`.
- Every event the author asserts: `(author :full-affirmative s1e)`.
- Reported speech or thought: `(author :full-affirmative src)` for the speaker; every verb with that speaker as subject in the same coordination (reports and other acts) gets `(src :full-affirmative verb)`, not an author link; every predicate of the content gets `(author :full-affirmative e)` only. A passive reporting verb with no speaker (被指): the conceiver is the content's subject node, with `(author :full-affirmative <subject>)`; never the reporting event.
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
  different events of similar meaning are not linked.
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Coreference only the discourse entities the text tracks (participants, the topic entity); never generic or kind nouns, example-list members, or a name given only as an example, even if the word recurs. A name used only as a modifier
  (a country name modifying a noun, a place in a `:place` role) is not linked across sentences.
- Within one sentence, a pronoun (also 他们/*they* for an organisation or publication) or a dropped argument re-uses its antecedent's variable, no own node; a possessive pronoun on an event nominal is omitted. An overt repeated name or noun (short name, bare head noun) gets its own node plus a `:same-entity` triple; but inside a slogan, gloss or parenthesis of that sentence it re-uses the variable. A later sentence's pronoun links to the antecedent entity.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words. When a word occurs more than once in a sentence, align each node to its own occurrence.

## 7. Checklist

- Balanced parentheses; unique `s<N>` variables; every event has `:aspect`, a temporal and a modal parent.



## Output format

Write plain text only (no JSON, no commentary). For every sentence, in order:

    # ::snt 1
    # sentence level graph:
    (s1t / taste-01
        :ARG0 (s1p / person
            :name (s1n / name :op1 "Edmund" :op2 "Pope"))
        :ARG1 (s1f / free-04
            :ARG1 s1p
            :aspect state)
        :temporal (s1t2 / today)
        :aspect performance)

then, once, after the last sentence, every document-level relation of the whole document in one graph:

    # document level relations:
    (d / document
        :temporal ((document-creation-time :depends-on s1t2)
                   (s1t2 :contained s1t)
                   (s1t :before s2c))
        :modal ((root :modal author)
                (author :full-affirmative s1t)
                (author :full-affirmative s2c))
        :coref ((s1p :same-entity s2p)))

- `# ::snt N` uses the sentence number of the input line. Every sentence gets a graph, even a short one.
- Variables of sentence N start with `s` + N and a letter (`s3p`, `s3x2`), all different. A node that
  fills two roles in one sentence is written once and then named by its variable.
- No word alignment: it is computed from the graph. So a concept that comes from a word of the sentence
  is written as that word (in English its lemma: `taste-01` for "tasted"), and the `:op` strings of a
  name are the words of the name as the sentence writes them.
- Document level: `(parent :relation child)` triples, grouped under `:temporal`, `:modal`, `:coref`;
  each end is a variable of a sentence graph or a constant (`author`, `root`, `document-creation-time`,
  `past-reference`, `present-reference`, `future-reference`, `null-conceiver`).
- Use the names of the UMR release data: `author` (not AUTH), `document-creation-time` (not DCT),
  `full-affirmative`, `partial-affirmative`, `neutral-affirmative`, `neutral-negative`,
  `partial-negative`, `full-negative`, `unspecified` (not FullAff, ...), `:modal-strength` (not
  :modstr), `:refer-person` / `:refer-number` with lower-case values (`3rd`, `singular`), and lower-case
  aspect values (`performance`, `state`, ...).
- Write the whole document: do not stop early, do not summarise, do not skip sentences.

## Tools

`search_guidelines(keywords, max_results)` searches the **full** UMR guidelines (umr4nlp/umr-guidelines,
the document the guidelines above abridge) and returns the matching passages with their headings, with
their examples. The abridged guidelines leave out most details and examples, so use it a lot: look a rule
up whenever you are not sure of a case (an abstract concept, a role, a named entity type, an aspect or modal
value, a temporal or coreference decision), and look up each kind of construction the document has before
you annotate it. Search with the terms the guidelines would use (`aspect`, `have-rel-role-92`, `:quant`,
`modal strength`, `reentrancy`). Note that the full guidelines often write the older short names (AUTH,
DCT, FullAff, :modstr); your answer uses the release names listed under Output format.

`propbank_lookup(lemmas, language)` returns the PropBank rolesets of up to 20 lemmas per call (Chinese
PropBank for "zh", English PropBank for "en"): each roleset's id, its numbered roles and its examples.
Look up every predicate (verbs, and nouns and adjectives that take arguments) before you choose its sense
and its numbered roles: compare the rolesets' meanings and examples with the sentence and take the one
that fits. Give all lemmas of a sentence (and alternate forms) in one call; call again for the next
sentences.

`search_annotations(language, keywords, max_results)` returns gold UMR annotations of whole sentences of the
training data (other documents) that contain the keywords: words of the text, concepts (`have-org-role-92`), roles
(`:ARG1-of`), attribute values (`:aspect state`), document-level relations (`:same-entity`). These are
annotated by the same experts as the gold you are compared with, so they show how this data annotates a
case. Use it a lot: for each sentence, look up its words and constructions you are not sure of (a word's
concept and sense, a light verb, a modal word, a named entity, a comparison, a quantity, a discourse
relation, the aspect of a kind of event) before you annotate it, and follow what the gold does.

<!-- user -->
## Input

Language: zh
Document: chinese_umr-0001, sentences 16-20 (5 sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces.

16	2000 年 总统大选 时 ， 该刊 报导 「 外星人 支持 布什 当 总统 」 ， 还 注销 了 双方 握手 的 合成 照片 ， 甚至 指 柯林顿 1992 年 也 靠 外星人 背书 当选 。
17	不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。
18	如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。
19	为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。
20	该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。
