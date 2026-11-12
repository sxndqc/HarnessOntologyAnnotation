# Review of the annotator's UMR for the 《世界新闻周报》 document: costly error patterns and instruction changes

The annotator was strong on concepts and senses: event concepts 100, senses 100, name tokens 100, other attributes 100. Most of the loss is in five places:
- temporal: F 56
- reentrancy: F 50
- peripheral roles on entities: F 74
- coreference chains: precision 71
- core arguments: F 88–90

The patterns are below, most costly first.

---

## 1. Temporal parents: dependent events anchored to the wrong node (h_temporal, 7 units wrong, partial or extra)

**What went wrong**
- **Sentence 1, 停止.** The annotation had `(document-creation-time :overlap s1x4)`. Gold anchors it to the main event: `(s1x3 :overlap s1x4)`.
- **Sentence 1, 闻名.** The annotation had `(s1x5 :overlap s1x7)`. Gold has `(s1x7 :contained s1x3)`. This is exactly the instruction's own example, and it was not followed.
- **Sentence 4, 继续.** The annotation had `(document-creation-time :overlap s4x4)`. Gold has `(s4x :overlap s4x2)`: the second conjunct of `but-91` hangs on the first.
- **Sentence 2, 综合.** The annotation had `(s1x5 :overlap s2x)`, anchoring it to the previous sentence's event. Gold has `(document-creation-time :before s2x)`.
- **Sentences 4 and 5.** For 停刊 (sentence 4) and 称为 (sentence 5), gold writes `(document-creation-time :depends-on X)`. The annotation used `:before`. This looks like a gold convention for the main event of these sentences. It is less certain to generalise, so mention it only as what the gold data does.

**Why it happens**
- The rule "anchor dependent events to the main event" is stated, but it is not tied to the cases where it applies: a 已经-state modifier, the conjuncts of `but-91` or `and`, a `:reason` event.
- Nothing says that each sentence's main event anchors to `document-creation-time` and not to an event in an earlier sentence. The general rule (2) "an event before it that is a clear reference time" invited the cross-sentence anchoring.

**Change to the instruction.** Add to 5.1:
> "Each sentence's main (root-most) event anchors to `document-creation-time`. Do not anchor it to an event of an earlier sentence unless the text explicitly sequences them (然后, after that). Every other event in the sentence takes an event of the **same sentence** as its parent:
> - modifier states (已经停止) → `(main :overlap x)`;
> - the second conjunct of `and`/`but-91` → `(first :overlap second)`;
> - a 闻名-type state whose reason is the main event → `(state :contained main)`."

Then repeat the sentence 1 example triples verbatim as a mandatory pattern.

## 2. Arguments and reentrancies the text does not express (g_reentrancy: 3 extra; core args: 2 wrong)

**What went wrong**
- **Sentence 1, 已经停止发行的小报.** The annotation had `小报 :ARG0-of (停止-01 :ARG1 (发行-01 :ARG0 小报))`. Gold has:
  `(s1x / 小报 :ARG1-of (s1x3 / 发行-01 :ARG1-of (s1x4 / 停止-01 :mod (s1x6 / 已经) :aspect state) :aspect habitual))`
  The noun is the thing *published* (ARG1 of 发行). The stopping is predicated of the publishing, not done by the paper.
- **Sentence 4, 不过仍继续发行网络版.** The annotation added `:ARG0 s4p` on both 继续-01 and 发行-01. Gold leaves the subject out:
  `(s4x2 / 继续-01 :ARG1 (s4x6 / 发行-01 :ARG1 (s4x7 / 网络版)))`

**Why it happens.** "Add a re-entrant or implicit argument only when the text expresses it" is a single line, and the annotator overrode it with world knowledge. The instruction's own aspect example (`停止-01 ... :mod 已经`) shows no structure, so the annotator invented the ARG0 chain.

**Change to the instruction.**
- Give the full structure for the 已经停止发行的小报 example: "noun modified by [停止 + V]: noun `:ARG1-of` V, V `:ARG1-of` 停止."
- Add: "Do not fill a Chinese zero subject of a second clause (仍继续发行…) by re-entrancy. Leave the role out."

## 3. A modifier shared by coordinated nouns put on the `and` node, and an invented `:subset` (d_peripheral_entity: 6 units; g_reentrancy: 2 missing)

**What went wrong.** For 各式各样奇怪的新闻与专栏 the annotation had:

`(and :op1 新闻 :op2 专栏 :mod 各式各样 :mod 奇怪 :subset s2x9)`

Gold has:

`(s2a2 / and :op1 (s2x4 / 新闻 :mod (s2x6 / 各式各样) :mod (s2x7 / 奇怪)) :op2 (s2x5 / 专栏 :mod s2x6 :mod s2x7))`

The rule about shared modifiers is already in the instruction, and it was not followed. `:subset` is not a UMR role at all. 其中 should be `内容 :mod (s2x11 / 其中)`.

**Change to the instruction.**
- Add the 各式各样奇怪的新闻与专栏 fragment above as an example. It shows that the second conjunct uses re-entrant variables.
- Add: "其中 (among them) → `:mod (其中)` on the noun. Use only roles from the closed list; there is no `:subset`."

## 4. Negation with 未经, and the modal strength of what it scopes over (c_polarity: 1 extra; i_modal: 1 wrong; core args: 1)

**What went wrong.** Gold annotates 未经 as `经-01 :aspect process` **without** `:polarity -`. The negation is carried only by `(author :full-negative s2x8)`. The embedded event 查证 gets `(author :partial-affirmative s2x13)` in gold. The annotator gave it full-negative.

**Change to the instruction.** Extend the existing 未经 line in 4.1:
> "未经 → `经-01`, no `:polarity` in the graph, `(author :full-negative 经)`. An event nominal inside its object (查证) is `(author :partial-affirmative x)`."

**A related gold idiom.** In 新闻查证程序 a procedure noun is named by an event. Gold has `程序 :ARG0-of (identity-91 :ARG1 (查证-01 ...))`. The annotation had `程序 :mod 查证-01`. Add this as an example.

## 5. `identity-91` is not given aspect or modal (c_aspect: 1; i_modal: 1)

**What went wrong.** The instruction says to give `identity-91` no temporal triple. The annotator stretched this to no aspect and no modal triple. Gold has `:aspect state` and `(author :full-affirmative s1i2)`.

**Change to the instruction.** Write in 4.1 and 5.1:
> "`identity-91` and the other abstract predicates take `:aspect state` and a modal triple. Only the **temporal** triple is left out."

## 6. Event coreference across different editions (j_coref_chain: 2 extra)

**What went wrong.** The annotation had `(s1x5 :same-entity s4x5)`, linking 发行 of the paper (sentence 1) with 发行 of the 网络版 (sentence 4). The participants differ, and it used `:same-entity` for events. The instruction's warning covers only 停止.

**Change to the instruction.**
> "A repeated habitual verb with a different object (publishing the paper vs. publishing the online edition) is not `:same-event`. Never use `:same-entity` between events."

## 7. Smaller role and structure errors

- **Coordinated two-noun compounds** (a_entity_found: 2; a_entity_concept: 1). For 奇闻轶事 the annotation had one concept. Gold nests an `and` inside the outer `and`: `(s1a2 / and :op1 (奇闻) :op2 (轶事))`. Add: "a four-character string made of two coordinated nouns, not a chengyu, splits into a nested `and`."
- **"In X's history" with a superlative** (d_peripheral_entity, d_core_args_abstract, e_peripheral_labels). For 美国历史上最… the annotation had `have-degree-91 :ARG5 (历史 :possessor 美国)`. Gold has `报纸 :temporal (s5x8 / 上 :op1 (历史 :place (country 美国)))`. Add this as an example. A country on an abstract noun is `:place`, consistent with the existing 美国小报 rule.
- **曾经** (e_peripheral_labels: 1). The annotation had `:mod`. Gold has `:temporal (曾经)`. Add 曾经 next to 目前 as a `:temporal` modifier. It does not belong with 已经, 都 and 也, which are `:mod`.

## What to keep

These examples and rules worked and produced exact matches:
- the 《》 name tokens;
- 一份 / 一个 as `:quant` + `:unit`;
- 以…而闻名 as `:ARG1-of 闻名 :reason 报导`;
- `but-91 :ARG1/:ARG2`;
- the `have-degree-91` superlative;
- the chengyu as `:mod`;
- 属-02 argument order;
- `:part-of` for 纸本;
- `:medium` for 电视;
- the aspect rules (habitual 发行 and 综合, state for 已经停止, performance for 被称为, process for 未经);
- pronoun and coreference chaining of the newspaper entity.

Keep all of these unchanged, and add the new cases above in the same example-driven style, since the annotator follows concrete fragments far more reliably than general rules.