I ranked the problems by how many judged units each one cost. The main sentence-level problem is how the first and later mentions of an entity are handled in a long sentence. The other problems are smaller: an argument number that was not copied from the frame, a connective that refers back to the previous sentence, one temporal relation, and one same-event link that should not be there.

## Error patterns, most costly first

### 1. An entity defined at its later mention, and part/whole written in reverse (about 5 units)
**Checks hit:** d_core_args_event partial, d_peripheral_entity extra, and g_reentrancy missing and extra.

**What happened:** The sentence opens with a cause clause. In it, a format noun (the old page layout) is the argument of a change verb, and it belongs to a named publication. The annotator wrote that format noun with no `:part-of`. It then defined the publication later, at its second mention (as the owner of a standard, deep inside a relative clause), and joined the two with an inverse `:part` back to the format node. Gold does two things differently:
- it defines the publication at its first mention, as `:part-of` under the format noun;
- it re-enters the publication at the later mention.

Because the annotator's tree was the wrong way round, every edge around these nodes was scored as wrong.

**Why:** The instruction says "write once and re-enter", but it never says *where* the full node goes. The "Formats and parts as arguments" rule speaks of what is created or changed. The annotator applied it to the created object but not to the format noun in the earlier clause. Nothing forbids using the inverse `:part`.

**Change:**
- Add a rule: "Define an entity's full node, with its name and appositive, at its first mention in word order, even when that mention is in a subordinate cause or condition clause placed under the root. Later mentions, including ones inside relative clauses, are re-entrancies."
- Add: "A part or format noun takes `:part-of` to its whole. Never write the inverse `:part` on the whole."
- Extend the parts rule to every format or part noun that is an argument, not only one that is created.

### 2. Argument number defaulted from English habit for an intransitive verb (2 units)
**Checks hit:** d_core_args_event and e_core_labels.

**What happened:** The verb meant "a publication starts publication". Its roleset has only `:ARG0`, which is the publication. The annotator wrote `:ARG1`. The instruction already has this rule ("many Chinese intransitive … verbs have only :ARG0"), but the annotator did not follow it.

**Change:** Make the rule concrete and add it to the checklist: "If the roleset lists only `:ARG0`, the single participant is `:ARG0`, even when it seems like a patient (it starts, ceases, is founded, appears). Before writing any `:ARG1`, confirm that the roleset has an `ARG1`."

### 3. A connective that links back to the previous sentence became a one-armed `but-91` (2 units)
**Checks hit:** a_event_found extra and i_modal extra.

**What happened:** The sentence opened with a contrast word that relates it to the previous sentence. The annotator made the root `but-91` with only `:ARG2`. Gold has no node for the connective: the main verb is the root.

**Change:** Add a rule: "A sentence-initial contrast or continuation connective whose first conjunct is in an earlier sentence gets no node and no modal triple. Use `but-91` or `contrast-91` only when both conjuncts are in the sentence."

### 4. An unwarranted `:same-event` link across sentences (2 units of coref precision)
**What happened:** One sentence says a publication was launched. The next sentence says someone created that publication's format. The annotator linked the two events. Gold does not, because the second event has a different object (a part or format, not the whole publication).

**Change:** Tighten 5.3: "`:same-event` only when both mentions have the same arguments in the same roles. A retelling that changes the object, the agent or the level of detail (the whole versus a part or edition) is not linked."

### 5. A narrative change in a following sentence put `:after` instead of `:overlap` (1 unit)
**What happened:** A sentence marked only with *also* said that a property of the earlier creation had become a characteristic. The annotator put it `:after` the earlier creation event; gold has `:overlap`. The instruction's "(`:overlap` or `:after`)" leaves the choice open.

**Change:** Say: "default `:overlap`; use `:after` only when the text has an explicit later-sequence word (then, later, afterwards)."

### 6. A trailing content clause attached to the whole instead of the created object (1 unit)
**What happened:** The clause telling what the new thing contains went under the publication instead of under the format noun, which is the creation verb's actual `:ARG1`.

**Change:** Clarify: "attach the trailing clause to the node that is the creation verb's own argument, not to that node's `:part-of` whole."

### Minor, no change recommended
- A compound role noun's inner verb got `-01`. Gold has `-00`, even though PropBank has the `-01` frame. The annotator followed the instruction, so the gold is inconsistent here; do not change the rule.

## Keep (these were fully right)
- **Aspect** was 100%: habitual for what a periodical regularly does, performance for completed changes, state for the reified reason and purpose predicates.
- **Clause-linking reason and purpose** were reified as `have-reason-91` / `have-purpose-91`, with no temporal parent.
- **Measure compounds** and **amounts reached**: the measure morpheme is the head, the verb stays the root, and `have-quant-91` with `:unit` carries the number.
- **Named works** have the title brackets as their own `:op`s. **Appositives** use `identity-91` with `:mod` descriptors. **A role noun before a name** uses `have-org-role-91`, with the agent compound decomposed.
- **Fused negation** got `:polarity -` plus full-negative. **Date and era** anchors use `:overlap`. **Relative clauses about earlier events** are `:before` their parent.
- **Coreference chains for the main entity**, each mention linked to its closest earlier mention, were right; only the same-event pair was extra.