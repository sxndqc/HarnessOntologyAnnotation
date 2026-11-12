## Summary of changes

The edits target the problems in the critique that will recur on other documents. Each changed rule also gets a short example under a new "## Examples" section at the end.

1. **Classifiers (2.2).** The old rule was wrong: it told the annotator to drop classifiers. Numeral + classifier phrases (including 一份, 一个) are now kept as `:quant N :unit (x / <classifier>)`.
2. **Title marks (2.2).** 《 》 are now included as the first and last `:opN` of a publication name.
3. **Discourse connectives (2.5).**
   - `but-91` and `contrast-91` take `:ARG1`/`:ARG2`, not `:opN`.
   - 由于/因为 map to `:reason`.
   - 以X而Y (known for X) is Y `:reason` X, attached inside the noun it modifies rather than as a new conjunct.
4. **Non-core roles (section 3).**
   - A country or region modifying a noun → `:place`.
   - A channel or medium (电视, 网络) → `:medium`.
   - A version or part of a publication → `:part-of`.
   - Adverbs 已经, 都, 也, 仍, 目前 → `:mod` or `:temporal` on the event they modify, never dropped or moved.
   - A modifier shared by coordinated nouns goes on each conjunct.
   - Re-entrant arguments are added only when the text expresses them.
   - Check the PropBank argument order of 属-type verbs.
5. **Aspect (4.1).**
   - Characteristic or repeated activities of an institution are `habitual`, even with 了 and without a frequency word.
   - 已经 + change-of-state verb used as a modifier is `state`.
   - 被称为-type passive naming is `performance`.
6. **Degree (4.2).** Superlatives and comparatives → `have-degree-91`; only intensifiers stay `:degree`. An adjectival chengyu before 的 is a `:mod`, not an event.
7. **Temporal (5.1).**
   - Copular/identity predicates and modifier properties get no temporal parent.
   - Dependent events in a sentence are chained to the sentence's main anchoring event.
   - 目前/现在 depend on `document-creation-time` (not `present-reference`), and the event then overlaps the time word.
8. **Coreference (5.3).** `:same-event` is used only when the participants are the same.

```json
{"summary": "Fix classifier rule (keep 一份/一个 as :quant+:unit), title marks as name tokens, but-91 :ARG1/:ARG2, 由于→:reason, 以X而Y→:reason, non-core role rules (:place for countries, :medium, :part-of, adverbs as :mod, shared modifiers on conjuncts, no invented arguments, 属 argument order), habitual/state/performance aspect rules, have-degree-91 for superlatives and chengyu as :mod, temporal rules (no parent for identity/modifier states, chain to main event, 目前 depends on DCT), same-event only with same participants; add Examples section.", "edits": [
{"op": "replace", "old": "an ordinary classifier (个, 本, 只, 位) is dropped (三本书 → `书 :quant 3`).", "new": "a numeral + classifier phrase is kept too, also with 一 (一份, 一个, 三本书 → `书 :quant 3 :unit (b / 本)`). Check with `search_annotations` when unsure."},
{"op": "insert_after", "anchor": "欧洲议会 → `:op1 \"欧洲\" :op2 \"议会\"`.", "text": " The title marks 《 》 around a publication's name are name tokens: they are the first and last `:opN`."},
{"op": "replace", "old": "- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而) `but-91`;", "new": "- contrast: `(c / contrast-91 :ARG1 ... :ARG2 ...)`; *but* (但是, 却, 然而, 不过) `but-91`. Both take `:ARG1` and `:ARG2`, never `:opN`;"},
{"op": "replace", "old": "*because* (因为, 由于) → `:cause`;", "new": "*because* (因为, 由于) → `:reason`; 以 X 而 Y (*known for X*) → Y `:reason` X. When such a clause describes a noun (e.g. the predicate noun of a 是 sentence), attach it inside that noun as `:ARG1-of`, not as a new conjunct;"},
{"op": "insert_after", "anchor": "`:subset-of`, `:name`, `:wiki`, `:opN`, `:vocative`, `:polite`, `:other-role` (when none fits).", "text": "\n\nFrequent choices:\n- A country or region modifying a noun (美国小报, *a US paper*) → `:place`, not `:mod`.\n- A channel or medium (电视, 网络, *TV*) → `:medium`.\n- A version, edition or part of a publication or thing (X的纸本) → `:part-of`, not `:possessor`.\n- Adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs such as 目前 → `:temporal` on that event. Never drop them, and never move them onto a noun or onto the connective (`but-91`, `and`).\n- A modifier shared by coordinated nouns goes on each conjunct, as one node re-used by re-entrancy, not on the `and` node.\n- Add an implicit or re-entrant argument only when the text expresses it.\n- Check the PropBank argument order: for 属-02 the thing owned is `:ARG0` and the owner `:ARG1`."},
{"op": "insert_after", "anchor": "| `process` | an event nominal, or a process whose type cannot be told (*the meeting*, 探索 as a noun) |", "text": "\n\n- A typical or repeated activity of a person or institution (publishing 发行, broadcasting, selling, collecting stories 综合) is `habitual`. This holds even without a frequency word, and even with 了, when the clause describes what the entity does in general.\n- 已经 + a change-of-state verb used as a modifier (已经停止发行的小报) is `state`: it is the entity's resulting condition.\n- A passive naming or evaluation (被称为, 被誉为) is `performance`.\n- 未经 (*without having undergone*) is `process`."},
{"op": "replace", "old": "- `:degree` for intensifiers and downtoners (*very, too, most*; 很, 非常, 太, 最) as a concept:", "new": "- A comparative or superlative (最, 更, *most*, *-er*) → `have-degree-91`. Its roles are `:ARG1` the entity, `:ARG2` the property, and `:ARG3` the degree (最/更, `most`/`more`).\n- An adjectival chengyu before 的 (荒诞不经的内容) is a `:mod`, not an event.\n- `:degree` is only for intensifiers and downtoners (*very, too*; 很, 非常, 太), as a concept:"},
{"op": "replace", "old": "(*nowadays*, 现在) on `past-reference` / `present-reference` / `future-reference`.", "new": "(*nowadays*, 现在, 目前) is also anchored to now: `(document-creation-time :depends-on s4t)`, then its event `(s4t :overlap s4e)`. Use `past-reference` / `present-reference` / `future-reference` only for vague times not tied to the moment of writing."},
{"op": "insert_after", "anchor": "- Annotate event–event relations only when they are clear.", "text": "\n- Give no temporal parent to a copular predicate (`identity-91` for 是) or to a property used as a modifier.\n- Within a sentence, anchor the dependent events (relative clauses, the 以…而 result, a second conjunct) to the sentence's main anchoring event, not each to `document-creation-time`. Example: `(document-creation-time :before s1f)`, then `(s1f :overlap s1s)` and `(s1k :contained s1f)`."},
{"op": "insert_after", "anchor": "- `(earlier :same-event later)`: two mentions of the same event.", "text": " Use it only when the participants are the same. *The paper stopped publishing* and *its print edition stopped* are different events."},
{"op": "append", "text": "\n## Examples\n\n- Classifier (2.2): 一份小报 → `(x / 小报 :quant 1 :unit (u / 份))`.\n- Title marks (2.2): 《世界新闻周报》 → `:name (n / name :op1 \"《\" :op2 \"世界\" :op3 \"新闻\" :op4 \"周报\" :op5 \"》\")`.\n- but-91 (2.5): 不过… → `(b / but-91 :ARG1 ... :ARG2 ...)`.\n- 以…而闻名 (2.5): a tabloid known for its reports → `(x / 小报 :ARG1-of (k / 闻名-01 :reason (r / 报导-01 :ARG0 x)))`.\n- 由于 (2.5): 由于…内容 → `:reason (c / 内容 ...)`.\n- Roles (3): 美国小报 → `:place (c / country ...)`; 电视节目 → `(p / 节目 :medium (t / 电视))`; 都经过 → `(j / 经-01 :mod (d / 都))`.\n- Shared modifier (3): 奇怪的新闻与专栏 → `(a / and :op1 (n / 新闻 :mod (q / 奇怪)) :op2 (z / 专栏 :mod q))`.\n- 属 (3): 属自己的节目 → `(p / 节目 :ARG0-of (s / 属-02 :ARG1 x))`.\n- Aspect (4.1): 发行 (a paper's publishing) → `:aspect habitual`; 已经停止发行的 → 停止 `:aspect state`; 被称为 → `:aspect performance`.\n- Superlative (4.2): 最富创意的报纸 → `(x / 报纸 :ARG1-of (h / have-degree-91 :ARG2 (f / 富-01 :ARG1 (c / 创意)) :ARG3 (z / 最)))`.\n- 历史上 (4.2): 美国历史上 → `:temporal (s / 上 :op1 (h / 历史 ...))`.\n- Temporal (5.1): 目前停刊 → `(document-creation-time :depends-on s4t)` `(s4t :overlap s4e)`; no temporal triple for `identity-91`.\n"}
]}
```