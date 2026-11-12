Below are the error patterns, most costly first. The costs come from the judge's lists above.

---

### 1. A sentence with both 虽然 and 不过: the annotator built the wrong top structure (snt12, the biggest single cost)

**Cost.** This one structure accounts for most of the snt12 losses:
- a_event_found: but-91 and identity-91 missing.
- d_core_args_abstract: about 8 units, since have-purpose-91 was matched against gold's have-mod-91.
- d_core_args_event, d_peripheral_event (`:medium`, `:quant`), modal: 6 units.
- temporal: 5 units.
- g_reentrancy: 3 units.
- The person/目的 confusion this created also spread into coreference.

**What happened.**
- 虽然 X（标语：Y），不过 Z 以博君一笑为目的 was annotated as `(have-purpose-91 :ARG1 报导 :ARG2 博君一笑-00 :concession (宣称 …))`.
- 都是真实的 became the event `真实-01`.
- The slogan in parentheses became `:medium 标语` of 宣称.

**Gold:**
```
(b / but-91
   :ARG1 (a / and
      :op1 (x / 宣称-01 :ARG0 n
              :ARG1 (h / have-mod-91 :ARG1 (r / 报导-01) :ARG2 (t / 真实) :mod 都 :quote x :aspect state))
      :op2 (i3 / identity-91 :ARG1 (y / 标语 :possessor n) :ARG2 (r2 / 报导-01 … :quote i3) :aspect state))
   :ARG2 (i2 / identity-91 :ARG1 (m / 目的 :purpose-of (r3 / 报导-01 :mod 大部分)) :ARG2 (g / 博君一笑) :aspect state))
```

**Why.** The instruction contradicts itself here. Section 2.5 maps 虽然 to `:concession` and says to reify 为(了) clauses as have-purpose-91. The but-91 rule only covers 不过 on its own. Nothing says what to do when 虽然 and 不过 come together. There is also no rule for 以 X 为目的, for 是 + adjective + 的, or for a parenthetical gloss.

**Change.** Add these rules to 2.5 and 2.3:
- "虽然/尽管 X，不过/但是/却 Y in one sentence → `but-91 :ARG1 X :ARG2 Y`, with no `:concession`."
- "以 X 为目的 / 以 X 为 Y → `identity-91 :ARG1 (目的 :purpose-of V) :ARG2 X`. Do not use have-purpose-91, which is only for 为(了) … clauses. X stays a plain concept (博君一笑), not an event."
- "X 是 Adj 的 / X 都是 Adj 的 → `have-mod-91 :ARG2 (Adj)`. The adjective has no sense and no aspect, and gets no temporal or modal triple."
- "A parenthetical 'N：Y' gloss (他们的标语：「…」) is its own clause: `identity-91 :ARG1 N :ARG2 Y`, `:aspect state`. Join it to the neighbouring clause with `and`. It is never `:medium`."
- "大部分的 N → `:mod (大部分)`, not `:quant`."

### 2. A pronoun or repeated noun for the document's main entity was given a new node, which broke coreference (j_coref_chain F 13, plus g_reentrancy and c_refer)

**What happened.**
- In snt12, 他们 (meaning the paper) became a new `person 3rd plural`. Gold re-enters the newspaper node (`标语 :possessor s12n`, `报导-01 :ARG0 s12n`).
- The annotator then chained `s12p → s13p`. Because its s12p was matched to gold's 目的, the snt13 他们 ended up in the wrong chain.
- In snt11, the bare 周报 in 周报的网络版 was made a re-entrancy to `s11z` (the named paper). Gold gives it its own node `(s11x5 / 周报)` with `(s11n2 :same-entity s11x5)`. The annotator's 仍 got matched to it.

**Why.** Section 2.1 already says a common-noun mention of a named entity is the Chinese word itself. But 5.3 says "within one sentence, coreference is a re-entrancy", and the annotator followed 5.3. Nothing says that 他们/它们 can refer to an organisation or publication.

**Change.**
- Narrow 5.3: "Re-entrancy is only for pronouns, zero arguments and 自己/其. A repeated common noun (周报, 该刊) always gets its own node, even in the same sentence, linked by a `:same-entity` triple."
- Add to 2.4: "A 他们/它们 that refers to an organisation or publication already in the same sentence is the bare variable of that node: no new person node, no refer attributes. In a later sentence, write the pronoun node and link it to the named entity: `(s12n :same-entity s13p)`."

### 3. Named-entity type and name tokens (f_name_tokens F 62, a_entity_concept, granularity)

**What happened, and the gold version:**
- **蝙蝠男孩, P'Lod (snt13).** The annotator wrote `person`. Gold has `individual-person`, which the instruction already requires; this is an instruction-following failure.
- **外星人 P'Lod (snt13).** The annotator added an appositive `identity-91 :ARG2 外星人` (an extra event plus an extra entity). Gold puts it in the name, `:op1 "外星人" :op2 "P" …`. In snt15 gold instead uses `(外星人 :name (n :op1 "P" :op2 "'" :op3 "Lod"))`. Either way, there is no identity-91.
- **希拉里·克林顿.** Gold keeps the middle dot as a token: `:op1 "希拉里" :op2 "·" :op3 "克林顿"`.
- **地球.** Gold has `(planet :name (n :op1 "地球"))`, not a common noun.

**Change.** Add to 2.2:
- "Keep 《 》 and the middle dot · as name tokens."
- "A bare category noun directly before a foreign name (外星人 P'Lod) is the node's concept or part of the name, never an appositive identity-91. Use identity-91 only when the noun has its own modifiers (旗下的八卦小报)."
- "地球 → `planet` with `:name`."
- Repeat the existing rule in the checklist: "every named person in a Chinese document is `individual-person`."

### 4. Reported content: the participants of 与 X 有关系, 后来, and :quote (snt15; also snt12)

**What happened, and the gold version:**
- **与 P'Lod 有暧昧关系.** The annotator wrote `有-01 :ARG0 Hillary :companion P'Lod`. Gold makes the 与-phrase a co-participant: `有-03 :ARG0 (and :op1 Hillary :op2 P'Lod) :ARG1 关系`.
- **…，后来还领养.** The annotator wrote `and` with `:temporal (后来)` and `:mod 还`. Gold uses `(consecutive :op1 有-03 :op2 领养)`, and drops 后来, 还 and 就 (3 extra nodes, 2 extra peripheral roles).
- **美国前第一夫人.** The annotator wrote `have-org-role-92 :ARG2 country`. Gold has `have-rel-role-91 :ARG3 (第一夫人 :mod 前 :place (country "美国"))`: first lady is a relational role, not an organisational title.
- **:quote.** Gold marks every quoted or reported clause with `:quote <reporting event>` (宣称, 指, the slogan). The annotator never used it, which cost 4 g_reentrancy units.

**Change.**
- Add to section 3: "与/和/跟 X 有 关系/联系 → `有-03 :ARG0 (and :op1 subject :op2 X)`."
- Add: "Two clauses joined by 后来/然后/接着 → `(consecutive :op1 … :op2 …)`. The connective gets no node."
- Make the existing "never drop" list explicit that it covers only 已经, 都, 也, 仍, 还 in ordinary assertions. Within consecutive, 还 and 后来 are absorbed, and the discourse particle 就 gets no node.
- Add: "第一夫人 / 夫人 → have-rel-role. The country is `:place` of the role noun."
- Turn the `:quote` remark into a rule: "the content clause of 宣称/指/说, and a quoted slogan, get `:quote <reporting event or identity node>`."

### 5. Aspect and argument choices that override the "institution's activity = habitual" rule (c_aspect F 74, core args)

**What happened, and the gold version:**
- **发行 under 停止.** Gold has `:aspect process`, with `:ARG0` the company (re-entrancy). The annotator wrote habitual and gave no ARG0.
- **继续 生存.** Gold has `继续-01 :ARG0 网络版 :ARG1 (生存-01 :ARG0 网络版 :aspect state)`. 生存 is a state, and the subject is ARG0 of both verbs. PropBank 继续-01 has ARG0 = agent.
- **甚至创造出.** Gold has performance (a completed result marked by 出). The annotator wrote habitual.
- **活动 (snt14).** Gold has activity.

**Change.** Add to 4.1:
- "An event noun that is the complement of an aspectual verb (停止/开始/继续 + N的发行) is `process`. The agent of the aspectual verb is re-entered as the noun's ARG0."
- "Under 继续, the subject is ARG0 of both 继续-01 and the inner verb."
- "Verb + resultative complement (创造出, 做成) for a past action → `performance`, even in a habitual context."
- "生存, 存在 → `state`."

### 6. 有 used to list examples, and 出现 roles (snt13)

**What happened, and the gold version:**
- **题材有 A、B…等.** The annotator wrote `有-07`. Gold has no 有 event: `报导-01 :ARG1 (题材 :example (and … 等))`, and the 报导 clause becomes the main event and temporal anchor. That anchor change is also why the snt13 temporal triples failed.
- **在新闻中重复出现的人物.** Gold has `人物 :ARG0-of (出现-01 :ARG1 (中 :op1 新闻) :frequency 重复)`. The annotator wrote ARG1 人物, ARG0 新闻, and `:mod 重复`.

**Change.**
- Add: "N 有 A、B、C 等 that lists the members of N → `N :example (and …)`, no 有 node."
- Add: "重复/经常/多次 → `:frequency`."
- Add: "For 出现-01, follow the gold usage: the thing that appears is ARG0, and the 在…中 location is ARG1 `(中 :op1 …)`." This is the reverse of what the PropBank labels (ARG0 location, ARG1 theme) suggest, so it needs to be stated outright, as was done for 属-02.

### 7. The superlative 其中最大宗 (snt14)

**What happened, and the gold version:**
- The annotator wrote `thing :ARG1-of (have-degree-91 :ARG2 大宗 :ARG3 最) :mod 其中`, plus the verb `算-01`.
- Gold has `算是-01` (it is in PropBank, so the instruction's "keep the compound as written" rule applied) and `implicit-argument :unit 宗 :ARG1-of (have-degree-91 … :ARG5 其中)`.
- The full guideline gives have-degree-91 ARG5 = the reference superset.

**Change.**
- Add to 4.2: "其中/之中 with a superlative is `:ARG5` of have-degree-91, not `:mod`."
- Add: "A headless superlative (最大宗) has an `implicit-argument` head, and its classifier is `:unit`."
- Restate in the PropBank step: "look up the compound first (算是, 改为) and use it if it exists."

### 8. Smaller items
- **母公司.** Gold splits it into `公司 :mod 母`.
- **Event nodes in s12 temporal.** Do not give temporal or modal triples to non-event nodes (真实, 博君一笑, 中).
- **Reported content in modal.** Gold adds `(speaker :full-affirmative content)` alongside the author triples. The instruction already says this; the annotator only half did it, giving the speaker the content of 宣称 but not the slogan's content.
- **Coreference across reported sentences.** Do not add a `:subset-of` triple without a clear set (the snt14 → snt13 题材 link was counted extra).

### What to keep
The instruction is working in these places and should stay as it is:
- **Format and attributes:** document format (k 100) and other attributes (100).
- **Title marks:** 《 》 as name tokens, as in the 世界新闻周报 name.
- **but-91 in a plain X，不过Y sentence:** correct in snt11.
- **Dates:** the date-entity as `:temporal` with `(document-creation-time :before d)(d :overlap main)`.
- **Dependent events:** anchored to the main event in snt11 (all temporal triples correct).
- **Aspect choices:** performance for 停止了 and 宣称, state for 有 and 算是.
- **Frequency:** `:frequency 经常`.
- **Modal strength:** `neutral-affirmative` for 可算是.
- **Superlative signal:** reifying 最 with have-degree-91.
- **Modal format:** the `(root :modal author)` skeleton.