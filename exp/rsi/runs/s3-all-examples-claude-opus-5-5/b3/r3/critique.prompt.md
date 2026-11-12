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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. The title marks 《 》 around a publication's name are name tokens: they are the first and last `:opN`. So is the middle dot (希拉里·克林顿 → `:op2 "·"`). A bare category noun before a foreign name (外星人 P'Lod) is the concept (`外星人 :name …`), not an appositive identity-91. But a name listed as an example of 人物/characters (如蝙蝠男孩、外星人P'Lod) is `individual-person`, the category noun its `:op1`; do not corefer it with a `外星人 :name` mention. 地球 → `planet :name`. Types: `person`,
`country`, `city`, `organization`,
`company`, `newspaper`, `publication`,
`event`,
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
- 其中 → `:mod (其中)` on the noun it introduces, not `:part`; with a superlative (其中最大宗) it is `:ARG5` of have-degree-91, and the head is `implicit-argument :unit 宗`.
- X 与/和/跟 Y 有关系 → `有-03 :ARG0 (and :op1 X :op2 Y)`, not `:companion`.
- N 有 A、B…等 listing N's kinds → `N :example (and …)`, no 有 node. 等 closing any list is the last `:opN` (`等`).
- 重复/经常 → `:frequency`; 大部分的 N → `:mod`; 母公司 → `公司 :mod 母`.
- 出现-01: what appears is `:ARG0`, the 在…中 place `:ARG1 (中 :op1 …)`.
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


- Title marks (2.2): 《世界新闻周报》 → `:name (n / name :op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》")`.
- but-91 (2.5): X，不过Y (within one sentence) → `(b / but-91 :ARG1 X :ARG2 Y)`. A sentence starting with 不过 → no but-91; root = main verb (跌-01).
- 以…而闻名 (2.5): a tabloid known for its reports → `(x / 小报 :ARG1-of (k / 闻名-01 :reason (r / 报导-01 :ARG0 x)))`.


- Shared modifier (3): 奇怪的新闻与专栏 → `(a / and :op1 (n / 新闻 :mod (q / 奇怪)) :op2 (z / 专栏 :mod q))`.
- 属 (3): 属自己的节目 → `(p / 节目 :ARG0-of (s / 属-02 :ARG1 x))`.

- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.
- 历史上 (4.2): 美国历史上 → `:temporal (s / 上 :op1 (h / 历史 ...))`.


- V1V2的N (3): 已经停止发行的小报 → `(x / 小报 :ARG1-of (f / 发行-01 :ARG1-of (t / 停止-01 :mod (y / 已经) :aspect state) :aspect habitual))`.




- Procedure compound (3): 一般的新闻查证程序 → `(x / 程序 :ARG0-of (i / identity-91 :ARG1 (c / 查证-01 :ARG1 (n / 新闻) :aspect process)) :mod (y / 一般))`.






- Temporal (5.1): 创刊于1979年 → `(document-creation-time :before s6d)` `(s6d :overlap s6x)`; purpose 为运用 → `(创立 :overlap 运用)`; reason 因为…改为 → `(创立 :before 改为)`; 遗留下来的印刷机 used by 运用 → `(运用 :before 遗留)`; 也成了…特色 → `(prev-main :overlap 成)`.
- Reified skeleton (2.5): 因为X，为Y，于是Z → `(h / have-reason-91 :ARG1 (h2 / have-purpose-91 :ARG1 Z :ARG2 Y :aspect state) :ARG2 X :aspect state)`.
- Part and relative clause (3): 创立黑白版面的《Y》，容纳…文章 → `:ARG1 (b / 版面 :mod (h / 黑白) :part-of (n / newspaper ...) :ARG0-of (r / 容纳-01 :ARG1 ... :aspect process))`.
- Appositive / agent noun (3): 旗下的八卦小报《X》 → `(n / newspaper :ARG1-of (i / identity-91 :ARG2 (x / 小报 :mod (q / 旗下) :mod (b / 八卦))))`; 创始人 → `(p / individual-person :ARG1-of (h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))` (no aspect, no modal on h).
- Quantity (3): 发行量达到120万份 → `(d / 达到-01 :ARG0 (l / 量 :quant-of (f / 发行-01 :ARG1 n) :ARG1-of (h / have-quant-91 :ARG2 1200000 :unit (u / 份))))`.
- Event noun (3): 黑白印刷也成了特色 → `:ARG0 (y / 印刷-01 :manner (h / 黑白) :aspect habitual)` + `(成 :overlap y)` `(author :full-affirmative y)`; 1980年代 → `(d / date-entity :era 1980)`.


- First mention (3): 《Y》将由黑白版面改为… then Y的标准 → `改为-01 :ARG1 (b / 版面 :part-of (n / newspaper :name ... :ARG1-of (identity-91 ...)) :mod (h / 黑白))` … `(标准 :possessor n)`.
- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`. 发行量跌至8万3千份 → `(d / 跌-01 :ARG0 (l / 量 ... :ARG1-of (h / have-quant-91 :ARG2 83000 :unit (u / 份))))`.

- 虽然…不过 (2.5): 虽然他们宣称X（标语：Y），不过大部分报导以博君一笑为目的 → `(b / but-91 :ARG1 (a / and :op1 宣称 :op2 (i / identity-91 :ARG1 标语 :ARG2 Y)) :ARG2 (i2 / identity-91 :ARG1 (m / 目的 :purpose-of 报导) :ARG2 (g / 博君一笑)))`.
- 是…的 (2.3): 都是真实的 → `(h / have-mod-91 :ARG2 (t / 真实) :mod (d / 都) :aspect state)`.
- Name (2.2): 外星人P'Lod → `(x / 外星人 :name (n / name :op1 "P" :op2 "'" :op3 "Lod"))`.
- 有关系 (3): 与P'Lod有暧昧关系，后来还领养 → `(c / consecutive :op1 (y / 有-03 :ARG0 (a / and :op1 h :op2 p) :ARG1 关系) :op2 领养-01)`.

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
    :ARG1 (s11t / 停止-01
        :ARG0 (s11c / company
            :name (s11n / name
                :op1 "美国"
                :op2 "媒体"
                :op3 "公司")
            :ARG1-of (s11i / identity-91
                :ARG2 (s11x / 公司
                    :mod (s11x2 / 母))))
        :ARG1 (s11f / 发行-01
            :ARG0 s11c
            :ARG1 (s11p / newspaper
                :name (s11n2 / name
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
    :ARG2 (s11j / 继续-01
        :ARG0 (s11w / 网络版
            :part-of (s11x4 / 周报))
        :ARG1 (s11s / 生存-01
            :ARG0 s11w
            :aspect state)
        :mod (s11r / 仍)
        :aspect activity))


# document level annotation:
(s11s0 / sentence
    :temporal ((document-creation-time :before s11d)
               (s11d :overlap s11t)
               (s11t :overlap s11f)
               (s11t :overlap s11j)
               (s11j :overlap s11s))
    :modal ((author :full-affirmative null-conceiver)
            (root :modal author)
            (author :full-affirmative s11t)
            (author :full-affirmative s11f)
            (author :full-affirmative s11j)
            (author :full-affirmative s11s))
    :coref ((s11p :same-entity s11x4)))


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
                :name (s12m / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》"))
            :ARG1 (s12h / have-mod-91
                :ARG1 (s12x2 / 报导-01
                    :aspect habitual)
                :ARG2 (s12x3 / 真实)
                :mod (s12d / 都)
                :quote s12x
                :aspect state)
            :aspect performance)
        :op2 (s12i / identity-91
            :ARG1 (s12x4 / 标语
                :possessor s12n)
            :ARG2 (s12x5 / 报导-01
                :ARG0 s12n
                :ARG1 (s12x6 / 事实)
                :mod (s12z / 只)
                :quote s12i
                :aspect habitual)
            :aspect state))
    :ARG2 (s12i2 / identity-91
        :ARG1 (s12x7 / 目的
            :purpose-of (s12x8 / 报导-01
                :mod (s12x9 / 大部分)
                :aspect habitual))
        :ARG2 (s12g / 博君一笑)
        :mod (s12d2 / 都)
        :aspect state))


# document level annotation:
(s12s0 / sentence
    :temporal ((document-creation-time :before s12x)
               (s12x :overlap s12x2)
               (s12x2 :overlap s12x5)
               (s12x2 :overlap s12x8))
    :modal ((author :full-affirmative null-conceiver)
            (root :modal author)
            (author :full-affirmative s12n)
            (author :full-affirmative s12x)
            (s12n :full-affirmative s12h)
            (author :full-affirmative s12h)
            (author :full-affirmative s12x2)
            (author :full-affirmative s12i)
            (s12n :full-affirmative s12x5)
            (author :full-affirmative s12x5)
            (author :full-affirmative s12i2)
            (author :full-affirmative s12x8))
    :coref ((s11x4 :same-entity s12n)))


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
            :frequency (s13j / 经常)
            :aspect habitual)
        :example (s13a2 / and
            :op1 (s13x / 外星人)
            :op2 (s13x2 / 航天员
                :mod (s13x3 / 古代))
            :op3 (s13x4 / 旅行
                :mod (s13x5 / 时间))
            :op4 (s13x6 / 大脚)
            :op5 (s13x7 / 欧帕兹)
            :op6 (s13x8 / 等)))
    :op2 (s13c / 创造-01
        :ARG0 s13p
        :ARG1 (s13w / 人物
            :mod (s13y / 一些)
            :mod (s13v / 虚拟)
            :ARG0-of (s13o / 出现-01
                :ARG1 (s13z / 中
                    :op1 (s13x9 / 新闻
                        :possessor s13p))
                :frequency (s13f / 重复)
                :aspect habitual)
            :example (s13a3 / and
                :op1 (s13i / individual-person
                    :name (s13n / name
                        :op1 "蝙蝠"
                        :op2 "男孩"))
                :op2 (s13i2 / individual-person
                    :name (s13n2 / name
                        :op1 "外星人"
                        :op2 "P"
                        :op3 "'"
                        :op4 "Lod"))
                :op3 (s13x10 / 等)))
        :mod (s13s / 甚至)
        :aspect performance))


# document level annotation:
(s13s0 / sentence
    :temporal ((document-creation-time :before s13r)
               (s13r :overlap s13c)
               (s13c :overlap s13o))
    :modal ((author :full-affirmative null-conceiver)
            (root :modal author)
            (author :full-affirmative s13r)
            (author :full-affirmative s13c)
            (author :full-affirmative s13o))
    :coref ((s12n :same-entity s13p)))


################################################################################
# meta-info
# :: snt14
Index: 1 2 3 4 5 6 7 8
Words: 其中 最大宗 可 算是 外星人 地球 活动 。

# sentence level graph:
(s14x / 算是-01
    :ARG0 (s14i / implicit-argument
        :unit (s14u / 宗)
        :ARG1-of (s14h / have-degree-91
            :ARG2 (s14d / 大-01
                :aspect state)
            :ARG3 (s14z / 最)
            :ARG5 (s14q / 其中)))
    :ARG1 (s14e / 活动-01
        :ARG0 (s14w / 外星人)
        :place (s14p / planet
            :name (s14n / name
                :op1 "地球"))
        :aspect activity)
    :modal-strength neutral-affirmative
    :aspect state)


# document level annotation:
(s14s0 / sentence
    :temporal ((document-creation-time :before s14x)
               (s14x :overlap s14d)
               (s14x :overlap s14e))
    :modal ((author :full-affirmative null-conceiver)
            (root :modal author)
            (author :neutral-affirmative s14x)
            (author :full-affirmative s14d)
            (author :full-affirmative s14e)))


################################################################################
# meta-info
# :: snt15
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 美国 前 第一夫人 希拉里 · 克林顿 就 被 指 与 外星人 P ' Lod 有 暧昧 关系 ， 后来 还 领养 外星 宝宝 。

# sentence level graph:
(s15z / 指-02
    :ARG1 (s15c / consecutive
        :op1 (s15y / 有-03
            :ARG0 (s15a / and
                :op1 (s15h / individual-person
                    :name (s15n / name
                        :op1 "希拉里"
                        :op2 "·"
                        :op3 "克林顿")
                    :ARG1-of (s15r / have-rel-role-91
                        :ARG3 (s15f / 第一夫人
                            :mod (s15q / 前)
                            :place (s15g / country
                                :name (s15n2 / name
                                    :op1 "美国")))))
                :op2 (s15p / 外星人
                    :name (s15n3 / name
                        :op1 "P"
                        :op2 "'"
                        :op3 "Lod")))
            :ARG1 (s15x / 关系
                :mod (s15m / 暧昧))
            :quote s15z
            :aspect state)
        :op2 (s15l / 领养-01
            :ARG0 s15h
            :ARG1 (s15b / 宝宝
                :mod (s15w / 外星))
            :quote s15z
            :aspect performance))
    :aspect performance)


# document level annotation:
(s15s0 / sentence
    :temporal ((document-creation-time :before s15z)
               (s15z :overlap s15y)
               (s15y :after s15l))
    :modal ((author :full-affirmative null-conceiver)
            (root :modal author)
            (author :full-affirmative s15z)
            (null-conceiver :full-affirmative s15y)
            (null-conceiver :full-affirmative s15l)
            (author :full-affirmative s15y)
            (author :full-affirmative s15l)))



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
a_entity_concept: R 100 / P 100 / F 100
a_granularity: R 94 / P 93 / F 94
b_event_sense: R 94 / P 94 / F 94
c_aspect: R 100 / P 100 / F 100
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 100 / P 100 / F 100
d_core_args_event: R 100 / P 100 / F 100
d_core_args_abstract: R 89 / P 89 / F 89
d_peripheral_event: R 100 / P 88 / F 93
d_peripheral_entity: R 95 / P 95 / F 95
e_core_labels: R 95 / P 95 / F 95
e_peripheral_labels: R 95 / P 95 / F 95
f_name_tokens: R 100 / P 100 / F 100
g_reentrancy: R 92 / P 100 / F 96
h_temporal: R 94 / P 89 / F 91
i_modal: R 84 / P 80 / F 82
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_found | extra | s11r: - -> 仍 | matches no gold node
a_granularity | missing | «周报» 周报: «周报» 周报 -> «《世界新闻周报》» newspaper | inside a wider predicted node
a_granularity | extra | «美国媒体公司» company: «公司» 公司 -> «美国媒体公司» company | wider than the gold node
a_granularity | extra | «《世界新闻周报》» newspaper: «周报» 周报 -> «《世界新闻周报》» newspaper | wider than the gold node
d_peripheral_event | extra | s11x2: - -> mod s11r/仍 (not in gold) | extra mod s11r/仍 (not in gold)
g_reentrancy | missing | s11x2/继续-01 -temporal-> s11d/date-entity: s11x2/继续-01 -temporal-> s11d/date-entity -> - | the prediction has no such edge
a_entity_found | extra | s12d2: - -> 都 | matches no gold node
a_granularity | missing | «P» individual-person/individual-person/person: «P» individual-person/individual-person/person -> «外星人P'Lod» individual-person | inside a wider predicted node
a_granularity | extra | «外星人P'Lod» individual-person: «P» individual-person/individual-person/person -> «外星人P'Lod» individual-person | wider than the gold node
d_peripheral_entity | partial | s13x13: example s13a3/and; mod s13x14/虚拟; quant s13x15/一些 -> example s13a3/and; mod s13x14/虚拟; mod s13x15/一些 | quant s13x15/一些: predicted as mod
e_peripheral_labels | wrong | s13x13 -quant-> s13x15: quant -> mod | quant -> mod
d_core_args_abstract | partial | s14h: arg1 s14i2/implicit-argument; arg1 s14x3/大; arg2 s14x4/最; arg5 s14x5/其中 -> arg1 s14i2/implicit-argument; arg2 s14x3/大; arg3 s14x4/最; arg5 s14x5/其中 | arg1 s14x3/大: predicted as arg2; arg2 s14x4/最: predicted as arg3
e_core_labels | wrong | s14h -arg1-> s14x3: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s14h -arg2-> s14x4: arg2 -> arg3 | arg2 -> arg3
a_granularity | missing | «P» individual-person: «P» individual-person -> «P'Lod» 外星人 | inside a wider predicted node
a_granularity | extra | «P'Lod» 外星人: «P» individual-person -> «P'Lod» 外星人 | wider than the gold node
b_event_sense | wrong | s15x2: 领养 -> 领养-01 | 领养 -> 领养-01
h_temporal | extra | 出现-01 «出现» (snt13 s13x16 = pred s13o): - -> 创造-01 «创造» (snt13 s13x = pred s13c) :overlap 出现-01 «出现» (snt13 s13x16 = pred s13o) | gold gives this node no temporal parent
h_temporal | missing | 航天员 «航天员» (snt13 s13x6 = pred s13x2): 创造-01 «创造» (snt13 s13x = pred s13c) :overlap 航天员 «航天员» (snt13 s13x6 = pred s13x2) -> - | the prediction gives this node no temporal parent
h_temporal | extra | 大 «最大宗» (snt14 s14x3 = pred s14d): - -> 算是-01 «算是» (snt14 s14x = pred s14x) :overlap 大 «最大宗» (snt14 s14x3 = pred s14d) | gold gives this node no temporal parent
i_modal | extra | null-conceiver: - -> author :full-affirmative null-conceiver | gold gives this node no modal parent
i_modal | partial | 报导-01 «报导» (snt12 s12x10 = pred s12x8): author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x8); newspaper (snt12 s12n = pred s12n) :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x8) -> author :full-affirmative 报导-01 «报导» (snt12 s12x10 = pred s12x8) | agrees on part of the relations
i_modal | extra | 大 «最大宗» (snt14 s14x3 = pred s14d): - -> author :full-affirmative 大 «最大宗» (snt14 s14x3 = pred s14d) | gold gives this node no modal parent
i_modal | missing | and (snt15 s15a = pred s15a): author :full-affirmative and (snt15 s15a = pred s15a) -> - | the prediction gives this node no modal parent
i_modal | wrong | 领养 «领养» (snt15 s15x2 = pred s15l): and (snt15 s15a = pred s15a) :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) -> author :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l); null-conceiver :full-affirmative 领养 «领养» (snt15 s15x2 = pred s15l) | right relation, wrong parent
i_modal | wrong | 有-03 «有» (snt15 s15x3 = pred s15y): and (snt15 s15a = pred s15a) :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) -> author :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y); null-conceiver :full-affirmative 有-03 «有» (snt15 s15x3 = pred s15y) | right relation, wrong parent

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.