**Summary of changes.** I made five fixes from the critique, each with a corrected or new example.

1. **-91/-92 nodes.** The 4.1 rule now separates two cases:
   - A -91/-92 node that is the predicate of a clause (X 是 Y, have-reason-91, have-purpose-91) gets `:aspect state` and a modal triple.
   - A -91/-92 node inside a noun phrase gets no aspect and no triples. This covers an appositive identity-91, have-org-role-91 or have-rel-role-92 for a role noun, and have-quant-91 under 量.
   - I corrected the contradicting examples (identity-91 aspect, 创始人).
2. **发行-01 under 量.** It gets no `:aspect` and no modal triple. Its only document-level triple is `(main :overlap 发行)`.
3. **Event nouns as arguments.** An event noun that is an argument of a verb (黑白印刷) keeps its sense and gets aspect, a temporal parent and a modal parent. I corrected the wrong Manner example.
4. **Repeated entities and 版面.** An entity mentioned twice in one sentence is written in full at its first textual mention; later mentions reuse the bare variable. 版面 is always `:part-of` the paper, never `paper :part 版面`.
5. **Prepositions before times.** A preposition before a time (至/在/于/到/从) gets no node.

```json
{"summary": "Clause-level vs NP-internal -91/-92 aspect/modal; no aspect on 发行 under 量; event nouns as arguments keep sense (fix 黑白印刷 example); entity full node at first textual mention, 版面 :part-of only; no node for prepositions before dates.", "edits": [
{"op": "replace", "old": "- `identity-91` and the other -91/-92 predicates are events too: give them `:aspect state` and a modal triple `(author :full-affirmative X)`. Only their temporal triple is left out. Exception: `have-degree-91` gets no `:aspect`,", "new": "- A -91/-92 node that is the predicate of a clause (X 是 Y as the main or a conjoined clause, have-reason-91, have-purpose-91) gets `:aspect state` and `(author :full-affirmative X)`, and no temporal triple. A -91/-92 node inside a noun phrase gets no `:aspect`, no temporal triple and no modal triple: an appositive `:ARG1-of (identity-91 ...)`, have-org-role-91/have-rel-role-92 reifying a role noun, have-quant-91 under 量. Likewise `have-degree-91` gets no `:aspect`,"},
{"op": "replace", "old": "The inner 发行-01 gets `(main :overlap 发行)` but no modal triple.", "new": "The inner 发行-01 gets no `:aspect` and no modal triple; its only document-level triple is `(main :overlap 发行)`."},
{"op": "replace", "old": "This holds even without a frequency word,", "new": "(Not 发行-01 under `量 :quant-of`: it has no aspect.) This holds even without a frequency word,"},
{"op": "replace", "old": "- A modifier of an event noun (黑白印刷) is `:manner`, not `:mod`.", "new": "- An event noun that is an argument of a verb (印刷 in 黑白印刷成了特色) keeps its PropBank sense (印刷-01) and gets aspect (a paper's practice: `habitual`), a temporal parent and a modal triple. Its modifier (黑白) is `:manner`, not `:mod`.\n- An entity mentioned twice in one sentence: write its full node (name, appositive, modifiers) at its first mention in the text, and only the bare variable at the later mention, even if the later mention comes first in the graph.\n- A preposition before a time (在, 于, 至, 到, 从 + 年) gets no node: the date-entity itself is the `:temporal`. Only 上 of 历史上 is a node."},
{"op": "replace", "old": "It is the argument of the verb, not a modifier of the name.", "new": "It is the argument of the verb, not a modifier of the name. A paper's 版面 (由黑白版面改为彩色版面) is always `版面 :part-of paper`, never `paper :part 版面`."},
{"op": "replace", "old": "- Manner (3): 黑白印刷 → `(y / 印刷 :manner (h / 黑白))`; 1980年代", "new": "- Event noun (3): 黑白印刷也成了特色 → `:ARG0 (y / 印刷-01 :manner (h / 黑白) :aspect habitual)` + `(成 :overlap y)` `(author :full-affirmative y)`; 1980年代"},
{"op": "replace", "old": "identity-91 → `:aspect state`.", "new": "clause-level identity-91 → `:aspect state`; appositive identity-91, have-org-role-91, have-quant-91 → no aspect, no modal triple."},
{"op": "replace", "old": "(h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))`.", "new": "(h / have-org-role-91 :ARG3 (r / 人 :ARG0-of (c / 创始-00 :aspect performance))))` (no aspect, no modal on h)."},
{"op": "append", "text": "\n- Preposition (3): 至2007年 → `:temporal (d / date-entity :year 2007)`, no 至 node.\n- First mention (3): 《Y》将由黑白版面改为… then Y的标准 → `改为-01 :ARG1 (b / 版面 :part-of (n / newspaper :name ... :ARG1-of (identity-91 ...)) :mod (h / 黑白))` … `(标准 :possessor n)`.\n- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`."}
]}
```