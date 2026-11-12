# Review of the UMR annotation instruction: error patterns, costs and fixes

Patterns are ordered by cost, most costly first. Unit counts come from the judge's list of failed units.

## 1. Temporal links within a sentence (h_temporal F 50, about 9 units)

**What went wrong:**
- **Wrong anchor (3 wrong links).** One sentence had a relative clause with an aspectual verb over a habitual event (an "already stopped publishing" type), plus a fame predicate and its reason event. The annotator anchored on the aspectual verb. It placed the habitual event `:before` it and linked the reason event to the document creation time separately. Gold anchors on the inner habitual event: document creation time `:before` it. The aspectual verb `:overlap`s it, the fame state is `:contained` in it, and the reason event `:overlap`s it.
- **Present-situation sentences (2 units).** Two main events describe the present: a lexical "has ceased" verb with "currently", and a naming verb. The annotator used `(document-creation-time :overlap e)`. Gold uses `:depends-on`. The instruction only says gold "often" does this, and the annotator did not check.
- **Missing parents (2 units).** A process nominal under a verb got no temporal parent. The comparison event that the annotator never created (see 6) also had none.

**Why:** "Pick one anchor, usually the main eventive predicate" gives no guidance when the only real events sit inside a noun phrase. It also says nothing about aspectual verbs. "Precision counts as much as recall: leave it out" pushed the annotator to drop the nominal event.

**Change:**
- When an aspectual verb (stop, continue, begin) takes an event, make the inner event the anchor. The aspectual verb, and any states or reasons that hang on that event, link to it with `:overlap` or `:contained`.
- Link every event of the sentence to the anchor. Do not give a second event its own link to the document creation time.
- Make the present-situation rule firm. For the main event of a sentence about the current state (with "currently", "already", or a naming or labelling verb in the present), write `(document-creation-time :depends-on e)`, not `:overlap`.
- A process nominal that is an argument of a verb takes that verb as its parent, with `:overlap`.

## 2. Participants borrowed or invented: extra re-entrancies (g_reentrancy P 44; d_core_args_event and abstract; about 7 units)

**What went wrong:**
- **Relative clause with an aspectual verb.** For "N that has stopped V-ing", the annotator attached the noun as `:ARG1-of` the aspectual verb. It then also put the noun as `:ARG1` of the inner verb, giving a double edge. Gold: the noun is `:ARG1-of` the inner verb, and the inner verb is `:ARG1-of` the aspectual verb, so the noun is not filled twice.
- **Zero subject filled anyway.** A clause with a dropped subject got an `:ARG0` pointing back to the named entity. Gold leaves it unfilled.
- **Invented relations.** The annotator added `:part-of` from a "web edition" noun to the publication, which gold does not have. It also added a non-existent `:subset` role between a partitive phrase ("among them, many items") and an earlier conjunction.

**Why:** The "fill only the arguments the syntax provides" rule is stated only for compounds and nominals.

**Change:**
- Extend that rule to dropped subjects and objects of finite clauses in a coordinate or contrast structure. Do not add a re-entrancy to an earlier mention. Leave the argument out unless the guidelines' zero-pronoun rule clearly applies.
- For a relative clause headed by an aspectual verb, attach the head noun to the inner verb, and attach the aspectual verb to the inner verb with `:ARG1-of`.
- A partitive word ("among them", "of which") is a `:mod` on the noun it modifies. Use only roles from the closed list.

## 3. Negator fused into a verb (未经-type) (concept, aspect, two role labels, nested modal; about 7 units)

**What went wrong:**
- **Concept and roles.** The annotator made the concept `<negated word>-00` with `:ARG1`/`:ARG2` and aspect `state`. Gold uses the positive verb's sense from PropBank (the 经-type verb), its own `:ARG0`/`:ARG1`, and aspect `process`.
- **"N1-verification procedure" compound.** The annotator attached the event as `:mod` of the procedure noun. Gold reifies it as an identity: procedure `:ARG0-of identity-91 :ARG1 <event>`.
- **Nested event under the negated verb.** Gold gives it `partial-affirmative`. The annotator gave `full-affirmative`, although the instruction told it to check the gold data.

**Change:**
- State that for a negator fused into a verb, the concept is the un-negated verb with its PropBank sense and roles, its aspect follows the verb (`process` for 经-type verbs), and the verb is `full-negative`.
- Say explicitly that an event nested under such a verb gets `partial-affirmative` from the author.
- For "a [process noun] [procedure/method/system]" apposition-like compounds, use `identity-91` linking the head noun to the event.

## 4. Aspect (c_aspect F 79, 3 units)

**What went wrong:**
- A possession verb with "once" and an experiential marker (过) got `performance`. Gold gives `state`: possession stays a state even when it is past and bounded.
- A lexical "cease publication" verb with "already" got `state` under rule 2. Gold gives `performance`. Rule 2 applies only to an aspectual verb taking an event complement.
- The fused-negation verb got `state` (see 3).

**Change:**
- Restrict rule 2 to aspectual verbs that take an event complement.
- A lexical verb of ending (closing down, ceasing publication) with "already" is `performance`.
- Add: state verbs (have, own, belong, be) remain `state` with 过, 曾经 or a duration.

## 5. `:wiki` added (f_wiki P 0, 4 units)

Gold Chinese data has no `:wiki`. The word "optional" in the instruction invites adding it.

**Change:** For Chinese documents, write no `:wiki`.

## 6. Superlative over a verb, and "in X's history" (core_args_abstract, missing event, missing entity, temporal and modal; about 6 units)

**What went wrong:**
- **Superlative.** In "most-[verb] [noun]" (a "richest in creativity" type), the annotator dropped the verb. It made the noun the `:ARG2` of `have-degree-91` and added an `:ARG5`. Gold: `:ARG2 (verb-01 :ARG1 noun :aspect state)`.
- **"In X's history".** Gold has `:temporal (上 :op1 历史)`, with the country as `:place` of the history noun. The annotator used `:mod`, although the place rule exists.
- **Modal link.** The annotator gave the abstract `have-degree-91` a modal link. Gold gives it none; the verb inside it gets the link.

**Change:**
- When the degree word modifies a verb, that verb is the `:ARG2` of `have-degree-91`, as an event with its own aspect, temporal parent and modal parent.
- A locative postposition phrase over a time-span noun ("in history", 历史上) is `:temporal` of the head noun, with the postposition as the concept and `:op1` the noun.
- Do not give `have-degree-91` a modal link.
- Make the place rule apply to every noun, abstract nouns included.

## 7. Smaller role and label choices (about 6 units)

- **Belong-type verb in a relative clause:** the annotator inverted the roles. In gold the owned thing is `:ARG0` and the owner `:ARG1`. Tell the annotator to read the roleset rather than assume possessum = `:ARG1`.
- **Channel noun ("TV programme"):** the annotator used `:mod`, but it should be `:medium`. The rule exists but was not applied; repeat it in the checklist.
- **"Once" / "formerly" (曾经):** gold uses `:temporal`, not `:mod`. Add it to the list of time adverbs, separate from scope adverbs like "also" and "already".
- **Entity type:** a periodical or tabloid name should be `newspaper`, not `publication` (2 units).
- **Coordination with mixed separators:** when the first two items are joined without the list comma (、) and the rest with it, gold nests the first pair as its own `and` (1 unit).
- **Coreference of a country name used as a modifier:** the annotator linked it across sentences, but gold does not link it (2 coref precision units). Coreference only the discourse entities that the text tracks.

## What the instruction got right and should keep

These checks were at 100:
- event senses;
- polarity and other attributes;
- name tokens, with the title marks as their own `:op`s;
- numeral + classifier `:unit`;
- document format.

These were also handled well:
- `identity-91` for "A is a B";
- the "famous for" rule (`:ARG1-of` the fame predicate, with `:reason` inside the noun);
- `habitual` for a publication's regular output;
- `but-91` with `:ARG1`/`:ARG2`;
- `:reason` for 由于 phrases;
- re-entrancy of a shared modifier on each conjunct;
- `:part-of` for an edition of a work;
- `performance` for naming verbs;
- `full-negative` on the negated verb;
- the coreference chain of the main entity.

Keep these rules as they are.