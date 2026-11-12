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

**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,
with an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value
and document-level relation counts. Take the time this needs:

- Read the guidelines below carefully before you start, and go back to them for every decision you are
  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named
  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.
- Follow the examples: when a sentence has a construction an example shows, annotate it the way the
  example does.
- Do not guess when you can check: the answer to almost every question is in the guidelines above and
  their examples; look it up there rather than answer from memory.
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
in PropBank is `<word>-00` — look the verb up first; many verbs that look rare have a sense (停刊-01). Keep compound verbs whole (称为 → `称为-01`, not `称-01`). Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
written in Chinese (`宇航员`, `航天器`). Use English only for the abstract concepts below and for entity
types (`person`, `thing`, `country`, `city`, `organization`, ...).

### 2.2 Named entities

`(c / country :wiki "Russia" :name (n / name :op1 "Russia"))`: an entity-type concept, an optional `:wiki`
(the Wikipedia title, or `-` when there is none), and `:name` with one `:opN` per word of the name.
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`.
In Chinese names keep the title brackets 《 》 as their own `:opN` (《世界新闻周报》 → `:op1 "《" :op2 "世界" ... :opN "》"`). Do not add `:wiki` in Chinese documents. A country or place name that modifies a noun (美国小报) is `:place`, not `:mod`. Do not corefer a repeated country name that is only such a modifier. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
a classifier is kept as the unit too, including 个, 份, 款, 本 (一份小报 → `小报 :quant 1 :unit (份)`).

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

When the text has a lexical verb that is in Chinese PropBank (属, 拥有), use that verb with its frame's roles instead of `belong-91` / `have-91`. Superlatives and comparatives (最, 更, *most, more*) use `(have-degree-91 :ARG1 X :ARG2 <property> :ARG3 (最))`, not `:degree`. `have-degree-91` gets no `:aspect`. A root `identity-91` / `have-*-91` (the sentence's main predicate) takes `:aspect state`; an `identity-91` inside a noun phrase (程序 :ARG0-of identity-91) takes none. A frame such as 历史上 / 在…上 is `:temporal (上 :op1 (历史))` on the noun, not an `:ARG4` of `have-degree-91`.

### 2.4 Pronouns and implicit participants

A pronoun is `person` or `thing` with person and number: 他 / *he* → `(p / person :refer-person 3rd
:refer-number singular)`; 我们 / *we* → `:refer-person 1st :refer-number plural`; 它 / *it* → `thing` with
3rd singular. A plural noun gets `:refer-number plural`. A Chinese zero subject or object that is clearly
recoverable may be added as such a node (aligned to no word) and linked by coreference.

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过, 可是) `but-91`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) and 以…而 → `:reason`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.

### 2.6 Multi-word expressions

An idiom, a phrasal verb or a fixed expression is one concept (`look-up-05`, `give-up-07`; a Chinese chengyu
is one concept). A discontinuous word (帮……忙) is one concept aligned to its span. A fixed four-character idiom is one concept. A pair of coordinated nouns written together (奇闻轶事) is split: `(and :op1 (奇闻) :op2 (轶事))`.

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

- Chinese adverbs are concepts, not only aspect cues. 已经, 都, 也, 仍, 还 and 其中 → `:mod (<word>)`; 曾经 → `:temporal (曾经)`. A medium (电视, 网络) is `:medium`.
- A modifier shared by coordinated nouns goes on each conjunct by reentrancy, never on the `and` node.
- Do not add arguments (agents, possessors) that the text does not express or clearly imply. Do not fill the subject of a later clause with an entity from an earlier clause (…，不过仍继续发行网络版: 发行 has no `:ARG0`).
- An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor` — but only when the whole is written with it (《…》的纸本). A bare 网络版 gets no `:part-of`.
- For an intransitive Chinese verb such as 停刊-01 (or a `-00` verb not in PropBank), the sole participant is `:ARG0`.
- When an event noun names what the head noun is (查证程序: the procedure is the verification), use `(程序 :ARG0-of (identity-91 :ARG1 (查证-01)))`, not `:mod`.
- In 'X 是 … Y，以 … 而 V' the second predicate modifies Y: `Y :ARG1-of (V :reason ...)`. Do not add a coordinating `and`.

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

Aspect cues: recurring activities of a publication or institution (发行, 报导, 综合) are `habitual`, even with 了. 已经 + 停止 or another end verb is `state` only inside a relative clause that describes an entity (已经停止发行的小报); as the main predicate, 已经 + an end verb (已经停刊) is `performance`. Passive naming (被称为) is `performance`. Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂. A negated event (未, 没) never gets `performance`; use `process` when its type cannot be told.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2). Exception: 未经 X / 没有经过 X → `经-01` with no `:polarity`; the negation is only the modal triple `(author :full-negative 经)`.
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
- Time expressions first: an absolute date (*1998*) depends on `root`; a relative one (*today, yesterday*,
  今天) depends on `document-creation-time` — `(document-creation-time :depends-on s1t)`; a vague one
  (*nowadays*) on `past-reference` / `present-reference` / `future-reference` (for 目前/现在 see the rule below).
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :contained s1e)`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent; a purpose is `:after` its main event.
- Anchor only the **main event** of a sentence to `document-creation-time` (or to a time expression of its clause). Attach every other event of the sentence to that main event or to a nearby event, usually `:overlap` (`:contained` if it lies inside it, `:before`/`:after` when the order is clear). Events inside relative clauses, modifiers and event nominals also need a parent, normally their governing event with `:overlap`. Leave no event without a temporal parent.
- Copular abstract predicates (`identity-91`, `have-mod-91`, `have-*-91`) normally get **no** temporal parent.
- A relative time word such as 目前 or 现在 is a `:temporal` node in the graph but gets **no** temporal parent of its own. Link the main event of its clause to `document-creation-time` with `:depends-on` (`(document-creation-time :depends-on <main event>)`), then chain the other events from that main event with `:overlap`.
- 曾经 and 已经 are graph nodes only: they get no temporal parent and no event hangs from them. A past event marked with 曾经 or 过 is `(document-creation-time :before <event>)`; chain the sentence's other events from it with `:overlap`.
- The main event of a naming or reputation clause (被称为, 被誉为) is `(document-creation-time :depends-on <event>)`, as with 目前.
- When the root is an abstract predicate (`identity-91`, `have-mod-91`), anchor to `document-creation-time` the first event inside it (usually a relative-clause event such as 发行) and hang every other event from that event: an end verb (停止) `:overlap`; a reputation or state holding within it (闻名) `:contained`; a co-occurring activity (报导) `:overlap`. Never anchor more than one event of a sentence to `document-creation-time`.
- An event that modifies a noun hangs from the event whose argument that noun is (查证 inside 程序, the argument of 经 → `(经 :overlap 查证)`), not from the sentence's first event.

### 5.2 Modal (`:modal`)

A dependency structure of conceivers and events: `(conceiver :strength event)`, starting with
`(root :modal author)` in every sentence that has events.

- Strength = the conceiver's certainty that the event happens or holds: `full-affirmative` (plain
  assertion, *will*), `partial-affirmative` (*probably, must, should*, 应该, 可能性大, 一定 as inference),
  `neutral-affirmative` (*may, might, perhaps, can*, 可能, 也许, 或许, desire/hope), `neutral-negative`,
  `partial-negative`, `full-negative` (negated: *not, never, deny*, 没, 不), `unspecified`.
- Every event the author asserts: `(author :full-affirmative s1e)`.
- The root abstract predicate (`identity-91`, `have-mod-91`, ...) of an asserted sentence also gets `(author :full-affirmative …)`, although it gets no temporal parent.
- Reported speech or thought: the author is certain of the speaker, the speaker of the content:
  `(author :full-affirmative s9p)` `(s9p :full-affirmative s9s3)`, where `s9p` is the speaker (a person
  node, or an event used as conceiver).
- An event under a modal or complement-taking predicate (*want, try, plan, decide, hope*, 想, 希望, 打算,
  决定, 需要): the predicate is asserted by the author, the complement has the predicate as parent with
  `unspecified` (or the strength the predicate implies): `(author :full-affirmative s3w)`
  `(s3w :unspecified s3g)`.
- A conceiver that is not in the text is `null-conceiver`. An event nominal naming a usual procedure (一般的…程序) under a negated event is `(author :partial-affirmative <nominal>)`. Purpose and condition clauses may use the
  constants `purpose` and `have-condition` as parents of their events.
- In the sentence graph, write the strength of an event that is not `full-affirmative` from the author as
  `:modal-strength <value>` too (the scorers move it to the document level).

### 5.3 Coreference (`:coref`)

- `(earlier :same-entity later)`: two mentions of the same entity — a pronoun and its antecedent, a repeated
  name, a definite description. Link each mention to its closest earlier mention, earlier one first;
  link entity nodes, never `name` nodes.
- `(earlier :same-event later)`: two mentions of the same event.
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.
- Link two mentions only when they pick out the same individual or the same single event. Do not link two mentions of the same verb with different arguments, times or polarity (发行 of the print edition vs 发行 of the online edition). Do not link noun phrases with the same head but different restrictors (许多内容 vs 荒诞不经的内容). Never put a `:subset-of` triple inside one sentence. When in doubt, leave the link out; chains like 周报 / 该周报 / 《…周报》 are what gold annotates.

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

## Examples

- Temporal chain (5.1): 目前…停刊，不过仍继续发行网络版 → `(document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`; 目前 has no temporal parent.
- Copular root (5.1): 是…已经停止发行的小报，以报导…而闻名 → `(document-creation-time :before 发行) (发行 :overlap 停止) (闻名 :contained 发行) (发行 :overlap 报导)`; modal `(author :full-affirmative identity-91)`.
- Coref (5.3): 发行 (print, stopped) vs 发行 (online edition, continuing) → no `:same-event`.
- Aspect (4.1): main predicate 纸本已经停刊 → `(停刊-01 :ARG0 (纸本 …) :aspect performance)`; 继续发行网络版 → bare `(网络版)`, no `:part-of`.
- 曾经 + 过 (4.1, 5.1): 也曾经短暂的拥有过一个节目 → `(拥有-01 :temporal (曾经) :aspect state)`, `(document-creation-time :before 拥有) (拥有 :overlap …)`; 曾经 has no temporal parent.
- Negation (4.2): 都未经一般的新闻查证程序 → `(经-01 :mod (都) :aspect process)` without `:polarity`; modal `(author :full-negative 经) (author :partial-affirmative 查证)`.
- Root copula (2.3): 是…小报 → `(identity-91 :ARG1 … :ARG2 … :aspect state)`.
- Naming (5.1): 被称为… → `(document-creation-time :depends-on 称为)`.
- Degree (2.3): 美国历史上最…的报纸 → `(报纸 :temporal (上 :op1 (历史 :place (country …))))`, `have-degree-91` without aspect; 称为 → `称为-01`.
- Classifier (2.2): 一个节目 → `(节目 :quant 1 :unit (个))`.
- Adverb (3): 已经停止 → `(停止-01 :mod (已经) :aspect state)`; 曾经 → `:temporal (曾经)`.
- Name (2.2): 美国…小报 → `(小报 :place (country :name (name :op1 "美国")))`, with no `:wiki`.
- Reason (2.5): 以报导…而闻名 → `(闻名-01 :reason (报导-01 ...))`.
- Lexical verb (2.3): 节目属周报 → `(属-02 :ARG0 节目 :ARG1 周报)`, not `belong-91`.
- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`.

</instruction>

# The sentences
6	《 世界 新闻 周报 》 创刊 于 1979 年 。
7	创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。
8	黑白 印刷 也 成 了 该刊 的 特色 。
9	在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。
10	不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。

# The annotator's annotation (as scored)
<annotation>
################################################################################
# meta-info
# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10
Words: 《 世界 新闻 周报 》 创刊 于 1979 年 。

# sentence level graph:
(s6c / 创刊-01
    :ARG0 (s6p / newspaper
        :name (s6n / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :temporal (s6d / date-entity
        :year 1979)
    :aspect performance)


# document level annotation:
(s6s0 / sentence
    :temporal ((root :depends-on s6d)
               (s6d :contained s6c))
    :modal ((root :modal author)
            (author :full-affirmative s6c)))


################################################################################
# meta-info
# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
Words: 创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。

# sentence level graph:
(s7c / 创立-01
    :ARG0 (s7p / person
        :name (s7n / name
            :op1 "格内洛索"
            :op2 "波普")
        :ARG1-of (s7h / have-org-role-92
            :ARG2 (s7w / newspaper
                :name (s7n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")
                :mod (s7b / 版面
                    :mod (s7h2 / 黑白)))
            :ARG3 (s7f / 创始人)))
    :ARG1 s7w
    :reason (s7g / 改为-01
        :ARG1 (s7x / 小报
            :name (s7n3 / name
                :op1 "《"
                :op2 "国家"
                :op3 "询问"
                :op4 "报"
                :op5 "》")
            :mod (s7z / 八卦)
            :possessor s7p)
        :source (s7b2 / 版面
            :mod (s7h3 / 黑白))
        :ARG2 (s7b3 / 版面
            :mod (s7c2 / 彩色))
        :aspect performance)
    :purpose (s7y / 运用-01
        :ARG0 s7p
        :ARG1 (s7j / 印刷机
            :mod (s7h4 / 黑白)
            :ARG1-of (s7l / 遗留-01
                :aspect state))
        :manner (s7q / 充分)
        :aspect process)
    :purpose (s7r / 容纳-01
        :ARG0 s7w
        :ARG1 (s7a / 文章
            :mod (s7e / 那些)
            :ARG0-of (s7f2 / 符合-01
                :polarity -
                :ARG1 (s7s / 标准
                    :possessor s7x)
                :aspect state))
        :aspect habitual)
    :aspect performance)


# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :before s7c)
               (s7c :overlap s7g)
               (s7c :after s7y)
               (s7c :after s7r)
               (s7r :overlap s7f2)
               (s7y :overlap s7l))
    :modal ((root :modal author)
            (author :full-affirmative s7c)
            (author :full-affirmative s7g)
            (author :full-affirmative s7l)
            (s7c :unspecified s7y)
            (s7c :unspecified s7r)
            (author :full-negative s7f2))
    :coref ((s6c :same-event s7c)
            (s6p :same-entity s7w)))


################################################################################
# meta-info
# :: snt8
Index: 1 2 3 4 5 6 7 8 9
Words: 黑白 印刷 也 成 了 该刊 的 特色 。

# sentence level graph:
(s8c / 成-01
    :ARG1 (s8y / 印刷-01
        :mod (s8h / 黑白)
        :aspect process)
    :ARG2 (s8t / 特色
        :possessor (s8k / newspaper
            :mod (s8g / 该)))
    :mod (s8m / 也)
    :aspect performance)


# document level annotation:
(s8s0 / sentence
    :temporal ((document-creation-time :before s8c)
               (s8c :overlap s8y))
    :modal ((root :modal author)
            (author :full-affirmative s8c)
            (author :full-affirmative s8y))
    :coref ((s7w :same-entity s8k)))


################################################################################
# meta-info
# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。

# sentence level graph:
(s9a / 达到-01
    :ARG1 (s9f / 发行量
        :possessor (s9p / newspaper
            :name (s9n / name
                :op1 "《"
                :op2 "世界"
                :op3 "新闻"
                :op4 "周报"
                :op5 "》")))
    :ARG2 (s9t / thing
        :quant 1200000
        :unit (s9u / 份))
    :temporal (s9d / date-entity
        :decade 1980)
    :aspect performance)


# document level annotation:
(s9s0 / sentence
    :temporal ((root :depends-on s9d)
               (s9d :contained s9a))
    :modal ((root :modal author)
            (author :full-affirmative s9a))
    :coref ((s8k :same-entity s9p)))


################################################################################
# meta-info
# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Words: 不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。

# sentence level graph:
(s10b / but-91
    :ARG2 (s10f / 跌-01
        :ARG1 (s10l / 发行量
            :possessor (s10k / newspaper
                :mod (s10g / 该)))
        :ARG4 (s10t / thing
            :quant 83000
            :unit (s10u / 份))
        :mod (s10y / 已经)
        :temporal (s10d / date-entity
            :year 2007)
        :aspect performance))


# document level annotation:
(s10s0 / sentence
    :temporal ((root :depends-on s10d)
               (s10d :contained s10f))
    :modal ((root :modal author)
            (author :full-affirmative s10b)
            (author :full-affirmative s10f))
    :coref ((s9p :same-entity s10k)))



</annotation>

# The gold annotation
<gold>
################################################################################
# meta-info
# :: snt6
Index: 1 2 3 4 5 6 7 8 9 10
Words: 《 世界 新闻 周报 》 创刊 于 1979 年 。

# sentence level graph:
(s6x / 创刊-01
    :ARG0 (s6n / newspaper
        :name (s6n2 / name
            :op1 "《"
            :op2 "世界"
            :op3 "新闻"
            :op4 "周报"
            :op5 "》"))
    :temporal (s6d / date-entity
        :year 1979)
    :aspect performance)


# document level annotation:
(s6s0 / sentence
    :temporal ((document-creation-time :before s6d)
               (s6d :overlap s6x))
    :modal ((root :modal author)
            (author :full-affirmative s6x)))


################################################################################
# meta-info
# :: snt7
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
Words: 创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。

# sentence level graph:
(s7h / have-reason-91
    :ARG1 (s7h2 / have-purpose-91
        :ARG1 (s7x13 / 创立-01
            :ARG0 (s7i3 / individual-person
                :name (s7n5 / name
                    :op1 "格内洛索"
                    :op2 "·"
                    :op3 "波普")
                :ARG1-of (s7h3 / have-org-role-91
                    :ARG3 (s7x22 / 人
                        :ARG0-of (s7x23 / 创始-00
                            :aspect performance))))
            :ARG1 (s7x14 / 版面
                :mod (s7x15 / 黑白)
                :part-of (s7n3 / newspaper
                    :name (s7n4 / name
                        :op1 "《"
                        :op2 "世界"
                        :op3 "新闻"
                        :op4 "周报"
                        :op5 "》"))
                :ARG0-of (s7x17 / 容纳-01
                    :ARG1 (s7x18 / 文章
                        :mod (s7x19 / 那些)
                        :ARG0-of (s7x20 / 符合-01
                            :ARG1 (s7x21 / 标准
                                :possessor s7n)
                            :aspect state
                            :polarity -))
                    :aspect process))
            :aspect performance)
        :ARG2 (s7x8 / 运用-01
            :ARG1 (s7x10 / 印刷机
                :mod (s7x11 / 黑白)
                :ARG1-of (s7x12 / 遗留-01
                    :aspect performance))
            :manner (s7x9 / 充分)
            :aspect activity)
        :aspect state)
    :ARG2 (s7x / 改为-01
        :ARG1 (s7x4 / 版面
            :part-of (s7n / newspaper
                :name (s7n2 / name
                    :op1 "《"
                    :op2 "国家"
                    :op3 "询问"
                    :op4 "报"
                    :op5 "》")
                :ARG1-of (s7i2 / identity-91
                    :ARG2 (s7x5 / 小报
                        :mod (s7x6 / 旗下)
                        :mod (s7x7 / 八卦))))
            :mod (s7x16 / 黑白))
        :ARG2 (s7x2 / 版面
            :mod (s7x3 / 彩色))
        :aspect performance)
    :aspect state)


# document level annotation:
(s7s0 / sentence
    :temporal ((document-creation-time :before s7x13)
               (s7x13 :overlap s7x23)
               (s7x13 :overlap s7x17)
               (s7x17 :overlap s7x20)
               (s7x13 :overlap s7x8)
               (s7x8 :before s7x12)
               (s7x13 :before s7x))
    :modal ((root :modal author)
            (author :full-affirmative s7x23)
            (author :full-negative s7x20)
            (author :full-affirmative s7x17)
            (author :full-affirmative s7x13)
            (author :full-affirmative s7x12)
            (author :full-affirmative s7x8)
            (author :full-affirmative s7h2)
            (author :full-affirmative s7x)
            (author :full-affirmative s7h))
    :coref ((s6n :same-entity s7n3)))


################################################################################
# meta-info
# :: snt8
Index: 1 2 3 4 5 6 7 8 9
Words: 黑白 印刷 也 成 了 该刊 的 特色 。

# sentence level graph:
(s8x / 成-01
    :ARG0 (s8x2 / 印刷-01
        :manner (s8x3 / 黑白)
        :aspect habitual)
    :ARG1 (s8x4 / 特色
        :possessor (s8x5 / 刊
            :mod (s8x6 / 该)))
    :mod (s8x7 / 也)
    :aspect performance)


# document level annotation:
(s8s0 / sentence
    :temporal ((s7x13 :overlap s8x)
               (s8x :overlap s8x2))
    :modal ((root :modal author)
            (author :full-affirmative s8x2)
            (author :full-affirmative s8x))
    :coref ((s7n3 :same-entity s8x5)))


################################################################################
# meta-info
# :: snt9
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Words: 在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。

# sentence level graph:
(s9x / 达到-01
    :ARG0 (s9x2 / 量
        :quant-of (s9x3 / 发行-01
            :ARG1 (s9n / newspaper
                :name (s9n2 / name
                    :op1 "《"
                    :op2 "世界"
                    :op3 "新闻"
                    :op4 "周报"
                    :op5 "》")))
        :ARG1-of (s9h / have-quant-91
            :ARG2 1200000
            :unit (s9x4 / 份)))
    :temporal (s9d / date-entity
        :era 1980)
    :aspect performance)


# document level annotation:
(s9s0 / sentence
    :temporal ((document-creation-time :before s9d)
               (s9d :overlap s9x)
               (s9x :overlap s9x3))
    :modal ((root :modal author)
            (author :full-affirmative s9x))
    :coref ((s8x5 :same-entity s9n)))


################################################################################
# meta-info
# :: snt10
Index: 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Words: 不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。

# sentence level graph:
(s10x / 跌-01
    :ARG0 (s10x2 / 量
        :quant-of (s10x3 / 发行-01
            :ARG1 (s10x4 / 刊
                :mod (s10x5 / 该)))
        :ARG1-of (s10h / have-quant-91
            :ARG2 83000
            :unit (s10x7 / 份)))
    :temporal (s10d / date-entity
        :year 2007)
    :mod (s10x6 / 已经)
    :aspect performance)


# document level annotation:
(s10s0 / sentence
    :temporal ((document-creation-time :before s10d)
               (s10d :overlap s10x)
               (s10x :overlap s10x3))
    :modal ((root :modal author)
            (author :full-affirmative s10x))
    :coref ((s9n :same-entity s10x4)))



</gold>

# umrjudge per check on these sentences (recall / precision / F1, percent)
a_event_found: R 80 / P 100 / F 89
a_event_concept: R 75 / P 75 / F 75
a_entity_found: R 94 / P 100 / F 97
a_entity_concept: R 79 / P 79 / F 79
a_granularity: R 100 / P 100 / F 100
b_event_sense: R 100 / P 100 / F 100
c_aspect: R 58 / P 64 / F 61
c_polarity: R 100 / P 100 / F 100
c_other_attributes: R 50 / P 29 / F 36
d_core_args_event: R 44 / P 48 / F 46
d_core_args_abstract: R 22 / P 67 / F 33
d_peripheral_event: R 62 / P 56 / F 59
d_peripheral_entity: R 75 / P 68 / F 71
e_core_labels: R 62 / P 62 / F 62
e_peripheral_labels: R 94 / P 94 / F 94
f_name_tokens: R 50 / P 40 / F 44
g_reentrancy: R 0 / P 0 / F 0
h_temporal: R 18 / P 21 / F 19
i_modal: R 67 / P 77 / F 71
j_coref_chain: R 48 / P 34 / F 40
k_doc_format: R 100 / P 100 / F 100

# The units umrjudge did not count as correct (check, verdict, unit: gold -> annotation, detail)
a_event_found | missing | s7h: have-reason-91 -> - | no node in the prediction matches it
a_event_found | missing | s7x23: 创始 -> - | no node in the prediction matches it
a_event_found | missing | s7i2: identity-91 -> - | no node in the prediction matches it
a_event_concept | wrong | s7h2: have-purpose -> 版面 | have-purpose -> 版面
a_entity_found | missing | s7n3: newspaper -> - | no node in the prediction matches it
a_entity_found | missing | s7x6: 旗下 -> - | no node in the prediction matches it
a_entity_concept | wrong | s7i3: individual-person -> person | individual-person -> person
a_entity_concept | wrong | s7x22: 人 -> 创始人 | 人 -> 创始人
a_entity_concept | wrong | s7x14: 版面 -> name | 版面 -> name
c_aspect | missing | s7h2:aspect: state -> - | the prediction has no :aspect
c_aspect | wrong | s7x17:aspect: process -> habitual | process -> habitual
c_aspect | wrong | s7x8:aspect: activity -> process | activity -> process
c_aspect | wrong | s7x12:aspect: performance -> state | performance -> state
c_other_attributes | extra | s7x14:op1: - -> 格内洛索 | gold has no :op1
c_other_attributes | extra | s7x14:op2: - -> 波普 | gold has no :op2
d_core_args_event | partial | s7x13: arg0 s7i3/individual-person; arg1 s7x14/版面 -> arg0 s7i3/individual-person | missing arg1 s7x14/版面
d_core_args_event | partial | s7x17: arg0 s7x14/版面; arg1 s7x18/文章 -> arg1 s7x18/文章 | missing arg0 s7x14/版面
d_core_args_event | partial | s7x: arg1 s7x4/版面; arg2 s7x2/版面 -> arg1 s7x5/小报; arg2 s7x2/版面 | missing arg1 s7x4/版面; extra arg1 s7x5/小报
d_core_args_abstract | missing | s7h2: arg1 s7x13/创立-01; arg2 s7x8/运用-01 -> - | missing arg1 s7x13/创立-01; missing arg2 s7x8/运用-01
d_core_args_abstract | partial | s7h3: arg1 s7i3/individual-person; arg3 s7x22/人 -> arg1 s7i3/individual-person; arg2 s7n/newspaper; arg3 s7x22/人 | extra arg2 s7n/newspaper
d_peripheral_event | extra | s7x13: - -> purpose s7x17/容纳-01; purpose s7x8/运用-01 | extra purpose s7x17/容纳-01; extra purpose s7x8/运用-01
d_peripheral_event | extra | s7x: - -> source s7x4/版面 | extra source s7x4/版面
d_peripheral_entity | missing | s7x14: mod s7x15/黑白 -> - | missing mod s7x15/黑白
d_peripheral_entity | wrong | s7n: part s7x4/版面 -> mod s7h2/have-purpose-91 | missing part s7x4/版面; extra mod s7h2/have-purpose-91
d_peripheral_entity | partial | s7x5: mod s7x6/旗下; mod s7x7/八卦 -> mod s7x7/八卦 | missing mod s7x6/旗下
e_core_labels | wrong | s7x -arg1-> s7x4: arg1 -> source | arg1 -> source
f_name_tokens | wrong | s7i3: 格内洛索 · 波普 -> 格内洛索 波普 | 格内洛索 · 波普 -> 格内洛索 波普
f_name_tokens | wrong | s7n: 《 国家 询问 报 》 -> 《 世界 新闻 周报 》 | 《 国家 询问 报 》 -> 《 世界 新闻 周报 》
f_name_tokens | extra | s7x5: - -> 《 国家 询问 报 》 | gold has no :name
g_reentrancy | missing | s7x21/标准 -possessor-> s7n/newspaper: s7x21/标准 -possessor-> s7n/newspaper -> - | the prediction has no such edge
g_reentrancy | extra | s7c/创立-01 -arg1-> s7w/newspaper: - -> s7c/创立-01 -arg1-> s7w/newspaper | gold has no such reentrancy
g_reentrancy | extra | s7r/容纳-01 -arg0-> s7w/newspaper: - -> s7r/容纳-01 -arg0-> s7w/newspaper | gold has no such reentrancy
g_reentrancy | extra | s7s/标准 -possessor-> s7x/小报: - -> s7s/标准 -possessor-> s7x/小报 | gold has no such reentrancy
g_reentrancy | extra | s7x/小报 -possessor-> s7p/person: - -> s7x/小报 -possessor-> s7p/person | gold has no such reentrancy
g_reentrancy | extra | s7y/运用-01 -arg0-> s7p/person: - -> s7y/运用-01 -arg0-> s7p/person | gold has no such reentrancy
a_entity_concept | wrong | s8x5: 刊 -> newspaper | 刊 -> newspaper
c_aspect | wrong | s8x2:aspect: habitual -> process | habitual -> process
d_core_args_event | wrong | s8x: arg0 s8x2/印刷-01; arg1 s8x4/特色 -> arg1 s8x2/印刷-01; arg2 s8x4/特色 | arg0 s8x2/印刷-01: predicted as arg1; arg1 s8x4/特色: predicted as arg2
d_peripheral_event | wrong | s8x2: manner s8x3/黑白 -> mod s8x3/黑白 | manner s8x3/黑白: predicted as mod
e_core_labels | wrong | s8x -arg0-> s8x2: arg0 -> arg1 | arg0 -> arg1
e_core_labels | wrong | s8x -arg1-> s8x4: arg1 -> arg2 | arg1 -> arg2
e_peripheral_labels | wrong | s8x2 -manner-> s8x3: manner -> mod | manner -> mod
a_event_found | missing | s9h: have-quant-91 -> - | no node in the prediction matches it
a_event_concept | wrong | s9x3: 发行 -> 发行量 | 发行 -> 发行量
a_entity_concept | wrong | s9x2: 量 -> thing | 量 -> thing
c_other_attributes | extra | s9x2:quant: - -> 1200000 | gold has no :quant
c_other_attributes | extra | s9d:decade: - -> 1980 | gold has no :decade
c_other_attributes | missing | s9d:era: 1980 -> - | the prediction has no :era
d_core_args_event | wrong | s9x: arg0 s9x2/量 -> arg1 s9x3/发行-01; arg2 s9x2/量 | arg0 s9x2/量: predicted as arg2; extra arg1 s9x3/发行-01
d_core_args_event | missing | s9x3: arg1 s9n/newspaper -> - | missing arg1 s9n/newspaper
d_peripheral_event | wrong | s9x3: quant s9x2/量 -> possessor s9n/newspaper | missing quant s9x2/量; extra possessor s9n/newspaper
d_peripheral_entity | extra | s9x2: - -> unit s9x4/份 | extra unit s9x4/份
e_core_labels | wrong | s9x -arg0-> s9x2: arg0 -> arg2 | arg0 -> arg2
e_core_labels | wrong | s9x3 -arg1-> s9n: arg1 -> possessor | arg1 -> possessor
a_event_concept | wrong | s10x3: 发行 -> but | 发行 -> but
a_event_concept | wrong | s10h: have-quant -> thing | have-quant -> thing
a_entity_concept | wrong | s10x2: 量 -> 发行量 | 量 -> 发行量
a_entity_concept | wrong | s10x4: 刊 -> newspaper | 刊 -> newspaper
c_other_attributes | missing | s10h:arg2: 83000 -> - | the prediction has no :arg2
c_other_attributes | extra | s10h:quant: - -> 83000 | gold has no :quant
d_core_args_event | wrong | s10x: arg0 s10x2/量 -> arg1 s10x2/量; arg4 s10h/have-quant-91 | arg0 s10x2/量: predicted as arg1; extra arg4 s10h/have-quant-91
d_core_args_event | wrong | s10x3: arg1 s10x4/刊 -> arg2 s10x/跌-01 | missing arg1 s10x4/刊; extra arg2 s10x/跌-01
d_core_args_abstract | missing | s10h: arg1 s10x2/量 -> - | missing arg1 s10x2/量
d_peripheral_event | missing | s10x3: quant s10x2/量 -> - | missing quant s10x2/量
d_peripheral_entity | extra | s10x2: - -> possessor s10x4/刊 | extra possessor s10x4/刊
e_core_labels | wrong | s10x -arg0-> s10x2: arg0 -> arg1 | arg0 -> arg1
h_temporal | wrong | date-entity (snt6 s6d = pred s6d): document-creation-time :before date-entity (snt6 s6d = pred s6d) -> root :depends-on date-entity (snt6 s6d = pred s6d) | wrong parent and relation
h_temporal | wrong | 创刊-01 «创刊» (snt6 s6x = pred s6c): date-entity (snt6 s6d = pred s6d) :overlap 创刊-01 «创刊» (snt6 s6x = pred s6c) -> date-entity (snt6 s6d = pred s6d) :contained 创刊-01 «创刊» (snt6 s6x = pred s6c) | right parent, wrong relation
h_temporal | wrong | 改为-01 «改为» (snt7 s7x = pred s7g): 创立-01 «创立» (snt7 s7x13 = pred s7c) :before 改为-01 «改为» (snt7 s7x = pred s7g) -> 创立-01 «创立» (snt7 s7x13 = pred s7c) :overlap 改为-01 «改为» (snt7 s7x = pred s7g) | right parent, wrong relation
h_temporal | wrong | 遗留-01 «遗留» (snt7 s7x12 = pred s7l): 运用-01 «运用» (snt7 s7x8 = pred s7y) :before 遗留-01 «遗留» (snt7 s7x12 = pred s7l) -> 运用-01 «运用» (snt7 s7x8 = pred s7y) :overlap 遗留-01 «遗留» (snt7 s7x12 = pred s7l) | right parent, wrong relation
h_temporal | wrong | 容纳-01 «容纳» (snt7 s7x17 = pred s7r): 创立-01 «创立» (snt7 s7x13 = pred s7c) :overlap 容纳-01 «容纳» (snt7 s7x17 = pred s7r) -> 创立-01 «创立» (snt7 s7x13 = pred s7c) :after 容纳-01 «容纳» (snt7 s7x17 = pred s7r) | right parent, wrong relation
h_temporal | missing | 创始 «创始人» (snt7 s7x23): 创立-01 «创立» (snt7 s7x13 = pred s7c) :overlap 创始 «创始人» (snt7 s7x23) -> - | the prediction has no node for it (its sentence graph lacks it)
h_temporal | wrong | 运用-01 «运用» (snt7 s7x8 = pred s7y): 创立-01 «创立» (snt7 s7x13 = pred s7c) :overlap 运用-01 «运用» (snt7 s7x8 = pred s7y) -> 创立-01 «创立» (snt7 s7x13 = pred s7c) :after 运用-01 «运用» (snt7 s7x8 = pred s7y) | right parent, wrong relation
h_temporal | wrong | 成-01 «成» (snt8 s8x = pred s8c): 创立-01 «创立» (snt7 s7x13 = pred s7c) :overlap 成-01 «成» (snt8 s8x = pred s8c) -> document-creation-time :before 成-01 «成» (snt8 s8x = pred s8c) | wrong parent and relation
h_temporal | wrong | date-entity (snt9 s9d = pred s9d): document-creation-time :before date-entity (snt9 s9d = pred s9d) -> root :depends-on date-entity (snt9 s9d = pred s9d) | wrong parent and relation
h_temporal | wrong | 达到-01 «达到» (snt9 s9x = pred s9a): date-entity (snt9 s9d = pred s9d) :overlap 达到-01 «达到» (snt9 s9x = pred s9a) -> date-entity (snt9 s9d = pred s9d) :contained 达到-01 «达到» (snt9 s9x = pred s9a) | right parent, wrong relation
h_temporal | missing | 发行-01 «发行量» (snt9 s9x3 = pred s9f): 达到-01 «达到» (snt9 s9x = pred s9a) :overlap 发行-01 «发行量» (snt9 s9x3 = pred s9f) -> - | the prediction gives this node no temporal parent
h_temporal | wrong | date-entity (snt10 s10d = pred s10d): document-creation-time :before date-entity (snt10 s10d = pred s10d) -> root :depends-on date-entity (snt10 s10d = pred s10d) | wrong parent and relation
h_temporal | wrong | 跌-01 «跌至» (snt10 s10x = pred s10f): date-entity (snt10 s10d = pred s10d) :overlap 跌-01 «跌至» (snt10 s10x = pred s10f) -> date-entity (snt10 s10d = pred s10d) :contained 跌-01 «跌至» (snt10 s10x = pred s10f) | right parent, wrong relation
h_temporal | missing | 发行-01 «发行量» (snt10 s10x3 = pred s10b): 跌-01 «跌至» (snt10 s10x = pred s10f) :overlap 发行-01 «发行量» (snt10 s10x3 = pred s10b) -> - | the prediction gives this node no temporal parent
i_modal | missing | have-reason-91 (snt7 s7h): author :full-affirmative have-reason-91 (snt7 s7h) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | missing | have-purpose-91 (snt7 s7h2 = pred s7b): author :full-affirmative have-purpose-91 (snt7 s7h2 = pred s7b) -> - | the prediction gives this node no modal parent
i_modal | wrong | 容纳-01 «容纳» (snt7 s7x17 = pred s7r): author :full-affirmative 容纳-01 «容纳» (snt7 s7x17 = pred s7r) -> 创立-01 «创立» (snt7 s7x13 = pred s7c) :unspecified 容纳-01 «容纳» (snt7 s7x17 = pred s7r) | wrong parent and relation
i_modal | missing | 创始 «创始人» (snt7 s7x23): author :full-affirmative 创始 «创始人» (snt7 s7x23) -> - | the prediction has no node for it (its sentence graph lacks it)
i_modal | wrong | 运用-01 «运用» (snt7 s7x8 = pred s7y): author :full-affirmative 运用-01 «运用» (snt7 s7x8 = pred s7y) -> 创立-01 «创立» (snt7 s7x13 = pred s7c) :unspecified 运用-01 «运用» (snt7 s7x8 = pred s7y) | wrong parent and relation
i_modal | extra | 发行-01 «发行量» (snt10 s10x3 = pred s10b): - -> author :full-affirmative 发行-01 «发行量» (snt10 s10x3 = pred s10b) | gold gives this node no modal parent
j_coref_chain | partial | newspaper (snt6 s6n = pred s6p): newspaper (snt7 s7n3); 刊 «该刊» (snt8 s8x5 = pred s8k); newspaper (snt9 s9n = pred s9p); 刊 «该刊» (snt10 s10x4 = pred s10k) -> newspaper (snt7 s7n = pred s7w); 刊 «该刊» (snt8 s8x5 = pred s8k); newspaper (snt9 s9n = pred s9p); 刊 «该刊» (snt10 s10x4 = pred s10k) | not linked to: newspaper (snt7 s7n3); wrongly linked to: newspaper (snt7 s7n = pred s7w)
j_coref_chain | extra | 创刊-01 «创刊» (snt6 s6x = pred s6c): - -> 创立-01 «创立» (snt7 s7x13 = pred s7c) | gold links it to nothing
j_coref_chain | extra | newspaper (snt7 s7n = pred s7w): - -> newspaper (snt6 s6n = pred s6p); 刊 «该刊» (snt8 s8x5 = pred s8k); newspaper (snt9 s9n = pred s9p); 刊 «该刊» (snt10 s10x4 = pred s10k) | gold links it to nothing
j_coref_chain | missing | newspaper (snt7 s7n3): newspaper (snt6 s6n = pred s6p); 刊 «该刊» (snt8 s8x5 = pred s8k); newspaper (snt9 s9n = pred s9p); 刊 «该刊» (snt10 s10x4 = pred s10k) -> - | the prediction has no node for it (its sentence graph lacks it)
j_coref_chain | extra | 创立-01 «创立» (snt7 s7x13 = pred s7c): - -> 创刊-01 «创刊» (snt6 s6x = pred s6c) | gold links it to nothing
j_coref_chain | partial | 刊 «该刊» (snt8 s8x5 = pred s8k): newspaper (snt7 s7n3); newspaper (snt9 s9n = pred s9p); newspaper (snt6 s6n = pred s6p); 刊 «该刊» (snt10 s10x4 = pred s10k) -> newspaper (snt7 s7n = pred s7w); newspaper (snt9 s9n = pred s9p); newspaper (snt6 s6n = pred s6p); 刊 «该刊» (snt10 s10x4 = pred s10k) | not linked to: newspaper (snt7 s7n3); wrongly linked to: newspaper (snt7 s7n = pred s7w)
j_coref_chain | partial | newspaper (snt9 s9n = pred s9p): 刊 «该刊» (snt8 s8x5 = pred s8k); 刊 «该刊» (snt10 s10x4 = pred s10k); newspaper (snt7 s7n3); newspaper (snt6 s6n = pred s6p) -> 刊 «该刊» (snt8 s8x5 = pred s8k); 刊 «该刊» (snt10 s10x4 = pred s10k); newspaper (snt7 s7n = pred s7w); newspaper (snt6 s6n = pred s6p) | not linked to: newspaper (snt7 s7n3); wrongly linked to: newspaper (snt7 s7n = pred s7w)
j_coref_chain | partial | 刊 «该刊» (snt10 s10x4 = pred s10k): newspaper (snt9 s9n = pred s9p); 刊 «该刊» (snt8 s8x5 = pred s8k); newspaper (snt7 s7n3); newspaper (snt6 s6n = pred s6p) -> newspaper (snt9 s9n = pred s9p); 刊 «该刊» (snt8 s8x5 = pred s8k); newspaper (snt7 s7n = pred s7w); newspaper (snt6 s6n = pred s6p) | not linked to: newspaper (snt7 s7n3); wrongly linked to: newspaper (snt7 s7n = pred s7w)

# Your answer
For each problem: the pattern, its cost (which checks, how many units), why it happens, and the change to the instruction.