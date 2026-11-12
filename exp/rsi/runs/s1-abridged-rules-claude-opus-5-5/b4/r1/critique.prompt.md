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



## Guidelines

# UMR guidelines, abridged



## 1. What a UMR is






**Variables.** Every node of sentence N has a variable starting with `s` + N (`s3d`, `s3p`), all
different within the document. A node that fills two roles is written once and then referred to by its
variable (re-entrancy: `:ARG0 s3p` above). Write the full node (name, appositive, `:part-of`) at the entity's first mention in word order, even inside a subordinate clause below the root; every later pronoun or unexpressed mention, also inside a relative clause, is a re-entrancy (a repeat with its own noun: see 5.3).

## 2. Concepts

### 2.1 Events

An event is a process or a state that is **predicated**, or a process used to **refer or modify**:

- verbs used as predicates (`deny-01`, Chinese `拥有-01`);
- event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events;
- participles and relative-clause verbs;
- predicated states: adjectives and nouns in predicate position (*he is tall*, 他很高) — through the
  abstract predicates of 2.3 when there is no lexical verb.

Not events: entity nouns, property words used as plain modifiers,
auxiliaries and modal verbs (*will, can, must*; 会, 能, 可以, 应该 — they affect `:aspect` and modal
strength, they are not nodes), light verbs (*make a decision* → `decide-01`; 进行访问 → `访问-01`),
the copula (*be*, 是) — it becomes one of the abstract predicates.

Only modal auxiliaries are dropped. Adverbs are nodes:
- aspectual and scope adverbs (*already, still, also, all*; 已经, 仍, 也, 都) are `:mod` on the event;
- past-time adverbs (*once, formerly*; 曾, 曾经) are `:temporal` (in the graph only; they get no temporal triple, see 5.1);
- a partitive like 其中 (*among them*) is `:mod` on the noun, but in a superlative it is the `:ARG5` comparison set;
- frequency adverbs (重复, 反复, 经常) are `:frequency`;
- a locative postposition after a time or period noun (X 时, X 中, X 以来, X 上 as in *in the history of ...*) is a `:temporal` node for the postposition with the noun as `:op1`, attached to the word it scopes over (often the head noun). After a place noun (在 N 中/上/里) the postposition node (`:op1` N) fills the verb's location role if the frame has one, else `:place`.

**Concept names.** An English event is its PropBank roleset (`deny-01`, `look-up-05`). A Chinese event is the
Chinese word as written with its Chinese PropBank sense (`拥有-01`, `执行-01`); a Chinese predicate that is not
in PropBank is `<word>-00`. Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :name (n / name :op1 "Russia"))`: an entity-type concept and `:name` with one `:opN` per word of the name.

- Do not write `:wiki`.

- The middle dot `·` in a transliterated foreign name is its own `:op`.
- For a titled work in title brackets 《 》, the brackets are their own first and last `:op`s.
- Choose the most specific type the name's head word or the context shows:
  - `newspaper` for a paper or weekly (报, 日报, 周报, tabloid);
  - `magazine` for 杂志 / 期刊;
  - `book`, `program`, etc. for other kinds of work;
  - `publication` only when the kind is unknown.
- A country or place name modifying a common noun (X 的历史, an X company) is `:place`, not `:mod`.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Any named being (human, character, alien, mascot) is `individual-person`, never `person` or the category noun; a name of common words is still a name (one `:op` per word), and a category word written with it at first mention goes inside the name. 地球, 月球, 太阳 are names: `planet`/`star` + `:name`.

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. A decade expression (X年代) is written with `:era` and the year number only (`:era 1980`), not `:decade` and not the written string. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`.
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

The belonging/membership sense of a verb is often not -01, and in it the owner is often `:ARG0` and the thing that belongs is `:ARG1`. A relative clause *the Y that belongs to X* then is `(y / Y :ARG0-of (b / V-0n :ARG1 x))` or `:ARG1-of`, whichever the frame gives the head noun; the owner fills the frame's owner role. Many Chinese intransitive and change-of-state verbs have only `:ARG0` (the thing that ceases, changes or acts). Do not default the theme to `:ARG1` by English habit. In particular, for change, become, reach and fall verbs (成, 达到, 跌, 变 type), the theme is usually `:ARG0` and the result or point reached is `:ARG1`. Copy the numbers from the roleset's role list every time. Traps: 有 has possession, existence/relationship-with and list-inclusion senses; count-as verbs (算是 type) number their roles from `:ARG0`. If the roleset lists only `:ARG0`, the single participant is `:ARG0` even when it looks like a patient (it starts, ceases, is founded, appears).

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. Do not add nodes for Chinese zero subjects or objects or for other unexpressed participants: leave the role out. A pronoun (also plural 他们/*they*) whose antecedent is an organization, company or publication is that entity: in the same sentence re-enter its variable (no new node); in a later sentence write the pronoun node and link it `:same-entity` to the entity, not to another pronoun. A possessive pronoun on an event noun adds no `:ARG0` or `:possessor`.

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
- N 有 A、B…等 where N is a topic, content or category noun listing its members: no 有/`have-91` node; N fills its outer role and takes `:example (a / and :op1 A ... :opk 等)`. 等 / *etc.* closing a list is always its last `:opN`, not `:mod`. List-item activity nouns, and an idiom filling an abstract predicate's value slot, are plain entities (no sense, aspect or triples). If N has no outer role but a relative-clause verb, that verb heads the clause (and is the anchor) with N as its argument.
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
- **Reciprocal relations.** In X 与/和/跟 Y 有关系/合作 type, both parties are `(a / and :op1 X :op2 Y)` in the first role, not `:companion`.
- **Describing clauses.** A clause that goes on describing the predicate noun of a copular sentence (*X is a Y, known for Z*) attaches under that noun, e.g. as `:ARG1-of`. It is not a separate top-level conjunct.
- **Trailing content clauses.** The same holds for a trailing clause without 为/为了 that tells what an object just created, named or described contains or does (…，容纳 Y). It attaches under that object (the creation verb's own argument, not its `:part-of` whole) as `:ARGn-of` with `:aspect process`. It is not `:purpose`, and it gets no re-entered subject.
- **Parts and media.** A physical edition or part of a publication is `:part-of` it, not `:possessor`. A medium noun (TV, 网络) modifying a program or product is `:medium`.
- **Heads.** In N1 的 N2, and in *change from A to B* (从 A 变为 B), the grammatical head common noun is the concept. A publication or organization name modifying it is `:part-of` (a part, section or edition of it) or `:possessor`, not the head.
- **Formats and parts as arguments.** When a format, layout or section noun (版面, edition, section) of a publication is an argument of any verb, that noun is the argument and the publication is its `:part-of`. Never write the inverse `:part` on the whole. This holds even when the publication's name is the grammatical head after 的 (V了 A的《X》 → `:ARG1 (a / A :part-of x)`).
- **Change from A to B.** In 从/由 A 变为/改为 B, A is the frame's 'thing changed' role (`:ARG1`), not `:source`; B is `:ARG2`.
- **Appositives.** An appositive descriptor before or after a name (its 旗下 tabloid 《X》) is `(x / <type> :name ... :ARG1-of (i / identity-91 :ARG2 (d / <descriptor> :mod ...)))`. Words like 旗下 stay a `:mod` node on the descriptor; do not turn them into a `:possessor` edge.
- **Role nouns with names.** A role, title or agent noun directly before or after a person's name is not an appositive `identity-91`. It is `(p / individual-person :name ... :ARG1-of (h / have-org-role-91 :ARG3 role))`, where role is e.g. `(r / 人 :ARG0-of (v / V-01))`. In Chinese documents write the role predicates as `have-org-role-91` / `have-rel-role-91`; spouse and kin titles (夫人, wife) use `have-rel-role-91`, and a modifying country is `:place` on the role noun. Use appositive `identity-91` only for non-role descriptors (e.g. of a publication).
- **Nested abstract predicates.** An abstract predicate that only modifies a noun gets no `:aspect` and no temporal or modal triple. This covers role reifications, an appositive `identity-91` and `have-quant-91`.

Reported speech and thought: the reported event is the `:ARG1` of the reporting verb. The top content event (and each conjunct) of a verb of saying, claiming, alleging or labelling, and of a quoted slogan, also gets `:quote <reporting event or introducing predicate>`.

## 4. Attributes

### 4.1 Aspect (`:aspect`, on every event)



| value | use for |
|---|---|
| `state` | states: non-verbal predicates (2.3), *be, have, know, want, like, believe*, 是, 有, 在, 知道, 喜欢, 认为 |
| `habitual` | an event that happens usually or repeatedly (经常, 每天) |
| `activity` | an ongoing process with no evidence of an end (*is running*, 正在, 着; a present-tense process; most generic statements of what is done) |
| `endeavor` | a process that ended without reaching its result (*worked on it for a week*, stop doing) |
| `performance` | a process that ended and reached its result: completed past events (*denied*, *was arrested*, 了, 过) |
| `process` | an event nominal, or a process whose type cannot be told |


Further aspect rules:
- **Repeated activity of an institution or periodical** (publishing, broadcasting, reporting, what it regularly contains or covers) is `habitual`, even with 了 and also as an event nominal (overrides `process`). Another event nominal for an ongoing generic activity is `activity`.
- **already + an aspectual stop verb governing another event** (已经停止 doing X) describing the current situation is `state`. A lexical termination verb with no governed event (a publication ceased, an organization dissolved) is `performance`, even with 已经.
- **Abstract predicates:** `identity-91` gets `:aspect state` only when it is the clause predicate (nested ones get none); `have-degree-91` gets no `:aspect` (the event under its `:ARG2` does).
- **A naming or evaluation passive** (*is called / is regarded as*, 被称为, 被誉为) is `performance`.
- An event noun governed by an aspectual verb (stop/start/continue + nominal) is `process`; the aspectual verb's subject is re-entered as its agent.
- **A negated event with a nominal event object** (没有经过X) is `process`.
- **Purpose verbs** naming an ongoing use are `activity`. A relative-clause verb giving what something is for or contains is `process`. A manner or property word on an event nominal is `:manner`, not `:mod`.
- **Stative verbs, continued.** Possession, belonging, existence, survival and knowing verbs stay `state` even with 了, 过, 曾经, a duration modifier or under *continue*. These markers only place the state in time for the temporal triples.

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
  context, 了, 过, 将, 会. When the root is a coordination, the first conjunct is the anchor; later conjuncts `:overlap` it unless an order word says otherwise. Statements about something the text says no longer exists are past (`:before`), even when generic.
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
  - An abstract predicate that is the content of a saying or thinking verb gets a modal parent but no temporal parent; its inner events are `(reporting-verb :overlap e)`.

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
  node, or an event used as conceiver). When the speaker is an expressed entity (also an organization), that node is the conceiver, never the reporting verb. Connectives (`and`, `but-91`, `contrast-91`) get no modal triple.
- An event under a modal or complement-taking predicate (*want, try, plan, decide, hope*, 想, 希望, 打算,
  决定, 需要): the predicate is asserted by the author, the complement has the predicate as parent with
  `unspecified` (or the strength the predicate implies): `(author :full-affirmative s3w)`
  `(s3w :unspecified s3g)`.
- A conceiver that is not in the text is `null-conceiver`. Write `(author :full-affirmative null-conceiver)` only if `null-conceiver` is a parent in that sentence. Purpose and condition clauses may use the
  constants `purpose` and `have-condition` as parents of their events. A purpose event that the text shows is actually realized is `(author :full-affirmative e)`.
- In the sentence graph, write the strength of an event that is not `full-affirmative` from the author as
  `:modal-strength <value>` too.

### 5.3 Coreference (`:coref`)

- `(earlier :same-entity later)`: two mentions of the same entity — a pronoun and its antecedent, a repeated
  name, a definite description. Link each mention to its closest earlier mention, earlier one first;
  link entity nodes, never `name` nodes.
- `(earlier :same-event later)`: two mentions of the very same event (the same act mentioned again, same arguments in the same roles; not a retelling with another object or agent, or a part instead of the whole). Do not link two different events that are merely related (e.g. a thing's founding and a later act by its founder).
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Link every mention of the main discourse entities. Do not build chains for incidental place names or other entities that occur only as modifiers (`:place`, `:mod`) in different sentences.
- Within one sentence, only pronouns and unexpressed mentions are re-entrancies; a mention with its own noun (shortened name, repeated head noun) is a new node plus a `:same-entity` triple.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.







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
    :op1 (s16b / 报导-01
        :ARG0 (s16k / 刊
            :mod (s16g / 该))
        :ARG1 (s16z / 支持-01
            :ARG0 (s16w / 外星人)
            :ARG1 (s16d / 当-01
                :ARG0 (s16p / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16t2 / 总统)
                :aspect state)
            :quote s16b
            :aspect state)
        :temporal (s16s / 时
            :op1 (s16x / 总统大选-00
                :temporal (s16y / date-entity
                    :year 2000)
                :aspect process))
        :aspect habitual)
    :op2 (s16c / 注销-01
        :ARG0 s16k
        :ARG1 (s16h / 照片
            :mod (s16m / 合成)
            :topic (s16o / 握手-01
                :ARG0 (s16f / 双方)
                :aspect process))
        :mod (s16r / 还)
        :aspect habitual)
    :op3 (s16e / 指-01
        :ARG0 s16k
        :ARG1 (s16l / 当选-01
            :ARG1 (s16q / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :temporal (s16y2 / date-entity
                :year 1992)
            :manner (s16v / 靠-01
                :ARG0 s16q
                :ARG1 (s16bs / 背书-01
                    :ARG0 (s16w2 / 外星人)
                    :aspect performance)
                :aspect performance)
            :mod (s16j / 也)
            :quote s16e
            :aspect performance)
        :mod (s16i / 甚至)
        :aspect habitual))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16y)
               (s16y :overlap s16b)
               (s16b :overlap s16x)
               (s16b :overlap s16z)
               (s16z :overlap s16d)
               (s16b :overlap s16c)
               (s16c :overlap s16o)
               (s16b :overlap s16e)
               (document-creation-time :before s16y2)
               (s16e :before s16l)
               (s16l :overlap s16v)
               (s16v :overlap s16bs))
    :modal ((root :modal author)
            (author :full-affirmative s16b)
            (author :full-affirmative s16c)
            (author :full-affirmative s16e)
            (author :full-affirmative s16x)
            (author :full-affirmative s16k)
            (s16k :full-affirmative s16z)
            (s16k :full-affirmative s16d)
            (s16k :full-affirmative s16o)
            (s16k :full-affirmative s16l)
            (s16k :full-affirmative s16v)
            (s16k :full-affirmative s16bs)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17h / have-mod-91
        :ARG1 (s17n / 内容
            :possessor (s17z / 周报))
        :ARG2 (s17t / 荒唐)
        :aspect state)
    :ARG2 (s17y / 有-01
        :ARG0 (s17p / 编辑
            :possessor s17z)
        :ARG1 (s17l / 能力
            :topic (s17d / 点-01
                :ARG0 s17p
                :ARG1 (s17a / and
                    :op1 (s17f / 荒谬
                        :possessor (s17w / 新闻
                            :mod (s17r / 真实)))
                    :op2 (s17g / 可笑
                        :possessor s17w))
                :place (s17t2 / 标题)
                :modal-strength neutral-affirmative
                :aspect habitual))
        :mod (s17m / 也)
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17h)
               (s17h :overlap s17y)
               (s17y :overlap s17d))
    :modal ((root :modal author)
            (author :full-affirmative s17h)
            (author :full-affirmative s17y)
            (s17y :neutral-affirmative s17d))
    :coref ((s16k :same-entity s17z)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18k / 刊登-01
    :ARG0 (s18p / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s18i / implicit-argument
        :quant 1
        :unit (s18u / 篇)
        :topic (s18f / 复制-01
            :ARG0 (s18c / country
                :name (s18n / name
                    :op1 "苏联"))
            :ARG1 (s18h / individual-person
                :name (s18n2 / name
                    :op1 "希特勒")
                :quant 10000
                :unit (s18g / 个))
            :quote s18k
            :aspect performance))
    :place (s18l / 位置
        :mod (s18x / 显著))
    :temporal (s18t / 时
        :op1 (s18z / 争论-01
            :ARG0 (s18q / 全世界)
            :ARG1 (s18e / 问题
                :mod (s18d / 道德)
                :topic (s18r / 复制人))
            :aspect activity))
    :aspect habitual)


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18k)
               (s18k :overlap s18z)
               (s18k :overlap s18f))
    :modal ((root :modal author)
            (author :full-affirmative s18k)
            (author :full-affirmative s18z)
            (author :full-affirmative s18p)
            (s18p :full-affirmative s18f))
    :coref ((s17z :same-entity s18p)))


################################################################################
# meta-info
# :: snt19
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Words: 为了 讽刺 美国 的 外交 政策 ， 他们 也 报导 了 一篇 「 美国 买通 外星人 去 追杀 宾拉登 」 。

# sentence level graph:
(s19h / have-purpose-91
    :ARG1 (s19b / 报导-01
        :ARG0 (s19p / person
            :refer-person 3rd
            :refer-number plural)
        :ARG1 (s19i / implicit-argument
            :quant 1
            :unit (s19u / 篇)
            :topic (s19m / 买通-01
                :ARG0 (s19c / country
                    :name (s19n / name
                        :op1 "美国"))
                :ARG1 (s19w / 外星人)
                :purpose (s19z / 追杀-01
                    :ARG0 s19w
                    :ARG1 (s19l / individual-person
                        :name (s19n2 / name
                            :op1 "宾拉登"))
                    :modal-strength unspecified
                    :aspect process)
                :quote s19b
                :aspect performance))
        :mod (s19e / 也)
        :aspect habitual)
    :ARG2 (s19f / 讽刺-01
        :ARG1 (s19g / 政策
            :mod (s19j / 外交)
            :possessor (s19c2 / country
                :name (s19n3 / name
                    :op1 "美国")))
        :aspect process)
    :aspect state)


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19b)
               (s19b :overlap s19f)
               (s19b :overlap s19m)
               (s19m :overlap s19z))
    :modal ((root :modal author)
            (author :full-affirmative s19h)
            (author :full-affirmative s19b)
            (author :full-affirmative s19f)
            (author :full-affirmative s19p)
            (s19p :full-affirmative s19m)
            (s19m :unspecified s19z))
    :coref ((s18p :same-entity s19p)
            (s19c2 :same-entity s19c)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20t / 贴-01
    :ARG0 (s20p / 好事者)
    :ARG1 (s20n / 新闻
        :quant 1
        :unit (s20u / 篇)
        :possessor (s20k / 刊
            :mod (s20g / 该))
        :topic (s20i / identity-91
            :ARG1 (s20s / 参议员
                :quant 12
                :unit (s20w / 位)
                :place (s20c / country
                    :name (s20cn / name
                        :op1 "美国")))
            :ARG2 (s20a / 外星人)
            :aspect state))
    :ARG2 (s20z / 墙上
        :possessor (s20j / 记者团
            :possessor (s20o / government-organization
                :name (s20on / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :mod (s20m / 甚至)
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20t))
    :modal ((root :modal author)
            (author :full-affirmative s20t)
            (author :full-affirmative s20k)
            (s20k :full-affirmative s20i))
    :coref ((s19p :same-entity s20k)))



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
a_event_found: R 100 / P 93 / F 97
a_event_concept: R 79 / P 79 / F 79
a_entity_found: R 100 / P 84 / F 91
a_entity_concept: R 76 / P 76 / F 76
a_granularity: R 100 / P 100 / F 100
b_event_sense: R 48 / P 48 / F 48
c_aspect: R 42 / P 53 / F 47
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 80 / P 80 / F 80
d_core_args_event: R 56 / P 75 / F 64
d_core_args_abstract: R 25 / P 33 / F 29
d_peripheral_event: R 67 / P 33 / F 44
d_peripheral_entity: R 32 / P 24 / F 27
e_core_labels: R 79 / P 79 / F 79
e_peripheral_labels: R 79 / P 79 / F 79
f_name_tokens: R 50 / P 57 / F 53
g_reentrancy: R 56 / P 45 / F 50
h_temporal: R 45 / P 43 / F 44
i_modal: R 37 / P 34 / F 35
j_coref_chain: R 100 / P 71 / F 83
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_event_found | extra | s16v: - -> 靠-01 | matches no gold node
a_entity_found | extra | s16y: - -> date-entity | matches no gold node
a_entity_found | extra | s16r: - -> 还 | matches no gold node
a_entity_found | extra | s16j: - -> 也 | matches no gold node
a_entity_found | extra | s16i: - -> 甚至 | matches no gold node
a_entity_concept | wrong | s16e: event -> 时 | event -> 时
b_event_sense | wrong | s16x8: 当-02 -> 当-01 | 当-02 -> 当-01
b_event_sense | wrong | s16x2: 注销 -> 注销-01 | 注销 -> 注销-01
b_event_sense | wrong | s16x11: 合成-01 -> 合成 | 合成-01 -> 合成
b_event_sense | wrong | s16x3: 指-02 -> 指-01 | 指-02 -> 指-01
b_event_sense | wrong | s16x15: 背书 -> 背书-01 | 背书 -> 背书-01
c_aspect | wrong | s16x:aspect: performance -> habitual | performance -> habitual
c_aspect | extra | s16x8:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s16x2:aspect: performance -> habitual | performance -> habitual
c_aspect | missing | s16x11:aspect: performance -> - | the prediction has no :aspect
c_aspect | wrong | s16x3:aspect: performance -> habitual | performance -> habitual
d_core_args_event | missing | s16x11: arg1 s16x10/照片 -> - | missing arg1 s16x10/照片
d_core_args_event | wrong | s16x14: arg0 s16i3/individual-person -> arg1 s16i3/individual-person | arg0 s16i3/individual-person: predicted as arg1
d_peripheral_event | extra | s16x2: - -> mod s16r/还 (not in gold) | extra mod s16r/还 (not in gold)
d_peripheral_event | extra | s16x3: - -> mod s16i/甚至 (not in gold) | extra mod s16i/甚至 (not in gold)
d_peripheral_event | partial | s16x14: temporal s16d/date-entity -> manner s16v/靠-01 (not in gold); mod s16j/也 (not in gold); temporal s16d/date-entity | extra manner s16v/靠-01 (not in gold); extra mod s16j/也 (not in gold)
d_peripheral_entity | wrong | s16x10: mod s16x12/握手-01 -> mod s16x11/合成-01; topic s16x12/握手-01 | mod s16x12/握手-01: predicted as topic; extra mod s16x11/合成-01
e_core_labels | wrong | s16x14 -arg0-> s16i3: arg0 -> arg1 | arg0 -> arg1
e_peripheral_labels | wrong | s16x10 -mod-> s16x12: mod -> topic | mod -> topic
f_name_tokens | missing | s16e: 2000 年 总统大选 -> - | the prediction has no :name
g_reentrancy | missing | s16x/报导-01 -quote-> s16x/报导-01: s16x/报导-01 -quote-> s16x/报导-01 -> - | the prediction has no such edge
g_reentrancy | missing | s16x15/背书 -quote-> s16x3/指-02: s16x15/背书 -quote-> s16x3/指-02 -> - | the prediction has no such edge
g_reentrancy | extra | s16v/靠-01 -arg0-> s16q/individual-person: - -> s16v/靠-01 -arg0-> s16q/individual-person | gold has no such reentrancy
g_reentrancy | extra | s16z/支持-01 -quote-> s16b/报导-01: - -> s16z/支持-01 -quote-> s16b/报导-01 | gold has no such reentrancy
a_event_concept | wrong | s17i2: identity -> have-mod | identity -> have-mod
a_event_concept | wrong | s17x7: 点出 -> 点 | 点出 -> 点
a_entity_found | extra | s17m: - -> 也 | matches no gold node
b_event_sense | wrong | s17x: 荒唐-01 -> 荒唐 | 荒唐-01 -> 荒唐
b_event_sense | wrong | s17x2: 有-06 -> 有-01 | 有-06 -> 有-01
b_event_sense | wrong | s17x8: 荒谬-01 -> 荒谬 | 荒谬-01 -> 荒谬
b_event_sense | wrong | s17x11: 真实-01 -> 真实 | 真实-01 -> 真实
b_event_sense | wrong | s17x9: 可笑-01 -> 可笑 | 可笑-01 -> 可笑
c_aspect | missing | s17x:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x8:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x11:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x9:aspect: state -> - | the prediction has no :aspect
d_core_args_event | partial | s17b: arg1 s17x/荒唐-01; arg2 s17x2/有-06 -> arg1 s17i2/identity-91; arg2 s17x2/有-06 | missing arg1 s17x/荒唐-01; extra arg1 s17i2/identity-91
d_core_args_event | missing | s17x: arg0 s17x3/内容 -> - | missing arg0 s17x3/内容
d_core_args_event | missing | s17x8: arg0 s17x10/新闻 -> - | missing arg0 s17x10/新闻
d_core_args_event | missing | s17x11: arg0 s17x10/新闻 -> - | missing arg0 s17x10/新闻
d_core_args_abstract | wrong | s17i2: arg1 s17x6/能力; arg2 s17x7/点出-01 -> arg1 s17x3/内容; arg2 s17x/荒唐-01 | missing arg1 s17x6/能力; missing arg2 s17x7/点出-01; extra arg1 s17x3/内容; extra arg2 s17x/荒唐-01
d_peripheral_event | extra | s17x2: - -> mod s17m/也 (not in gold) | extra mod s17m/也 (not in gold)
d_peripheral_event | extra | s17x8: - -> possessor s17x10/新闻 | extra possessor s17x10/新闻
d_peripheral_entity | extra | s17x3: - -> possessor s17x4/周报 | extra possessor s17x4/周报
d_peripheral_entity | missing | s17x4: part s17x3/内容 -> - | missing part s17x3/内容
d_peripheral_entity | extra | s17x6: - -> topic s17x7/点出-01 | extra topic s17x7/点出-01
d_peripheral_entity | extra | s17x10: - -> mod s17x11/真实-01 | extra mod s17x11/真实-01
e_core_labels | wrong | s17x8 -arg0-> s17x10: arg0 -> possessor | arg0 -> possessor
g_reentrancy | missing | s17x9/可笑-01 -arg0-> s17x10/新闻: s17x9/可笑-01 -arg0-> s17x10/新闻 -> - | the prediction has no such edge
g_reentrancy | extra | s17g/可笑 -possessor-> s17w/新闻: - -> s17g/可笑 -possessor-> s17w/新闻 | gold has no such reentrancy
a_event_concept | wrong | s18h: have-example -> 时 | have-example -> 时
a_entity_concept | wrong | s18i2: implicit-predicate -> individual-person | implicit-predicate -> individual-person
a_entity_concept | wrong | s18p: publication -> implicit-argument | publication -> implicit-argument
a_entity_concept | wrong | s18x6: 世界 -> 全世界 | 世界 -> 全世界
a_entity_concept | wrong | s18x7: 全 -> country | 全 -> country
a_entity_concept | wrong | s18x10: 人 -> 复制人 | 人 -> 复制人
b_event_sense | wrong | s18x3: 显著-01 -> 显著 | 显著-01 -> 显著
c_aspect | wrong | s18x:aspect: performance -> habitual | performance -> habitual
c_aspect | missing | s18x3:aspect: state -> - | the prediction has no :aspect
c_aspect | wrong | s18x11:aspect: process -> performance | process -> performance
c_other_attributes | extra | s18i2:quant: - -> 10000 | gold has no :quant
d_core_args_event | partial | s18x: arg0 s18t/thing; arg1 s18x2/位置; arg2 s18p/publication -> arg0 s18t/thing; arg1 s18p/publication | missing arg1 s18x2/位置; arg2 s18p/publication: predicted as arg1
d_core_args_event | missing | s18x3: arg0 s18x2/位置 -> - | missing arg0 s18x2/位置
d_core_args_event | wrong | s18x11: arg1 s18x10/人 -> arg0 s18x7/全; arg1 s18i2/implicit-predicate | missing arg1 s18x10/人; extra arg0 s18x7/全; extra arg1 s18i2/implicit-predicate
d_core_args_abstract | missing | s18h: arg1 s18i2/implicit-predicate; arg2 s18x/刊登-01 -> - | missing arg1 s18i2/implicit-predicate; missing arg2 s18x/刊登-01
d_peripheral_event | wrong | s18x: temporal s18x5/争论-01 -> place s18x2/位置; temporal s18h/have-example-91 | missing temporal s18x5/争论-01; extra place s18x2/位置; extra temporal s18h/have-example-91
d_peripheral_entity | extra | s18i2: - -> unit s18n/name | extra unit s18n/name
d_peripheral_entity | extra | s18x2: - -> mod s18x3/显著-01 | extra mod s18x3/显著-01
d_peripheral_entity | partial | s18p: unit s18x4/篇 -> topic s18x11/复制-01; unit s18x4/篇 | extra topic s18x11/复制-01
d_peripheral_entity | missing | s18x6: mod s18x7/全 -> - | missing mod s18x7/全
e_core_labels | wrong | s18x -arg1-> s18x2: arg1 -> place | arg1 -> place
e_core_labels | wrong | s18x -arg2-> s18p: arg2 -> arg1 | arg2 -> arg1
f_name_tokens | extra | s18i2: - -> 希特勒 | gold has no :name
f_name_tokens | missing | s18p: 「 苏联 复制 一万个 希特勒 」 -> - | the prediction has no :name
f_name_tokens | extra | s18x7: - -> 苏联 | gold has no :name
g_reentrancy | extra | s18f/复制-01 -quote-> s18k/刊登-01: - -> s18f/复制-01 -quote-> s18k/刊登-01 | gold has no such reentrancy
a_event_found | extra | s19z: - -> 追杀-01 | matches no gold node
a_event_concept | wrong | s19h: have-reason -> have-purpose | have-reason -> have-purpose
a_entity_found | extra | s19l: - -> individual-person | matches no gold node
a_entity_found | extra | s19c2: - -> country | matches no gold node
a_entity_concept | wrong | s19p2: publication -> implicit-argument | publication -> implicit-argument
a_entity_concept | wrong | s19x4: 篇 -> 买通 | 篇 -> 买通
c_aspect | extra | s19h:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s19x:aspect: performance -> habitual | performance -> habitual
c_aspect | wrong | s19x2:aspect: performance -> process | performance -> process
c_other_attributes | missing | s19x3:quant: 1 -> - | the prediction has no :quant
d_peripheral_entity | partial | s19p2: unit s19x7/篇 -> topic s19x4/篇; unit s19x7/篇 | extra topic s19x4/篇
d_peripheral_entity | missing | s19x3: unit s19x4/篇 -> - | missing unit s19x4/篇
d_peripheral_entity | extra | s19x4: - -> purpose s19z/追杀-01 (not in gold) | extra purpose s19z/追杀-01 (not in gold)
d_peripheral_entity | wrong | s19x5: possessor s19c/country; topic s19x6/外交 -> mod s19x6/外交; possessor s19c2/country (not in gold) | missing possessor s19c/country; topic s19x6/外交: predicted as mod; extra possessor s19c2/country (not in gold)
e_peripheral_labels | wrong | s19x5 -topic-> s19x6: topic -> mod | topic -> mod
f_name_tokens | missing | s19p2: 「 美国 买通 外星人 去 追杀 宾拉登 」 -> - | the prediction has no :name
g_reentrancy | missing | s19x2/讽刺-01 -arg0-> s19p/person: s19x2/讽刺-01 -arg0-> s19p/person -> - | the prediction has no such edge
g_reentrancy | extra | s19z/追杀-01 -arg0-> s19w/外星人: - -> s19z/追杀-01 -arg0-> s19w/外星人 | gold has no such reentrancy
g_reentrancy | extra | s19m/买通-01 -quote-> s19b/报导-01: - -> s19m/买通-01 -quote-> s19b/报导-01 | gold has no such reentrancy
a_event_concept | wrong | s20x: 贴到 -> 贴 | 贴到 -> 贴
a_event_concept | wrong | s20x3: 好事 -> 甚至 | 好事 -> 甚至
a_entity_found | extra | s20w: - -> 位 | matches no gold node
a_entity_found | extra | s20a: - -> 外星人 | matches no gold node
a_entity_concept | wrong | s20x2: 者 -> 好事者 | 者 -> 好事者
a_entity_concept | wrong | s20b: building -> government-organization | building -> government-organization
a_entity_concept | wrong | s20p: publication -> country | publication -> country
c_aspect | missing | s20x3:aspect: state -> - | the prediction has no :aspect
d_core_args_event | partial | s20x: arg0 s20x2/者; arg1 s20x4/墙上; arg2 s20x6/新闻 -> arg0 s20x2/者; arg1 s20x6/新闻; arg2 s20x4/墙上 | arg1 s20x4/墙上: predicted as arg2; arg2 s20x6/新闻: predicted as arg1
d_core_args_event | missing | s20x3: arg0 s20x2/者 -> - | missing arg0 s20x2/者
d_core_args_abstract | wrong | s20i2: arg1 s20x6/新闻; arg2 s20p/publication -> arg1 s20n2/name; arg2 s20a/外星人 (not in gold) | missing arg1 s20x6/新闻; missing arg2 s20p/publication; extra arg1 s20n2/name; extra arg2 s20a/外星人 (not in gold)
d_peripheral_event | extra | s20x: - -> mod s20x3/好事 | extra mod s20x3/好事
d_peripheral_entity | extra | s20x4: - -> possessor s20x5/记者团 | extra possessor s20x5/记者团
d_peripheral_entity | wrong | s20x5: place s20b/building; place s20x4/墙上 -> possessor s20b/building | place s20b/building: predicted as possessor; missing place s20x4/墙上
d_peripheral_entity | partial | s20x6: unit s20x7/篇 -> possessor s20x8/刊; topic s20i2/identity-91; unit s20x7/篇 | extra possessor s20x8/刊; extra topic s20i2/identity-91
d_peripheral_entity | partial | s20x8: mod s20x9/该; part s20x6/新闻 -> mod s20x9/该 | missing part s20x6/新闻
e_core_labels | wrong | s20x -arg1-> s20x4: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s20x -arg2-> s20x6: arg2 -> arg1 | arg2 -> arg1
e_peripheral_labels | wrong | s20x5 -place-> s20b: place -> possessor | place -> possessor
f_name_tokens | wrong | s20p: 「 12 位 美国 参议员 是 外星人 ！ 」 -> 美国 | 「 12 位 美国 参议员 是 外星人 ！ 」 -> 美国
h_temporal | extra | ?靠-01 «靠» (snt16 s16v): - -> 当选-01 «当选» (snt16 s16x14 = pred s16l) :overlap ?靠-01 «靠» (snt16 s16v) | a predicted node that matches nothing in gold
h_temporal | extra | ?date-entity (snt16 s16y): - -> document-creation-time :before ?date-entity (snt16 s16y) | a predicted node that matches nothing in gold
h_temporal | extra | date-entity (snt16 s16d = pred s16y2): - -> document-creation-time :before date-entity (snt16 s16d = pred s16y2) | gold gives this node no temporal parent
h_temporal | extra | name (snt16 s16n3 = pred s16x): - -> 报导-01 «报导» (snt16 s16x = pred s16b) :overlap name (snt16 s16n3 = pred s16x) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): document-creation-time :before 报导-01 «报导» (snt16 s16x = pred s16b) -> ?date-entity (snt16 s16y) :overlap 报导-01 «报导» (snt16 s16x = pred s16b) | wrong parent and relation
h_temporal | missing | 合成-01 «合成» (snt16 s16x11 = pred s16m): 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 合成-01 «合成» (snt16 s16x11 = pred s16m) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 握手-01 «握手» (snt16 s16x12 = pred s16o): 合成-01 «合成» (snt16 s16x11 = pred s16m) :overlap 握手-01 «握手» (snt16 s16x12 = pred s16o) -> 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 握手-01 «握手» (snt16 s16x12 = pred s16o) | right relation, wrong parent
h_temporal | wrong | 背书 «背书» (snt16 s16x15 = pred s16bs): 当选-01 «当选» (snt16 s16x14 = pred s16l) :overlap 背书 «背书» (snt16 s16x15 = pred s16bs) -> ?靠-01 «靠» (snt16 s16v) :overlap 背书 «背书» (snt16 s16x15 = pred s16bs) | right relation, wrong parent
h_temporal | wrong | 指-02 «指» (snt16 s16x3 = pred s16e): 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 指-02 «指» (snt16 s16x3 = pred s16e) -> 报导-01 «报导» (snt16 s16x = pred s16b) :overlap 指-02 «指» (snt16 s16x3 = pred s16e) | right relation, wrong parent
h_temporal | extra | identity-91 (snt17 s17i2 = pred s17h): - -> document-creation-time :before identity-91 (snt17 s17i2 = pred s17h) | gold gives this node no temporal parent
h_temporal | missing | 荒唐-01 «荒唐» (snt17 s17x = pred s17t): document-creation-time :before 荒唐-01 «荒唐» (snt17 s17x = pred s17t) -> - | the prediction gives this node no temporal parent
h_temporal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17r): 荒谬-01 «荒谬» (snt17 s17x8 = pred s17f) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17r) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 有-06 «有» (snt17 s17x2 = pred s17y): 荒唐-01 «荒唐» (snt17 s17x = pred s17t) :overlap 有-06 «有» (snt17 s17x2 = pred s17y) -> identity-91 (snt17 s17i2 = pred s17h) :overlap 有-06 «有» (snt17 s17x2 = pred s17y) | right relation, wrong parent
h_temporal | missing | 荒谬-01 «荒谬» (snt17 s17x8 = pred s17f): 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 荒谬-01 «荒谬» (snt17 s17x8 = pred s17f) -> - | the prediction gives this node no temporal parent
h_temporal | missing | 可笑-01 «可笑» (snt17 s17x9 = pred s17g): 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 可笑-01 «可笑» (snt17 s17x9 = pred s17g) -> - | the prediction gives this node no temporal parent
h_temporal | extra | 复制-01 «复制» (snt18 s18x11 = pred s18f): - -> 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 复制-01 «复制» (snt18 s18x11 = pred s18f) | gold gives this node no temporal parent
h_temporal | missing | 显著-01 «显著» (snt18 s18x3 = pred s18x): 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 显著-01 «显著» (snt18 s18x3 = pred s18x) -> - | the prediction gives this node no temporal parent
h_temporal | extra | ?追杀-01 «追杀» (snt19 s19z): - -> 篇 «一篇» (snt19 s19x4 = pred s19m) :overlap ?追杀-01 «追杀» (snt19 s19z) | a predicted node that matches nothing in gold
h_temporal | extra | 篇 «一篇» (snt19 s19x4 = pred s19m): - -> 报导-01 «报导» (snt19 s19x = pred s19b) :overlap 篇 «一篇» (snt19 s19x4 = pred s19m) | gold gives this node no temporal parent
h_temporal | missing | 好事 «好事者» (snt20 s20x3 = pred s20m): 贴到-01 «贴到» (snt20 s20x = pred s20t) :overlap 好事 «好事者» (snt20 s20x3 = pred s20m) -> - | the prediction gives this node no temporal parent
i_modal | extra | ?靠-01 «靠» (snt16 s16v): - -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative ?靠-01 «靠» (snt16 s16v) | a predicted node that matches nothing in gold
i_modal | extra | name (snt16 s16n3 = pred s16x): - -> author :full-affirmative name (snt16 s16n3 = pred s16x) | gold gives this node no modal parent
i_modal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) -> author :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) | right relation, wrong parent
i_modal | missing | 合成-01 «合成» (snt16 s16x11 = pred s16m): author :full-affirmative 合成-01 «合成» (snt16 s16x11 = pred s16m) -> - | the prediction gives this node no modal parent
i_modal | wrong | 握手-01 «握手» (snt16 s16x12 = pred s16o): author :full-affirmative 握手-01 «握手» (snt16 s16x12 = pred s16o) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 握手-01 «握手» (snt16 s16x12 = pred s16o) | right relation, wrong parent
i_modal | wrong | 当选-01 «当选» (snt16 s16x14 = pred s16l): author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16l) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16l) | right relation, wrong parent
i_modal | wrong | 背书 «背书» (snt16 s16x15 = pred s16bs): author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16bs) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16bs) | right relation, wrong parent
i_modal | wrong | 注销 «注销» (snt16 s16x2 = pred s16c): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16c) -> author :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16c) | right relation, wrong parent
i_modal | wrong | 指-02 «指» (snt16 s16x3 = pred s16e): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16e) -> author :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16e) | right relation, wrong parent
i_modal | wrong | 支持-01 «支持» (snt16 s16x6 = pred s16z): author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z) | right relation, wrong parent
i_modal | extra | 当-02 «当» (snt16 s16x8 = pred s16d): - -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16d) | gold gives this node no modal parent
i_modal | missing | 荒唐-01 «荒唐» (snt17 s17x = pred s17t): author :full-affirmative 荒唐-01 «荒唐» (snt17 s17x = pred s17t) -> - | the prediction gives this node no modal parent
i_modal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17r): author :full-affirmative 真实-01 «真实» (snt17 s17x11 = pred s17r) -> - | the prediction gives this node no modal parent
i_modal | partial | 点出-01 «点» (snt17 s17x7 = pred s17d): author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) [from the sentence-graph modal-strength] -> author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) [from the sentence-graph modal-strength]; 有-06 «有» (snt17 s17x2 = pred s17y) :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) | agrees on part of the relations
i_modal | missing | 荒谬-01 «荒谬» (snt17 s17x8 = pred s17f): author :full-affirmative 荒谬-01 «荒谬» (snt17 s17x8 = pred s17f) -> - | the prediction gives this node no modal parent
i_modal | missing | 可笑-01 «可笑» (snt17 s17x9 = pred s17g): author :full-affirmative 可笑-01 «可笑» (snt17 s17x9 = pred s17g) -> - | the prediction gives this node no modal parent
i_modal | extra | thing (snt18 s18t = pred s18p): - -> author :full-affirmative thing (snt18 s18t = pred s18p) | gold gives this node no modal parent
i_modal | wrong | 复制-01 «复制» (snt18 s18x11 = pred s18f): author :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18f) -> thing (snt18 s18t = pred s18p) :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18f) | right relation, wrong parent
i_modal | missing | 显著-01 «显著» (snt18 s18x3 = pred s18x): author :full-affirmative 显著-01 «显著» (snt18 s18x3 = pred s18x) -> - | the prediction gives this node no modal parent
i_modal | extra | ?追杀-01 «追杀» (snt19 s19z): - -> author :unspecified ?追杀-01 «追杀» (snt19 s19z) [from the sentence-graph modal-strength]; 篇 «一篇» (snt19 s19x4 = pred s19m) :unspecified ?追杀-01 «追杀» (snt19 s19z) | a predicted node that matches nothing in gold
i_modal | extra | have-reason-91 (snt19 s19h = pred s19h): - -> author :full-affirmative have-reason-91 (snt19 s19h = pred s19h) | gold gives this node no modal parent
i_modal | extra | person (snt19 s19p = pred s19p): - -> author :full-affirmative person (snt19 s19p = pred s19p) | gold gives this node no modal parent
i_modal | extra | 篇 «一篇» (snt19 s19x4 = pred s19m): - -> person (snt19 s19p = pred s19p) :full-affirmative 篇 «一篇» (snt19 s19x4 = pred s19m) | gold gives this node no modal parent
i_modal | wrong | identity-91 (snt20 s20i2 = pred s20i): author :full-affirmative identity-91 (snt20 s20i2 = pred s20i) -> 刊 «该刊» (snt20 s20x8 = pred s20k) :full-affirmative identity-91 (snt20 s20i2 = pred s20i) | right relation, wrong parent
i_modal | missing | 好事 «好事者» (snt20 s20x3 = pred s20m): author :full-affirmative 好事 «好事者» (snt20 s20x3 = pred s20m) -> - | the prediction gives this node no modal parent
i_modal | extra | 刊 «该刊» (snt20 s20x8 = pred s20k): - -> author :full-affirmative 刊 «该刊» (snt20 s20x8 = pred s20k) | gold gives this node no modal parent
j_coref_chain | extra | ?country «美国» (snt19 s19c2): - -> country (snt19 s19c = pred s19c) | a predicted node that matches nothing in gold
j_coref_chain | extra | country (snt19 s19c = pred s19c): - -> ?country «美国» (snt19 s19c2) | gold links it to nothing

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.