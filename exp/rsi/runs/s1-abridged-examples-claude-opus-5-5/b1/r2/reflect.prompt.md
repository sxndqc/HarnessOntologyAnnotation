<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 18457). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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
in PropBank is `<word>-00`. Entities and modifiers are the word itself, lemmatized in English (`doctor`, `health`) and as
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

When the text has a lexical verb that is in Chinese PropBank (属, 拥有), use that verb with its frame's roles instead of `belong-91` / `have-91`. Superlatives and comparatives (最, 更, *most, more*) use `(have-degree-91 :ARG1 X :ARG2 <property> :ARG3 (最))`, not `:degree`.

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
- Do not add arguments (agents, possessors) that the text does not express or clearly imply.
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

Aspect cues: recurring activities of a publication or institution (发行, 报导, 综合) are `habitual`, even with 了. 已经 + 停止 or another end verb used to describe an entity is `state` (the resulting state). Passive naming (被称为) is `performance`.

Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them
only when they are clear.

### 4.2 Polarity, mode, degree, quantity

- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is
  then negative (5.2).
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
  (*nowadays*, 现在) on `past-reference` / `present-reference` / `future-reference`.
- Then every event: (1) a time expression of its clause, if there is one (`(s1t :contained s1e)`); else
  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)
  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a
  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from
  context, 了, 过, 将, 会.
- An event in a complement clause takes its matrix event as parent; a purpose is `:after` its main event.
- Anchor only the **main event** of a sentence to `document-creation-time` (or to a time expression of its clause). Attach every other event of the sentence to that main event or to a nearby event, usually `:overlap` (`:contained` if it lies inside it, `:before`/`:after` when the order is clear). Events inside relative clauses, modifiers and event nominals also need a parent, normally their governing event with `:overlap`. Leave no event without a temporal parent.
- Copular abstract predicates (`identity-91`, `have-mod-91`, `have-*-91`) normally get **no** temporal parent.
- A relative time word such as 目前 or 现在 is a time node attached as `(document-creation-time :depends-on <node>)`. Do not attach it to `present-reference`. Then chain the events from it with `:overlap`.

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
- `(earlier :same-event later)`: two mentions of the same event.
- `(a :subset-of b)`: the entity or event a is a subset or part of b.
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

## Examples

- Temporal chain (5.1): 目前…发行…网络版 → `(document-creation-time :depends-on s4x) (s4x :overlap s4x2) (s4x2 :overlap s4x6)`. The other events of a sentence hang from its main event: `(document-creation-time :before s1x3) (s1x3 :overlap s1x4)`.
- Classifier (2.2): 一个节目 → `(节目 :quant 1 :unit (个))`.
- Adverb (3): 已经停止 → `(停止-01 :mod (已经) :aspect state)`; 曾经 → `:temporal (曾经)`.
- Name (2.2): 美国…小报 → `(小报 :place (country :name (name :op1 "美国")))`, with no `:wiki`.
- Reason (2.5): 以报导…而闻名 → `(闻名-01 :reason (报导-01 ...))`.
- Lexical verb (2.3): 节目属周报 → `(属-02 :ARG0 节目 :ARG1 周报)`, not `belong-91`.
- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`.

</instruction>

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 84.8)
<critique>
# Review of the annotator's UMR for the 《世界新闻周报》 document: what in the instruction to change

Most of the lost score is in **temporal** (F 50) and **coreference** (chain P 56, subset P 0). After those come a few local graph errors in sentences 4 and 5. Two of the costliest patterns come from the instruction itself: one of its examples is wrong, and one of its rules is too broad.

## 1. Temporal anchoring: the wrong main event, and a wrong example (h_temporal, about 8 units)

**What went wrong.**
- **Sentence 1** (是…已经停止发行的…小报，以报导…而闻名):
  - The root is `identity-91`, so the annotator had no verbal main event. It anchored two events to the document creation time (DCT): `(document-creation-time :overlap s1x5 停止)` and `(document-creation-time :overlap s1x7 闻名)`. It also hung 报导 from 闻名.
  - Gold anchors the first real event, 发行, and hangs everything else from it: `(document-creation-time :before s1x3 发行) (s1x3 :overlap s1x4 停止) (s1x7 闻名 :contained s1x3) (s1x3 :overlap s1x8 报导)`.
  - That is 4 units in one sentence.
- **Sentence 4** (目前…纸本已经停刊，不过仍继续发行网络版):
  - Annotation: `(document-creation-time :depends-on s4x 目前) (s4x :overlap s4x2 停刊)`.
  - Gold: `(document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`. 目前 gets **no** temporal parent.
  - The instruction's own example, "目前…发行…网络版 → `(document-creation-time :depends-on s4x) (s4x :overlap s4x2)…`", was clearly copied from this gold. But it misread `s4x` as 目前; in gold it is the event 停刊. The rule in 5.1 ("a relative time word such as 目前 … attached as `(document-creation-time :depends-on <node>)`") was built on that misreading. The annotator followed it faithfully.
- **Sentence 5**: gold has `(document-creation-time :depends-on s5x 称为)`; the annotation has `:before`. This is the same pattern as sentence 4: in these sentences gold links the main event to DCT with `:depends-on`.
- **Sentence 2**: 查证 was attached to 综合. Gold attaches it to its governing event: `(s2x8 经 :overlap s2x13 查证)`. The instruction already says "normally their governing event". The annotator did not follow it here.

**Changes to the instruction.**
- **Fix the example** to: `目前…停刊…继续发行 → (document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`.
- **Rewrite the 目前/现在 rule**: "A relative time word such as 目前 or 现在 is a `:temporal` node in the graph but gets no temporal parent of its own. Link the main event of its clause to `document-creation-time` with `:depends-on`, then chain the other events from that main event with `:overlap`."
- **Add a rule for copular sentences**: "When the root is an abstract predicate (`identity-91`, `have-mod-91`), anchor to DCT the first event inside it, usually a relative-clause event such as 发行. Hang every other event from that event: an end verb (停止) `:overlap`; a reputation or state that holds within it (闻名) `:contained`; a co-occurring activity (报导) `:overlap`. Do not anchor more than one event of a sentence to DCT."
- **Stress the governing-event rule**: "An event that modifies a noun hangs from the event whose argument that noun is (查证 in 程序 → 经), not from the sentence's first event."

## 2. Too many coreference and subset links (j_coref_chain 4 extra units, j_coref_subset 1 extra)

**What went wrong.**
- `(s1x4 :same-event s4x6)`: 发行 in sentence 1 is the publication that stopped; 发行 in sentence 4 is the still-continuing publication of the online edition. These are different events.
- `(s2x9 :same-entity s5x9)`: 许多内容 (much of the content, not verified) and 荒诞不经的内容 (its absurd content) are different sets.
- `(s2x9 :subset-of s2a2)`: a within-sentence `:subset-of` link, which gold does not use.

**Why.** Section 5.3 tells the annotator to link mentions but gives it no reason to hold back, so it linked repeated words.

**Change.** Add: "Link two mentions only when they pick out the same individual or the same single event. Do not link two mentions of the same verb that have different arguments, times or polarity (发行 of the print edition vs 发行 of the online edition). Do not link two noun phrases with the same head but different restrictors (许多内容 vs 荒诞不经的内容). Do not put a `:subset-of` triple inside one sentence. When in doubt, leave the link out: the newspaper chain (周报 / 该周报 / 《世界新闻周报》) is the kind of chain gold annotates."

## 3. The "已经 + end verb = state" rule was over-applied (c_aspect 1 unit; it also cost the 停刊 temporal unit)

**What went wrong.** In sentence 4, 已经停刊 is a main predicate. The annotator gave it `:aspect state`; gold has `:aspect performance`.

**Why.** The 4.1 cue was meant for sentence 1's relative clause (已经停止发行的小报), where `state` is right. The annotator applied it to a main predicate.

**Change.** Narrow the cue: "only when 已经 + 停止/停刊 sits in a relative clause that describes an entity (…的 N). As the main predicate, 已经 + an end verb is `performance`."

## 4. Roles invented or mislabelled in sentence 4 (d_core_args / e_core_labels / d_peripheral / g_reentrancy, about 6 units)

**What went wrong.**
- 纸本 of 停刊: annotation `:ARG1`; gold `:ARG0`.
- 《世界新闻周报》的纸本: annotation `:possessor`; gold `(纸本 :part-of (newspaper …))`.
- The annotator added `:ARG0 s4n` to 发行-01, but the text gives no subject. Gold has `(发行-01 :ARG1 (网络版) :aspect habitual)` only.

**Changes to the instruction.**
- Add: "An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor`."
- Add: "For a `-01` sense of an intransitive verb that is not in PropBank (停刊, 停业), the sole participant is `:ARG0`."
- Repeat the existing rule with this case: "Do not fill the subject of a second clause with an entity from the first clause (…，不过仍继续发行网络版 has no `:ARG0`)."

## 5. Superlative scope and concept form in sentence 5 (a_event_concept 1, a_entity_found 1, d_core_args_abstract 1, d_peripheral 1, c_aspect 1)

**What went wrong.**
- 称为: the annotator wrote `称-01`; gold has `称为-01`. A Chinese concept should keep the verb as written.
- 美国历史上: the annotator made it `:ARG4` of `have-degree-91`. Gold has `(报纸 :temporal (上 :op1 (历史 :place (country …))))`.
- `have-degree-91` was given `:aspect state`. Gold gives it no aspect.

**Changes to the instruction.**
- Add: "Keep compound verbs whole (称为 → `称为-01`, not `称-01`)."
- Add: "A 在/…上 frame such as 历史上 is `:temporal (上 :op1 (历史))` on the noun. It is not `:ARG4` of `have-degree-91`."
- Add: "`have-degree-91` gets no `:aspect`." Gold annotations generally treat it as an abstract predicate with no aspect; this sentence is an example.

## 6. Smaller items (about 1–2 units each)

- **The `identity-91` root needs a modal triple.** Gold has `(author :full-affirmative s1i2)`. Add: "In the modal list, the root abstract predicate of an asserted sentence gets `(author :full-affirmative …)`, even though it gets no temporal parent." The temporal rule ("Copular abstract predicates … normally get **no** temporal parent") is right; keep it.
- **程序 with an event-noun modifier.** 新闻查证程序 in gold is `(程序 :ARG0-of (identity-91 :ARG1 (查证-01 …)))`, not `:mod 查证-01`. Add a line: when an event noun names what the head noun *is* (the procedure is the verification), use `identity-91`.
- **未经 in gold has no `:polarity -` and has aspect `process`, while its modal is `full-negative`.** Other gold sentences (未被录取, 并未受伤) do use `:polarity -` together with full-negative. So this one is a gold quirk. Keep the current polarity rule.

## What the instruction should keep

The annotator got these right, and the matching rules should stay as they are:

- **Named entities**: bracketed names split into words with 《 》 as their own `:opN`, no `:wiki`, `newspaper` as the type, and 美国 as `:place` on 小报. f_name_tokens scored 100.
- **Classifiers** as `:quant` + `:unit` (一份 → 份, 一个 → 个).
- **以…而闻名** as `(闻名-01 :reason 报导-01)` with no extra `and`.
- **Lexical verbs** used instead of abstract predicates: `属-02` and `拥有-01` rather than `belong-91` / `have-91`.
- **Superlatives**: `have-degree-91 :ARG3 (最)`.
- **Adverbs**: 已经, 都, 也, 仍, 其中 as `:mod`, and 曾经 as `:temporal`.
- **Shared modifiers** on coordinated nouns written by re-entrancy on each conjunct (各式各样 and 奇怪 on both 新闻 and 专栏).
- **Habitual aspect** for a publication's recurring activities (发行, 报导, 综合).
- **The newspaper coreference chain** (s1n → s2x2 → s3x2 → s4n → s5x2) and the `:medium` and `:duration` roles. Event senses scored 100.
</critique>

# Earlier edits
- batch 1, reflection 1 (10/10 edits applied): Fix temporal chaining (anchor one main event, chain others with :overlap, no parent for copular -91 predicates, relative time words depend on DCT); Chinese classifiers as :unit; adverbs as :mod nodes; Chinese name brackets, no wiki, :place/:medium; aspect cues (habitual institutional activity, 已经+stop = state, 被称为 = performance); :reason for 因为/由于/以…而; 不过/可是 → but-91; distribute modifiers over con -> AnCast++ comp 84.8 on the batch, kept

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.