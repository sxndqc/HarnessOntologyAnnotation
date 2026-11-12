# Review of the annotation of sentences 16–20, with changes to the instruction

The annotator found every event (event-found F 100), got every person/number attribute right (F 100) and used the right core role labels (F 100). The losses come from about eight patterns, listed below with the costliest first. Three of them come from rules in the instruction that disagree with the gold for this document (patterns 2, 4 and 5). Two more come from conflicts that are smaller in cost or in how many sentences show them (pattern 8: purpose clauses and the subject of a purpose verb). The others are cases the instruction does not cover.

---

## 1. A headline in 「…」 after 一篇 / 新闻 was annotated as a clause instead of a named publication (about 25 units)

**Checks hit:** a_entity_concept (s18p, s19p2, s19x4, s20p), f_name_tokens (3 missing or wrong), d_core_args (the ARG2 of 刊登, the ARG2 of identity-91), c_other_attributes (`:quant 10000` on 希特勒, `:quant 1` on 复制-01), g_reentrancy (4 extra: `:quote`, `追杀 :ARG0`, and others), h_temporal (2 extra) and i_modal (about 5 extra speaker triples). The extra 外星人 coreference link also comes from this.

**Examples:**
- 刊登一篇「苏联复制一万个希特勒」
  - The annotation had `:ARG2 (s18p / 复制-01 :ARG0 (country "苏联") :ARG1 (individual-person "希特勒" :quant 10000 :unit 一万个) :quant 1 :unit 篇 :quote s18k)`, plus `(s18t :full-affirmative s18p)`.
  - Gold: `:ARG2 (s18p / publication :name (n / name :op1 "「" :op2 "苏联" :op3 "复制" :op4 "一万个" :op5 "希特勒" :op6 "」") :unit (篇) :quant 1)`. This node has no temporal triple and no modal triple.
- 该刊的一篇新闻「12位美国参议员是外星人！」
  - The annotation had `identity-91 :ARG2 (have-role-91 …)`.
  - Gold: `(新闻 :ARG1-of (identity-91 :ARG2 (publication :name (… :op1 "「" … :op8 "！" :op9 "」")) :aspect state))`.

**Why it happens:** The instruction only covers reported speech (`:quote`, speaker as conceiver) and 《》 titles. It never says that a quoted headline counted as an article (一篇「…」) is a name. Without such a rule, the annotator treated every quote as reported content.

**Change:** Add to 2.2:
> A headline or article title in 「 」 that is counted (一篇「…」) or set in apposition to 新闻/报导/文章 is `publication :name`. Every word between the marks, and the marks 「 」 and any ！ themselves, is one `:opN`. Put 一篇 on the publication as `:quant 1 :unit 篇`. Do not parse the headline's words: no events, no `:quote`, no speaker triple, no temporal or modal triple for anything inside the title.
>
> Keep the reported-speech analysis only for 「…」 directly after a reporting verb with no classifier. Example: 报导「外星人支持布什当总统」 → `支持-01`, as gold does in sentence 16.

---

## 2. Who is the conceiver in a reporting sentence, and which nodes get modal triples (about 15 units of i_modal; i_modal F 40)

**Examples:**
- Sentence 16, where the paper reports, publishes and claims:
  - The annotation had `(author :full-affirmative 报导/注销/指)` and `(s16k :full-affirmative 支持/当/当选/背书)`.
  - Gold has the reverse:
    - the paper is the conceiver of its own acts: `(s16x4 :full-affirmative s16x)`, `(s16x4 :full-affirmative s16x2)`, `(s16x4 :full-affirmative s16x3)`;
    - the content events hang from the author: `(author :full-affirmative 支持)`, `(author :full-affirmative 当选)`, `(author :full-affirmative 背书)`;
    - 当-02, nested under 支持, has no modal triple and no aspect.
- Extra triples on nodes that gold leaves without a modal parent:
  - connectives: `(author :full-affirmative s16a)` on and, `(author :full-affirmative s17b)` on but-91, and the same on s19h (have-reason-91);
  - entity nodes in sentences 18–20 (s18t, s19p, s20k).
- Sentence 17: the instruction's complement rule gave `(s17y :neutral-affirmative s17d)`. Gold has `(author :neutral-affirmative 点出)`, and `(author :full-affirmative …)` for 荒谬 and 可笑, not 点出 as their parent.

**Why it happens:**
- Section 5.2 tells the annotator to make the speaker the conceiver of the content. That is wrong for this gold's 报导/指 pattern.
- Section 2.5 explicitly gives have-reason-91/have-purpose-91 an author triple.
- Nothing says that `and`/`but-91` get no modal triple.
- Nothing says that an entity gets an author triple only when it really is a conceiver.

**Change:** Rewrite the reported-speech bullet in 5.2:
> When a publication or person 报导/指/刊登 something, write `(author :full-affirmative paper)` once. Then the paper parents its own verbs: `(paper :full-affirmative 报导-01)`. The reported content events get `(author :full-affirmative X)`. An event that is an argument of another content event (当 under 支持) gets no modal triple.
>
> Never give a modal triple to `and`, `or`, `but-91`, `contrast-91` or `consecutive`.
>
> A participant entity gets an author triple only when it parents some event in the same sentence.
>
> For ability (有能力 V), use `(author :neutral-affirmative V)`. Events inside V's object get `(author :full-affirmative …)`.

Delete the have-reason-91/have-purpose-91 author-triple requirement in 2.5, or mark it as uncertain.

---

## 3. Chinese property words and compound nouns were kept as plain `:mod` or as one concept (about 15 units)

**Checks hit:** b_event_sense, c_aspect, d_core_args_event, h_temporal (2 missing), i_modal (2 missing) and a_entity_concept (3).

**Examples:**
- 真实新闻: the annotation had `新闻 :mod (真实)`. Gold: `(新闻 :ARG0-of (真实-01 :aspect state))`, plus `(荒谬 :overlap 真实)` and `(author :full-affirmative 真实)`.
- 显著位置: gold has `(位置 :ARG0-of (显著-01 :aspect state))`.
- 好事者: gold has `(者 :ARG0-of (好事-00 :aspect state))`, plus `(贴到 :overlap 好事)`.
- 复制人: gold has `(人 :ARG1-of (复制-01 :aspect process))`.
- 全世界: gold has `(世界 :mod (全))`.

**Why it happens:** Section 2.1 says *"property words used as plain modifiers (a tall man: :mod tall)"*. That rule does not hold here: Chinese PropBank lists 真实-01 and 显著-01 as stative predicates.

**Change:** In 2.1, replace the *tall man* rule for Chinese with:
> A Chinese adjective that has a PropBank roleset (真实, 显著, 荒唐) is an event even when it modifies a noun: `N :ARG0-of (X-01 :aspect state)`, with a temporal triple `(head-event :overlap X)` and `(author :full-affirmative X)`. Keep `:mod` only for words with no roleset.
>
> Split a compound noun that ends in an agent or patient head: X者 → `者 :ARG0-of X-00`; V人 → `人 :ARG1-of V-01`. 全世界 → `世界 :mod 全`.

The narrower *adjectival chengyu → :mod* rule in 4.2 can stay.

---

## 4. Adverbs 还, 也 and 甚至 became nodes (about 8 units)

**Checks hit:** a_entity_found (s16h2, s16y, s16sz, s20m extra), d_peripheral_event (3 extra) and one confused concept match (s17e 也 matched against s17i2).

**Examples:**
- 还注销了… → gold has no 还.
- 甚至指… and 甚至被…贴到 → gold has no 甚至.
- 柯林顿…也靠 and 其编辑也有能力 → gold has no 也.
- 他们也报导了 → gold does keep 也 here (`:mod 也`). This is the one exception.

**Why it happens:** Section 3 says *"已经, 都, 也, 仍, 还 → a :mod node … Never drop them"*.

**Change:**
> 甚至 gets no node. 还 or 也 that only adds a further conjunct or a further clause (还注销, 但…也有) gets no node.
>
> Keep 也 as `:mod` only when the main verb of a stand-alone sentence carries it (他们也报导了). Keep 已经, 都 and 仍 as now.

---

## 5. Named events and institutions (about 8 units)

**Examples:**
- 2000年总统大选:
  - The annotation had `(总统大选 :temporal (date-entity :year 2000))`, with that date anchored to the document-creation time.
  - Gold: `:temporal (s16e / event :name (n / name :op1 "2000" :op2 "年" :op3 "总统大选"))`. Gold gives it no temporal triple.
- 美国参议院记者团的墙上:
  - The annotation had `墙上 :possessor (记者团 :mod (government-organization "参议院" :place (country "美国")))`.
  - Gold: `(墙上 :place-of (记者团 :place (building :name (n / name :op1 "美国" :op2 "参议院"))))`.

**Change:** Add to 2.2:
> A dated recurring event (2000年总统大选, 1998年世界杯) is `event :name`, with the year and 年 as name tokens. It has no date-entity and no temporal triple.
>
> A country name prefixed to an institution (美国参议院) is part of one name. When the text refers to the place (a wall in it), the type is `building`.
>
> X的墙上/里 for a group located there → `墙上 :place-of X`.

---

## 6. The structure of sentence 16's 指 clause (about 10 units)

These errors cover concepts, senses, reentrancy, temporal and `:quote`.

**Examples:**
- 靠外星人背书当选:
  - The annotation had `当选 :manner (靠-01 :ARG0 柯林顿 :ARG1 (背书-01 :ARG0 s16w))`.
  - Gold: `当选 :reason (背书-00 :ARG0 (s16x16 / 外星人) :aspect performance :quote s16x3)`. Gold has no 靠 node, and 外星人 is a new node.
- The annotator reused the first 外星人 (s16w). That breaks the instruction's own rule that a repeated noun gets its own node. It also linked the generic 外星人 across sentences to s19w, which gold does not do.
- Temporal:
  - gold has `(指 :before 当选)`, not `(1992 :overlap 当选)`, and gives the 1992 date no triple;
  - 指's parent is 注销, the previous conjunct, not 报导;
  - gold has `(注销 :overlap 合成)`, not `:before`.

**Change:**
> 靠 X (而) V → `V :reason X`, with no 靠 node.
>
> Every content event under 指/宣称 gets `:quote <reporting verb>`, nested ones included (背书).
>
> A reported past event takes the reporting verb as its temporal parent, `(指 :before 当选)`, even when it has its own date.
>
> In `and` with three or more conjuncts, chain the conjuncts: `(op1 :overlap op2)`, `(op2 :overlap op3)`.
>
> Never corefer generic or kind nouns (外星人 in different reports). Restate the "repeated noun gets its own node" rule in 2.4 as well.

---

## 7. 有能力 + VP, and possession versus part (about 8 units)

**Examples:**
- 有能力在标题点出…:
  - The annotation had `有-01`, with `能力 :mod (点出-01)`.
  - Gold: `有-06`, with `能力 :ARG1-of (identity-91 :ARG2 点出-01 :aspect state)` and `(author :full-affirmative identity-91)`.
- Possession versus part:
  - 周报内容 → gold has `内容 :part-of 周报`; the annotation had `:possessor`.
  - 该刊的一篇新闻 → gold has `新闻 :part-of 刊`; the annotation had `:possessor`.
- Other labels:
  - 外交政策 → gold has `政策 :topic 外交`; the annotation had `:mod`.
  - 握手的照片 → gold has `照片 :mod 握手-01`; the annotation had `:topic`.

**Change:**
> 能力/权力/机会 + VP → `N :ARG1-of (identity-91 :ARG2 VP :aspect state)`. 有 meaning "have (an ability)" is `有-06`.
>
> Extend the `:part-of` rule beyond editions: a publication's 内容, 新闻, 文章 or 版面 → `:part-of` the publication.
>
> Domain nouns before 政策/问题 (外交政策) → `:topic`. An event noun describing a picture (握手的照片) → `:mod`.

---

## 8. Smaller conflicts with the gold (about 5 units)

- **为了 讽刺… → `have-reason-91` in gold.** The annotation had have-purpose-91 with `:aspect state`; gold's have-reason-91 has no aspect and no modal triple. The gold in this document disagrees with 2.5. Because the evidence is mixed, add a note rather than flipping the rule.
- **The purpose verb's subject is copied in gold: `讽刺 :ARG0 他们`.** The checklist line "no subject copied onto a purpose verb" made the annotator miss it. Allow the subject when it is the overt subject of the main clause.
- **The aspect of 讽刺 is `performance` in gold.** The rule "a purpose verb is activity" is wrong here: in a completed past narration, the purpose verb takes the main verb's aspect.
- **The aspect of 支持 in a quoted claim is `state` in gold** (the annotation had activity).
- **Senses: gold uses 注销-00 and 背书-00,** although PropBank lists 注销-01 and 背书-01. This is gold noise and needs no rule.

---

## What to keep

- The event inventory: event-found F 100 and granularity F 100.
- Pronoun person and number: F 100.
- Core role labels: F 100.
- The but-91 skeleton in sentence 17 for 虽然…但.
- Anchoring each main reporting or publishing verb with `(document-creation-time :before X)`.
- `:temporal (争论-01 …)` for the 在…时 clause.
- `:quant 1 :unit 篇` for 一篇.
- `刊 :mod 该` for 该刊.
- The paper's coreference chain across sentences 16–20 (recall 100). Gold links each mention to 周报 (s17x4), and the chain scores the same either way.
- Reading the 被 passive as `贴到-01 :ARG0` agent, `:ARG2` theme, with `performance`.