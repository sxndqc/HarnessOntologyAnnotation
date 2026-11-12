<!-- system -->
You review UMR annotations made with an instruction, and say what in the instruction should change.
<!-- user -->
An annotator (a model) annotated the sentences below in Uniform Meaning Representation (UMR), following the instruction below. A judge (umrjudge) then compared its annotation with the expert gold annotation, check by check (concepts, senses, roles, attributes, named entities, reentrancy, and the document-level temporal, modal and coreference relations).

Your task: find the error patterns that cost the most, explain why they happen given the instruction (a rule that is missing, unclear, wrong, or not followed), and say what to change in the instruction to fix them so that they do not recur on other documents. Order them by cost, most costly first. Say also what the annotator got right that the instruction should keep. For each problem give one or two concrete examples from these sentences: the words, what the annotation had, and the correct annotation fragment.

You may use the tools to check the guidelines (search_guidelines), PropBank (propbank_lookup) and how other gold annotations do a case (search_annotations).

# The instruction
<instruction>
# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph, then all the document-level relations (temporal, modal, coreference) of the document. The document
is under **Input** at the end, one sentence per line.

**Make the annotation as correct as you can.** It is scored against an expert gold annotation, concept by concept and relation by relation:

- Follow the examples: when a sentence has a construction an example shows, annotate it the way the
  example does.
- Do not guess when you can check: `search_guidelines` when the guidelines do not settle a case, `propbank_lookup` for every predicate (look up the compound first: 算是, 改为; use it if it exists), `search_annotations` for how gold annotates a construction. Many calls are expected.
- Before the next sentence, recheck the graph: every meaningful word has a concept, every event an aspect, every role the right direction; at the end check the document-level relations.

## Guidelines

# UMR guidelines, abridged



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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. The title marks 《 》 around a publication's name are name tokens: they are the first and last `:opN`. So is the middle dot (希拉里·克林顿 → `:op2 "·"`). A bare category noun before a foreign name (外星人 P'Lod) is the concept (`外星人 :name …`), not an appositive identity-91. But a name listed as an example of 人物/characters (如蝙蝠男孩、外星人P'Lod) is `individual-person`, the category noun its `:op1`; do not corefer it with a `外星人 :name` mention. 地球 → `planet :name`. Types as in AMR (`company`, `newspaper`, `spaceship`, ...).

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
X (都)是 Adj 的 → `have-mod-91 :ARG1 X :ARG2 (Adj)`; the Adj has no sense, aspect or triples. A parenthetical gloss N：「Y」 → `identity-91 :ARG1 N :ARG2 Y :aspect state`, joined by `and` to the neighbouring clause, never `:medium`. 前第一夫人 → `have-rel-role-91 :ARG3 (第一夫人 :mod (前) :place country)`, not have-org-role; 前 never on the -91.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.
In Chinese documents, a named person, or a personal pronoun for one individual (他, 她), is `individual-person`, not `person`. 他们/它们 for an organisation or paper of the same sentence is that node's variable; in a later sentence it is a `person` node linked by `:same-entity`.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91`. Both take `:ARG1` and `:ARG2`, never `:opN`. Use them only for a contrast between two clauses of the same sentence. A sentence-initial 不过/但是 that contrasts with the previous sentence gets no node, and the sentence's main verb is the root; 虽然/尽管 X，不过/但是/却 Y in one sentence → `but-91 :ARG1 X :ARG2 Y`, no `:concession`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:reason`; 以 X 而 Y (*known for X*) → Y `:reason` X. When such a clause describes a noun (e.g. the predicate noun of a 是 sentence), attach it inside that noun as `:ARG1-of`, not as a new conjunct; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) without 不过/但是 → `:concession`.
- When 因为/由于 … (于是/所以/而) or 为(了) … (于是) links whole clauses as the sentence's main structure, reify it. Reason: `have-reason-91` with `:ARG1` the result and `:ARG2` the cause. Purpose: `have-purpose-91` with `:ARG1` the main event and `:ARG2` the purpose. Both get `:aspect state` and `(author :full-affirmative X)`. If both occur, have-reason-91 is the root and has-purpose-91 is its `:ARG1`. Keep `:reason`/`:purpose` roles only for phrase-level modifiers.
- 以 X 为目的 → `identity-91 :ARG1 (目的 :purpose-of V) :ARG2 X :aspect state`, not have-purpose-91; X (博君一笑) has no sense.
- 后来/然后/接着 joining clauses → `(consecutive :op1 … :op2 …)`; the connective and 还/就 there get no node.

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
- 其中 → `:mod (其中)` on the noun it introduces, not `:part`; with a superlative (其中最大宗) it is `:ARG5` of have-degree-91, and the head is `implicit-argument :unit 宗`; there have-degree-91 is `:ARG1 (大) :ARG2 (最) :ARG5 (其中)`, 大 bare, no aspect or triples.
- X 与/和/跟 Y 有关系 → `有-03 :ARG0 (and :op1 X :op2 Y)`, not `:companion`.
- N 有 A、B…等 listing N's kinds → `N :example (and …)`, no 有 node. 等 closing any list is the last `:opN` (`等`).
- 一些/许多/几 → `:quant (一些)`, not `:mod`. 重复/经常 → `:frequency`; 大部分的 N → `:mod`; 母公司 → `公司 :mod 母`.
- 出现-01: what appears is `:ARG0`, the 在…中 place `:ARG1 (中 :op1 …)`.
- N1 + V + N2 where N2 (程序, 过程, 制度, 方式, 手续) is the procedure that V names: `N2 :ARG0-of (identity-91 :ARG1 V)`, and N1 is the object of V (`V :ARG1 N1`), with V `:aspect process`. Do not flatten N1 and V into `:mod`s of N2. Other modifiers (一般) stay `:mod` of N2.
- Nouns run together without 、 (奇闻轶事) form their own inner `and`; 、 separates the outer conjuncts.
- Aspectual and scalar adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs 目前, 曾经, 现在, 当时 → `:temporal` on that event. Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`). Except: no node for 仍/还 before 继续/保持/依然, nor for 都 in 都以…为目的. A sentence-initial date over a `but-91`/`and` root is `:temporal` of each clause's event (re-used).
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

Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. The content node (of 宣称/指/说, or a slogan's content under identity-91) always gets `:quote <reporting event or identity node>`, and the speaker gets `(speaker :full-affirmative content)`. If the content is an `and`/`consecutive`, put `:quote` on each event conjunct, never on the connective. 他们的 on an event noun inside a claim adds no `:ARG0`.

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
- A single claim or announcement (宣称) is `performance`. A generic topic event noun (外星人在地球的活动) is `activity`, not habitual.
- 未经 (*without having undergone*) → `经-01`, `:aspect process`, with no `:polarity -`. Its negation is only the modal triple `(author :full-negative 经-01)`.
- A -91/-92 node that is the predicate of a clause (X 是 Y as the main or a conjoined clause, have-reason-91, have-purpose-91) gets `:aspect state` and `(author :full-affirmative X)`, and no temporal triple. A -91/-92 node inside a noun phrase gets no `:aspect`, no temporal triple and no modal triple: an appositive `:ARG1-of (identity-91 ...)`, have-org-role-91/have-rel-role-92 reifying a role noun, have-quant-91 under 量. Likewise `have-degree-91` gets no `:aspect`, no temporal triple and no modal triple. The property under its `:ARG2` (富-01) carries the aspect, the temporal triple and the modal triple.
- Stative verbs (拥有, 有, 是, 在, 属) stay `state` even with 过, 曾经 or 了.
- 已经 + a change-of-state verb as the main predicate (纸本已经停刊) is `performance`. `state` applies only to the 的-modifier form.
- A purpose verb (为充分运用) is `activity`. A relative clause saying what a created thing does (容纳) is `process`. A participle of a completed earlier event (遗留下来的) is `performance`.
- Overriding the habitual rule: an event noun under 停止/开始/继续 (停止…的发行) is `process`, with the aspectual verb's agent re-entered as its ARG0; under 继续 the subject is ARG0 of both verbs. 生存, 存在 → `state`. Verb + result complement (创造出) → `performance`.



### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2).
- `:mode imperative` (commands, 请, 别), `:mode interrogative` (questions; the questioned argument is
  `amr-unknown`, a yes/no question gets `:polarity amr-unknown`), `:mode expressive` (interjections).
- A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91`. Its roles are `:ARG1` the entity, `:ARG2` the property, and `:ARG3` the degree (最/更, `most`/`more`).
- An adjectival chengyu before 的 (荒诞不经的内容) is a `:mod`, not an event.
- `:degree` is only for intensifiers and downtoners (*very, too*; 很, 非常, 太), as a concept:
  `:degree (v / very)`.


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
- Give no temporal parent to `identity-91` or to a plain `:mod` word with no sense. Every other node with a sense and an `:aspect` gets a parent, normally `(main-event :overlap X)`. This includes the property under have-degree-91 (富-01). An event inside a noun takes as parent the event whose argument contains it (未经…查证程序 → `(经-01 :overlap 查证-01)`), not the sentence's main event.
- Anchor each sentence's main event to `document-creation-time`. Use `:before` when it is clearly past (了, 过, 曾经, 已经停止). Use `:depends-on` only with an explicit present marker (目前, 现在) or a naming still in force (被称为, 被誉为). Once the document has put its topic in the past (the paper stopped in 2007), its claims (宣称), habits (经常报导) and the author's evaluations of it (算是) are `(document-creation-time :before X)`. Do not anchor it to an event of an earlier sentence unless a word (然后, 之后, 同时, 也) marks that relation. A sentence that states the result or a feature of the event just narrated (也成了…特色) → `(previous-main-event :overlap X)`.
- Within a sentence, anchor the dependent events (relative clauses, a second conjunct) to the sentence's main anchoring event, not each to `document-creation-time`. The main event is always the parent (first element). In `(and :op1 A :op2 B)`, B's parent is A: `(A :overlap B)`, never document-creation-time. A -91 node that is the content of a reporting verb gets no temporal triple; the first event inside it takes the reporting verb as parent, and further events on the same topic (other 报导) take that event as parent.
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
  node, or an event used as conceiver). The content events of a claim (and the events of a following clause that goes on about what was claimed) get both `(author :full-affirmative X)` and `(speaker :full-affirmative X)`; an event nested inside a claimed -91 state gets only the author triple.
- An event under a modal or complement-taking predicate (*want, try, plan, decide, hope*, 想, 希望, 打算,
  决定, 需要): the predicate is asserted by the author, the complement has the predicate as parent with
  `unspecified` (or the strength the predicate implies): `(author :full-affirmative s3w)`
  `(s3w :unspecified s3g)`.
- Never write `(author … null-conceiver)`; `null-conceiver` only parents an event when no text node can. Agentless 被指/据说: the conceiver is the reported clause's subject (X与Y → its `and`): `(author :full-affirmative and)` `(and :full-affirmative E)`, no author triple on E. Purpose and condition clauses may use the
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
- Within one sentence, pronouns, zero arguments and 自己/其 are re-entrancies. A repeated noun (周报 after the named paper, 该刊) always gets its own node, even in the same sentence, linked by `:same-entity`. No `:subset-of` without a clearly stated set.

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect`; negated events have `:polarity -`.
- Every named person in a Chinese document is `individual-person`. Plain concepts with no sense (真实, 博君一笑, 中) get no temporal or modal triple.
- Every event and time expression has a temporal parent; every event has a modal parent.
- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.
- For each entity mentioned twice in a sentence, find its first mention by word position; the full node goes there (even inside the `:ARG2` of have-reason-91), every other mention is the bare variable.
- No argument or `:possessor` that the text does not express: no subject copied onto a purpose verb, and no owner added to a name.

## Examples




- 以…而闻名 (2.5): a tabloid known for its reports → `(x / 小报 :ARG1-of (k / 闻名-01 :reason (r / 报导-01 :ARG0 x)))`.


- Shared modifier (3): 奇怪的新闻与专栏 → `(a / and :op1 (n / 新闻 :mod (q / 奇怪)) :op2 (z / 专栏 :mod q))`.
- 属 (3): 属自己的节目 → `(p / 节目 :ARG0-of (s / 属-02 :ARG1 x))`.

- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.



- V1V2的N (3): 已经停止发行的小报 → `(x / 小报 :ARG1-of (f / 发行-01 :ARG1-of (t / 停止-01 :mod (y / 已经) :aspect state) :aspect habitual))`.




- Procedure compound (3): 一般的新闻查证程序 → `(x / 程序 :ARG0-of (i / identity-91 :ARG1 (c / 查证-01 :ARG1 (n / 新闻) :aspect process)) :mod (y / 一般))`.






- Temporal (5.1): 创刊于1979年 → `(document-creation-time :before s6d)` `(s6d :overlap s6x)`; purpose 为运用 → `(创立 :overlap 运用)`; reason 因为…改为 → `(创立 :before 改为)`; 遗留下来的印刷机 used by 运用 → `(运用 :before 遗留)`; 也成了…特色 → `(prev-main :overlap 成)`.
- Reified skeleton (2.5): 因为X，为Y，于是Z → `(h / have-reason-91 :ARG1 (h2 / have-purpose-91 :ARG1 Z :ARG2 Y :aspect state) :ARG2 X :aspect state)`.
- Part and relative clause (3): 创立黑白版面的《Y》，容纳…文章 → `:ARG1 (b / 版面 :mod (h / 黑白) :part-of (n / newspaper ...) :ARG0-of (r / 容纳-01 :ARG1 ... :aspect process))`.
- Appositive / agent noun (3): 旗下的八卦小报《X》 → `(n / newspaper :ARG1-of (i / identity-91 :ARG2 (x / 小报 :mod (q / 旗下) :mod (b / 八卦))))`; 创始人 → `(p / individual-person :ARG1-of (h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))` (no aspect, no modal on h).

- Event noun (3): 黑白印刷也成了特色 → `:ARG0 (y / 印刷-01 :manner (h / 黑白) :aspect habitual)` + `(成 :overlap y)` `(author :full-affirmative y)`; 1980年代 → `(d / date-entity :era 1980)`.


- First mention (3): 《Y》将由黑白版面改为… then Y的标准 → `改为-01 :ARG1 (b / 版面 :part-of (n / newspaper :name ... :ARG1-of (identity-91 ...)) :mod (h / 黑白))` … `(标准 :possessor n)`.
- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`. 发行量跌至8万3千份 → `(d / 跌-01 :ARG0 (l / 量 ... :ARG1-of (h / have-quant-91 :ARG2 83000 :unit (u / 份))))`.

- 虽然…不过 (2.5): 虽然他们宣称X（标语：Y），不过大部分报导以博君一笑为目的 → `(b / but-91 :ARG1 (a / and :op1 宣称 :op2 (i / identity-91 :ARG1 标语 :ARG2 Y)) :ARG2 (i2 / identity-91 :ARG1 (m / 目的 :purpose-of 报导) :ARG2 (g / 博君一笑)))`; that 报导 also gets `(newspaper :full-affirmative 报导)`.

- Name (2.2): 外星人P'Lod → `(x / 外星人 :name (n / name :op1 "P" :op2 "'" :op3 "Lod"))`.
- 有关系 (3): 与P'Lod有暧昧关系，后来还领养 → `(c / consecutive :op1 (y / 有-03 :ARG0 (a / and :op1 h :op2 p) :ARG1 关系) :op2 领养-01)`.

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
            :ARG1 (s16d / 当-02
                :ARG0 (s16p / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16t / 总统)
                :aspect process)
            :quote s16b
            :aspect activity)
        :temporal (s16x / 总统大选
            :temporal (s16d1 / date-entity
                :year 2000))
        :aspect performance)
    :op2 (s16c / 注销-01
        :ARG0 s16k
        :ARG1 (s16h / 照片
            :ARG1-of (s16s / 合成-01
                :aspect performance)
            :topic (s16w2 / 握手-01
                :ARG0 (s16f2 / 双方)
                :aspect process))
        :mod (s16h2 / 还)
        :aspect performance)
    :op3 (s16e / 指-02
        :ARG0 s16k
        :ARG1 (s16f / 当选-01
            :ARG0 (s16p2 / individual-person
                :name (s16n2 / name
                    :op1 "柯林顿"))
            :temporal (s16d2 / date-entity
                :year 1992)
            :mod (s16y / 也)
            :manner (s16l / 靠-01
                :ARG0 s16p2
                :ARG1 (s16bs / 背书-01
                    :ARG0 s16w
                    :aspect process)
                :aspect state)
            :quote s16e
            :aspect performance)
        :mod (s16sz / 甚至)
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16d1)
               (s16d1 :overlap s16b)
               (s16b :overlap s16z)
               (s16z :overlap s16d)
               (s16b :overlap s16c)
               (s16c :before s16s)
               (s16s :overlap s16w2)
               (s16b :overlap s16e)
               (document-creation-time :before s16d2)
               (s16d2 :overlap s16f)
               (s16f :overlap s16l)
               (s16l :overlap s16bs))
    :modal ((root :modal author)
            (author :full-affirmative s16a)
            (author :full-affirmative s16b)
            (author :full-affirmative s16k)
            (s16k :full-affirmative s16z)
            (s16k :full-affirmative s16d)
            (author :full-affirmative s16c)
            (author :full-affirmative s16s)
            (author :full-affirmative s16w2)
            (author :full-affirmative s16e)
            (s16k :full-affirmative s16f)
            (s16k :full-affirmative s16l)
            (s16k :full-affirmative s16bs)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17h / 荒唐-01
        :ARG0 (s17n / 内容
            :possessor (s17z / 周报))
        :aspect state)
    :ARG2 (s17y / 有-01
        :ARG0 (s17p / 编辑
            :possessor s17z)
        :ARG1 (s17l / 能力
            :mod (s17d / 点出-01
                :ARG0 s17p
                :ARG1 (s17a / and
                    :op1 (s17m / 荒谬-01
                        :ARG0 (s17x / 新闻
                            :mod (s17r / 真实))
                        :aspect state)
                    :op2 (s17k / 可笑-01
                        :ARG0 s17x
                        :aspect state))
                :place (s17t / 标题)
                :modal-strength neutral-affirmative
                :aspect habitual))
        :mod (s17e / 也)
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17h)
               (s17h :overlap s17y)
               (s17y :overlap s17d)
               (s17d :overlap s17m)
               (s17m :overlap s17k))
    :modal ((root :modal author)
            (author :full-affirmative s17b)
            (author :full-affirmative s17h)
            (author :full-affirmative s17y)
            (s17y :neutral-affirmative s17d)
            (s17d :full-affirmative s17m)
            (s17d :full-affirmative s17k))
    :coref ((s16k :same-entity s17z)))


################################################################################
# meta-info
# :: snt18
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 如 全世界 在 争论 复制人 的 道德 问题 时 ， 它 在 显著 位置 刊登 一篇 「 苏联 复制 一万个 希特勒 」 。

# sentence level graph:
(s18k / 刊登-01
    :ARG0 (s18t / thing
        :refer-person 3rd
        :refer-number singular)
    :ARG1 (s18w / 位置
        :mod (s18x / 显著))
    :ARG2 (s18p / 复制-01
        :ARG0 (s18s / country
            :name (s18n / name
                :op1 "苏联"))
        :ARG1 (s18h / individual-person
            :name (s18n2 / name
                :op1 "希特勒")
            :quant 10000
            :unit (s18g / 一万个))
        :quant 1
        :unit (s18u / 篇)
        :quote s18k
        :aspect performance)
    :temporal (s18z / 争论-01
        :ARG0 (s18q / 全世界)
        :ARG1 (s18w2 / 问题
            :mod (s18d / 道德)
            :topic (s18f / 复制人))
        :aspect activity)
    :aspect performance)


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18k)
               (s18k :overlap s18z)
               (s18k :overlap s18p))
    :modal ((root :modal author)
            (author :full-affirmative s18k)
            (author :full-affirmative s18z)
            (author :full-affirmative s18t)
            (s18t :full-affirmative s18p))
    :coref ((s17z :same-entity s18t)))


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
        :ARG1 (s19m / 买通-01
            :ARG0 (s19c / country
                :name (s19n / name
                    :op1 "美国"))
            :ARG1 (s19w / 外星人)
            :ARG2 (s19z / 追杀-01
                :ARG0 s19w
                :ARG1 (s19l / individual-person
                    :name (s19n2 / name
                        :op1 "宾拉登"))
                :aspect process)
            :quant 1
            :unit (s19u / 篇)
            :quote s19b
            :aspect performance)
        :mod (s19y / 也)
        :aspect performance)
    :ARG2 (s19f / 讽刺-01
        :ARG1 (s19e / 政策
            :mod (s19j / 外交)
            :possessor s19c)
        :aspect activity)
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
            (s19p :full-affirmative s19z))
    :coref ((s18t :same-entity s19p)
            (s16w :same-entity s19w)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20t / 贴到-01
    :ARG0 (s20p / 好事者)
    :ARG1 (s20q / 墙上
        :possessor (s20j / 记者团
            :mod (s20o / government-organization
                :name (s20n2 / name
                    :op1 "参议院")
                :place (s20c / country
                    :name (s20n / name
                        :op1 "美国")))))
    :ARG2 (s20x / 新闻
        :quant 1
        :unit (s20u / 篇)
        :possessor (s20k / 刊
            :mod (s20g / 该))
        :ARG1-of (s20i / identity-91
            :ARG2 (s20r / have-role-91
                :ARG1 (s20s / 参议员
                    :quant 12
                    :unit (s20u2 / 位)
                    :place s20c)
                :ARG3 (s20w / 外星人)
                :quote s20i
                :aspect state)))
    :mod (s20m / 甚至)
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20t))
    :modal ((root :modal author)
            (author :full-affirmative s20t)
            (author :full-affirmative s20k)
            (s20k :full-affirmative s20r))
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
a_event_found: R 100 / P 100 / F 100
a_event_concept: R 86 / P 86 / F 86
a_entity_found: R 100 / P 87 / F 93
a_entity_concept: R 74 / P 74 / F 74
a_granularity: R 100 / P 100 / F 100
b_event_sense: R 78 / P 78 / F 78
c_aspect: R 67 / P 73 / F 70
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 60 / P 38 / F 46
d_core_args_event: R 73 / P 84 / F 78
d_core_args_abstract: R 33 / P 67 / F 44
d_peripheral_event: R 67 / P 33 / F 44
d_peripheral_entity: R 33 / P 29 / F 31
e_core_labels: R 100 / P 100 / F 100
e_peripheral_labels: R 83 / P 83 / F 83
f_name_tokens: R 38 / P 50 / F 43
g_reentrancy: R 67 / P 40 / F 50
h_temporal: R 59 / P 52 / F 55
i_modal: R 44 / P 36 / F 40
j_coref_chain: R 100 / P 71 / F 83
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_found | extra | s16h2: - -> 还 | matches no gold node
a_entity_found | extra | s16y: - -> 也 | matches no gold node
a_entity_found | extra | s16sz: - -> 甚至 | matches no gold node
a_entity_concept | wrong | s16x7: 外星人 -> date-entity | 外星人 -> date-entity
a_entity_concept | wrong | s16e: event -> 靠 | event -> 靠
b_event_sense | wrong | s16x2: 注销 -> 注销-01 | 注销 -> 注销-01
b_event_sense | wrong | s16x15: 背书 -> 背书-01 | 背书 -> 背书-01
c_aspect | wrong | s16x6:aspect: state -> activity | state -> activity
c_aspect | extra | s16x8:aspect: - -> process | gold has no :aspect
c_aspect | wrong | s16x15:aspect: performance -> process | performance -> process
c_other_attributes | extra | s16x7:year: - -> 2000 | gold has no :year
d_core_args_event | partial | s16x6: arg0 s16x7/外星人; arg1 s16x8/当-02 -> arg0 s16x16/外星人; arg1 s16x8/当-02 | missing arg0 s16x7/外星人; extra arg0 s16x16/外星人
d_core_args_event | missing | s16x15: arg0 s16x16/外星人 -> - | missing arg0 s16x16/外星人
d_peripheral_event | wrong | s16x: temporal s16e/event -> temporal s16n3/name | missing temporal s16e/event; extra temporal s16n3/name
d_peripheral_event | extra | s16x2: - -> mod s16h2/还 (not in gold) | extra mod s16h2/还 (not in gold)
d_peripheral_event | extra | s16x3: - -> mod s16sz/甚至 (not in gold) | extra mod s16sz/甚至 (not in gold)
d_peripheral_event | partial | s16x14: temporal s16d/date-entity -> manner s16e/event; mod s16y/也 (not in gold); temporal s16d/date-entity | extra manner s16e/event; extra mod s16y/也 (not in gold)
d_peripheral_entity | wrong | s16x10: mod s16x12/握手-01 -> topic s16x12/握手-01 | mod s16x12/握手-01: predicted as topic
e_peripheral_labels | wrong | s16x10 -mod-> s16x12: mod -> topic | mod -> topic
f_name_tokens | missing | s16e: 2000 年 总统大选 -> - | the prediction has no :name
g_reentrancy | missing | s16x/报导-01 -quote-> s16x/报导-01: s16x/报导-01 -quote-> s16x/报导-01 -> - | the prediction has no such edge
g_reentrancy | missing | s16x15/背书 -quote-> s16x3/指-02: s16x15/背书 -quote-> s16x3/指-02 -> - | the prediction has no such edge
g_reentrancy | extra | s16l/靠-01 -arg0-> s16p2/individual-person: - -> s16l/靠-01 -arg0-> s16p2/individual-person | gold has no such reentrancy
g_reentrancy | extra | s16bs/背书-01 -arg0-> s16w/外星人: - -> s16bs/背书-01 -arg0-> s16w/外星人 | gold has no such reentrancy
g_reentrancy | extra | s16z/支持-01 -quote-> s16b/报导-01: - -> s16z/支持-01 -quote-> s16b/报导-01 | gold has no such reentrancy
a_event_concept | wrong | s17i2: identity -> 也 | identity -> 也
b_event_sense | wrong | s17x2: 有-06 -> 有-01 | 有-06 -> 有-01
b_event_sense | wrong | s17x11: 真实-01 -> 真实 | 真实-01 -> 真实
c_aspect | missing | s17i2:aspect: state -> - | the prediction has no :aspect
c_aspect | missing | s17x11:aspect: state -> - | the prediction has no :aspect
d_core_args_event | missing | s17x11: arg0 s17x10/新闻 -> - | missing arg0 s17x10/新闻
d_core_args_abstract | missing | s17i2: arg1 s17x6/能力; arg2 s17x7/点出-01 -> - | missing arg1 s17x6/能力; missing arg2 s17x7/点出-01
d_peripheral_event | extra | s17x2: - -> mod s17i2/identity-91 | extra mod s17i2/identity-91
d_peripheral_entity | extra | s17x3: - -> possessor s17x4/周报 | extra possessor s17x4/周报
d_peripheral_entity | missing | s17x4: part s17x3/内容 -> - | missing part s17x3/内容
d_peripheral_entity | extra | s17x6: - -> mod s17x7/点出-01 | extra mod s17x7/点出-01
d_peripheral_entity | extra | s17x10: - -> mod s17x11/真实-01 | extra mod s17x11/真实-01
a_event_concept | wrong | s18h: have-example -> name | have-example -> name
a_entity_concept | wrong | s18i2: implicit-predicate -> country | implicit-predicate -> country
a_entity_concept | wrong | s18p: publication -> individual-person | publication -> individual-person
a_entity_concept | wrong | s18x6: 世界 -> 全世界 | 世界 -> 全世界
a_entity_concept | wrong | s18x7: 全 -> name | 全 -> name
a_entity_concept | wrong | s18x10: 人 -> 复制人 | 人 -> 复制人
b_event_sense | wrong | s18x3: 显著-01 -> 显著 | 显著-01 -> 显著
c_aspect | missing | s18x3:aspect: state -> - | the prediction has no :aspect
c_aspect | wrong | s18x11:aspect: process -> performance | process -> performance
c_other_attributes | extra | s18h:op1: - -> 苏联 | gold has no :op1
c_other_attributes | wrong | s18p:quant: 1 -> 10000 | 1 -> 10000
c_other_attributes | extra | s18x7:op1: - -> 希特勒 | gold has no :op1
c_other_attributes | extra | s18x11:quant: - -> 1 | gold has no :quant
d_core_args_event | partial | s18x: arg0 s18t/thing; arg1 s18x2/位置; arg2 s18p/publication -> arg0 s18t/thing; arg1 s18x2/位置; arg2 s18x11/复制-01 | missing arg2 s18p/publication; extra arg2 s18x11/复制-01
d_core_args_event | missing | s18x3: arg0 s18x2/位置 -> - | missing arg0 s18x2/位置
d_core_args_event | wrong | s18x11: arg1 s18x10/人 -> arg0 s18i2/implicit-predicate; arg1 s18p/publication | missing arg1 s18x10/人; extra arg0 s18i2/implicit-predicate; extra arg1 s18p/publication
d_core_args_abstract | missing | s18h: arg1 s18i2/implicit-predicate; arg2 s18x/刊登-01 -> - | missing arg1 s18i2/implicit-predicate; missing arg2 s18x/刊登-01
d_peripheral_event | extra | s18x11: - -> unit s18x4/篇 | extra unit s18x4/篇
d_peripheral_entity | extra | s18x2: - -> mod s18x3/显著-01 | extra mod s18x3/显著-01
d_peripheral_entity | wrong | s18p: unit s18x4/篇 -> unit s18n/name | missing unit s18x4/篇; extra unit s18n/name
d_peripheral_entity | missing | s18x6: mod s18x7/全 -> - | missing mod s18x7/全
f_name_tokens | extra | s18i2: - -> 苏联 | gold has no :name
f_name_tokens | wrong | s18p: 「 苏联 复制 一万个 希特勒 」 -> 希特勒 | 「 苏联 复制 一万个 希特勒 」 -> 希特勒
g_reentrancy | extra | s18p/复制-01 -quote-> s18k/刊登-01: - -> s18p/复制-01 -quote-> s18k/刊登-01 | gold has no such reentrancy
a_event_concept | wrong | s19h: have-reason -> have-purpose | have-reason -> have-purpose
a_entity_found | extra | s19l: - -> individual-person | matches no gold node
a_entity_concept | wrong | s19p2: publication -> 买通 | publication -> 买通
a_entity_concept | wrong | s19x4: 篇 -> 追杀 | 篇 -> 追杀
c_aspect | extra | s19h:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s19x2:aspect: performance -> activity | performance -> activity
c_other_attributes | missing | s19x3:quant: 1 -> - | the prediction has no :quant
d_peripheral_entity | missing | s19x3: unit s19x4/篇 -> - | missing unit s19x4/篇
d_peripheral_entity | wrong | s19x5: possessor s19c/country; topic s19x6/外交 -> mod s19x6/外交 | missing possessor s19c/country; topic s19x6/外交: predicted as mod
e_peripheral_labels | wrong | s19x5 -topic-> s19x6: topic -> mod | topic -> mod
f_name_tokens | missing | s19p2: 「 美国 买通 外星人 去 追杀 宾拉登 」 -> - | the prediction has no :name
g_reentrancy | missing | s19x2/讽刺-01 -arg0-> s19p/person: s19x2/讽刺-01 -arg0-> s19p/person -> - | the prediction has no such edge
g_reentrancy | extra | s19m/买通-01 -quote-> s19b/报导-01: - -> s19m/买通-01 -quote-> s19b/报导-01 | gold has no such reentrancy
g_reentrancy | extra | s19z/追杀-01 -arg0-> s19w/外星人: - -> s19z/追杀-01 -arg0-> s19w/外星人 | gold has no such reentrancy
g_reentrancy | extra | s19e/政策 -possessor-> s19c/country: - -> s19e/政策 -possessor-> s19c/country | gold has no such reentrancy
a_event_concept | wrong | s20x3: 好事 -> have-role | 好事 -> have-role
a_entity_found | extra | s20o: - -> government-organization | matches no gold node
a_entity_found | extra | s20u2: - -> 位 | matches no gold node
a_entity_found | extra | s20m: - -> 甚至 | matches no gold node
a_entity_concept | wrong | s20x2: 者 -> 好事者 | 者 -> 好事者
a_entity_concept | wrong | s20b: building -> country | building -> country
a_entity_concept | wrong | s20p: publication -> 外星人 | publication -> 外星人
c_aspect | missing | s20i2:aspect: state -> - | the prediction has no :aspect
d_core_args_event | wrong | s20x3: arg0 s20x2/者 -> arg1 s20n2/name; arg3 s20p/publication | missing arg0 s20x2/者; extra arg1 s20n2/name; extra arg3 s20p/publication
d_core_args_abstract | partial | s20i2: arg1 s20x6/新闻; arg2 s20p/publication -> arg1 s20x6/新闻; arg2 s20x3/好事 | missing arg2 s20p/publication; extra arg2 s20x3/好事
d_peripheral_event | extra | s20x: - -> mod s20m/甚至 (not in gold) | extra mod s20m/甚至 (not in gold)
d_peripheral_entity | extra | s20x4: - -> possessor s20x5/记者团 | extra possessor s20x5/记者团
d_peripheral_entity | wrong | s20x5: place s20b/building; place s20x4/墙上 -> mod s20o/government-organization (not in gold) | missing place s20b/building; missing place s20x4/墙上; extra mod s20o/government-organization (not in gold)
d_peripheral_entity | partial | s20x6: unit s20x7/篇 -> possessor s20x8/刊; unit s20x7/篇 | extra possessor s20x8/刊
d_peripheral_entity | partial | s20x8: mod s20x9/该; part s20x6/新闻 -> mod s20x9/该 | missing part s20x6/新闻
f_name_tokens | wrong | s20b: 美国 参议院 -> 美国 | 美国 参议院 -> 美国
f_name_tokens | missing | s20p: 「 12 位 美国 参议员 是 外星人 ！ 」 -> - | the prediction has no :name
g_reentrancy | extra | s20s/参议员 -place-> s20c/country: - -> s20s/参议员 -place-> s20c/country | gold has no such reentrancy
g_reentrancy | extra | s20r/have-role-91 -quote-> s20i/identity-91: - -> s20r/have-role-91 -quote-> s20i/identity-91 | gold has no such reentrancy
h_temporal | extra | date-entity (snt16 s16d = pred s16d2): - -> document-creation-time :before date-entity (snt16 s16d = pred s16d2) | gold gives this node no temporal parent
h_temporal | extra | event (snt16 s16e = pred s16l): - -> 当选-01 «当选» (snt16 s16x14 = pred s16f) :overlap event (snt16 s16e = pred s16l) | gold gives this node no temporal parent
h_temporal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): document-creation-time :before 报导-01 «报导» (snt16 s16x = pred s16b) -> 外星人 «外星人» (snt16 s16x7 = pred s16d1) :overlap 报导-01 «报导» (snt16 s16x = pred s16b) | wrong parent and relation
h_temporal | wrong | 合成-01 «合成» (snt16 s16x11 = pred s16s): 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 合成-01 «合成» (snt16 s16x11 = pred s16s) -> 注销 «注销» (snt16 s16x2 = pred s16c) :before 合成-01 «合成» (snt16 s16x11 = pred s16s) | right parent, wrong relation
h_temporal | wrong | 当选-01 «当选» (snt16 s16x14 = pred s16f): 指-02 «指» (snt16 s16x3 = pred s16e) :before 当选-01 «当选» (snt16 s16x14 = pred s16f) -> date-entity (snt16 s16d = pred s16d2) :overlap 当选-01 «当选» (snt16 s16x14 = pred s16f) | wrong parent and relation
h_temporal | wrong | 背书 «背书» (snt16 s16x15 = pred s16bs): 当选-01 «当选» (snt16 s16x14 = pred s16f) :overlap 背书 «背书» (snt16 s16x15 = pred s16bs) -> event (snt16 s16e = pred s16l) :overlap 背书 «背书» (snt16 s16x15 = pred s16bs) | right relation, wrong parent
h_temporal | wrong | 指-02 «指» (snt16 s16x3 = pred s16e): 注销 «注销» (snt16 s16x2 = pred s16c) :overlap 指-02 «指» (snt16 s16x3 = pred s16e) -> 报导-01 «报导» (snt16 s16x = pred s16b) :overlap 指-02 «指» (snt16 s16x3 = pred s16e) | right relation, wrong parent
h_temporal | extra | 外星人 «外星人» (snt16 s16x7 = pred s16d1): - -> document-creation-time :before 外星人 «外星人» (snt16 s16x7 = pred s16d1) | gold gives this node no temporal parent
h_temporal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17r): 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17r) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | 可笑-01 «可笑» (snt17 s17x9 = pred s17k): 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 可笑-01 «可笑» (snt17 s17x9 = pred s17k) -> 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) :overlap 可笑-01 «可笑» (snt17 s17x9 = pred s17k) | right relation, wrong parent
h_temporal | extra | 复制-01 «复制» (snt18 s18x11 = pred s18p): - -> 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 复制-01 «复制» (snt18 s18x11 = pred s18p) | gold gives this node no temporal parent
h_temporal | missing | 显著-01 «显著» (snt18 s18x3 = pred s18x): 刊登-01 «刊登» (snt18 s18x = pred s18k) :overlap 显著-01 «显著» (snt18 s18x3 = pred s18x) -> - | the prediction gives this node no temporal parent
h_temporal | extra | publication (snt19 s19p2 = pred s19m): - -> 报导-01 «报导» (snt19 s19x = pred s19b) :overlap publication (snt19 s19p2 = pred s19m) | gold gives this node no temporal parent
h_temporal | extra | 篇 «一篇» (snt19 s19x4 = pred s19z): - -> publication (snt19 s19p2 = pred s19m) :overlap 篇 «一篇» (snt19 s19x4 = pred s19z) | gold gives this node no temporal parent
h_temporal | missing | 好事 «好事者» (snt20 s20x3 = pred s20r): 贴到-01 «贴到» (snt20 s20x = pred s20t) :overlap 好事 «好事者» (snt20 s20x3 = pred s20r) -> - | the prediction gives this node no temporal parent
i_modal | extra | and (snt16 s16a = pred s16a): - -> author :full-affirmative and (snt16 s16a = pred s16a) | gold gives this node no modal parent
i_modal | extra | event (snt16 s16e = pred s16l): - -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative event (snt16 s16e = pred s16l) | gold gives this node no modal parent
i_modal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) -> author :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) | right relation, wrong parent
i_modal | wrong | 当选-01 «当选» (snt16 s16x14 = pred s16f): author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16f) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16f) | right relation, wrong parent
i_modal | wrong | 背书 «背书» (snt16 s16x15 = pred s16bs): author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16bs) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16bs) | right relation, wrong parent
i_modal | wrong | 注销 «注销» (snt16 s16x2 = pred s16c): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16c) -> author :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16c) | right relation, wrong parent
i_modal | wrong | 指-02 «指» (snt16 s16x3 = pred s16e): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16e) -> author :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16e) | right relation, wrong parent
i_modal | wrong | 支持-01 «支持» (snt16 s16x6 = pred s16z): author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z) -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16z) | right relation, wrong parent
i_modal | extra | 当-02 «当» (snt16 s16x8 = pred s16d): - -> 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16d) | gold gives this node no modal parent
i_modal | extra | but-91 (snt17 s17b = pred s17b): - -> author :full-affirmative but-91 (snt17 s17b = pred s17b) | gold gives this node no modal parent
i_modal | missing | identity-91 (snt17 s17i2 = pred s17e): author :full-affirmative identity-91 (snt17 s17i2 = pred s17e) -> - | the prediction gives this node no modal parent
i_modal | missing | 真实-01 «真实» (snt17 s17x11 = pred s17r): author :full-affirmative 真实-01 «真实» (snt17 s17x11 = pred s17r) -> - | the prediction gives this node no modal parent
i_modal | partial | 点出-01 «点» (snt17 s17x7 = pred s17d): author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) [from the sentence-graph modal-strength] -> author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) [from the sentence-graph modal-strength]; 有-06 «有» (snt17 s17x2 = pred s17y) :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) | agrees on part of the relations
i_modal | wrong | 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m): author :full-affirmative 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) -> 点出-01 «点» (snt17 s17x7 = pred s17d) :full-affirmative 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) | right relation, wrong parent
i_modal | wrong | 可笑-01 «可笑» (snt17 s17x9 = pred s17k): author :full-affirmative 可笑-01 «可笑» (snt17 s17x9 = pred s17k) -> 点出-01 «点» (snt17 s17x7 = pred s17d) :full-affirmative 可笑-01 «可笑» (snt17 s17x9 = pred s17k) | right relation, wrong parent
i_modal | extra | thing (snt18 s18t = pred s18t): - -> author :full-affirmative thing (snt18 s18t = pred s18t) | gold gives this node no modal parent
i_modal | wrong | 复制-01 «复制» (snt18 s18x11 = pred s18p): author :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18p) -> thing (snt18 s18t = pred s18t) :full-affirmative 复制-01 «复制» (snt18 s18x11 = pred s18p) | right relation, wrong parent
i_modal | missing | 显著-01 «显著» (snt18 s18x3 = pred s18x): author :full-affirmative 显著-01 «显著» (snt18 s18x3 = pred s18x) -> - | the prediction gives this node no modal parent
i_modal | extra | have-reason-91 (snt19 s19h = pred s19h): - -> author :full-affirmative have-reason-91 (snt19 s19h = pred s19h) | gold gives this node no modal parent
i_modal | extra | person (snt19 s19p = pred s19p): - -> author :full-affirmative person (snt19 s19p = pred s19p) | gold gives this node no modal parent
i_modal | extra | publication (snt19 s19p2 = pred s19m): - -> person (snt19 s19p = pred s19p) :full-affirmative publication (snt19 s19p2 = pred s19m) | gold gives this node no modal parent
i_modal | extra | 篇 «一篇» (snt19 s19x4 = pred s19z): - -> person (snt19 s19p = pred s19p) :full-affirmative 篇 «一篇» (snt19 s19x4 = pred s19z) | gold gives this node no modal parent
i_modal | missing | identity-91 (snt20 s20i2 = pred s20i): author :full-affirmative identity-91 (snt20 s20i2 = pred s20i) -> - | the prediction gives this node no modal parent
i_modal | wrong | 好事 «好事者» (snt20 s20x3 = pred s20r): author :full-affirmative 好事 «好事者» (snt20 s20x3 = pred s20r) -> 刊 «该刊» (snt20 s20x8 = pred s20k) :full-affirmative 好事 «好事者» (snt20 s20x3 = pred s20r) | right relation, wrong parent
i_modal | extra | 刊 «该刊» (snt20 s20x8 = pred s20k): - -> author :full-affirmative 刊 «该刊» (snt20 s20x8 = pred s20k) | gold gives this node no modal parent
j_coref_chain | extra | 外星人 «外星人» (snt16 s16x16 = pred s16w): - -> name (snt19 s19n = pred s19w) | gold links it to nothing
j_coref_chain | extra | name (snt19 s19n = pred s19w): - -> 外星人 «外星人» (snt16 s16x16 = pred s16w) | gold links it to nothing

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.