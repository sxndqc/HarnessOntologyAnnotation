Here is my review, with the costliest patterns first. All advice is given as general rules.

## 1. Possession or belonging verb with the wrong sense and roles (about 6 units)
**Checks:** b_event_sense 1, d_core_args_event 1, e_core_labels 1, g_reentrancy 2 (one missing, one extra), plus the knock-on effect on reentrancy F1, which was the lowest check at 73.

**What happened:** a relative clause "Y that belongs to X" used a belonging verb. The annotator took the -01 sense and English-style roles (theme as `:ARG1`, owner as `:ARG2`). The Chinese PropBank frame that fits is the membership sense, -02. In that frame the owner is `:ARG0` and the thing that belongs is `:ARG1`. So the modified noun should be `:ARG0-of`, and the owner should be re-entered as `:ARG1`.

**Why:** the instruction already says "the belonging/membership sense of a verb is often not -01", but the annotator did not open the frames. Nothing in the instruction forces it to.

**Change:**
- Make the lookup a required step. For every Chinese predicate, first list all of its senses with their role descriptions. Then pick the sense whose descriptions match the participants.
- Copy the role numbers from that sense, not from the -01 sense or from English.
- Add a sample case: a belonging verb in a relative clause. Its roles are owner = `:ARG0` and possessum = `:ARG1`, and the head noun takes whichever inverse role the frame gives it.

## 2. Verb-word concepts: fused negation and multi-character verbs (about 4 units)
**Checks:** a_event_concept 2 and the matching sense units.

**What happened:**
- A negation fused into the verb ("not-pass-through" type) was written as a new `-00` concept spelled with the negator. Gold uses the positive verb with its own PropBank sense (`经-01`). The negation appears only as full-negative at the document level.
- A segmented word "call-as" (`称为`) was cut down to its first character (`称`). The whole word has its own PropBank frame.

**Why:** the instruction tells the annotator not to write `:polarity -` on fused negation, but it does not say which concept to use. It also does not say that a segmented token is looked up as a whole word.

**Change:**
- For a word that is negator + verb, the concept is the verb part with its own PropBank sense and roles. Add no polarity, and put `full-negative` in the modal triples.
- Look up a predicate as the whole segmented token first. Use a shorter or `-00` form only if the whole token is not in PropBank.

## 3. Type for a titled periodical (2 entity_concept units + 2 granularity units)
**What happened:** a title in 《 》 whose head word is a newspaper or weekly (报 / 周报 / 日报) was typed `publication`. Gold uses `newspaper`.

**Change:** choose the most specific entity type that the name's head or the context shows:
- `newspaper` for 报 / 周报 / tabloid;
- `magazine` for 杂志 / 期刊;
- `book`, `program` and so on for other kinds of work;
- `publication` only when the kind is unknown.

## 4. Temporal structure when the root is identity-91 (3 h_temporal units)
**What happened:**
- The annotator wrote the reputation state as a child of the anchor, `(anchor :contained state)`. Gold writes it with the state as the parent: `(state :contained anchor)`.
- The annotator put the cause or means event under the reputation state. Gold puts it directly under the anchor with `:overlap`.

**Why:** the instruction's wording ("are `:contained` in the anchor", and "the event it depends on" as a parent) led straight to both errors.

**Change:** rewrite the rule with explicit triples:
- `(document-creation-time :before anchor)`;
- `(reputation-state :contained anchor)`;
- every other event of the predicate noun, including the means or reason of the reputation, is `(anchor :overlap e)`. None of them hang under the reputation state.

## 5. Aspect of a stative verb with 曾经 / 过 (1 c_aspect unit)
**What happened:** a possession verb with "once" and experiential 过 was marked `performance`. Gold keeps it `state`.

**Change:** stative verbs (possession, belonging, existence, knowing) stay `state` even when they carry 了, 过 or 曾经, or a duration modifier. Those markers only place the state in the past for the temporal triples.

## 6. Relations the text does not express (1 g_reentrancy unit)
**What happened:** the annotator added a `:part-of` link back to the publication on a second part noun (an online edition). The text only implies that relation.

**Change:** extend the "Unexpressed participants" rule to non-core roles as well. Re-enter a node only when a word or construction in the text expresses that relation.

## 7. Minor, gold-specific (about 2 units)
- A process noun whose type is given by an event nominal ("the X procedure", where X is an event) is linked in gold as `noun :ARG0-of (identity-91 :ARG1 event)`, not `:mod event`. Add this as an example only if it shows up repeatedly.
- That event, sitting inside a negated generic clause, got `partial-affirmative` in gold, not `full-affirmative`. This is too idiosyncratic to turn into a rule.

## What to keep
The annotator handled these well, and the instruction should keep the rules behind them:
- named entities with the 《 》 brackets as their own `:op`s;
- nested `and` for a parallel-noun compound inside a list, and shared modifiers re-entered on each conjunct;
- numeral + classifier as `:quant` / `:unit`, including when the number is 1;
- a country name as `:place` on a common noun;
- the identity-91 root for a copular sentence, with the describing clause attached under the predicate noun;
- `habitual` for what a periodical regularly publishes or contains;
- `state` for 已经 + an aspectual stop verb, and `performance` with `(document-creation-time :depends-on e)` for a completed status change or a naming passive;
- a superlative as `have-degree-91` with the property verb (and its object) under `:ARG2`, no temporal or modal triples for it, and the scope phrase as a `:temporal` postposition node;
- `:medium` for a TV or online modifier, and `:part-of` for an edition of a publication;
- `but-91`, `:reason` for 由于, and `process` aspect on a negated verb with a nominal event object;
- the coreference chain over the main entity, with each mention linked to the closest earlier one;
- one anchor per sentence, with the other events attached by `:overlap`.

The instruction already contains most of these rules, and it should keep them.