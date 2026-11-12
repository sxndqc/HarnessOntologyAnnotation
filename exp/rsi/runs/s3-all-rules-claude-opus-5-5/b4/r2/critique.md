The costliest losses come from how the instruction handles reported speech, time phrases and noun phrases that hide an extra frame. The perfect scores (coreference chains, person/number on pronouns, document format) show the basics should stay. Problems are ordered by cost, most costly first.

## 1. Modal links for a series of reports by one source (≈9 modal units, plus 3 reentrancy units)
**What happened:** A periodical was the subject of several coordinated reporting verbs (report, say, claim). The annotator gave each reporting verb an author link, and gave each predicate of the reported content two links: one from the author and one from the periodical. Gold does it the other way round:
- the source entity gets `(author :full-affirmative src)`;
- each reporting verb gets `(src :full-affirmative verb)`;
- the content's predicates get an author link only.

Gold also puts `:quote <reporting verb>` on every event of the content, nested reason events included. The annotator only put it on the content's top event.

**Why:** Section 5.2 tells the annotator to give the content "both" links and to give the speaker an author link. It never says that the reporting act itself sits under the speaker.

**Change:** Rewrite the reported-speech rule:
- the speaker node is under the author;
- every reporting or claiming verb with that speaker as subject has the speaker as its modal parent;
- content predicates get the author only.

Extend the `:quote` rule to every event inside the content (reason, manner and complement events too).

## 2. Time phrases: "named event + 时" and "clause + 时" (≈12 units across concepts, names, entities, temporal and peripheral checks)
**What happened:**
- **Year + event noun + 时:** The annotator built a 时 node over the event noun with a separate `date-entity`. Gold makes the whole phrase a named `event` (year, 年 and event noun as `:opN`), used directly as `:temporal`, with no 时 node, no date node and no temporal link. The main verb then links to `document-creation-time` directly.
- **Clause + 时:** Gold uses the clause's event itself as `:temporal`, again with no 时 node.

**Why:** The annotator extended the postposition rule (在 N 中 → `中 :op1 N`) to 时. The named-event rule exists but has no trigger for this case.

**Change:**
- Add: "时 / 的时候 after a clause or event noun gets no node; the event itself is `:temporal`."
- Add: "year + 年 + event noun is a named event; never split off a date-entity."
- Add: a date inside reported content gets no temporal parent. The content event takes the reporting verb as parent (`:before` for a past event claimed later), not the date.

## 3. A noun with a content complement, and a news noun with a quoted title (≈10 units)
**Ability-type noun + verb phrase** (have the ability to X):
- Gold: `noun :ARG1-of (identity-91 :ARG2 event)`, with `:aspect state` and an author modal link. The event gets `(author :neutral-affirmative event)`, not a link from 有.
- Annotator: `:mod event`, with the modal parent set to the 有 verb.

**Measure + news/article noun + 「title」:**
- Gold: the news noun is the head. It carries `:quant`/`:unit` and `:part-of` the periodical, and is `:ARG1-of identity-91 :ARG2 (publication :name …)` with `:aspect state` and an author link.
- Annotator: made the publication the head and moved the news noun, the quantity and the owner onto it.

**Why:** Section 2.2 makes any quoted title "next to an article/news noun" the publication itself. It also says an apposition identity-91 gets no aspect and no links.

**Change:**
- Keep "publication with quant/unit" only for a classifier + quoted title with no common noun.
- When a common noun is present, that noun is the head, and identity-91 links it to the titled publication.
- This identity-91, and the "ability/right/chance to X" identity, take `:aspect state` and an author modal link (no temporal link). The no-aspect rule should apply only to apposition on a named entity.
- An ability complement gets author `neutral-affirmative`.

## 4. Unsplit compounds and attributive predicates (≈10 units)
The annotator kept several kinds of compound whole that gold splits:
- **Verb/adjective + 者:** Gold uses `者 :ARG0-of (X-00 :aspect state)`. Section 2.2 names only 人/者 after a verb, so an adjective-like stem was not split.
- **Verb + 人, where the person undergoes the verb:** Gold uses `人 :ARG1-of (V :aspect process)`.
- **全 + noun:** Gold uses `noun :mod 全`.
- **Attributive adjective that has a roleset:** Gold uses `:ARG0-of (adj-01 :aspect state)`, with an overlap link to the event it modifies and an author link. The annotator used a plain `:mod`, although section 3.1 already says to check PropBank first.

**Change:**
- State the split rule generally: any stem before 人/者 that is a predicate (verb or adjective) becomes an event. Use `:ARG0-of` if the person does or has it, `:ARG1-of` if it is done to them.
- Split 全/各/该-type prefixes as `:mod`.
- Repeat in the checklist: "every attributive adjective: look up its roleset before writing `:mod`."

## 5. Adverbs that only chain clauses (≈7 extra nodes and peripheral units)
**What happened:** The annotator gave nodes to 还 and 甚至 opening a later conjunct, and to 也 in a 但…也 clause or a reported clause. Gold drops them all; it keeps 也 only where it links to a previous sentence.

**Why:** Section 3.1 says "every adverb that carries meaning gets its own node."

**Change:** Add an exception: 还, 甚至, and 也 that only mark a clause as additional or climactic relative to another clause of the same sentence (a coordination chain or a but-91 second half) get no node.

## 6. Verbs that express means or reason, and verb concepts (≈8 units)
- **靠/凭/通过 N (by relying on N) + main verb:** Gold has no node for 靠-type verbs; N or its event becomes `:reason` of the main verb. The annotator made a `靠-01 :manner` event, which brought an extra node, reentrancy, temporal and modal links. Add this as a rule.
- **Missing senses:** Words missing from PropBank must be `-00`. The annotator wrote `-01` twice without checking.
- **Verb + result word:** A verb plus its result complement written as one token (V到) is one concept, `V到-01`.
- **Sense of 有:** having an ability takes a different 有 sense from having or owning something.

Make the instruction say: "write `-00` unless `propbank_lookup` returned that exact roleset."

## 7. Purpose frame, frame modals, and the aspect of purpose events (≈5 units)
**What gold did:**
- Used `have-reason-91` for 为了 + clause.
- Gave the reified frame no `:aspect` and no modal link.
- Gave but-91 no modal link either.
- Gave the purpose event `performance` aspect, because it was carried out in a past report.

**Instruction conflicts:** Section 2.5 says to give both frames `:aspect state` and an author link, and section 4.1 says a purpose is `activity`.

**Change:**
- Discourse frames (but-91, contrast-91, have-reason-91, have-purpose-91) take no aspect and no modal link.
- A purpose that was actually carried out in a past narrative takes the aspect of the main event.
- Mention that gold treats 为了 clauses as `have-reason-91`.

## 8. Non-core roles of noun modifiers (≈6 units)
| Modifier | Gold role | Annotator's role |
|---|---|---|
| Content or part of a publication | `:part-of` | `:possessor` |
| Issue or matter "of" a subject (问题 of X) | `:topic` | `:possessor` |
| Domain noun on a policy-type noun (外交 政策) | `:topic` | `:mod` |
| Named legislative body as the location of a group | `building :place` | organization as `:mod` |

Extend the section 3.1 role list with these.

## 9. Temporal links
**Coordinated clauses:** Gold chains the conjuncts in sequence (op1 → op2 → op3), with each later conjunct `:overlap` the previous one. The annotator hung them all on op1. Change "link the other events to the anchor" to chain them.

**Relative-clause events:** A participle on a noun (synthesised photo) `:overlap`s the clause verb rather than coming `:before` it. The event nominal inside it hangs on that participle.

**Characterising states:** In a document narrating a past entity, characterising states take `(document-creation-time :before e)`, not `:overlap`.

## 10. Example sentences
A sentence opened by 如/例如 that illustrates the previous one is `have-example-91 :ARG1 (implicit-predicate) :ARG2 <main event>`. The annotator dropped 如 entirely. Add this to section 2.5.

## Keep
- Coreference: each mention links to the nearest earlier mention, and same-sentence pronouns re-use the antecedent's variable (100% on chains).
- Pronouns as `thing`/`person` with person and number.
- Bare classifier + 「」 titles as `publication` with `:quant`/`:unit` and the 「」 marks as `:opN`.
- `individual-person` for named people, with no `:wiki` in Chinese documents.
- `document-creation-time :before` on the anchor of past narrative sentences.
- `process` for event nominals that modify a noun.
- `performance` for completed past participles.
- Core-argument choice (core arguments of events about 94%, core role labels 97%).