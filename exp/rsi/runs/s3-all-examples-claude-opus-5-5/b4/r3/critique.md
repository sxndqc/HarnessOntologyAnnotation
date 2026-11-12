Overall the annotation is close to gold. Event detection, named-entity tokens, coreference chains and document format all scored 100. Most of the lost units come from seven small, repeatable patterns, listed below from most to least costly.

## 1. A verb that modifies a noun was left as a bare `:mod` (合成照片): about 7 units
**Checks hit:** sense, aspect, core args, peripheral entity, 2 temporal, 1 modal.

- **The case:** in snt16, 合成 照片 ("composite photo").
- **Annotation had:** `(s16h / 照片 :mod (s16s / 握手-01 …) :mod (s16c / 合成))`, so 握手 took 注销 as its temporal parent.
- **Gold has:** `(照片 :ARG1-of (s16x11 / 合成-01 :aspect performance) :mod (握手-01 …))`, with the triples `(注销 :overlap 合成-01)`, `(合成-01 :overlap 握手-01)` and `(author :full-affirmative 合成-01)`.
- **Why it happens:** the instruction makes only *adjectives* with a roleset (真实, 显著) into events before a noun. Nothing covers a transitive *verb* used before a noun, so the annotator treated it like the "plain modifier" case. 合成-01 does exist in PropBank (ARG1 = the thing synthesised). Once 合成 became a `:mod`, the chaining rule ("the first modifier takes V, each further one the previous modifier") put 握手 on the wrong parent.
- **Change:** add to 2.1: "A verb with a roleset placed directly before a noun whose result or patient is that noun (合成照片, 复制人) is an event: `N :ARG1-of (V-01)`. Use `:aspect performance` when the thing was already produced, and give it a temporal and a modal triple. It counts as the first modifier event in the chaining rule." Also add 合成照片 as an example.

## 2. Roles taken from habit, not from the roleset (刊登 在显著位置): 3 units
**Checks hit:** core arg, peripheral, label.

- **Annotation had:** `:place (s18w / 位置 …)`.
- **Gold has:** `:ARG1 (位置 :ARG0-of (显著-01 …))`.
- **Why:** PropBank 刊登-01 defines ARG1 as the location and ARG2 as the thing published. The annotator looked up the roleset correctly for ARG2 but still turned 在 X into `:place`.
- **Change:** extend the line "Take numbered roles from the roleset you looked up" to: "If the roleset has a location or place argument (刊登-01 ARG1, 在报纸刊登), a 在…-phrase fills that numbered role, not `:place`."

## 3. The speaker was made conceiver of a 报导 that reports no content (snt19): 2 modal units
- **Annotation had:** `(author :full-affirmative s19p) (s19p :full-affirmative s19b)`.
- **Gold has:** only `(author :full-affirmative s19x)`, with no modal triple on the person.
- **Why:** 5.2 says "A publication or person conceives its own reporting verbs (报导, 指, 注销, 宣称)" without restriction. Here the object of 报导 is a headline-publication (`publication :name`), not reported content. In snt16, where 报导 does introduce reported content, the annotator's speaker-conceiver structure was correct.
- **Change:** limit the rule: "only when the verb's ARG1 is reported content (a clause, marked with `:quote`). When the object is a `publication :name` headline or an article noun, write `(author :full-affirmative V)` and give the speaker no modal triple."

## 4. Wrong roleset sense where the PropBank frame is defective or the meaning differs: 2 units
- **The cases:** in snt16, 注销 → gold `注销-00`, and 背书 → gold `背书-00`.
- **Annotation had:** `注销-01` and `背书-01`.
- **Why:**
  - 背书-01 in PropBank has an empty ARG0 and no examples, so it is a defective frame.
  - 注销-01 means deregistering or cancelling (example: 注销 该公司), but here the word means "ran / printed (a photo)".
  - The instruction says "use the roleset if it exists".
- **Change:** "If the roleset's arguments are empty, or its meaning (as shown by its examples) does not fit the word's use in the sentence, use `<word>-00`."

## 5. Placement of `:quote` with 报导「…」: 2 reentrancy units
- **Annotation had:** `支持-01 :quote s16b`.
- **Gold has:** `:quote s16x` on 报导-01 itself (a self-reference), and no `:quote` on 支持.
- **Under 指 in the same sentence:** the annotator followed the existing rule (content events carry `:quote 指`) and matched gold.
- **Change (optional, since this looks like a gold convention):** "When the reported content is a quoted 「…」 clause directly after 报导, put `:quote` on the reporting verb itself (`报导-01 :quote <its own variable>`), not on the content events. For content without 「」 (指…), keep `:quote` on each content event."

## 6. 全世界 written as one concept: 2 units
- **Annotation had:** `(s18q / 全世界)`.
- **Gold has:** `(世界 :mod (全))`.
- **Change:** add next to the 一些/许多 rule: "A quantifier prefix 全/整/各 + noun (全世界, 全国) splits into the noun with `:mod (全)`."

## 7. Temporal parent of conjuncts in an argument-level `and`: 1 unit
- **The case:** in snt17, 荒谬与可笑 is the ARG1 of 点出.
- **Annotation had:** `(荒谬 :overlap 可笑)`.
- **Gold has:** `(点出 :overlap 可笑)`.
- **Why:** the rule "In `(and :op1 A :op2 B)`, B's parent is A" is stated without restriction.
- **Change:** limit it to clause-level coordination (the root `and` or conjoined clauses). "When the `and` is an argument of an event, each conjunct takes that event as parent."

## Not worth chasing
- Gold's snt19 `也 :unit 篇 :quant 1` (3 units) duplicates the publication's 篇 onto 也, so it looks like a gold error. Do not add a rule for it.
- The granularity "extra" on the snt18 publication is a matching artefact: gold also has the publication node.

## Keep (these worked)
- **Headline publications:** `publication :name` with every mark as an `:opN`, plus `:quant 1 :unit 篇`. All name tokens were correct.
- **Named election as time:** `event :name` 2000年总统大选 used as `:temporal`, with no triple.
- **Structure of 有能力 + VP:** 有-06 → identity-91, with `neutral-affirmative` on the VP and `full-affirmative` on identity-91.
- **Example and purpose skeletons:** the 如… skeleton (have-example-91 / implicit-predicate) and the 为了 X，S skeleton (have-reason-91, X `performance`, subject re-entered as ARG0).
- **Snt20 structure:** 新闻 head with `:part-of 刊`, identity-91 → publication with `:aspect state` and an author triple, `墙上 :place-of 记者团`, `building :name` 美国 参议院, and 者 `:ARG0-of 好事-00`.
- **Reported past event:** `(指 :before 当选)`, and the `:quote` on the nested `:reason` under 指.
- **Coreference:** repeated mentions of the paper (周报, 它, 他们, 该刊) were linked with `:same-entity`, and the chain scored 100.