Most checks were perfect: temporal, modal, coreference, polarity, named entities, event and entity concepts. All of the misses come from three kinds of construction. The costliest one is where the full node of a named entity goes when the entity is mentioned twice in one sentence.

## 1. A named entity mentioned twice in one sentence: full node at the wrong mention, wrong roles around it (most costly)
**Cost:** about 7 units.
- g_reentrancy dropped to 0: one re-entrancy missing, one extra.
- d_peripheral_entity: 3 units (an extra `:possessor`, a wrong `:mod`, a missing `:mod` on the apposition noun).
- The `:part`/`:part-of` edge was also counted wrong.

**What happened:** A periodical is named first as the owner of a component noun inside a change construction ("由 X 改为 Y", where X is a layout or edition of the periodical). It is named again later in the sentence as the possessor of a standard.
- The annotator wrote the full node (name, apposition, modifiers) at the later mention, because that comes first when you walk the graph.
- It then pointed back to the component with an inverse `:part`.
- The gold writes the full node at the first mention in the text, as `:part-of` on the component noun. The later possessor is a re-entrancy.

**Why it happened:**
- The instruction says "first occurrence in reading order", which can be read as graph order.
- The change-verb rule already says "not an inverse `:part`", but the annotator did not apply it. This is probably because the periodical was written somewhere else in the graph.
- A related slip: an attributive word in front of the apposition noun ("旗下的 [modifier] 小报 《N》") was attached to the named entity, not to the apposition noun it modifies in the text.

**Changes:**
- Say plainly: "Reading order" means the order of the words in the sentence, not the order of the PENMAN graph. When the same entity appears twice in one sentence, the full node (name, apposition, all its modifiers) goes at the word-first mention, even if that mention is lower in the graph. Every other mention is a bare variable.
- Repeat in the change-verb rule: the subject is `:part-of` on X even when it also fills a role elsewhere. Never add `:part` from the entity back to X.
- Add: modifiers written before an apposition noun (`的`-phrases, 旗下, property words) attach to the apposition noun inside `identity-91 :ARG2`, not to the named entity.

## 2. Role direction in `have-org-role-91` for a role noun before a name
**Cost:** 2 units (d_core_args_abstract partial, e_core_labels wrong).

**What happened:** The annotator wrote `:ARG0-of` where the instruction's own template says `:ARG1-of`. The rule was there and was not followed. Most likely the "role noun = verb + 人/者" pattern `:ARG0-of (v / verb…)` sat right next to it and its `:ARG0-of` leaked over.

**Change:** In 2.2 and in the checklist, add: "The holder of a title is always `:ARG1` of `have-org-role-91` (`:ARG1-of` on the person). `:ARG0` is never used with `have-org-role-91`/`have-rel-role-92`." Keep the `:ARG0-of` template for the inner verb of a verb + 人 role noun, and present it clearly as a separate case.

## 3. Aspect of a habitual practice named by a process nominal
**Cost:** 1 unit (c_aspect).

**What happened:** A process nominal named a way of producing a publication (printing in a certain manner) and was the subject of "became the publication's feature". The gold marks it `habitual`; the annotator used `process` (step 3).

**Why it happened:** Step 1 lists only "publishing, reporting, compiling, broadcasting". It also does not say that step 1 comes before step 3 for nominals.

**Change:** Widen step 1 to cover any production or distribution activity of a periodical or organisation (printing, issuing, distributing, broadcasting). Say it applies to process nominals too: a nominal naming the routine practice of an entity, especially as the subject of "is or became its feature or trademark", is `habitual`, not `process`.

## 4. Aspect of a relative-clause verb that says what a new publication will hold
**Cost:** 1 unit (c_aspect: gold `process`, annotator `state`).

**Why it happened:** Step 1 says the capacity or content of a publication is "`process` or `state`" and leaves the choice open.

**Change:** Settle it: a verb saying what a publication or container holds or carries (contains, holds, carries articles) is `process`. Keep `state` for plain possession, being and belonging verbs.

## 5. Sense of a verb morpheme split out of a role noun
**Cost:** 1 unit (b_event_sense).

**What happened:** For the inner verb of a verb + 人 role noun, the gold used `-00` even though a PropBank roleset (`-01`) exists for that verb.

**Change (low confidence, it rests on one case):** When the inner verb is split out of a verb + 人/者 role noun and is a bound morpheme, not used as a free verb in the sentence, use `<morpheme>-00`. Check the gold data with `search_annotations` before applying this widely.

## What to keep
The annotator followed these rules exactly, and they gave 100% on their checks:
- The reified `have-reason-91` / `have-purpose-91` nesting for a paired reason/result plus a marked purpose, with author links and no temporal parent.
- The "verb + 量" split with `have-quant-91` and its classifier unit, and no aspect on either.
- The temporal rules:
  - date `:overlap` on the event, and `:before` from `document-creation-time` to an absolute past date;
  - `:era` for a decade;
  - a past participle `:before` the event it modifies (the `(main :before rc-event)` rule);
  - a reason event `:before` its result;
  - a sentence with 也成 linked `:overlap` to the earlier event it continues from;
  - a process nominal `:overlap` with its verb.
- The modal rules: `full-negative` with `:polarity -`, and `author :full-affirmative` on every node that has an aspect.
- Coreference to the closest earlier mention.
- The title marks kept as name ops, the middle dot kept as its own op, no `:wiki`.
- A demonstrative + 刊 written as `刊 :mod 该`.
- The component noun as head with the work as `:part-of` (the 版 的 《N》 rule).
- Adverbs (也, 已经) as `:mod` on the verb.