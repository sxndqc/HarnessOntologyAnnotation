I made changes only for the critique's most costly patterns, and freed room by trimming redundant or niche text, since the instruction was close to the 30000-character limit.

**What I add or change:**
1. **Quoted article titles (about 35 units).** A title in 「」 or “” used with a classifier, or next to an article or news noun, is now a `publication` name. Every word and mark of the title is an `:opN`, and nothing inside it is analysed. I also added named events with a year in the name: `event :name`, with no links.
2. **Compound words (about 15 units).**
   - A verb + 人/者 word is split, with `:ARG0-of` for the agent and `:ARG1-of` for a patient or product.
   - The inner verb gets an aspect, an `:overlap` link to the clause verb, and the author as its modal parent.
   - A demonstrative or totality prefix + noun is split into the noun with a `:mod` of the prefix.
3. **Attributive modifiers (about 15 units).** A modifier that has a PropBank roleset is now an event attached by an inverse role, with links. Only words with no roleset stay a plain `:mod`. An event nominal that modifies a noun is `:mod` with `process` aspect. I adjusted the "Not events" line in 2.1 so it agrees with this.
4. **Smaller discourse fixes.**
   - A sentence-opening 如/例如 is `have-example-91`.
   - The temporal anchor of but-91 is its `:ARG1` event.
   - Discourse frames get no modal link.
   - A 为了 clause that shares the main subject re-enters it as `:ARG0`, and the no-borrowing rule is narrowed to match.
   - The articles or contents of a publication are `:part-of` it.
5. **"Has the ability to V" and 靠 X.** Added `有-06` with an `identity-91` on 能力 for the ability case, and `:reason` with no node for 靠.

**What I leave out:** the critique's publication-as-conceiver modal pattern. It contradicts the reported-speech rules validated on batch 3, and its own guidance on dates is ambiguous.

**What I trim to make room:**
- The event-type examples in 2.1.
- The role-noun examples, which the 2.2 rule and the table already cover.
- The mixed-separator rule.
- Wording in the relative-clause-with-aspectual-verb bullet, the fused-negation rule and the fame rule.
- The checklist, which I merge.

```json
{"summary": "Add: 「」 article titles as unanalysed publication names; named year-events; split verb+人/者 (agent/patient) and prefix+noun compounds; attributive modifiers with a roleset become inverse-role events; have-example-91, but-91 anchor, 为了 shared subject, publication parts :part-of, 有-06 ability, 靠 as :reason. Trim redundant text to fit.", "edits": [
{"op": "replace", "old": "- verbs used as predicates (`deny-01`, Chinese `拥有-01`);\n- event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events;\n- participles and relative-clause verbs (*the man who left*: `(p / person :ARG0-of (l / leave-11))`);", "new": "- predicate verbs, event nominals with process meaning (会议, 比赛), participles and relative-clause verbs;"},
{"op": "replace", "old": "property words used as plain modifiers (*a tall man*: `:mod (t / tall)`),", "new": "modifier words with no roleset (see 3.1),"},
{"op": "replace", "old": "Role nouns are reified the same way: *the president of Russia* →\n`(p / person :ARG1-of (h / have-org-role-91 :ARG2 (c / country ...) :ARG3 (p2 / president)))`;\n*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.", "new": ""},
{"op": "replace", "old": "separately, a role noun built from a verb + 人/者 is `(r / 人 :ARG0-of (v / verb-0N ...))` (`performance` for a completed act, e.g. founding).", "new": "separately, split a verb + 人/者 word: `(r / 人 :ARG0-of (v / verb-0N ...))` for the agent, `:ARG1-of` for a patient or product (aspect `performance` completed act, `state` disposition, `process` kind; it `:overlap`s the clause verb, author modal parent). Split a demonstrative or totality prefix + noun word (这/该/全/整+N) into `(n / N :mod (d / prefix))`."},
{"op": "insert_after", "anchor": "then the words, then a last `:opN \"》\"`.", "text": " A 「」/“” article or headline title used with a classifier or next to an article/news noun is a name too: `(p / publication :quant N :unit <classifier> :name (n / name :op1 \"「\" … :opN \"」\"))`, every word and mark an `:opN`; nothing inside it is analysed. A named event with a year in its name is `(e / event :name (n / name :op1 \"<year>\" :op2 \"年\" …))`, no links."},
{"op": "insert_after", "anchor": "Discourse 就/便 outside a condition gets no node.", "text": "\n- A sentence-opening 如/例如 offering the sentence as an example of the previous claim: `(h / have-example-91 :ARG1 (i / implicit-predicate) :ARG2 <main event>)`. A but-91's temporal anchor is its `:ARG1` event (the `:ARG2` event `:overlap`s it); discourse frames get no modal link. A 为了 clause whose subject is the main subject re-enters it as `:ARG0`. 有 能力 V → `有-06 :ARG1 (能力 :ARG1-of (identity-91 :ARG2 <V event>))`; 靠 X to achieve Y → `Y :reason <X event>`, no 靠 node."},
{"op": "replace", "old": "This also holds for purpose clauses, infinitive-like and", "new": "This also holds for infinitive-like and"},
{"op": "replace", "old": "- Coordination with mixed separators: if the first two items are joined without 、 and the rest with 、, the first pair is its\n  own nested `and` inside the outer `and`.\n", "new": ""},
{"op": "replace", "old": "N is `:ARG1-of` (or `:ARG0-of`) the inner verb, and\n  the aspectual verb is attached to the inner verb by `:ARG1-of`; N is not also an argument of the aspectual verb.", "new": "N is `:ARGn-of` the inner verb, which is `:ARG1-of` the aspectual verb; N is not its argument."},
{"op": "replace", "old": "an edition, section or component of a whole → `:part-of` (not\n  `:possessor`).", "new": "an edition, section or component of a whole, or an article of a publication → `:part-of` (not `:possessor`)."},
{"op": "replace", "old": "- A property word or chengyu used attributively (\"absurd content\", X 的 Y with X a property) is a `:mod` concept,", "new": "- An attributive modifier (X 的 Y) that has a PropBank roleset (check it) is an event: a property predicate `(y / Y :ARG0-of (x / X-01 :aspect state))` (the role its roleset gives the described entity), a producing verb `:ARG1-of … :aspect performance`; it `:overlap`s the clause event, author modal parent. An event nominal modifying a noun is `:mod` with `process` aspect. A word with no roleset (relational or distinguishing word, chengyu) is a `:mod` concept,"},
{"op": "replace", "old": "`:polarity`. The verb is `full-negative` in the modal layer. Events nested under it do not inherit the\n  negation: an event nested under the fused-negation verb gets `partial-affirmative`, with `author` as its modal parent (not the negated verb).", "new": "`:polarity`; the verb is `full-negative` (modal) and an event nested under it gets `(author :partial-affirmative e)`."},
{"op": "replace", "old": "- **\"Famous for X\" in a defining sentence.** The fame state gets no temporal parent of its own; it is the parent of the habitual\n  relative-clause event: `(fame :contained habitual-event)`, and that event also keeps its own `document-creation-time` link. The reason\n  event (X) hangs on the habitual event with `:overlap`, not on the fame state.", "new": "- **Fame in a defining sentence.** The fame state has no temporal parent; it is the parent of the habitual RC event `(fame :contained e)`, which keeps its own DCT link; the reason event `:overlap`s e."},
{"op": "replace", "old": "- Parentheses balanced; every variable defined once; all variables start with `s<N>`.\n- Every event has `:aspect`; negated events have `:polarity -`.\n- Every event and time expression has a temporal parent; every event has a modal parent.", "new": "- Balanced parentheses; unique `s<N>` variables; every event has `:aspect`, a temporal and a modal parent.\n- Compounds split (prefix + noun, verb + 人/者); 「」 titles are unanalysed names."}
]}
```