The critique found five patterns. Two of them come from gold errors (the 出现 temporal variable typo and 领养-00), so I leave those alone. I fix the other three, which will recur on other documents:

1. **Reported-content modal rule.** Only nodes that carry their own `:quote` (the top content node, a slogan's verb) get both the `author` triple and the speaker triple. Events nested inside the content without a `:quote` (the subject 报导 of 报导是真实的) get only the `author` triple. For 被指 or 据说 with no written speaker, the content events get only the conceiver triple, with no `author` triple. The author still asserts the subject node and 指.
2. **Slogan verb re-entrancy.** A quoted slogan whose owner is written takes that owner as `:ARG0` of its verb. This is an exception next to the control-verb exception; the rule that 他们的报导 adds no `:ARG0` stays.
3. **Alignment cases.** Every sentence must be aligned. A shortened repeat (周报) is aligned to its own word. In 母公司美国媒体公司, `公司` is aligned to 母公司 and `company` to the name words only. 外星人 before a name is aligned to its own word, apart from the name.

I updated the 被指 and quote examples to match the new modal rule. The instruction was 79 characters under its limit, so I freed space by:
- shortening the preamble;
- dropping the "UMR 0.9" line;
- trimming the list of named-entity types;
- dropping the duplicate idiom sentence and the scorer parenthetical;
- dropping the rarely used `purpose`/`have-condition` constants sentence;
- dropping the named-person example, which repeats the rule in 2.2.

```json
{"summary": "Fix reported-content modal triples (only :quote nodes get author+speaker; nested events author only; 被指/据说 content events conceiver only), add slogan-verb :ARG0 re-entrancy exception, add explicit alignment cases for short repeats/母公司/外星人, update examples; free space by trimming preamble and redundant text.", "edits": [
{"op": "replace", "old": "**Make the annotation as correct as you can**: it is compared node by node and relation by relation with an expert gold annotation. Check every decision against the guidelines, follow the examples, and check each graph (concepts, aspect, role direction, document-level coverage) before moving on.", "new": "Check every decision against the guidelines and examples, and check each graph before moving on."},
{"op": "delete", "old": "UMR 0.9 abridged, for Chinese and English at Stage 1 (numbered PropBank roles), with the names of the UMR release data."},
{"op": "replace", "old": "`publication`, `river`,\n`mountain`, `building`, `airport`, `road`, `event`,", "new": "`publication`, `event`,"},
{"op": "delete", "old": " A fixed four-character idiom is one concept."},
{"op": "delete", "old": " (the scorers move it to the document level)"},
{"op": "delete", "old": " Purpose and condition clauses may use the\n  constants `purpose` and `have-condition` as parents of their events."},
{"op": "delete", "old": "- Named person (2.2): 格内洛索·波普 → `(individual-person :name (name :op1 \"格内洛索\" :op2 \"·\" :op3 \"波普\"))`.\n"},
{"op": "replace", "old": "- Reported speech or thought: `(author :full-affirmative s9p)` for the speaker node, and each content event gets **both** `(author :full-affirmative X)` and `(s9p :full-affirmative X)`. The conceiver is the speaker's entity node, not the reporting verb; with no written speaker (被指) use the whole subject node of the first content event (the `and` if coordinated). The top content node (with `:quote`, even an abstract predicate) gets both `author` and conceiver triples.", "new": "- Reported speech or thought: `(author :full-affirmative s9p)` for the speaker node. Each node carrying `:quote` (the top content node, even an abstract predicate, and a slogan's verb) gets both `(author :full-affirmative X)` and `(s9p :full-affirmative X)`; events nested inside it without their own `:quote` (the subject 报导 of 报导是真实的) get only the `author` triple. The conceiver is the speaker's entity node, not the reporting verb. With no written speaker (被指, 据说: an unverified claim) the conceiver is the whole subject node of the first content event (the `and` if coordinated), and the content events get **only** `(<subject> :full-affirmative X)`, no `author` triple; author still asserts the subject node and 指."},
{"op": "insert_after", "anchor": "(它停止了它的发行 → 发行 `:ARG0` 它).", "text": " Likewise the verb of a quoted slogan whose owner is written (他们的标语：「只报导事实…」) takes that owner as `:ARG0`."},
{"op": "insert_after", "anchor": "node is aligned to the name's words.", "text": " Align every sentence. A shortened repeat (周报) is aligned to its own word; in 母公司美国媒体公司, `公司 :mod 母` → 母公司 and `company` → the name words only; 外星人 before a name → the 外星人 word only."},
{"op": "replace", "old": "conceiver = the `and` subject.", "new": "modal `(author :full-affirmative <and-subject>) (author :full-affirmative 指) (<and-subject> :full-affirmative 有) (<and-subject> :full-affirmative 领养)`, no author triple on 有/领养."},
{"op": "replace", "old": ", likewise each content 报导; slogan → `(identity-91 :aspect state)`.", "new": "; inner subject 报导 only `(author …)`; slogan → `(identity-91 :aspect state)` with `(报导-01 :ARG0 s12n :quote identity-91)` getting both triples."}
]}
```