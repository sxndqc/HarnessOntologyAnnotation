Below are the error patterns, most costly first. For each one: the cost, why it happened, and what to change in the instruction.

## 1. 他们 standing for the newspaper became a new `person` node
**Cost:** the biggest single loss. It accounts for most of j_coref_chain (F 13) and adds 2 units each in a_entity_found, g_reentrancy and d_core_args, plus temporal and modal parents tied to that node.

**Examples:**
- snt12 他们的报导 / 他们的标语
  - Annotation: a new `(s12p / person :refer-person 3rd :refer-number plural)`, used as `:ARG0` of 报导 and as `:possessor` of 标语.
  - Gold: no `:ARG0` on the first 报导 (`(s12x4 / 报导-01 :aspect habitual)`), and `(s12x5 / 标语 :possessor s12n)`, where s12n is the 《世界新闻周报》 node.
- snt13 他们经常报导
  - Annotation: `(s12p :same-entity s13p)`.
  - Gold: `(s12n :same-entity s13p)`. The chain runs from the newspaper to the pronoun.

**Why:** Section 2.4 says a pronoun is always `person`/`thing` with person and number. Nothing says what to do when 他们/它 refers back to an organisation or publication.

**Change:** add to 2.4 and 5.3:
- "When 他们/它/其 refers to an organisation or publication already mentioned in the same sentence, do not make a new node. Use that entity's variable (`标语 :possessor s12n`). A possessive 他们的 in front of an event noun adds no `:ARG0`."
- "In a later sentence the pronoun is its own `person` node, but its coreference goes to the named entity (`(s12n :same-entity s13p)`), not to an earlier pronoun node."

## 2. 其中最大宗可算是外星人地球活动 (snt14): roles, modal strength and tense all wrong
**Cost:** about 14 units across d_core_args (event and abstract), e_core_labels ×3, a_entity, b_event_sense, i_modal, h_temporal and j_coref_subset.

**What went wrong:**
- **算是 roles.** The annotation had `算是 :ARG1 thing :ARG2 活动`. PropBank 算是-01 has `ARG0` = the entity described and `ARG1` = what it counts as.
  - Gold: `(算是-01 :ARG0 (implicit-argument :ARG1-of (have-degree-91 :ARG1 (大) :ARG2 (最) :ARG5 (其中)) :unit (宗)) :ARG1 (活动-01 …))`.
- **Modal strength.** 可 was ignored, giving `(author :full-affirmative s14x)`. Gold has `(author :neutral-affirmative s14x)`.
- **Temporal relation.** The annotation had `(document-creation-time :overlap s14x)`. Gold has `:before`.
- **Sense.** 活动 was written with no sense. Gold has `活动-01`; it is in PropBank.
- **Extra subset link.** The annotation added `(s14t :subset-of s13t)`. Gold has no such triple.

**Why:**
- The rule that modal verbs "are not nodes" was followed, but the second half, that they change modal strength, was not applied to 可.
- Rule 2.3 tells the annotator to look up lexical verbs, but the annotator did not check 算是's role numbers.
- The 5.1 rule "a sentence that sums up the earlier text is anchored to document-creation-time" gives no relation, so the annotator picked `:overlap`.
- Section 2.1 tells the annotator to annotate event nominals as events, but does not say they still take their PropBank sense.

**Change:**
- In 5.2, add: "可/能/可以 before a predicate (可算是) make that predicate `neutral-affirmative` from the author."
- In 5.1, change the summing-up rule to: "…is `(document-creation-time :before X)` in a past-tense narrative document."
- In 3, add: "算是-01: `:ARG0` = the thing described, `:ARG1` = what it counts as."
- Add: "其中最 + noun with no head noun → `implicit-argument` with `have-degree-91 :ARG1 <adj> :ARG2 (最) :ARG5 (其中)`; a classifier such as 宗 is `:unit`."
- In 2.1, add: "an event nominal that has a PropBank frame takes its sense (活动-01)."
- In 5.3, add: "No `:subset-of` link from a 其中 phrase."

## 3. 母公司美国媒体公司 and the short 周报 mention (snt11)
**Cost:** about 12 units across a_entity_found, a_granularity ×4, d_core_args, d_core_args_abstract, f_name_tokens, g_reentrancy ×3 and j_coref.

**What went wrong:**
- **The company.** The annotation had `(公司 :mod 母 :name "美国" "媒体" "公司")`.
  - Gold: `(s11c / company :name … :ARG1-of (identity-91 :ARG2 (公司 :mod (母))))`.
- **The short mention 周报.** 周报的网络版 was written `:part-of s11n`, a re-entrancy to the full 《世界新闻周报》 node.
  - Gold: a separate `(s11x5 / 周报)` node, plus `(s11n2 :same-entity s11x5)` in the coreference list.
- **Missing `:ARG0` on 发行.** Gold has `发行 :ARG0 s11c`. The instruction's own control rule (它停止了它的发行 → 发行 `:ARG0` 它) covers this, but the annotator did not apply it.
- **Shared date.** Gold has `继续 :temporal s11d`: the sentence-initial date also scopes the second clause.

**Why:**
- The apposition rule in 3 only covers common noun + 《name》, so a role noun before an organisation name was merged into it.
- The "refer to it by its bare variable" rule in 3 and "within one sentence, coreference is a re-entrancy" in 5.3 directly caused the 周报 merge.

**Change:**
- Extend the apposition rule: "<role noun> + <organisation name> (母公司美国媒体公司) → entity-type node (`company`) with the name, plus `:ARG1-of (identity-91 :ARG2 <role noun>)`."
- Qualify the re-entrancy rule: "A shortened repeat of a name (周报 after 《世界新闻周报》) is its own node with the bare word as its concept, linked by an in-sentence `:same-entity` triple. Use re-entrancy only for pronouns and for exact repeats."
- Add: "A sentence-initial date shared by both clauses of 不过/但 goes on both main events as `:temporal`."
- Restate the control rule next to 停止/开始 + 的 + event noun.

## 4. Modal and temporal structure of reported content (snt12, snt15)
**Cost:** about 9 units: i_modal ×7 and h_temporal ×2.

**snt12:**
- **Conceiver on the wrong node.** The annotator gave the conceiver triple to the inner 报导 (`s12n :full-affirmative s12r`).
  - Gold puts it on the top node of the quoted content, `(s12n :full-affirmative s12h)` (the have-mod-91).
  - Gold also adds `(author :full-affirmative s12h)`, plus `(s12n :full-affirmative …)` on the slogan's 报导 and on the 大部分的报导 clause.
- **Slogan identity-91.** It needs `:aspect state`, and its 报导 needs `:quote s12i3`.
- **Temporal parents.** The other content events should hang from the first content event, `(s12x4 :overlap s12x6) (s12x4 :overlap s12x10)`, not from 宣称. The instruction already says this; the annotator did not follow it.

**snt15:**
- **Conceiver of 被指.** Gold's conceiver is the coordinated subject `s15a` (the `and` node), with `(author :full-affirmative s15a)`. The annotator used Hillary alone (s15p).

**Change:**
- In 5.2: "The conceiver triples go on the top node of the content: the node that carries `:quote`, even an abstract predicate. Give that node both `author` and conceiver triples."
- "For 被指 the conceiver is the whole subject node of the content's first event (the `and` node when it is coordinated)."
- "A quoted slogan is `identity-91 :aspect state`, and its inner event carries `:quote` that identity-91."
- "宣称 as a past claim is `performance`, not `activity`."

## 5. Named fictional characters in a 如…等 list (snt13)
**Cost:** about 9 units: f_name_tokens ×3, a_entity_concept ×2, a_granularity, c_other_attributes ×3 (the main reason its precision is 40), plus an extra coreference link.

**What went wrong:**
- 蝙蝠男孩 was written `(男孩 :mod 蝙蝠)`. Gold has `(individual-person :name (name :op1 "蝙蝠" :op2 "男孩"))`.
- 外星人P'Lod was written `(外星人 :name "P" "'" "Lod")`. Gold has `(individual-person :name (name :op1 "外星人" :op2 "P" :op3 "'" :op4 "Lod"))`.

**Why:** The instruction's own rule "外星人 P'Lod is no apposition: (外星人 :name …)" fits gold in snt15 but not in this list. Gold is not consistent here.

**Change:** limit that rule: "In a list of example characters (如 A、B 等), each character is `individual-person` with the whole written name, the descriptor included (`:op1 "外星人" :op2 "P" …`). Use `(外星人 :name …)` only in running narrative." Also: "Do not corefer mentions whose node types differ in this way unless the text makes them the same." Gold does not link snt13's P'Lod to snt15's.

## 6. Extra adverb nodes
**Cost:** about 6 units across a_entity_found, d_peripheral_event and a_event_concept.

**What went wrong:**
- snt15: 就 and 还 (后来还领养) were added as `:mod`.
- snt12: the 都 of 都以…为目的 was added as `:mod`.
- snt11: 仍 was added as `:mod`.

Gold omits all of these. Gold does keep the 都 in 都是真实的 and 甚至.

**Change:** narrow the adverb list in 3: "Focus particles 就 and additive 还 after 后来 are not annotated. 仍 next to 继续 is redundant and gets no node. Keep 都 only when it quantifies the subject of a copular predicate."

## 7. Smaller problems
- **出现's location (snt13).** 在他们的新闻中 was written as `:place`. Gold uses a numbered argument: `出现 :ARG1 (中 :op1 新闻)`. Change: "A location role in a 出现/在…中 frame is a numbered argument; look up the frame." (PropBank lists the location as ARG0, but gold uses ARG1.)
- **Temporal parent in snt13.** `(s13c :after s13x)` was extra. Events inside a relative clause on the created object should be `:overlap`, or follow gold.

## What to keep
- Event detection (a_event_found 100) and person/number attributes (c_refer 100).
- The clause-level structures: `but-91` with `and`, `identity-91` with `目的 :purpose-of`, `consecutive` with `:quote` on both content events, and `:example (and … (等))` lists.
- The control re-entrancy for 继续生存.
- `individual-person` plus `have-rel-role-91 :ARG3 (第一夫人 :mod 前 :place country)`.
- The date chain `(document-creation-time :before date)(date :overlap 停止)` and `(有 :after 领养)`.
- 领养-01: PropBank has this sense. Gold's 领养-00 is a gold slip, so do not change the "look the verb up first" rule.