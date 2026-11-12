# Review of the annotation of document sentences 11–15: error patterns and changes to the instruction

The annotator found every event (event found 100, event concept 100) and got person/number attributes and the document format right. Most points were lost on the document-level checks: coreference (F 11), temporal (F 54), modal (F 70), and on re-entrancy (F 44). Below, the patterns are ordered by cost, most costly first.

## 1. A plural pronoun that stands for an organization or publication became a new `person` node
**Cost:** about 13 units.
- Coreference (j): 6 units. The whole chain for the publication broke.
- Re-entrancy (g): 2 units.
- Entity found (a): 1 extra unit.
- Core arguments of events (d): 1 extra argument.
- Modal (i): 3 units, partly.

**What happened.** A plural pronoun ("they / their") referred to a periodical named earlier in the same sentence.
- The annotator made a fresh `person 3rd plural` node, attached it as an extra `:ARG0` and `:possessor`, and chained the next sentence's pronoun to that new node.
- Gold re-enters the publication's node within the sentence. Across sentences, gold links the next sentence's `person` node to the publication with `:same-entity`.
- Gold also leaves out the agent of an event noun inside a reported clause when no word expresses it.

**Why.** Section 2.4 says every pronoun is `person`/`thing`. Nothing says that a pronoun whose antecedent is an organization or publication in the same sentence is a re-entrancy of that node.

**Change.** Add to 2.4 and 5.3:
- "A pronoun (also a plural *they / 他们*) whose antecedent is an organization, company or publication is that entity. In the same sentence, re-enter its variable; create no `person` node. In a later sentence, write the `person` node and link it `(organization :same-entity person)`, never to another pronoun node."
- Add: "The possessive pronoun of an event noun does not by itself add an `:ARG0`, unless it is the only way the agent is expressed."

## 2. Reported content was not marked with `:quote`, and its modal conceiver was wrong
**Cost:** about 12 units.
- Re-entrancy (g): 4 units for missing `:quote` edges.
- Modal (i): about 6 units.
- Temporal parents (h): 2 units, linked to this.

**What happened.**
- Gold puts `:quote <reporting event>` on the top content event under a verb of claiming, and on events in a quoted slogan. For a slogan, the quoted event points to the `identity-91` that introduces it.
- Gold gives the events of the clause that the claim contrasts with a second parent: the claimant as conceiver as well as the author.
- In a passive allegation (被指), gold does not use the reporting verb as conceiver.

**Why.** Section 3 mentions `:quote` only as something "the release data also marks". So the annotator treated it as optional and wrote none.

**Change.**
- Make it a rule: "Every content event of a verb of saying, claiming, alleging or labelling (also a quoted slogan) gets `:quote <the reporting event or the predicate that introduces the quotation>`. Put it on the top content event and on each conjunct."
- For the modal side: "Content of a claim gets `(speaker :full-affirmative e)`. When the speaker is an organization, the organization node is the conceiver. Never use the reporting verb itself as conceiver when the speaker is an expressed entity."

## 3. Temporal parents were chosen wrongly in coordinated and reported structures
**Cost:** about 11 temporal units (h F 54).

**What happened.**
- **Coordinated root.** When the root is an `and` of two clauses, gold anchors the **first conjunct** to `document-creation-time` and makes the second conjunct `:overlap` the first. The annotator anchored on the second conjunct.
- **Claims with contrasting clauses.** Under a verb of claiming, gold makes the claimed event the parent of the other events in the sentence that describe the same activity. Gold gives the `have-mod-91` content predicate no temporal parent. The annotator hung everything on the claiming verb and gave `have-mod-91` a parent.
- **Nodes gold leaves out.** The annotator gave temporal parents to a relative-clause verb inside a created object, using `:after` with no explicit order word. It also gave a temporal parent and a modal parent to an idiom used as a goal noun in 以…为目的.
- **Present tense in a past story.** The annotator read a generic "can be regarded as" evaluation, about a publication that had already ceased, as present (`:overlap` DCT). Gold has `:before`.

**Change.**
- "When the root is a coordination, the first conjunct is the anchor and the later conjuncts `:overlap` it, unless an order word says otherwise."
- "Under a verb of claiming, the claimed event is the reference time of the other descriptions of the same activity. Abstract content predicates (`have-mod-91` as claimed content) get no temporal parent."
- "Use `:after`/`:before` only with an explicit order word."
- "A concept that only names a goal or content (an idiom as the `:ARG2` of the 以…为目的 identity) is an entity: no aspect, no temporal or modal triple."
- "Statements about a publication or organization that the text has already said no longer exists are past (`:before` DCT), even when they are generic."

## 4. Frames, senses and core-role numbers did not follow the roleset
**Cost:** about 12 units.
- Event sense (b): 2 units.
- Core labels (e): 5 units.
- Core arguments of events and of abstract predicates (d): 3 units.

**What happened.**
- **算是.** Its roleset is `ARG0` = the thing described, `ARG1` = what it is considered as. The annotator used `ARG1`/`ARG2` from English habit.
- **出现.** The roleset has a location argument. The annotator put the 在…中 locative under `:place`. Gold puts it as a numbered argument (`:ARG1`).
- **指.** A passive "is alleged that" was given `指-01` (refer to) instead of `指-02` (claim).
- **有.** A relationship that two parties have was given `有-01` (ownership) instead of `有-03`.

**Why.** The instruction already has a required lookup. It was not followed for frames that are not -01, nor for passive verbs of saying.

**Change.** Add to the lookup rule:
- "Also check verbs of saying and alleging in the passive (the claim sense)."
- "Check 有 used for relations or existence (not possession)."
- "A locative phrase that a roleset lists as an argument is that numbered role, not `:place`."
- "A V是 verb's roleset starts at `ARG0`."

**Smaller point.** For a superlative with an implicit head, gold here numbered the property `:ARG1` and the degree word `:ARG2`. Other gold data uses `:ARG2`/`:ARG3`, as the instruction table does. Keep the table, but note this headless variant only as possible.

## 5. A comitative partner in a symmetric relation, and a descriptor written before a name
**Cost:** about 10 units.
- Entity concept (a): 2 units.
- Name tokens (f): 2 units.
- Other attributes (c): 4 units.
- Core labels (e): 1 unit.
- Coreference (j): 2 extra units.

**What happened.**
- In "X 与 Y 有 关系" (X has a relationship with Y), gold coordinates both parties, `:ARG0 (and :op1 X :op2 Y)`. The annotator used `:companion`.
- When a generic species or category noun stands before a name in a later mention, gold makes the noun the concept and the name only the rest. The annotator, following the instruction's rule that "a descriptor word written as part of the name is an `:op`", put the noun into the name.

**Change.**
- "For a reciprocal or symmetric relation (与/和/跟 Y 有关系, 合作, 结婚 type), both parties are the conjuncts of `and` in the first role; no `:companion`."
- Narrow the descriptor rule: "A common category noun before a name is the concept with `:name` for the rest. Write it as an `:op` only when it is fixed into the name itself."

## 6. A repeated short form of a name in the same sentence was re-entered
**Cost:** about 8 units.
- Entity concept (a): 1 unit; granularity (a): 2 units; peripheral roles (d): 2 units; coreference (j): 1 unit; re-entrancy (g): 1 unit.
- The missing node also shifted the alignment of an adverb.

**What happened.** A later mention used a shortened head noun of a name ("the weekly" after the full title). Gold makes it its own node, `:part-of` the thing it is part of, with a `:coref` triple inside the sentence.

**Why.** The instruction contradicts itself. Section 1 says "a repeat with its own noun: see 5.3", but 5.3 says "Within one sentence, coreference is a re-entrancy."

**Change.** "Pronouns and zero mentions within a sentence are re-entrancies. A repeated mention with its own noun (also a shortened name) is a new node and gets a `:same-entity` triple, even in the same sentence."

## 7. Aspectual and control verbs: missing shared arguments and wrong aspect
**Cost:** about 7 units.
- Re-entrancy (g): 3 units.
- Core arguments of events (d): 2 units.
- Aspect (c): 1 unit.

**What happened.**
- **Event noun under a stop verb.** For "stop the distribution of X", gold gives the event noun `:aspect process`. The annotator applied the institution "habitual" rule. Gold also re-enters the stopping subject as the event noun's `:ARG0`.
- **Continue verb.** In a main clause with a continue verb (继续), the subject is the continue verb's `:ARG0` (its roleset has an agent) and is re-entered as `:ARG0` of the inner verb.
- **Shared date.** A date that scopes over both clauses of a but-coordination is re-entered as `:temporal` on the second clause.

**Change.**
- "An event noun governed by an aspectual verb (stop/start/continue + nominal) is `process`. Its agent is the aspectual verb's subject, by re-entrancy."
- "In a main clause, the subject of 继续/开始/停止 + verb fills the aspectual verb's agent role and the inner verb's role."
- "A sentence-initial date shared by coordinated clauses is re-entered on each."
- Keep the relative-clause exception as a separate case.

## 8. Smaller issues
- **Modal triples on connectives** (2 units). Gold gives `but-91` / `contrast-91` / `and` no modal triple. State this in 5.2, and keep the exception for `have-reason-91` / `have-purpose-91`.
- **Coreference of generic nouns** (2 units). A bare kind or category noun repeated in two sentences was chained, and gold has no such chain. Extend the 5.3 ban on chains to "generic or kind nouns, and items of example lists".
- **Aspect of a single claim** (1 unit). A claim made by a periodical is a single speech act, `performance`. The "repeated activity of an institution → habitual" rule should cover only publishing, reporting and contents, not a claim about them.
- **Event noun in an example list.** It is treated as an entity (no `-01`, no aspect, no triples).
- **Aspect of a generic activity** (1 unit). A generic ongoing activity in an evaluation is `activity`, not `process`.

## What to keep
The following matched gold and should stay in the instruction:
- The `but-91` with an `and` `:ARG1` for 虽然…不过 (although … but).
- The identity rule for 以 X 为目的 (`目的 :purpose-of E`, with the quantifier as `:mod`).
- `:example (and … 等)` lists, with 等 as the last `:op`.
- Appositive `identity-91` for a parent company.
- The newspaper type and title brackets as `:op`s.
- Splitting the middle dot `·` into its own `:op`.
- `have-rel-role-91` with `:place` and `:mod` on the title noun.
- `planet` + `:name`.
- `consecutive` for a sequence adverb.
- The headless superlative written as `implicit-argument :unit`.
- `:frequency` for frequency adverbs.
- `:mod` for scope adverbs.
- The rule for anchoring a date (`(DCT :before date)`, `(date :overlap anchor)`).
- Full person and number attributes on pronouns.