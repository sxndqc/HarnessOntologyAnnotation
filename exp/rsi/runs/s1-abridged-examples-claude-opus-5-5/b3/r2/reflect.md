The batch's main losses came from pronouns that stand for organisations, the 其中最…可算是 construction, names inside appositions and their shortened repeats, and the modal structure of reported content. I fixed those and the smaller recurring problems. To stay under the 30000-character limit, I cut space elsewhere first:

- **Space made:** I shortened the preamble and the abridgement note, removed the checklist (it repeated the rules) and the "finer aspect values" note, and dropped four examples that only restated their rules.

**Changes:**

1. **Pronouns for organisations (2.4):** 他们/它/其 that refers to an organisation or publication named in the same sentence reuses that entity's variable. A possessive 他们的 before an event noun adds no `:ARG0`. In a later sentence the pronoun is its own node, and its coreference goes to the named entity.
2. **其中最…可算是 (3, 5.1, 5.2, 2.1):**
   - 算是-01 roles: `:ARG0` is the thing described, `:ARG1` is what it counts as.
   - 其中最 + adjective with no head noun becomes `implicit-argument` with `have-degree-91`, and the classifier is `:unit`.
   - 可/能/可以 before a predicate makes it `neutral-affirmative`.
   - A summing-up sentence in a past narrative is `document-creation-time :before`.
   - Event nominals keep their PropBank sense (活动-01).
   - No `:subset-of` link from a 其中 phrase.
3. **Appositions and shortened repeats (3, 5.3):**
   - A role noun before an organisation name becomes the entity node plus `identity-91`.
   - A shortened repeat of a name (周报) is its own node, linked by an in-sentence `:same-entity`. Re-entrancy is only for exact repeats.
   - A sentence-initial date shared by both clauses of 不过/但 goes on both main events.
4. **Reported content (5.2, 2.5, 4.1):**
   - The top content node (the one with `:quote`) gets both the author triple and the conceiver triple.
   - The conceiver of 被指 is the whole subject node (the `and` node when coordinated).
   - A quoted slogan's `identity-91` takes `:aspect state`, and its inner event carries `:quote`.
   - 宣称 as a past claim is `performance`.
5. **Characters in a 如…等 list:** each is `individual-person` with the full written name, the descriptor included, and is not coreferred with the narrative mention.
6. **Adverbs:** no node for 就, for 还 after 后来, for 仍 beside 继续, or for 都 in 都以…为目的.
7. **出现's location:** 在 N 中 is `(中 :op1 N)` as 出现's `:ARG1`.

```json
{"summary": "Freed space (shorter preamble/abridgement note, removed checklist and redundant examples), then fixed: org/publication pronouns reuse the entity variable and corefer to the named entity; 算是-01 roles, implicit-argument for 其中最, 可 = neutral-affirmative, summary sentences DCT :before, event nominal senses, no subset-of from 其中; role-noun + org name apposition, shortened name repeat as own node with in-sentence same-entity, shared sentence-initial date; conceiver triples on the :quote top node, 被指 conceiver = whole subject, slogan identity-91 state + :quote, 宣称 performance; list characters as individual-person with full name; narrower adverb nodes; 出现 :ARG1. Added examples.", "edits": [
{"op": "replace", "old": "**Make the annotation as correct as you can.** It is compared, node by node and relation by relation,\nwith an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value\nand document-level relation counts. Take the time this needs:\n\n- Read the guidelines below carefully before you start, and go back to them for every decision you are\n  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named\n  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.\n- Follow the examples: when a sentence has a construction an example shows, annotate it the way the\n  example does.\n- Before you go on to the next sentence, check the graph against the guidelines once more: every word\n  that carries meaning has its concept, every event its aspect, every role the right direction; and at\n  the end check that the document-level relations cover every event and entity the guidelines ask for.", "new": "**Make the annotation as correct as you can**: it is compared node by node and relation by relation with an expert gold annotation. Check every decision against the guidelines, follow the examples, and check each graph (concepts, aspect, role direction, document-level coverage) before moving on."},
{"op": "replace", "old": "A short version of the UMR 0.9 specification (`umr_guidelines.md` in this folder, umr4nlp/umr-guidelines),\nfor annotating Chinese and English at Stage 1 (numbered PropBank roles). Where the full guideline uses the older short names (`AUTH`, `DCT`,\n`FullAff`, `:modstr`, `:ref-person`, `Performance`), this version uses the names of the UMR release data\n(`author`, `document-creation-time`, `full-affirmative`, `:modal-strength`, `:refer-person`, `performance`).", "new": "UMR 0.9 abridged, for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data."},
{"op": "replace", "old": "## 7. Checklist\n\n- Parentheses balanced; every variable defined once; all variables start with `s<N>`.\n- Every event has `:aspect`; negated events have `:polarity -`.\n- Every event and time expression has a temporal parent; every event has a modal parent (except the inner verb of a V+量 compound, which has only a temporal parent).\n- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.", "new": ""},
{"op": "delete", "old": "Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them\nonly when they are clear."},
{"op": "replace", "old": "event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events;", "new": "event nominals with process meaning (*the meeting*, *the attack*, 会议, 比赛) — annotate them as events, with their PropBank sense (活动-01);"},
{"op": "insert_after", "anchor": "linked by coreference.", "text": " A 他们/它/其 standing for an organization or publication named in the same sentence is no new node: reuse its variable; a possessive 他们的 before an event noun adds no `:ARG0`. In a later sentence the pronoun is its own node, coreferred to the named entity, not to an earlier pronoun."},
{"op": "replace", "old": "已经, 都, 也, 仍, 还 and 其中 → `:mod (<word>)`;", "new": "已经, 都, 也, 甚至, 还 and 其中 → `:mod (<word>)`, but no node for 就, for 还 after 后来, for 仍 beside 继续, or for 都 in 都以…为目的;"},
{"op": "insert_after", "anchor": "`:ARG1-of (identity-91 :ARG2 (<noun> :mod …))`.", "text": " Likewise a role noun before an organization name (母公司美国媒体公司): `company` with the name `:ARG1-of (identity-91 :ARG2 (公司 :mod (母)))`."},
{"op": "replace", "old": "and refer to it at later mentions in the same sentence by its bare variable (`:possessor s7n`).", "new": "and refer to it at later exact repeats in the same sentence by its bare variable (`:possessor s7n`). A shortened repeat (周报 after 《世界新闻周报》) is its own node `(周报)` with an in-sentence `:same-entity` triple. A sentence-initial date shared by both clauses of 不过/但 is `:temporal` of both main events."},
{"op": "replace", "old": "Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.", "new": "Within one sentence, coreference is a re-entrancy (one variable), except a shortened name repeat (see 3)."},
{"op": "replace", "old": "Never put a `:subset-of` triple inside one sentence.", "new": "Never put a `:subset-of` triple inside one sentence or from a 其中 phrase."},
{"op": "replace", "old": "Look up the whole compound first (算是-01, 称为-01).", "new": "Look up the whole compound first (称为-01; 算是-01: `:ARG0` thing described, `:ARG1` what it counts as). 其中最 + Adj with no head noun → `implicit-argument :ARG1-of (have-degree-91 :ARG1 (Adj) :ARG2 (最) :ARG5 (其中))`, classifier (宗) as `:unit`."},
{"op": "replace", "old": "A common noun directly before a name (外星人 P'Lod) is no apposition: `(外星人 :name (name …))`, no identity-91.", "new": "A common noun directly before a name (外星人 P'Lod) in running text is no apposition: `(外星人 :name (name …))`, no identity-91; in a 如 A、B 等 list each character is `individual-person` named with all its written words, descriptor included, and is not coreferred with the narrative mention."},
{"op": "replace", "old": "在 N 中 → `(中 :op1 N)`;", "new": "在 N 中 → `(中 :op1 N)` (出现 `:ARG1`);"},
{"op": "replace", "old": "is anchored to `document-creation-time` itself.", "new": "is `(document-creation-time :before X)` in a past narrative."},
{"op": "replace", "old": "with no written speaker (被指) use the passive subject.", "new": "with no written speaker (被指) use the whole subject node of the first content event (the `and` if coordinated). The top content node (with `:quote`, even an abstract predicate) gets both `author` and conceiver triples."},
{"op": "replace", "old": "joined to its clause by `and`.", "new": "joined to its clause by `and`; a quoted slogan's identity-91 takes `:aspect state` and its inner event `:quote` that identity-91."},
{"op": "insert_after", "anchor": "- Every event the author asserts: `(author :full-affirmative s1e)`.", "text": "\n- 可/能/可以 before a predicate (可算是) make it `neutral-affirmative` from the author."},
{"op": "replace", "old": "Passive naming (被称为) is `performance`.", "new": "Passive naming (被称为) and a past claim (宣称) are `performance`."},
{"op": "delete", "old": "- Name (2.2): 美国…小报 → `(小报 :place (country :name (name :op1 \"美国\")))`, with no `:wiki`."},
{"op": "delete", "old": "- Date (5.1): 1980年代…改为 → `(document-creation-time :before s9d) (s9d :overlap s9x)`, `(date-entity :era 1980)`."},
{"op": "delete", "old": "- Coref (5.3): 发行 (print, stopped) vs 发行 (online edition, continuing) → no `:same-event`."},
{"op": "delete", "old": "- Adverb (3): 已经停止 → `(停止-01 :mod (已经) :aspect state)`; 曾经 → `:temporal (曾经)`."},
{"op": "replace", "old": "`(author :full-affirmative 报导) (s12n :full-affirmative 报导)`.", "new": "`(author :full-affirmative have-mod-91) (s12n :full-affirmative have-mod-91)`, likewise each content 报导; slogan → `(identity-91 :aspect state)`."},
{"op": "replace", "old": "conceiver = passive subject.", "new": "conceiver = the `and` subject."},
{"op": "append", "text": "- Pronoun (2.4): 他们的报导…他们的标语 → `(报导-01 :aspect habitual)`, `(标语 :possessor s12n)`; next sentence 他们 → `(s12n :same-entity s13p)`.\n- 算是 (3): 其中最大宗可算是…活动 → `(算是-01 :ARG0 (implicit-argument :ARG1-of (have-degree-91 :ARG1 (大) :ARG2 (最) :ARG5 (其中)) :unit (宗)) :ARG1 (活动-01 …))`, `(author :neutral-affirmative 算是) (document-creation-time :before 算是)`.\n- Apposition (3): 母公司美国媒体公司 → `(company :name … :ARG1-of (identity-91 :ARG2 (公司 :mod (母))))`; later 周报的网络版 → `(网络版 :part-of (s11x5 / 周报))` + `(s11n2 :same-entity s11x5)`.\n- List names (3): 如蝙蝠男孩、外星人P'Lod等 → `(individual-person :name (name :op1 \"蝙蝠\" :op2 \"男孩\"))`, `(individual-person :name (name :op1 \"外星人\" :op2 \"P\" :op3 \"'\" :op4 \"Lod\"))`."}
]}
```