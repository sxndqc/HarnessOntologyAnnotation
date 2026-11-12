# Review of the annotation of sentences 11–15: error patterns, causes and instruction changes

Concepts, event arguments, named-entity structure and most attributes were nearly perfect. Most of the lost score is in the document-level relations: temporal F 51, modal F 77, reentrancy F 78 and coref F 80. One naming case also cost several units across checks. The patterns are listed below, most costly first.

---

## 1. Temporal anchoring of a defunct paper's claims, habits and evaluations (h_temporal: about 8 of 15 units wrong, missing or extra)

**What went wrong**

- **Sentence 12, 宣称:** the annotation had `(document-creation-time :depends-on s12x)`. Gold has `(document-creation-time :before s12x)`.
- **Sentence 14, 算是:** the same mistake. The annotation had `:depends-on`; gold has `(document-creation-time :before s14x)`.
- **Sentence 13, 经常报导 (s13b):** the annotation had `(document-creation-time :overlap s13b)`. Gold has `:before`, because the paper stopped printing in 2007 (sentence 11), so its habits are past.
- **Sentence 13, second conjunct 创造:** the annotation anchored it to the document-creation time with `(document-creation-time :before s13c)`. Gold anchors it to the first conjunct: `(s13x2 :overlap s13x)`.
- **Sentence 12, quoted content:** the annotation gave the reported `have-mod-91` a parent, `(s12x :overlap s12h)`, and hung the 报导 events from it or from 宣称. Gold gives s12h no temporal parent. It puts the inner 报导 under the reporting verb, `(s12x :overlap s12x4)`, and the other 报导 events under that 报导: `(s12x4 :overlap s12x6)` and `(s12x4 :overlap s12x10)`.

**Why it happens**

- The instruction says to use `:depends-on` for "a current state, or a naming or evaluation that still holds". The annotator stretched this to every claim (宣称) and every evaluation (算是). Nothing in the instruction says that a document about a paper that has already ended is narrated in the past.
- The rule "-91 predicate … no temporal triple" exists, but it is worded for main or conjoined clauses. The annotator did not apply it to the -91 node that is the content of a reporting verb.
- The rule on second conjuncts exists, but was not followed for `and`.

**What to change**

- Add: *"Once the document has placed its topic in the past (the paper stopped in 2007), its claims (宣称), habits (经常报导) and the author's evaluations of it (算是) are `(document-creation-time :before X)`. Use `:depends-on` only with an explicit present marker (目前, 现在) or for a naming that is still in force (被称为)."*
- Add: *"A -91/-92 node that is the content (`:ARG1`) of a reporting verb gets no temporal triple. The first event inside it takes the reporting verb as parent. Further events of the same sentence on the same topic (other 报导) take that event as parent."*
- Make the conjunct rule explicit: *"In `(and :op1 A :op2 B)`, B's parent is A: `(A :overlap B)`. It is never the document-creation time."*

## 2. Modal triples for reported content (i_modal: 6 units, in sentences 12 and 15)

**What went wrong**

- **Sentence 12:** gold gives the content events **both** an author triple and a speaker triple: `(author :full-affirmative s12h)`, `(s12n :full-affirmative s12h)`, and likewise for s12x6 and s12x10. The event nested inside the claimed state (s12x4) gets only `(author :full-affirmative s12x4)`. The annotator gave each of these events a single parent, and for s12x10 it left out the newspaper triple.
- **Sentence 15, 被指 with no named accuser:** gold uses the subject node s15a as the conceiver: `(author :full-affirmative s15a)`, `(s15a :full-affirmative s15x3)` and `(s15a :full-affirmative s15x2)`. The annotator used the event 指 as the conceiver (allowed by the instruction's own "speaker" definition). This looks like a gold quirk; do not over-invest in it.

**Why it happens:** the instruction says "the author is certain of the speaker, the speaker of the content". That reads as one parent per event.

**What to change**

- State that, as gold does, the content events of a claim (and the events of the adversative clause that goes on talking about what the speaker reports, like 大部分的报导 here) get **both** `(author :full-affirmative X)` and `(speaker :full-affirmative X)`.
- State that an event nested inside a claimed -91 state gets only the author triple.

## 3. A name with a category noun inside a list of characters (about 10 units: a_entity_concept, a_granularity ×4, f_name_tokens ×2, c_other_attributes ×3, plus 2 extra coref)

**What went wrong:** in sentence 13, 虚拟人物如蝙蝠男孩、外星人P'Lod, the annotator wrote `(外星人 :name (name :op1 "P" :op2 "'" :op3 "Lod"))`. Gold has:

```
(s13i3 / individual-person :name (s13n2 / name :op1 "外星人" :op2 "P" :op3 "'" :op4 "Lod"))
```

In sentence 15 (与外星人P'Lod有暧昧关系), gold does use `外星人 :name …`, which is what the instruction's example shows. Because the two mentions in gold have different types, gold does not link them. The annotator's `(s13x16 :same-entity s15x3)` was therefore scored as extra, and coref precision fell to 67.

**Why it happens:** the instruction's 2.2 rule and its 外星人 P'Lod example cover only the sentence 15 context.

**What to change:** add a sentence to 2.2: *"When the named entity is listed as an `:example` of 人物 or characters (如蝙蝠男孩、外星人P'Lod), it is `individual-person`, and the category noun becomes the first name token (`:op1 "外星人"`). In other contexts, keep `外星人 :name`."* This also removes the cross-type coref link.

## 4. Leaving 等 out of lists (a_entity_found: 2 missing)

**What went wrong:** in sentence 13, both lists ended in 等, and the annotator gave 等 no node. Gold has `:op6 (s13x10 / 等)` and `:op3 (s13x20 / 等)`.

**What to change:** amend the rule "N 有 A、B…等 → N :example (and …)" to say that *"等 closing a list is the last `:opN` of the `and`, as a concept `等`."*

## 5. Where `:quote` goes when the content is a connective (g_reentrancy: 3 units)

**What went wrong:** in sentence 15, the annotator put `:quote s15z` on the `consecutive` node. Gold puts it on each conjunct event: `(有-03 … :quote s15x)` and `(领养 … :quote s15x)`.

**What to change:** add *"If the content of 指/说/宣称 is an `and` or `consecutive`, put `:quote` on each event conjunct, never on the connective."*

## 6. Smaller attribute and role slips (about 6 units)

- **Aspect of 宣称 (sentence 12):** the annotation had `activity`; gold has `performance`. Add to 4.1: a single claim or announcement is `performance`.
- **Aspect of 活动 (sentence 14):** the annotation had `habitual`; gold has `activity`. The habitual rule is for the habits of a person or institution. Add that a generic topic noun such as "aliens' activities on Earth" is `activity`.
- **前 in 美国前第一夫人 (sentence 15):** the annotation attached `:mod 前` to `have-rel-role-91`. Gold has `(第一夫人 :mod (前) :place country)`. Add this to the 第一夫人 line in 2.3.
- **Extra `:ARG0 s12p` on 他们的报导 in the claim (sentence 12):** gold has none, which cost one reentrancy unit. This is consistent with the instruction's checklist ("no argument the text does not express"). Reinforce it: 他们的 on an event noun inside a claim adds no ARG0.
- **仍 and 都 nodes:** sentence 11 仍 with 继续 is an extra node. In sentence 12, 都 before 以…为目的 is an extra node; gold drops 都 there but keeps the 都 of 都是真实的. Gold also re-enters the clause-initial date on the second clause (`继续 :temporal s11d`).
  - Replace "never drop 仍" with: *"仍 next to 继续 gets no node. A sentence-initial date shared by both clauses is re-entered as `:temporal` on the second clause too."*
  - Note that the 以X为目的 example already shows no 都.
- **have-degree-91 roles in 其中最大宗 (sentence 14):** gold here has `:ARG1 大 :ARG2 最`, which contradicts the instruction's own 最富创意 example (`:ARG2` property, `:ARG3` 最). Only 2 units are at stake. Leave the general rule alone and, at most, add a note for 其中最大宗.
- **领养-01 vs 领养-00:** PropBank does have 领养-01, so the annotator was right. Gold's `-00` is a gold quirk; make no change.

## What to keep

- The reified skeletons: but-91 with the 虽然…不过 structure, and `identity-91` for the slogan and for 以博君一笑为目的.
- The appositive `company :ARG1-of identity-91 (公司 :mod 母)`.
- Names with 《 》 and · as name tokens; `planet` for 地球.
- `发行-01 :aspect process` under 停止.
- `implicit-argument :unit 宗` with `:ARG5 其中`; `have-rel-role-91` for 第一夫人.
- `consecutive` for 后来.
- The sentence 11 temporal chain: date → 停止 → the other events.
- The coref chain for the paper (周报 / 他们).
- `:modal-strength neutral-affirmative` for 可 算是.

All of these matched gold and should stay as they are.