Overall the annotation came close to gold: concepts, senses, core roles, names, temporal links and coreference all scored 100. The points it lost come from a few rules that are missing or wrong in the instruction. Most costly first:

### 1. The tabloid 《国家询问报》 in snt7 was attached in the wrong place: subject of 改为 instead of `:part-of` the old layout
**Cost:** g_reentrancy 2 of 2 units (F = 0), d_peripheral_entity 2 units (one missing, one extra). This is the biggest loss.

- **Words:** 旗下的八卦小报《国家询问报》将由黑白版面改为彩色版面 … 不符合《国家询问报》标准的文章
- **What the annotator did:** It built the full tabloid node (name plus `identity-91` 小报) at the second mention, under 标准 `:possessor`. It then re-entered that node as `改为-01 :ARG0 s7n5`, and the old 版面 had only `:mod 黑白`.
- **Gold:**
  ```
  (改为-01 :ARG1 (版面 :part-of (s7n / newspaper :name … :ARG1-of (identity-91 :ARG2 (小报 :mod 旗下 :mod 八卦))) :mod (黑白))
           :ARG2 (版面 :mod (彩色)))
  … (标准 :possessor s7n)
  ```
- **Why it happened:** The instruction pulls in two directions:
  - "由 X 改为 Y: X is `:ARG1`" and its example `改为 :ARG1 (版面 :mod (黑白))` show no `:part-of`.
  - The `:part-of` rule only covers 纸本 / 网络版 / 分部, and only "when the whole is written with it".
  
  So the annotator had nowhere to put the topic-subject 小报 except `:ARG0`. That also breaks the instruction's own ban on filling unexpressed agents.
- **Change:**
  1. Add: "In `<Whole> 由 X 改为 Y`, when X and Y are parts or features of the subject (版面, 颜色, 名称), 改为 has no `:ARG0`. The subject is `:part-of` on X (`改为 :ARG1 (版面 :part-of <newspaper>) :ARG2 (版面 …)`)."
  2. Fix the 改为 example to show this.
  3. Add a general rule: "Build a repeated entity in full (name, apposition) at its first mention in the graph, and use a bare variable re-entrancy (`:possessor s7n`) for later mentions in the same sentence."

### 2. The 发行 inside 发行量 should get no `:aspect` and no modal triple
**Cost:** c_aspect 2 extra units, i_modal 2 extra units (precision 88).

- **What the annotator did:** snt9 and snt10 had `(发行-01 :ARG1 … :aspect habitual)` plus `(author :full-affirmative s9f)` / `(author :full-affirmative s10f)`.
- **Gold:** `(量 :quant-of (发行-01 :ARG1 …))` with no aspect and no modal parent. Its temporal link `(达到 :overlap 发行)` is kept.
- **Why it happened:** The annotator followed the instruction. Section 2.2 says the inner V-01 "is an event (aspect, temporal parent…, modal parent)", and that rule is wrong.
- **Change:** Rewrite it as: "the inner V-01 of a V+量 compound gets **no** `:aspect` and **no** modal triple; it only gets the temporal triple `(<governing verb> :overlap V)`." Also remove "aspect" from the 发行量 example.

### 3. Aspect of a purpose event and of a relative-clause event in a founding sentence
**Cost:** c_aspect 2 units.

- **Purpose event 运用 (为充分运用…):** the annotator had `performance`; gold has `activity`. A purpose is something intended and ongoing, not a completed event, even when the text presents it as realized. Section 5.2 tells the annotator to treat a realized purpose as full-affirmative, and that seems to have pushed it towards `performance`.
  - **Add to 4.1:** "A purpose event (为/为了 X, `have-purpose-91 :ARG2`) is `activity`, not `performance`, even when it is modally full-affirmative."
- **Relative-clause event 容纳 (版面 :ARG0-of 容纳 …文章):** the annotator had `habitual`; gold has `process`. The cue "recurring activities of a publication … are habitual" was applied too widely.
  - **Narrow that cue:** "The habitual rule is only for the publication's own recurring verbs (发行, 报导, 印刷, 综合) used as predicates. A relative clause that describes what a newly founded thing was designed to do (容纳…文章的版面) is `process`."

### 4. Named persons should be `individual-person`
**Cost:** a_entity_concept 1 unit.

- **What the annotator did:** 格内洛索·波普 was annotated as `person :name …`.
- **Gold:** `individual-person`. Other Chinese gold files do the same (凯蒂·佩芮, 张启楷 → `individual-person`).
- **Change:** In 2.2, add `individual-person` as the type for a named human in Chinese documents. Keep `person` for pronouns and unnamed people.

### What to keep
These rules gave full scores here and should stay as they are:
- the nested `have-reason-91` / `have-purpose-91` root, with `:aspect state` and full-affirmative modal;
- the temporal chain: `(创立 :before 改为)`, `(运用 :before 遗留)`, `(s7x :overlap s8x)`, and the date anchoring `(document-creation-time :before date)` `(date :overlap event)`;
- the 发行量 structure (`量 :quant-of`, `have-quant-91 :ARG2 … :unit (份)`, theme as `:ARG0` of 达到/跌);
- 该刊 → `(刊 :mod 该)`, 已经 → `:mod`, and the whole-concept compounds (创始人 via `have-org-role-91` + 创始-00);
- the 符合 negation as `:polarity -` plus `full-negative`;
- the coreference chain 周报 → 刊 → 周报 → 刊.