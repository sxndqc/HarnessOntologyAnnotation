I've ranked the problems by roughly how many judge units each one cost. The worst scores were temporal (F 43), peripheral roles on events (F 33), core arguments of abstract predicates (F 37), core arguments of events (F 54), re-entrancy (F 56) and other attributes (F 57).

## 1. Temporal anchoring: the wrong main event, and wrong relations for reported content and contrast (about 12 h_temporal units)

**What went wrong**
- **Contrast clause marked `:after`.** In snt11, 不过…仍继续生存 had `(s11x :after s11x3)`. Gold has `(s11x :overlap s11x2)`. The online edition is still going on at the same time as the stop, so it overlaps.
- **Reported content hung from the reporting verb.** In snt12 the annotator hung every event from 宣称: `(s12x3 :overlap s12x4/s12x5/s12x)`. Gold hangs only the first content event from 宣称 (`s12x :overlap s12x4`). The slogan's 报导 and the main clause's 报导 then hang from that first content event (`s12x4 :overlap s12x6`, `s12x4 :overlap s12x10`).
- **Content of a 被指 report given `:before`.** In snt15 the annotator had `(s15x :before s15x2)` and `(s15x2 :before s15x3)`. Gold has `(s15x :overlap s15x3)` for the content, and `(s15x3 :after s15x2)` for 后来领养, which comes after the relationship.
- **The wrong event anchored to the document creation time (DCT).** In snt13 the annotator anchored a 有 node, which gold doesn't have. Gold anchors the first event, 报导, and hangs 创造 from it.
- **A sentence chained from the previous one when it shouldn't be.** snt14 had `(s13x :overlap s14x)`. Gold has `(document-creation-time :before s14x)`. It is a new evaluative statement, not part of the same episode.
- **Temporal parents given to non-events.** 出现 (`s13x4 :before s13x5`) and 博君一笑 got parents; gold gives them none.

**Why it happens.** The rule "continues the previous sentence's episode → hang from its main event" is too broad, so it was applied to a summary sentence (snt14). There is no rule for where reported content goes in time. There is also no rule that 仍/继续 in a contrast clause means `:overlap`.

**What to add to the instruction**
- "Content of a reporting verb (宣称, 指, 说): its first event is `:overlap` the reporting verb. Other content events and later clauses hang from that first content event. 后来 X after Y → `(Y :after X)`."
- "A clause with 仍/继续/还 that contrasts with a past event overlaps it (`:overlap`), never `:after`."
- "A sentence that judges or sums up the earlier text (算是, 其中最…) is anchored to `document-creation-time` itself."
- "Anchor the first predicated event in reading order to DCT."

## 2. Clause structure for 虽然…不过, 以 X 为目的 and parenthetical slogans (snt12; about 15 units across event_found, core_args_abstract, peripheral and modal)

**What went wrong.** The annotator built `have-purpose-91` as the root, with 宣称 as a `:concession` and the slogan as `:medium`. Gold has:
```
(but-91 :ARG1 (and :op1 (宣称-01 :ARG0 周报 :ARG1 (have-mod-91 …))
                   :op2 (identity-91 :ARG1 (标语 :possessor 周报) :ARG2 (报导-01 :ARG1 事实 :mod 只)))
        :ARG2 (identity-91 :ARG1 (目的 :purpose-of (报导-01 :mod 大部分)) :ARG2 (博君一笑)))
```

**Why it happens**
- Section 2.5 says 虽然 → `:concession` and does not cover the paired 虽然…不过.
- The have-purpose-91 rule (for "paired connectives") pulled in 以…为目的, which is not a pair of connectives.
- Nothing says what to do with a parenthetical "X: Y".

**What to add to the instruction**
- "虽然 X，不过/但是 Y → `but-91 :ARG1 X :ARG2 Y`. `:concession` is only for 虽然/尽管 with no second connective."
- "以 X 为目的 → `(identity-91 :ARG1 (目的 :purpose-of <event>) :ARG2 X)`. 目的 is a node; X is a plain noun concept, not an event."
- "A parenthetical 'N：quote' is `(identity-91 :ARG1 N :ARG2 <quoted content>)`, joined to the clause it follows with `and`."
- "大部分 on a nominalized event is `:mod`, not `:quant`."

## 3. Shared arguments of control and aspectual verbs: a rule in the instruction caused this (g_reentrancy R 42, plus core_args; about 8 units)

**What went wrong**
- In snt11, 停止了…的发行 needs 发行 `:ARG0 s11c`, and the annotator left it out.
- 网络版继续生存 should be `(继续-01 :ARG0 (网络版) :ARG1 (生存-01 :ARG0 网络版))`. The annotator put 网络版 only under 生存.
- In snt11, 继续 also shares `:temporal s11d` in gold.

**Why it happens.** The instruction says "Never re-use a participant … as an unexpressed agent … every re-entrancy needs a pronoun or an overt word." The annotator followed it. In a control construction, though, the overt subject *is* the shared argument.

**What to change.** Narrow the rule: "Exception: the subject of a control or aspectual verb (继续, 停止, 开始, 开始/停止 + nominalized V, 想, 打算) is also the `:ARG0` of the embedded event, by re-entrancy. The subject of 继续/停止 is `:ARG0` of the control verb too."

## 4. Reported speech: `:quote` and modal parents (g_reentrancy 4 units, i_modal about 8 units)

**What went wrong**
- No `:quote` was used anywhere. Gold has `have-mod-91 :quote s12x`, slogan `报导 :quote s12i3`, and in snt15 `有-03 :quote s15x` and `领养 :quote s15x`.
- In snt12, reported events got only the speaker as modal parent. Gold gives them **both** `(author :full-affirmative X)` and `(s12n :full-affirmative X)`.
- In snt15 the annotator used the event 指 as conceiver: `(s15x :full-affirmative s15x2)`. Gold uses the subject node, `(s15a :full-affirmative …)`, plus `(author :full-affirmative s15a)`.
- The annotator added `(author :full-affirmative s11b)` to `but-91` and `(author :full-affirmative s12h)` to the snt12 root have-purpose-91 (which matches gold's `and`). Gold gives connectives no modal parent.

**What to change**
- Make `:quote <reporting event>` mandatory on the top node of a quoted or claimed content (宣称, 指, a slogan), not optional ("release data also marks…").
- "Each content event gets both `(author :full-affirmative X)` and `(<speaker> :full-affirmative X)`. When the speaker is not written (被指), use the passive subject as conceiver."
- "Discourse connectives (`but-91`, `and`, `consecutive`) get no modal triple." Keep "root abstract predicate → author FA" only for `identity-91`/`have-*-91`.

## 5. Lists with 有 and 等, and the frame of 出现 (snt13; about 10 units)

**What went wrong**
- 他们经常报导的题材有 A、B…等 was built as a 有-01 predicate. Gold has `(报导-01 :ARG1 (题材 :example (and :op1 … :op6 (等))) :frequency (经常))`.
- 等 should be the last `:opN` of the `and`, not `:mod` on it (this happened twice).
- 时间旅行 in a noun list is an entity `(旅行 :mod 时间)`, not an event with aspect.
- 在新闻中重复出现的人物 should be `(人物 :ARG0-of (出现-01 :ARG1 (中 :op1 新闻) :frequency (重复)))`. The annotator used `:ARG1-of`, `:place` and `:manner`.

**Why it happens.** There is no rule for "X 有 A、B 等" lists, nor for 等. The instruction does say to take role numbers from the Chinese roleset, but this wasn't followed for 出现: in PropBank, 出现-01 has ARG0 = possessor/location and ARG1 = theme, so gold's ARG0-of for 人物 doesn't follow the roleset either.

**What to add to the instruction**
- "'<topic noun> 有 A、B…等' listing examples → `:example (and …)` on the noun; 有 is not an event. 等 → the last `:opN` of the `and`."
- "如 A、B 等 → `:example (and :op1 A :op2 B :op3 (等))`."
- "Nouns in a list of topics (时间旅行) are entities."
- "重复/经常 → `:frequency`."
- "在 N 中 → `(中 :op1 N)`."

## 6. Named entities and role nouns (f_name_tokens, granularity, entity_concept; about 10 units)

**What went wrong**
- **外星人 P'Lod.** The annotator wrote `(individual-person :name "P" "'" "Lod" :ARG1-of (identity-91 :ARG2 外星人))`. Gold has `:op1 "外星人" :op2 "P"…` in snt13, and `(外星人 :name (name "P" "'" "Lod"))` in snt15. Either way, gold uses no identity-91 for a classifying noun in front of a name. Add: "A common-noun title directly before a name (外星人 P'Lod) is not an apposition: make the noun the concept with `:name`, or put it inside the name. No identity-91."
- **地球.** It should be `(planet :name (name :op1 "地球"))`. Add `planet` to the list of types.
- **母公司.** It should be `(公司 :mod (母))`. Add: "A noun compound made of a modifier morpheme and a head that is itself a word (母公司, 外星宝宝) is split into head `:mod` modifier."
- **美国前第一夫人.** Gold has `(have-rel-role-91 :ARG3 (第一夫人 :mod (前) :place (country 美国)))`. The annotator had `have-org-role-92 … :temporal (前)`. Add: "前 (former) → `:mod (前)` on the role noun. A kinship-like title (第一夫人) uses have-rel-role. A country modifying the title is `:place` on the title."

## 7. "X 与 Y 有关系", senses, and compound verbs (snt15, snt14; about 8 units)

**What went wrong**
- 与 Y 有暧昧关系 should be `(有-03 :ARG0 (and :op1 X :op2 Y) :ARG1 (关系 :mod 暧昧))`, not `:companion`.
- The annotator chose senses 指-01 and 有-01. Gold has 指-02 ("points out/claims", which fits 被指) and 有-03.
- In snt14 the annotator wrote 算-01 although 算是-01 is in PropBank (ARG0 = entity described, ARG1 = what it is considered as). This breaks the existing "keep compound verbs whole" rule. The rule should say "look up the whole compound (算是, 称为) first."
- 后来 and 就 should not be `:temporal`/`:mod` nodes here. Gold expresses 后来 through `consecutive :op1 有 :op2 领养`.

**What to add:** "X 与 Y 有 关系/联系 → `有-03 :ARG0 (and X Y)`." "被指 → 指-02." "后来/然后 between two clauses → `(consecutive :op1 … :op2 …)`, not a `:temporal` node."

## 8. Aspect (c_aspect F 80; 4 units)

**What went wrong**
- 发行 under 停止 as a nominalized object should be `process`. The annotator made it `habitual`, carrying the publication-verb rule too far.
- 生存 is a `state`, not `activity`.
- 活动 (ongoing alien activities) is `activity`, not `process`.

**What to add:** "The habitual rule does not apply to an event nominal that is the object of 停止/开始 (它的发行 → `process`). Verbs of existing or surviving (生存, 存在) → `state`."

## What to keep
- The `but-91` root for a 不过 contrast inside one sentence (snt11) was correct.
- Date-entity anchoring was correct: `(document-creation-time :before s11d)` and `(s11d :overlap s11x)`.
- 《》 name tokens were correct, and so were individual-person for Hillary and no `:wiki`.
- Pronoun person and number were correct (c_refer 100).
- The coreference chain 周报 → 《世界新闻周报》 → 他们 was correct, and nothing in a sentence was linked to itself.
- Reading 可 as neutral-affirmative on 算是 was correct.
- `:aspect performance` for 宣称/创造/停止 was correct.
- `:part-of` on 网络版 when 周报 is written with it was correct.
- 甚至/仍/都 as `:mod` concepts were correct.
- `have-mod-91` for 报导都是真实的 was correct.

Keep these rules. The one change I'd make to existing coreference practice is the P'Lod mentions: gold doesn't link them across sentences, probably because the entity is built differently in each sentence. So keep the "when in doubt, leave it out" rule for named entities that are built differently in different sentences.