<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29766). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

# The current instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value
and document-level relation counts. Take the time this needs:

- Read the guidelines below first and look up every decision you are unsure of; annotate a construction an example shows the way the example does.
- Before you go on to the next sentence, check the graph against the guidelines once more: every word
  that carries meaning has its concept, every event its aspect, every role the right direction; and at
  the end check that the document-level relations cover every event and entity the guidelines ask for.

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
variable (re-entrancy: `:ARG0 s3p` above). Write the full node (name, appositive, `:part-of`) at the entity's first mention in word order, even inside a subordinate clause below the root; every later mention, also inside a relative clause, is a re-entrancy.

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
- a partitive like 其中 (*among them*) is `:mod` on the noun;
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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

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

Use an abstract predicate only when there is no lexical predicate. A Chinese verb with its own PropBank frame keeps that frame and its roles. For example, a possession or belonging verb such as 属于 or 拥有 is that verb with its own fitting sense (see Chinese role numbering below), not `belong-91` / `have-91`. Do not use `:degree` on a property verb for a superlative; use `have-degree-91`. Its `:ARG2` is the property word itself. If the property is a verb with its own object (*rich in X, full of X*, 富X, 充满X), keep that verb as an event with its object (`(r / V-01 :ARG1 X :aspect state)`) and put it under `:ARG2`; do not drop the verb or put the object noun there. Use `:ARG5` only for an explicit comparison set (*among N, of all N*, 在…中); a scope like *in history* is a `:temporal` postposition node (2.1), not `:ARG5`.

**Chinese role numbering (required lookup).** For every Chinese predicate:
1. Look it up as the whole segmented token. A two-character verb is not cut down to its first character. Use a shorter form or `-00` only if the whole token has no frame. If a verb + complement token (V至, V到, V为, V成) has no frame, use the bare verb's frame; the endpoint fills that frame's end-point role (or comes through `have-quant-91`, 2.2). Never use a concept whose word is not a PropBank lemma unless it is `-00`.
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
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.
- **Clause-linking reason and purpose (overrides the phrasal rules above).** When a reason connective (因为…于是/所以, 由于…, 所以) or a purpose connective (为/为了 + a clause) links two full clauses, reify it: `(h / have-reason-91 :ARG1 effect-event :ARG2 cause-event :aspect state)`, `(h2 / have-purpose-91 :ARG1 main-event :ARG2 purpose-event :aspect state)`. The reified node is the root, or sits above the main event. It gets `(author :full-affirmative h)` but no temporal parent (see 5.1). Keep `:cause` / `:reason` / `:purpose` only when the cause or purpose is a phrase, not a full clause.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span.

A compound made of two coordinated nouns (AB where A and B are parallel nouns, e.g. a four-character N1N2 meaning *N1 and N2*) is split: `(a / and :op1 N1 :op2 N2)`. A true idiom stays one concept. When such a parallel-noun pair is one item of a longer list, nest it as its own `and` inside the outer `and`.

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
- **Role nouns with names.** A role, title or agent noun directly before or after a person's name is not an appositive `identity-91`. It is `(p / individual-person :name ... :ARG1-of (h / have-org-role-91 :ARG3 role))`, where role is e.g. `(r / 人 :ARG0-of (v / V-01))`. In Chinese documents write the role predicates as `have-org-role-91` / `have-rel-role-91`. Use appositive `identity-91` only for non-role descriptors (e.g. of a publication).
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

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

Further aspect rules:
- **Repeated activity of an institution or periodical** (publishing, broadcasting, reporting, what it regularly contains or covers) is `habitual`, even with 了 or other completion marking.
- **already + an aspectual stop verb governing another event** (已经停止 doing X) describing the current situation is `state`. A lexical termination verb with no governed event (a publication ceased, an organization dissolved) is `performance`, even with 已经.
- **Abstract predicates:** `identity-91` gets `:aspect state` only when it is the clause predicate (nested ones get none); `have-degree-91` gets no `:aspect` (the event under its `:ARG2` does).
- **A naming or evaluation passive** (*is called / is regarded as*, 被称为, 被誉为) is `performance`.
- **A negated event with a nominal event object** (没有经过X) is `process`.
- **Stative verbs keep `state`.** (see below)
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

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect` (`have-degree-91` excepted); negated events have `:polarity -` (fused negation verbs excepted).
- Every Chinese predicate uses the sense and numbered roles of its own PropBank roleset (`:ARG1` only if the roleset has one).
- Before writing `:coref`, drop every pair where both mentions are only `:place`/`:mod` modifiers.
- Every event and time expression has a temporal parent; every event has a modal parent.
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.


</instruction>

# The critique (training batch 3: chinese_umr-0001, sentences 11-15; AnCast++ comprehensive 61.3)
<critique>
The costliest problems are three Chinese constructions the instruction does not cover, or covers wrongly: a two-sided concession, a purpose stated with a noun (以 X 为 目的), and a list after "topics include". Each one breaks the graph's skeleton, and the temporal and modal errors follow from that. Next come reported speech and some missing argument re-entries, then a set of smaller rules about senses, names, coreference and adverbs.

## 1. Clause skeleton: concession, purpose stated with a noun, and lists after "include" (~35 units)
**Checks hit:** event and entity found, core arguments (event and abstract), peripheral roles, temporal (6 of the errors), modal (5).

**What went wrong:**
- **虽然…不过/但是 with both connectives.** The annotator used `:concession` (rule 2.5 says 虽然 → `:concession`). Gold uses `but-91`, with the concessive clause(s) as `:ARG1` and the main clause as `:ARG2`. A parenthetical clause added to the first part becomes a second conjunct under `and`, not a role of the claim verb.
- **以 X 为 目的.** The annotator applied the `have-purpose-91` rule (meant for 为/为了 + clause) and dropped the noun 目的. Gold keeps the noun: `(identity-91 :ARG1 (目的 :purpose-of event) :ARG2 X)`. The quantifier (大部分) goes on the event as `:mod`.
- **"The topics/contents include A, B, C 等".** The annotator made 有 the root, with the list as its argument. Gold drops the copular 有: the topic noun is the argument of the reporting verb, and the list hangs under it as `:example`. 等 is the last `:opN` of the list `and`, not a `:mod`.
- **The anchor follows the skeleton.** Because the skeleton was wrong, the anchor was wrong too, and so were most of the temporal and modal triples of those two sentences.

**Changes to the instruction:**
- In 2.5: "When the concessive clause (虽然/尽管) is answered by 但/但是/不过/却 in the main clause, use `(but-91 :ARG1 concessive :ARG2 main)`. Use `:concession` only when there is no adversative word."
- "以 X 为 目的/目标/宗旨 is a copular frame. Keep the noun: `(identity-91 :ARG1 (目的 :purpose-of E) :ARG2 X :aspect state)`. `have-purpose-91` is only for 为/为了 + clause."
- "N 有 A、B…等 where N is a topic, content or category noun listing its members: no 有/`have-91` node. Use `N :example (and :op1 A … :opk 等)`."
- "等 / *etc.* closing a list is its last `:opN`."
- "A clause in parentheses that restates or exemplifies the previous one is a conjunct under `and`. It is not `:medium` and not `:ARG1-of identity-91` on a noun."

## 2. Reported speech: `:quote`, the speaker's arguments, sense choice, and modal strength (~15 units)
**Checks hit:** reentrancy (4 missing `:quote`), sense, modal, core arguments.

**What went wrong:**
- **Wrong sense.** A passive "is alleged to" verb (被指) was given the "refer to" sense. Its "point out / claim" sense was the right one; the lookup did not compare the senses.
- **No `:quote` edges.** Gold marks each reported clause with `:quote <reporting verb>`, also when the content is not in quotation marks (claims, allegations, slogans). The annotator wrote none.
- **Content treated as a complement of a modal predicate.** The annotator gave the content `:unspecified` from the reporting verb. Gold has the content `full-affirmative` from a conceiver, and the conceiver itself gets `(author :full-affirmative conceiver)`.
- **Arguments re-entered in the wrong places.** The annotator re-entered the speaker as `:ARG0` of the reported events. Yet it left out the claim verb's own `:ARG0`, the newspaper.

**Changes to the instruction:**
- Turn the `:quote` remark in §3 into a rule: "Every content clause of a verb of saying, claiming, alleging or sloganeering gets `:quote <that verb>`."
- In 5.2: "Verbs of saying or claiming are not modal predicates. Their content is `full-affirmative` from the speaker, or from the conceiver the clause names if the speaker is unexpressed. Never use `unspecified` for them."
- "A one-time claim or statement is `performance`, even by a periodical. The habitual rule is only for publishing, reporting and covering."

## 3. Shared subjects of aspectual and nominalized verbs (~8 units)
**Checks hit:** core arguments, reentrancy, aspect.

**What went wrong:**
- **继续/停止 + verb.** 继续-01 has `:ARG0` (agent) and `:ARG1` (thing that continues). Gold puts the subject as `:ARG0` of the aspectual verb and re-enters it as `:ARG0` of the inner verb. The annotator left it only on the inner verb.
- **Stopping a nominal event (停止 X 的发行).** The stopper is also the doer of the nominal event. Gold re-enters it; the annotator did not.
- **Aspect of a nominal object.** That nominal event is `process` in gold. The annotator wrote `habitual`, because of the periodical rule.

**Changes to the instruction:**
- "With an aspectual verb (停止, 继续, 开始), the subject fills the aspectual verb's agent role from its roleset. It is also re-entered as the subject of the governed verb or nominal."
- "An event nominal that is the object of an aspectual verb is `process`. This overrides the periodical-habitual rule."
- Also qualify the existing relative-clause rule ("the noun is an argument of the inner verb only"): it holds only when the roleset lacks an agent role.

## 4. A repeated mention inside the same sentence, and compound nouns (~10 units)
**Checks hit:** granularity (4), entity concept, coreference chain (3 partial plus 1 missing).

**What went wrong:**
- **Shortened repeat of a name.** A shortened repeat of a name already given in the sentence (a bare common noun after the full title) gets its own node in gold, linked by a `:coref` triple even within the sentence. The annotator re-entered the named node, as the instruction told it to.
- **Head + modifier compounds.** 母公司 should be `公司 :mod 母`.

**Changes to the instruction:**
- "A mention written out again with its own word (a shortened name, a common noun) gets its own node, plus `(earlier :same-entity later)` even within the sentence. Re-entrancy is only for unexpressed or shared arguments and pronoun-less repeats."
- "Split head + modifier compounds whose head is a free noun (X公司, X版 where X is a modifier): `head :mod X`."

## 5. Superlatives, a missing head noun, and the whole-token lookup (~10 units)
**Checks hit:** concept, core arguments, core labels.

**What went wrong:**
- **Whole token cut short.** 算是 has its own frame (`:ARG0` the thing described, `:ARG1` what it counts as). The annotator cut it to 算, against lookup step 1.
- **Missing head noun.** In "最大 + classifier" the head noun is missing. Gold writes `implicit-argument :unit <classifier>` and makes it the argument.
- **其中 as comparison set.** In a superlative, 其中 is `:ARG5`. The instruction's "partitive 其中 is `:mod`" rule misled the annotator here.
- **Modal of the inner event.** Under a hedged copular verb (可 → `neutral-affirmative` on the verb, which the annotator got right), the inner event is still `full-affirmative` from the author, not from the copular verb.

**Changes to the instruction:**
- Add an example of an aspectual or evaluative verb + 是 (算是, 就是) that has its own frame, to stop the cut.
- "Quantifier/classifier + superlative with no head noun: `(implicit-argument :unit <classifier> :ARG1-of (have-degree-91 …))`."
- "In a superlative, 其中 / 在…中 is `:ARG5`. The `:mod` rule for 其中 is only for non-comparative partitives."
- "An event inside a hedged copula's complement keeps `(author :full-affirmative e)`."

## 6. Discourse adverbs, comitative 与, and role nouns (~12 units)
**Checks hit:** extra entities, concept, sense, core arguments.

**What went wrong:**
- **Sequence adverbs.** 后来/然后/接着 linking two clauses should be `(consecutive :op1 first :op2 later)`. The annotator kept 后来 as a `:temporal` node, plus a past-reference triple, and kept 还 as `:mod`.
- **Focus particle 就.** Gold gives it no node.
- **"A 与 B 有 relation".** Both participants form an `and` that is the subject. B is not `:companion`. The sense must also be chosen by its role description; the annotator again defaulted to -01.
- **Kinship-type titles (第一夫人, wife).** These are `have-rel-role-91`, not `have-org-role-91`. The country goes as `:place` on the role noun, not as `:ARG2`.

**Changes to the instruction:**
- Add to 2.5: "A sequence adverb between two clauses gives `consecutive` (or `after`/`before`) with the clauses as `:op1`/`:op2`. The adverb itself and the additive 还 under it get no node."
- "Discourse/focus particles 就, 便 get no node."
- "A 与/和/跟 B + symmetric predicate (have a relation, meet, marry): `(and :op1 A :op2 B)` fills the subject role."
- "Spouse titles (第一夫人, wife) are `have-rel-role-91`. A modifying country is `:place` on the role noun."

## 7. Named characters and planets, and over-linking coreference (~12 units)
**Checks hit:** name tokens, other attributes (precision 40), entity concept, coreference precision (29).

**What went wrong:**
- **Named fictional characters.** Gold treats them as `individual-person`, with any descriptor word that is part of the name inside the name ("外星人 P'Lod" → `:op1 "外星人"`). The annotator used `person`, or the kind noun as the type.
- **地球.** It should be `planet :name`.
- **Over-linked coreference.** The annotator linked generic kind nouns (aliens as a topic, then as a class) across sentences.

**Changes to the instruction:**
- "Any named individual being, including fictional characters and aliens, is `individual-person`. A descriptor written as part of the name is an `:op`."
- "Celestial bodies are `planet`/`star` + `:name`."
- "Do not link generic or kind-level mentions of a class (bare nouns in a topic list, generic subjects) by `:coref`."

## 8. Smaller rules (~6 units)
- **Locatives and frequency adverbs.** "在 N 中 + appear/exist": the postposition node `(中 :op1 N)` is the verb's location argument (`:ARG1`), not `:place`. So the postposition rule in 2.1 applies to space too, not only to time nouns. 重复/反复/经常 are `:frequency`, not `:mod`.
- **Kind modifiers on a compound topic noun.** In 时间旅行 as a list item, the noun is an entity with `:mod`. It is not an event, so it gets no aspect or document-level triples.
- **A time adverb shared by coordinated clauses.** 仍 contrasting with an earlier date gets no node. Re-enter the date as `:temporal` on the second clause.

## What to keep
- Named-entity format: Chinese name tokens split, title brackets as their own `:op`s, the middle dot as its own `:op`.
- Date entities and the anchoring of a dated sentence on its date, with `:overlap`.
- Pronoun person and number (`c_refer` 100%).
- The `but-91` structure for a contrast with 不过 between clauses.
- The appositive `identity-91` for 母公司-type descriptors.
- `have-mod-91` for a claimed property.
- Event-nominal and relative-clause attachment (`:ARG0-of`).
- `neutral-affirmative` for 可.
- The document format (`k_doc_format` 100%).
</critique>

# Earlier edits
- batch 1, reflection 1 (15/15 edits applied): Temporal: one anchor per sentence, other events hang off it with :overlap, every event gets a parent, no depends-on for vague present adverbs, copular identity left out. Classifiers become :quant+:unit (also 1); adverbs are nodes. No implicit arguments. Attachment rules for aspectual-verb relatives, shared modifiers, describing clauses, part-of and medium. Aspect rules for habitual, already+stop a -> AnCast++ comp 78.4 on the batch, kept
- batch 1, reflection 2 (9/9 edits applied): Fix temporal anchoring (identity-91 root, aspectual verbs, past-time adverbs, result-now depends-on, have-degree-91 exception), superlative ARG2/ARG5 and 上 postposition, Chinese PropBank role numbering, attributes on identity-91/have-degree-91, shared-subject re-entrancy, fused negation, narrowed already+stop rule, nested and-pairs, coref checklist. -> AnCast++ comp 89.3 on the batch, kept
- batch 1, reflection 3 (7/7 edits applied): Fix misleading belonging-verb sense example and make PropBank frame lookup (whole token, all senses) mandatory; specify concept for fused negation; specific periodical entity types; explicit identity-91 temporal triples; stative verbs keep state aspect; no unexpressed non-core relations. -> AnCast++ comp 95.0 on the batch, kept
- batch 2, reflection 1 (18/18 edits applied): Reify clause-level reason/purpose (have-reason-91/have-purpose-91); split verb+量/率/额 compounds and use have-quant-91 for amounts reached; bare-verb frame for V至/V到 tokens; widen Chinese ARG0-theme warning; narrow shared-subject re-entrancy, head-noun/appositive/旗下 rules; individual-person, middle-dot op, agent nouns; fix temporal rules for absolute dates, purpose, cause/earlier relatives, depends- -> AnCast++ comp 77.9 on the batch, kept
- batch 2, reflection 2 (9/10 edits applied): Keep the reach/fall verb as root (ARG0 theme, performance) with have-quant-91 attribute-free; no sentence-initial one-arg but-91; measure-compound inner verb without aspect/modal; format/part noun as argument with publication :part-of, A in 由A改为B is ARG1; trailing contains-clauses as ARGn-of process; role noun with name -> role predicate (Chinese -91 names, per critique); nested abstract predicate -> AnCast++ comp 96.0 on the batch, kept
- batch 2, reflection 3 (10/10 edits applied): Define entities at first mention and re-enter later; part-of only (no inverse :part), for any part/format argument; enforce ARG0-only rolesets (checklist); no node for a connective linking to an earlier sentence; stricter :same-event; narrative change defaults to :overlap; trailing clause attaches to the creation verb's own argument. Trimmed intro/header text to stay under the limit. -> AnCast++ comp 98.1 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.