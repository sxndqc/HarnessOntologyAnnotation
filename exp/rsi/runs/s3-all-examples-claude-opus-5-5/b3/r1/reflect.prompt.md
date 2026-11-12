<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 29859). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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

`(c / country :name (n / name :op1 "Russia"))`: an entity-type concept, **no `:wiki`**, and `:name` with one `:opN` per word of the name.
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
- When 因为/由于 … (于是/所以/而) or 为(了) … (于是) links whole clauses as the sentence's main structure, reify it. Reason: `have-reason-91` with `:ARG1` the result and `:ARG2` the cause. Purpose: `have-purpose-91` with `:ARG1` the main event and `:ARG2` the purpose. Both get `:aspect state` and `(author :full-affirmative X)`. If both occur, have-reason-91 is the root and has-purpose-91 is its `:ARG1`. The 因为 clause (`:ARG2`, printed last) usually comes first in the text: entities first named there get their full nodes there. Keep `:reason`/`:purpose` roles only for phrase-level modifiers.

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
- Take numbered roles from the roleset you looked up, not from English habit: Chinese PropBank often makes the theme of an intransitive change verb `:ARG0` (跌-01, 达到-01). For 属-02 the thing owned is `:ARG0` and the owner `:ARG1`.
- X版面的《Y》 / Y的X版面 (a layout, edition or part of a publication): the head is 版面 with `:mod` X and `:part-of` the publication. It is the argument of the verb, not a modifier of the name. A paper's 版面 (由黑白版面改为彩色版面) is always `版面 :part-of paper`, never `paper :part 版面`.
- A clause after ， that says what the created or changed thing does (容纳…文章) is `:ARG0-of` that thing, `:aspect process`. It is not a `:purpose`, and it gives the thing no new role in the main verb.
- An appositive common noun before a name (旗下的八卦小报《X》) → the named entity `:ARG1-of (identity-91 :ARG2 noun)`. Keep all of the noun's modifiers (旗下, 八卦) on it.
- A ‑人 agent noun (创始人, 创办人) → `人 :ARG0-of (verb-00/01)`. The verb is an event with its own aspect, temporal triple and modal triple.
- Keep a verb compound as written (改为-01 with `:ARG1` old, `:ARG2` new), not 改-01 with `:source`.
- A verb + 量 measure of an entity's activity (发行量) → `量 :quant-of (发行-01 :ARG1 entity)`. The inner 发行-01 gets no `:aspect` and no modal triple; its only document-level triple is `(main :overlap 发行)`. 量 is `:ARG0` of 达到-01 and of 跌-01 (跌至). The value reached by 达到/跌至/增至 → `量 :ARG1-of (have-quant-91 :ARG2 N :unit 份)`, not a numbered argument of the verb.
- An event noun that is an argument of a verb (印刷 in 黑白印刷成了特色) keeps its PropBank sense (印刷-01) and gets aspect (a paper's practice: `habitual`), a temporal parent and a modal triple. Its modifier (黑白) is `:manner`, not `:mod`.
- An entity mentioned twice in one sentence: write its full node (name, appositive, modifiers) at its first mention in the text, and only the bare variable at the later mention, even if the later mention comes first in the graph.
- A preposition before a time (在, 于, 至, 到, 从 + 年) gets no node: the date-entity itself is the `:temporal`. Only 上 of 历史上 is a node.

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

- A typical or repeated activity of a person or institution (publishing 发行, broadcasting, selling, collecting stories 综合) is `habitual`. (Not 发行-01 under `量 :quant-of`: it has no aspect.) This holds even without a frequency word, and even with 了, when the clause describes what the entity does in general.
- 已经 + a change-of-state verb used as a modifier (已经停止发行的小报) is `state`: it is the entity's resulting condition.
- A passive naming or evaluation (被称为, 被誉为) is `performance`.
- 未经 (*without having undergone*) → `经-01`, `:aspect process`, with no `:polarity -`. Its negation is only the modal triple `(author :full-negative 经-01)`.
- A -91/-92 node that is the predicate of a clause (X 是 Y as the main or a conjoined clause, have-reason-91, have-purpose-91) gets `:aspect state` and `(author :full-affirmative X)`, and no temporal triple. A -91/-92 node inside a noun phrase gets no `:aspect`, no temporal triple and no modal triple: an appositive `:ARG1-of (identity-91 ...)`, have-org-role-91/have-rel-role-92 reifying a role noun, have-quant-91 under 量. Likewise `have-degree-91` gets no `:aspect`, no temporal triple and no modal triple. The property under its `:ARG2` (富-01) carries the aspect, the temporal triple and the modal triple.
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
- Time expressions first: a date (absolute or relative) depends on `document-creation-time`, never on `root`: `(document-creation-time :before d)` for a past date, `:after` for a future one; a relative one (*today, yesterday*,
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
- For each entity mentioned twice in a sentence, find its first mention by word position; the full node goes there (even inside the `:ARG2` of have-reason-91), every other mention is the bare variable.
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
- Aspect (4.1): 曾经拥有过 → `:aspect state`; 纸本已经停刊 → `:aspect performance`; clause-level identity-91 → `:aspect state`; appositive identity-91, have-org-role-91, have-quant-91 → no aspect, no modal triple.

- Procedure compound (3): 一般的新闻查证程序 → `(x / 程序 :ARG0-of (i / identity-91 :ARG1 (c / 查证-01 :ARG1 (n / 新闻) :aspect process)) :mod (y / 一般))`.
- Entity type (2.1): 该周报 → `(z / 周报 :mod (g / 该))`, not `newspaper`.
- have-degree-91 (4.1): no `:aspect` on it and no triples for it; only 富-01 gets `(s5main :overlap s5f)` and `(author :full-affirmative s5f)`.
- Main event (5.1): 停止发行/拥有过 → `(document-creation-time :before e)`; 被称为 → `(document-creation-time :depends-on e)`; 以…而闻名 → `(闻名 :contained 发行)`.
- 曾经 (3): 曾经拥有过 → `:temporal (c / 曾经)`.
- 未经 (4.1): `(j / 经-01 :aspect process)` with no `:polarity`, plus the triple `(author :full-negative j)`.

- Temporal (5.1): 创刊于1979年 → `(document-creation-time :before s6d)` `(s6d :overlap s6x)`; purpose 为运用 → `(创立 :overlap 运用)`; reason 因为…改为 → `(创立 :before 改为)`; 遗留下来的印刷机 used by 运用 → `(运用 :before 遗留)`; 也成了…特色 → `(prev-main :overlap 成)`.
- Reified skeleton (2.5): 因为X，为Y，于是Z → `(h / have-reason-91 :ARG1 (h2 / have-purpose-91 :ARG1 Z :ARG2 Y :aspect state) :ARG2 X :aspect state)`.
- Part and relative clause (3): 创立黑白版面的《Y》，容纳…文章 → `:ARG1 (b / 版面 :mod (h / 黑白) :part-of (n / newspaper ...) :ARG0-of (r / 容纳-01 :ARG1 ... :aspect process))`.
- Appositive / agent noun (3): 旗下的八卦小报《X》 → `(n / newspaper :ARG1-of (i / identity-91 :ARG2 (x / 小报 :mod (q / 旗下) :mod (b / 八卦))))`; 创始人 → `(p / individual-person :ARG1-of (h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))` (no aspect, no modal on h).
- Quantity (3): 发行量达到120万份 → `(d / 达到-01 :ARG0 (l / 量 :quant-of (f / 发行-01 :ARG1 n) :ARG1-of (h / have-quant-91 :ARG2 1200000 :unit (u / 份))))`.
- Event noun (3): 黑白印刷也成了特色 → `:ARG0 (y / 印刷-01 :manner (h / 黑白) :aspect habitual)` + `(成 :overlap y)` `(author :full-affirmative y)`; 1980年代 → `(d / date-entity :era 1980)`.

- Preposition (3): 至2007年 → `:temporal (d / date-entity :year 2007)`, no 至 node.
- First mention (3): 《Y》将由黑白版面改为… then Y的标准 → `改为-01 :ARG1 (b / 版面 :part-of (n / newspaper :name ... :ARG1-of (identity-91 ...)) :mod (h / 黑白))` … `(标准 :possessor n)`.
- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`. 发行量跌至8万3千份 → `(d / 跌-01 :ARG0 (l / 量 ... :ARG1-of (h / have-quant-91 :ARG2 83000 :unit (u / 份))))`.

</instruction>

# The critique (training batch 3: chinese_umr-0001, sentences 11-15; AnCast++ comprehensive 60.2)
<critique>
Below are the error patterns, most costly first. The costs come from the judge's lists above.

---

### 1. A sentence with both 虽然 and 不过: the annotator built the wrong top structure (snt12, the biggest single cost)

**Cost.** This one structure accounts for most of the snt12 losses:
- a_event_found: but-91 and identity-91 missing.
- d_core_args_abstract: about 8 units, since have-purpose-91 was matched against gold's have-mod-91.
- d_core_args_event, d_peripheral_event (`:medium`, `:quant`), modal: 6 units.
- temporal: 5 units.
- g_reentrancy: 3 units.
- The person/目的 confusion this created also spread into coreference.

**What happened.**
- 虽然 X（标语：Y），不过 Z 以博君一笑为目的 was annotated as `(have-purpose-91 :ARG1 报导 :ARG2 博君一笑-00 :concession (宣称 …))`.
- 都是真实的 became the event `真实-01`.
- The slogan in parentheses became `:medium 标语` of 宣称.

**Gold:**
```
(b / but-91
   :ARG1 (a / and
      :op1 (x / 宣称-01 :ARG0 n
              :ARG1 (h / have-mod-91 :ARG1 (r / 报导-01) :ARG2 (t / 真实) :mod 都 :quote x :aspect state))
      :op2 (i3 / identity-91 :ARG1 (y / 标语 :possessor n) :ARG2 (r2 / 报导-01 … :quote i3) :aspect state))
   :ARG2 (i2 / identity-91 :ARG1 (m / 目的 :purpose-of (r3 / 报导-01 :mod 大部分)) :ARG2 (g / 博君一笑) :aspect state))
```

**Why.** The instruction contradicts itself here. Section 2.5 maps 虽然 to `:concession` and says to reify 为(了) clauses as have-purpose-91. The but-91 rule only covers 不过 on its own. Nothing says what to do when 虽然 and 不过 come together. There is also no rule for 以 X 为目的, for 是 + adjective + 的, or for a parenthetical gloss.

**Change.** Add these rules to 2.5 and 2.3:
- "虽然/尽管 X，不过/但是/却 Y in one sentence → `but-91 :ARG1 X :ARG2 Y`, with no `:concession`."
- "以 X 为目的 / 以 X 为 Y → `identity-91 :ARG1 (目的 :purpose-of V) :ARG2 X`. Do not use have-purpose-91, which is only for 为(了) … clauses. X stays a plain concept (博君一笑), not an event."
- "X 是 Adj 的 / X 都是 Adj 的 → `have-mod-91 :ARG2 (Adj)`. The adjective has no sense and no aspect, and gets no temporal or modal triple."
- "A parenthetical 'N：Y' gloss (他们的标语：「…」) is its own clause: `identity-91 :ARG1 N :ARG2 Y`, `:aspect state`. Join it to the neighbouring clause with `and`. It is never `:medium`."
- "大部分的 N → `:mod (大部分)`, not `:quant`."

### 2. A pronoun or repeated noun for the document's main entity was given a new node, which broke coreference (j_coref_chain F 13, plus g_reentrancy and c_refer)

**What happened.**
- In snt12, 他们 (meaning the paper) became a new `person 3rd plural`. Gold re-enters the newspaper node (`标语 :possessor s12n`, `报导-01 :ARG0 s12n`).
- The annotator then chained `s12p → s13p`. Because its s12p was matched to gold's 目的, the snt13 他们 ended up in the wrong chain.
- In snt11, the bare 周报 in 周报的网络版 was made a re-entrancy to `s11z` (the named paper). Gold gives it its own node `(s11x5 / 周报)` with `(s11n2 :same-entity s11x5)`. The annotator's 仍 got matched to it.

**Why.** Section 2.1 already says a common-noun mention of a named entity is the Chinese word itself. But 5.3 says "within one sentence, coreference is a re-entrancy", and the annotator followed 5.3. Nothing says that 他们/它们 can refer to an organisation or publication.

**Change.**
- Narrow 5.3: "Re-entrancy is only for pronouns, zero arguments and 自己/其. A repeated common noun (周报, 该刊) always gets its own node, even in the same sentence, linked by a `:same-entity` triple."
- Add to 2.4: "A 他们/它们 that refers to an organisation or publication already in the same sentence is the bare variable of that node: no new person node, no refer attributes. In a later sentence, write the pronoun node and link it to the named entity: `(s12n :same-entity s13p)`."

### 3. Named-entity type and name tokens (f_name_tokens F 62, a_entity_concept, granularity)

**What happened, and the gold version:**
- **蝙蝠男孩, P'Lod (snt13).** The annotator wrote `person`. Gold has `individual-person`, which the instruction already requires; this is an instruction-following failure.
- **外星人 P'Lod (snt13).** The annotator added an appositive `identity-91 :ARG2 外星人` (an extra event plus an extra entity). Gold puts it in the name, `:op1 "外星人" :op2 "P" …`. In snt15 gold instead uses `(外星人 :name (n :op1 "P" :op2 "'" :op3 "Lod"))`. Either way, there is no identity-91.
- **希拉里·克林顿.** Gold keeps the middle dot as a token: `:op1 "希拉里" :op2 "·" :op3 "克林顿"`.
- **地球.** Gold has `(planet :name (n :op1 "地球"))`, not a common noun.

**Change.** Add to 2.2:
- "Keep 《 》 and the middle dot · as name tokens."
- "A bare category noun directly before a foreign name (外星人 P'Lod) is the node's concept or part of the name, never an appositive identity-91. Use identity-91 only when the noun has its own modifiers (旗下的八卦小报)."
- "地球 → `planet` with `:name`."
- Repeat the existing rule in the checklist: "every named person in a Chinese document is `individual-person`."

### 4. Reported content: the participants of 与 X 有关系, 后来, and :quote (snt15; also snt12)

**What happened, and the gold version:**
- **与 P'Lod 有暧昧关系.** The annotator wrote `有-01 :ARG0 Hillary :companion P'Lod`. Gold makes the 与-phrase a co-participant: `有-03 :ARG0 (and :op1 Hillary :op2 P'Lod) :ARG1 关系`.
- **…，后来还领养.** The annotator wrote `and` with `:temporal (后来)` and `:mod 还`. Gold uses `(consecutive :op1 有-03 :op2 领养)`, and drops 后来, 还 and 就 (3 extra nodes, 2 extra peripheral roles).
- **美国前第一夫人.** The annotator wrote `have-org-role-92 :ARG2 country`. Gold has `have-rel-role-91 :ARG3 (第一夫人 :mod 前 :place (country "美国"))`: first lady is a relational role, not an organisational title.
- **:quote.** Gold marks every quoted or reported clause with `:quote <reporting event>` (宣称, 指, the slogan). The annotator never used it, which cost 4 g_reentrancy units.

**Change.**
- Add to section 3: "与/和/跟 X 有 关系/联系 → `有-03 :ARG0 (and :op1 subject :op2 X)`."
- Add: "Two clauses joined by 后来/然后/接着 → `(consecutive :op1 … :op2 …)`. The connective gets no node."
- Make the existing "never drop" list explicit that it covers only 已经, 都, 也, 仍, 还 in ordinary assertions. Within consecutive, 还 and 后来 are absorbed, and the discourse particle 就 gets no node.
- Add: "第一夫人 / 夫人 → have-rel-role. The country is `:place` of the role noun."
- Turn the `:quote` remark into a rule: "the content clause of 宣称/指/说, and a quoted slogan, get `:quote <reporting event or identity node>`."

### 5. Aspect and argument choices that override the "institution's activity = habitual" rule (c_aspect F 74, core args)

**What happened, and the gold version:**
- **发行 under 停止.** Gold has `:aspect process`, with `:ARG0` the company (re-entrancy). The annotator wrote habitual and gave no ARG0.
- **继续 生存.** Gold has `继续-01 :ARG0 网络版 :ARG1 (生存-01 :ARG0 网络版 :aspect state)`. 生存 is a state, and the subject is ARG0 of both verbs. PropBank 继续-01 has ARG0 = agent.
- **甚至创造出.** Gold has performance (a completed result marked by 出). The annotator wrote habitual.
- **活动 (snt14).** Gold has activity.

**Change.** Add to 4.1:
- "An event noun that is the complement of an aspectual verb (停止/开始/继续 + N的发行) is `process`. The agent of the aspectual verb is re-entered as the noun's ARG0."
- "Under 继续, the subject is ARG0 of both 继续-01 and the inner verb."
- "Verb + resultative complement (创造出, 做成) for a past action → `performance`, even in a habitual context."
- "生存, 存在 → `state`."

### 6. 有 used to list examples, and 出现 roles (snt13)

**What happened, and the gold version:**
- **题材有 A、B…等.** The annotator wrote `有-07`. Gold has no 有 event: `报导-01 :ARG1 (题材 :example (and … 等))`, and the 报导 clause becomes the main event and temporal anchor. That anchor change is also why the snt13 temporal triples failed.
- **在新闻中重复出现的人物.** Gold has `人物 :ARG0-of (出现-01 :ARG1 (中 :op1 新闻) :frequency 重复)`. The annotator wrote ARG1 人物, ARG0 新闻, and `:mod 重复`.

**Change.**
- Add: "N 有 A、B、C 等 that lists the members of N → `N :example (and …)`, no 有 node."
- Add: "重复/经常/多次 → `:frequency`."
- Add: "For 出现-01, follow the gold usage: the thing that appears is ARG0, and the 在…中 location is ARG1 `(中 :op1 …)`." This is the reverse of what the PropBank labels (ARG0 location, ARG1 theme) suggest, so it needs to be stated outright, as was done for 属-02.

### 7. The superlative 其中最大宗 (snt14)

**What happened, and the gold version:**
- The annotator wrote `thing :ARG1-of (have-degree-91 :ARG2 大宗 :ARG3 最) :mod 其中`, plus the verb `算-01`.
- Gold has `算是-01` (it is in PropBank, so the instruction's "keep the compound as written" rule applied) and `implicit-argument :unit 宗 :ARG1-of (have-degree-91 … :ARG5 其中)`.
- The full guideline gives have-degree-91 ARG5 = the reference superset.

**Change.**
- Add to 4.2: "其中/之中 with a superlative is `:ARG5` of have-degree-91, not `:mod`."
- Add: "A headless superlative (最大宗) has an `implicit-argument` head, and its classifier is `:unit`."
- Restate in the PropBank step: "look up the compound first (算是, 改为) and use it if it exists."

### 8. Smaller items
- **母公司.** Gold splits it into `公司 :mod 母`.
- **Event nodes in s12 temporal.** Do not give temporal or modal triples to non-event nodes (真实, 博君一笑, 中).
- **Reported content in modal.** Gold adds `(speaker :full-affirmative content)` alongside the author triples. The instruction already says this; the annotator only half did it, giving the speaker the content of 宣称 but not the slogan's content.
- **Coreference across reported sentences.** Do not add a `:subset-of` triple without a clear set (the snt14 → snt13 题材 link was counted extra).

### What to keep
The instruction is working in these places and should stay as it is:
- **Format and attributes:** document format (k 100) and other attributes (100).
- **Title marks:** 《 》 as name tokens, as in the 世界新闻周报 name.
- **but-91 in a plain X，不过Y sentence:** correct in snt11.
- **Dates:** the date-entity as `:temporal` with `(document-creation-time :before d)(d :overlap main)`.
- **Dependent events:** anchored to the main event in snt11 (all temporal triples correct).
- **Aspect choices:** performance for 停止了 and 宣称, state for 有 and 算是.
- **Frequency:** `:frequency 经常`.
- **Modal strength:** `neutral-affirmative` for 可算是.
- **Superlative signal:** reifying 最 with have-degree-91.
- **Modal format:** the `(root :modal author)` skeleton.
</critique>

# Earlier edits
- batch 1, reflection 1 (11/11 edits applied): Fix classifier rule (keep 一份/一个 as :quant+:unit), title marks as name tokens, but-91 :ARG1/:ARG2, 由于→:reason, 以X而Y→:reason, non-core role rules (:place for countries, :medium, :part-of, adverbs as :mod, shared modifiers on conjuncts, no invented arguments, 属 argument order), habitual/state/performance aspect rules, have-degree-91 for superlatives and chengyu as :mod, temporal rules (no parent for  -> AnCast++ comp 82.1 on the batch, kept
- batch 1, reflection 2 (11/11 edits applied): Temporal: parent-first and one-parent rule; every aspect-bearing event gets a parent; main event to DCT; vague present adverbs get no triple (main event depends-on DCT); corrected example. Aspect: -91 predicates are state plus modal; stative verbs stay state with 过; 已经 main predicate is performance. Implicit arguments: V1V2的N chain, :part-of only with written owner, no copied subjects, 其中 as :mod. -> AnCast++ comp 88.6 on the batch, kept
- batch 1, reflection 3 (10/10 edits applied): Add N1+V+N2 procedure compound rule (identity-91) and its temporal parent; restrict English entity types to named nodes/pronouns; have-degree-91 has no aspect/temporal/modal; resolve :before vs :depends-on for main events; 以…而闻名 → (闻名 :contained 发行); 曾经 → :temporal; 未经 without :polarity -; examples. -> AnCast++ comp 95.0 on the batch, kept
- batch 2, reflection 1 (13/13 edits applied): Fix temporal labels (date/purpose -> overlap, reason -> before, earlier participle -> before), cross-sentence anchoring for result sentences, reify sentence-level reason/purpose as have-reason-91/have-purpose-91, 版面 :part-of and relative :ARG0-of clauses, appositive identity-91, individual-person and -人 agent nouns, 发行量 + have-quant-91 pattern, restrict but-91 to intra-sentence, :era for decades,  -> AnCast++ comp 92.9 on the batch, kept
- batch 2, reflection 2 (9/9 edits applied): Clause-level vs NP-internal -91/-92 aspect/modal; no aspect on 发行 under 量; event nouns as arguments keep sense (fix 黑白印刷 example); entity full node at first textual mention, 版面 :part-of only; no node for prepositions before dates. -> AnCast++ comp 97.0 on the batch, kept
- batch 2, reflection 3 (8/8 edits applied): Dates depend on document-creation-time (not root); first-mention full node enforced via 2.5 note and checklist step; general Chinese PropBank ARG0-theme warning and 量 :ARG0 of 达到/跌; examples; trimmed obsolete :wiki note. -> AnCast++ comp 98.8 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.