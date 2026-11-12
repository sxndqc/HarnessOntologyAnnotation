# Review of the annotator's UMR for the 《世界新闻周报》 document: what in the instruction to change

Most of the lost score is in **temporal** (F 50) and **coreference** (chain P 56, subset P 0). After those come a few local graph errors in sentences 4 and 5. Two of the costliest patterns come from the instruction itself: one of its examples is wrong, and one of its rules is too broad.

## 1. Temporal anchoring: the wrong main event, and a wrong example (h_temporal, about 8 units)

**What went wrong.**
- **Sentence 1** (是…已经停止发行的…小报，以报导…而闻名):
  - The root is `identity-91`, so the annotator had no verbal main event. It anchored two events to the document creation time (DCT): `(document-creation-time :overlap s1x5 停止)` and `(document-creation-time :overlap s1x7 闻名)`. It also hung 报导 from 闻名.
  - Gold anchors the first real event, 发行, and hangs everything else from it: `(document-creation-time :before s1x3 发行) (s1x3 :overlap s1x4 停止) (s1x7 闻名 :contained s1x3) (s1x3 :overlap s1x8 报导)`.
  - That is 4 units in one sentence.
- **Sentence 4** (目前…纸本已经停刊，不过仍继续发行网络版):
  - Annotation: `(document-creation-time :depends-on s4x 目前) (s4x :overlap s4x2 停刊)`.
  - Gold: `(document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`. 目前 gets **no** temporal parent.
  - The instruction's own example, "目前…发行…网络版 → `(document-creation-time :depends-on s4x) (s4x :overlap s4x2)…`", was clearly copied from this gold. But it misread `s4x` as 目前; in gold it is the event 停刊. The rule in 5.1 ("a relative time word such as 目前 … attached as `(document-creation-time :depends-on <node>)`") was built on that misreading. The annotator followed it faithfully.
- **Sentence 5**: gold has `(document-creation-time :depends-on s5x 称为)`; the annotation has `:before`. This is the same pattern as sentence 4: in these sentences gold links the main event to DCT with `:depends-on`.
- **Sentence 2**: 查证 was attached to 综合. Gold attaches it to its governing event: `(s2x8 经 :overlap s2x13 查证)`. The instruction already says "normally their governing event". The annotator did not follow it here.

**Changes to the instruction.**
- **Fix the example** to: `目前…停刊…继续发行 → (document-creation-time :depends-on s4x 停刊) (s4x :overlap s4x2 继续) (s4x2 :overlap s4x6 发行)`.
- **Rewrite the 目前/现在 rule**: "A relative time word such as 目前 or 现在 is a `:temporal` node in the graph but gets no temporal parent of its own. Link the main event of its clause to `document-creation-time` with `:depends-on`, then chain the other events from that main event with `:overlap`."
- **Add a rule for copular sentences**: "When the root is an abstract predicate (`identity-91`, `have-mod-91`), anchor to DCT the first event inside it, usually a relative-clause event such as 发行. Hang every other event from that event: an end verb (停止) `:overlap`; a reputation or state that holds within it (闻名) `:contained`; a co-occurring activity (报导) `:overlap`. Do not anchor more than one event of a sentence to DCT."
- **Stress the governing-event rule**: "An event that modifies a noun hangs from the event whose argument that noun is (查证 in 程序 → 经), not from the sentence's first event."

## 2. Too many coreference and subset links (j_coref_chain 4 extra units, j_coref_subset 1 extra)

**What went wrong.**
- `(s1x4 :same-event s4x6)`: 发行 in sentence 1 is the publication that stopped; 发行 in sentence 4 is the still-continuing publication of the online edition. These are different events.
- `(s2x9 :same-entity s5x9)`: 许多内容 (much of the content, not verified) and 荒诞不经的内容 (its absurd content) are different sets.
- `(s2x9 :subset-of s2a2)`: a within-sentence `:subset-of` link, which gold does not use.

**Why.** Section 5.3 tells the annotator to link mentions but gives it no reason to hold back, so it linked repeated words.

**Change.** Add: "Link two mentions only when they pick out the same individual or the same single event. Do not link two mentions of the same verb that have different arguments, times or polarity (发行 of the print edition vs 发行 of the online edition). Do not link two noun phrases with the same head but different restrictors (许多内容 vs 荒诞不经的内容). Do not put a `:subset-of` triple inside one sentence. When in doubt, leave the link out: the newspaper chain (周报 / 该周报 / 《世界新闻周报》) is the kind of chain gold annotates."

## 3. The "已经 + end verb = state" rule was over-applied (c_aspect 1 unit; it also cost the 停刊 temporal unit)

**What went wrong.** In sentence 4, 已经停刊 is a main predicate. The annotator gave it `:aspect state`; gold has `:aspect performance`.

**Why.** The 4.1 cue was meant for sentence 1's relative clause (已经停止发行的小报), where `state` is right. The annotator applied it to a main predicate.

**Change.** Narrow the cue: "only when 已经 + 停止/停刊 sits in a relative clause that describes an entity (…的 N). As the main predicate, 已经 + an end verb is `performance`."

## 4. Roles invented or mislabelled in sentence 4 (d_core_args / e_core_labels / d_peripheral / g_reentrancy, about 6 units)

**What went wrong.**
- 纸本 of 停刊: annotation `:ARG1`; gold `:ARG0`.
- 《世界新闻周报》的纸本: annotation `:possessor`; gold `(纸本 :part-of (newspaper …))`.
- The annotator added `:ARG0 s4n` to 发行-01, but the text gives no subject. Gold has `(发行-01 :ARG1 (网络版) :aspect habitual)` only.

**Changes to the instruction.**
- Add: "An edition, version or part of a publication or organization (纸本, 网络版, 分部) takes `:part-of` its whole, not `:possessor`."
- Add: "For a `-01` sense of an intransitive verb that is not in PropBank (停刊, 停业), the sole participant is `:ARG0`."
- Repeat the existing rule with this case: "Do not fill the subject of a second clause with an entity from the first clause (…，不过仍继续发行网络版 has no `:ARG0`)."

## 5. Superlative scope and concept form in sentence 5 (a_event_concept 1, a_entity_found 1, d_core_args_abstract 1, d_peripheral 1, c_aspect 1)

**What went wrong.**
- 称为: the annotator wrote `称-01`; gold has `称为-01`. A Chinese concept should keep the verb as written.
- 美国历史上: the annotator made it `:ARG4` of `have-degree-91`. Gold has `(报纸 :temporal (上 :op1 (历史 :place (country …))))`.
- `have-degree-91` was given `:aspect state`. Gold gives it no aspect.

**Changes to the instruction.**
- Add: "Keep compound verbs whole (称为 → `称为-01`, not `称-01`)."
- Add: "A 在/…上 frame such as 历史上 is `:temporal (上 :op1 (历史))` on the noun. It is not `:ARG4` of `have-degree-91`."
- Add: "`have-degree-91` gets no `:aspect`." Gold annotations generally treat it as an abstract predicate with no aspect; this sentence is an example.

## 6. Smaller items (about 1–2 units each)

- **The `identity-91` root needs a modal triple.** Gold has `(author :full-affirmative s1i2)`. Add: "In the modal list, the root abstract predicate of an asserted sentence gets `(author :full-affirmative …)`, even though it gets no temporal parent." The temporal rule ("Copular abstract predicates … normally get **no** temporal parent") is right; keep it.
- **程序 with an event-noun modifier.** 新闻查证程序 in gold is `(程序 :ARG0-of (identity-91 :ARG1 (查证-01 …)))`, not `:mod 查证-01`. Add a line: when an event noun names what the head noun *is* (the procedure is the verification), use `identity-91`.
- **未经 in gold has no `:polarity -` and has aspect `process`, while its modal is `full-negative`.** Other gold sentences (未被录取, 并未受伤) do use `:polarity -` together with full-negative. So this one is a gold quirk. Keep the current polarity rule.

## What the instruction should keep

The annotator got these right, and the matching rules should stay as they are:

- **Named entities**: bracketed names split into words with 《 》 as their own `:opN`, no `:wiki`, `newspaper` as the type, and 美国 as `:place` on 小报. f_name_tokens scored 100.
- **Classifiers** as `:quant` + `:unit` (一份 → 份, 一个 → 个).
- **以…而闻名** as `(闻名-01 :reason 报导-01)` with no extra `and`.
- **Lexical verbs** used instead of abstract predicates: `属-02` and `拥有-01` rather than `belong-91` / `have-91`.
- **Superlatives**: `have-degree-91 :ARG3 (最)`.
- **Adverbs**: 已经, 都, 也, 仍, 其中 as `:mod`, and 曾经 as `:temporal`.
- **Shared modifiers** on coordinated nouns written by re-entrancy on each conjunct (各式各样 and 奇怪 on both 新闻 and 专栏).
- **Habitual aspect** for a publication's recurring activities (发行, 报导, 综合).
- **The newspaper coreference chain** (s1n → s2x2 → s3x2 → s4n → s5x2) and the `:medium` and `:duration` roles. Event senses scored 100.