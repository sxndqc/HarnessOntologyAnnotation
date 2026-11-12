**Summary of changes.** The instruction was at the 30,000-character limit, so I first freed space. I removed redundant text: the generic intro paragraph, the long two-level overview, the entity-type list, a duplicated decade rule, a generic self-check bullet and the "precision" line. The new rules target the costliest problems in the critique:

1. **Coreference within a sentence (largest cost).** The old rule treated every same-sentence coreference as re-entrancy. It now splits two cases:
   - A pronoun or dropped argument re-uses its antecedent's variable. This includes 他们/*they* used for an organisation or publication.
   - An overtly repeated name or noun gets its own node plus a `:same-entity` triple.
   - A possessive pronoun on an event nominal is omitted.
   - A pronoun in a later sentence links to the antecedent entity.
   - The checklist line is updated to match.
2. **Paired 虽然/尽管 … 但是/不过/却.** In one sentence this now gives `but-91`; unpaired 虽然 keeps `:concession`.
3. **`:quote` is mandatory.** It goes on the top event of reported or quoted content and on each of its conjuncts, including passive reporting. A quoted slogan's content takes `:quote` on its framing node.
4. **后来 chains.** 还/也 right after 后来 gets no node, and a dropped later subject re-enters the first clause's subject.
5. **Existing rules made visible.** The control-verb re-entrancy and the shared time expression over both halves of `but-91` are added to the checklist.
6. **Frequency and location.**
   - Frequency adverbs → `:frequency`.
   - Every location postposition becomes `(中 :op1 N)`.
   - Check the roleset for a location argument before using `:place`.
7. **Named characters.** Fictional named characters are `individual-person`. A bare category noun right before a name is the type concept, not an apposition.
8. **Temporal anchoring.** In a coordination, the anchor is the first conjunct's event. `have-mod-91` and `identity-91` get no temporal parent, even inside reported content; their eventive argument takes the matrix verb as parent.
9. **Omitted head noun.** It is `implicit-argument`, not `thing`.

```json
{"summary": "Freed space by trimming redundant text; added rules for same-sentence pronoun vs repeated-noun coreference, paired concessive -> but-91, mandatory :quote, 后来 chain subject re-entry, :frequency adverbs, location postpositions/roleset location args, named characters and category nouns before names, coordination anchor and no temporal parent for have-mod-91/identity-91, implicit-argument; checklist updated.", "edits": [
{"op": "delete", "old": "Abridged UMR 0.9 guidelines for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the\nUMR release data (`author`, `document-creation-time`, `full-affirmative`, `:modal-strength`, `:refer-person`)."},
{"op": "replace", "old": "A UMR has two levels.\n\n- **Sentence level**: one rooted, directed graph per sentence in PENMAN notation, adapted from AMR:\n  concepts (events, entities, abstract concepts), the relations between them (participant roles and\n  non-participant roles) and attributes (aspect, polarity, mode, quantity, person and number, degree).\n- **Document level**: three kinds of relations between the nodes of the sentence graphs, across sentences:\n  **temporal** dependencies, **modal** dependencies, and **coreference**.", "new": "A UMR has one graph per sentence (PENMAN, adapted from AMR) and document-level temporal, modal and coreference relations."},
{"op": "replace", "old": "Types: `person`,\n`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,\n`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,\n`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,\n`disease`, `product`, `spaceship`, ... (as in AMR).", "new": "Types as in AMR (`country`, `city`, `organization`, `company`, `planet`, `spaceship`, ...)."},
{"op": "delete", "old": "Decades (X年代) use `:era`. "},
{"op": "delete", "old": "- Precision counts as much as recall: when a link is not clear, leave it out.\n"},
{"op": "delete", "old": "- Before the next sentence, check the graph: every meaningful word has its concept, every event its aspect, every\n  role the right direction; at the end check the document-level relations cover every event and entity."},
{"op": "replace", "old": "- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.", "new": "- Within one sentence, a pronoun (also 他们/*they* for an organisation or publication) or a dropped argument re-uses its antecedent's variable, no own node; a possessive pronoun on an event nominal is omitted. An overt repeated name or noun (short name, bare head noun) gets its own node plus a `:same-entity` triple. A later sentence's pronoun links to the antecedent entity."},
{"op": "insert_after", "anchor": "*although* (虽然, 尽管) → `:concession`.", "text": " With 但是/不过/却 later in the same sentence, 虽然/尽管 gives `but-91 :ARG1 <concessive clause(s)> :ARG2 <main clause>` instead."},
{"op": "replace", "old": "The\nUMR release data also marks it with `:quote <reporting event>` when the content is a quotation.", "new": "The reported content's top event, and each of its conjuncts, always gets `:quote <reporting event>` (also passive 被指/被称); a quoted slogan's content gets `:quote` on its framing node."},
{"op": "insert_after", "anchor": "no node for 后来.", "text": " nor for 还/也 right after it; a dropped subject of the later clause re-enters the first clause's subject."},
{"op": "replace", "old": "- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.", "new": "- Same-sentence pronouns are re-entrancies, repeated nouns own nodes + `:coref`; control subjects re-enter nominal complements; a time over both halves of but-91 attaches to both."},
{"op": "insert_after", "anchor": "`:temporal`, not `:mod`.", "text": " Frequency adverbs (经常, 常常, 往往, 重复; *often, repeatedly*) are `:frequency`."},
{"op": "insert_after", "anchor": "The place rule holds for abstract nouns too.", "text": " Every location postposition likewise: 在 N 中/上/里 → `(z / 中 :op1 N)`. Check the roleset for a location argument (出现-type) before using `:place`."},
{"op": "replace", "old": "A named human is `individual-person`.", "new": "A named human or character, fictional too, is `individual-person`. A bare category noun right before a name (no 的, no title) is the type concept, not an apposition."},
{"op": "replace", "old": "Pick one anchor event (usually the main eventive predicate)", "new": "Pick one anchor event (the main eventive predicate; in a coordination, the first conjunct's)"},
{"op": "replace", "old": "(`identity-91`, `have-role-91` of a defining \"A is a B\" sentence);", "new": "(`identity-91`, `have-mod-91`, `have-role-91` of a defining \"A is a B\" sentence), also inside reported content; their eventive argument takes the matrix verb as parent;"},
{"op": "insert_after", "anchor": "A plural noun gets `:refer-number plural`.", "text": " An omitted head noun is `implicit-argument`, not `thing`."}
]}
```