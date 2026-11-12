The critique's errors that will recur fall into a few groups, and several rules that earlier reflections reported adding are missing from the current text. The edits restore them in compact form and fix the rules that are wrong.

**Rule fixes**
1. **Dropped subjects.** The ban on re-entering dropped subjects is replaced: a subject shared across coordinated clauses or a chain of actions now re-enters every conjunct. The main subject also re-enters as agent of a 为了 clause and of an ability or control complement. Dropped objects are still left out.
2. **Habitual aspect.** It now covers only generic practices. A single counted, 了-marked or occasion-bound publishing or reporting act is `performance`.
3. **Fronted 为了 clause.** It uses `have-reason-91`, to be confirmed with `search_annotations`.
4. **Adverbs.** 甚至 and additive 还/也 that only link a clause to the previous one get no node.

**Constructions added back**
5. 靠/通过 X → X is `:reason` of Y, with no node for the relying verb.
6. 有能力 V → `有-06` with an `identity-91` structure and its modal links.
7. Sentence-initial 如 → `have-example-91`.
8. 全 + noun → noun `:mod 全`.
9. V+到/在/上 compounds use the whole roleset; a roleset with no usable roles → `-00`.
10. A verb + 人 compound naming the patient → `:ARG1-of`.

**Roles**
11. Never `:poss`; the correct roles are given instead (`:part-of`, `:possessor`, `:topic`).

**Temporal**
12. Chained past conjuncts link each to the previous conjunct.
13. A reported event earlier than the report is `(report :before content)`, and a date inside reported content gets no links.
14. An attributive participle is `:before` only when anteriority is explicit; otherwise `:overlap`.
15. An evaluation in a past narrative is `:before` DCT unless it has an explicit present marker.

**Modal and quotes**
16. A reporting subject is the conceiver of all its conjoined acts.
17. The nested complement in a quoted headline gets no `:quote`, aspect or links.

**Space**
Some redundant phrases are trimmed to stay under the length limit.

```json
{"summary": "Fix dropped-subject re-entrancy rule, restrict habitual, fronted 为了 -> have-reason-91, no nodes for additive 还/也/甚至, add 靠/有能力/如/全/V到/-00/patient 人 constructions, ban :poss, temporal fixes (chained conjuncts, reported past, participles, evaluative statements), modal conjunct conceiver and headline complement; trim redundancies for space.", "edits": [
{"op": "replace", "old": "  The same holds for dropped subjects and objects of finite clauses (in coordination, contrast or a chain of clauses): do not\n  add a re-entrancy to an earlier mention; leave the argument out. This also holds for infinitive-like and\n  trailing clauses (never fill their agent with an entity of the main clause) and for possessors: a word like 旗下 is a `:mod`\n  concept, not a `:possessor` taken from elsewhere.", "new": "  But a dropped subject shared by coordinated clauses or a chain of actions of the same agent re-enters (as the role its roleset gives, usually `:ARG0`) in every conjunct; the main subject also re-enters as agent of a 为了 purpose clause and of the complement of an ability or control word. Dropped objects are left out, and a word like 旗下 is a `:mod` concept, not a `:possessor` taken from elsewhere."},
{"op": "replace", "old": "This holds whatever the tense, and also under an\n   aspectual verb (continue, stop).", "new": "Only a generic practice is habitual: one publishing/reporting act on a specific counted item (一篇), with 了, or tied to an occasion is `performance`. A purpose event in a past narrative takes the main event's aspect."},
{"op": "insert_after", "anchor": "nesting have-purpose-91 inside have-reason-91\n  when both occur.", "text": " A fronted 为了 clause with no paired marker: gold uses `have-reason-91 :ARG1 <main event> :ARG2 <purpose event>` (confirm with `search_annotations`)."},
{"op": "replace", "old": "- Every adverb that carries meaning (*already, still, also, all/both*; 已经, 仍, 也, 都, 均) gets its own node,", "new": "- Every adverb with real scope (*already, still, all/both*; 已经, 仍, 都, 均) gets its own node (甚至 and additive 还/也 that only link a clause to the previous clause or sentence get none),"},
{"op": "replace", "old": "(`performance` for a completed act,\ne.g. founding).", "new": "(`performance` for a completed act,\ne.g. founding); a verb + 人 naming the patient (a V-ed person) is `(r / 人 :ARG1-of (v / verb-01 :aspect process))`."},
{"op": "insert_after", "anchor": "- Change verbs with 由 X 改为/变为 Y: the original X is `:ARG1` and the result Y is `:ARG2`; never `:source`.", "text": "\n- Never `:poss` (not a role): content/section of a publication → `:part-of`; staff of an organisation, a country's policy → `:possessor`; the domain of a policy/problem noun → `:topic`.\n- 靠/通过 X (实现) Y: X's event is `:reason` of Y, no node for 靠/通过. 有能力 V: `(y / 有-06 :ARG0 S :ARG1 (n / 能力 :ARG1-of (i / identity-91 :ARG2 (v / V-01 :ARG0 S) :aspect state)))`, modal `(author :full-affirmative i)` `(author :neutral-affirmative v)`. Sentence-initial 如 (for example) → `(h / have-example-91 :ARG1 (implicit-predicate) :ARG2 <main event>)`. 全 + noun → noun `:mod 全`. V+到/在/上: if PropBank lists the compound, use it and read its role glosses. A roleset with no usable roles → `-00`."},
{"op": "replace", "old": "and link\n  the other events of the sentence to it:", "new": "and link\n  the other events of the sentence to it (but in a coordinated chain of past actions link each conjunct to the previous conjunct with the order relation):"},
{"op": "replace", "old": "a sentence about the current state (with currently/already, 目前/已经, or a present naming or labelling verb).", "new": "a sentence about the current state (with currently/already, 目前/已经, or a present naming or labelling verb). A general evaluation of a subject narrated in the past, with no present marker, is `:before`."},
{"op": "replace", "old": "Clauses restating or qualifying a report's content take the content's main event as parent, not the reporting verb.", "new": "Clauses restating or qualifying a report's content take the content's main event as parent, not the reporting verb. A reported event earlier than the report is `(report :before content)`; a date inside reported content gets no temporal parent and parents no event."},
{"op": "replace", "old": "- A relative-clause or participle event that describes an earlier completed event (left over, inherited, built) is before the\n  event whose argument it modifies: `(main :before rc-event)`.", "new": "- A relative-clause or participle event is `(main :before rc-event)` only when anteriority is explicit (left over, inherited); otherwise an attributive participle `:overlap`s."},
{"op": "replace", "old": "every reporting or claiming verb with that speaker as subject (each verb of a series of reports too) gets `(src :full-affirmative verb)`", "new": "every verb with that speaker as subject in the same coordination (reports and other acts) gets `(src :full-affirmative verb)`"},
{"op": "insert_after", "anchor": "`(s3w :unspecified s3g)`.", "text": " The nested complement (serve as X) of a want/support verb in a quoted headline gets no `:quote`, aspect or links."},
{"op": "delete", "old": " Many calls are expected."},
{"op": "delete", "old": " (e.g. two different kinds of stopping)"},
{"op": "delete", "old": " The place rule holds for abstract nouns too."},
{"op": "delete", "old": " (e.g. a common noun that also appears\ninside a name)"},
{"op": "delete", "old": "\n- Every attributive adjective: check its roleset before writing `:mod`."}
]}
```