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
    :ARG1 (s11s / 停止-01
        :ARG0 (s11c / company
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司")
            :ARG1-of (s11i / identity-91
                :ARG2 (s11c2 / 公司
                    :mod (s11m / 母))))
        :ARG1 (s11f / 发行-01
            :ARG1 (s11x / newspaper
                :name (s11n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :aspect habitual)
        :temporal (s11d / date-entity
            :year 2007
            :month 7)
        :aspect performance)
    :ARG2 (s11j / 继续-01
        :ARG1 (s11v / 生存-01
            :ARG0 (s11w / 网络版
                :part-of s11x)
            :aspect state)
        :mod (s11r / 仍)
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11s)
               (s11s :overlap s11f)
               (s11s :overlap s11j)
               (s11j :overlap s11v))
    :modal ((root :modal author)
            (author :full-affirmative s11b)
            (author :full-affirmative s11s)
            (author :full-affirmative s11f)
            (author :full-affirmative s11j)
            (author :full-affirmative s11v)))


################################################################################
# meta-info
# :: snt12
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
Words: 虽然 《 世界 新闻 周报 》 宣称 他们 的 报导 都是 真实 的 （ 他们 的 标语 ： 「 只 报导 事实 ： 世界 新闻 周报 ！ 」 ） ， 不过 大部分 的 报导 都 以 博君一笑 为 目的 。

# sentence level graph:
(s12b / but-91
    :ARG1 (s12a / and
        :op1 (s12c / 宣称-01
            :ARG0 (s12x / newspaper
                :name (s12n / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :ARG1 (s12h / have-mod-91
                :ARG1 (s12r / 报导-01
                    :ARG0 (s12p / person
                        :refer-person 3rd
                        :refer-number plural)
                    :aspect habitual)
                :ARG2 (s12t / 真实)
                :mod (s12d / 都)
                :aspect state)
            :aspect habitual)
        :op2 (s12i / identity-91
            :ARG1 (s12g / 标语
                :possessor s12p)
            :ARG2 (s12r2 / 报导-01
                :ARG0 s12x
                :ARG1 (s12f / 事实)
                :mod (s12z / 只)
                :aspect habitual)
            :aspect state))
    :ARG2 (s12i2 / identity-91
        :ARG1 (s12m / 目的
            :purpose-of (s12r3 / 报导-01
                :mod (s12q / 大部分)
                :aspect habitual))
        :ARG2 (s12y / 博君一笑-00
            :aspect process)
        :mod (s12d2 / 都)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12c)
               (s12c :overlap s12h)
               (s12h :overlap s12r)
               (s12c :overlap s12r2)
               (s12c :overlap s12r3)
               (s12r3 :overlap s12y))
    :modal ((root :modal author)
            (author :full-affirmative s12b)
            (author :full-affirmative s12c)
            (author :full-affirmative s12x)
            (s12x :full-affirmative s12h)
            (s12x :full-affirmative s12r)
            (author :full-affirmative s12i)
            (author :full-affirmative s12r2)
            (author :full-affirmative s12i2)
            (author :full-affirmative s12r3)
            (author :full-affirmative s12y))
    :coref ((s11x :same-entity s12x)))


################################################################################
# meta-info
# :: snt13
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
Words: 他们 经常 报导 的 题材 有 外星人 、 古代 航天员 、 时间 旅行 、 大脚 、 欧帕兹 等 ， 他们 甚至 创造 出 一些 在 他们 的 新闻 中 重复 出现 的 虚拟 人物 如 蝙蝠 男孩 、 外星人 P ' Lod 等 。

# sentence level graph:
(s13a / and
    :op1 (s13t / 题材
        :ARG1-of (s13r / 报导-01
            :ARG0 (s13p / person
                :refer-person 3rd
                :refer-number plural)
            :frequency (s13f / 经常)
            :aspect habitual)
        :example (s13a2 / and
            :op1 (s13w / 外星人)
            :op2 (s13h / 航天员
                :mod (s13g / 古代))
            :op3 (s13l / 旅行-01
                :mod (s13s / 时间)
                :aspect process)
            :op4 (s13j / 大脚)
            :op5 (s13o2 / 欧帕兹)
            :op6 (s13e / 等)))
    :op2 (s13c / 创造-01
        :ARG0 s13p
        :ARG1 (s13k / 人物
            :mod (s13v / 虚拟)
            :quant (s13y / 一些)
            :ARG0-of (s13o / 出现-01
                :place (s13z / 中
                    :op1 (s13n / 新闻
                        :possessor s13p))
                :frequency (s13q / 重复)
                :aspect habitual)
            :example (s13a3 / and
                :op1 (s13i / individual-person
                    :name (s13n2 / name
                        :op1 "蝙蝠"
                        :op2 "男孩"))
                :op2 (s13i2 / individual-person
                    :name (s13n3 / name
                        :op1 "外星人"
                        :op2 "P"
                        :op3 "'"
                        :op4 "Lod"))
                :op3 (s13e2 / 等)))
        :mod (s13m / 甚至)
        :aspect performance))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13c)
               (s13c :overlap s13r)
               (s13r :overlap s13l)
               (s13c :after s13o))
    :modal ((root :modal author)
            (author :full-affirmative s13r)
            (author :full-affirmative s13l)
            (author :full-affirmative s13c)
            (author :full-affirmative s13o))
    :coref ((s12p :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14s / 算是-01
    :ARG1 (s14i / implicit-argument
        :unit (s14u / 宗)
        :ARG1-of (s14h2 / have-degree-91
            :ARG2 (s14d / 大)
            :ARG3 (s14z / 最)
            :ARG5 (s14q / 其中)))
    :ARG2 (s14h / 活动-01
        :ARG0 (s14w / 外星人)
        :place (s14p / planet
            :name (s14n / name
                :op1 "地球"))
        :aspect process)
    :modal-strength neutral-affirmative
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :overlap s14s)
               (s14s :overlap s14h))
    :modal ((root :modal author)
            (author :neutral-affirmative s14s)
            (author :full-affirmative s14h))
    :coref ((s13w :same-entity s14w)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15z / 指-01
    :ARG1 (s15c / consecutive
        :op1 (s15y / 有-01
            :ARG0 (s15i / individual-person
                :name (s15n / name
                    :op1 "希拉里"
                    :op2 "·"
                    :op3 "克林顿")
                :ARG1-of (s15r / have-rel-role-91
                    :ARG3 (s15f / 第一夫人
                        :place (s15k / country
                            :name (s15n2 / name
                                :op1 "美国"))
                        :mod (s15q / 前))))
            :ARG1 (s15g / 关系
                :mod (s15m / 暧昧))
            :companion (s15o / individual-person
                :name (s15n3 / name
                    :op1 "外星人"
                    :op2 "P"
                    :op3 "'"
                    :op4 "Lod"))
            :aspect state)
        :op2 (s15l / 领养-01
            :ARG0 s15i
            :ARG1 (s15b / 宝宝
                :mod (s15w / 外星))
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
    :coref ((s13i2 :same-entity s15o)))



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
a_event_found: R 100 / P 100 / F 100
a_event_concept: R 100 / P 100 / F 100
a_entity_found: R 100 / P 97 / F 98
a_entity_concept: R 95 / P 95 / F 95
a_granularity: R 93 / P 93 / F 93
b_event_sense: R 83 / P 83 / F 83
c_aspect: R 84 / P 84 / F 84
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 100 / P 33 / F 50
d_core_args_event: R 82 / P 73 / F 77
d_core_args_abstract: R 89 / P 89 / F 89
d_peripheral_event: R 93 / P 81 / F 87
d_peripheral_entity: R 90 / P 100 / F 95
e_core_labels: R 84 / P 84 / F 84
e_peripheral_labels: R 100 / P 100 / F 100
f_name_tokens: R 89 / P 89 / F 89
g_reentrancy: R 33 / P 67 / F 44
h_temporal: R 59 / P 50 / F 54
i_modal: R 75 / P 66 / F 70
j_coref_chain: R 17 / P 8 / F 11
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_concept | wrong | s11x5: 周报 -> 仍 | 周报 -> 仍
a_granularity | missing | «周报» 周报: «周报» 周报 -> «《世界新闻周报》» newspaper | inside a wider predicted node
a_granularity | extra | «美国媒体公司» company: «公司» 公司 -> «美国媒体公司» company | wider than the gold node
a_granularity | extra | «《世界新闻周报》» newspaper: «周报» 周报 -> «《世界新闻周报》» newspaper | wider than the gold node
c_aspect | wrong | s11x8:aspect: process -> habitual | process -> habitual
d_core_args_event | partial | s11x2: arg0 s11x4/网络版; arg1 s11x3/生存-01 -> arg1 s11x3/生存-01 | missing arg0 s11x4/网络版
d_core_args_event | extra | s11x3: - -> arg0 s11x4/网络版 | extra arg0 s11x4/网络版
d_peripheral_event | extra | s11x2: - -> mod s11x5/周报 | extra mod s11x5/周报
d_peripheral_entity | missing | s11x5: part s11x4/网络版 -> - | missing part s11x4/网络版
g_reentrancy | missing | s11x2/继续-01 -temporal-> s11d/date-entity: s11x2/继续-01 -temporal-> s11d/date-entity -> - | the prediction has no such edge
g_reentrancy | missing | s11x3/生存-01 -arg0-> s11x4/网络版: s11x3/生存-01 -arg0-> s11x4/网络版 -> - | the prediction has the edge but not as a reentrancy
g_reentrancy | missing | s11x8/发行-01 -arg0-> s11c/company: s11x8/发行-01 -arg0-> s11c/company -> - | the prediction has no such edge
g_reentrancy | extra | s11x/newspaper -part-> s11w/网络版: - -> s11x/newspaper -part-> s11w/网络版 | gold has no such reentrancy
a_entity_found | extra | s12p: - -> person | matches no gold node
a_entity_found | extra | s12d2: - -> 都 | matches no gold node
c_aspect | wrong | s12x:aspect: performance -> habitual | performance -> habitual
d_core_args_event | extra | s12x4: - -> arg0 s12p/person (not in gold) | extra arg0 s12p/person (not in gold)
g_reentrancy | missing | s12h/have-mod-91 -quote-> s12x/宣称-01: s12h/have-mod-91 -quote-> s12x/宣称-01 -> - | the prediction has no such edge
g_reentrancy | missing | s12x5/标语 -possessor-> s12n/newspaper: s12x5/标语 -possessor-> s12n/newspaper -> - | the prediction has no such edge
g_reentrancy | missing | s12x6/报导-01 -quote-> s12i3/identity-91: s12x6/报导-01 -quote-> s12i3/identity-91 -> - | the prediction has no such edge
g_reentrancy | extra | s12g/标语 -possessor-> s12p/person: - -> s12g/标语 -possessor-> s12p/person | gold has no such reentrancy
a_granularity | missing | «P» individual-person/individual-person/person: «P» individual-person/individual-person/person -> «外星人P'Lod» individual-person | inside a wider predicted node
a_granularity | extra | «外星人P'Lod» individual-person: «P» individual-person/individual-person/person -> «外星人P'Lod» individual-person | wider than the gold node
d_core_args_event | partial | s13x16: arg0 s13x13/人物; arg1 s13x18/中 -> arg0 s13x13/人物 | missing arg1 s13x18/中
d_peripheral_event | partial | s13x16: frequency s13x17/重复 -> frequency s13x17/重复; place s13x18/中 | extra place s13x18/中
e_core_labels | wrong | s13x16 -arg1-> s13x18: arg1 -> place | arg1 -> place
c_aspect | wrong | s14x6:aspect: activity -> process | activity -> process
d_core_args_event | wrong | s14x: arg0 s14i2/implicit-argument; arg1 s14x6/活动-01 -> arg1 s14i2/implicit-argument; arg2 s14x6/活动-01 | arg0 s14i2/implicit-argument: predicted as arg1; arg1 s14x6/活动-01: predicted as arg2
d_core_args_abstract | partial | s14h: arg1 s14i2/implicit-argument; arg1 s14x3/大; arg2 s14x4/最; arg5 s14x5/其中 -> arg1 s14i2/implicit-argument; arg2 s14x3/大; arg3 s14x4/最; arg5 s14x5/其中 | arg1 s14x3/大: predicted as arg2; arg2 s14x4/最: predicted as arg3
e_core_labels | wrong | s14x -arg0-> s14i2: arg0 -> arg1 | arg0 -> arg1
e_core_labels | wrong | s14x -arg1-> s14x6: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s14h -arg1-> s14x3: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s14h -arg2-> s14x4: arg2 -> arg3 | arg2 -> arg3
a_entity_concept | wrong | s15a: and -> individual-person | and -> individual-person
a_entity_concept | wrong | s15x11: 外星人 -> name | 外星人 -> name
a_granularity | missing | «外星人» 外星人: «外星人» 外星人 -> «外星人P'Lod» individual-person | inside a wider predicted node
a_granularity | missing | «P» individual-person: «P» individual-person -> «外星人P'Lod» individual-person | inside a wider predicted node
a_granularity | extra | «外星人P'Lod» individual-person: «外星人» 外星人; «P» individual-person -> «外星人P'Lod» individual-person | one predicted node for 2 gold nodes
b_event_sense | wrong | s15x: 指-02 -> 指-01 | 指-02 -> 指-01
b_event_sense | wrong | s15x3: 有-03 -> 有-01 | 有-03 -> 有-01
b_event_sense | wrong | s15x2: 领养 -> 领养-01 | 领养 -> 领养-01
c_other_attributes | extra | s15x11:op1: - -> 外星人 | gold has no :op1
c_other_attributes | extra | s15x11:op2: - -> p | gold has no :op2
c_other_attributes | extra | s15x11:op3: - -> ' | gold has no :op3
c_other_attributes | extra | s15x11:op4: - -> lod | gold has no :op4
d_core_args_event | partial | s15x3: arg0 s15a/and; arg1 s15x4/关系 -> arg0 s15i2/individual-person; arg1 s15x4/关系 | missing arg0 s15a/and; extra arg0 s15i2/individual-person
e_core_labels | wrong | s15x3 -arg0-> s15a: arg0 -> companion | arg0 -> companion
f_name_tokens | extra | s15a: - -> 外星人 p ' lod | gold has no :name
f_name_tokens | missing | s15x11: p ' lod -> - | the prediction has no :name
g_reentrancy | missing | s15x2/领养 -quote-> s15x/指-02: s15x2/领养 -quote-> s15x/指-02 -> - | the prediction has no such edge
g_reentrancy | missing | s15x3/有-03 -quote-> s15x/指-02: s15x3/有-03 -quote-> s15x/指-02 -> - | the prediction has no such edge
h_temporal | extra | have-mod-91 (snt12 s12h = pred s12h): - -> 宣称-01 «宣称» (snt12 s12x = pred s12c) :overlap have-mod-91 (snt12 s12h = pred s12h) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt12 s12x10 = pred s12r3): 报导-01 «报导» (snt12 s12x4 = pred s12r) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12r3) -> 宣称-01 «宣称» (snt12 s12x = pred s12c) :overlap 报导-01 «报导» (snt12 s12x10 = pred s12r3) | right relation, wrong parent
h_temporal | extra | 博君一笑 «博君一笑» (snt12 s12x12 = pred s12y): - -> 报导-01 «报导» (snt12 s12x10 = pred s12r3) :overlap 博君一笑 «博君一笑» (snt12 s12x12 = pred s12y) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt12 s12x4 = pred s12r): 宣称-01 «宣称» (snt12 s12x = pred s12c) :overlap 报导-01 «报导» (snt12 s12x4 = pred s12r) -> have-mod-91 (snt12 s12h = pred s12h) :overlap 报导-01 «报导» (snt12 s12x4 = pred s12r) | right relation, wrong parent
h_temporal | wrong | 报导-01 «报导» (snt12 s12x6 = pred s12r2): 报导-01 «报导» (snt12 s12x4 = pred s12r) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12r2) -> 宣称-01 «宣称» (snt12 s12x = pred s12c) :overlap 报导-01 «报导» (snt12 s12x6 = pred s12r2) | right relation, wrong parent
h_temporal | wrong | 创造-01 «创造» (snt13 s13x = pred s13c): 报导-01 «报导» (snt13 s13x2 = pred s13r) :overlap 创造-01 «创造» (snt13 s13x = pred s13c) -> document-creation-time :before 创造-01 «创造» (snt13 s13x = pred s13c) | wrong parent and relation
h_temporal | extra | 出现-01 «出现» (snt13 s13x16 = pred s13o): - -> 创造-01 «创造» (snt13 s13x = pred s13c) :after 出现-01 «出现» (snt13 s13x16 = pred s13o) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt13 s13x2 = pred s13r): document-creation-time :before 报导-01 «报导» (snt13 s13x2 = pred s13r) -> 创造-01 «创造» (snt13 s13x = pred s13c) :overlap 报导-01 «报导» (snt13 s13x2 = pred s13r) | wrong parent and relation
h_temporal | missing | 航天员 «航天员» (snt13 s13x6 = pred s13h): 创造-01 «创造» (snt13 s13x = pred s13c) :overlap 航天员 «航天员» (snt13 s13x6 = pred s13h) -> - | the prediction gives this node no temporal parent
h_temporal | extra | 旅行 «旅行» (snt13 s13x7 = pred s13l): - -> 报导-01 «报导» (snt13 s13x2 = pred s13r) :overlap 旅行 «旅行» (snt13 s13x7 = pred s13l) | gold gives this node no temporal parent
h_temporal | wrong | 算是-01 «算是» (snt14 s14x = pred s14s): document-creation-time :before 算是-01 «算是» (snt14 s14x = pred s14s) -> document-creation-time :overlap 算是-01 «算是» (snt14 s14x = pred s14s) | right parent, wrong relation
i_modal | extra | but-91 (snt11 s11b = pred s11b): - -> author :full-affirmative but-91 (snt11 s11b = pred s11b) | gold gives this node no modal parent
i_modal | extra | but-91 (snt12 s12b = pred s12b): - -> author :full-affirmative but-91 (snt12 s12b = pred s12b) | gold gives this node no modal parent
i_modal | partial | have-mod-91 (snt12 s12h = pred s12h): author :full-affirmative have-mod-91 (snt12 s12h = pred s12h); newspaper (snt12 s12n = pred s12x) :full-affirmative have-mod-91 (snt12 s12h = pred s12h) -> newspaper (snt12 s12n = pred s12x) :full-affirmative have-mod-91 (snt12 s12h = pred s12h) | agrees on part of the relations
i_modal | partial | 报导-01 «报导» (snt12 s12x10 = pred s12r3): author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12r3); newspaper (snt12 s12n = pred s12x) :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12r3) -> author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12r3) | agrees on part of the relations
i_modal | extra | 博君一笑 «博君一笑» (snt12 s12x12 = pred s12y): - -> author :full-affirmative 博君一笑 «博君一笑» (snt12 s12x12 = pred s12y) | gold gives this node no modal parent
i_modal | wrong | 报导-01 «报导» (snt12 s12x4 = pred s12r): author :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12r) -> newspaper (snt12 s12n = pred s12x) :full-affirmative 报导-01 «报导» (snt12 s12x4 = pred s12r) | right relation, wrong parent
i_modal | partial | 报导-01 «报导» (snt12 s12x6 = pred s12r2): author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12r2); newspaper (snt12 s12n = pred s12x) :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12r2) -> author :full-affirmative 报导-01 «报导» (snt12 s12x6 = pred s12r2) | agrees on part of the relations
i_modal | extra | 旅行 «旅行» (snt13 s13x7 = pred s13l): - -> author :full-affirmative 旅行 «旅行» (snt13 s13x7 = pred s13l) | gold gives this node no modal parent
i_modal | missing | and (snt15 s15a = pred s15o): author :full-affirmative and (snt15 s15a = pred s15o) -> - | the prediction gives this node no modal parent
i_modal | wrong | 领养 «领养» (snt15 s15x2 = pred s15l): and (snt15 s15a = pred s15o) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) -> 指-02 «指» (snt15 s15x = pred s15z) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) | right relation, wrong parent
i_modal | wrong | 有-03 «有» (snt15 s15x3 = pred s15y): and (snt15 s15a = pred s15o) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) -> 指-02 «指» (snt15 s15x = pred s15z) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) | right relation, wrong parent
j_coref_chain | partial | newspaper (snt11 s11n2 = pred s11x): 周报 «周报» (snt11 s11x5 = pred s11r); newspaper (snt12 s12n = pred s12x); person «P» (snt13 s13p = pred s13p) -> newspaper (snt12 s12n = pred s12x) | not linked to: 周报 «周报» (snt11 s11x5 = pred s11r); person «P» (snt13 s13p = pred s13p)
j_coref_chain | missing | 周报 «周报» (snt11 s11x5 = pred s11r): newspaper (snt11 s11n2 = pred s11x); newspaper (snt12 s12n = pred s12x); person «P» (snt13 s13p = pred s13p) -> - | the prediction links it to nothing
j_coref_chain | extra | ?person (snt12 s12p): - -> person «P» (snt13 s13p = pred s13p) | a predicted node that matches nothing in gold
j_coref_chain | partial | newspaper (snt12 s12n = pred s12x): newspaper (snt11 s11n2 = pred s11x); 周报 «周报» (snt11 s11x5 = pred s11r); person «P» (snt13 s13p = pred s13p) -> newspaper (snt11 s11n2 = pred s11x) | not linked to: 周报 «周报» (snt11 s11x5 = pred s11r); person «P» (snt13 s13p = pred s13p)
j_coref_chain | extra | individual-person «P» (snt13 s13i3 = pred s13i2): - -> and (snt15 s15a = pred s15o) | gold links it to nothing
j_coref_chain | wrong | person «P» (snt13 s13p = pred s13p): newspaper (snt12 s12n = pred s12x); newspaper (snt11 s11n2 = pred s11x); 周报 «周报» (snt11 s11x5 = pred s11r) -> ?person (snt12 s12p) | linked to another chain than gold's
j_coref_chain | extra | 外星人 «外星人» (snt13 s13x5 = pred s13w): - -> 外星人 «外星人» (snt14 s14x7 = pred s14w) | gold links it to nothing
j_coref_chain | extra | 外星人 «外星人» (snt14 s14x7 = pred s14w): - -> 外星人 «外星人» (snt13 s13x5 = pred s13w) | gold links it to nothing
j_coref_chain | extra | and (snt15 s15a = pred s15o): - -> individual-person «P» (snt13 s13i3 = pred s13i2) | gold links it to nothing

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.