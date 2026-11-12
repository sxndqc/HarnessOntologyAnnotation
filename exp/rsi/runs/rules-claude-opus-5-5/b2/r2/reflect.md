I made eight compact edits. Each targets a pattern from the critique that will recur on other documents, and the total stays under the 30,000-character limit.

1. **Decomposed quantity noun.** The inner verb and `have-quant-91` get no `:aspect` and no modal link, and `have-quant-91` gets no temporal link. The same measure at another time or with another value is not coreferent.
2. **Full node at first occurrence.** An entity used twice in a sentence is written in full at its first mention in reading order; later mentions are re-entrancies. In 由X改为Y with component nouns, the subject is `:part-of` on X.
3. **Trailing clause on a restructured object.** It attaches to the component noun. A verb saying what a publication contains is `process`, no longer "process or state".
4. **Appositive `identity-91`.** It gets no aspect and no temporal or modal links.
5. **Linking to the previous sentence.** 也/还 + a change-of-state verb is now listed as a trigger for this link.
6. **Habitual step.** It now covers routine production practices such as printing, including when the event is a noun used as an argument.
7. **Dates.** A decade is `:era`, never `:decade`. Years and decades take `:overlap`; `:contained` is kept only for explicit during/within wording.
8. **Sentence-initial connective.** It gets no discourse frame.

```json
{"summary": "Quantity-noun inner nodes get no aspect/modal (have-quant-91 no temporal), measures not coreferent; full node at first mention; change-clause components take subject as :part-of; trailing clause attaches to component noun; contains = process; appositive identity-91 gets no attributes/links; 也+成为 triggers link to previous anchor; habitual widened to production practices incl. nouns; decades :era and :overlap; no frame for sentence-initial connectives.", "edits": [
{"op": "insert_after", "anchor": "on the quantity noun, not a separate `thing` argument.", "text": " Neither the inner verb nor `have-quant-91` gets `:aspect` or a modal link, and `have-quant-91` gets no temporal link. A measure noun (circulation, sales, price) at another time or value is not coreferent; corefer only its owner."},
{"op": "insert_after", "anchor": "(re-entrancy: `:ARG0 s3p` above).", "text": " Write an entity's full node (name, apposition) at its first occurrence in reading order; later mentions are re-entrancies."},
{"op": "replace", "old": "the original X is `:ARG1` and the result Y is `:ARG2`; never `:source`.", "new": "the original X is `:ARG1` and the result Y is `:ARG2`; never `:source`. When X and Y are components (layout, edition, format) of the subject, the subject is `:part-of` on X, not its own argument and not an inverse `:part`."},
{"op": "replace", "old": "and the work is its `:part-of`; modifiers of the component (colour, style) stay on it.", "new": "and the work is its `:part-of`; modifiers of the component (colour, style) stay on it. A trailing relative clause on such an object attaches to the component noun."},
{"op": "replace", "old": "Only verbs of publishing or reporting; the capacity or content of a publication (contains articles, has N pages) is not habitual (`process` or `state`).", "new": "Only routine production practices (publishing, printing, issuing, reporting, broadcasting), also when the event is a noun used as an argument; what a publication contains or holds (articles, N pages) is not habitual but `process`."},
{"op": "replace", "old": "Copular and identity predicates get no temporal parent but do get a modal parent.", "new": "Copular and identity predicates get no temporal parent but do get a modal parent. An `identity-91` reifying an apposition inside a noun phrase gets no `:aspect` and no links at all."},
{"op": "replace", "old": "explicitly continues from it (*also became*, *as a", "new": "explicitly continues from it (也/还 + 成/成为/变成, *also became*, *as a"},
{"op": "replace", "old": "clearly a long span and the event a point inside it.", "new": "explicitly a span (during, within, 期间); a year or decade takes `:overlap`."},
{"op": "insert_after", "anchor": "`:decade`, `:century`.", "text": " A decade (X年代) is `:era`, never `:decade`."},
{"op": "insert_after", "anchor": "These frames take `:ARG1`/`:ARG2`, never `:op1`/`:op2`.", "text": " A connective opening a sentence (不过, 但是, 然而, 因此) that relates it to an earlier sentence gets no frame; annotate the clause alone."}
]}
```