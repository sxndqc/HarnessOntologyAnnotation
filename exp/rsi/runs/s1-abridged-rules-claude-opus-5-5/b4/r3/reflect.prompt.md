<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29986). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

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
- a locative postposition after a time or period noun (X 时, X 中, X 以来, X 上 as in *in the history of ...*) is a `:temporal` node for the postposition with the noun as `:op1`, attached to the word it scopes over (often the head noun). After a verb or clause, 时 gets no node: that event itself is the `:temporal`. After a place noun (在 N 中/上/里) the postposition node (`:op1` N) fills the verb's location role if the frame has one, else `:place`.

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
- A headline in 「 」/“ ” counted by a classifier (一篇) or set after an article noun (新闻, 文章) is `publication` + `:name`: one `:op` per token, including the quotation marks and inner punctuation, plus the classifier's `:quant`/`:unit`. Its words get no nodes, triples, `:quote` or coref. A preceding article noun takes `:ARG1-of (identity-91 :ARG2 pub :aspect state)` (author full-affirmative).
- A year + named occasion (election, games) is `event` + `:name` (all tokens as `:op`s), as `:temporal` of the verb, with no date triple.
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
1. Look it up as the whole segmented token. A two-character verb (also a V是 token like 算是) is not cut down to its first character. Use a shorter form or `-00` only if the whole token has no frame. Look up every adjective too, predicative or attributive. A framed one is `adj-01 :aspect state` with `:ARG0` the thing described (attributive: `noun :ARG0-of`; X 的 Adj-noun: `:ARG0 X`) and normal triples. `have-mod-91` is only for frameless words. If a verb + complement token (V至, V到, V为, V成) has no frame, use the bare verb's frame; the endpoint fills that frame's end-point role (or comes through `have-quant-91`, 2.2). Never use a concept whose word is not a PropBank lemma unless it is `-00`.
2. List all its senses with role descriptions (not only -01), choose the one matching the participants, and copy its role numbers (not from -01 or English habit).

Belonging senses are often not -01; there the owner is often `:ARG0` and the belonging thing `:ARG1` (a relative clause uses `:ARG0-of`/`:ARG1-of` as the frame gives the head noun). Many intransitive, change-of-state, become, reach, fall and be-elected verbs (成, 达到, 跌, 变 type) take the theme as `:ARG0` (result `:ARG1`); if the roleset lists only `:ARG0`, the single participant is `:ARG0` even when it looks like a patient. Traps: 有 has possession, existence/relationship-with, described-as-having (ability, feature) and list-inclusion senses (有-06: an entity has a feature or capacity). For 能力/机会/权利 + V, write `noun :ARG1-of (identity-91 :ARG2 V)`, not `:purpose`; V is `habitual` with `(author :neutral-affirmative V)`; count-as verbs (算是) number from `:ARG0`; publishing/posting verbs usually make the place published in a numbered argument (not `:place`).

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

**Participant roles**: the numbered roles of the predicate's roleset. Use the
inverse `:ARGn-of` for a relative clause or a participant nominal: 卖菜的人 → `(p / person :ARG0-of (m /
卖-01 :ARG1 (c / 菜)))`.

**Non-participant roles**: the closed UMR list (`:mod`, `:possessor`, `:part-of`, `:topic`, `:temporal`, `:place`, `:manner`, `:cause`, `:reason`, `:purpose`, `:condition`, `:concession`, `:duration`, `:frequency`, `:degree`, `:quant`, `:unit`, `:medium`, `:example`, `:opN`, ...; `:other-role` when none fits).

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
- `:degree` for intensifiers (很, 非常, 太) as a concept; `:quant` for numbers and quantifiers.

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
- Then pick **one anchor per sentence**: the matrix (main) event. Only the anchor is linked to the outside: (1) to a time expression (date, era) of its own clause, not one inside reported content, if there is one: `(s1t :overlap s1e)`, never `:contains`; else (2) to an event of an earlier sentence, only when the text marks the sequence (then, thereupon, 于是, 也 continuing the story): `(s2c :before s3a)`; an independent past event is not linked to a similar earlier event; else (3) to
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会. When the root is a coordination, the first conjunct is the anchor; later conjuncts `:overlap` it unless an order word says otherwise. Statements about something the text says no longer exists are past (`:before`), even when generic.
- Every other event of the sentence takes the anchor, or the event or entity-modifying event it depends on, as its parent. Use `:overlap` unless the order is explicit (`:before`/`:after`). A purpose clause is `:overlap` its main event. An earlier event in reported content is `:before` the reporting verb. A cause clause, and a relative clause describing an earlier event (left over, previously ...), is `:before` its parent, even when it is marked future (将) relative to its own time. This covers subordinate, complement, coordinated and cause clauses, relative-clause verbs, event nominals, negated events and events in noun-phrase modifiers.
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
first and last, both included). A node with no word in the sentence (a `name` node, `and` without a conjunction) is `0-0`. A named entity's type
node is aligned to the name's words.







</instruction>

# The critique (training batch 4: chinese_umr-0001, sentences 16-20; AnCast++ comprehensive 76.7)
<critique>
Below are the error patterns, most costly first. Unit counts are approximate. They come from the judge's list of units it did not count as correct.

---

### 1. Reported speech by a publication: modal parents, temporal chaining and `:quote` (about 15 units: i_modal 7, h_temporal 5, g_reentrancy 3, j_coref 2)

There are three separate problems.

**a. Modal parent of the reporting verbs versus their content.**
- **Gold:** when an expressed organization or publication reports, claims or retracts something, the gold makes that entity the conceiver of its own reporting acts (`entity :full-affirmative report-verb`). The reported content events sit directly under `author`.
- **Annotator:** it did the reverse (`author → report-verb`, `entity → content`). That is what the instruction literally says in 5.2.
- The gold pattern goes against the general guidelines and may not be consistent across documents. Before rewriting 5.2, check more gold documents (search_annotations with `:full-affirmative` + a publication speaker).
- If the pattern holds, add this rule: *"When an expressed organization or publication is the agent of a series of reporting acts, that entity is the modal parent of the reporting events; their content events are under `author`; an argument clause nested inside the content (e.g. *someone becomes X*) gets no modal triple."*

**b. Temporal chaining in coordination and inside content.** Three rules to add:
- In a multi-clause `and`, each later conjunct `:overlap`s the conjunct just before it (a chain), not the first conjunct.
- An event nominal or modifier inside a noun phrase that is under another modifier event takes that nearer event as its parent, not the clause verb.
- A means or support event introduced by 靠/凭 (*by means of X*) `:overlap`s the event it enables, not `:before`.
- Also: a date expression that appears only inside reported content gets no temporal triple at all. The instruction says the anchor must not link to such a date, but it doesn't say the date itself gets no triple.

**c. `:quote` and coreference in content.**
- `:quote` goes on every event of the reported content, including subordinate reason or means events inside it, not only the top content event.
- Two mentions of a generic kind noun (a bare plural class such as *aliens* used generically) in different clauses are separate nodes with **no** `:same-entity` link. Add this to 5.3. It also stops the core-argument mix-up that a coref link causes when nodes are matched.

### 2. Demonstrative + noun written as one token (该X, 此X, 本X) (about 9 units: a_entity_concept 4, d_peripheral 2, plus knock-on temporal and peripheral errors from bad node matching)

- **Error:** the annotator kept the token as one entity concept.
- **Gold:** splits it into the noun with the demonstrative as `:mod` (`(k / 刊 :mod (g / 该))`).
- **Cause:** 2.6 says to split "free head noun + modifier" compounds, but only gives a noun-noun example. Demonstratives are listed under "not events" and look as if they get no node at all.
- **Fix:** add *"A demonstrative + noun token (该/此/本/这 + noun) is split: noun `:mod` demonstrative. Coref links the noun node."*

### 3. Frames and role numbers not taken from the whole token (about 10 units: event concept 2, sense 2, core labels 4, core args 2)

- **Verb + complement tokens.** The annotator cut such tokens (V出, V到) down to the bare verb even though the whole token has its own frame. The instruction already says to look up the whole token, so this rule was not followed. Strengthen it: *"Check V+complement tokens (V出, V到, V上, V成) as a whole first; use the bare verb only if the whole token is not in PropBank."*
- **Publishing and posting verbs.** In these frames the place is often `:ARG1` and the thing published or posted is `:ARG2`. The annotator used the English order (thing = `:ARG1`). The current sentence ("usually make the place … a numbered argument") is too vague. Replace it with: *"For publishing/posting verbs, copy the role numbers from the frame. Typically ARG1 = location/medium and ARG2 = entity published or posted."*
- **Sense choice for common polysemous verbs.** The annotator defaulted to -01 again:
  - a "serve as / hold a position" verb should be the position-holder sense;
  - a "point out / claim" verb used for a saying should be the claim sense, not the "refer to" sense.
  
  Add: *"For a verb of saying, pick the claim/assert sense. For 'serve as [title]', pick the position-holder sense."*
- Don't chase the gold's -00 on verbs that do have a PropBank frame. It doesn't generalize.

### 4. Role noun with a possessive pronoun or owner (其编辑, *its editors*) (about 6 units: extra event and entity, core args, 4 reentrancies)

- **Error:** the annotator built `person :ARG1-of have-org-role-91 :ARG2 org :ARG3 editor`.
- **Gold:** keeps the noun itself, with the owner as `:possessor`, and re-enters that noun as the agent of later verbs.
- **Fix:** limit reification to role nouns that appear with a person's name or in an explicit title construction. Add *"A role or occupation noun with only a possessor (its/其 X, the paper's X) is the noun itself + `:possessor`, not a reified role."*

### 5. A 为了 purpose clause before the main clause (about 6 units)

- **Concept:** the gold used `have-reason-91` for 为了 + clause. Check other gold before changing the concept.
- **Aspect and modal:** the reified node had no `:aspect` and no modal triple. Change 2.5: the reified reason/purpose node gets **no `:aspect`** and **no modal triple**.
- **Purpose verb:** the purpose verb is `performance` when the main act that serves the purpose is completed (not `process`). It re-enters the shared subject as `:ARG0`. This reverses the current "do not re-enter the subject into 为/为了-purpose clauses" rule for the case where the purpose clause comes before the main clause and shares its subject.

### 6. Concessive and contrast anchoring, and stance verbs (about 4 units)

- **But-91 anchor:** when the root is `but-91`/`contrast-91`, its `:ARG1` is the anchor and `:ARG2` `:overlap`s it, as with the first conjunct of `and`.
- **Tense:** descriptions of a publication or institution that the document treats as past are `:before` the document creation time. The rule already exists (the past rule in 5.1), but it was not applied to the anchor.
- **`identity-91` aspect:** under 能力/机会 the `identity-91` gets `:aspect state`. Make this an explicit exception to "nested abstract predicates get no aspect".
- **Stance verbs:** support, oppose or favour as a stance (*X supports Y doing Z*) is `state`, not `activity`. Add these to the stative list in 4.1.

### 7. 时 after a named occasion (about 3 units)

- **Error:** the annotator built a 时 node with `:op1` the named event and gave it a date triple. It then became the anchor's parent.
- **Fix:** add to 2.1: *"After a named occasion (event + `:name`), 时 gets no node; the event is the `:temporal` of the verb directly; the verb anchors to the document creation time."*

### 8. Smaller patterns (1–3 units each)

- **Sentence-initial 如 / 例如 / *for example*:** this introduces an example of the preceding statement. Use `(h / have-example-91 :ARG1 (i / implicit-predicate) :ARG2 main-event)` as the root.
- **Event nouns that classify a noun:** an event noun classifying a noun (*a photo of a handshake*, the *X 的 photo* type) is `:mod`, not `:topic`.
- **Country with 的 on what it has or does:** X 的 N, where N is something the country owns or produces (policy, army), is `:possessor`. Restrict the `:place` rule to place names modifying a noun directly, without 的. A field noun before the head (外交政策) is `:topic`.
- **Agent nouns from a trait word:** an agent noun built from a character-trait word (好事者 type) is `state`, not `habitual`.
- **Legislature named as a location:** a named legislature used as the location of something is a `building` + `:name`. The group inside it is `:place` building. A locative noun (墙上) is linked with `:place-of` to the group, not `:possessor`.
- **Words inside a compound:** an inner verb of a decomposed V+人 compound gets a modal triple but no temporal parent.

### What to keep (these scored well)

- Publication headlines as `publication` + `:name`, with quote marks as `:op`s and `:quant`/`:unit` from the classifier.
- The appositive `identity-91` for an article noun followed by its headline.
- The `:part-of` rule linking an article to its publication.
- The 能力 + V → `identity-91` rule, with V `habitual` and author neutral-affirmative.
- The V+人 / 者 decomposition.
- `:refer-person` / `:refer-number` on pronouns, and treating a pronoun for a publication as a new node with `:same-entity` to the publication.
- `but-91` for 虽然…但.
- Named occasions as `event` + `:name`.

Abstract-predicate core arguments, the refer attributes and the other attributes all scored 100.
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
- batch 4, reflection 2 (10/13 edits applied): Add rules for quoted headlines as publication names, framed Chinese adjectives as ARG0 state events, ability/有-06, clause+时 and named occasions, 如 → have-example-91, reported-content temporal anchoring, and coref to nearest noun mention. Clause-linking reason/purpose nodes lose aspect and modal; purpose clauses re-enter the subject. Compress role lists, 4.2 and alignment text to fit the limit. -> AnCast++ comp 76.7 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.