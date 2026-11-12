**Summary of changes.** Three fixes, one per pattern in the critique. One trim keeps the instruction under the size limit.

1. **Dates anchored to `root` (§5.1).** The instruction itself told the annotator to attach absolute dates to `root`, which gold never does.
   - The rule now says every date depends on `document-creation-time`: `:before` for a past date, `:after` for a future one, `:depends-on` for the present.
   - It says dates are never attached to `root`.
   - The 1979年 example is added next to the existing 1980年代 example.
2. **Full node at the wrong mention.** The first-mention rule existed but was not applied. The likely cause is that have-reason-91 prints the 因为 clause last, as `:ARG2`.
   - A note under the reified skeleton (2.5) says the 因为 clause usually comes first in the text, so its entities get their full nodes there.
   - The Checklist (§7) now has a step to run on every sentence: check which mention comes first by word position.
3. **PropBank argument order.**
   - The warning now covers all Chinese intransitive change verbs (跌-01, 达到-01, 属-02), where the theme is often `:ARG0`.
   - The 量 bullet now says 量 is the `:ARG0` of 达到-01 and 跌-01.
   - A 跌至 example is merged into the existing 量 example.
4. **Trim.** The obsolete `:wiki` explanation is removed, since the instruction already says not to use `:wiki`.

```json
{"summary": "Dates depend on document-creation-time (not root); first-mention full node enforced via 2.5 note and checklist step; general Chinese PropBank ARG0-theme warning and 量 :ARG0 of 达到/跌; examples; trimmed obsolete :wiki note.", "edits": [
{"op": "replace", "old": "**no `:wiki`** (do not add `:wiki` in Chinese documents; the gold has none; ignore the following note on it)\n(the Wikipedia title, or `-` when there is none), and", "new": "**no `:wiki`**, and"},
{"op": "replace", "old": "an absolute date (*1998*) depends on `root`; a relative one (*today, yesterday*,", "new": "a date (absolute or relative) depends on `document-creation-time`, never on `root`: `(document-creation-time :before d)` for a past date, `:after` for a future one; a relative one (*today, yesterday*,"},
{"op": "replace", "old": "- Check the PropBank argument order: for 属-02 the thing owned is `:ARG0` and the owner `:ARG1`.", "new": "- Take numbered roles from the roleset you looked up, not from English habit: Chinese PropBank often makes the theme of an intransitive change verb `:ARG0` (跌-01, 达到-01). For 属-02 the thing owned is `:ARG0` and the owner `:ARG1`."},
{"op": "replace", "old": "The value reached by 达到/跌至/增至 → `量 :ARG1-of", "new": "量 is `:ARG0` of 达到-01 and of 跌-01 (跌至). The value reached by 达到/跌至/增至 → `量 :ARG1-of"},
{"op": "insert_after", "anchor": "If both occur, have-reason-91 is the root and has-purpose-91 is its `:ARG1`.", "text": " The 因为 clause (`:ARG2`, printed last) usually comes first in the text: entities first named there get their full nodes there."},
{"op": "insert_after", "anchor": "- Coreference across sentences is in `:coref`; within a sentence it is a re-entrancy.", "text": "\n- For each entity mentioned twice in a sentence, find its first mention by word position; the full node goes there (even inside the `:ARG2` of have-reason-91), every other mention is the bare variable."},
{"op": "replace", "old": "- Temporal (5.1): 1980年代…创刊 → `(s6d :overlap s6x)`;", "new": "- Temporal (5.1): 创刊于1979年 → `(document-creation-time :before s6d)` `(s6d :overlap s6x)`;"},
{"op": "replace", "old": "- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`.", "new": "- 量 (3): 该刊发行量 → `(f / 发行-01 :ARG1 (k / 刊 :mod (g / 该)))`, no aspect; only `(main :overlap f)`. 发行量跌至8万3千份 → `(d / 跌-01 :ARG0 (l / 量 ... :ARG1-of (h / have-quant-91 :ARG2 83000 :unit (u / 份))))`."}
]}
```