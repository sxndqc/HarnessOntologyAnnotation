# Review of the annotation of a five-sentence Chinese document (founding and circulation history of a tabloid)

Most checks are high. These cost the most: aspect (F 73), reentrancy (F 0), temporal (F 83), modal (P 75) and coreference (P 71). Almost every lost unit comes from one of the patterns below. They are listed from most to least costly.

## 1. Over-annotating the decomposed "verb + 量" quantity noun (about 12 units)
**Checks:** c_aspect (4 extra), i_modal (4 extra), h_temporal (2 extra), j_coref (2 extra).

**What happened:** The annotator split the quantity noun correctly into `量 :quant-of verb` plus `have-quant-91`. It then treated both inner nodes as full events:
- it gave the inner verb `:aspect process` and an author modal link;
- it gave `have-quant-91` `:aspect state`, a temporal parent and a modal parent.

The gold gives neither inner node an aspect. Neither gets a modal link, and `have-quant-91` gets no temporal link. Only the inner verb gets a temporal link: `:overlap` with the clause verb.

The annotator also linked the two quantity nouns of two sentences as `:same-entity`. They are the same measure at different dates with different values, and the gold links nothing.

**Why:** Three general rules pulled the annotator the wrong way, and there is no exception for this structure:
- aspect step 3 ("a process noun → process");
- "every node that carries :aspect gets a modal parent";
- "a process nominal … do not leave it without a parent".

**Change:** Add to the quantity-noun rule in 3.1 and 5.1:
- "In a decomposed quantity noun, neither the inner verb nor the `have-quant-91` gets `:aspect`.
- Neither gets a modal link.
- Only the inner verb gets a temporal link (`:overlap` with the clause verb). `have-quant-91` gets none.
- A measure noun (circulation, sales, population, price) mentioned again at another time, with another value, is not coreferent. Corefer only its owner entity."

## 2. Where a named work goes in a long sentence with several clauses, and its re-entrancy (about 5 units)
**Checks:** g_reentrancy (1 missing, 1 extra), d_peripheral_entity (1 extra, 1 missing), plus a placement that cost a core role.

**What happened:**
- The tabloid is the subject of a change clause ("X will change from A layout to B layout"). The annotator built the tabloid in full later, inside a "does not meet X's standard" clause, and pointed back with an inverse `:part` to the change clause's component noun.
- The gold builds the named entity, with its apposition, where it first appears in reading order: as `:part-of` of the component noun (the layout). It then uses a re-entrancy for the later `:possessor`.

**Why:** The instruction says nothing about which mention of a re-used entity carries the full node. It also does not say that the topic of a change clause is the whole, of which the changed component is a part.

**Change:**
- "When an entity occurs more than once in a sentence, write its full node (name, apposition) at its first occurrence in reading order. Later mentions are re-entrancies.
- In 'X 由 A 改为 B', when A and B are components (layout, edition, format) of the subject X, X is `:part-of` on A. X is not a separate argument, and the relation is not written as an inverse `:part`."

## 3. Attaching a trailing descriptive clause when the object is "component of a named work" (2 units)
**Checks:** d_core_args, c_aspect.

**What happened:**
- The object was "[colour] 版面 的 《N》", which the component rule correctly makes `版面 :part-of 《N》`. The annotator then attached the trailing clause "containing articles …" to the named work. The gold attaches it to the head component noun.
- The annotator gave the containing verb `state`; the gold gives `process`.

**Why:**
- The relative-clause rule says "attach to the object just introduced", but it does not say which node that is when the object has been restructured.
- The aspect rule says "the capacity or content of a publication … (`process` or `state`)". That leaves the choice open, and the annotator picked the wrong one.

**Change:**
- "When the object has been restructured by the component rule, a trailing relative clause attaches to the head node of the object, the component noun.
- A verb saying what a publication or its section contains or holds is `process`." Remove "or state".

## 4. Appositive `identity-91` inside a noun phrase gets attributes (2 units)
**Checks:** c_aspect (extra), i_modal (extra).

**What happened:** The annotator gave the apposition reification of the named tabloid `:aspect state` and an author modal link. The gold gives it neither.

**Why:** The instruction says "copular and identity predicates … do get a modal parent". It does not tell a predicated identity ("A is a B") apart from an appositive one.

**Change:** "An `identity-91` that reifies an apposition inside a noun phrase gets no `:aspect`, no temporal link and no modal link. Only a predicated identity (a copular sentence) gets a modal parent."

## 5. Linking a sentence to the previous one with "also" (1 unit, structural)
**Check:** h_temporal.

**What happened:** The sentence says the printing style "also became" the publication's feature. The annotator anchored its main event to `document-creation-time :before`. The gold uses `(previous anchor :overlap main event)`.

**Why:** The rule exists ("*also became* … 于是 → `:overlap`"), but the annotator did not follow it. The word "also" (也) is not listed as a trigger.

**Change:** List 也/还 + a change-of-state verb (成, 成为, 变成) explicitly among the triggers that link the anchor to the previous sentence's anchor with `:overlap`.

## 6. Habitual aspect for a production practice used as a noun subject (1 unit)
**Check:** c_aspect.

**What happened:** "Black-and-white printing became its feature." The annotator gave printing `process`, following step 3. The gold gives `habitual`.

**Why:** Step 1 is limited to "Only verbs of publishing or reporting", so printing was excluded.

**Change:** Widen step 1 to the routine production practices of a publication or organisation: printing, issuing, publishing, broadcasting. Say that step 1 also wins when the event is a noun used as an argument.

## 7. Decade dates (2 units, plus the decade's temporal relation)
**Checks:** c_other_attributes, h_temporal.

**What happened:**
- The annotator wrote `:decade 1980`, but the instruction already says "Decades (X年代) use `:era`". This is a rule not followed, so make it stand out: put it in the Dates paragraph and in the checklist.
- It used `:contained` because a decade is "a long span". The gold uses `:overlap`.

**Change:** "A date expression of the clause, whether a year, a decade or a span, takes its event with `:overlap`." Drop the `:contained` exception, or limit it to explicit "during/within" wording.

## 8. A frame for a connective that opens a sentence (1 unit)
**Check:** a_event_found.

**What happened:** The annotator built `but-91` with only `:ARG2` for a 不过 at the start of a sentence. The gold has no such node.

**Change:** "A connective at the start of a sentence (不过, 但是, 然而, 因此) that relates the sentence to an earlier one gets no discourse frame. Annotate the clause alone."

## Minor
- The gold uses a `-00` sense for the founder verb inside the "verb + 人" role noun, although PropBank has `-01`. This costs 1 unit and is likely a gold inconsistency. No change is needed.

## Keep these rules: the annotator applied them correctly
- The reified `have-reason-91` / `have-purpose-91` nesting, with `state` aspect and author links.
- `have-org-role-91` with the "人 + `:ARG0-of` verb" founder role noun.
- Named entities with the 《》 tokens and the `·` token, `newspaper` as the type, and no `:wiki`.
- The component noun as `:part-of` the work.
- The change frame with `:ARG1` / `:ARG2` (not `:source`).
- The split of the quantity noun with `have-quant-91` and the classifier as `:unit`.
- Temporal linking inside the sentence:
  - the purpose clause `:overlap`s its main event;
  - the event left over from earlier is `:before` the event of its clause;
  - the reason clause is ordered with `:before` against its result.
- `full-negative` for the negated "meet" verb.
- The `已经` and `也` adverbs as `:mod` on the predicate.
- Coreference of the publication across sentences, each mention linked to its closest earlier one.