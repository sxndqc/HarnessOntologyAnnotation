The critique's misses come from a few narrow rules. Three of them were caused by the instruction's own wording or examples (曾经, 停刊-00, `:part-of`). Here are the edits:

1. **曾经 and 已经 (5.1).** They are graph nodes only: they get no temporal parent, and no event hangs from them. A past event marked by 曾经 or 过 goes `:before` from `document-creation-time`.
2. **Stative verbs (4.1).** 拥有, 有, 属 and 是 stay `state` even with 过, 了, 曾经 or 短暂.
3. **Negation (4.2).**
   - 未经 / 没有经过 X gives `经-01` without `:polarity`; the negation is expressed only by `(author :full-negative …)`.
   - A negated event never gets `performance`.
4. **停刊 (2.1 and 3).** 停刊 is `停刊-01`, so the rule and the example are corrected. The annotator should look a verb up before falling back to `-00`.
5. **Editions (3).** An edition takes `:part-of` only when its whole is written with it.
6. **Root abstract predicate (2.3).** A root `identity-91` or `have-*-91` gets `:aspect state`. One embedded in a noun phrase, and `have-degree-91`, get no aspect.
7. **Naming clauses (5.1).** A naming or reputation main event (被称为) is linked as `(document-creation-time :depends-on …)`.
8. **Usual procedures (5.2).** A narrow modal rule: an event nominal naming a usual procedure under a negated event is `partial-affirmative` from the author.

The Examples section is updated to match.

```json
{"summary": "Fix 曾经 temporal handling and stative aspect with 过; no :polarity on 未经 and no performance for negated events; 停刊-01 not -00; :part-of only with an expressed whole; :aspect state on root abstract predicates; :depends-on for naming clauses; partial-affirmative for usual-procedure nominals under negation; update examples.", "edits": [
{"op": "replace", "old": "a Chinese predicate that is not\nin PropBank is `<word>-00`.", "new": "a Chinese predicate that is not\nin PropBank is `<word>-00` — look the verb up first; many verbs that look rare have a sense (停刊-01)."},
{"op": "replace", "old": "`have-degree-91` gets no `:aspect`.", "new": "`have-degree-91` gets no `:aspect`. A root `identity-91` / `have-*-91` (the sentence's main predicate) takes `:aspect state`; an `identity-91` inside a noun phrase (程序 :ARG0-of identity-91) takes none."},
{"op": "replace", "old": "- An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor`.", "new": "- An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor` — but only when the whole is written with it (《…》的纸本). A bare 网络版 gets no `:part-of`."},
{"op": "replace", "old": "- For an intransitive Chinese verb not in PropBank (停刊, 停业), the sole participant is `:ARG0`.", "new": "- For an intransitive Chinese verb such as 停刊-01 (or a `-00` verb not in PropBank), the sole participant is `:ARG0`."},
{"op": "replace", "old": "Passive naming (被称为) is `performance`.", "new": "Passive naming (被称为) is `performance`. Possession and other stative verbs (拥有, 有, 属, 是) stay `state` even with 过, 了 or 曾经, and even when limited by 短暂. A negated event (未, 没) never gets `performance`; use `process` when its type cannot be told."},
{"op": "replace", "old": "- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is\n  then negative (5.2).", "new": "- Negation: `:polarity -` on the negated concept (没, 不, 未, *not, never*); the event's modal strength is\n  then negative (5.2). Exception: 未经 X / 没有经过 X → `经-01` with no `:polarity`; the negation is only the modal triple `(author :full-negative 经)`."},
{"op": "insert_after", "anchor": "then chain the other events from that main event with `:overlap`.", "text": "\n- 曾经 and 已经 are graph nodes only: they get no temporal parent and no event hangs from them. A past event marked with 曾经 or 过 is `(document-creation-time :before <event>)`; chain the sentence's other events from it with `:overlap`.\n- The main event of a naming or reputation clause (被称为, 被誉为) is `(document-creation-time :depends-on <event>)`, as with 目前."},
{"op": "insert_after", "anchor": "- A conceiver that is not in the text is `null-conceiver`.", "text": " An event nominal naming a usual procedure (一般的…程序) under a negated event is `(author :partial-affirmative <nominal>)`."},
{"op": "replace", "old": "- Aspect (4.1): main predicate 纸本已经停刊 → `(停刊-00 :ARG0 (纸本 :part-of (newspaper …)) :aspect performance)`.", "new": "- Aspect (4.1): main predicate 纸本已经停刊 → `(停刊-01 :ARG0 (纸本 …) :aspect performance)`; 继续发行网络版 → bare `(网络版)`, no `:part-of`.\n- 曾经 + 过 (4.1, 5.1): 也曾经短暂的拥有过一个节目 → `(拥有-01 :temporal (曾经) :aspect state)`, `(document-creation-time :before 拥有) (拥有 :overlap …)`; 曾经 has no temporal parent.\n- Negation (4.2): 都未经一般的新闻查证程序 → `(经-01 :mod (都) :aspect process)` without `:polarity`; modal `(author :full-negative 经) (author :partial-affirmative 查证)`.\n- Root copula (2.3): 是…小报 → `(identity-91 :ARG1 … :ARG2 … :aspect state)`.\n- Naming (5.1): 被称为… → `(document-creation-time :depends-on 称为)`."}
]}
```