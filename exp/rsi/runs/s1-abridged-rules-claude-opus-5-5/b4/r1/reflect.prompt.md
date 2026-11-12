<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29933). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

# The current instruction
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

# The critique (training batch 4: chinese_umr-0001, sentences 16-20; AnCast++ comprehensive 42.2)
<critique>
# Review of the UMR annotation of sentences 16–20: costly error patterns and changes to the instruction

The patterns are ordered by cost, highest first. Counts are approximate units from umrjudge.

## 1. Property words were left as plain modifiers or wrapped in `have-mod-91` (about 35 units, the largest cost)

**What went wrong.** Chinese adjectives and stative words should be events, but the annotator left them out. This covers:
- a predicative adjective in a concessive clause;
- adjectives in "X 与 Y" coordinations under a verb;
- attributive adjectives on nouns, such as "real news", "prominent position" and "composite photo";
- the stative part of an agent compound.

The gold makes each of them a `<word>-01` event with `:aspect state`. The described noun is `:ARG0` of the event (written `:ARG0-of` when the word modifies the noun). Each event also gets `(parent :overlap e)` and `(author :full-affirmative e)`.

The annotator instead used `have-mod-91` (wrong concept, wrong arguments, and a wrong anchor for the sentence), `:mod`, or `:possessor`. This shows up in b_event_sense, c_aspect, d_core_args, h_temporal and i_modal. Another gold document (an attributive adjective done as `:ARG0-of 特别-01 :aspect state`) confirms the practice.

**Why.** Section 2.1 lists "property words used as plain modifiers" as not events. Section 2.3 says to use `have-mod-91` for "X is Adj". Both are English-centred rules.

**Change.** Add a Chinese rule: a Chinese adjective or stative word that has a PropBank frame is always an event, whether it is a predicate or an attributive modifier (with or without 的).
- Predicate: `(e / Adj-01 :ARG0 theme :aspect state)`.
- Attributive: `(n / noun :ARG0-of (e / Adj-01 :aspect state))`.
- In both cases, use the role number the roleset gives; it is often `:ARG0`.
- It gets temporal `:overlap` with its governing event and `(author :full-affirmative e)`.
- Use `have-mod-91` only when the property word has no frame.
- Keep the "not events" clause only for non-frame modifiers, such as demonstratives, plain nouns and sense-less words.

## 2. A quoted headline was annotated as an inner clause instead of as a named work (about 25 units)

**What went wrong.** An article title in 「 」 brackets was the object of a publishing or reporting verb, counted with an article classifier ("一篇 「…」") or placed after "新闻". The annotator parsed its content into events, countries, persons and `:quote` links, plus an `implicit-argument` head. This produced many extra nodes, modal and temporal triples, and reentrancies.

The gold makes the title `publication :name` with every word as an `:opN`, the brackets included, and `:quant 1 :unit 篇` on that node. When an article noun is present, the gold links them as `(noun :ARG1-of (identity-91 :ARG2 publication-name))`. The title's content gets no events and no modal or temporal triples.

**Why.** Section 2.2 gives the bracket rule only for 《 》. Nothing distinguishes a quoted title from quoted reported content.

**Change.** Add this rule: a quoted string that names an article or headline is a named `publication`, and its whole text, brackets and punctuation included, is split into `:op`s. Treat it this way when it is:
- counted with an article classifier (篇, 则);
- in apposition to an article noun; or
- the object of a publishing verb.

No inner structure is built for it. Keep the clause analysis plus `:quote` only when the quotation is the direct content of a verb of saying or reporting and has no article classifier or article noun.

## 3. The wrong sense, the wrong frame roles, or a split compound verb (about 15 units)

**What went wrong.**
- A verb of claiming was given the "refer to" sense instead of the "point out / claim" sense.
- A verb of holding a position was given its first sense instead of the position-holder sense.
- 有 + ability was given `有-01` instead of the sense for an entity described as having something.
- A V到 token that has its own frame was cut back to the bare verb. PropBank has 贴到-01 (ARG1 is the place, ARG2 is the thing posted).
- A verb + directional complement written as two tokens was not merged, although PropBank has the compound (点出-01).
- For publishing verbs, the frame's location role is `:ARG1` and the published item is `:ARG2`. The annotator used `:place` and `:ARG1`.
- The subject of "be elected" took `:ARG1` instead of the frame's `:ARG0`.

**Why.** The lookup rule exists in the instruction but was not applied fully. It also does not cover verb + complement written as separate tokens.

**Change.** Strengthen step 1 of the Chinese role-numbering rule:
- Always look up V+complement tokens (V到, V出, V上) as a whole before falling back to the bare verb.
- When the complement is a separate token, also look up the joined form, and if it has a frame, make it one concept aligned to both tokens.
- Add an explicit check: for publishing and posting verbs, the location is a numbered argument, not `:place`.
- Restate that roles are always copied from the chosen sense, including for change-of-state and election verbs.

## 4. Specific reports by a periodical were marked `habitual` (about 6 units)

**What went wrong.** Specific reporting, publishing and deleting acts, each about one particular article or event, were marked `habitual` because of the rule on "repeated activity of an institution". The gold uses `performance`.

**Change.** Narrow that rule. `habitual` applies only to the generic, regular activity of a periodical (what it publishes or covers in general). A single act tied to one specific item or occasion is `performance` when it is completed, even when the agent is a publication.

## 5. Focus and additive adverbs became nodes (about 7 units)

**What went wrong.** The annotator made nodes for "even" (甚至) and for an additive 还 linking coordinated clauses. In sentences 16–17 the gold had no node for 也. The instruction's "adverbs are nodes" rule caused this.

**Change.** Add to the no-node list (where 就 and 便 already are):
- 甚至 / *even*;
- 还 and 也 when they only link a clause to a preceding clause or sentence.

Keep 也 or 还 as `:mod` only when it scopes over an argument inside one clause. Gold practice on 也 is inconsistent: sentence 19 keeps one, so this split is a judgement call.

## 6. A means verb was kept as its own event (about 5 units)

**What went wrong.** In "靠 X 而/to achieve Y", the annotator made 靠 an event with `:manner`. The gold drops 靠 and makes X the `:reason` of Y. X's event carries `:quote` from the reporting verb, like the main content.

**Change.** Add a rule: a reliance or means verb introducing the cause of a result (靠, 凭, 借) gets no node. Its object event is `:reason` of the result event.

## 7. Compounds and word-internal structure were not split (about 6 units)

**What went wrong.** Three kinds of compound were kept whole:
- a V+人 compound for a kind of entity;
- 全 + noun;
- a V+者 agent compound outside a role construction.

The gold splits them as follows:
- V+人 → `人 :ARG1-of V-01 :aspect process`;
- 全 + noun → noun `:mod 全`;
- V+者 → `者 :ARG0-of V-0x`.

**Change.** Make the agent-noun decomposition of section 2.3 general, so it applies wherever the noun occurs. Extend it to V+人 patient compounds (written `:ARG1-of`). Split 全/各 + noun into noun `:mod`.

## 8. Purpose clause details (about 4 units)

**What went wrong.** The gold reified a 为了 clause with `have-reason-91` (not `have-purpose-91`). It gave that node no `:aspect` and no modal triple, and it re-entered the main subject as `:ARG0` of the purpose verb.

**Change.**
- Write no `:aspect` on the reified reason or purpose node, and no modal triple for it.
- When the main clause's agent is clearly the agent of the purpose verb, re-enter it there. This revises "do not re-enter into 为/为了 clauses".
- Check gold practice on which concept to use; this case shows `have-reason-91`.

## 9. Smaller structural cases (about 10 units)

- **Named event.** A named event with its year (a year + election type) is `event :name` with all words as `:op`s. It is not a 时 node plus a `date-entity`.
- **Example sentences.** A sentence opening with 如 (*for example*) that illustrates the previous sentence is rooted in `have-example-91 :ARG1 implicit-predicate :ARG2 main-event`.
- **Edge choices.**
  - The content of a publication is `:part-of` it, not `:possessor`. Extend the "Parts and media" rule to content and articles.
  - An event noun modifying a noun with 的 is `:mod`, not `:topic`.
  - A domain noun before 政策 is `:topic`.
  - A named building or institution containing a group is `:place` of that group; use `building` for a legislature's seat.

## 10. Modal triples on entities

**What went wrong.** The annotator added `(author :full-affirmative <entity or pronoun>)` even when the entity was only a pseudo-conceiver of title content.

**Change.** Add a conceiver entity triple only when that entity really parents reported content (not a named title).

**Caveat.** In sentence 16 the gold put the publication as conceiver of its own reporting acts and the author as conceiver of the content. That contradicts section 5.2, so do not rewrite the rule from this one case.

## Keep these

- Person and number attributes on pronouns (100%).
- Coreference linking a pronoun to the publication entity.
- Re-entering a shared agent across coordinated verbs.
- `but-91` for 虽然…但.
- `:quant` and `:unit` for classifiers, including 1.
- The past-time anchoring of matrix events.
- `(reporting-verb :before content)` for an earlier reported event.
- The granularity rules and document format (both 100%).
</critique>

# Earlier edits
- batch 1, reflection 1 (15/15 edits applied): Temporal: one anchor per sentence, other events hang off it with :overlap, every event gets a parent, no depends-on for vague present adverbs, copular identity left out. Classifiers become :quant+:unit (also 1); adverbs are nodes. No implicit arguments. Attachment rules for aspectual-verb relatives, shared modifiers, describing clauses, part-of and medium. Aspect rules for habitual, already+stop a -> AnCast++ comp 78.4 on the batch, kept
- batch 1, reflection 2 (9/9 edits applied): Fix temporal anchoring (identity-91 root, aspectual verbs, past-time adverbs, result-now depends-on, have-degree-91 exception), superlative ARG2/ARG5 and 上 postposition, Chinese PropBank role numbering, attributes on identity-91/have-degree-91, shared-subject re-entrancy, fused negation, narrowed already+stop rule, nested and-pairs, coref checklist. -> AnCast++ comp 89.3 on the batch, kept
- batch 1, reflection 3 (7/7 edits applied): Fix misleading belonging-verb sense example and make PropBank frame lookup (whole token, all senses) mandatory; specify concept for fused negation; specific periodical entity types; explicit identity-91 temporal triples; stative verbs keep state aspect; no unexpressed non-core relations. -> AnCast++ comp 95.0 on the batch, kept
- batch 2, reflection 1 (18/18 edits applied): Reify clause-level reason/purpose (have-reason-91/have-purpose-91); split verb+量/率/额 compounds and use have-quant-91 for amounts reached; bare-verb frame for V至/V到 tokens; widen Chinese ARG0-theme warning; narrow shared-subject re-entrancy, head-noun/appositive/旗下 rules; individual-person, middle-dot op, agent nouns; fix temporal rules for absolute dates, purpose, cause/earlier relatives, depends- -> AnCast++ comp 77.9 on the batch, kept
- batch 2, reflection 2 (9/10 edits applied): Keep the reach/fall verb as root (ARG0 theme, performance) with have-quant-91 attribute-free; no sentence-initial one-arg but-91; measure-compound inner verb without aspect/modal; format/part noun as argument with publication :part-of, A in 由A改为B is ARG1; trailing contains-clauses as ARGn-of process; role noun with name -> role predicate (Chinese -91 names, per critique); nested abstract predicate -> AnCast++ comp 96.0 on the batch, kept
- batch 2, reflection 3 (10/10 edits applied): Define entities at first mention and re-enter later; part-of only (no inverse :part), for any part/format argument; enforce ARG0-only rolesets (checklist); no node for a connective linking to an earlier sentence; stricter :same-event; narrative change defaults to :overlap; trailing clause attaches to the creation verb's own argument. Trimmed intro/header text to stay under the limit. -> AnCast++ comp 98.1 on the batch, kept
- batch 3, reflection 1 (14/19 edits applied): Freed space (intro, §1 example, type list, checklist). Added: but-91 for 虽然…但; 以X为目的 as identity-91 with the noun; topic-list :example with 等 as last op; parenthetical clauses as and-conjuncts; consecutive for sequence adverbs, no node for 就/便; mandatory :quote, speaker as ARG0, saying-verb modal full-affirmative, hedged-copula complements author-affirmative; one-time claims performance; aspectual -> AnCast++ comp 77.4 on the batch, kept
- batch 3, reflection 2 (10/11 edits applied): Org/publication pronouns re-entered or coreffed to the entity; mandatory :quote with speaker entity as conceiver; first conjunct anchors a coordinated root; ceased entities past; repeated noun mentions within a sentence are new nodes + coref (fixes contradiction); reciprocal relations as and; category noun before name is concept; no modal on connectives; no coref for generic nouns; event noun unde -> AnCast++ comp 79.1 on the batch, kept
- batch 3, reflection 3 (27/27 edits applied): Fix named-being/celestial rule contradiction, same-sentence repeat coref contradiction, temporal exemption for abstract-predicate content of saying verbs, entity status of list items/idioms in value slots, topic-noun conjunct headed by its relative verb, habitual-over-process for periodical nominals, existence verbs state, null-conceiver only when used, place postpositions, possessive pronoun no : -> AnCast++ comp 84.0 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.