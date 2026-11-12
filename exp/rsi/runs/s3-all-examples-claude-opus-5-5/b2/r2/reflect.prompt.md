<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 27736). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

# The current instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value
and document-level relation counts. Take the time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.
- Follow the examples: when a sentence has a construction an example shows, annotate it the way the
  example does.
- Do not guess when you can check: use the three tools (see Tools): search the full guidelines with
  `search_guidelines` whenever the guidelines above do not settle a case, look up every predicate in
  PropBank with `propbank_lookup` before you choose its sense and numbered roles, and look up how the gold
  data annotates a construction, a word or a relation with `search_annotations`. Call them as often as you
  need: many calls are expected.
- Before you go on to the next sentence, check the graph against the guidelines once more: every word
  that carries meaning has its concept, every event its aspect, every role the right direction; and at
  the end check that the document-level relations cover every event and entity the guidelines ask for.

## Guidelines

# UMR guidelines, abridged

A short version of the UMR 0.9 specification (`umr_guidelines.md` in this folder, umr4nlp/umr-guidelines),
for annotating Chinese and English at Stage 1 (numbered PropBank roles). It keeps what an annotator needs for
most sentences and leaves out the typological material, the fine-grained lattices, the field-linguistics
sections and most of the examples. Where the full guideline uses the older short names (`AUTH`, `DCT`,
`FullAff`, `:modstr`, `:ref-person`, `Performance`), this version uses the names of the UMR release data
(`author`, `document-creation-time`, `full-affirmative`, `:modal-strength`, `:refer-person`, `performance`).

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
variable (re-entrancy: `:ARG0 s3p` above).

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
types (`person`, `thing`, `country`, `city`, `organization`, ...). Use an English entity type only for a node with `:name`, or for a pronoun. A common-noun mention, even one that refers back to a named entity (该周报, 这家公司), is the Chinese word itself (`周报`) with its `:mod (该)`. Coreference links it to the named mention.

### 2.2 Named entities

`(c / country :name (n / name :op1 "Russia"))`: an entity-type concept, **no `:wiki`** (do not add `:wiki` in Chinese documents; the gold has none; ignore the following note on it)
(the Wikipedia title, or `-` when there is none), and `:name` with one `:opN` per word of the name.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. The title marks 《 》 around a publication's name are name tokens: they are the first and last `:opN`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. A decade (1980年代) is written `:era 1980`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
a numeral + classifier phrase is kept too, also with 一 (一份, 一个, 三本书 → `书 :quant 3 :unit (b / 本)`). A number that goes into `have-quant-91` is its `:ARG2`, and the classifier is `:unit` of have-quant-91, with no `:quant` on the unit. Check with `search_annotations` when unsure.

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
| cause, reason | `have-cause-91` / `:cause` | |

Role nouns are reified the same way: *the president of Russia* →
`(p / person :ARG1-of (h / have-org-role-92 :ARG2 (c / country ...) :ARG3 (p2 / president)))`;
*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.
In Chinese documents, a named person, or a personal pronoun for one individual (他, 她), is `individual-person`, not `person`.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91`. Both take `:ARG1` and `:ARG2`, never `:opN`. Use them only for a contrast between two clauses of the same sentence. A sentence-initial 不过/但是 that contrasts with the previous sentence gets no node, and the sentence's main verb is the root;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; 以 X 而 Y (*known for X*) → Y `:reason` X. When such a clause describes a noun (e.g. the predicate noun of a 是 sentence), attach it inside that noun as `:ARG1-of`, not as a new conjunct; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.
- When 因为/由于 … (于是/所以/而) or 为(了) … (于是) links whole clauses as the sentence's main structure, reify it. Reason: `have-reason-91` with `:ARG1` the result and `:ARG2` the cause. Purpose: `have-purpose-91` with `:ARG1` the main event and `:ARG2` the purpose. Both get `:aspect state` and `(author :full-affirmative X)`. If both occur, have-reason-91 is the root and has-purpose-91 is its `:ARG1`. Keep `:reason`/`:purpose` roles only for phrase-level modifiers.

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

Frequent choices:
- A country or region modifying a noun (美国小报, *a US paper*) → `:place`, not `:mod`.
- A channel or medium (电视, 网络, *TV*) → `:medium`.
- A version, edition or part of a publication or thing (X的纸本) → `:part-of`, not `:possessor`, but only when X is written in the phrase. 网络版 alone gets no owner.
- 其中 → `:mod (其中)` on the noun it introduces, not `:part`.
- N1 + V + N2 where N2 (程序, 过程, 制度, 方式, 手续) is the procedure that V names: `N2 :ARG0-of (identity-91 :ARG1 V)`, and N1 is the object of V (`V :ARG1 N1`), with V `:aspect process`. Do not flatten N1 and V into `:mod`s of N2. Other modifiers (一般) stay `:mod` of N2.
- Nouns run together without 、 (奇闻轶事) form their own inner `and`; 、 separates the outer conjuncts.
- Aspectual and scalar adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs 目前, 曾经, 现在, 当时 → `:temporal` on that event. Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`).
- A modifier shared by coordinated nouns goes on each conjunct, as one node re-used by re-entrancy, not on the `and` node.
- Add an implicit or re-entrant argument only when the text expresses it. Do not copy a subject or owner into another clause unless a word (自己, 其, a pronoun) refers to it.
- V1V2的N (已经停止发行的小报): N is `:ARG1-of` the inner verb, and the inner verb is `:ARG1-of` the outer verb. Do not make N an argument of the outer verb.
- Check the PropBank argument order: for 属-02 the thing owned is `:ARG0` and the owner `:ARG1`.
- X版面的《Y》 / Y的X版面 (a layout, edition or part of a publication): the head is 版面 with `:mod` X and `:part-of` the publication. It is the argument of the verb, not a modifier of the name.
- A clause after ， that says what the created or changed thing does (容纳…文章) is `:ARG0-of` that thing, `:aspect process`. It is not a `:purpose`, and it gives the thing no new role in the main verb.
- An appositive common noun before a name (旗下的八卦小报《X》) → the named entity `:ARG1-of (identity-91 :ARG2 noun)`. Keep all of the noun's modifiers (旗下, 八卦) on it.
- A ‑人 agent noun (创始人, 创办人) → `人 :ARG0-of (verb-00/01)`. The verb is an event with its own aspect, temporal triple and modal triple.
- Keep a verb compound as written (改为-01 with `:ARG1` old, `:ARG2` new), not 改-01 with `:source`.
- A verb + 量 measure of an entity's activity (发行量) → `量 :quant-of (发行-01 :ARG1 entity)`. The inner 发行-01 gets `(main :overlap 发行)` but no modal triple. The value reached by 达到/跌至/增至 → `量 :ARG1-of (have-quant-91 :ARG2 N :unit 份)`, not a numbered argument of the verb.
- A modifier of an event noun (黑白印刷) is `:manner`, not `:mod`.

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

- A typical or repeated activity of a person or institution (publishing 发行, broadcasting, selling, collecting stories 综合) is `habitual`. This holds even without a frequency word, and even with 了, when the clause describes what the entity does in general.
- 已经 + a change-of-state verb used as a modifier (已经停止发行的小报) is `state`: it is the entity's resulting condition.
- A passive naming or evaluation (被称为, 被誉为) is `performance`.
- 未经 (*without having undergone*) → `经-01`, `:aspect process`, with no `:polarity -`. Its negation is only the modal triple `(author :full-negative 经-01)`.
- `identity-91` and the other -91/-92 predicates are events too: give them `:aspect state` and a modal triple `(author :full-affirmative X)`. Only their temporal triple is left out. Exception: `have-degree-91` gets no `:aspect`, no temporal triple and no modal triple. The property under its `:ARG2` (富-01) carries the aspect, the temporal triple and the modal triple.
- Stative verbs (拥有, 有, 是, 在, 属) stay `state` even with 过, 曾经 or 了.
- 已经 + a change-of-state verb as the main predicate (纸本已经停刊) is `performance`. `state` applies only to the 的-modifier form.
- A purpose verb (为充分运用) is `activity`. A relative clause saying what a created thing does (容纳) is `process`. A participle of a completed earlier event (遗留下来的) is `performance`.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2).
- `:mode imperative` (commands, 请, 别), `:mode interrogative` (questions; the questioned argument is
  `amr-unknown`, a yes/no question gets `:polarity amr-unknown`), `:mode expressive` (interjections).
- A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91`. Its roles are `:ARG1` the entity, `:ARG2` the property, and `:ARG3` the degree (最/更, `most`/`more`).
- An adjectival chengyu before 的 (荒诞不经的内容) is a `:mod`, not an event.
- `:degree` is only for intensifiers and downtoners (*very, too*; 很, 非常, 太), as a concept:
  `:degree (v / very)`.
- `:quant` for numbers and quantifiers (`:quant 3`, `:quant (a / all)`).

## 5. Document level

The document-level annotation of sentence N is one graph `(sNs0 / sentence ...)` with up to three lists of
`(parent :relation child)` triples. The triples of sentence N have at least one node of sentence N; the
other end can be a node of an earlier sentence or a constant.

### 5.1 Temporal (`:temporal`)

A dependency structure: each event and each time expression gets **one reference time** as its parent, and
the relation says where the **child** is relative to the **parent**: **In every triple `(A :rel B)`, A is the parent and B the child; every event and time node is the child of exactly one triple.**

- `:before` (child before parent), `:after` (child after parent), `:overlap` (child and parent overlap),
  `:contained` (child inside parent), `:contains`, `:depends-on` (between time nodes).
- Constants: `document-creation-time`, `past-reference`, `present-reference`, `future-reference`, `root`.
- Time expressions first: an absolute date (*1998*) depends on `root`; a relative one (*today, yesterday*,
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`; a vague one
  (*nowadays*, 现在, 目前) gets no triple of its own (it stays `:temporal` in the graph). The sentence's main event attaches directly: `(document-creation-time :depends-on s4e)`. The sentence's other events attach to the main event: `(s4e :overlap s4e2)`. Use `past-reference` / `present-reference` / `future-reference` only for vague times not tied to the moment of writing.
- Then every event: (1) a date or period of its clause, if there is one, with `:overlap` (`(s1t :overlap s1e)`; never `:contained` here); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent.
- A purpose clause → `(main :overlap X)`. A reason or cause clause → `(main :before X)` when it happened first (the usual case), else `(main :overlap X)`. When they are reified as have-reason-91 / have-purpose-91 (2.5), the parent is the main event under `:ARG1`, and the -91 nodes get no temporal triple.
- A participle describing an earlier state of a noun (遗留下来的, 留下的) → `(V :before participle)`, where V is the event whose argument contains the noun. A ‑人 agent noun's verb (创始人 → 创始-00) → `(main :overlap verb)`.
- Annotate event–event relations only when they are clear.
- Give no temporal parent to `identity-91` or to a plain `:mod` word with no sense. Every other node with a sense and an `:aspect` gets a parent, normally `(main-event :overlap X)`. This includes the property under have-degree-91 (富-01). An event inside a noun takes as parent the event whose argument contains it (未经…查证程序 → `(经-01 :overlap 查证-01)`), not the sentence's main event.
- Anchor each sentence's main event to `document-creation-time`. Use `:before` when it is clearly past (了, 过, 曾经, 已经停止). Use `:depends-on` when it is a current state, or a naming or evaluation that still holds (目前…, 被称为, 被誉为). Do not anchor it to an event of an earlier sentence unless a word (然后, 之后, 同时, 也) marks that relation. A sentence that states the result or a feature of the event just narrated (也成了…特色) → `(previous-main-event :overlap X)`.
- Within a sentence, anchor the dependent events (relative clauses, a second conjunct) to the sentence's main anchoring event, not each to `document-creation-time`. Example (main event 发行 s1f, dependents 停止 s1s and 报导 s1b): `(document-creation-time :before s1f)`, `(s1f :overlap s1s)`, `(s1f :overlap s1b)`. The main event is always the parent (first element).
- 以 X 而闻名: the reputation state 闻名 is the parent of the entity's habitual event, `(闻名 :contained 发行)`. 闻名 itself gets no parent.

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
  constants `purpose` and `have-condition` as parents of their events.
- In the sentence graph, write the strength of an event that is not `full-affirmative` from the author as
  `:modal-strength <value>` too (the scorers move it to the document level).

### 5.3 Coreference (`:coref`)

- `(earlier :same-entity later)`: two mentions of the same entity — a pronoun and its antecedent, a repeated
  name, a definite description. Link each mention to its closest earlier mention, earlier one first;
  link entity nodes, never `name` nodes.
- `(earlier :same-event later)`: two mentions of the same event. Use it only when the participants are the same. *The paper stopped publishing* and *its print edition stopped* are different events.
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Link the document's participant chains. Do not link a country or place name used only as a modifier (`:place` of a noun, the 美国 of 美国历史) to another such mention.
- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect`; negated events have `:polarity -`.
- Every event and time expression has a temporal parent; every event has a modal parent.
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.
- No argument or `:possessor` that the text does not express: no subject copied onto a purpose verb, and no owner added to a name.

## Examples

- Classifier (2.2): 一份小报 → `(x / 小报 :quant 1 :unit (u / 份))`.
- Title marks (2.2): 《世界新闻周报》 → `:name (n / name :op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》")`.
- but-91 (2.5): X，不过Y (within one sentence) → `(b / but-91 :ARG1 X :ARG2 Y)`. A sentence starting with 不过 → no but-91; root = main verb (跌-01).
- 以…而闻名 (2.5): a tabloid known for its reports → `(x / 小报 :ARG1-of (k / 闻名-01 :reason (r / 报导-01 :ARG0 x)))`.
- 由于 (2.5): 由于…内容 → `:reason (c / 内容 ...)`.
- Roles (3): 美国小报 → `:place (c / country ...)`; 电视节目 → `(p / 节目 :medium (t / 电视))`; 都经过 → `(j / 经-01 :mod (d / 都))`.
- Shared modifier (3): 奇怪的新闻与专栏 → `(a / and :op1 (n / 新闻 :mod (q / 奇怪)) :op2 (z / 专栏 :mod q))`.
- 属 (3): 属自己的节目 → `(p / 节目 :ARG0-of (s / 属-02 :ARG1 x))`.
- Aspect (4.1): 发行 (a paper's publishing) → `:aspect habitual`; 已经停止发行的 → 停止 `:aspect state`; 被称为 → `:aspect performance`.
- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.
- 历史上 (4.2): 美国历史上 → `:temporal (s / 上 :op1 (h / 历史 ...))`.
- Temporal (5.1): 目前纸本停刊，网络版继续发行 → `(document-creation-time :depends-on s4e)` `(s4e :overlap s4e2)`; no triple for 目前; no temporal triple for `identity-91`.
- Temporal (5.1): 富-01 under have-degree-91 → `(s5main :overlap s5f)`.
- V1V2的N (3): 已经停止发行的小报 → `(x / 小报 :ARG1-of (f / 发行-01 :ARG1-of (t / 停止-01 :mod (y / 已经) :aspect state) :aspect habitual))`.
- No invented owner (3): 发行网络版 → `(f / 发行-01 :ARG1 (w / 网络版))`.
- Inner and (3): 奇闻轶事、传奇与新闻 → `(a / and :op1 (a2 / and :op1 奇闻 :op2 轶事) :op2 传奇 :op3 新闻)`.
- Aspect (4.1): 曾经拥有过 → `:aspect state`; 纸本已经停刊 → `:aspect performance`; identity-91 → `:aspect state`.

- Procedure compound (3): 一般的新闻查证程序 → `(x / 程序 :ARG0-of (i / identity-91 :ARG1 (c / 查证-01 :ARG1 (n / 新闻) :aspect process)) :mod (y / 一般))`.
- Entity type (2.1): 该周报 → `(z / 周报 :mod (g / 该))`, not `newspaper`.
- have-degree-91 (4.1): no `:aspect` on it and no triples for it; only 富-01 gets `(s5main :overlap s5f)` and `(author :full-affirmative s5f)`.
- Main event (5.1): 停止发行/拥有过 → `(document-creation-time :before e)`; 被称为 → `(document-creation-time :depends-on e)`; 以…而闻名 → `(闻名 :contained 发行)`.
- 曾经 (3): 曾经拥有过 → `:temporal (c / 曾经)`.
- 未经 (4.1): `(j / 经-01 :aspect process)` with no `:polarity`, plus the triple `(author :full-negative j)`.

- Temporal (5.1): 1980年代…创刊 → `(s6d :overlap s6x)`; purpose 为运用 → `(创立 :overlap 运用)`; reason 因为…改为 → `(创立 :before 改为)`; 遗留下来的印刷机 used by 运用 → `(运用 :before 遗留)`; 也成了…特色 → `(prev-main :overlap 成)`.
- Reified skeleton (2.5): 因为X，为Y，于是Z → `(h / have-reason-91 :ARG1 (h2 / have-purpose-91 :ARG1 Z :ARG2 Y :aspect state) :ARG2 X :aspect state)`.
- Part and relative clause (3): 创立黑白版面的《Y》，容纳…文章 → `:ARG1 (b / 版面 :mod (h / 黑白) :part-of (n / newspaper ...) :ARG0-of (r / 容纳-01 :ARG1 ... :aspect process))`.
- Appositive / agent noun (3): 旗下的八卦小报《X》 → `(n / newspaper :ARG1-of (i / identity-91 :ARG2 (x / 小报 :mod (q / 旗下) :mod (b / 八卦))))`; 创始人 → `(p / individual-person :ARG1-of (h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))`.
- Quantity (3): 发行量达到120万份 → `(d / 达到-01 :ARG0 (l / 量 :quant-of (f / 发行-01 :ARG1 n) :ARG1-of (h / have-quant-91 :ARG2 1200000 :unit (u / 份))))`.
- Manner (3): 黑白印刷 → `(y / 印刷 :manner (h / 黑白))`; 1980年代 → `(d / date-entity :era 1980)`.

</instruction>

# The critique (training batch 2: chinese_umr-0001, sentences 6-10; AnCast++ comprehensive 92.9)
<critique>
Across these five sentences the annotation matches gold on almost every check. Event and entity concepts, core roles, role labels, name tokens, coreference and format all score 100. The losses come from five patterns. Four of them come straight from the instruction: one rule is too broad, two rules are missing, and two examples are wrong.

## 1. `:aspect state` and a modal triple on -91/-92 nodes inside a noun phrase (8 units, the costliest)
**Cost:** c_aspect 4 extra and i_modal 4 extra. The nodes are have-org-role-91 s7h3, identity-91 s7i (the appositive), and have-quant-91 s9h and s10h.

**Example:**
- 创始人 格内洛索·波普: the annotation had `(s7h3 / have-org-role-91 :ARG3 (s7r / 人 …) :aspect state)` plus `(author :full-affirmative s7h3)`.
- Gold has `(s7h3 / have-org-role-91 :ARG3 (s7x22 / 人 …))`, with no aspect and no modal triple.
- 发行量达到120万份: the annotation had `(s9h / have-quant-91 :ARG2 1200000 :unit (s9u / 份) :aspect state)` plus `(author :full-affirmative s9h)`. Gold has the same node with neither.

**Why:** the annotator followed the instruction. Section 4.1 says "`identity-91` and the other -91/-92 predicates are events too: give them `:aspect state` and a modal triple". That holds only for -91 nodes that are clause-level predicates. In this document those are have-reason-91 and have-purpose-91, which gold does annotate this way. Other gold documents follow the same split: a clause-level `identity-91` ("X 为 Y") has `:aspect state`, but an appositive `:ARG1-of (identity-91 :ARG2 名模)` and `have-org-role-91` have no aspect.

**Change:** replace the 4.1 bullet with something like:
> "A -91/-92 node that is the predicate of a clause (X 是 Y as the main or a conjoined clause, have-reason-91, have-purpose-91) gets `:aspect state` and `(author :full-affirmative X)`, and no temporal triple. A -91/-92 node *inside a noun phrase* gets no `:aspect`, no temporal triple and no modal triple. That covers an appositive `:ARG1-of (identity-91 …)`, `have-org-role-91`/`have-rel-role-92` that reify a role noun, and `have-quant-91` under 量."

Also fix the examples that contradict this:
- Remove "identity-91 → `:aspect state`" from the aspect example, or limit it to clause-level use.
- In the 创始人 example, state that have-org-role-91 has no aspect.

## 2. `:aspect habitual` on 发行-01 under 量 (2 units)
**Cost:** c_aspect 2 extra (s9f and s10f).

**Example:** 该刊发行量: the annotation had `(s10f / 发行-01 :ARG1 (s10k / 刊 …) :aspect habitual)`. Gold has `(s10x3 / 发行-01 :ARG1 (s10x4 / 刊 …))`, with no `:aspect`.

**Why:** the 量 rule says the inner 发行-01 "gets `(main :overlap 发行)` but no modal triple". It says nothing about aspect. Meanwhile the general rule "publishing 发行 … is habitual" applies.

**Change:** extend the rule to say: "The inner 发行-01 under `量 :quant-of` has **no `:aspect`** and no modal triple. Its only document-level relation is `(main :overlap 发行)`." Keep the temporal triple: the annotator got it right in both sentences.

## 3. 黑白印刷 annotated as an entity with no sense (4 units)
**Cost:** b_event_sense 1, c_aspect 1 missing, h_temporal 1 missing, i_modal 1 missing.

**Example:** 黑白印刷也成了该刊的特色: the annotation had `:ARG0 (s8y / 印刷 :manner (s8h / 黑白))` and no triples for it.

Gold has:
```
:ARG0 (s8x2 / 印刷-01 :manner (s8x3 / 黑白) :aspect habitual)
```
plus `(s8x :overlap s8x2)` and `(author :full-affirmative s8x2)`.

**Why:** the instruction's own example is wrong. It reads "Manner (3): 黑白印刷 → `(y / 印刷 :manner (h / 黑白))`", and the annotator copied it exactly. The rule beside it ("A modifier of an event noun … is `:manner`") calls 印刷 an event noun, but the example drops the sense.

**Change:** correct the example to `(y / 印刷-01 :manner (h / 黑白) :aspect habitual)`, with `(成 :overlap 印刷)` and `(author :full-affirmative 印刷)`. Then add a general line: "An event noun that is the subject or object of a verb (印刷 as the thing that 成了特色) keeps its PropBank sense and gets aspect, a temporal parent and a modal parent. A paper's ongoing practice is `habitual`."

## 4. A recurring named entity defined at its second mention, and its part relation inverted (4 units)
**Cost:** g_reentrancy 1 missing and 1 extra, d_peripheral_entity 1 missing and 1 extra.

**Example:** 《国家询问报》 appears twice in sentence 7: first as the paper whose 版面 is changed (将由黑白版面改为彩色版面), then as the owner of the 标准. The annotation defined the full named entity under `标准 :possessor (s7z2 / newspaper :part s7b3 :name … :ARG1-of (identity-91 …))` and pointed back to the 改为 版面 with `:part`.

Gold defines the entity at its first textual mention and reuses the variable later:
```
:ARG2 (s7x / 改为-01
    :ARG1 (s7x4 / 版面
        :part-of (s7n / newspaper :name (…"国家" "询问" "报"…)
                      :ARG1-of (s7i2 / identity-91 :ARG2 (s7x5 / 小报 :mod 旗下 :mod 八卦)))
        :mod (s7x16 / 黑白)) …)
… (s7x21 / 标准 :possessor s7n)
```

**Why:** the annotator also missed that 旗下的八卦小报《国家询问报》将由黑白版面改为… means the paper's 版面 changes. That 版面 is `:part-of` the paper, written on the 版面, as the existing rule "X版面的《Y》 / Y的X版面 … `:part-of` the publication" says. The PENMAN serialization puts `:ARG1` (创立) before `:ARG2` (改为), so the annotator wrote the entity out in full at the place that comes first in the graph. That was its later word mention.

**Change:** add two rules.
- "When an entity is mentioned twice in one sentence, write its full node (name, appositive, modifiers) where it is mentioned **first in the text**, and use the bare variable at the later mention (`标准 :possessor s7n`), even if the later mention comes earlier in the graph."
- "A 版面 or edition that belongs to a paper is always `版面 :part-of paper`, written on the 版面. Never write `paper :part 版面`."

## 5. A node for the preposition 至 before a date (2 units)
**Cost:** a_entity_found 1 extra, d_peripheral_event 1 partial.

**Example:** 至2007年: the annotation had `:temporal (s10z / 至 :op1 (s10d / date-entity :year 2007))`. Gold has `:temporal (s10d / date-entity :year 2007)`.

**Why:** the annotator likely extended the 美国历史上 → `(上 :op1 历史)` example to a preposition. Nothing in the instruction says that 在/至/到/于 + a date gets no node. The annotator did handle 在1980年代 and 于1979年 correctly.

**Change:** add "A preposition before a time (在, 于, 至, 到, 从 … 年) gets no node. The date-entity is the `:temporal` itself. The 上 of 历史上 is the only exception shown."

## What the instruction should keep
These rules produced correct annotations here and should stay:
- **Reified skeleton:** the have-reason-91 / have-purpose-91 skeleton, with aspect and modal on both.
- **Sentence 7 rules:** the 版面 `:part-of` 《世界新闻周报》 plus `:ARG0-of 容纳-01 :aspect process`, the appositive `identity-91 :ARG2 小报 :mod 旗下 :mod 八卦`, and `人 :ARG0-of 创始-00`. Also the procedure for 改为-01 with `:ARG1`/`:ARG2`.
- **Quantity:** `量 :quant-of 发行-01` with `have-quant-91 :ARG2 N :unit 份`.
- **Names and common nouns:** title marks as name tokens, no `:wiki`, `individual-person`, and 该刊 → `刊 :mod 该` rather than a newspaper type.
- **Adverbs and connectives:** 已经 and 也 as `:mod`, no node for sentence-initial 不过, and `:era 1980`.
- **Temporal anchoring:** a date anchored to `document-creation-time` and then `(date :overlap main)`, `(prev-main :overlap 成)` for 也成了, and purpose/reason/participle anchoring all matched gold (h_temporal precision 100).
- **Coreference:** the chain linking each mention to its closest earlier mention (j_coref_chain 100).
</critique>

# Earlier edits
- batch 1, reflection 1 (11/11 edits applied): Fix classifier rule (keep 一份/一个 as :quant+:unit), title marks as name tokens, but-91 :ARG1/:ARG2, 由于→:reason, 以X而Y→:reason, non-core role rules (:place for countries, :medium, :part-of, adverbs as :mod, shared modifiers on conjuncts, no invented arguments, 属 argument order), habitual/state/performance aspect rules, have-degree-91 for superlatives and chengyu as :mod, temporal rules (no parent for  -> AnCast++ comp 82.1 on the batch, kept
- batch 1, reflection 2 (11/11 edits applied): Temporal: parent-first and one-parent rule; every aspect-bearing event gets a parent; main event to DCT; vague present adverbs get no triple (main event depends-on DCT); corrected example. Aspect: -91 predicates are state plus modal; stative verbs stay state with 过; 已经 main predicate is performance. Implicit arguments: V1V2的N chain, :part-of only with written owner, no copied subjects, 其中 as :mod. -> AnCast++ comp 88.6 on the batch, kept
- batch 1, reflection 3 (10/10 edits applied): Add N1+V+N2 procedure compound rule (identity-91) and its temporal parent; restrict English entity types to named nodes/pronouns; have-degree-91 has no aspect/temporal/modal; resolve :before vs :depends-on for main events; 以…而闻名 → (闻名 :contained 发行); 曾经 → :temporal; 未经 without :polarity -; examples. -> AnCast++ comp 95.0 on the batch, kept
- batch 2, reflection 1 (13/13 edits applied): Fix temporal labels (date/purpose -> overlap, reason -> before, earlier participle -> before), cross-sentence anchoring for result sentences, reify sentence-level reason/purpose as have-reason-91/have-purpose-91, 版面 :part-of and relative :ARG0-of clauses, appositive identity-91, individual-person and -人 agent nouns, 发行量 + have-quant-91 pattern, restrict but-91 to intra-sentence, :era for decades,  -> AnCast++ comp 92.9 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.