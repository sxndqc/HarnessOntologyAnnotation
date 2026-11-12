**Summary of changes**

These edits target the critique's recurring problems. Space is freed by cutting text that repeats other sections.

1. **Coreference (largest cost).**
   - Coreference is limited to tracked entities. Generic or kind nouns, members of example lists, and names given only as examples are never linked.
   - A repeated name inside a slogan, gloss or parenthesis of the same sentence re-uses the existing variable instead of getting a new node.
2. **Modal links for reported content.**
   - Each predicate in the content gets both the author and the speaker as modal parents.
   - Event nominals inside the content get the author only.
   - A passive reporting verb with no speaker uses the content's subject as conceiver, never the reporting event.
3. **Temporal links.**
   - A date that opens a but-91 or contrast sentence attaches to both clauses.
   - A "still / continue" clause `:overlap`s the first clause, never `:after`.
   - Clauses that restate or qualify a report's content hang on the content's main event, not on the reporting verb.
4. **Superlative with no head noun.**
   - The pattern is `implicit-argument` with the classifier as `:unit`, under `have-degree-91` with `:ARG5` for the partitive word.
   - The general ban on `:ARG5` is lifted, and the partitive-as-`:mod` rule now has an exception for this case.
5. **Appearance verbs.** The gold convention is stated: the appearing entity is `:ARG0` and the location is `:ARG1`.
6. **Aspect.**
   - State verbs stay `state` under 继续/仍.
   - An activity noun that is the complement of a judging verb is `activity`.
7. **Trimmed for space:**
   - the intro sentence about scoring;
   - the opening line of section 1;
   - the duplicate `:degree` bullet;
   - the AMR type list;
   - the verbose "Then every event" bullet;
   - a duplicate checklist line.

```json
{"summary": "Coref restricted (no generic/example-list nouns; repeated name in slogan/parenthesis = re-entrancy); reported-content modal: author+speaker parents, nominals author-only, passive 被指 conceiver = content subject; temporal: date opening but-91 on both clauses, still/continue overlap, restating clauses hang on content main event; superlative with dropped head (implicit-argument, ARG5 partitive); 出现-type role convention; aspect fixes; trimmed redundant text for space.", "edits": [
{"op": "delete", "old": " It is compared node by\nnode and relation by relation with an expert gold annotation made by these guidelines; every concept, sense, role,\nattribute and relation counts."},
{"op": "delete", "old": "A UMR has one graph per sentence (PENMAN, adapted from AMR) and document-level temporal, modal and coreference relations.\n\n"},
{"op": "delete", "old": " Types as in AMR (`country`, `city`, `organization`, `company`, `planet`, `spaceship`, ...)."},
{"op": "delete", "old": "- `:degree` for intensifiers and downtoners (*very, too, most*; 很, 非常, 太, 最) as a concept:\n  `:degree (v / very)`.\n"},
{"op": "delete", "old": "- No borrowed participants: every re-entrancy is licensed by the syntax of that clause."},
{"op": "delete", "old": " (the scorers move it to the document level)"},
{"op": "replace", "old": "- Then every event: (1) a time expression of its clause, if there is one (`(s1t :overlap s1e)`); else\n  (2) an event before it that is a clear reference time (`(s2c :before s3a)`); else (3)\n  `document-creation-time` (`(document-creation-time :before s3d)` for a past event, `:overlap` for a\n  present state, `:after` for a future event). Chinese has no tense: decide past, present or future from\n  context, 了, 过, 将, 会.", "new": "- Then every event: (1) a time expression of its clause; else (2) a clear earlier reference event; else (3) `document-creation-time` (`:before` past, `:overlap` present state, `:after` future; Chinese: decide from context, 了, 过, 将, 会)."},
{"op": "replace", "old": "- Coreference only the discourse entities the text tracks (participants, the topic entity).", "new": "- Coreference only the discourse entities the text tracks (participants, the topic entity); never generic or kind nouns, example-list members, or a name given only as an example, even if the word recurs."},
{"op": "replace", "old": "An overt repeated name or noun (short name, bare head noun) gets its own node plus a `:same-entity` triple.", "new": "An overt repeated name or noun (short name, bare head noun) gets its own node plus a `:same-entity` triple; but inside a slogan, gloss or parenthesis of that sentence it re-uses the variable."},
{"op": "replace", "old": "- Reported speech or thought: the author is certain of the speaker, the speaker of the content:\n  `(author :full-affirmative s9p)` `(s9p :full-affirmative s9s3)`, where `s9p` is the speaker (a person\n  node, or an event used as conceiver). Every event of the reported content, including an appended slogan or quotation and later clauses still reporting it, takes the speaker as modal parent; the content's top node carries `:quote <saying verb>`.", "new": "- Reported speech or thought: `(author :full-affirmative s9p)` for the speaker; every predicate of the content (also an appended slogan and later clauses about that source's reports) gets both `(author :full-affirmative e)` and `(s9p :full-affirmative e)`; event nominals that are arguments inside the content get author only. The content's top node carries `:quote <saying verb>`. A passive reporting verb with no speaker (被指): the conceiver is the content's subject node, with `(author :full-affirmative <subject>)`; never the reporting event."},
{"op": "replace", "old": "A time expression scoping over both clauses of a but-91/contrast attaches to both clause events.", "new": "A time expression over (or opening) a but-91/contrast attaches to both clause events; a still/continue second clause `:overlap`s the first, never `:after`."},
{"op": "replace", "old": "- An event in a complement clause takes its matrix event as parent.", "new": "- An event in a complement clause takes its matrix event as parent. Clauses restating or qualifying a report's content take the content's main event as parent, not the reporting verb."},
{"op": "replace", "old": "Do not use `:ARG5` and give `have-degree-91` itself no modal link.", "new": "Give `have-degree-91` itself no modal link. With no head noun (其中 最 Adj + classifier): `(i / implicit-argument :unit <classifier> :ARG1-of (h / have-degree-91 :ARG1 (a / Adj) :ARG2 (m / 最) :ARG5 (q / 其中)))`."},
{"op": "replace", "old": "a partitive word (其中, *among them, of which*) is a\n  `:mod` on the noun it modifies.", "new": "a partitive word (其中, *among them, of which*) is a\n  `:mod` on the noun it modifies, unless a superlative follows (then `:ARG5`, see have-degree-91)."},
{"op": "replace", "old": "Check the roleset for a location argument (出现-type) before using `:place`.", "new": "Appearance verbs (出现-type): the appearing entity is `:ARG0`, the 在 N 中 location `:ARG1` (gold convention)."},
{"op": "replace", "old": "stay `state` even with 过, 曾经 or a duration.", "new": "stay `state` even with 过, 曾经, a duration, or under 继续/仍."},
{"op": "replace", "old": "3. Is the event a process noun, including the object of a light or experiential verb (经, 经过, 进行, undergo)? → `process`.", "new": "3. Is the event a process noun, including the object of a light or experiential verb (经, 经过, 进行, undergo)? → `process` (but an activity noun complementing a judging verb, 算/是-type, is `activity`)."}
]}
```