<!-- system -->
You improve the instruction of a UMR annotator by editing it.
<!-- user -->
You are improving the instruction an annotator (a model) follows to annotate whole documents in Uniform Meaning Representation (UMR). It is scored against expert gold annotations; the score that counts is AnCast++ (sentence graphs and document-level relations). Below are the current instruction, a critique of its annotation of a training batch, and what earlier edits did.

Edit the instruction to fix the problems of the critique that will recur on other documents. Prefer few, high-value changes; keep what works; keep the instruction clear and consistent (fix a rule rather than adding a contradicting one). The output format and the tools' descriptions are fixed and not part of the instruction: do not restate or change them. The instruction may be at most 30000 characters (now 15877). Never copy text of the test documents. Write general rules only. Do not record details: no specific words, names, sentences or annotations of these sentences, and no examples taken from them (short schematic patterns such as X 的 Y or (x / ...-01 :ARG0 ...) are fine). An edit that copies 8 or more characters of the training document is rejected.

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

# The critique (training batch 1: chinese_umr-0001, sentences 1-5; AnCast++ comprehensive 57.0)
<critique>
The costliest losses were temporal links (F 47), aspect (F 60), re-entrancy (F 18) and peripheral roles (F 33/48). Next came smaller structural slips in classifiers, name tokens, discourse frames and degree. Senses (100), document format (100), modal (91) and event detection (97) were strong. Some gold choices below are quirky, so where the gold data shows a pattern I describe the pattern rather than claim it is the guideline rule.

## 1. Temporal links: an anchor for every node, all hung on the document time (h_temporal, about 11 units, P 41)
**What went wrong:**
- **Too many anchors.** Every event and every time expression got a temporal parent. That included:
  - the copular identity predicate at the root of a defining sentence;
  - a "famous for" state;
  - a property word in a modifier;
  - a vague time word like "currently".

  Gold gives none of these a temporal parent.
- **Wrong parents inside a sentence.** Gold chains the events to each other. The publishing event is the parent, the "stopped" state overlaps it, and the "famous" state is `:contained` in it. The annotator instead hung several events on the document-creation-time, or on the time word.
- **Wrong relation.** For the main event of a present-situation sentence, gold uses `(document-creation-time :depends-on event)`; the annotator used `:overlap`.

**Why:** Section 5.1 says that every event and time expression gets a parent and that vague time words depend on past/present-reference. Nothing tells the annotator to limit links, so it over-generates.

**Change to the instruction:**
- Give temporal parents only to real eventive predicates, not to copular or identity predicates, plain states used as attributes, or property modifiers.
- Do not give vague deictic time words ("now", "currently") a parent of their own.
- Within a sentence, pick one anchor event and link the other events to it (`:overlap` / `:contained`), not each one to the document time.
- Link the anchor event to the document time.
- Precision matters as much as recall: leave out a link when unsure.

## 2. Aspect of recurring and resultative events (c_aspect, 8 units, F 60)
**What went wrong:**
- **Recurring activities.** An organisation's or periodical's regular activity (publishing, compiling content, continuing to publish) was marked endeavor, performance or activity. Gold marks it habitual, even when it is in the past or under an aspectual verb such as "continue" or "stop".
- **Resulting condition.** "Has already stopped", used to describe the current condition, was marked performance; gold marks it state.
- **Negated process noun.** A process named by a noun after a negated "undergo" verb was marked performance; gold marks it process.
- **Passive naming.** A passive verb of naming ("is called X") was marked state; gold marks it performance.

**Why:** Table 4.1 points to "completed past → performance" and "ongoing → activity" without asking first whether the event is a recurring routine.

**Change to the instruction:** Add a decision order:
1. Is the event a routine or recurring practice of its subject (publishing, reporting, compiling)? Then it is habitual, whatever the tense or aspectual verb.
2. Does an aspectual or completive predicate ("already stopped", "has ended") describe a present condition? Then it is state.
3. Is the event a process noun, including the object of a light or experiential verb? Then it is process.
4. Is it a verb of naming or labelling? Then it is performance.

## 3. Modifiers and arguments attached to the wrong node (d_peripheral, g_reentrancy, about 12 units)
**What went wrong:**
- **Adverbs dropped.** Content adverbs ("already", the scope adverb "all/both") had no node or sat on the noun. Gold puts them as `:mod` on the predicate.
- **Shared modifiers on a coordination.** Adjectives that modify both conjuncts were put once on the `and` node. Gold puts them on each conjunct and re-uses the same variable (re-entrancy).
- **Arguments filled from context.** The annotator added a participant to a noun compound that has an event modifier ("X-verification procedure") by taking it from the context. The compound's own noun is the argument.
- **"Famous for X" clauses.** The annotator made such a clause a separate `and` conjunct with a `:manner` role. Gold attaches "famous" to the noun it describes as `:ARG1-of` and makes the X clause a `:reason`. The X clause's agent is that noun, not the subject's name node.

**Change to the instruction:**
- Every adverb that carries meaning gets a node. Attach it with `:mod` to the predicate it scopes over, not to a noun.
- A modifier distributed over coordinated nouns goes on each conjunct, as a re-entrancy.
- Fill only the arguments the syntax provides; do not borrow them from elsewhere in the sentence.
- For "known/famous for X" (以…而闻名): the famous thing is `:ARG1`, and X is `:reason`.
- When a "known for" clause follows "A is a B", attach it inside the B noun.

## 4. Non-core role labels (e_peripheral, d_peripheral_entity, about 7 units)
**What went wrong:**
- A country modifying a noun ("American tabloid", "American history") got `:mod`; gold uses `:place`.
- A medium noun on a programme ("TV programme") got `:mod`; gold uses `:medium`.
- A part of a whole ("print edition of the paper") got `:possessor`; gold uses `:part-of`.
- A causal phrase (由于) got `:cause`; gold uses `:reason`.

**Change to the instruction:**
- A country or place word modifying a noun → `:place`.
- A channel or medium noun → `:medium`.
- An edition, section or component of a whole → `:part-of`.
- Use `:reason` for 由于/因为 phrases that give a reason for a state or a judgement. Section 2.5 currently says `:cause`; fix it.

## 5. Classifiers and measure words (c_other_attributes, a_entity, 5 units)
**What went wrong:** The annotator dropped ordinary classifiers, following the instruction. Gold keeps them: `:quant 1 :unit (份/个)`. Gold data does this consistently (个, 面, 只, 位).

**Change to the instruction:** Replace the rule "an ordinary classifier is dropped" with this: numeral + classifier → `:quant N :unit (classifier)`. Keep a demonstrative + classifier as `:unit` as well.

## 6. Named-entity tokens (f_name_tokens, 2 units, plus a mismatch on the classifier node)
**What went wrong:** In the gold, the book-title marks 《 》 are their own `:op`s of the name. The annotator left them out.

**Change to the instruction:** Include the title brackets as the first and last `:opN` of a work or publication name.

## 7. Superlatives and degree (a_event, d_core, 3 units)
**What went wrong:** "The most creative X" was written as `:degree (most)` with the noun as `:ARG0`. Gold uses `(X :ARG1-of (have-degree-91 :ARG2 property :ARG3 最))`. A property word in an attributive clause ("absurd content") should be a plain `:mod`, not an event with aspect, temporal and modal links. That extra event cost 3 more units.

**Change to the instruction:**
- Comparatives and superlatives use `have-degree-91`. Keep `:degree` only for plain intensifiers such as "very".
- State the existing rule more forcefully: an attributive property word, including a chengyu, is a `:mod` concept, not an event.

## 8. Discourse-frame roles (e_core_labels, 2 units)
**What went wrong:** `but-91` and `contrast-91` take `:ARG1` and `:ARG2`. The annotator used `:op1` and `:op2`, and also put a clause-level time word on the frame instead of on the clause it modifies.

**Change to the instruction:** Say this explicitly in 2.5, and require time adverbials to attach to the event they modify, never to the discourse node.

## 9. Over-linking coreference and negation (j_coref, c_polarity, i_modal, about 5 units)
**What went wrong:**
- **Coreference.** The annotator linked two different cessation events as `:same-event`: stopping publication and ceasing print. Gold does not link them.
- **"Not undergone" (未经).** The annotator put `:polarity -` on the event. Gold keeps it as full-negative in the modal layer without `:polarity`. It also gives the embedded process noun partial-affirmative strength, not full-negative.

**Change to the instruction:**
- Use `:same-event` only when the mentions are clearly the same event instance with the same participants.
- A negator fused into a verb (未经) is recorded as modal full-negative on that verb. The negation does not automatically pass to the events nested under it.

## Keep these
- **Senses.** Looking up every predicate in PropBank gave a perfect sense score. One caveat: on the possessive 属 the annotator's argument order followed PropBank, but gold reverses it. Where they conflict, check gold usage.
- **Entity coreference.** Linking each mention of the same entity to its closest earlier mention was all correct (recall 100).
- **Modal links.** `(root :modal author)` followed by author full-affirmative for asserted events worked well (F 91).
- **Name handling.** The type + name structure, Chinese word-level `:op`s, `identity-91` for "A is a B", and a `but-91` root for 不过 were all right.
- **Document format.** The document-level format was perfect.
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