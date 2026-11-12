Below are the error patterns in order of cost, each with what to change in the instruction. Then what the annotator got right and the instruction should keep.

## 1. "Amount reached" sentences: the verb was dropped and have-quant-91 made the root (most costly, about 20 units)
**What happened.** In a clause where a measured noun reaches or falls to a number (达到 N, 跌至 N), the annotator removed the lexical verb. It made `have-quant-91` the sentence root with `:aspect state`. In one sentence a sentence-initial "but" connective became a `but-91` root, with the clause as its only argument.

**What gold does.** The verb stays the root, with its own frame: the theme is `:ARG0`, it has `:aspect performance`, and the time and adverb modifiers attach to it. The measure noun is `:ARG0`, and `have-quant-91` hangs as `:ARG1-of` on that noun.

**Cost:**
- a_event_found: 1 missing
- a_event_concept: 1 wrong
- c_aspect: 1 wrong and 4 extra
- d_core_args: 1
- d_peripheral: 2 missing (the modifiers sat on the wrong node)
- h_temporal: 6
- i_modal: 5

**Why.** The "Amounts reached" rule only says where `have-quant-91` goes. It never says the verb is kept. It also says nothing about the aspect, temporal or modal treatment of `have-quant-91` there.

**Fix — rewrite the rule:**
- "The verb of reaching or falling (达到, 跌至 → its bare-verb frame) stays as the event. It is the root when it is the main verb. The measured noun is its theme (`:ARG0`, from the frame), and it carries `(:ARG1-of (have-quant-91 :ARG2 N :unit …))`."
- "This `have-quant-91` gets no `:aspect`, no temporal parent and no modal parent."
- "Time expressions and adverbs (already, 已经) attach to the verb."
- "A sentence-initial connective that only links to the previous sentence (不过/但是 at the start of the sentence) does not become a one-argument `but-91` root. The main verb stays the root."

## 2. The rule for the verb inside a measure compound is wrong (4 units)
**What happened.** The annotator followed the instruction: the inner verb of a "V + 量" compound got `:aspect habitual` and `(author :full-affirmative …)`.

**What gold does.** It gives that inner verb neither. It keeps only the temporal `:overlap` with the governing verb.

**Fix.** Change the "Measure compounds" rule to: "the inner verb gets no `:aspect` and no modal triple; it keeps its arguments and its temporal `:overlap` with the governing verb."

## 3. Whether the publication or its format/part is the argument (about 10 units)
**What happened.** Two cases went wrong:
- **Changing a publication's format.** In "X changes from format A to format B" (由 A 改为 B), the annotator made the publication `:ARG1` and the old format `:source`. Gold makes the old-format noun `:ARG1` (the thing changed) with the publication as its `:part-of`, and the new format `:ARG2`.
- **Founding a paper with a given format.** In "founded the [format]-type [publication]" (创立了 A版面的《X》), the annotator made the publication `:ARG1` with `:mod` format. Gold makes the format/part noun the argument, with `:part-of` the named publication.

**Cost:** d_core_args 2, d_peripheral 4, e_labels 3.

**Fix.** Extend the "Heads" and "Parts and media" rules:
- "When a format, layout or section noun (版面, edition, section) is what is created or changed for a publication, that noun is the argument and the publication is its `:part-of`. This holds even when the publication's name is the grammatical head after 的."
- "In 从/由 A 变为/改为 B, A is the frame's 'thing changed' role (`:ARG1`), not `:source`; B is `:ARG2`."

## 4. A trailing clause saying what the object holds or does became `:purpose` (4 units)
**What happened.** A clause after the object that says what the founded thing holds (，容纳…) was made `:purpose` of the main verb. The annotator added a re-entrant `:ARG0` and gave it `habitual`.

**What gold does.** The clause is `:ARG0-of` on the object noun, with `:aspect process`. That matches the instruction's own "relative-clause verb giving what something is for or contains is `process`".

**Fix.** Widen "Describing clauses" beyond copular sentences: "A trailing clause without 为/为了 that tells what the object (just created, named or described) contains or does attaches under that object as `:ARGn-of`, with `:aspect process`. It is not `:purpose`, and there is no extra re-entrancy."

## 5. A role noun before a name, and nested abstract predicates (about 7 units)
**What happened.** For a title or agent noun right before a personal name (V+人 compound + name), the annotator used `identity-91 :ARG2`. Gold uses `have-org-role-91 :ARG1 person :ARG3 (人 :ARG0-of V)`. Across the cases, gold gives role and appositive reifications nested inside a noun phrase (`have-org-role`, the appositive `identity-91`) no `:aspect` and no modal triple.

**Cost:** concept 1, label 1, aspect 2 extra, modal 2 extra.

**Fix.**
- "A role or title noun directly before or after a person's name → `have-org-role-91 :ARG3 role`. Use `identity-91 :ARG2` only for non-role descriptors (e.g. of a publication)."
- "Abstract predicates that only modify a noun get no `:aspect` and no modal or temporal triple. The current rule giving `identity-91` `:aspect state` and a modal parent should apply only when `identity-91` is the clause predicate."

## 6. Temporal relations to dates and to earlier sentences (3 units)
**What happened.**
- **Date to event.** The annotator wrote `(date :contains event)`. Gold uses `:overlap`.
- **Anchor of a new sentence.** The annotator anchored a new sentence's main past event to a similar event of the previous sentence. Gold links it to `document-creation-time :before`.

**Fix.**
- "A date or era and the event in its clause: `(date :overlap event)`."
- "Link an anchor to an earlier sentence's event only when the text marks the sequence (then, thereupon, 也成了 continuing the story). An independent past event gets `(document-creation-time :before e)`."

## 7. Smaller points
- **Black-and-white printing:** a format/colour word on an event nominal should be `:manner`, and a periodical's printing should be `habitual`. The instruction already says both; the annotator didn't follow them. Add a worked example of this kind.
- **Decades:** a decade expression should be `:era` with the year number only (`:era 1980`), not the written string.

## What to keep
- Named entities: the 《 》 brackets as their own `:op`s, the middle dot as its own `:op`, the `newspaper` type, `individual-person` (all 100%).
- Reifying a clause-linking reason or purpose as `have-reason-91` / `have-purpose-91` with the right arguments.
- Splitting measure compounds into 量 `:quant-of` V.
- A negated relative-clause verb getting `:polarity -` and `full-negative`.
- `已经` / `也` as `:mod`.
- The coreference chains (100%), including the definite "this paper" (该刊) linked to the name.
- The past-date triples with `document-creation-time`.