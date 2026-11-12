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
A Chinese adjective that has a roleset (真实, 显著) is an event even before a noun: `N :ARG0-of (真实-01 :aspect state)`, with `(head-event :overlap X)` and an author triple. X者 → `者 :ARG0-of (X-00 :aspect state)`; 复制人 → `人 :ARG1-of (复制-01 :aspect process)`.

**Concept names.** An English event is its PropBank roleset (`deny-01`, `look-up-05`). A Chinese event is the
Chinese word as written with its Chinese PropBank sense (`拥有-01`, `执行-01`); a Chinese predicate that is not
in PropBank is `<word>-00`. Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...). Use an English entity type only for a node with `:name`, or for a pronoun. A common-noun mention, even one that refers back to a named entity (该周报, 这家公司), is the Chinese word itself (`周报`) with its `:mod (该)`. Coreference links it to the named mention.

### 2.2 Named entities

`(c / country :name (n / name :op1 "Russia"))`: an entity-type concept, **no `:wiki`**, and `:name` with one `:opN` per word of the name.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. The title marks 《 》 around a publication's name are name tokens: they are the first and last `:opN`. So is the middle dot (希拉里·克林顿 → `:op2 "·"`). A bare category noun before a foreign name (外星人 P'Lod) is the concept (`外星人 :name …`), not an appositive identity-91. But a name listed as an example of 人物/characters (如蝙蝠男孩、外星人P'Lod) is `individual-person`, the category noun its `:op1`; do not corefer it with a `外星人 :name` mention. 地球 → `planet :name`. Types as in AMR (`company`, `newspaper`, `spaceship`, ...). A headline in 「 」 counted as an article (一篇「…」) or in apposition to 新闻/报导 is `publication :name`: every word and each mark (「, 」, ！) is an `:opN`; 一篇 → `:quant 1 :unit 篇`. Nothing inside it gets a node, `:quote`, temporal or modal triple. 「…」 right after a reporting verb, with no classifier, stays reported content. A dated election (2000年总统大选) is `event :name` ("2000" "年" "总统大选"), no date-entity, no triple. 美国参议院 as a place → `building :name` ("美国" "参议院").

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
- 靠 X (而) V → `V :reason X`, no 靠 node. 有能力 + VP → `有-06 :ARG1 (能力 :ARG1-of (identity-91 :ARG2 VP :aspect state))`, identity-91 with an author triple. A publication's 内容/新闻/文章 → `:part-of` it. 外交政策 → `政策 :topic 外交`; 握手的照片 → `照片 :mod 握手-01`. X的墙上 (a group located there) → `墙上 :place-of X`.
- N 有 A、B…等 listing N's kinds → `N :example (and …)`, no 有 node. 等 closing any list is the last `:opN` (`等`).
- 一些/许多/几 → `:quant (一些)`, not `:mod`. 重复/经常 → `:frequency`; 大部分的 N → `:mod`; 母公司 → `公司 :mod 母`.
- 出现-01: what appears is `:ARG0`, the 在…中 place `:ARG1 (中 :op1 …)`.
- N1 + V + N2 where N2 (程序, 过程, 制度, 方式, 手续) is the procedure that V names: `N2 :ARG0-of (identity-91 :ARG1 V)`, and N1 is the object of V (`V :ARG1 N1`), with V `:aspect process`. Do not flatten N1 and V into `:mod`s of N2. Other modifiers (一般) stay `:mod` of N2.
- Nouns run together without 、 (奇闻轶事) form their own inner `and`; 、 separates the outer conjuncts.
- Aspectual and scalar adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs 目前, 曾经, 现在, 当时 → `:temporal` on that event. Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`). Except: no node for 甚至, for 仍/还 before 继续/保持/依然, for 都 in 都以…为目的, or for 还/也 that only adds a further conjunct or clause (还注销了, 但其编辑也有); keep 也 on a stand-alone sentence's main verb (他们也报导了). A sentence-initial date over a `but-91`/`and` root is `:temporal` of each clause's event (re-used).
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
- Within a sentence, anchor the dependent events (relative clauses, a second conjunct) to the sentence's main anchoring event, not each to `document-creation-time`. The main event is always the parent (first element). In `(and :op1 A :op2 B)`, B's parent is A: `(A :overlap B)`, never document-creation-time. With three or more conjuncts, chain them: `(op1 :overlap op2)` `(op2 :overlap op3)`. A reported past event takes the reporting verb as parent (`(指 :before 当选)`), even if it has its own date (which then gets no triple). A -91 node that is the content of a reporting verb gets no temporal triple; the first event inside it takes the reporting verb as parent, and further events on the same topic (other 报导) take that event as parent.
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
- Within one sentence, pronouns, zero arguments and 自己/其 are re-entrancies. A repeated noun (周报 after the named paper, 该刊) always gets its own node, even in the same sentence, linked by `:same-entity`. No `:subset-of` without a clearly stated set. Never corefer generic kind nouns (外星人 in two different reports).

## 6. Alignment

Every node of a sentence graph is aligned to the words that express it: `s1x: 4-4` (1-based word positions,
first and last, both included). A node with no word in the sentence (`person` for a zero pronoun, `and`
without a conjunction, `have-mod-91` without a copula, a `name` node) is `0-0`. A named entity's type
node is aligned to the name's words.

## 7. Checklist

- Parentheses balanced; every variable defined once; all variables start with `s<N>`.
- Every event has `:aspect`; negated events have `:polarity -`.

- Every event and time expression has a temporal parent; every event has a modal parent.

- For each entity mentioned twice in a sentence, find its first mention by word position; the full node goes there (even inside the `:ARG2` of have-reason-91), every other mention is the bare variable.
- No argument or `:possessor` that the text does not express: no subject copied onto a purpose verb, and no owner added to a name.

## Examples








- 属 (3): 属自己的节目 → `(p / 节目 :ARG0-of (s / 属-02 :ARG1 x))`.

- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.
















- Reified skeleton (2.5): 因为X，为Y，于是Z → `(h / have-reason-91 :ARG1 (h2 / have-purpose-91 :ARG1 Z :ARG2 Y :aspect state) :ARG2 X :aspect state)`.

- Appositive / agent noun (3): 旗下的八卦小报《X》 → `(n / newspaper :ARG1-of (i / identity-91 :ARG2 (x / 小报 :mod (q / 旗下) :mod (b / 八卦))))`; 创始人 → `(p / individual-person :ARG1-of (h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))` (no aspect, no modal on h).

- Event noun (3): 黑白印刷也成了特色 → `:ARG0 (y / 印刷-01 :manner (h / 黑白) :aspect habitual)` + `(成 :overlap y)` `(author :full-affirmative y)`; 1980年代 → `(d / date-entity :era 1980)`.



- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`. 发行量跌至8万3千份 → `(d / 跌-01 :ARG0 (l / 量 ... :ARG1-of (h / have-quant-91 :ARG2 83000 :unit (u / 份))))`.



- Name (2.2): 外星人P'Lod → `(x / 外星人 :name (n / name :op1 "P" :op2 "'" :op3 "Lod"))`.

- Headline (2.2): 刊登一篇「苏联复制一万个希特勒」 → `:ARG2 (p / publication :name (n / name :op1 "「" :op2 "苏联" … :op6 "」") :quant 1 :unit (u / 篇))`, no triples.
- Adjective (2.1): 真实新闻 → `(x / 新闻 :ARG0-of (z / 真实-01 :aspect state))`.
- 靠 (3): 靠外星人背书当选 → `(d / 当选-01 :reason (b / 背书-00 :ARG0 (w / 外星人)))`.

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
        :ARG1 (s16s / 支持-01
            :ARG0 (s16w / 外星人)
            :ARG1 (s16d / 当-02
                :ARG0 (s16p / individual-person
                    :name (s16n / name
                        :op1 "布什"))
                :ARG1 (s16t / 总统)
                :aspect state)
            :quote s16b
            :aspect state)
        :temporal (s16e / event
            :name (s16n2 / name
                :op1 "2000"
                :op2 "年"
                :op3 "总统大选"))
        :aspect performance)
    :op2 (s16x / 注销-01
        :ARG0 s16k
        :ARG1 (s16y / 照片
            :mod (s16w2 / 握手-01
                :ARG0 (s16f / 双方)
                :aspect performance)
            :ARG1-of (s16h / 合成-01
                :aspect performance))
        :temporal s16e
        :aspect performance)
    :op3 (s16z / 指-02
        :ARG0 s16k
        :ARG1 (s16x2 / 当选-01
            :ARG0 (s16p2 / individual-person
                :name (s16n3 / name
                    :op1 "柯林顿"))
            :temporal (s16d2 / date-entity
                :year 1992)
            :reason (s16b2 / 背书-00
                :ARG0 (s16w3 / 外星人)
                :aspect performance)
            :mod (s16y2 / 也)
            :quote s16z
            :aspect performance)
        :temporal s16e
        :aspect performance))


# document level annotation:
(s16s0 / sentence
    :temporal ((document-creation-time :before s16b)
               (s16b :overlap s16x)
               (s16x :overlap s16z)
               (s16b :overlap s16s)
               (s16s :overlap s16d)
               (s16x :before s16w2)
               (s16x :before s16h)
               (s16z :before s16x2)
               (s16x2 :before s16b2))
    :modal ((root :modal author)
            (author :full-affirmative s16b)
            (author :full-affirmative s16x)
            (author :full-affirmative s16z)
            (author :full-affirmative s16k)
            (author :full-affirmative s16s)
            (s16k :full-affirmative s16s)
            (author :full-affirmative s16d)
            (s16k :full-affirmative s16d)
            (author :full-affirmative s16w2)
            (author :full-affirmative s16h)
            (author :full-affirmative s16x2)
            (s16k :full-affirmative s16x2)
            (author :full-affirmative s16b2)
            (s16k :full-affirmative s16b2)))


################################################################################
# meta-info
# :: snt17
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Words: 不过 周报 内容 虽然 荒唐 ， 但 其 编辑 也 有 能力 在 标题 点 出 真实 新闻 的 荒谬 与 可笑 。

# sentence level graph:
(s17b / but-91
    :ARG1 (s17h / 荒唐-01
        :ARG0 (s17n / 内容
            :part-of (s17z / 周报))
        :aspect state)
    :ARG2 (s17y / 有-06
        :ARG0 (s17j / 编辑
            :possessor s17z)
        :ARG1 (s17l / 能力
            :ARG1-of (s17i / identity-91
                :ARG2 (s17d / 点出-01
                    :ARG0 s17j
                    :ARG1 (s17a / and
                        :op1 (s17m / 荒谬-01
                            :ARG0 (s17x / 新闻
                                :ARG0-of (s17r / 真实-01
                                    :aspect state))
                            :aspect state)
                        :op2 (s17k / 可笑-01
                            :ARG0 s17x
                            :aspect state))
                    :place (s17t / 标题)
                    :aspect habitual)
                :aspect state))
        :aspect state))


# document level annotation:
(s17s0 / sentence
    :temporal ((document-creation-time :before s17h)
               (s17h :overlap s17y)
               (s17y :overlap s17d)
               (s17d :overlap s17m)
               (s17m :overlap s17k)
               (s17d :overlap s17r))
    :modal ((root :modal author)
            (author :full-affirmative s17h)
            (author :full-affirmative s17y)
            (author :full-affirmative s17i)
            (author :full-affirmative s17d)
            (author :full-affirmative s17m)
            (author :full-affirmative s17k)
            (author :full-affirmative s17r))
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
        :ARG0-of (s18x / 显著-01
            :aspect state))
    :ARG2 (s18p / publication
        :name (s18n / name
            :op1 "「"
            :op2 "苏联"
            :op3 "复制"
            :op4 "一万个"
            :op5 "希特勒"
            :op6 "」")
        :quant 1
        :unit (s18u / 篇))
    :temporal (s18z / 争论-01
        :ARG0 (s18s / 世界
            :mod (s18q / 全))
        :ARG1 (s18e / 问题
            :mod (s18d / 道德)
            :topic (s18r / 人
                :ARG1-of (s18f / 复制-01
                    :aspect process)))
        :aspect activity)
    :aspect performance)


# document level annotation:
(s18s0 / sentence
    :temporal ((document-creation-time :before s18k)
               (s18k :overlap s18z)
               (s18z :overlap s18f)
               (s18k :overlap s18x))
    :modal ((root :modal author)
            (author :full-affirmative s18k)
            (author :full-affirmative s18z)
            (author :full-affirmative s18f)
            (author :full-affirmative s18x))
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
        :ARG1 (s19q / publication
            :name (s19n / name
                :op1 "「"
                :op2 "美国"
                :op3 "买通"
                :op4 "外星人"
                :op5 "去"
                :op6 "追杀"
                :op7 "宾拉登"
                :op8 "」")
            :quant 1
            :unit (s19u / 篇))
        :mod (s19y / 也)
        :aspect performance)
    :ARG2 (s19f / 讽刺-01
        :ARG1 (s19z / 政策
            :topic (s19w / 外交)
            :place (s19c / country
                :name (s19n2 / name
                    :op1 "美国")))
        :aspect activity)
    :aspect state)


# document level annotation:
(s19s0 / sentence
    :temporal ((document-creation-time :before s19b)
               (s19b :overlap s19f))
    :modal ((root :modal author)
            (author :full-affirmative s19h)
            (author :full-affirmative s19b)
            (author :full-affirmative s19f))
    :coref ((s18t :same-entity s19p)))


################################################################################
# meta-info
# :: snt20
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Words: 该刊 的 一篇 新闻 「 12 位 美国 参议员 是 外星人 ！ 」 甚至 被 好事者 贴到 了 美国 参议院 记者团 的 墙上 。

# sentence level graph:
(s20t / 贴到-01
    :ARG0 (s20z / 者
        :ARG0-of (s20h / 好事-00
            :aspect state))
    :ARG1 (s20q / 墙上
        :place-of (s20j / 记者团
            :place (s20b / building
                :name (s20n2 / name
                    :op1 "美国"
                    :op2 "参议院"))))
    :ARG2 (s20p / publication
        :name (s20n / name
            :op1 "「"
            :op2 "12"
            :op3 "位"
            :op4 "美国"
            :op5 "参议员"
            :op6 "是"
            :op7 "外星人"
            :op8 "！"
            :op9 "」")
        :ARG1-of (s20i / identity-91
            :ARG2 (s20x / 新闻
                :part-of (s20k / 刊
                    :mod (s20g / 该))
                :quant 1
                :unit (s20u / 篇))))
    :aspect performance)


# document level annotation:
(s20s0 / sentence
    :temporal ((document-creation-time :before s20t)
               (s20t :overlap s20h))
    :modal ((root :modal author)
            (author :full-affirmative s20t)
            (author :full-affirmative s20h))
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
a_event_found: R 96 / P 100 / F 98
a_event_concept: R 96 / P 96 / F 96
a_entity_found: R 96 / P 98 / F 97
a_entity_concept: R 100 / P 100 / F 100
a_granularity: R 100 / P 98 / F 99
b_event_sense: R 96 / P 96 / F 96
c_aspect: R 88 / P 84 / F 86
c_refer: R 100 / P 100 / F 100
c_other_attributes: R 80 / P 100 / F 89
d_core_args_event: R 98 / P 98 / F 98
d_core_args_abstract: R 67 / P 67 / F 67
d_peripheral_event: R 90 / P 90 / F 90
d_peripheral_entity: R 86 / P 94 / F 90
e_core_labels: R 95 / P 95 / F 95
e_peripheral_labels: R 95 / P 95 / F 95
f_name_tokens: R 100 / P 100 / F 100
g_reentrancy: R 67 / P 67 / F 67
h_temporal: R 77 / P 74 / F 76
i_modal: R 75 / P 72 / F 74
j_coref_chain: R 100 / P 100 / F 100
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_entity_found | extra | s16y2: - -> 也 | matches no gold node
b_event_sense | wrong | s16x2: 注销 -> 注销-01 | 注销 -> 注销-01
c_aspect | extra | s16x8:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s16x12:aspect: process -> performance | process -> performance
d_peripheral_event | partial | s16x14: temporal s16d/date-entity -> mod s16y2/也 (not in gold); temporal s16d/date-entity | extra mod s16y2/也 (not in gold)
g_reentrancy | missing | s16x/报导-01 -quote-> s16x/报导-01: s16x/报导-01 -quote-> s16x/报导-01 -> - | the prediction has no such edge
g_reentrancy | missing | s16x15/背书 -quote-> s16x3/指-02: s16x15/背书 -quote-> s16x3/指-02 -> - | the prediction has no such edge
g_reentrancy | extra | s16x/注销-01 -temporal-> s16e/event: - -> s16x/注销-01 -temporal-> s16e/event | gold has no such reentrancy
g_reentrancy | extra | s16z/指-02 -temporal-> s16e/event: - -> s16z/指-02 -temporal-> s16e/event | gold has no such reentrancy
g_reentrancy | extra | s16s/支持-01 -quote-> s16b/报导-01: - -> s16s/支持-01 -quote-> s16b/报导-01 | gold has no such reentrancy
a_event_found | missing | s18h: have-example-91 -> - | no node in the prediction matches it
a_entity_found | missing | s18i2: implicit-predicate -> - | no node in the prediction matches it
a_granularity | extra | «「苏联复制一万个希特勒」» publication: «复制» 复制-01 -> «「苏联复制一万个希特勒」» publication | wider than the gold node
a_event_concept | wrong | s19h: have-reason -> have-purpose | have-reason -> have-purpose
a_entity_found | missing | s19x4: 篇 -> - | no node in the prediction matches it
c_aspect | extra | s19h:aspect: - -> state | gold has no :aspect
c_aspect | wrong | s19x2:aspect: performance -> activity | performance -> activity
c_other_attributes | missing | s19x3:quant: 1 -> - | the prediction has no :quant
d_peripheral_entity | missing | s19x3: unit s19x4/篇 -> - | missing unit s19x4/篇
d_peripheral_entity | partial | s19x5: possessor s19c/country; topic s19x6/外交 -> place s19c/country; topic s19x6/外交 | possessor s19c/country: predicted as place
e_peripheral_labels | wrong | s19x5 -possessor-> s19c: possessor -> place | possessor -> place
g_reentrancy | missing | s19x2/讽刺-01 -arg0-> s19p/person: s19x2/讽刺-01 -arg0-> s19p/person -> - | the prediction has no such edge
c_aspect | missing | s20i2:aspect: state -> - | the prediction has no :aspect
d_core_args_event | partial | s20x: arg0 s20x2/者; arg1 s20x4/墙上; arg2 s20x6/新闻 -> arg0 s20x2/者; arg1 s20x4/墙上; arg2 s20p/publication | missing arg2 s20x6/新闻; extra arg2 s20p/publication
d_core_args_abstract | wrong | s20i2: arg1 s20x6/新闻; arg2 s20p/publication -> arg1 s20p/publication; arg2 s20x6/新闻 | arg1 s20x6/新闻: predicted as arg2; arg2 s20p/publication: predicted as arg1
e_core_labels | wrong | s20i2 -arg1-> s20x6: arg1 -> arg2 | arg1 -> arg2
e_core_labels | wrong | s20i2 -arg2-> s20p: arg2 -> arg1 | arg2 -> arg1
h_temporal | wrong | 合成-01 «合成» (snt16 s16x11 = pred s16h): 注销 «注销» (snt16 s16x2 = pred s16x) :overlap 合成-01 «合成» (snt16 s16x11 = pred s16h) -> 注销 «注销» (snt16 s16x2 = pred s16x) :before 合成-01 «合成» (snt16 s16x11 = pred s16h) | right parent, wrong relation
h_temporal | wrong | 握手-01 «握手» (snt16 s16x12 = pred s16w2): 合成-01 «合成» (snt16 s16x11 = pred s16h) :overlap 握手-01 «握手» (snt16 s16x12 = pred s16w2) -> 注销 «注销» (snt16 s16x2 = pred s16x) :before 握手-01 «握手» (snt16 s16x12 = pred s16w2) | wrong parent and relation
h_temporal | wrong | 背书 «背书» (snt16 s16x15 = pred s16b2): 当选-01 «当选» (snt16 s16x14 = pred s16x2) :overlap 背书 «背书» (snt16 s16x15 = pred s16b2) -> 当选-01 «当选» (snt16 s16x14 = pred s16x2) :before 背书 «背书» (snt16 s16x15 = pred s16b2) | right parent, wrong relation
h_temporal | wrong | 真实-01 «真实» (snt17 s17x11 = pred s17r): 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17r) -> 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 真实-01 «真实» (snt17 s17x11 = pred s17r) | right relation, wrong parent
h_temporal | wrong | 可笑-01 «可笑» (snt17 s17x9 = pred s17k): 点出-01 «点» (snt17 s17x7 = pred s17d) :overlap 可笑-01 «可笑» (snt17 s17x9 = pred s17k) -> 荒谬-01 «荒谬» (snt17 s17x8 = pred s17m) :overlap 可笑-01 «可笑» (snt17 s17x9 = pred s17k) | right relation, wrong parent
h_temporal | extra | 复制-01 «复制» (snt18 s18x11 = pred s18f): - -> 争论-01 «争论» (snt18 s18x5 = pred s18z) :overlap 复制-01 «复制» (snt18 s18x11 = pred s18f) | gold gives this node no temporal parent
i_modal | wrong | 报导-01 «报导» (snt16 s16x = pred s16b): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) -> author :full-affirmative 报导-01 «报导» (snt16 s16x = pred s16b) | right relation, wrong parent
i_modal | partial | 当选-01 «当选» (snt16 s16x14 = pred s16x2): author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16x2) -> author :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16x2); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当选-01 «当选» (snt16 s16x14 = pred s16x2) | agrees on part of the relations
i_modal | partial | 背书 «背书» (snt16 s16x15 = pred s16b2): author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16b2) -> author :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16b2); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 背书 «背书» (snt16 s16x15 = pred s16b2) | agrees on part of the relations
i_modal | wrong | 注销 «注销» (snt16 s16x2 = pred s16x): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16x) -> author :full-affirmative 注销 «注销» (snt16 s16x2 = pred s16x) | right relation, wrong parent
i_modal | wrong | 指-02 «指» (snt16 s16x3 = pred s16z): 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16z) -> author :full-affirmative 指-02 «指» (snt16 s16x3 = pred s16z) | right relation, wrong parent
i_modal | partial | 支持-01 «支持» (snt16 s16x6 = pred s16s): author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16s) -> author :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16s); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 支持-01 «支持» (snt16 s16x6 = pred s16s) | agrees on part of the relations
i_modal | extra | 当-02 «当» (snt16 s16x8 = pred s16d): - -> author :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16d); 刊 «该刊» (snt16 s16x4 = pred s16k) :full-affirmative 当-02 «当» (snt16 s16x8 = pred s16d) | gold gives this node no modal parent
i_modal | wrong | 点出-01 «点» (snt17 s17x7 = pred s17d): author :neutral-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) -> author :full-affirmative 点出-01 «点» (snt17 s17x7 = pred s17d) | right parent, wrong relation
i_modal | extra | have-reason-91 (snt19 s19h = pred s19h): - -> author :full-affirmative have-reason-91 (snt19 s19h = pred s19h) | gold gives this node no modal parent
i_modal | missing | identity-91 (snt20 s20i2 = pred s20i): author :full-affirmative identity-91 (snt20 s20i2 = pred s20i) -> - | the prediction gives this node no modal parent

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.