The changes target the recurring patterns in the critique. Because the instruction is within about 520 characters of the limit, every edit is short.

1. **Where an entity's full node goes.** "First occurrence in reading order" now says plainly that it means word order in the text, not graph order. Every other mention is a bare variable.
2. **Change-verb rule.** It now says the subject stays `:part-of` on X even when the subject also fills another role. That other role is a re-entrancy, and no inverse `:part` is added.
3. **Modifiers before an apposition noun.** Modifiers written before the apposition noun (的-phrases, 旗下, property words) attach to that noun inside `identity-91 :ARG2`, not to the named entity.
4. **`have-org-role-91` direction.** The title holder is always `:ARG1` (`:ARG1-of` on the person), never `:ARG0`. The verb + 人/者 pattern is marked as a separate case.
5. **Aspect step 1.**
   - Habitual now covers production and distribution practices (printing, issuing) and process nominals that name a routine practice.
   - It applies before step 3.
   - The open choice "`process` or `state`" for content verbs is settled as `process`.

I did not add the `-00` sense rule for a verb morpheme split out of a role noun. The critique rates it low confidence and it rests on one case.

```json
{"summary": "Clarify full-node placement by text order; part-of in change clauses even when the entity is reused; pre-apposition modifiers go on the apposition noun; have-org-role-91 holder is always ARG1; habitual covers production practices incl. nominals, and content verbs of publications are process.", "edits": [
{"op": "replace", "old": "Write an entity's full node (name, apposition) at its first occurrence in reading order; later mentions are re-entrancies.", "new": "Write an entity's full node (name, apposition, all modifiers) at its first mention in the order of the words of the sentence (text order, not graph order), even when that mention sits deeper in the graph; every other mention is a bare variable."},
{"op": "replace", "old": "the subject is `:part-of` on X, not its own argument and not an inverse `:part`.", "new": "the subject is `:part-of` on X, not its own argument and not an inverse `:part`, even when it also fills a role elsewhere (that role is then a re-entrancy)."},
{"op": "replace", "old": "`:ARG1-of (i / identity-91 :ARG2 <head noun with all its\nmodifiers>)` on the named entity.", "new": "`:ARG1-of (i / identity-91 :ARG2 <head noun with all its\nmodifiers>)` on the named entity; modifiers written before the apposition noun (的-phrases, 旗下, property words) go on that noun, not on the entity."},
{"op": "replace", "old": "`:ARG1-of (h / have-org-role-91\n:ARG3 <role>)`;", "new": "`:ARG1-of (h / have-org-role-91\n:ARG3 <role>)` (the holder is always `:ARG1`, never `:ARG0`); separately,"},
{"op": "replace", "old": "an organisation or periodical publishing,\n   reporting, compiling, broadcasting)? → `habitual`. Only verbs of publishing or reporting; the capacity or content of a\n   publication (contains articles, has N pages) is not habitual (`process` or `state`).", "new": "an organisation or periodical publishing,\n   printing, issuing, reporting, broadcasting)? → `habitual`, also for a process nominal naming such a practice (e.g. subject of\n   \"is/became its feature\"); this step precedes step 3. A verb of what a publication holds or carries (contains articles) is `process`."}
]}
```