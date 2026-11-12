The annotation is very close to gold. Every concept, sense, aspect, polarity, modal triple and coreference link matches. All the lost points come from three patterns, listed most costly first.

---

## 1. A newspaper named twice in one sentence got its full node at the wrong mention (g_reentrancy fell to F 0; d_peripheral_entity lost 2 units)

**The error.** In sentence 7, 《国家询问报》 appears twice:
- first in the text at words 10–14, in the 因为 clause (…小报《国家询问报》将由黑白版面改为彩色版面);
- again at words 48–53 (不符合《国家询问报》标准).

The annotator put the full node (name plus the appositive identity-91 小报) under the second mention, the one with 标准. In the 改为 clause it left only the bare variable:

- Annotation: `改为-01 :ARG1 (s7b2 / 版面 :part-of s7n3 …)` … `(s7s / 标准 :possessor (s7n3 / newspaper :name … :ARG1-of (s7i / identity-91 :ARG2 (s7x / 小报 …))))`
- Gold: `改为-01 :ARG1 (s7x4 / 版面 :part-of (s7n / newspaper :name (…"国家" "询问" "报"…) :ARG1-of (s7i2 / identity-91 :ARG2 (s7x5 / 小报 :mod 旗下 :mod 八卦))) :mod 黑白)` … `(s7x21 / 标准 :possessor s7n)`

Because of this, the judge counted the re-entrancy on the wrong edge: one missing and one extra re-entrancy. It also counted a missing `:part` edge and an extra `:possessor` edge.

**Why it happens.** The instruction already has the rule ("write its full node … at its first mention in the text … even if the later mention comes first in the graph") and a worked example ("First mention (3)") for exactly this sentence. The annotator still didn't follow it. The likely reason: have-reason-91 puts the 因为 clause last, as `:ARG2`. When the annotator writes the graph top-down, the 标准 mention inside `:ARG1` comes first in the graph, and it writes the full node at the first place it meets the entity.

**What to change.**
- Put the rule in the Checklist (§7) as a step to run on every sentence: "For each entity that occurs twice in one sentence, find which mention comes first by word position. The full node goes there, even when it is the `:ARG2` of have-reason-91 and is printed last. Every other mention is the bare variable."
- Add a short note under 2.5 (reified skeleton): "The 因为 clause (`:ARG2`) is usually first in the text. Entities first named there get their full nodes there."

## 2. Absolute dates were anchored to `root` (h_temporal lost 3 units)

**The error.** In sentences 6, 9 and 10 the annotator wrote:
- `(root :depends-on s6d)` for 1979年;
- `(root :depends-on s9t)` for 1980年代;
- `(root :depends-on s10t)` for 2007年.

Gold has `(document-creation-time :before s6d)`, `(document-creation-time :before s9d)` and `(document-creation-time :before s10d)`.

**Why it happens.** The instruction itself is wrong here. §5.1 says "an absolute date (*1998*) depends on `root`", and the annotator followed it exactly.

**What to change.** Replace that sentence with: "A date (absolute or relative) depends on `document-creation-time`: `(document-creation-time :before d)` for a past date, `:after` for a future one, `:depends-on` for today or a date containing the DCT. Do not attach dates to `root`." Then add an example: 创刊于1979年 → `(document-creation-time :before s6d)` `(s6d :overlap s6x)`.

## 3. Wrong numbered role for 跌-01 (d_core_args_event and e_core_labels, 1 unit each)

**The error.** In sentence 10 (该刊发行量已经跌至…), the annotation has `(s10d / 跌-01 :ARG1 (s10l / 量 …))`. Gold has `:ARG0 (s10x2 / 量 …)`.

**Why it happens.** In Chinese PropBank, 跌-01 has ARG0 = theme and ARG1 = range (its example: 美元汇率 微跌 → ARG0). The annotator assumed the English pattern, where the thing that falls is ARG1, and didn't apply the roleset it should have looked up. The instruction warns about argument order only for 属-02. Its 量 note says what the value is ("not a numbered argument of the verb") but not which role the subject takes.

**What to change.**
- Make the PropBank warning general: "Chinese PropBank often makes the theme of an intransitive change verb `:ARG0` (跌-01, 达到-01, 属-02). Take the role from the roleset you looked up, not from the English habit of making the patient ARG1."
- Extend the 量 bullet: "The 量 node is `:ARG0` of 达到-01 and of 跌-01 (跌至 → 跌-01)."
- Add the example: 发行量跌至8万3千份 → `(d / 跌-01 :ARG0 (l / 量 :quant-of … :ARG1-of (h / have-quant-91 :ARG2 83000 :unit (u / 份))))`.

---

## What to keep (all scored 100)

- **Reified skeleton for 因为…为…于是:** have-reason-91 as root, with have-purpose-91 as its `:ARG1`, and `:aspect state` plus a full-affirmative modal triple on both.
- **Agent noun:** 创始人 → `人 :ARG0-of 创始-00`, with no aspect or modal triple on have-org-role-91.
- **Publication part and its relative clause:** 版面 `:part-of` the newspaper, and 容纳-01 as `:ARG0-of` 版面 with `:aspect process`.
- **Appositive:** the named newspaper gets `:ARG1-of identity-91`, keeping both modifiers (旗下, 八卦) on the noun.
- **发行量:** `量 :quant-of 发行-01` with no aspect, the value through have-quant-91 + `:unit 份`, and only the `(main :overlap 发行)` triple.
- **Event noun:** 印刷-01 `:manner 黑白`, `:aspect habitual`, with `(prev-main :overlap 成)` for 也成了.
- **Smaller points:** the 1980年代 decade as `:era 1980`; no node for 至; no but-91 for a sentence-initial 不过; 已经 as a `:mod` node.
- **Common-noun mentions:** 该刊 → `刊 :mod 该`, linked by coreference to the named mention.
- **Within-sentence temporal links:** `(创立 :before 改为)`, `(运用 :before 遗留)`, and the purpose clause and relative clauses as `:overlap` of the main event.

All of these rules and examples should stay in the instruction unchanged.