<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format (and the tools' descriptions, if the annotator has tools) are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 15598). Never copy text of the test documents. Record examples: for each problem you fix, add a short concrete example from these sentences (the words and the correct annotation fragment, a line or two) to a section "## Examples" at the end of the instruction (create it if it is not there), next to the rule it illustrates; keep the examples short and drop or merge old ones when the instruction gets near its size limit.

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
Chinese names are split into words, not characters: 欧洲议会 → `:op1 "欧洲" :op2 "议会"`. Types: `person`,
`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,
`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,
`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,
`disease`, `product`, `spaceship`, ... (as in AMR).

Dates: `(d / date-entity :year 1998 :month 4 :day 3)`, also `:weekday`, `:season`, `:dayperiod`, `:era`,
`:decade`, `:century`. Durations and amounts: `(t / temporal-quantity :quant 3 :unit (y / year))`,
`(m / monetary-quantity :quant 500 :unit (d / dollar))`. Ordinals: `(o / ordinal-entity :value 2)`.
Numbers are written as digits. In Chinese, a real measure word is a unit (三杯水 → `水 :quant 3 :unit 杯`);
an ordinary classifier (个, 本, 只, 位) is dropped (三本书 → `书 :quant 3`).

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

### 2.5 Discourse relations (combining clauses)

- coordination: `(a / and :op1 ... :op2 ...)`, `or`;
- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而) `but-91`;
- concession `:concession`, condition `:condition`, cause `:cause` (或 `have-cause-91`), purpose `:purpose`,
  manner `:manner`, temporal sequence `:temporal (b / before :op1 ...)` / `after` / `consecutive`;
- *if* (如果, 只要) → `:condition` on the main event; *because* (因为, 由于) → `:cause`; *in order to* (为了)
  → `:purpose`; *although* (虽然, 尽管) → `:concession`.

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
- Annotate event–event relations only when they are clear.

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


</instruction>

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 55.7)
<critique>
# Review of the annotator's UMR of the *Weekly World News* document, with changes to the instruction

The biggest losses were in temporal relations (F 30), reentrancy (F 15), aspect (F 60), event core and peripheral roles, and named-entity tokens and wiki. Most of these come from a handful of rules that the instruction leaves out or gets wrong for Chinese. The problems are listed below, most costly first.

---

## 1. Temporal structure: the annotator anchors everything to DCT or to a time word, not to other events (h_temporal F 30, about 12 units)

**What went wrong:**
- **Sentence 1:** every event hung from `document-creation-time` (DCT), and 停止 was used as the parent of 发行.
  - Gold anchors only the main habitual event to DCT and hangs the rest from it: `(document-creation-time :before s1x3) (s1x3 :overlap s1x4) (s1x7 :contained s1x3) (s1x3 :overlap s1x8)`.
  - Gold gives no temporal parent to `identity-91`. The annotator's `(document-creation-time :overlap s1i)` was counted as extra.
- **Sentence 4:** the annotator wrote `(present-reference :depends-on s4m) (s4m :contained s4t) (s4m :contained s4j)`. Gold does not anchor the events to 目前. It chains them: `(document-creation-time :depends-on s4x) (s4x :overlap s4x2) (s4x2 :overlap s4x6)`.
- **Sentence 5:** gold has `(document-creation-time :depends-on s5x)`; the annotator wrote `:overlap`.
- **Missing parents:** two events got no temporal parent at all:
  - 查证 in sentence 2: gold `(s2x8 :overlap s2x13)`.
  - 属 in sentence 3: gold `(s3x :overlap s3x6)`.

**Why:** Rule 5.1 says "Annotate event–event relations only when they are clear" and makes DCT the default. That pushes the annotator to anchor every clause to DCT. Nothing tells it that:
- the other events of a sentence normally chain off the first one, usually with `:overlap`;
- events inside nouns and relative clauses also need a parent;
- non-verbal `identity-91` and abstract predicates may get no temporal parent;
- the release data uses `document-creation-time :depends-on <event>` for the main event of some sentences.

**Change:**
- Replace the "only when they are clear" line with: "Anchor one main event of each sentence to DCT (or to a time expression). Attach every other event of the sentence to that event or to a nearby event, usually with `:overlap` (`:contained` if it lies inside it). Every event inside a relative clause or modifier also gets a parent, normally its governing event with `:overlap`."
- Add: "Do not give `identity-91` or `have-*-91` copular predicates a temporal parent."
- Add: "A time word like 目前 or 现在 is a modifier. Do not make it the parent of the events."
- Add the sentence 4 chain from gold as an example.

## 2. Measure words, aspect markers and adverbs dropped as nodes (a_entity_found, d_peripheral, c_other_attributes: about 12 units)

**What went wrong:**
- **Classifier plus measure word:**
  - 一份…小报: gold has `:quant 1 :unit (s1x5 / 份)`. The annotator dropped both.
  - 一个…节目: gold has `:quant 1 :unit (s3x7 / 个)`. The annotator dropped the unit.

  The instruction says 个 "is dropped", which is wrong for this data. Another gold document confirms it: 一款 → `:quant 1 :unit (款)`.
- **Adverbs gold keeps as `:mod` nodes, which the annotator left out:**
  - 已经 in sentence 1 (`:mod (s1x6 / 已经)` on 停止) and in sentence 4;
  - 都 in sentence 2;
  - 其中 in sentence 2;
  - 曾经 in sentence 3 (gold has `:temporal (s3x9 / 曾经)`).

**Why:** Section 2.2 explicitly says to drop 个/本/只/位. The instruction also never says that Chinese adverbs (已经, 都, 也, 仍, 曾经) become nodes. The annotator did keep 也 and 仍, but treated 已经 and 曾经 as pure aspect markers.

**Change:**
- Rewrite the classifier rule: "一 + classifier + noun → `:quant 1 :unit (<classifier>)`, for 个, 份, 款 and the like as well."
- Add: "Adverbs such as 已经, 都, 也, 仍, 曾经 and 其中 are concepts: `:mod (<word>)`, or `:temporal` for 曾经. They are not only aspect cues."

## 3. Named entities: brackets, wiki, and how the country modifier attaches (f_name_tokens 50, f_wiki 0, e_peripheral_labels: about 9 units)

**What went wrong:**
- **Title brackets:** the annotator wrote `:op1 "世界" :op2 "新闻" :op3 "周报"` in sentences 1 and 4. Gold includes the brackets: `:op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》"`. Another gold document does the same for every 《…》 title.
- **Wiki:** the annotator added `:wiki` three times (the paper twice and 美国 once in each of sentences 1 and 5 — four wiki values in all). Gold Chinese data has no `:wiki`, so each one counts as an extra.
- **Country as modifier:**
  - 美国超市小报 and 美国历史: gold uses `:place (s1c / country …)`. The annotator used `:mod`.
  - 电视节目: gold uses `:medium (电视)`. The annotator used `:mod`.
- **Unwanted coref:** 美国 in sentence 1 and 美国 in sentence 5 were linked; gold does not link them.

**Change:**
- "In Chinese names, keep the title brackets 《 》 as their own `:opN`."
- "Do not add `:wiki` in Chinese documents."
- "A country or place name that modifies a noun is `:place`, not `:mod`. A medium (电视, 网络) is `:medium`."
- "Do not corefer a repeated country name used only as a modifier."

## 4. Aspect (c_aspect F 60, 6 units)

**What went wrong:**
| word | annotator | gold | note |
|---|---|---|---|
| 发行 (sentence 1) | process | habitual | |
| 停止 (sentence 1) | performance | state | 已经停止 = it is in the stopped state |
| 综合 (sentence 2) | performance | habitual | a characterizing description of the paper |
| 经 (sentence 2) | habitual | process | |
| 发行 (sentence 4) | activity | habitual | |
| 称为 (sentence 5) | state | performance | |

**Why:** The table in 4.1 ties 了 to `performance`. It does not say that verbs describing what a publication or organization regularly does (发行, 报导, 综合) are `habitual`, even with 了. It also does not say that 已经 + a stop or end verb in a relative clause that describes something is a resulting `state`.

**Change:** add to 4.1:
- "Recurring institutional activities (publishing, reporting, compiling) are `habitual`, even with 了."
- "已经 + 停止 or another end verb used to describe an entity → `state`."
- "Passive naming or labelling (被称为) → `performance`."

## 5. Clause structure and reentrancy (g_reentrancy F 15, core and peripheral roles)

**What went wrong:**
- **Sentence 1, wrong root and wrong arguments:**
  - The annotator wrapped the sentence in `and` and made 闻名 a separate clause whose ARG1 and ARG0 point to the name node.
  - Gold puts 闻名 inside the predicate noun: `小报 :ARG1-of (闻名-01 :reason (报导-01 :ARG0 s1x …))`.
  - The annotator also added `发行-01 :ARG1 s1x` and inverted the stop relation. Gold has `发行-01 :ARG1-of (停止-01)`.
- **Sentence 2, modifiers on a coordination:**
  - The annotator put shared modifiers on the `and` node and added a made-up role `:subset`.
  - Gold distributes them to each conjunct as reentrancies: `新闻 :mod s2x6 :mod s2x7`, `专栏 :mod s2x6 :mod s2x7`.
- **Sentence 4, invented arguments:** `发行-01 :ARG0 s4n` and `网络版 :possessor s4n` are not in the text. They were counted as extra reentrancies.
- **以…而闻名:** gold uses `:reason`, not `:cause`. The same holds for 由于 in sentence 5: gold `:reason`, annotator `:cause`.

**Change:**
- "In 'X 是 … Y, 以 … 而 V' the second predicate modifies Y (`Y :ARG1-of V`). Do not add a coordinating `and`."
- "Distribute a shared modifier to each conjunct by reentrancy. Never put `:mod` on `and`."
- "Do not add arguments that are not expressed or clearly implied."
- "因为, 由于 and 以…而 → `:reason`." This fixes the instruction's current mapping of 因为/由于 to `:cause`.

## 6. Lexical choices: concept splits, abstract-predicate frames, core roles (event and entity concepts, core args: about 7 units)

**What went wrong:**
- **奇闻轶事:** treated as one chengyu node. Gold splits it: `and :op1 奇闻 :op2 轶事`, because it is two nouns.
- **属 in sentence 3:** the annotator used `belong-91` with ARG2. Gold uses the PropBank verb `属-02` with `:ARG0` = 节目 and `:ARG1` = 周报. A lexical verb present in Chinese PropBank wins over the abstract predicate.
- **停刊:** gold has `:ARG0 纸本`; the annotator used ARG1. Also, 纸本 is `:part-of` the newspaper, not its `:possessor`.
- **不过:** gold uses `but-91`; the annotator used `contrast-91`. The instruction already lists *but* → `but-91` for 但是 but not for 不过. Add 不过 and 可是 to that list.
- **最富创意:** gold has `have-degree-91 :ARG2 (富-01 :ARG1 创意) :ARG3 (最)`. The annotator wrote `:degree 最` on 富. The table should add `have-degree-91` for superlatives and comparatives.
- **历史上:** gold makes 上 a node with `:op1 历史`, attached as `:temporal`.
- **未经…程序:** gold has `程序 :ARG0-of (identity-91 :ARG1 查证-01)` and no `:polarity` on 经-01 (the negation is carried only by the modal relation). Gold also makes 查证 `partial-affirmative` from the author. These are idiosyncratic. A short note would suffice: "With 未经 a negated event, the full-negative modal relation is enough."

**Change:**
- Add to 2.6: "A chengyu is one concept only if it is a fixed four-character idiom. Coordinated noun pairs such as 奇闻轶事 are split."
- Add to 2.3: "Prefer the Chinese PropBank verb (属-02, 拥有-01) over `belong-91` / `have-91` when the verb is in the text; check its roles with the frame."

## Keep (worked well)

- **Modal annotation (F 94):** `(root :modal author)` plus `full-affirmative` for asserted events, and `full-negative` for 未经. Keep 5.2 as it is.
- **Coreference chain for the paper (recall 100):** 周报 linked across sentences, earlier mention first, entity nodes only. Keep 5.3.
- **Senses and document format:** all PropBank senses were correct (100) and the document format was correct (100). Keep the `<word>-01` and `-00` rules and the format conventions.
- **identity-91 for 是:** used correctly, with ARG1 and ARG2 right (core args of abstract predicates scored 100).
- **Chinese concept wording:** concepts kept as written in Chinese, and event nominals such as 查证 marked `process`.
</critique>

# Earlier edits
(none: the first edit)

# Your answer
A short summary of what you change and why, then one JSON block (```json ... ```) of the form
{"summary": "...", "edits": [...]}, where each edit is one of
  {"op": "replace", "old": "<text that occurs exactly once>", "new": "<its replacement>"}
  {"op": "insert_after", "anchor": "<text that occurs exactly once>", "text": "<text to insert after it>"}
  {"op": "append", "text": "<text to add at the end>"}
  {"op": "delete", "old": "<text that occurs exactly once>"}
  {"op": "rewrite", "text": "<the whole new instruction>"}  (only to consolidate; then no other edit)
Edits apply in order; one whose anchor is not found exactly once is skipped.