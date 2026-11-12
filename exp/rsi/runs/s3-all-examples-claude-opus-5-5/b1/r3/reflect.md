**Summary of changes.** These fix the recurring patterns in the critique and keep the rules that matched gold.

1. **N1+V+N2 procedure compounds.** A noun like 新闻查证程序 is now `N2 :ARG0-of (identity-91 :ARG1 V)`, with N1 as `:ARG1` of V. The event inside the noun takes the event that contains it as its temporal parent, not the sentence's main event.
2. **Entity types.** English entity types are used only for named nodes and pronouns. A common-noun mention such as 该周报 stays as the Chinese word.
3. **have-degree-91.** It gets no aspect, no temporal triple and no modal triple. The property under its `:ARG2` carries all three.
4. **Main-event anchoring.** The contradiction in 5.1 is resolved:
   - use `:before` for clearly past main events;
   - use `:depends-on` for current states and for namings or evaluations that still hold.
5. **以…而闻名.** 闻名 is the parent of the habitual event through `:contained`.
6. **曾经** is `:temporal`, not `:mod`.
7. **未经** gets no `:polarity -`. The negation is only the full-negative modal triple.

A short example for each fix is added to the Examples section.

```json
{"summary": "Add N1+V+N2 procedure compound rule (identity-91) and its temporal parent; restrict English entity types to named nodes/pronouns; have-degree-91 has no aspect/temporal/modal; resolve :before vs :depends-on for main events; 以…而闻名 → (闻名 :contained 发行); 曾经 → :temporal; 未经 without :polarity -; examples.", "edits": [
{"op": "replace", "old": "- Adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs such as 目前 → `:temporal` on that event.", "new": "- Aspectual and scalar adverbs 已经, 都, 也, 仍, 还 → a `:mod` node on the event they modify. Time adverbs 目前, 曾经, 现在, 当时 → `:temporal` on that event."},
{"op": "insert_after", "anchor": "- 其中 → `:mod (其中)` on the noun it introduces, not `:part`.", "text": "\n- N1 + V + N2 where N2 (程序, 过程, 制度, 方式, 手续) is the procedure that V names: `N2 :ARG0-of (identity-91 :ARG1 V)`, and N1 is the object of V (`V :ARG1 N1`), with V `:aspect process`. Do not flatten N1 and V into `:mod`s of N2. Other modifiers (一般) stay `:mod` of N2."},
{"op": "insert_after", "anchor": "`city`, `organization`, ...).", "text": " Use an English entity type only for a node with `:name`, or for a pronoun. A common-noun mention, even one that refers back to a named entity (该周报, 这家公司), is the Chinese word itself (`周报`) with its `:mod (该)`. Coreference links it to the named mention."},
{"op": "replace", "old": "Only their temporal triple is left out.", "new": "Only their temporal triple is left out. Exception: `have-degree-91` gets no `:aspect`, no temporal triple and no modal triple. The property under its `:ARG2` (富-01) carries the aspect, the temporal triple and the modal triple."},
{"op": "replace", "old": "- 未经 (*without having undergone*) is `process`.", "new": "- 未经 (*without having undergone*) → `经-01`, `:aspect process`, with no `:polarity -`. Its negation is only the modal triple `(author :full-negative 经-01)`."},
{"op": "replace", "old": "Every other node with a sense and an `:aspect` gets a parent, normally `(main-event :overlap X)`. This includes an event inside a noun (查证-01) and the property under have-degree-91 (富-01).", "new": "Every other node with a sense and an `:aspect` gets a parent, normally `(main-event :overlap X)`. This includes the property under have-degree-91 (富-01). An event inside a noun takes as parent the event whose argument contains it (未经…查证程序 → `(经-01 :overlap 查证-01)`), not the sentence's main event."},
{"op": "replace", "old": "- Anchor each sentence's main event to `document-creation-time` (`:before` if past).", "new": "- Anchor each sentence's main event to `document-creation-time`. Use `:before` when it is clearly past (了, 过, 曾经, 已经停止). Use `:depends-on` when it is a current state, or a naming or evaluation that still holds (目前…, 被称为, 被誉为)."},
{"op": "replace", "old": "(relative clauses, the 以…而 result, a second conjunct)", "new": "(relative clauses, a second conjunct)"},
{"op": "insert_after", "anchor": "The main event is always the parent (first element).", "text": "\n- 以 X 而闻名: the reputation state 闻名 is the parent of the entity's habitual event, `(闻名 :contained 发行)`. 闻名 itself gets no parent."},
{"op": "append", "text": "\n- Procedure compound (3): 一般的新闻查证程序 → `(x / 程序 :ARG0-of (i / identity-91 :ARG1 (c / 查证-01 :ARG1 (n / 新闻) :aspect process)) :mod (y / 一般))`.\n- Entity type (2.1): 该周报 → `(z / 周报 :mod (g / 该))`, not `newspaper`.\n- have-degree-91 (4.1): no `:aspect` on it and no triples for it; only 富-01 gets `(s5main :overlap s5f)` and `(author :full-affirmative s5f)`.\n- Main event (5.1): 停止发行/拥有过 → `(document-creation-time :before e)`; 被称为 → `(document-creation-time :depends-on e)`; 以…而闻名 → `(闻名 :contained 发行)`.\n- 曾经 (3): 曾经拥有过 → `:temporal (c / 曾经)`.\n- 未经 (4.1): `(j / 经-01 :aspect process)` with no `:polarity`, plus the triple `(author :full-negative j)`."}
]}
```