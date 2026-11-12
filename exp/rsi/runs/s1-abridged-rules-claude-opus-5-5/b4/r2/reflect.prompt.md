<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29415). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

# The current instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.



## Guidelines





## 1. What a UMR is






**Variables.** Every node of sentence N has a variable starting with `s` + N (`s3d`, `s3p`), all
different within the document. A node that fills two roles is written once and then referred to by its
variable (re-entrancy). Write the full node (name, appositive, `:part-of`) at the entity's first mention in word order, even inside a subordinate clause below the root; every later pronoun or unexpressed mention, also inside a relative clause, is a re-entrancy (a repeat with its own noun: see 5.3).

## 2. Concepts

### 2.1 Events

An event is a process or a state that is **predicated**, or a process used to **refer or modify**:

- verbs used as predicates (`deny-01`, Chinese `拥有-01`);
- event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events;
- participles and relative-clause verbs;
- predicated states: adjectives and nouns in predicate position (*he is tall*, 他很高) — through the
  abstract predicates of 2.3 when there is no lexical verb.

Not events: entity nouns, frameless modifiers (demonstratives, plain nouns),
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
| X is Adj (no frame) | `have-mod-91` | `:ARG1` theme, `:ARG2` property |
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
A compound V + 人/者 noun is decomposed wherever it occurs: agent `(p / 人 :ARG0-of (v / V-01))` (`:aspect performance` when it is a role noun under `:ARG3`), patient `(p / 人 :ARG1-of (v / V-01 :aspect process))`. 全/各 + noun is noun `:mod 全`.

Use an abstract predicate only when there is no lexical predicate. A Chinese verb with its own PropBank frame keeps that frame and its roles. For example, a possession or belonging verb such as 属于 or 拥有 is that verb with its own fitting sense (see Chinese role numbering below), not `belong-91` / `have-91`. Do not use `:degree` on a property verb for a superlative; use `have-degree-91`. Its `:ARG2` is the property word itself. If the property is a verb with its own object (*rich in X, full of X*, 富X, 充满X), keep that verb as an event with its object (`(r / V-01 :ARG1 X :aspect state)`) and put it under `:ARG2`; do not drop the verb or put the object noun there. A superlative with no head noun (最大 + classifier) is `(i / implicit-argument :unit <classifier> :ARG1-of (h / have-degree-91 ...))`. Use `:ARG5` only for an explicit comparison set (*among N, of all N*, 在…中); a scope like *in history* is a `:temporal` postposition node (2.1), not `:ARG5`.

**Chinese role numbering (required lookup).** For every Chinese predicate:
1. Look it up as the whole segmented token. A two-character verb (also a V是 token like 算是) is not cut down to its first character. Use a shorter form or `-00` only if the whole token has no frame. If a verb + complement token (V至, V到, V为, V成) has no frame, use the bare verb's frame; the endpoint fills that frame's end-point role (or comes through `have-quant-91`, 2.2). Never use a concept whose word is not a PropBank lemma unless it is `-00`.
2. List all its senses with role descriptions (not only -01), choose the one matching the participants, and copy its role numbers (not from -01 or English habit).

Belonging senses are often not -01; there the owner is often `:ARG0` and the belonging thing `:ARG1` (a relative clause uses `:ARG0-of`/`:ARG1-of` as the frame gives the head noun). Many intransitive, change-of-state, become, reach, fall and be-elected verbs (成, 达到, 跌, 变 type) take the theme as `:ARG0` (result `:ARG1`); if the roleset lists only `:ARG0`, the single participant is `:ARG0` even when it looks like a patient. Traps: 有 has possession, existence/relationship-with, described-as-having (ability, feature) and list-inclusion senses; count-as verbs (算是) number from `:ARG0`; publishing/posting verbs usually make the place published in a numbered argument (not `:place`).

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
- A sequence adverb linking two clauses (后来, 然后, 接着) → `(c / consecutive :op1 first :op2 later)` (or `after`/`before`); the adverb and an additive 还 with it get no node. Focus particles 就, 便 and 甚至 (*even*) get no node, nor does 还/也 that only links a clause to an earlier clause or sentence (`:mod` only when it scopes inside one clause).
- A means verb (靠, 凭, 借 X 而/to Y) gets no node: X's event is the `:reason` of Y.
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
- **Unexpressed participants.** Fill a role (core, or `:part-of`, `:possessor`, `:mod`, ...) and re-enter a node only when a word or construction expresses that participant in that role, not when merely implied. A subject shared through a control or means frame (以 X 而 Y, *known for doing X*, *try to X*) counts as expressed: re-enter it in the embedded verb. Do not re-enter the subject into 为/为了-purpose clauses or relative clauses unless a word fills the role.
- **Aspectual verb in a relative clause.** When a head noun is modified by an aspectual verb plus another verb (*the X that stopped/began doing Y*), the noun is an argument of the inner verb only: `(x / X :ARG1-of (p / V-01 :ARG1-of (s / stop-01)))`. It is not an argument of the aspectual verb as well. Check the aspectual verb's roleset.
- **Shared modifiers.** A modifier shared by coordinated nouns (*various A and B*) goes on each conjunct by re-entrancy, not on the `and` node. Do not add `:subset` there.
- **Reciprocal relations.** In X 与/和/跟 Y 有关系/合作 type, both parties are `(a / and :op1 X :op2 Y)` in the first role, not `:companion`.
- **Describing clauses.** A clause that goes on describing the predicate noun of a copular sentence (*X is a Y, known for Z*) attaches under that noun, e.g. as `:ARG1-of`. It is not a separate top-level conjunct.
- **Trailing content clauses.** The same holds for a trailing clause without 为/为了 that tells what an object just created, named or described contains or does (…，容纳 Y). It attaches under that object (the creation verb's own argument, not its `:part-of` whole) as `:ARGn-of` with `:aspect process`. It is not `:purpose`, and it gets no re-entered subject.
- **Parts, content and media.** An edition, section, format or layout noun, or an article or content item, of a publication is `:part-of` it (never `:possessor`, never inverse `:part`). As a verb's argument the part noun is the argument, even when the publication name is the head after 的 (V了 A的《X》 → `:ARG1 (a / A :part-of x)`). A medium noun (TV, 网络) modifying a program or product is `:medium`.
- **Heads.** In N1 的 N2, and in *change from A to B* (从 A 变为 B), the grammatical head common noun is the concept. A publication or organization name modifying it is `:part-of` (a part, section or edition of it) or `:possessor`, not the head.
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
- **Generic regular activity of an institution or periodical** (what it publishes, broadcasts or covers in general) is `habitual`, even with 了 and as an event nominal (overrides `process`). A single act about one specific item or occasion is `performance` when completed, even with a publication as agent. Another event nominal for an ongoing generic activity is `activity`.
- **already + an aspectual stop verb governing another event** (已经停止 doing X) describing the current situation is `state`. A lexical termination verb with no governed event (a publication ceased, an organization dissolved) is `performance`, even with 已经.
- **Abstract predicates:** `identity-91` gets `:aspect state` only when it is the clause predicate (nested ones get none); `have-degree-91` gets no `:aspect` (the event under its `:ARG2` does).
- **A naming or evaluation passive** (*is called / is regarded as*, 被称为, 被誉为) is `performance`.
- An event noun governed by an aspectual verb (stop/start/continue + nominal) is `process`; the aspectual verb's subject is re-entered as its agent.
- **A negated event with a nominal event object** (没有经过X) is `process`.
- **Purpose verbs** naming an ongoing use are `activity`. A relative-clause verb giving what something is for or contains is `process`. A manner or property word on an event nominal is `:manner`, not `:mod`.
- **Stative verbs, continued.** Possession, belonging, existence, survival and knowing verbs stay `state` even with 了, 过, 曾经, a duration modifier or under *continue*. These markers only place the state in time for the temporal triples.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2). Fused negation (未经 type): no `:polarity -`; the concept is the verb without the negator, with its own sense and roles (no `-00` spelled with the negator). Mark only `full-negative` at the document level.
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
- Every other event of the sentence takes the anchor, or the event or entity-modifying event it depends on, as its parent. Use `:overlap` unless the order is explicit (`:before`/`:after`). A purpose clause is `:overlap` its main event. A cause clause, and a relative clause describing an earlier event (left over, previously ...), is `:before` its parent, even when it is marked future (将) relative to its own time. This covers subordinate, complement, coordinated and cause clauses, relative-clause verbs, event nominals, negated events and events in noun-phrase modifiers.
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

# The critique (training batch 4: chinese_umr-0001, sentences 16-20; AnCast++ comprehensive 49.9)
<critique>
# Review of the annotation of the tabloid passage: what to change in the instruction

The costliest errors come from three things the instruction does not cover:
- **Quoted headlines** were parsed as clauses instead of being treated as titled works.
- **Chinese adjectives** were not treated as PropBank stative verbs.
- **Some connective and postposition rules** in the instruction disagree with gold.

The patterns are listed from most to least costly.

---

### 1. A quoted headline counted as an article was parsed as a clause (largest cost)
**Pattern.** A headline in 「 」 was the object of a publishing or reporting verb and was counted by a classifier (一篇). The annotator analysed the words inside the quotes as events. It created `implicit-argument` plus `:topic` event, inner verbs, inner country and person names, `:quote` edges, and modal and temporal triples for them. It also built coreference chains through the headline's inner nouns. The same happened with a headline placed in apposition after an article noun (新闻 「…」).

Gold treats each such headline as a **`publication` named entity**:
- one `:op` per token, with the opening and closing quotation marks and the internal punctuation each as its own `:op`;
- the classifier's `:quant 1 :unit 篇` goes on that publication node;
- when the headline follows an article noun, the noun takes `:ARG1-of (identity-91 :ARG2 publication)` with `:aspect state`, and that `identity-91` gets the author modal triple.

**Cost.** f_name_tokens (3 names missing). a_entity_concept (3 wrong). About 6 extra entity nodes. Several extra or wrong core-argument, `:topic` and `:purpose` units. Extra re-entrancies (`:quote`, re-entered agent). About 8 extra modal triples, about 4 extra temporal triples, and the whole extra coreference chain (j_coref precision 56).

**Why.** Section 2.2 gives the title-bracket rule only for 《 》. The quote rule in section 3 tells the annotator to parse any reported content as events. Nothing separates a headline used as a countable object from a reported clause.

**Change.** Add to 2.2:
> A headline or title in quotation marks (「 」, “ ”) that is counted by a classifier (一篇, 一则) or set in apposition to an article noun (新闻, 文章, 报导) names a work. Write it as `publication` + `:name`, with one `:op` per token, including the quotation marks and inner punctuation. Do not analyse its words: no events, no inner names, no `:quote`, no triples, no coreference into it. Put the classifier's `:quant`/`:unit` on the publication node. An article noun before it takes `:ARG1-of (identity-91 :ARG2 publication)` (state, author full-affirmative).
>
> Only a quoted clause directly after a verb of saying, with no classifier, is reported content (section 3).

### 2. Chinese adjectives were left as plain modifiers or put under `have-mod-91`
**Pattern.** Chinese property words (ridiculous, absurd, laughable, true, prominent) were handled in two wrong ways:
- in predicate position: `have-mod-91` with the adjective as a bare `:ARG2`;
- as attributive modifiers: `:mod` with no sense.

Gold makes each one an event with its PropBank sense (`-01`). Its only role is `:ARG0`, the thing described. It has `:aspect state`, an `:overlap` temporal parent, and `(author :full-affirmative)`. An attributive one is written `noun :ARG0-of (adj-01 :aspect state)`. A property of a noun that follows 的 (the absurdity of X) is `adj-01 :ARG0 X`, not `:possessor`.

**Cost.** b_event_sense (5). c_aspect (4 missing). d_core_args (3 missing `:ARG0`, plus the wrong `have-mod-91` abstract arguments). About 5 missing temporal triples and about 5 missing modal triples. Extra `:mod` and `:possessor` edges. 1 missing re-entrancy.

**Why.** Section 2.3 says "X is Adj (no frame) → have-mod-91" and lists "plain modifiers" as non-events. The annotator did not look up adjectives in PropBank, because the required lookup reads as being for verbs only. Chinese PropBank frames most adjectives as single-argument verbs (`荒唐-01`, `显著-01`, `真实-01`, `荒谬-01` and `可笑-01` all have `ARG0` = the entity described).

**Change.** Add to the required lookup:
> Look up every Chinese adjective, predicative or attributive, in PropBank. If it has a frame, it is an event `adj-01` whose `:ARG0` is the thing described (as an attribute: `noun :ARG0-of adj-01`). Give it `:aspect state`, `:overlap` with its governing event, and an author modal triple. Use `have-mod-91` only when the word has no frame.

### 3. Ability noun with a content verb, and the 有 sense
**Pattern.** For "has the ability to V", the annotator used `有-01` with `:purpose V`, and put V's modal under 有. Gold uses `有-06` (entity described / thing it has). The ability noun takes `:ARG1-of (identity-91 :ARG2 V :aspect state)`. V is `habitual`, and the modal triple is `(author :neutral-affirmative V)`.

**Change.**
> An ability, right or opportunity noun with a content verb (能力/机会/权利 + V) links the content as `noun :ARG1-of (identity-91 :ARG2 V)`, never as `:purpose`. Give V `habitual` when it states a general capacity. Its modal parent is the author with `neutral-affirmative`, not 有.

Also add 有-06 (an entity described as having a feature or capacity) to the 有 trap list.

### 4. Sense and lemma lookup was not followed (b_event_sense 61)
**Pattern.**
- `当-01` was used where the participants called for `当-02` (position holder / position).
- `指-01` was used where they called for `指-02` (point out / claim).
- The token 贴到 was cut down to 贴, even though `贴到-01` exists. Its roles are `ARG1` = the place and `ARG2` = the thing posted, so the annotator's arguments were swapped too.
- For `刊登-01`, `ARG1` is the location and `ARG2` is the thing published. The annotator swapped them as well.

**Why.** The instruction already requires looking up the whole token and comparing all senses, but the annotator applied it to only a few verbs.

**Change.** Keep the rule and make it stricter:
> Before writing any Chinese concept, write out the token's full roleset list. The `-01` sense is chosen only if its role descriptions fit. For posting and publishing verbs, check which number holds the location and which holds the item; they are often `ARG1` = location and `ARG2` = item.

Give 当-02 and 指-02 as examples of a later sense being the correct one.

### 5. Postposition time nodes, named events and 如 "for example"
**Pattern.**
- **Named event with 时.** For a year plus a famous event plus 时, the annotator built a `时` node with an event and a separate date. Gold writes one `event` named entity: `:name` holds the year, 年 and the event noun as `:op`s, it attaches as `:temporal` on the clause's verb, and it gets no date triple.
- **Clause with 时.** For a clause plus 时, gold attaches the clause's event directly as `:temporal` and makes no 时 node.
- **Sentence-initial 如.** The annotator ignored a sentence-initial 如 (for example). Gold reifies it as `(have-example-91 :ARG1 (implicit-predicate) :ARG2 main-event)`, with no aspect and no triples.

**Cost.** Wrong and extra concepts, a missing name, wrong `:temporal` attachments, and 3 or 4 temporal units.

**Change.**
- Limit the 时/中 postposition-node rule in 2.1 to bare time or period nouns. When the item before 时 is a verb or clause, the event itself is the `:temporal`.
- A specific named occasion (a year + election, a games) is `event` + `:name`, with all its tokens as `:op`s.
- Add the 如 / 例如 opening-a-sentence rule as described above.

### 6. Temporal structure of reported and coordinated clauses (h_temporal 47)
**Pattern.**
- **Anchor on a time in the content.** The annotator anchored the reporting verb to a date inside the reported material. Gold links it `(document-creation-time :before reporting verb)`.
- **Earlier event in a claim.** A claim that refers to an earlier event (with its own earlier year) should be `(claim-verb :before content)`. The annotator instead made the content `:overlap` its date.
- **Order of a means or reason clause.** A means or reason sub-event of that content is `:overlap` with it, not `:before`.
- **Coordinated conjuncts.** Gold chains each conjunct to the previous one, not every conjunct to the first.
- **Defunct subject.** In the concessive sentence, the subject no longer exists, so gold dates its state `:before` the document creation time. The annotator used `:overlap`. The instruction already has this rule; it was not followed.

**Change.**
- Anchor rule (1) applies only to a time expression of the main clause itself. A date inside reported content does not anchor the reporting verb.
- An event in reported content that happened earlier than the report is `:before` the reporting verb.
- Make the "something that no longer exists → past" rule explicit for properties of that entity (its content, its staff).

### 7. Purpose connective 为了 + clause
**Pattern.** The annotator followed the instruction: `have-purpose-91` with `:aspect state`, an author triple, no re-entered subject, and `讽刺` as `process`. Gold uses `have-reason-91`, gives it no aspect and no modal triple, and re-enters the subject as `:ARG0` of the purpose verb. The purpose verb is `performance`, since it was realised together with the main event.

**Change.**
- The reified clause-linking node gets no `:aspect` and no modal triple.
- A purpose clause with no subject of its own re-enters the main subject; this overrides the "do not re-enter into 为了" line.
- A purpose that was carried out takes the main event's aspect.
- Gold may prefer `have-reason-91` here. This rests on one sentence, so state it with care.

### 8. Modal parents in reported content
**Pattern.** Gold is not fully consistent here.
- In the coordinated reporting sentence, gold puts the **reporting verbs** under the publication as conceiver: `(author → publication)` and `(publication → each reporting verb)`. The content events go under the author.
- In later sentences, gold gives the pronoun or publication no modal triple at all.
- The annotator added `(author :full-affirmative entity)` plus content-under-entity in every sentence, and an `:unspecified` triple from a support verb to its complement. Gold gives that complement no modal parent.

**Change (low priority).** Do not add the speaker-as-conceiver structure when the "content" is a titled work (pattern 1). Do not treat ordinary transitive verbs (support, endorse) as complement-taking modal predicates.

### 9. Coreference target and generic nouns
**Pattern.**
- The annotator linked a later full-noun mention to the immediately preceding pronoun. Gold links pronouns and later mentions to the **nearest earlier full-noun mention** of the entity.
- The annotator chained a generic kind noun ("aliens") across sentences. Gold leaves it unlinked.

**Change.** In 5.3:
> Link each new mention to the closest earlier mention that is a noun or name, not a pronoun. Generic kind nouns (bare nouns naming a class, especially inside quoted or fictional content) get no coreference.

### 10. Smaller items
- **Single-token compounds.** Keep a single segmented token as one concept (墙上, 记者团). The modifier-split and postposition rules apply only to separate tokens.
- **Named legislative bodies.** A legislative chamber named as a location is `building`.
- **Event modifying a noun with 的.** An event noun modifying a content noun with 的 (a photo of a handshake) is `:mod`, not `:topic`.
- **Owning country.** A country that owns an institutional thing (its policy) is `:possessor`. Keep `:place` for location. The instruction's "X 的 N → :place" rule is too broad.
- **Domain noun.** A domain noun on a policy-type noun (foreign policy) is `:topic`.
- **Agent noun with a disposition verb.** In a V者 agent noun with a disposition verb (好事者), the verb is `state`, not `habitual`.
- **Complement of a support verb.** A position verb under a support verb gets no `:aspect`.
- **`:quote` placement.** Gold puts `:quote` on every event of the claimed content, including its reason sub-event. Do not put `:quote` on the content of a plain report verb whose object is a titled work.

---

### Keep these (they were scored correct)
- Event and entity detection, granularity, `:refer-*` values on pronouns, and the document format. These scored 100 or close to it.
- A pronoun for a publication becomes a pronoun node linked `:same-entity` to the publication.
- `该刊` is written `刊 :mod 该`, and 内容 / 编辑 are `:part-of` / `:possessor` of the publication.
- `but-91` for 虽然…但; V者 decomposition; `全 :mod`; classifier `:quant`/`:unit`; and the `复制人` split.
- Most aspects of completed past acts (`performance`), and `(document-creation-time :before main event)` anchoring for narrative sentences.
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
- batch 4, reflection 1 (14/17 edits applied): Chinese framed adjectives/stative words become state events (have-mod-91 only frameless); quoted article titles as named publications; stronger whole-token/joined V+complement lookup and role traps; habitual narrowed to generic periodical activity; no node for 甚至/linking 还也/means verbs; general V+人/者 decomposition and 全/各 split; parts/content merged rule; compressions to stay under limit. -> AnCast++ comp 49.9 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.