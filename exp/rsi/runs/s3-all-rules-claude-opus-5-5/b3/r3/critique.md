I've ordered the problems by how many judged units they cost. Each one has the cost, why it happened, and a general rule to change or add in the instruction.

## 1. Coreference: too many links, and a repeated name given its own node (j_coref P 33; about 9 units, plus a cascade into entity, argument and reentrancy checks)
**Cost:**
- Two category nouns were linked across sentences: a generic kind noun that appears in an example list and again in a later sentence.
- A fictional character mentioned in two sentences was linked. Gold links neither case.
- Inside a quoted slogan in a parenthesis, the publication's name came back without its title marks. The annotator gave it a new node plus `:same-entity`. Gold re-uses the publication's variable.
- That one extra node cost 1 entity_found unit, 1 partial core argument, 2 missing re-entrancies and 4 partial coref chains.

**Why:** Section 5.3 says "an overt repeated name … gets its own node plus `:same-entity`". It never limits coreference to tracked participants with a definite referent.

**Change:**
- A repeated name inside a slogan, gloss, parenthesis or quote in the same sentence that refers to an entity already in that sentence is a re-entrancy, not a new node.
- Do not corefer generic or kind-denoting nouns (bare nouns naming a category, members of an example list), even when the same word recurs.
- Do not corefer a named entity that appears only as an example or list member in one sentence with a later mention, unless the text treats it as a discourse topic.
- Never link a `name` node: the annotator did this once.

## 2. Modal parents for reported content (i_modal; 7 units)
**Cost:**
- **Active reporting verb with a clause object:** the annotator gave the content's events only the speaker as conceiver. Gold gives each content event **both** `(author :full-affirmative e)` and `(speaker :full-affirmative e)`.
- **Later clauses about the same source:** gold also gives the speaker as an extra parent to the restating slogan clause and to the "but" clause about that source's reports.
- **Event nominal inside the content:** a nominal used as the content's argument (not its top) is author-only in gold. The annotator gave it the speaker.
- **Passive reporting verb with no agent:** for the 被指 type, gold does not use the reporting verb as conceiver. It uses the content's subject node, with `(author :full-affirmative <that node>)`. The annotator put the verb in the conceiver slot.

**Change:** Rewrite the reported-speech rule in 5.2:
- The content's predicates get both author and speaker as parents.
- Event nominals inside the content stay with author only.
- When a passive reporting verb has no overt speaker, the conceiver is the content's subject node. That node gets `(author :full-affirmative X)`. Never use the reporting event as conceiver.

## 3. Temporal links inside "but" sentences and reported content (h_temporal 71; 5 units, plus 1 reentrancy)
**Cost:**
- In a past "stopped X, but Y still continues" sentence, the annotator linked the second clause with `:after`. Gold uses `:overlap`.
- The fronted date was not re-entered on the second clause. The instruction already says a time over both halves of but-91 attaches to both, but this was not followed.
- In the reported-content sentence, the slogan clause and the later "but" clause were hung on the reporting verb. Gold hangs them on the first event inside the content: the topic event that the later clauses restate.
- An absolute present judgement with a "can be counted as" verb was given `:overlap` to document-creation-time. Gold uses `:before`.

**Change:**
- In a but-91 or contrast with "still / continue", the continuing clause `:overlap`s the first clause. Never use `:after`.
- Put the date-reentrancy rule in the main body, not only the checklist, and state it is mandatory when the date opens the sentence.
- When later clauses restate or qualify the content of a report, their events take the content's main event as parent, not the reporting verb.

## 4. Superlative nominal with a dropped head (have-degree-91; about 7 units)
**Cost:** The case is a "superlative + adjective + classifier" compound used as the subject, with a partitive "among them" word before it. The annotator kept it as one concept with `:mod` partitive. Gold has:
- `implicit-argument` as the head, with `:unit` set to the classifier;
- `:ARG1-of (have-degree-91 :ARG1 <adjective> :ARG2 <superlative word> :ARG5 <partitive>)`.

**Why:** The instruction contradicts gold three ways:
- It says "do not use `:ARG5`".
- It puts 最 in `:ARG3`.
- It says a partitive word is `:mod`.

**Change:** Add a case. A superlative compound with no head noun (最 + adjective + classifier) is split as gold does above. The partitive word (其中, *among them*) is the comparison set, `:ARG5`, not `:mod`. Limit the "partitive is `:mod`" rule to cases with no degree word.

## 5. Control and argument roles (d_core 86, d_peripheral_event 71)
- **Control not applied:** the subject of a stopping verb was not re-entered as `:ARG0` of its event-nominal complement (publication). The instruction already has this control rule; put it in the checklist, explicitly including nominal complements and the stopping verb.
- **Appearance verb (出现 type):** the annotator followed PropBank (location = ARG0). Gold puts the appearing entity in `:ARG0` and the "in N 中" location in `:ARG1`. State this gold convention, as the instruction already does for belong-type rolesets.
- **Quantity word on an event nominal:** a "most of" quantity word on an event nominal is `:mod` in gold, not `:quant`.
- **Relative-clause head:** when the noun is the object of a relative clause (*the topics they often report*), gold makes the verb the clause's main conjunct and the noun its `:ARG1`. The annotator put the noun at the top with `:ARG1-of`. Add a rule: in "N that X V-s 有 A, B…" (topic sentences), the reported verb heads the clause and N is its `:ARG1`.
- **Missing `:quote`:** the slogan's content event did not get `:quote <its identity-91 framing node>`. The instruction already says this; give an example.

## 6. Aspect (c_aspect 89; 2 units)
- **State verb under "continue":** a survive/exist verb under a continuation verb was given `activity`. Step 2 already lists 生存 as `state`. Add that this holds even under 继续 and 仍.
- **Activity noun:** an activity noun as the predicate complement of a judging verb is `activity` in gold, not `process`. Narrow step 3 (process nominals) to nominals that are arguments of light or experiential verbs or are the subject/object of eventive verbs, not complements of "count as / be".

## 7. Smaller items
- **Bound-morpheme compounds:** a compound made of a bound modifier morpheme and a full noun (parent + company type) splits into the noun with `:mod` the morpheme. Add this to 2.1.
- **Planet names:** a well-known planet name used as a place is a named entity: `(planet :name …)`.
- **Fictional character in an example list:** a character written as "category noun + foreign name" was `individual-person` in gold, with the category noun inside the name. The same character in a later sentence was category noun + `:name`. The gold is inconsistent here, so this is low priority; at most, prefer `individual-person` for named fictional characters in lists.
- **Sense for 领养:** the predicate has a PropBank roleset (`-01`), but gold used `-00`. The cost is one unit; no rule change is advised.

## Keep
- The 以…为目的 purpose-noun identity rule: matched exactly.
- The `have-rel-role-91` rule for a title held through marriage, and `consecutive` with the dropped subject re-entered: both correct.
- The `but-91` rule for a 虽然…不过 sentence (the "although" clause inside `:ARG1`): correct.
- Title marks inside the name, the classifier and example-list rules (`:example (and … 等)`), and `:quote` on each conjunct of reported content: all correct.
- The habitual aspect for a publication's reporting practice, and `performance` for a completed past claim: correct.
- Pronoun handling (refer-person, refer-number; `c_refer` 100) and the event concepts (100): keep as written.