<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29497). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

# The current instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.

**Make the annotation as correct as you can**: it is compared node by node and relation by relation with an expert gold annotation. Read the guidelines first, follow their examples, and check each graph (concepts, aspect, role direction) and the document-level relations before going on.

## Guidelines

# UMR guidelines, abridged

UMR 0.9, abridged, for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data.

## 1. What a UMR is

A UMR has two levels.

- **Sentence level**: one rooted, directed graph per sentence in PENMAN notation, adapted from AMR:
  concepts (events, entities, abstract concepts), the relations between them (participant roles and
  non-participant roles) and attributes (aspect, polarity, mode, quantity, person and number, degree).
- **Document level**: three kinds of relations between the nodes of the sentence graphs, across sentences:
  **temporal** dependencies, **modal** dependencies, and **coreference**.

**Variables.** Every node of sentence N has a variable starting with `s` + N (`s3d`, `s3p`), all
different within the document. A node that fills two roles is written once and then referred to by its
variable (re-entrancy: `:ARG0 s3p` above). Write the full node (name, appositive, `:part-of`) at the entity's first mention in word order, even inside a subordinate clause below the root; every later pronoun or unexpressed mention, also inside a relative clause, is a re-entrancy (a repeat with its own noun: see 5.3).

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
- past-time adverbs (*once, formerly*; 曾, 曾经) are `:temporal` (in the graph only; they get no temporal triple, see 5.1);
- a partitive like 其中 (*among them*) is `:mod` on the noun, but in a superlative it is the `:ARG5` comparison set;
- frequency adverbs (重复, 反复, 经常) are `:frequency`;
- a locative postposition after a time or period noun (X 时, X 中, X 以来, X 上 as in *in the history of ...*) is a `:temporal` node for the postposition with the noun as `:op1`, attached to the word it scopes over (often the head noun).

**Concept names.** An English event is its PropBank roleset (`deny-01`, `look-up-05`). A Chinese event is the
Chinese word as written with its Chinese PropBank sense (`拥有-01`, `执行-01`); a Chinese predicate that is not
in PropBank is `<word>-00`. Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :name (n / name :op1 "Russia"))`: an entity-type concept and `:name` with one `:opN` per word of the name.

- Do not write `:wiki`.
- A named human is `individual-person`, not `person`. `person` stays for pronouns and unnamed people.
- The middle dot `·` in a transliterated foreign name is its own `:op`.
- For a titled work in title brackets 《 》, the brackets are their own first and last `:op`s.
- Choose the most specific type the name's head word or the context shows:
  - `newspaper` for a paper or weekly (报, 日报, 周报, tabloid);
  - `magazine` for 杂志 / 期刊;
  - `book`, `program`, etc. for other kinds of work;
  - `publication` only when the kind is unknown.
- A country or place name modifying a common noun (X 的历史, an X company) is `:place`, not `:mod`.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Types as in AMR (`country`, `city`, `organization`, `company`, ...). A celestial body is `planet`/`star` + `:name`. Any named being, also a fictional character or alien, is `individual-person`; a descriptor word written as part of the name is an `:op`.

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. A decade expression (X年代) is written with `:era` and the year number only (`:era 1980`), not `:decade` and not the written string. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a numeral + classifier or measure word gives `:quant N` plus `:unit <classifier>` on the noun, for real measure words and ordinary classifiers (个, 本, 份, 位) alike, and also when the number is 1 (一个X → `X :quant 1 :unit 个`).

**Measure compounds.** A Chinese noun made of a verb + 量 / 率 / 额 (the quantity, rate or amount of V-ing) is split. The measure morpheme is the head, `(q / 量 :quant-of (e / V-01 :ARG1 ...))`. The inner verb gets no `:aspect` and no modal triple; it keeps only its temporal `:overlap` with the governing verb, and its own arguments (the owner, etc.) attach to the verb, not as `:possessor`. **Amounts reached.** In a clause where a measured noun reaches, falls to or amounts to a number (达到 N, 跌至 N, 为 N), the verb stays the event.
- It uses its own frame (or the bare verb's frame). It is the root when it is the main verb, with `:aspect performance` for a completed change.
- The measured noun is its theme, usually `:ARG0` (check the frame).
- The number goes on the measured noun as `(q :ARG1-of (h / have-quant-91 :ARG2 N :unit (u / <classifier>)))`. This `have-quant-91` gets no `:aspect`, no temporal parent and no modal parent.
- Time expressions and adverbs (已经, 也) attach to the verb.
- Never drop the verb, and never make `have-quant-91` the root. Do not create a separate `thing :quant N`.

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
A compound agent noun (V + 人/者, e.g. a founder or initiator) is decomposed: `(p / 人 :ARG0-of (v / V-01 :aspect performance))`, placed where the role noun goes (e.g. under `:ARG3` of the role predicate).

Use an abstract predicate only when there is no lexical predicate. A Chinese verb with its own PropBank frame keeps that frame and its roles. For example, a possession or belonging verb such as 属于 or 拥有 is that verb with its own fitting sense (see Chinese role numbering below), not `belong-91` / `have-91`. Do not use `:degree` on a property verb for a superlative; use `have-degree-91`. Its `:ARG2` is the property word itself. If the property is a verb with its own object (*rich in X, full of X*, 富X, 充满X), keep that verb as an event with its object (`(r / V-01 :ARG1 X :aspect state)`) and put it under `:ARG2`; do not drop the verb or put the object noun there. A superlative with no head noun (最大 + classifier) is `(i / implicit-argument :unit <classifier> :ARG1-of (h / have-degree-91 ...))`. Use `:ARG5` only for an explicit comparison set (*among N, of all N*, 在…中); a scope like *in history* is a `:temporal` postposition node (2.1), not `:ARG5`.

**Chinese role numbering (required lookup).** For every Chinese predicate:
1. Look it up as the whole segmented token. A two-character verb (also a V是 token like 算是) is not cut down to its first character. Use a shorter form or `-00` only if the whole token has no frame. If a verb + complement token (V至, V到, V为, V成) has no frame, use the bare verb's frame; the endpoint fills that frame's end-point role (or comes through `have-quant-91`, 2.2). Never use a concept whose word is not a PropBank lemma unless it is `-00`.
2. List all of its senses with their role descriptions. Do not stop at -01.
3. Choose the sense whose role descriptions match the participants in the sentence.
4. Copy the role numbers from that sense, not from -01 and not from English habit.

The belonging/membership sense of a verb is often not -01, and in it the owner is often `:ARG0` and the thing that belongs is `:ARG1`. A relative clause *the Y that belongs to X* then is `(y / Y :ARG0-of (b / V-0n :ARG1 x))` or `:ARG1-of`, whichever the frame gives the head noun; the owner fills the frame's owner role. Many Chinese intransitive and change-of-state verbs have only `:ARG0` (the thing that ceases, changes or acts). Do not default the theme to `:ARG1` by English habit. In particular, for change, become, reach and fall verbs (成, 达到, 跌, 变 type), the theme is usually `:ARG0` and the result or point reached is `:ARG1`. Copy the numbers from the roleset's role list every time. If the roleset lists only `:ARG0`, the single participant is `:ARG0` even when it looks like a patient (it starts, ceases, is founded, appears).

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. Do not add nodes for Chinese zero subjects or objects or for other unexpressed participants: leave the role out.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91`; a sentence-initial connective whose first conjunct is in an earlier sentence gets no node and no modal triple (the main verb is the root);
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为) → `:cause` (phrasal); 由于 and the frame 以…而 → `:reason` (phrasal); *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession` only when the main clause has no adversative word; when it is answered by 但/但是/不过/却, use `(b / but-91 :ARG1 concessive :ARG2 main)` (a further clause added to the concessive part makes `:ARG1` an `and`).
- A sequence adverb linking two clauses (后来, 然后, 接着) → `(c / consecutive :op1 first :op2 later)` (or `after`/`before`); the adverb and an additive 还 with it get no node. Focus particles 就, 便 get no node.
- A clause in parentheses restating or exemplifying the previous one is a conjunct under `and`.
- 以 X 为 目的/目标/宗旨 is copular: keep the noun, `(i / identity-91 :ARG1 (m / 目的 :purpose-of E) :ARG2 X :aspect state)`; a quantifier (大部分) is `:mod` on E.
- N 有 A、B…等 where N is a topic, content or category noun listing its members: no 有/`have-91` node; N fills its outer role and takes `:example (a / and :op1 A ... :opk 等)`. 等 / *etc.* closing a list is always its last `:opN`, not `:mod`.
- **Clause-linking reason and purpose (overrides the phrasal rules above).** When a reason connective (因为…于是/所以, 由于…, 所以) or a purpose connective (为/为了 + a clause) links two full clauses, reify it: `(h / have-reason-91 :ARG1 effect-event :ARG2 cause-event :aspect state)`, `(h2 / have-purpose-91 :ARG1 main-event :ARG2 purpose-event :aspect state)`. The reified node is the root, or sits above the main event. It gets `(author :full-affirmative h)` but no temporal parent (see 5.1). Keep `:cause` / `:reason` / `:purpose` only when the cause or purpose is a phrase, not a full clause.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span.

A compound made of two coordinated nouns (AB where A and B are parallel nouns, e.g. a four-character N1N2 meaning *N1 and N2*) is split: `(a / and :op1 N1 :op2 N2)`. A true idiom stays one concept. A compound of a free head noun + modifier (母公司 type) is split: `head :mod modifier`. When such a parallel-noun pair is one item of a longer list, nest it as its own `and` inside the outer `and`.

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
- **Unexpressed participants.** Do not fill a roleset slot with a participant the text does not express. Re-enter a node only when the text itself expresses that participant in that role. The same holds for non-core relations (`:part-of`, `:possessor`, `:mod`, ...): add one only when a word or construction expresses it, not when it is merely implied. A subject grammatically shared through a control or means frame (以 X 而 Y, *known for doing X*, *try to X*) counts as expressed: re-enter it as the subject of the embedded verb too. Do not re-enter the subject into 为/为了-purpose clauses or into relative clauses; leave those roles out unless a word fills them.
- **Aspectual verb in a relative clause.** When a head noun is modified by an aspectual verb plus another verb (*the X that stopped/began doing Y*), the noun is an argument of the inner verb only: `(x / X :ARG1-of (p / V-01 :ARG1-of (s / stop-01)))`. It is not an argument of the aspectual verb as well. Check the aspectual verb's roleset.
- **Shared modifiers.** A modifier shared by coordinated nouns (*various A and B*) goes on each conjunct by re-entrancy, not on the `and` node. Do not add `:subset` there.
- **Describing clauses.** A clause that goes on describing the predicate noun of a copular sentence (*X is a Y, known for Z*) attaches under that noun, e.g. as `:ARG1-of`. It is not a separate top-level conjunct.
- **Trailing content clauses.** The same holds for a trailing clause without 为/为了 that tells what an object just created, named or described contains or does (…，容纳 Y). It attaches under that object (the creation verb's own argument, not its `:part-of` whole) as `:ARGn-of` with `:aspect process`. It is not `:purpose`, and it gets no re-entered subject.
- **Parts and media.** A physical edition or part of a publication is `:part-of` it, not `:possessor`. A medium noun (TV, 网络) modifying a program or product is `:medium`.
- **Heads.** In N1 的 N2, and in *change from A to B* (从 A 变为 B), the grammatical head common noun is the concept. A publication or organization name modifying it is `:part-of` (a part, section or edition of it) or `:possessor`, not the head.
- **Formats and parts as arguments.** When a format, layout or section noun (版面, edition, section) of a publication is an argument of any verb, that noun is the argument and the publication is its `:part-of`. Never write the inverse `:part` on the whole. This holds even when the publication's name is the grammatical head after 的 (V了 A的《X》 → `:ARG1 (a / A :part-of x)`).
- **Change from A to B.** In 从/由 A 变为/改为 B, A is the frame's 'thing changed' role (`:ARG1`), not `:source`; B is `:ARG2`.
- **Appositives.** An appositive descriptor before or after a name (its 旗下 tabloid 《X》) is `(x / <type> :name ... :ARG1-of (i / identity-91 :ARG2 (d / <descriptor> :mod ...)))`. Words like 旗下 stay a `:mod` node on the descriptor; do not turn them into a `:possessor` edge.
- **Role nouns with names.** A role, title or agent noun directly before or after a person's name is not an appositive `identity-91`. It is `(p / individual-person :name ... :ARG1-of (h / have-org-role-91 :ARG3 role))`, where role is e.g. `(r / 人 :ARG0-of (v / V-01))`. In Chinese documents write the role predicates as `have-org-role-91` / `have-rel-role-91`; spouse and kin titles (夫人, wife) use `have-rel-role-91`, and a modifying country is `:place` on the role noun. Use appositive `identity-91` only for non-role descriptors (e.g. of a publication).
- **Nested abstract predicates.** An abstract predicate that only modifies a noun gets no `:aspect` and no temporal or modal triple. This covers role reifications, an appositive `identity-91` and `have-quant-91`.

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


Further aspect rules:
- **Repeated activity of an institution or periodical** (publishing, broadcasting, reporting, what it regularly contains or covers) is `habitual`, even with 了 or other completion marking.
- **already + an aspectual stop verb governing another event** (已经停止 doing X) describing the current situation is `state`. A lexical termination verb with no governed event (a publication ceased, an organization dissolved) is `performance`, even with 已经.
- **Abstract predicates:** `identity-91` gets `:aspect state` only when it is the clause predicate (nested ones get none); `have-degree-91` gets no `:aspect` (the event under its `:ARG2` does).
- **A naming or evaluation passive** (*is called / is regarded as*, 被称为, 被誉为) is `performance`.
- **A negated event with a nominal event object** (没有经过X) is `process`.
- **Purpose verbs** naming an ongoing use are `activity`. A relative-clause verb giving what something is for or contains is `process`. A manner or property word on an event nominal is `:manner`, not `:mod`. Example: a periodical printed in some colour or format → `(y / 印刷-01 :manner (c / <colour word>) :aspect habitual)`.
- **Stative verbs, continued.** Possession, belonging, existence and knowing verbs stay `state` even with 了, 过, 曾经 or a duration modifier. These markers only place the state in time for the temporal triples.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2). Exception: when the negation is fused into one verb word (未经 type), write no `:polarity -`. The concept is the verb part without the negator, with its own PropBank sense and roles. Do not create a `-00` concept spelled with the negator. Mark only `full-negative` at the document level.
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
- Time expressions first: a past absolute date (*1998*) is `(document-creation-time :before date)` (a future one `:after`); a relative one (*today, yesterday*,
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`; a vague past or future one on `past-reference` / `future-reference`. A vague present adverb (*currently, nowadays*, 现在, 目前) gets no temporal triple of its own.
- Then pick **one anchor per sentence**: the matrix (main) event. Only the anchor is linked to the outside: (1) to a time expression (date, era) of its clause, if there is one: `(s1t :overlap s1e)`, never `:contains`; else (2) to an event of an earlier sentence, only when the text marks the sequence (then, thereupon, 于是, 也 continuing the story): `(s2c :before s3a)`; an independent past event is not linked to a similar earlier event; else (3) to
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- Every other event of the sentence takes the anchor, or the event or entity-modifying event it depends on, as its parent. Use `:overlap` unless the order is explicit (`:before`/`:after`). A purpose clause is `:overlap` its main event. A cause clause, and a relative clause describing an earlier event (left over, previously ...), is `:before` its parent, even when it is marked future (将) relative to its own time. This covers:
  - subordinate, complement, coordinated and cause/reason clauses;
  - relative-clause verbs and event nominals;
  - negated events;
  - events inside noun-phrase modifiers.
  Do not give these their own `document-creation-time` link.
- Past-time adverbs (*once, formerly*, 曾, 曾经) are not reference times: give them no triple and link their event directly, `(document-creation-time :before e)`.
- A naming or evaluation passive (被称为, 被誉为) whose result describes the present is linked as `(document-creation-time :depends-on e)`. Use this only for naming and evaluation. A narrative change (成了, became) that continues an earlier sentence's story takes that earlier event as its reference time with `:overlap` (`:after` only with an explicit later-sequence word).
- An aspectual verb (*stop, begin, continue*) and the event it governs are `:overlap`, never `:before`/`:after`.
- Every event node must get exactly one temporal parent. Exceptions (also: `have-reason-91` and `have-purpose-91` get no temporal parent, but their argument events do):
  - `identity-91` is left out of the temporal structure but still gets its modal parent. When a sentence's root is `identity-91`, choose as anchor the event inside the predicate noun that is most clearly placed in time, usually a completed past event (`(document-creation-time :before e)`). The triples are:
- `(document-creation-time :before anchor)`;
- for a reputation or property state of that noun, `(state :contained anchor)`. The state is the parent and the anchor is the child; the state itself gets no other temporal parent;
- every other event of the predicate noun, including the means or reason of the reputation, is `(anchor :overlap e)`. None of them hang under the reputation state.
  - `have-degree-91` gets no temporal parent and no modal parent. The event under its `:ARG2` does get them.

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
  constants `purpose` and `have-condition` as parents of their events. A purpose event that the text shows is actually realized is `(author :full-affirmative e)`.
- In the sentence graph, write the strength of an event that is not `full-affirmative` from the author as
  `:modal-strength <value>` too (the scorers move it to the document level).

### 5.3 Coreference (`:coref`)

- `(earlier :same-entity later)`: two mentions of the same entity — a pronoun and its antecedent, a repeated
  name, a definite description. Link each mention to its closest earlier mention, earlier one first;
  link entity nodes, never `name` nodes.
- `(earlier :same-event later)`: two mentions of the very same event (the same act mentioned again, same arguments in the same roles; not a retelling with another object or agent, or a part instead of the whole). Do not link two different events that are merely related (e.g. a thing's founding and a later act by its founder).
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Link every mention of the main discourse entities. Do not build chains for incidental place names or other entities that occur only as modifiers (`:place`, `:mod`) in different sentences.
- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Balanced parentheses; each variable defined once, starting with `s<N>`.
- Every event has `:aspect`, a temporal and a modal parent (exceptions above); Chinese predicates use their own roleset's sense and roles.
- No `:coref` pair of two mere `:place`/`:mod` modifiers or generic mentions.


</instruction>

# The critique (training batch 3: chinese_umr-0001, sentences 11-15; AnCast++ comprehensive 77.4)
<critique>
# Review of the annotation of document sentences 11–15: error patterns and changes to the instruction

The annotator found every event (event found 100, event concept 100) and got person/number attributes and the document format right. Most points were lost on the document-level checks: coreference (F 11), temporal (F 54), modal (F 70), and on re-entrancy (F 44). Below, the patterns are ordered by cost, most costly first.

## 1. A plural pronoun that stands for an organization or publication became a new `person` node
**Cost:** about 13 units.
- Coreference (j): 6 units. The whole chain for the publication broke.
- Re-entrancy (g): 2 units.
- Entity found (a): 1 extra unit.
- Core arguments of events (d): 1 extra argument.
- Modal (i): 3 units, partly.

**What happened.** A plural pronoun ("they / their") referred to a periodical named earlier in the same sentence.
- The annotator made a fresh `person 3rd plural` node, attached it as an extra `:ARG0` and `:possessor`, and chained the next sentence's pronoun to that new node.
- Gold re-enters the publication's node within the sentence. Across sentences, gold links the next sentence's `person` node to the publication with `:same-entity`.
- Gold also leaves out the agent of an event noun inside a reported clause when no word expresses it.

**Why.** Section 2.4 says every pronoun is `person`/`thing`. Nothing says that a pronoun whose antecedent is an organization or publication in the same sentence is a re-entrancy of that node.

**Change.** Add to 2.4 and 5.3:
- "A pronoun (also a plural *they / 他们*) whose antecedent is an organization, company or publication is that entity. In the same sentence, re-enter its variable; create no `person` node. In a later sentence, write the `person` node and link it `(organization :same-entity person)`, never to another pronoun node."
- Add: "The possessive pronoun of an event noun does not by itself add an `:ARG0`, unless it is the only way the agent is expressed."

## 2. Reported content was not marked with `:quote`, and its modal conceiver was wrong
**Cost:** about 12 units.
- Re-entrancy (g): 4 units for missing `:quote` edges.
- Modal (i): about 6 units.
- Temporal parents (h): 2 units, linked to this.

**What happened.**
- Gold puts `:quote <reporting event>` on the top content event under a verb of claiming, and on events in a quoted slogan. For a slogan, the quoted event points to the `identity-91` that introduces it.
- Gold gives the events of the clause that the claim contrasts with a second parent: the claimant as conceiver as well as the author.
- In a passive allegation (被指), gold does not use the reporting verb as conceiver.

**Why.** Section 3 mentions `:quote` only as something "the release data also marks". So the annotator treated it as optional and wrote none.

**Change.**
- Make it a rule: "Every content event of a verb of saying, claiming, alleging or labelling (also a quoted slogan) gets `:quote <the reporting event or the predicate that introduces the quotation>`. Put it on the top content event and on each conjunct."
- For the modal side: "Content of a claim gets `(speaker :full-affirmative e)`. When the speaker is an organization, the organization node is the conceiver. Never use the reporting verb itself as conceiver when the speaker is an expressed entity."

## 3. Temporal parents were chosen wrongly in coordinated and reported structures
**Cost:** about 11 temporal units (h F 54).

**What happened.**
- **Coordinated root.** When the root is an `and` of two clauses, gold anchors the **first conjunct** to `document-creation-time` and makes the second conjunct `:overlap` the first. The annotator anchored on the second conjunct.
- **Claims with contrasting clauses.** Under a verb of claiming, gold makes the claimed event the parent of the other events in the sentence that describe the same activity. Gold gives the `have-mod-91` content predicate no temporal parent. The annotator hung everything on the claiming verb and gave `have-mod-91` a parent.
- **Nodes gold leaves out.** The annotator gave temporal parents to a relative-clause verb inside a created object, using `:after` with no explicit order word. It also gave a temporal parent and a modal parent to an idiom used as a goal noun in 以…为目的.
- **Present tense in a past story.** The annotator read a generic "can be regarded as" evaluation, about a publication that had already ceased, as present (`:overlap` DCT). Gold has `:before`.

**Change.**
- "When the root is a coordination, the first conjunct is the anchor and the later conjuncts `:overlap` it, unless an order word says otherwise."
- "Under a verb of claiming, the claimed event is the reference time of the other descriptions of the same activity. Abstract content predicates (`have-mod-91` as claimed content) get no temporal parent."
- "Use `:after`/`:before` only with an explicit order word."
- "A concept that only names a goal or content (an idiom as the `:ARG2` of the 以…为目的 identity) is an entity: no aspect, no temporal or modal triple."
- "Statements about a publication or organization that the text has already said no longer exists are past (`:before` DCT), even when they are generic."

## 4. Frames, senses and core-role numbers did not follow the roleset
**Cost:** about 12 units.
- Event sense (b): 2 units.
- Core labels (e): 5 units.
- Core arguments of events and of abstract predicates (d): 3 units.

**What happened.**
- **算是.** Its roleset is `ARG0` = the thing described, `ARG1` = what it is considered as. The annotator used `ARG1`/`ARG2` from English habit.
- **出现.** The roleset has a location argument. The annotator put the 在…中 locative under `:place`. Gold puts it as a numbered argument (`:ARG1`).
- **指.** A passive "is alleged that" was given `指-01` (refer to) instead of `指-02` (claim).
- **有.** A relationship that two parties have was given `有-01` (ownership) instead of `有-03`.

**Why.** The instruction already has a required lookup. It was not followed for frames that are not -01, nor for passive verbs of saying.

**Change.** Add to the lookup rule:
- "Also check verbs of saying and alleging in the passive (the claim sense)."
- "Check 有 used for relations or existence (not possession)."
- "A locative phrase that a roleset lists as an argument is that numbered role, not `:place`."
- "A V是 verb's roleset starts at `ARG0`."

**Smaller point.** For a superlative with an implicit head, gold here numbered the property `:ARG1` and the degree word `:ARG2`. Other gold data uses `:ARG2`/`:ARG3`, as the instruction table does. Keep the table, but note this headless variant only as possible.

## 5. A comitative partner in a symmetric relation, and a descriptor written before a name
**Cost:** about 10 units.
- Entity concept (a): 2 units.
- Name tokens (f): 2 units.
- Other attributes (c): 4 units.
- Core labels (e): 1 unit.
- Coreference (j): 2 extra units.

**What happened.**
- In "X 与 Y 有 关系" (X has a relationship with Y), gold coordinates both parties, `:ARG0 (and :op1 X :op2 Y)`. The annotator used `:companion`.
- When a generic species or category noun stands before a name in a later mention, gold makes the noun the concept and the name only the rest. The annotator, following the instruction's rule that "a descriptor word written as part of the name is an `:op`", put the noun into the name.

**Change.**
- "For a reciprocal or symmetric relation (与/和/跟 Y 有关系, 合作, 结婚 type), both parties are the conjuncts of `and` in the first role; no `:companion`."
- Narrow the descriptor rule: "A common category noun before a name is the concept with `:name` for the rest. Write it as an `:op` only when it is fixed into the name itself."

## 6. A repeated short form of a name in the same sentence was re-entered
**Cost:** about 8 units.
- Entity concept (a): 1 unit; granularity (a): 2 units; peripheral roles (d): 2 units; coreference (j): 1 unit; re-entrancy (g): 1 unit.
- The missing node also shifted the alignment of an adverb.

**What happened.** A later mention used a shortened head noun of a name ("the weekly" after the full title). Gold makes it its own node, `:part-of` the thing it is part of, with a `:coref` triple inside the sentence.

**Why.** The instruction contradicts itself. Section 1 says "a repeat with its own noun: see 5.3", but 5.3 says "Within one sentence, coreference is a re-entrancy."

**Change.** "Pronouns and zero mentions within a sentence are re-entrancies. A repeated mention with its own noun (also a shortened name) is a new node and gets a `:same-entity` triple, even in the same sentence."

## 7. Aspectual and control verbs: missing shared arguments and wrong aspect
**Cost:** about 7 units.
- Re-entrancy (g): 3 units.
- Core arguments of events (d): 2 units.
- Aspect (c): 1 unit.

**What happened.**
- **Event noun under a stop verb.** For "stop the distribution of X", gold gives the event noun `:aspect process`. The annotator applied the institution "habitual" rule. Gold also re-enters the stopping subject as the event noun's `:ARG0`.
- **Continue verb.** In a main clause with a continue verb (继续), the subject is the continue verb's `:ARG0` (its roleset has an agent) and is re-entered as `:ARG0` of the inner verb.
- **Shared date.** A date that scopes over both clauses of a but-coordination is re-entered as `:temporal` on the second clause.

**Change.**
- "An event noun governed by an aspectual verb (stop/start/continue + nominal) is `process`. Its agent is the aspectual verb's subject, by re-entrancy."
- "In a main clause, the subject of 继续/开始/停止 + verb fills the aspectual verb's agent role and the inner verb's role."
- "A sentence-initial date shared by coordinated clauses is re-entered on each."
- Keep the relative-clause exception as a separate case.

## 8. Smaller issues
- **Modal triples on connectives** (2 units). Gold gives `but-91` / `contrast-91` / `and` no modal triple. State this in 5.2, and keep the exception for `have-reason-91` / `have-purpose-91`.
- **Coreference of generic nouns** (2 units). A bare kind or category noun repeated in two sentences was chained, and gold has no such chain. Extend the 5.3 ban on chains to "generic or kind nouns, and items of example lists".
- **Aspect of a single claim** (1 unit). A claim made by a periodical is a single speech act, `performance`. The "repeated activity of an institution → habitual" rule should cover only publishing, reporting and contents, not a claim about them.
- **Event noun in an example list.** It is treated as an entity (no `-01`, no aspect, no triples).
- **Aspect of a generic activity** (1 unit). A generic ongoing activity in an evaluation is `activity`, not `process`.

## What to keep
The following matched gold and should stay in the instruction:
- The `but-91` with an `and` `:ARG1` for 虽然…不过 (although … but).
- The identity rule for 以 X 为目的 (`目的 :purpose-of E`, with the quantifier as `:mod`).
- `:example (and … 等)` lists, with 等 as the last `:op`.
- Appositive `identity-91` for a parent company.
- The newspaper type and title brackets as `:op`s.
- Splitting the middle dot `·` into its own `:op`.
- `have-rel-role-91` with `:place` and `:mod` on the title noun.
- `planet` + `:name`.
- `consecutive` for a sequence adverb.
- The headless superlative written as `implicit-argument :unit`.
- `:frequency` for frequency adverbs.
- `:mod` for scope adverbs.
- The rule for anchoring a date (`(DCT :before date)`, `(date :overlap anchor)`).
- Full person and number attributes on pronouns.
</critique>

# Earlier edits
- batch 1, reflection 1 (15/15 edits applied): Temporal: one anchor per sentence, other events hang off it with :overlap, every event gets a parent, no depends-on for vague present adverbs, copular identity left out. Classifiers become :quant+:unit (also 1); adverbs are nodes. No implicit arguments. Attachment rules for aspectual-verb relatives, shared modifiers, describing clauses, part-of and medium. Aspect rules for habitual, already+stop a -> AnCast++ comp 78.4 on the batch, kept
- batch 1, reflection 2 (9/9 edits applied): Fix temporal anchoring (identity-91 root, aspectual verbs, past-time adverbs, result-now depends-on, have-degree-91 exception), superlative ARG2/ARG5 and 上 postposition, Chinese PropBank role numbering, attributes on identity-91/have-degree-91, shared-subject re-entrancy, fused negation, narrowed already+stop rule, nested and-pairs, coref checklist. -> AnCast++ comp 89.3 on the batch, kept
- batch 1, reflection 3 (7/7 edits applied): Fix misleading belonging-verb sense example and make PropBank frame lookup (whole token, all senses) mandatory; specify concept for fused negation; specific periodical entity types; explicit identity-91 temporal triples; stative verbs keep state aspect; no unexpressed non-core relations. -> AnCast++ comp 95.0 on the batch, kept
- batch 2, reflection 1 (18/18 edits applied): Reify clause-level reason/purpose (have-reason-91/have-purpose-91); split verb+量/率/额 compounds and use have-quant-91 for amounts reached; bare-verb frame for V至/V到 tokens; widen Chinese ARG0-theme warning; narrow shared-subject re-entrancy, head-noun/appositive/旗下 rules; individual-person, middle-dot op, agent nouns; fix temporal rules for absolute dates, purpose, cause/earlier relatives, depends- -> AnCast++ comp 77.9 on the batch, kept
- batch 2, reflection 2 (9/10 edits applied): Keep the reach/fall verb as root (ARG0 theme, performance) with have-quant-91 attribute-free; no sentence-initial one-arg but-91; measure-compound inner verb without aspect/modal; format/part noun as argument with publication :part-of, A in 由A改为B is ARG1; trailing contains-clauses as ARGn-of process; role noun with name -> role predicate (Chinese -91 names, per critique); nested abstract predicate -> AnCast++ comp 96.0 on the batch, kept
- batch 2, reflection 3 (10/10 edits applied): Define entities at first mention and re-enter later; part-of only (no inverse :part), for any part/format argument; enforce ARG0-only rolesets (checklist); no node for a connective linking to an earlier sentence; stricter :same-event; narrative change defaults to :overlap; trailing clause attaches to the creation verb's own argument. Trimmed intro/header text to stay under the limit. -> AnCast++ comp 98.1 on the batch, kept
- batch 3, reflection 1 (14/19 edits applied): Freed space (intro, §1 example, type list, checklist). Added: but-91 for 虽然…但; 以X为目的 as identity-91 with the noun; topic-list :example with 等 as last op; parenthetical clauses as and-conjuncts; consecutive for sequence adverbs, no node for 就/便; mandatory :quote, speaker as ARG0, saying-verb modal full-affirmative, hedged-copula complements author-affirmative; one-time claims performance; aspectual -> AnCast++ comp 77.4 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.