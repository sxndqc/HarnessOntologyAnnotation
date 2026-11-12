Below are the error patterns, most costly first. For each I give its cost (the judge's checks and about how many units), why it happened, and the change to the instruction.

## 1. Quoted article titles were turned into event structures instead of named publications (about 35 units)
**Cost:** a_entity_concept, f_name_tokens (all the missing names), extra events and entities, d_core_args_abstract, c_other_attributes (stray `:quant`), and the extra temporal, modal, reentrancy and coref triples hung on those invented nodes. This hit three of the five sentences.

**Why:** A title in 「…」 after a count of articles ("one piece of"), or set beside a news or article noun, is the name of a work in the gold. It is `publication :name`, with every word as an `:opN`, the opening and closing 「 」 included. The instruction covers only 《》 titles. So the annotator broke each title into predicates, with names, quantities, role reifications, `:quote` and conceivers inside it. All of that was extra.

**Change:**
- Add a rule: "A quoted headline or article title in 「」 or “” that names an article, used with a classifier or beside an article or news noun, is `(p / publication :name (n / name :op1 "「" … :opN "」"))`. Every word of the title, punctuation included, is an `:opN`. Nothing inside it is analysed: no events, no entities, no `:quote`, no temporal, modal or coref triples. The classifier and number go on the publication as `:unit`/`:quant`."
- When the title is in apposition to a noun ("the article 「…」"), use `(noun :ARG1-of (i / identity-91 :ARG2 publication :aspect state))`. That `identity-91` gets the author as its modal parent and no temporal parent.
- Keep the existing reported-speech analysis only for a quote that is the direct content of a verb of saying or reporting, with no classifier.

## 2. Compound words that should be split into head + modifier (about 15 units)
**Cost:** a_entity_concept and d_peripheral (missing `:mod`) wherever these words appear. Several of the judge's mismatches (one node matched to an unrelated `:mod` node in two sentences) come from the same cause.

**Why:** The gold splits words built as a demonstrative plus a one-character noun, "all/whole" plus a noun, and a verb plus 者/人:
- demonstrative + noun → `noun :mod demonstrative`;
- whole/all + noun → `noun :mod whole/all`;
- verb + 者 for an agent → `者 :ARG0-of verb`;
- verb + 人 for a patient ("cloned person") → `人 :ARG1-of verb`.

The instruction has a verb + 人/者 rule only for the agent case, and it was not applied here. The patient case and the demonstrative case are not mentioned at all.

**Change:**
- Extend 2.2/2.4: "Split a word made of a demonstrative or totality prefix plus a noun into the noun with `:mod` of the prefix. Split verb + 者/人 into 者/人 with `:ARG0-of` (agent) or `:ARG1-of` (patient, e.g. the thing produced) of the verb. A verb not in PropBank is `-00`. The verb gets `:aspect` (state for a disposition, process for a kind), an `:overlap` temporal link to the clause verb, and the author as its modal parent."
- Add a checklist item that names this rule.

## 3. Attributive property words were `:mod` instead of events (about 15 units)
**Cost:** b_event_sense, c_aspect (missing), d_core_args_event, d_peripheral_entity, h_temporal, i_modal.

**Why:** The instruction's last bullet of 3.1 ("a property word used attributively is a `:mod` concept with no aspect and no links") is too broad. In the gold, an attributive modifier that has a Chinese PropBank roleset is an event attached by an inverse role:
- property predicates with an "entity described" `:ARG0` (e.g. 显著-01, 真实-01) → `noun :ARG0-of (x / word-01 :aspect state)`;
- verbs that produce something (e.g. 合成-01) → `noun :ARG1-of (x / verb-01 :aspect performance)`.

Each of these gets an `:overlap` temporal link to the clause event and the author as its modal parent. Only words with no roleset (distinguishing or relational words such as "diplomatic", "moral") stay `:mod`.

**Change:**
- Rewrite that bullet: "Look the modifier up in PropBank. If it has a roleset, annotate it as an event with an inverse role, using the role the roleset gives the described entity. Otherwise use `:mod`."
- Also: an event nominal that modifies a noun (an "X's handshake photo" kind) is `:mod`, with `process` aspect, not `:topic`.

## 4. The modal and temporal treatment of reports by a publication (about 14 units in i_modal and h_temporal)
**What went wrong:**
- **Who is the conceiver.** In the gold, when a publication or other source is the subject of a series of reporting verbs, the source is the conceiver of those reporting verbs: author → source, then source → each reporting verb. Each content event gets only the author as its parent. The annotator did the reverse: author → reporting verb, and source → content.
- **Temporal links in the content.**
  - A past event inside reported content took the reporting verb as its temporal parent, with `:before`. It was not linked to its date.
  - Dates inside the content got no temporal parent.
  - A means or support clause inside the content `:overlap`s its event. The annotator used `:after`.
- **No links for complement events in the content.** An event that is the complement of the content's predicate (e.g. "support X to become president") got no aspect and no modal link.

**Why:** The instruction (5.2) says content predicates get both the author and the speaker as parents. The date rule (5.1) also competes with "an event in a complement clause takes its matrix event as parent".

**Change:**
- State the source-as-conceiver pattern for publications and organisations that report.
- State an order of precedence: "Inside reported content, the matrix reporting verb is the temporal parent (`:before` for a past event it reports). A date inside the content is a `:temporal` role only and gets no document-level link."

## 5. Verb + complement compounds, senses and constructions with 有 and 靠 (about 10 units)
- **Directional or resultative complements.** A verb with such a complement is one concept when PropBank lists the compound (e.g. 点出-01, 贴到-01), even when it is split over two tokens. Use the compound roleset's own roles: for the posting verb, `:ARG1` is the place and `:ARG2` is the thing posted. The annotator had these reversed.
- **"Have the ability to V".** This is `有-06 :ARG1 (能力 :ARG1-of (identity-91 :ARG2 V-event :aspect state))`. It is not `:mod`.
  - The `identity-91` gets the author as its modal parent.
  - The inner event's `neutral-affirmative` comes from the author, not from 有.
- **Relying on a supporter.** "Rely on X('s support) to achieve Y" (靠 X) is `Y :reason X-event` with no node for the reliance verb.
- **Choosing senses.** Add: "Pick the sense whose role glosses fit (有-06 for an ability or an attribute held). Use `-00` for a word that is not in PropBank." The annotator gave `-01` to words PropBank does not list.

## 6. Named events with a year in the name (about 6 units)
A dated election or another named event ("the 2000 presidential election") is `(e / event :name (n / name :op1 "2000" :op2 "年" :op3 …))`. It is not a process noun with a `date-entity`, and it gets no temporal or modal links. Add this to 2.2.

## 7. Example sentences and discourse frames (about 7 units)
- **Sentence-initial "for example".** An opening 如/例如 that offers the sentence as an example of the previous claim is `(h / have-example-91 :ARG1 (i / implicit-predicate) :ARG2 <main event>)`. Add this to 2.5.
- **but-91.** Discourse frames get no modal link. The temporal anchor of a but-91 is its `:ARG1` clause: document-creation-time `:before` for a past-tense description. The `:ARG2` clause `:overlap`s it. The annotator anchored on `:ARG2` and used `:overlap` with document-creation-time.
- **Parts of a publication.** The contents or articles of a publication are `:part-of` the publication, not `:possessor`. Extend the component rule in 3.1 to cover this.

## 8. Purpose clauses and adverbs (about 6 units)
- **为了 clauses.** For 为了 with a shared subject, the gold re-enters the main subject as the purpose event's `:ARG0`. The rule "never fill the agent of a purpose clause" is too absolute. The gold also used `have-reason-91` with no aspect and no modal link.
  - Make the agent rule depend on the subject being shared.
  - Drop the instruction to give the frame `:aspect state` and `(author :full-affirmative h)`.
  - Treat the frame's name as uncertain until other gold data confirm it.
- **Adverbs.** Additive and escalating adverbs that link clauses (还 and 也 in a list of acts, "even" 甚至) got no node in the gold. Narrow "every adverb gets a node" to adverbs that scope over a single predicate.
- **Coreference of repeated country names.** Do not corefer two mentions of a country name inside one sentence when one or both are only modifiers.

## What to keep
The annotator did these well, and the instruction should keep the rules behind them:
- **Structure:** event detection (98 F), granularity (100), format (100), and pronoun person/number (100).
- **Discourse frames:** the `and` frame for chains of reporting verbs, and but-91 for 虽然…但.
- **Classifiers:** classifiers kept as `:unit` with `:quant`.
- **Past events:** `performance` aspect for completed past acts, and document-creation-time `:before` for past sentence anchors.
- **Coreference:** pronouns linked to the publication.
- **Habitual aspect:** `habitual` for a recurring editorial practice.
- **Reported content:** the reported-content analysis for a verb of reporting with a direct clause object, with `:quote` on the content's top event.