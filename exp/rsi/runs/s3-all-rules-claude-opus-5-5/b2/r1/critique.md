# How the instruction should change, judging by this document

**Overview.** Coreference, polarity, granularity and the document format were perfect, and modal links were good (F 93). Two areas lost the most points: temporal links (F 19) and the structure of the long reason-and-purpose sentence (core arguments of events F 53, of abstract predicates 0, reentrancy precision 25). Quantity nouns came next. Most of the temporal loss comes from rules that the instruction states but that the gold data does not follow.

## 1. Temporal links: the date rule and same-time narrative links are wrong (h_temporal, about 15 units)

**What went wrong:**
- **Absolute dates.** All three were attached as `(root :depends-on date)`. Gold puts `(document-creation-time :before date)` for a past date.
- **Event under a date.** All three were linked to their date with `:contained`. Gold uses `:overlap`.
- **Anchor of a new narrative sentence.** It was hung on the previous sentence's event. Gold links the anchor to `document-creation-time :before`.
- **Main event versus its reason and purpose clauses:**
  - Purpose clauses were made `:after` the main event. Gold has them `:overlap`, because the purpose holds at the time of the action.
  - The reason event (a change announced for the future, but past relative to the document) was made `:after`. Gold places it before the main event.
- **Event inside a relative clause** ("left-over", "inherited"): annotated as `:overlap`; gold places it before the event it modifies.
- **Next-sentence result state** ("X also became a feature"): annotated `:after`; gold uses `:overlap` with the previous anchor.
- **Event nominals inside a "process+量" noun** got no temporal parent (2 units missing).

**Why:** The instruction directly says "an absolute date depends on root" and gives the example `(s1t :contained s1e)`. Its rule "a purpose is `:after` its main event" goes against the gold. The search_annotations results confirm the gold pattern: `document-creation-time :before s4x` and `(s7r :contained s7x)` occur, but `:before` from DCT is the norm in past narrative.

**Changes to make:**
- A past absolute date gets `(document-creation-time :before date)`. Use `:after` for a future date. Keep `:depends-on` only for relative deictic dates.
- An event in the clause of a date or time expression gets `(date :overlap event)`. Use `:contained` only when the time expression is clearly a long span and the event is a point in it.
- In a past narrative, the anchor event of each sentence links to `document-creation-time :before`. Link it to an earlier sentence's event only when the sentence explicitly follows from that event, e.g. "also became", "as a result". Then use `:overlap` unless the order is stated.
- A purpose clause `:overlap`s its main event; drop "purpose is `:after`". A reason or cause event comes before its result.
- An event in a relative clause or participle that describes an earlier completed event (left over, inherited, built) comes before the event that uses it.
- A future marker inside a reason clause about past events means future *relative to that past*. It does not mean after the main event.

## 2. Clauses joined by both a reason marker and a purpose marker (about 20 units across several checks)

**What went wrong:** The sentence had a reason marker paired with a result marker, plus a purpose marker. Gold reifies this as `have-reason-91 (:ARG1 result, :ARG2 cause, :aspect state)` and nests `have-purpose-91 (:ARG1 main event, :ARG2 purpose, :aspect state)` inside it. Both get `author :full-affirmative`. The annotator used `:reason` and `:purpose` roles, so it missed 2 abstract nodes, their 4 arguments, their aspects and their modal links. Search_annotations shows this reified pattern in other gold documents too.

**Why:** Section 2.5 maps reason and purpose markers only to roles.

**Change:** When a reason marker is paired with a result marker (因为…于是/所以, 由于…而), or when a clause has a marked purpose, use the reified `have-reason-91` or `have-purpose-91` as above, with `:aspect state` and an author modal link. Keep `:reason` and `:purpose` roles for unpaired phrases inside one clause.

## 3. Arguments borrowed from elsewhere in the sentence (g_reentrancy P 25; core arguments)

**What went wrong:** Three arguments were borrowed:
- the founder was made the agent of the purpose verb;
- the founder was made the possessor of the other periodical;
- the new periodical was made the agent of the "contain" clause.

Gold leaves the first two out. The third clause is attached as `:ARG0-of` on the noun it describes, a relative-clause reading.

**Why:** The instruction already forbids this, but only for "finite clauses in coordination". The annotator read it as not covering purpose clauses or possessors.

**Change:** Widen the rule. Never fill an argument of a purpose clause, an infinitive-like clause or a trailing clause with an entity from the main clause. Never add `:possessor` from a word like 旗下 ("under one's banner"); keep that word as a `:mod` concept. A trailing clause that describes the object just introduced (a new entity plus what it holds or does) is a relative clause: attach it with `:ARGn-of` on that object.

## 4. "Component of a named work" phrases and change-of-state verbs (about 10 units)

**What went wrong:** In "[colour] edition 的 《Name》", gold makes the component noun the head, `(版面 :mod 黑白 :part-of newspaper)`. The annotator made the named entity the head with `:mod` component, which also produced a mismatch in name alignment. In "由 X 改为 Y" (change from X to Y), gold puts X as `:ARG1`, the thing changed (component `:part-of` work), and Y as `:ARG2`. The annotator used `:source` for X and gave the periodical as `:ARG1`.

**Change:**
- When a component, edition or section noun modifies a named work through 的, the component noun is the head and the work is its `:part-of`.
- For change verbs with 由 X 改为/变为 Y, the original state X is `:ARG1` and the result Y is `:ARG2`. Never use `:source`.

## 5. Quantity nouns ("process + 量") and amounts (about 20 units across sentences 9 and 10)

**What went wrong:** Gold decomposes such a noun into `(量 :quant-of (verb-01 :ARG1 entity) :ARG1-of (have-quant-91 :ARG2 number :unit classifier))`, and the process gets a temporal `:overlap` with the main verb. The annotator kept a single compound noun with `:possessor`. It also turned the number into `thing :quant N :unit`, and in one case used `:ARG3`, which made a node mismatch.

**Caveat:** Another gold document keeps a "-量" compound whole, so state this as the convention when the first part is a clear verb.

**Change:** Split the quantity noun: `量` is the head, the verb is a separate event reached through `:quant-of`, and the owner of the quantity is that verb's `:ARG1` (not `:possessor`). A reached or fallen-to amount is `have-quant-91 :ARG1 <quantity noun> :ARG2 <number> :unit <classifier>`, attached to the quantity noun through `:ARG1-of`. Do not make it a separate `thing` argument of the verb.

## 6. Role nouns, apposition and person names (about 10 units)

**What went wrong:**
- **Founder title** ("founder" + name): gold is `individual-person` + `:ARG1-of have-org-role-91 :ARG3 (人 :ARG0-of 创始-00 :aspect performance)`. The annotator used `person`, `创始-01` and `:ARG0-of` directly, with `state` aspect.
- **Appositive in front of a name** ("its gossip tabloid 《N》"): gold is `named-entity :ARG1-of (identity-91 :ARG2 (head noun :mod …))`. The annotator dropped the head noun and one modifier.
- **Middle dot in a transliterated foreign name:** gold keeps "·" as its own `:opN`; the annotator dropped it.

**Changes:**
- Named humans are `individual-person` (the gold data uses this concept).
- A title or role noun in front of a name is `have-org-role-91 :ARG3 <role>`. A role noun built from a verb plus 人/者 is `人 :ARG0-of verb`, with `performance` aspect for a completed act.
- A descriptive noun phrase in apposition to a name is `identity-91`, with all its modifiers kept.
- Keep "·" as a name op.
- Always check that a Chinese verb's sense exists in PropBank. If it does not, use `-00`.

## 7. Aspect and modifier details (about 6 units)

**What went wrong:**
- The purpose verb was `performance`; gold has `activity`.
- The relative-clause past event was `state`; gold has `performance`.
- The capacity clause ("contain articles") was `habitual`; gold has `process`. The instruction's "periodical publishing → habitual" rule was over-applied here.
- A colour or style word modifying a process nominal was `:mod`; gold has `:manner`.
- "1980年代" (the 1980s) was given `:decade`; gold has `:era`.

**Changes:**
- A purpose or intended action is `activity`.
- A completed event in a participle or relative clause is `performance`.
- Limit the habitual rule to verbs of publishing or reporting, not to the capacity or content of a publication.
- A modifier that says *how* a process nominal is done is `:manner`.
- Follow the gold convention for decade expressions (`:era` in this data).

## What to keep
- Named-entity handling: periodical names as `newspaper`, title marks as ops, no `:wiki`.
- Same-entity coreference chains to the closest earlier mention, including the "该刊" (this periodical) type of mention: 100%.
- `:polarity -` with `full-negative`, and an author modal link on every event.
- `:mod` for adverbs such as 也 and 已经; date-entities inside the clause; classifier as `:unit`.
- The sense and aspect of the main events (founding, became, reached, fell).