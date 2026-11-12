**Summary of changes.** I fixed the recurring problems from the critique and freed space by removing redundant examples and introductory text. The instruction stays under the 30000-character limit.

1. **Named beings and celestial bodies.** I replaced the rule "the category noun before a name is the concept", which contradicted the next rule. Now any named being is `individual-person`. A name made of common words is still a name. 地球/月球/太阳 are `planet`/`star` + `:name`.
2. **Repeats within a sentence.** Section 5.3 now agrees with section 1. Only pronouns and unexpressed mentions are re-entered. A repeat with its own noun gets a new node plus `:same-entity`.
3. **Temporal structure.**
   - An abstract predicate that is the content of a saying or thinking verb gets no temporal parent.
   - Its inner events attach to the reporting verb with `:overlap`.
4. **Topic-list rules.**
   - List-item activity nouns are plain entities, and so is an idiom filling an abstract predicate's value slot.
   - A topic noun with no outer role is headed by its relative-clause verb.
5. **Aspect.**
   - The institution/periodical habitual rule overrides `process` for event nominals.
   - A generic ongoing nominal is `activity`.
   - Existence and survival verbs stay `state`, also under *continue*.
6. **Modal.** `(author … null-conceiver)` is written only when `null-conceiver` is actually used in that sentence.
7. **Smaller items.**
   - Place-noun postpositions (在 N 中) are a node filling the verb's location role.
   - A possessive pronoun on an event noun adds no `:possessor`.
   - The role-lookup section now names the traps for 有's senses and for count-as verbs numbered from `:ARG0`.
8. **Space freed.** I removed or shortened redundant intro text, examples, the checklist and duplicate type lines.

```json
{"summary": "Fix named-being/celestial rule contradiction, same-sentence repeat coref contradiction, temporal exemption for abstract-predicate content of saying verbs, entity status of list items/idioms in value slots, topic-noun conjunct headed by its relative verb, habitual-over-process for periodical nominals, existence verbs state, null-conceiver only when used, place postpositions, possessive pronoun no :possessor, 有/count-as lookup traps; trimmed redundant text for space.", "edits": [
{"op": "delete", "old": "It is compared node by node with an expert gold annotation; check each graph and its document-level relations."},
{"op": "delete", "old": "UMR 0.9, abridged, for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data."},
{"op": "delete", "old": "A UMR has two levels."},
{"op": "delete", "old": "- **Sentence level**: one rooted PENMAN graph per sentence (concepts, roles, attributes)."},
{"op": "delete", "old": "- **Document level**: temporal, modal and coreference relations between nodes, across sentences."},
{"op": "delete", "old": "- Balanced parentheses; each variable defined once, starting with `s<N>`."},
{"op": "delete", "old": "## 7. Checklist"},
{"op": "delete", "old": "| cause, reason | `have-cause-91` / `:cause` | |"},
{"op": "replace", "old": "`:modal-strength <value>` too (the scorers move it to the document level).", "new": "`:modal-strength <value>` too."},
{"op": "delete", "old": "Use the coarse values:"},
{"op": "replace", "old": "- participles and relative-clause verbs (*the man who left*: `(p / person :ARG0-of (l / leave-11))`);", "new": "- participles and relative-clause verbs;"},
{"op": "delete", "old": "- A named human is `individual-person`, not `person`. `person` stays for pronouns and unnamed people."},
{"op": "delete", "old": " (*a tall man*: `:mod (t / tall)`)"},
{"op": "delete", "old": " Ordinals: `(o / ordinal-entity :value 2)`."},
{"op": "delete", "old": " (*the meeting*, 探索 as a noun)"},
{"op": "delete", "old": "*he walks to work*, "},
{"op": "delete", "old": " Example: a periodical printed in some colour or format → `(y / 印刷-01 :manner (c / <colour word>) :aspect habitual)`."},
{"op": "replace", "old": "Types as in AMR (`country`, `city`, `organization`, `company`, ...). A celestial body is `planet`/`star` + `:name`. Any named being, also a fictional character or alien, is `individual-person`; a common category noun before a name is the concept, with `:name` for the rest.", "new": "Any named being (human, character, alien, mascot) is `individual-person`, never `person` or the category noun; a name of common words is still a name (one `:op` per word), and a category word written with it at first mention goes inside the name. 地球, 月球, 太阳 are names: `planet`/`star` + `:name`."},
{"op": "replace", "old": "- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.", "new": "- Within one sentence, only pronouns and unexpressed mentions are re-entrancies; a mention with its own noun (shortened name, repeated head noun) is a new node plus a `:same-entity` triple."},
{"op": "insert_after", "anchor": "The event under its `:ARG2` does get them.", "text": "\n  - An abstract predicate that is the content of a saying or thinking verb gets a modal parent but no temporal parent; its inner events are `(reporting-verb :overlap e)`."},
{"op": "insert_after", "anchor": "等 / *etc.* closing a list is always its last `:opN`, not `:mod`.", "text": " List-item activity nouns, and an idiom filling an abstract predicate's value slot, are plain entities (no sense, aspect or triples). If N has no outer role but a relative-clause verb, that verb heads the clause (and is the anchor) with N as its argument."},
{"op": "replace", "old": "is `habitual`, even with 了 or other completion marking.", "new": "is `habitual`, even with 了 and also as an event nominal (overrides `process`). Another event nominal for an ongoing generic activity is `activity`."},
{"op": "replace", "old": "Possession, belonging, existence and knowing verbs stay `state` even with 了, 过, 曾经 or a duration modifier.", "new": "Possession, belonging, existence, survival and knowing verbs stay `state` even with 了, 过, 曾经, a duration modifier or under *continue*."},
{"op": "insert_after", "anchor": "A conceiver that is not in the text is `null-conceiver`.", "text": " Write `(author :full-affirmative null-conceiver)` only if `null-conceiver` is a parent in that sentence."},
{"op": "insert_after", "anchor": "attached to the word it scopes over (often the head noun).", "text": " After a place noun (在 N 中/上/里) the postposition node (`:op1` N) fills the verb's location role if the frame has one, else `:place`."},
{"op": "replace", "old": "adds no `:ARG0` by itself", "new": "adds no `:ARG0` or `:possessor`"},
{"op": "insert_after", "anchor": "Copy the numbers from the roleset's role list every time.", "text": " Traps: 有 has possession, existence/relationship-with and list-inclusion senses; count-as verbs (算是 type) number their roles from `:ARG0`."}
]}
```