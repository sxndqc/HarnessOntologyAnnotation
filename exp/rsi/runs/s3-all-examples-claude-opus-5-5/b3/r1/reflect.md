**Summary of changes.** These edits fix the recurring error patterns from the critique. To stay under the 30000-character limit, I compressed the intro and removed example lines that only repeat stated rules.

1. **虽然…不过 together.** A sentence with both now becomes `but-91 :ARG1 X :ARG2 Y` with no `:concession`. This removes the contradiction in 2.5.
2. **以 X 为目的.** It becomes `identity-91 :ARG1 (目的 :purpose-of V) :ARG2 X`. It is not have-purpose-91.
3. **New 2.3 patterns.**
   - 是 Adj 的 → `have-mod-91`, with an Adj that has no sense, aspect or triples.
   - A parenthetical slogan gloss → `identity-91`, joined by `and`, never `:medium`.
   - 第一夫人 → `have-rel-role-91`.
4. **Coreference.**
   - Re-entrancy is only for pronouns, zero arguments and 自己/其.
   - A repeated noun gets its own node plus `:same-entity`, even in the same sentence.
   - 他们 for an organisation in the same sentence re-enters that node.
   - No `:subset-of` without a clearly stated set.
5. **Names.**
   - The middle dot is a name token.
   - A bare category noun before a foreign name is the concept, not an appositive identity-91.
   - 地球 → `planet`.
   - The `individual-person` rule is repeated in the checklist.
6. **Reported speech.** `:quote` is now a rule, and the speaker gets its own modal triple for the content.
7. **New role rules.**
   - 与X有关系 → `有-03 :ARG0 (and …)`.
   - 后来 → `consecutive`, with no node for the connective, 还 or 就.
   - A listing 有 → `:example`, with no 有 node.
   - 重复/经常 → `:frequency`; 大部分 → `:mod`; 母公司 → `公司 :mod 母`.
   - 出现-01: what appears is `:ARG0`, the 在…中 place `:ARG1`.
   - 其中 with a superlative → `:ARG5` of have-degree-91, with an `implicit-argument` head.
   - Look up the PropBank compound first (算是, 改为).
8. **Aspect.**
   - An event noun under 停止/继续 → `process`, with the aspectual verb's agent re-entered as its ARG0.
   - Under 继续, the subject is ARG0 of both verbs.
   - 生存/存在 → `state`.
   - A resultative complement (创造出) → `performance`.
9. **Non-events.** Plain concepts with no sense (真实, 博君一笑, 中) get no temporal or modal triples.

```json
{"summary": "Fix 虽然+不过 → but-91; 以X为目的 → identity-91; 是Adj的 → have-mod-91; parenthetical gloss → identity-91; first lady → have-rel-role-91; re-entrancy only for pronouns (repeated nouns get own node + :same-entity), 他们 for org; names (·, category noun before foreign name, planet); :quote rule; 有关系 → 有-03 with and; 后来 → consecutive; listing 有 → :example; :frequency; 出现 roles; 其中+superlative → :ARG5 + implicit-argument; compound lookup first; aspect for nouns under 停止/继续, 生存 state, resultative performance; no triples for non-events. Trimmed intro and redundant examples to fit size.", "edits": [
{"op": "replace", "old": "A short version of the UMR 0.9 specification (`umr_guidelines.md` in this folder, umr4nlp/umr-guidelines),\nfor annotating Chinese and English at Stage 1 (numbered PropBank roles). It keeps what an annotator needs for\nmost sentences and leaves out the typological material, the fine-grained lattices, the field-linguistics\nsections and most of the examples. Where the full guideline uses the older short names (`AUTH`, `DCT`,\n`FullAff`, `:modstr`, `:ref-person`, `Performance`), this version uses the names of the UMR release data\n(`author`, `document-creation-time`, `full-affirmative`, `:modal-strength`, `:refer-person`, `performance`).", "new": "Abridged UMR 0.9 guidelines for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data."},
{"op": "replace", "old": "It is compared, node by node and relation by relation,\nwith an expert gold annotation made by these guidelines, so every concept, sense, role, attribute value\nand document-level relation counts. Take the time this needs:", "new": "It is scored against an expert gold annotation, concept by concept and relation by relation:"},
{"op": "replace", "old": "- Read the guidelines below carefully before you start, and go back to them for every decision you are\n  not sure of: the concept and its sense, the numbered and non-core roles, abstract concepts and named\n  entities, aspect, modal strength, polarity, and the temporal, modal and coreference relations.", "new": "- Read the guidelines below first and return to them for every unsure decision."},
{"op": "replace", "old": "- Do not guess when you can check: use the three tools (see Tools): search the full guidelines with\n  `search_guidelines` whenever the guidelines above do not settle a case, look up every predicate in\n  PropBank with `propbank_lookup` before you choose its sense and numbered roles, and look up how the gold\n  data annotates a construction, a word or a relation with `search_annotations`. Call them as often as you\n  need: many calls are expected.", "new": "- Do not guess when you can check: `search_guidelines` when the guidelines do not settle a case, `propbank_lookup` for every predicate (look up the compound first: 算是, 改为; use it if it exists), `search_annotations` for how gold annotates a construction. Many calls are expected."},
{"op": "replace", "old": "- Before you go on to the next sentence, check the graph against the guidelines once more: every word\n  that carries meaning has its concept, every event its aspect, every role the right direction; and at\n  the end check that the document-level relations cover every event and entity the guidelines ask for.", "new": "- Before the next sentence, recheck the graph: every meaningful word has a concept, every event an aspect, every role the right direction; at the end check the document-level relations."},
{"op": "delete", "old": "Finer values (`inceptive`, `directed-activity`, `semelfactive`, ...) exist in the full guideline; use them\nonly when they are clear."},
{"op": "delete", "old": "- Roles (3): 美国小报 → `:place (c / country ...)`; 电视节目 → `(p / 节目 :medium (t / 电视))`; 都经过 → `(j / 经-01 :mod (d / 都))`."},
{"op": "delete", "old": "- 由于 (2.5): 由于…内容 → `:reason (c / 内容 ...)`."},
{"op": "delete", "old": "- Aspect (4.1): 发行 (a paper's publishing) → `:aspect habitual`; 已经停止发行的 → 停止 `:aspect state`; 被称为 → `:aspect performance`."},
{"op": "delete", "old": "- Temporal (5.1): 富-01 under have-degree-91 → `(s5main :overlap s5f)`."},
{"op": "delete", "old": "- No invented owner (3): 发行网络版 → `(f / 发行-01 :ARG1 (w / 网络版))`."},
{"op": "delete", "old": "- Inner and (3): 奇闻轶事、传奇与新闻 → `(a / and :op1 (a2 / and :op1 奇闻 :op2 轶事) :op2 传奇 :op3 新闻)`."},
{"op": "delete", "old": "- Aspect (4.1): 曾经拥有过 → `:aspect state`; 纸本已经停刊 → `:aspect performance`; clause-level identity-91 → `:aspect state`; appositive identity-91, have-org-role-91, have-quant-91 → no aspect, no modal triple."},
{"op": "delete", "old": "- Entity type (2.1): 该周报 → `(z / 周报 :mod (g / 该))`, not `newspaper`."},
{"op": "delete", "old": "- have-degree-91 (4.1): no `:aspect` on it and no triples for it; only 富-01 gets `(s5main :overlap s5f)` and `(author :full-affirmative s5f)`."},
{"op": "delete", "old": "- Main event (5.1): 停止发行/拥有过 → `(document-creation-time :before e)`; 被称为 → `(document-creation-time :depends-on e)`; 以…而闻名 → `(闻名 :contained 发行)`."},
{"op": "delete", "old": "- 曾经 (3): 曾经拥有过 → `:temporal (c / 曾经)`."},
{"op": "delete", "old": "- Preposition (3): 至2007年 → `:temporal (d / date-entity :year 2007)`, no 至 node."},
{"op": "insert_after", "anchor": "A sentence-initial 不过/但是 that contrasts with the previous sentence gets no node, and the sentence's main verb is the root;", "text": " 虽然/尽管 X，不过/但是/却 Y in one sentence → `but-91 :ARG1 X :ARG2 Y`, no `:concession`;"},
{"op": "replace", "old": "*although* (虽然, 尽管) → `:concession`.", "new": "*although* (虽然, 尽管) without 不过/但是 → `:concession`."},
{"op": "insert_after", "anchor": "Keep `:reason`/`:purpose` roles only for phrase-level modifiers.", "text": "\n- 以 X 为目的 → `identity-91 :ARG1 (目的 :purpose-of V) :ARG2 X :aspect state`, not have-purpose-91; X (博君一笑) has no sense.\n- 后来/然后/接着 joining clauses → `(consecutive :op1 … :op2 …)`; the connective and 还/就 there get no node."},
{"op": "insert_after", "anchor": "*his wife* → `(p / person :ARG1-of (h / have-rel-role-92 :ARG2 p2 :ARG3 (w / wife)))`.", "text": "\nX (都)是 Adj 的 → `have-mod-91 :ARG1 X :ARG2 (Adj)`; the Adj has no sense, aspect or triples. A parenthetical gloss N：「Y」 → `identity-91 :ARG1 N :ARG2 Y :aspect state`, joined by `and` to the neighbouring clause, never `:medium`. 第一夫人 → `have-rel-role-91 :ARG3 (第一夫人 :place country)`, not have-org-role."},
{"op": "insert_after", "anchor": "In Chinese documents, a named person, or a personal pronoun for one individual (他, 她), is `individual-person`, not `person`.", "text": " 他们/它们 for an organisation or paper of the same sentence is that node's variable; in a later sentence it is a `person` node linked by `:same-entity`."},
{"op": "insert_after", "anchor": "they are the first and last `:opN`.", "text": " So is the middle dot (希拉里·克林顿 → `:op2 \"·\"`). A bare category noun before a foreign name (外星人 P'Lod) is the concept (`外星人 :name …`), not an appositive identity-91. 地球 → `planet :name`."},
{"op": "replace", "old": "- 其中 → `:mod (其中)` on the noun it introduces, not `:part`.", "new": "- 其中 → `:mod (其中)` on the noun it introduces, not `:part`; with a superlative (其中最大宗) it is `:ARG5` of have-degree-91, and the head is `implicit-argument :unit 宗`.\n- X 与/和/跟 Y 有关系 → `有-03 :ARG0 (and :op1 X :op2 Y)`, not `:companion`.\n- N 有 A、B…等 listing N's kinds → `N :example (and …)`, no 有 node.\n- 重复/经常 → `:frequency`; 大部分的 N → `:mod`; 母公司 → `公司 :mod 母`.\n- 出现-01: what appears is `:ARG0`, the 在…中 place `:ARG1 (中 :op1 …)`."},
{"op": "replace", "old": "Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. The\nUMR release data also marks it with `:quote <reporting event>` when the content is a quotation.", "new": "Reported speech and thought: the reported event is the `:ARG1` of the reporting verb, as in AMR. The content node (of 宣称/指/说, or a slogan's content under identity-91) always gets `:quote <reporting event or identity node>`, and the speaker gets `(speaker :full-affirmative content)`."},
{"op": "replace", "old": "- Within one sentence, coreference is a re-entrancy in the graph (one variable), not a `:coref` triple.", "new": "- Within one sentence, pronouns, zero arguments and 自己/其 are re-entrancies. A repeated noun (周报 after the named paper, 该刊) always gets its own node, even in the same sentence, linked by `:same-entity`. No `:subset-of` without a clearly stated set."},
{"op": "insert_after", "anchor": "A participle of a completed earlier event (遗留下来的) is `performance`.", "text": "\n- Overriding the habitual rule: an event noun under 停止/开始/继续 (停止…的发行) is `process`, with the aspectual verb's agent re-entered as its ARG0; under 继续 the subject is ARG0 of both verbs. 生存, 存在 → `state`. Verb + result complement (创造出) → `performance`."},
{"op": "insert_after", "anchor": "- Every event has `:aspect`; negated events have `:polarity -`.", "text": "\n- Every named person in a Chinese document is `individual-person`. Plain concepts with no sense (真实, 博君一笑, 中) get no temporal or modal triple."},
{"op": "append", "text": "\n- 虽然…不过 (2.5): 虽然他们宣称X（标语：Y），不过大部分报导以博君一笑为目的 → `(b / but-91 :ARG1 (a / and :op1 宣称 :op2 (i / identity-91 :ARG1 标语 :ARG2 Y)) :ARG2 (i2 / identity-91 :ARG1 (m / 目的 :purpose-of 报导) :ARG2 (g / 博君一笑)))`.\n- 是…的 (2.3): 都是真实的 → `(h / have-mod-91 :ARG2 (t / 真实) :mod (d / 都) :aspect state)`.\n- Name (2.2): 外星人P'Lod → `(x / 外星人 :name (n / name :op1 \"P\" :op2 \"'\" :op3 \"Lod\"))`.\n- 有关系 (3): 与P'Lod有暧昧关系，后来还领养 → `(c / consecutive :op1 (y / 有-03 :ARG0 (a / and :op1 h :op2 p) :ARG1 关系) :op2 领养-01)`."}
]}
```