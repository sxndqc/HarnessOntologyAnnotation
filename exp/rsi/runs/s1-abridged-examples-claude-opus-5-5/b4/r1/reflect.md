## Summary of changes

The critique's recurring problems are addressed by these edits. To stay under the 30000-character limit, I freed space first:
- removed the English sample graph and the preamble;
- shortened the entity-type list;
- dropped examples that only repeat a rule stated in the text.

The fixes:
1. **「…」 headlines/titles** become `publication` names with bracket and punctuation `:opN`s and `:quant 1 :unit (篇)`. They get no inner events, no `:quote` and no triples. Named events with a year are `event` names, and a named institution is one name.
2. **Chinese adjectives in CPB** (荒唐, 真实, 显著…) are `-01` stative events with `:ARG0`, `:aspect state`, a temporal parent and a modal triple. As modifiers they attach by `:ARG0-of`. V+者 is `者 :ARG0-of`.
3. **Sense and role numbers come from CPB for every predicate.** 刊登/贴到 take `:ARG1` = location and `:ARG2` = the thing published.
4. **Adverb nodes:** no node for 甚至 or 还; 也 only as the sole adverb of a simple clause; 靠 X V becomes `V :reason X`.
5. **Aspect:** the habitual cue is dropped when a single occasion or article is given. Sentence-initial 为了 X，Y about a done act becomes `have-reason-91`. An event nominal modifying a noun is `:mod` with `process`.
6. **Temporal:**
   - Reported content that is clearly earlier than the report takes `:before`.
   - Coordinated clauses chain from the previous conjunct.
   - Under a connective root, the first clause is anchored and the next chains from it.
   - Events in modifiers take `:overlap`.
7. **Modal:** a publication's own reporting acts are conceived by the publication, and their content gets only the author triple. An author→entity triple is written only for real conceivers.
8. **`:part-of`** extends to a publication's content and articles.

```json
{"summary": "Free space (drop sample graph, preamble, long type list, redundant examples); add rules for 「」 titles as publication names, named events with year, Chinese CPB adjectives as stative -01 verbs, general CPB roleset lookup (刊登/贴到 roles), fewer adverb nodes and 靠 as :reason, narrowed habitual cue, 为了-initial have-reason-91, nominal modifiers as :mod process, temporal chaining for coordinated/connective clauses and earlier reported content, publication as conceiver of its reporting acts, :part-of for content/articles; add short examples.", "edits": [
{"op": "delete", "old": "```\nHe denied any wrongdoing.\n\n(s3d / deny-01\n    :ARG0 (s3p / person\n        :refer-person 3rd\n        :refer-number singular)\n    :ARG1 (s3d2 / do-02\n        :ARG0 s3p\n        :ARG1 (s3t / thing\n            :mod (s3a / any)\n            :ARG1-of (s3w / wrong-02))\n        :aspect process)\n    :aspect performance)\n\n(s3s0 / sentence\n    :temporal ((document-creation-time :before s3d)\n               (s3d :before s3d2))\n    :modal ((root :modal author)\n            (author :full-affirmative s3p)\n            (s3p :full-affirmative s3d)\n            (s3d :unspecified s3d2))\n    :coref ((s2p :same-entity s3p)))\n```"},
{"op": "replace", "old": "(re-entrancy: `:ARG0 s3p` above)", "new": "(re-entrancy)"},
{"op": "delete", "old": "**Make the annotation as correct as you can**: it is compared node by node and relation by relation with an expert gold annotation. Check every decision against the guidelines, follow the examples, and check each graph (concepts, aspect, role direction, document-level coverage) before moving on."},
{"op": "delete", "old": "UMR 0.9 abridged, for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data."},
{"op": "replace", "old": "Types: `person`,\n`country`, `city`, `province`, `state`, `nationality`, `ethnic-group`, `language`, `organization`,\n`company`, `government-organization`, `political-party`, `university`, `newspaper`, `publication`, `river`,\n`mountain`, `building`, `airport`, `road`, `event`, `war`, `conference`, `festival`, `award`, `law`,\n`disease`, `product`, `spaceship`, `planet` (地球), ... (as in AMR).", "new": "Types as in AMR (`country`, `city`, `organization`, `company`, `newspaper`, `publication`, `building`, `event`, `planet` (地球), ...)."},
{"op": "insert_after", "anchor": "Do not add `:wiki` in Chinese documents.", "text": " A headline or article title in 「 」 (一篇「…」, 新闻「…」) is `(publication :name (name :op1 \"「\" … :opN \"」\"))`, one `:opN` per word, punctuation included, with `:quant 1 :unit (篇)` after 一篇; no inner events, no `:quote`, no modal or temporal triples; after a common noun: `(新闻 :ARG1-of (identity-91 :ARG2 (publication …)))`. A named event with a year (2000年总统大选) is `(event :name (name :op1 \"2000\" :op2 \"年\" :op3 \"总统大选\"))`, not a date-entity; a following 时 adds no node. A named institution is one name (美国参议院 → `(building :name (name :op1 \"美国\" :op2 \"参议院\"))`)."},
{"op": "insert_after", "anchor": "the copula (*be*, 是) — it becomes one of the abstract predicates.", "text": "\n\n**Chinese adjectives are verbs.** Look up every adjective, predicate or modifier: if CPB has it (荒唐, 荒谬, 可笑, 真实, 显著), it is `<word>-01` with `:ARG0` = the thing described, `:aspect state`, a temporal parent (`:overlap` its governing event) and `(author :full-affirmative …)`; as a modifier it is `:ARG0-of` (显著位置 → `(位置 :ARG0-of (显著-01 :aspect state))`). V+者 → `(者 :ARG0-of (V-00 :aspect state))`. `have-mod-91`/`:mod` only for words not in CPB (黑白, 八卦)."},
{"op": "replace", "old": "- Take role numbers from the Chinese roleset, not from the English equivalent:", "new": "- Take the sense and role numbers of every Chinese predicate from its CPB roleset, never from English (当-02 position holder; 当选 `:ARG0` electee; 刊登, 贴到, 登: `:ARG1` location, `:ARG2` thing published, no `:place`):"},
{"op": "replace", "old": "已经, 都, 也, 甚至, 还 and 其中 → `:mod (<word>)`, but no node for 就, for 还 after 后来, for 仍 beside 继续, or for 都 in 都以…为目的;", "new": "已经, 都 and 其中 → `:mod (<word>)`; 也 only as the sole adverb of a simple clause; no node for 甚至, 还, 就, 仍 beside 继续, or 都 in 都以…为目的; 靠 X V → `V :reason X`, no 靠 node;"},
{"op": "replace", "old": "(纸本, 网络版, 分部) takes `:part-of` its whole", "new": "(纸本, 网络版, 分部), or its content or article (内容, 一篇新闻), takes `:part-of` its whole"},
{"op": "replace", "old": "used as predicates are `habitual`, even with 了; this cue", "new": "used as predicates are `habitual`, even with 了, unless one occasion or article is given (time clause, 一篇, one headline → `performance`); this cue"},
{"op": "insert_after", "anchor": "even when it is modally full-affirmative.", "text": " But a sentence-initial 为了 X，Y about a done act is `(have-reason-91 :ARG1 Y :ARG2 X)` with no `:aspect`; X takes Y's aspect and gets no temporal or modal triple. An event nominal modifying a noun is `:mod` with `process` (握手的照片 → `(照片 :mod (握手-01 :aspect process))`)."},
{"op": "replace", "old": "Reported content (宣称, 指, 说): its first event is `(<report> :overlap X)`;", "new": "Reported content (宣称, 指, 说): its first event is `(<report> :overlap X)`, or `(<report> :before X)` when clearly earlier (earlier year, 过); a date inside it gets no parent;"},
{"op": "insert_after", "anchor": "Leave no event without a temporal parent.", "text": " Chain clauses joined by `and`/还 each from the previous conjunct (`(报导 :overlap 注销) (注销 :overlap 指)`); under `but-91` or another connective root, anchor the first clause's event (`:before` DCT in a past narrative) and chain the next from it. A completed event in a modifier is `:overlap`; `:before` only for a clear resultative participle."},
{"op": "insert_after", "anchor": "The top content node (with `:quote`, even an abstract predicate) gets both `author` and conceiver triples.", "text": "\n- A publication's reporting acts (报导, 注销, 指 with the paper as subject): `(author :full-affirmative <paper>) (<paper> :full-affirmative <act>)`; their content events get only the author triple. Write `(author :full-affirmative <entity>)` only for an entity that conceives some event."},
{"op": "delete", "old": "- Superlative (2.3): 最富创意 → `(have-degree-91 :ARG2 (富-01 :ARG1 (创意)) :ARG3 (最))`."},
{"op": "delete", "old": "- Named person (2.2): 格内洛索·波普 → `(individual-person :name (name :op1 \"格内洛索\" :op2 \"·\" :op3 \"波普\"))`."},
{"op": "delete", "old": "- List names (3): 如蝙蝠男孩、外星人P'Lod等 → `(individual-person :name (name :op1 \"蝙蝠\" :op2 \"男孩\"))`, `(individual-person :name (name :op1 \"外星人\" :op2 \"P\" :op3 \"'\" :op4 \"Lod\"))`."},
{"op": "delete", "old": "- Degree (2.3): 美国历史上最…的报纸 → `(报纸 :temporal (上 :op1 (历史 :place (country …))))`, `have-degree-91` without aspect; 称为 → `称为-01`."},
{"op": "delete", "old": "- Apposition (3): 旗下的八卦小报《国家询问报》 → `(newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 :mod (旗下) :mod (八卦))))`."},
{"op": "delete", "old": "- Measure noun (2.2): 发行量达到120万份 → `(达到-01 :ARG0 (量 :quant-of (发行-01 :ARG1 …) :ARG1-of (have-quant-91 :ARG2 1200000 :unit (份))) :aspect performance)`, `(达到 :overlap 发行)`."},
{"op": "delete", "old": "- Control (3): 网络版继续生存 → `(继续-01 :ARG0 s11n :ARG1 (生存-01 :ARG0 s11n :aspect state))`; temporal `(停止 :overlap 继续)`."},
{"op": "delete", "old": "- List (3): 题材有A、B等 → `(题材 :example (and :op1 A :op2 B :op3 (等)))`; 重复出现 → `:frequency (重复)`."},
{"op": "delete", "old": "- Apposition (3): 母公司美国媒体公司 → `(company :name … :ARG1-of (identity-91 :ARG2 (公司 :mod (母))))`; later 周报的网络版 → `(网络版 :part-of (s11x5 / 周报))` + `(s11n2 :same-entity s11x5)`."},
{"op": "append", "text": "- Title (2.2): 刊登一篇「苏联复制…」 → `(刊登-01 :ARG2 (publication :name (name :op1 \"「\" :op2 \"苏联\" … \"」\") :quant 1 :unit (篇)))`, no events inside.\n- Adjective (2.1): 内容虽然荒唐 → `(荒唐-01 :ARG0 (内容 :part-of 周报) :aspect state)`.\n- Report (5.1, 5.2): 指柯林顿1992年靠外星人背书当选 → `(当选-01 :ARG0 柯林顿 :reason (背书-00 :ARG0 外星人))`, `(指 :before 当选)`, `(刊 :full-affirmative 指) (author :full-affirmative 当选)`.\n"}
]}
```