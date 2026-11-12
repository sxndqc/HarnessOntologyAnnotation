The most costly errors fall into four groups:
1. **Reentrancy (F 38):** the instruction forbids filling dropped subjects, but gold fills them.
2. **Over-used habitual aspect** and `have-purpose-91`.
3. **Constructions the instruction does not cover:** "rely on X to …", "have the ability to V", "如" giving an example, verb + 到 verbs.
4. **The invalid role `:poss`**, used where gold has `:part-of` or `:possessor`.

## 1. Dropped subjects are not filled (g_reentrancy R 33 / P 43; also d_core_args)
- **Pattern:** gold re-enters the subject in these cases, and the annotation had none of them (4 missing edges):
  - the shared subject of each later conjunct in a coordinated chain of past actions;
  - the agent of a 为了 purpose clause;
  - the agent of the verb complementing "have the ability to V".
- **Why:** §3.1 says to leave these out: "dropped subjects … in coordination … do not add a re-entrancy", and "never fill their agent with an entity of the main clause". The annotator followed a rule that is wrong.
- **Change:**
  - When a subject is dropped in coordinated clauses that share it (one series of actions by the same agent), re-enter that subject as the `:ARG0` of every conjunct.
  - Also re-enter the main subject as the agent of a purpose clause and of the complement of ability or control nouns.
  - Keep the ban only for noun compounds and nominal events whose participant is not in the syntax.

## 2. Habitual over-applied to single publishing acts (c_aspect: 3 of the 7 aspect errors)
- **Pattern:** "report / print / carry one article", with 了, a 一篇 count, or a "when X happened" clause, was marked `habitual`. Gold marks it `performance`.
- **Why:** §4.1 step 1 makes any publishing verb of a periodical habitual "whatever the tense".
- **Change:** use `habitual` only for a generic practice with no specific instance. A publishing or reporting verb whose object is one particular counted item, or that is tied to a specific occasion or completion marker, is `performance`.
- **Also:** a purpose event in a past narrative was given `activity`. The instruction already says it takes the main event's aspect; repeat this in §4.1 step order so it is not missed.

## 3. 为了 purpose became `have-purpose-91` (1 concept)
- In this data, gold reifies a fronted 为了 clause as `have-reason-91` (`:ARG1` main event, `:ARG2` purpose event).
- Either align §2.5 with gold, or at least state that a fronted 为了 clause with no paired marker uses the gold convention. Check this with `search_annotations` before writing the rule.

## 4. "Rely on X to achieve Y" (靠 + event): one error that spreads (~10 units)
- **Pattern:** an extra `靠-01` node was used as `:manner`. That one node caused errors in:
  - event_found, temporal and modal (one extra unit each);
  - reentrancy (an extra `:quote`);
  - peripheral roles;
  - node matching, which then swapped the two repeated names and the repeated noun (f_name_tokens 2, core args 4).
- **Change:** "achieve Y by relying on / through X" → X's event is `:reason` of Y, with no node for the relying verb. This also keeps repeated words matched to the right node; always align each occurrence of a repeated word separately (§6).

## 5. "Have the ability to V" (有能力 V) (~7 units)
- **Pattern:** the annotation used `有-01` and `能力 :mod V`. Gold uses `有-06` with `能力 :ARG1-of (identity-91 :ARG2 V-event :aspect state)`, and the V-event's `:ARG0` re-enters the subject.
- **Modal:** gold has `(author :full-affirmative identity-91)` and `(author :neutral-affirmative V)`, not `有` as the conceiver.
- **Change:** add this as an explicit construction.

## 6. Additive and escalating adverbs given nodes (4 extra entities, 3 extra peripheral roles)
- **Pattern:** 还 (also), 甚至 (even), and 也 when it links to a previous clause got `:mod` nodes. Gold drops them in a coordinated chain and in a sentence that escalates on the previous one.
- **Why:** §3.1 says "every adverb … also, 也 … gets its own node".
- **Change:** 甚至 and an additive 还/也 that only link a clause to the previous clause or sentence get no node. Keep nodes for 已经, 仍, 都/均 and other adverbs with real scope.

## 7. Temporal links inside coordinations and reported content (h_temporal 70)
- **Linking:** in a coordination of past actions, gold links each conjunct to the *previous* conjunct, not all to the first one.
- **Reported past events:** a reported event earlier than the report is `(report :before content)`. A date inside reported content gets no temporal parent of its own and does not parent the event.
- **Attributive participles:** a participle on a noun inside a conjunct (e.g. "composited photo") is `:overlap`, not `:before`. Loosen §5.1's "relative clause describing an earlier event → `:before`" rule so it applies only when anteriority is explicit (e.g. left over, inherited).
- **Evaluative statements in a past narrative:** a general evaluative statement about a subject the document narrates in the past takes `:before` DCT. Use `:depends-on` only with an explicit present marker (目前, 现在).

## 8. Quotes and modals in reported content (~5 units)
- Gold puts no `:quote` on, and gives no aspect or modal link to, the nested "serve as X" complement under a support/want-type verb in a quoted headline. Extend the "complement of a modal predicate" treatment to it.
- When the reporting subject is the conceiver, gold makes it the conceiver of *every* conjunct it performs in the same coordination, not only the speech verbs. State this in §5.2.

## 9. Invalid and wrong modifier roles (d_peripheral_entity 53, e_peripheral_labels 76)
- **`:poss`:** used 5 times, but it is not in the closed list. Add explicitly: never `:poss`.
  - content or section of a publication → `:part-of`;
  - staff of an organisation, a country's policy → `:possessor`.
- **Other modifier roles:**
  - the domain noun of a "policy / problem" noun (foreign-affairs policy, a problem about X) → `:topic`, not `:mod` or a possessor;
  - "wall of a body inside a named building": the named building is a `building` with `:place`, and the wall is `:place-of` the body, not a possessor.

## 10. Unsplit compounds, and the "如" example construction (~7 units)
- Sentence-initial 如 ("for example") → `(have-example-91 :ARG1 (implicit-predicate) :ARG2 <main event>)`.
- 全 + noun → noun `:mod 全`.
- A verb + 人 compound naming the patient (a cloned person) → `(人 :ARG1-of (verb-01 :aspect process))`. Extend the existing verb+人/者 agent rule to patients.

## 11. Concept and sense choice for verb + result complements (~5 units)
- **Pattern:** a verb + 到 verb was cut down to the bare verb, and its roles were inverted.
- **Change:** if PropBank lists the whole verb + 到/在/上 compound, use it and read its role glosses. Here `贴到-01` has `:ARG1` = the place and `:ARG2` = the thing posted.
- **Smaller issue:** gold used `-00` for two verbs whose PropBank entries exist but have empty or unclear roles. Low priority; a note that "a roleset with no usable roles → `-00`" would cover it.

## What to keep
- Headline/article titles as `publication` names with title marks, and the `identity-91` + `:part-of` treatment of an article noun.
- Classifier as `:unit`.
- The year-named `event` with no date link.
- The speaker-as-conceiver structure for reporting verbs.
- `but-91` for 虽然…但.
- Splitting verb + 者 into an agent role.
- Pronoun person and number (`c_refer` 100).
- Linking every coreference to the publication (coref 100).