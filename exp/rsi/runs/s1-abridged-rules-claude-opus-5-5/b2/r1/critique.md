Below are the error patterns, ordered by how much they cost. For each one: what goes wrong, which checks it hits, why it happens given the instruction, and the change to make.

## 1. Clause-linking connectives kept as plain `:cause` / `:purpose` edges instead of abstract predicates (most costly)
**Cost:** a_event_found (have-reason-91 missing), a_event_concept (have-purpose-91), d_core_args_abstract (5 units wrong), d_peripheral_event (3 extra), i_modal (have-reason-91 missing), h_temporal (1 extra). That is about 12 units, all in one long sentence.

**Why:** Section 2.5 says *because* → `:cause`, *in order to* → `:purpose`. Gold annotations of Chinese reify a causal connective pair (因为 … 于是 / 由于 / 所以) and a purpose clause (为 … / 为了 …) when it links whole clauses:
- `(h / have-reason-91 :ARG1 result :ARG2 cause :aspect state)`
- `(h2 / have-purpose-91 :ARG1 main-event :ARG2 purpose-event :aspect state)`

The reified node is then the root, or sits above the main event. Other gold documents do the same (I checked).

**Change:** Rewrite 2.5 for Chinese: "When a reason or purpose connective links two full clauses, use `have-reason-91` (`:ARG1` effect, `:ARG2` cause) or `have-purpose-91` (`:ARG1` main event, `:ARG2` purpose). These carry `:aspect state` and `(author :full-affirmative …)`, but get no temporal parent. Keep `:cause` / `:purpose` / `:reason` only for phrasal modifiers." Add this case to the identity-91 / have-degree-91 exceptions in 5.1.

## 2. Measure compounds (event + 量, rate or amount nouns) and numbers flattened
**Cost:** a_event_concept, a_entity_concept, a_event_found (have-quant-91), c_other_attributes (`:quant` vs `:ARG2`), d_core_args_event, d_peripheral, e_core_labels, h_temporal (2 missing). That is about 25 units over two sentences.

**Why:** Nothing in the instruction covers a noun formed from a verb plus a measure morpheme. The annotator made it one entity, attached the owner as `:possessor`, and put the number as `:quant` on a `thing`.

Gold handles this case as follows:
- It splits the compound: `(q / 量 :quant-of (e / V-01 :ARG1 owner))`. The verb is a real event, so it gets aspect, a temporal link (`:overlap` with the main verb) and a modal link.
- It gives the amount reached as `(q :ARG1-of (h / have-quant-91 :ARG2 N :unit (u / 份)))` on the measured noun, not as a separate `thing` argument.

**Change:**
- Add a rule to 2.1/2.6: "A Chinese noun made of a verb + 量 / 率 / 额 (quantity, rate or amount of V-ing) is split. The measure morpheme is the head, with `:quant-of` the verb event; the verb's own arguments attach to the verb."
- Add a rule to 2.2: "A number reached, fallen to or amounting to (达到 N, 跌至 N, 为 N) goes on the measured noun as `have-quant-91 :ARG2 N :unit …`. Do not create a `thing :quant N`."

## 3. A verb + directional/result complement treated as one predicate
**Cost:** a_event_concept, plus the wrong core-role cascade above.

**Why:** Step 1 of the role-numbering procedure says "look up the whole segmented token". When that token is verb + 至 / 到 / 为 and has no frame, the annotator kept the whole token anyway. Gold uses the bare verb's frame, and the endpoint fills that frame's end-point role (or comes through have-quant-91).

**Change:** "If a verb + complement token (V至, V到, V为, V成) has no frame, use the bare verb's frame. Never use a concept whose word is not a PropBank lemma."

## 4. Chinese role numbers taken from English habit
**Cost:** e_core_labels and d_core_args_event, about 6 units.

**Why:** The annotator gave the theme of 成, 达到 and 跌 as `:ARG1` and the result as `:ARG2`. In these Chinese frames, `:ARG0` is the theme and `:ARG1` is the result or point reached (I checked PropBank). The instruction already warns about this, but only for intransitive and belonging verbs, and the warning was not followed.

**Change:** Widen the warning. "In Chinese PropBank, the theme of change, become, reach and fall verbs is usually `:ARG0`, and the result or end point is `:ARG1`. Copy the numbers from the roleset's role list every time."

## 5. The wrong head chosen in a 的-phrase or appositive; inferred re-entrancies
**Cost:** a_entity_concept, d_core_args, d_peripheral_entity, g_reentrancy (4 extra; precision 20), c_other_attributes. About 15 units.

What went wrong:
- In "X版面的《Name》" and "《Name》 changes from X版面 to Y版面", gold makes the common noun (版面) the head, with the publication as `:part-of`. The annotator made the name the head and moved the noun to `:mod` / `:source`.
- An appositive "its 旗下 tabloid 《Name》" is `Name :ARG1-of (identity-91 :ARG2 小报 :mod 旗下 :mod 八卦)`. The annotator dropped it and inferred a `:possessor` re-entrancy.
- The annotator re-entered the subject as the purpose verb's `:ARG0` and as the relative clause's `:ARG0`. Gold has neither.

**Why:** The instruction's rule "a subject shared through a … purpose/means frame counts as expressed: re-enter it" invites these extra re-entrancies.

**Change:**
- Narrow that rule to frames where the subject is grammatically shared (以…而, *try to*). Say explicitly: "do not re-enter into 为-purpose clauses or relative clauses."
- Add: "In N1 的 N2 and in V-from-A-to-B, the grammatical head noun is the concept; a publication or organization name modifying it is `:part-of` / `:possessor`."
- Add: "An appositive descriptor before a name is `identity-91`."
- Add: "Do not turn words like 旗下 into a `:possessor` edge; keep them as a `:mod` node."

## 6. Agent nouns, named persons and name tokens
**Cost:** a_entity_concept (2), a_event_found (1), f_name_tokens, temporal and modal links for the missing event (2).

**What gold does:**
- A compound agent noun (V-er: 创始人, 发起人) is `(人 :ARG0-of (V-00/01 :aspect performance))`, under `have-org-role-91 :ARG3`.
- A named human is `individual-person`.
- The middle dot `·` in a transliterated foreign name is its own `:op`.

**Change:** Add these three rules to 2.2 and 2.3. The instruction currently says `person`, which is wrong for named individuals.

## 7. Temporal rules that are wrong in the instruction
**Cost:** h_temporal, about 12 of roughly 17 units (F 19).

Five parts of the instruction contradict gold:
- **Absolute dates:** gold puts a past absolute date as `(document-creation-time :before date)`, and the event is `(date :overlap event)`. The instruction prescribes `root :depends-on` and `:contained`. Fix 5.1 to the gold form.
- **Purpose clauses:** gold puts them `:overlap` the main event. The instruction says `:after`. Change it.
- **Cause and earlier relative clauses:** a cause clause and a relative clause describing an earlier event ("left over", "previously …") are `:before` their parent, even when the cause clause is marked future (将) relative to its own time. Add this.
- **The 已经 / 成了 "result state" rule** (`document-creation-time :depends-on e`) led the annotator to detach a narrative "became" event. Gold anchors it to the previous sentence's event with `:overlap`. Restrict the depends-on rule to naming and evaluation passives. Say that a narrative change continuing an earlier sentence's story takes that event as its reference time.
- **Decade expressions:** gold writes a decade (X年代) as `:era`, not `:decade`. This is a minor fix to the date-entity line.

## 8. Aspect
**Cost:** 3 units.

Three kinds of event got the wrong value:
- A purpose verb that names an ongoing use is `activity`, not `process`.
- A relative-clause verb giving what something is for or contains is `process`, not `habitual`.
- A nominalized habitual practice that is the subject of "became a feature" is `habitual`, and its manner word is `:manner`, not `:mod`.

**Change:** Add "purpose verb → activity" and "a manner or property word on an event nominal is `:manner`."

## 9. Modal and coref details
**Cost:** i_modal 1 unit, j_coref 2 units.

- **Modal:** a purpose clause whose event is in fact realized is `(author :full-affirmative)`, not `unspecified` under the main event.
- **Coref:** do not link two different events with `:same-event` (here a founding of the publication and the founding act in the next sentence). Allow `:same-event` only when it is the very same event mentioned again.

## What to keep
These parts of the instruction produced correct results and should stay:
- named-entity typing (`newspaper`, title-bracket ops);
- senses (b_event_sense 100%);
- polarity;
- the entity coreference chains (recall 100%);
- doc format;
- the `:aspect performance` default for completed events;
- the 已经 `:mod` rule;
- the date-entity structure;
- the basic modal skeleton (`root :modal author`, full-negative for negated relative clauses).