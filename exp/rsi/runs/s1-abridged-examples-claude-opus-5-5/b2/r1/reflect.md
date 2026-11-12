The critique's largest losses come from rules that will recur on other Chinese documents. I fix those and keep everything that worked.

1. **Wrong temporal rule for absolute dates.** The old rule (`root :depends-on`, then `:contained`) is replaced: a past date is now `(document-creation-time :before date)`, and the event of its clause is `(date :overlap event)`. Other temporal fixes:
   - A reason comes before its result.
   - A purpose overlaps its main event; this replaces the old `:after` rule.
   - A continuing sentence hangs from the previous sentence's main event.
   - Resultative participles come before the event that uses them.
2. **Clause-linking predicates.** Paired connectives (因为/为 … 于是) now root in `have-reason-91` / `have-purpose-91`. A sentence-initial 不过 is not annotated.
3. **Noun-phrase structure.** New rules cover:
   - apposition of a common noun and a 《name》 (the name is the head, plus `identity-91`), with 旗下 as `:mod`;
   - an object 版面 that is `:part-of` the named paper;
   - 由 X 改为 Y (X is `:ARG1`, Y is `:ARG2`);
   - role nouns like 创始人;
   - 该刊 keeping its own word as the concept;
   - the middle dot · in names;
   - V+量 measure nouns with `have-quant-91`;
   - 年代 as `:era`.
4. **Arguments and roles.**
   - The rule against inventing arguments is made stronger.
   - Role numbers come from Chinese PropBank (成/达到/跌: the theme is `:ARG0`).
   - Manner adjectives on event nouns are `:manner`, and 印刷 is `habitual`.
5. **Modal and coreference.**
   - A realized purpose is `author :full-affirmative`.
   - Events expressed by different verbs are not coreferred.
   - Examples are added for each fix.

```json
{"summary": "Fix date anchoring (DCT :before date, date :overlap event), reason/purpose temporal order, cross-sentence anchoring; add have-reason-91/have-purpose-91 for paired clause connectives; apposition with identity-91, 由X改为Y roles, part-of objects, role nouns, 量 measure nouns with have-quant-91, middle dot in names, :era for 年代, 该刊; stronger no-invented-arguments rule; Chinese PropBank role numbering for 成/达到/跌; :manner + habitual for 印刷; realized purpose full-affirmative; no coref across different verbs; sentence-initial 不过 not annotated; examples.", "edits": [
{"op": "replace", "old": "an absolute date (*1998*) depends on `root`;", "new": "a past absolute date (*1998*, 1980年代) is `(document-creation-time :before <date>)` (never `root :depends-on`);"},
{"op": "replace", "old": "(1) a time expression of its clause, if there is one (`(s1t :contained s1e)`);", "new": "(1) a time expression of its clause, if there is one (`(s1t :overlap s1e)`, not `:contained`);"},
{"op": "replace", "old": "- An event in a complement clause takes its matrix event as parent; a purpose is `:after` its main event.", "new": "- An event in a complement clause takes its matrix event as parent. A purpose event is `:overlap` its main event (`(创立 :overlap 运用)`). A reason comes before its result: `(<reason> :before <result>)` (因为 X，于是 Z → `(X :before Z)`). A resultative participle (遗留下来) comes before the event that uses it (`(运用 :before 遗留)`).\n- A sentence with no time expression that continues the previous sentence's episode hangs its main event from that sentence's main event (`(s7x :overlap s8x)`), not from `document-creation-time`."},
{"op": "insert_after", "anchor": "Chinese names are split into words, not characters: 欧洲议会 → `:op1 \"欧洲\" :op2 \"议会\"`.", "text": " A middle dot in a transliterated name is its own `:opN` (格内洛索·波普 → `:op1 \"格内洛索\" :op2 \"·\" :op3 \"波普\"`)."},
{"op": "insert_after", "anchor": "a classifier is kept as the unit too, including 个, 份, 款, 本 (一份小报 → `小报 :quant 1 :unit (份)`).", "text": "\nA V+量 compound (发行量, 产量, 销量) is `(量 :quant-of (V-01 :ARG1 <whose>))`; the inner V-01 is an event (aspect, temporal parent overlapping the governing verb, modal parent). The amount it reaches is `量 :ARG1-of (have-quant-91 :ARG2 <number> :unit (<classifier>))`, not a separate `:ARG` of 达到/跌 and not `thing :quant`. A decade (1980年代) is `date-entity :era 1980`."},
{"op": "replace", "old": "*but* (但是, 却, 然而, 不过, 可是) `but-91`;", "new": "*but* (但是, 却, 然而, 不过, 可是) `but-91` when it links two clauses of the same sentence; a sentence-initial 不过/但是 that links to the previous sentence is not annotated (the root is the clause's verb);"},
{"op": "insert_after", "anchor": "*although* (虽然, 尽管) → `:concession`.", "text": "\n- When whole clauses are linked by paired connectives (因为 X，于是/所以 Z; 为 Y，于是 …), use abstract predicates as the root: `have-reason-91` (`:ARG1` result, `:ARG2` reason) and `have-purpose-91` (`:ARG1` main event, `:ARG2` purpose), nested when both occur: `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用) :ARG2 改为)`. Each takes `:aspect state`, no temporal parent, and `(author :full-affirmative …)`. 以…而 inside a clause stays `:reason`."},
{"op": "replace", "old": "- Do not add arguments (agents, possessors) that the text does not express or clearly imply.", "new": "- Do not add arguments (agents, possessors, organizations) that the text does not express. Never re-use a participant from elsewhere in the sentence as an unexpressed agent or possessor: every re-entrancy needs a pronoun or an overt word. 旗下 is `:mod (旗下)`, not a possessor."},
{"op": "insert_after", "anchor": "Do not add a coordinating `and`.", "text": "\n- Apposition `<common noun> + 《name》` (八卦小报《国家询问报》): the named entity is the head, and the common noun hangs from it by `:ARG1-of (identity-91 :ARG2 (<noun> :mod …))`.\n- In V 了 Adj-N 的《Name》 the object is the head noun with `:part-of` the named entity (创立了黑白版面的《…》 → `创立 :ARG1 (版面 :mod (黑白) :part-of (newspaper …))`); a relative clause before it (容纳…的) modifies that noun.\n- 由 X 改为/变为 Y: X is `:ARG1`, Y is `:ARG2`; no `:source`.\n- A role noun built from a verb (创始人) is `(person :ARG1-of (have-org-role-91 :ARG3 (人 :ARG0-of (创始-00 :aspect performance))))`, with no `:ARG2` unless the organization is written with it.\n- Take role numbers from the Chinese roleset, not from the English equivalent: for change-of-state and amount verbs (成-01, 达到-01, 跌-01, 增至) the theme is `:ARG0` (成-01 `:ARG0` theme, `:ARG1` result). Look it up.\n- An adjective saying how an event noun's action is done is `:manner` (黑白印刷 → `印刷 :manner (黑白)`).\n- A demonstrative + abbreviated noun keeps the word as its concept (该刊 → `(刊 :mod (该))`, not `newspaper`)."},
{"op": "replace", "old": "Aspect cues: recurring activities of a publication or institution (发行, 报导, 综合) are `habitual`", "new": "Aspect cues: recurring activities of a publication or institution (发行, 报导, 综合, 印刷) are `habitual`"},
{"op": "insert_after", "anchor": "A conceiver that is not in the text is `null-conceiver`.", "text": " A purpose the text presents as realized (founded to hold such articles, and it did) is `(author :full-affirmative <purpose>)`, not `unspecified` under the main event."},
{"op": "insert_after", "anchor": "Never put a `:subset-of` triple inside one sentence.", "text": " Do not link events expressed by different verbs (创刊 vs 创立) unless the text makes them clearly identical."},
{"op": "append", "text": "\n- Date (5.1): 1980年代…改为 → `(document-creation-time :before s9d) (s9d :overlap s9x)`, `(date-entity :era 1980)`.\n- Clause links (2.5): 因为 X，为 Y，于是 Z → `(have-reason-91 :ARG1 (have-purpose-91 :ARG1 创立 :ARG2 运用 :aspect state) :ARG2 改为 :aspect state)`; temporal `(创立 :overlap 运用) (创立 :before 改为)`.\n- Apposition (3): 旗下的八卦小报《国家询问报》 → `(newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 :mod (旗下) :mod (八卦))))`.\n- 改为 (3): 由黑白版面改为彩色版面 → `改为 :ARG1 (版面 :mod (黑白)) :ARG2 (版面 :mod (彩色))`.\n- Measure noun (2.2): 发行量达到120万份 → `(达到-01 :ARG0 (量 :quant-of (发行-01 :ARG1 …) :ARG1-of (have-quant-91 :ARG2 1200000 :unit (份))) :aspect performance)`, `(达到 :overlap 发行)`.\n- Roles (3): 黑白印刷也成了该刊的特色 → `(成-01 :ARG0 (印刷-01 :manner (黑白) :aspect habitual) :ARG1 (特色 :poss… (刊 :mod (该))))`; temporal from previous sentence's main event."}
]}
```