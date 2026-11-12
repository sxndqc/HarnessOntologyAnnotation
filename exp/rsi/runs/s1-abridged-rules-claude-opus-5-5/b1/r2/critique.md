The costliest error is the temporal structure (about 11 units). Next come superlatives built on a property verb (about 9 units) and Chinese verbs whose argument numbers or sense were assumed rather than checked in PropBank (about 7 units). Most other checks were already strong.

## 1. Temporal anchors and constants (h_temporal F 43, about 11 units)

What went wrong, by kind:

**(a) Copular identity sentence with events inside the predicate noun.**
- The annotator anchored on the "known for" state, linking it to document creation time with `:overlap`. It also ordered the "stopped" event `:before` the event it stops, even though the order of a stop and the event it stops was not stated.
- Gold anchors on the past event inside the predicate noun (`DCT :before`). Every other event of the sentence hangs off that anchor: the reputation state is `:contained` in it, and the rest are `:overlap`.
- **Why:** rule 5.1 says "the anchor is the matrix event". When the matrix is `identity-91`, which has no temporal link, the rule does not say what replaces it.
- **Change:** "When the root is `identity-91`, choose as anchor the event in the predicate noun that is most clearly placed in time, usually a completed past event. The reputation or property states are then `:contained` in it, and everything else is `:overlap`. An aspectual verb (stop, begin) and the event it governs are `:overlap`, never `:before`/`:after`."

**(b) Past-time adverbs (曾经 type).**
- The annotator made the adverb a time expression (`past-reference :depends-on adv`, then `adv :contained event`).
- Gold gives the adverb no temporal triple and uses `document-creation-time :before event`.
- **Change:** "Past-time adverbs (once, formerly, 曾, 曾经) stay `:temporal` nodes in the graph but are not reference times. Give them no temporal triple, and link the event directly as `(document-creation-time :before e)`." Do the same as the instruction already does for vague present adverbs.

**(c) Events whose result holds now** (a termination already done, as in 已经 + a termination verb; a naming/evaluation passive).
- Gold uses `(document-creation-time :depends-on e)`. The annotator used `:overlap` and `:before`.
- **Change:** add this case to 5.1: a completed event whose result describes the present situation (a status reached, a name or evaluation given) is linked as `(document-creation-time :depends-on e)`.

**(d) `have-degree-91`.** The annotator gave it a temporal parent, a modal parent and `:aspect state`. Gold gives it none of these, consistently across documents. It is the same kind of exception as `identity-91`; see item 4.

## 2. Superlative of a property verb, and "history 上" (about 9 units)

**What went wrong:**
- For "most + property verb + noun object" (最富创意 type), the annotator dropped the verb and put the noun as `:ARG2` of `have-degree-91`.
- It also made the scope phrase "in X's history" (X 历史上) an `:ARG5` comparison set and dropped the postposition.

**What gold does:**
- `:ARG2` is the property verb as an event (`富-01 :ARG1 创意`, `:aspect state`).
- The scope phrase is a `:temporal` node for 上 with the time noun as `:op1`, attached to the head noun.

**What it cost:** a missing event, its aspect, temporal and modal links, the missing 上 node, and three wrong `have-degree-91` arguments.

**Why:** 2.3 says to use `have-degree-91` but not what fills `:ARG2` when the property is a verb with an object. The locative-postposition rule lists 时/中/以来 only.

**Changes:**
- "In a superlative or comparative, `:ARG2` is the property word itself. If it is a verb with its own object (rich in X, full of X), keep the verb as an event concept with its object, and put that verb under `:ARG2`."
- "Use `:ARG5` only for an explicit comparison set (among N, of all N). A scope like 'in history' (X 上, X 以来) is a `:temporal` (or `:range`) postposition node with the noun as `:op1`."
- Extend the postposition list to 上 after time or period nouns (历史上).

## 3. Chinese verbs: argument numbering and sense guessed from English (about 7 units)

**What went wrong:**
- A "belonging" verb in a relative clause got sense -01 with `:ARG1` = the thing and `:ARG2` = the owner. In PropBank, -02 is the belonging sense, with `:ARG0` = the owner and `:ARG1` = the thing that belongs.
  - In gold, the program is `:ARG0-of` the verb, and the newspaper (the 自己 referent) is re-entered as its `:ARG1`.
- A "cease publication" verb has only `:ARG0` in PropBank (the publication). The annotator used `:ARG1`.

**Why:** the instruction warns against abstract predicates, which is why the verb was right, but it never says the Chinese PropBank roleset decides the numbering. The annotator then fell back on English habits (theme = `:ARG1`).

**Change:** "For every Chinese predicate, look up its frames. Choose the sense whose role descriptions fit, and use exactly the numbered roles that roleset defines. Many Chinese intransitive and change-of-state verbs have only `:ARG0`. Do not default the theme to `:ARG1`."

## 4. Attributes on abstract predicates (3 units)

**What went wrong:**
- `identity-91` had no `:aspect`, but gold has `:aspect state`.
- `have-degree-91` was given `:aspect state`, but gold gives it no aspect, and also no temporal or modal parent.

**Change** (state both together):
- "`identity-91` gets `:aspect state` and a modal parent, but no temporal parent."
- "`have-degree-91` gets no `:aspect`, no temporal parent and no modal parent. The event under its `:ARG2`, if any, gets all of these."

## 5. Coreference of an incidental place name (j_coref precision 71, 2 units)

The annotator linked a country name that appears only as a `:place` modifier in two sentences, which the instruction already forbids. The rule was not followed.

**Change:** add it to the final checklist as well: "Before writing `:coref`, drop every pair where both mentions are only `:place`/`:mod` modifiers."

## 6. Smaller patterns (1–2 units each)

- **Shared subject in a purpose or means frame** (以 X 而 Y, "known for doing X"): gold re-enters the subject of Y as `:ARG0` of X. The instruction's "unexpressed participants" rule made the annotator leave it out.
  - **Change:** "A subject shared through a control or serial frame counts as expressed; re-enter it."
- **Negation fused into a verb word** (未经 type): gold puts no `:polarity -` on the graph, only `full-negative` at the document level.
  - **Change:** add this as an exception to "negated events have `:polarity -`".
- **Noun + event-nominal modifier meaning "a procedure that is X"**: gold uses `程序 :ARG0-of (identity-91 :ARG1 event)`, not `:mod event`.
- **Termination verb with 已经:** the rule "already + stop/cease → `state`" was over-applied. Gold restricts it to the aspectual verb that governs another event (stop doing X). A lexical termination verb (ceased publication) with 已经 is `performance`. Narrow the rule to say so.
- **A list whose first item is a fixed pair of parallel nouns:** gold nests the pair as its own `and` inside the outer `and`. Say this in 2.6.
- **Event nominal inside a negated clause:** gold gives it author-level `partial-affirmative`, not `(negated event :unspecified x)`. This is a minor point and probably not worth a rule.

## What to keep

The instruction already produced these correctly, so keep the rules behind them:
- Named entities, including title brackets as their own `:op`s.
- `:quant 1` with `:unit` for a classifier.
- `:place` for a country modifying a noun.
- Shared modifiers re-entered on each conjunct.
- `:medium` for a TV program and `:part-of` for a print edition.
- 由于 → `:reason`; 但/不过 → `but-91`.
- `habitual` for a periodical's publishing and contents.
- `performance` for a naming passive; `state` for 已经停止.
- `:mod` for 已经/仍/也/都 and `:temporal` for 曾经 in the graph.
- Main-entity coreference chains, and the format of the document-level annotation.

All of these scored at or near 100.