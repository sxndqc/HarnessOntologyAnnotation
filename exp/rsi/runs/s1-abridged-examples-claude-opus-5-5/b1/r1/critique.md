# Review of the annotator's UMR of the *Weekly World News* document, with changes to the instruction

The biggest losses were in temporal relations (F 30), reentrancy (F 15), aspect (F 60), event core and peripheral roles, and named-entity tokens and wiki. Most of these come from a handful of rules that the instruction leaves out or gets wrong for Chinese. The problems are listed below, most costly first.

---

## 1. Temporal structure: the annotator anchors everything to DCT or to a time word, not to other events (h_temporal F 30, about 12 units)

**What went wrong:**
- **Sentence 1:** every event hung from `document-creation-time` (DCT), and 停止 was used as the parent of 发行.
  - Gold anchors only the main habitual event to DCT and hangs the rest from it: `(document-creation-time :before s1x3) (s1x3 :overlap s1x4) (s1x7 :contained s1x3) (s1x3 :overlap s1x8)`.
  - Gold gives no temporal parent to `identity-91`. The annotator's `(document-creation-time :overlap s1i)` was counted as extra.
- **Sentence 4:** the annotator wrote `(present-reference :depends-on s4m) (s4m :contained s4t) (s4m :contained s4j)`. Gold does not anchor the events to 目前. It chains them: `(document-creation-time :depends-on s4x) (s4x :overlap s4x2) (s4x2 :overlap s4x6)`.
- **Sentence 5:** gold has `(document-creation-time :depends-on s5x)`; the annotator wrote `:overlap`.
- **Missing parents:** two events got no temporal parent at all:
  - 查证 in sentence 2: gold `(s2x8 :overlap s2x13)`.
  - 属 in sentence 3: gold `(s3x :overlap s3x6)`.

**Why:** Rule 5.1 says "Annotate event–event relations only when they are clear" and makes DCT the default. That pushes the annotator to anchor every clause to DCT. Nothing tells it that:
- the other events of a sentence normally chain off the first one, usually with `:overlap`;
- events inside nouns and relative clauses also need a parent;
- non-verbal `identity-91` and abstract predicates may get no temporal parent;
- the release data uses `document-creation-time :depends-on <event>` for the main event of some sentences.

**Change:**
- Replace the "only when they are clear" line with: "Anchor one main event of each sentence to DCT (or to a time expression). Attach every other event of the sentence to that event or to a nearby event, usually with `:overlap` (`:contained` if it lies inside it). Every event inside a relative clause or modifier also gets a parent, normally its governing event with `:overlap`."
- Add: "Do not give `identity-91` or `have-*-91` copular predicates a temporal parent."
- Add: "A time word like 目前 or 现在 is a modifier. Do not make it the parent of the events."
- Add the sentence 4 chain from gold as an example.

## 2. Measure words, aspect markers and adverbs dropped as nodes (a_entity_found, d_peripheral, c_other_attributes: about 12 units)

**What went wrong:**
- **Classifier plus measure word:**
  - 一份…小报: gold has `:quant 1 :unit (s1x5 / 份)`. The annotator dropped both.
  - 一个…节目: gold has `:quant 1 :unit (s3x7 / 个)`. The annotator dropped the unit.

  The instruction says 个 "is dropped", which is wrong for this data. Another gold document confirms it: 一款 → `:quant 1 :unit (款)`.
- **Adverbs gold keeps as `:mod` nodes, which the annotator left out:**
  - 已经 in sentence 1 (`:mod (s1x6 / 已经)` on 停止) and in sentence 4;
  - 都 in sentence 2;
  - 其中 in sentence 2;
  - 曾经 in sentence 3 (gold has `:temporal (s3x9 / 曾经)`).

**Why:** Section 2.2 explicitly says to drop 个/本/只/位. The instruction also never says that Chinese adverbs (已经, 都, 也, 仍, 曾经) become nodes. The annotator did keep 也 and 仍, but treated 已经 and 曾经 as pure aspect markers.

**Change:**
- Rewrite the classifier rule: "一 + classifier + noun → `:quant 1 :unit (<classifier>)`, for 个, 份, 款 and the like as well."
- Add: "Adverbs such as 已经, 都, 也, 仍, 曾经 and 其中 are concepts: `:mod (<word>)`, or `:temporal` for 曾经. They are not only aspect cues."

## 3. Named entities: brackets, wiki, and how the country modifier attaches (f_name_tokens 50, f_wiki 0, e_peripheral_labels: about 9 units)

**What went wrong:**
- **Title brackets:** the annotator wrote `:op1 "世界" :op2 "新闻" :op3 "周报"` in sentences 1 and 4. Gold includes the brackets: `:op1 "《" :op2 "世界" :op3 "新闻" :op4 "周报" :op5 "》"`. Another gold document does the same for every 《…》 title.
- **Wiki:** the annotator added `:wiki` three times (the paper twice and 美国 once in each of sentences 1 and 5 — four wiki values in all). Gold Chinese data has no `:wiki`, so each one counts as an extra.
- **Country as modifier:**
  - 美国超市小报 and 美国历史: gold uses `:place (s1c / country …)`. The annotator used `:mod`.
  - 电视节目: gold uses `:medium (电视)`. The annotator used `:mod`.
- **Unwanted coref:** 美国 in sentence 1 and 美国 in sentence 5 were linked; gold does not link them.

**Change:**
- "In Chinese names, keep the title brackets 《 》 as their own `:opN`."
- "Do not add `:wiki` in Chinese documents."
- "A country or place name that modifies a noun is `:place`, not `:mod`. A medium (电视, 网络) is `:medium`."
- "Do not corefer a repeated country name used only as a modifier."

## 4. Aspect (c_aspect F 60, 6 units)

**What went wrong:**
| word | annotator | gold | note |
|---|---|---|---|
| 发行 (sentence 1) | process | habitual | |
| 停止 (sentence 1) | performance | state | 已经停止 = it is in the stopped state |
| 综合 (sentence 2) | performance | habitual | a characterizing description of the paper |
| 经 (sentence 2) | habitual | process | |
| 发行 (sentence 4) | activity | habitual | |
| 称为 (sentence 5) | state | performance | |

**Why:** The table in 4.1 ties 了 to `performance`. It does not say that verbs describing what a publication or organization regularly does (发行, 报导, 综合) are `habitual`, even with 了. It also does not say that 已经 + a stop or end verb in a relative clause that describes something is a resulting `state`.

**Change:** add to 4.1:
- "Recurring institutional activities (publishing, reporting, compiling) are `habitual`, even with 了."
- "已经 + 停止 or another end verb used to describe an entity → `state`."
- "Passive naming or labelling (被称为) → `performance`."

## 5. Clause structure and reentrancy (g_reentrancy F 15, core and peripheral roles)

**What went wrong:**
- **Sentence 1, wrong root and wrong arguments:**
  - The annotator wrapped the sentence in `and` and made 闻名 a separate clause whose ARG1 and ARG0 point to the name node.
  - Gold puts 闻名 inside the predicate noun: `小报 :ARG1-of (闻名-01 :reason (报导-01 :ARG0 s1x …))`.
  - The annotator also added `发行-01 :ARG1 s1x` and inverted the stop relation. Gold has `发行-01 :ARG1-of (停止-01)`.
- **Sentence 2, modifiers on a coordination:**
  - The annotator put shared modifiers on the `and` node and added a made-up role `:subset`.
  - Gold distributes them to each conjunct as reentrancies: `新闻 :mod s2x6 :mod s2x7`, `专栏 :mod s2x6 :mod s2x7`.
- **Sentence 4, invented arguments:** `发行-01 :ARG0 s4n` and `网络版 :possessor s4n` are not in the text. They were counted as extra reentrancies.
- **以…而闻名:** gold uses `:reason`, not `:cause`. The same holds for 由于 in sentence 5: gold `:reason`, annotator `:cause`.

**Change:**
- "In 'X 是 … Y, 以 … 而 V' the second predicate modifies Y (`Y :ARG1-of V`). Do not add a coordinating `and`."
- "Distribute a shared modifier to each conjunct by reentrancy. Never put `:mod` on `and`."
- "Do not add arguments that are not expressed or clearly implied."
- "因为, 由于 and 以…而 → `:reason`." This fixes the instruction's current mapping of 因为/由于 to `:cause`.

## 6. Lexical choices: concept splits, abstract-predicate frames, core roles (event and entity concepts, core args: about 7 units)

**What went wrong:**
- **奇闻轶事:** treated as one chengyu node. Gold splits it: `and :op1 奇闻 :op2 轶事`, because it is two nouns.
- **属 in sentence 3:** the annotator used `belong-91` with ARG2. Gold uses the PropBank verb `属-02` with `:ARG0` = 节目 and `:ARG1` = 周报. A lexical verb present in Chinese PropBank wins over the abstract predicate.
- **停刊:** gold has `:ARG0 纸本`; the annotator used ARG1. Also, 纸本 is `:part-of` the newspaper, not its `:possessor`.
- **不过:** gold uses `but-91`; the annotator used `contrast-91`. The instruction already lists *but* → `but-91` for 但是 but not for 不过. Add 不过 and 可是 to that list.
- **最富创意:** gold has `have-degree-91 :ARG2 (富-01 :ARG1 创意) :ARG3 (最)`. The annotator wrote `:degree 最` on 富. The table should add `have-degree-91` for superlatives and comparatives.
- **历史上:** gold makes 上 a node with `:op1 历史`, attached as `:temporal`.
- **未经…程序:** gold has `程序 :ARG0-of (identity-91 :ARG1 查证-01)` and no `:polarity` on 经-01 (the negation is carried only by the modal relation). Gold also makes 查证 `partial-affirmative` from the author. These are idiosyncratic. A short note would suffice: "With 未经 a negated event, the full-negative modal relation is enough."

**Change:**
- Add to 2.6: "A chengyu is one concept only if it is a fixed four-character idiom. Coordinated noun pairs such as 奇闻轶事 are split."
- Add to 2.3: "Prefer the Chinese PropBank verb (属-02, 拥有-01) over `belong-91` / `have-91` when the verb is in the text; check its roles with the frame."

## Keep (worked well)

- **Modal annotation (F 94):** `(root :modal author)` plus `full-affirmative` for asserted events, and `full-negative` for 未经. Keep 5.2 as it is.
- **Coreference chain for the paper (recall 100):** 周报 linked across sentences, earlier mention first, entity nodes only. Keep 5.3.
- **Senses and document format:** all PropBank senses were correct (100) and the document format was correct (100). Keep the `<word>-01` and `-00` rules and the format conventions.
- **identity-91 for 是:** used correctly, with ARG1 and ARG2 right (core args of abstract predicates scored 100).
- **Chinese concept wording:** concepts kept as written in Chinese, and event nominals such as 查证 marked `process`.