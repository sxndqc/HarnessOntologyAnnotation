Almost everything was right. Every check except five scored 100. The points lost come from about five patterns, and two of them come from errors in the gold annotation itself.

## 1. Who is the conceiver of reported content (i_modal: 4 partial units, the biggest real loss)

**What went wrong.** The instruction says: "each content event gets **both** `(author :full-affirmative X)` and `(s9p :full-affirmative X)`." The annotator followed this rule exactly, and the gold does not follow it in two ways.

- **被指, with no speaker written (snt15).** For 被指与外星人P'Lod有暧昧关系，后来还领养外星宝宝, the annotation gave each content event both triples:
  - for 有: `(author :full-affirmative s15x2) (s15a :full-affirmative s15x2)`
  - for 领养: `(author :full-affirmative s15x6) (s15a :full-affirmative s15x6)`

  The gold has only the conceiver triple for the content events:
  - `(s15a :full-affirmative 有) (s15a :full-affirmative 领养)`

  The gold does keep `(author :full-affirmative s15a)` and `(author :full-affirmative 指)`. The author does not vouch for a rumour, so the `author` triple on its content is wrong. This is 2 units.
- **Events under a quoted claim (snt12).** In 宣称他们的报导都是真实的, the gold puts both triples on the quoted top node (`have-mod-91`) and on the slogan verb, which carries its own `:quote`. The 报导 that is only the subject *inside* the claim (s12x4) gets only `(author :full-affirmative …)`. The annotator also added `(s12n :full-affirmative s12x2)` there.

  The gold also adds `(s12n :full-affirmative s12x10)` for the 报导 in the 不过 clause (大部分的报导都以博君一笑为目的). That clause is not reported speech, so this triple is probably a gold quirk. Do not write a rule for it. This is 2 units.

**Change to the instruction.** Replace the "both" sentence with:
> "Reported content: the speaker node gets `(author :full-affirmative speaker)`. The **top content node** (the one carrying `:quote`) and any other node carrying its own `:quote` get both `(author …)` and `(speaker :full-affirmative …)`. Events nested inside a content node without their own `:quote` (e.g. the subject 报导 of 报导是真实的) get only the `author` triple. **Exception, 被指 / 据说 with no written speaker (an unverified claim):** the content events get **only** the conceiver triple `(<subject node> :full-affirmative X)`, with no `author` triple. `author` still gets `:full-affirmative` on the subject node and on 指."

Also update the 被指 example in the Examples list so that it shows this exception.

## 2. A slogan's verb is missing its owner as `:ARG0` (g_reentrancy: 1 missing edge)

**What went wrong.** In 他们的标语：「只报导事实：世界新闻周报！」 the annotation has `(s12x6 / 报导-01 :ARG1 (事实) :mod (只) …)` with no agent. The gold is `(s12x6 / 报导-01 :ARG0 s12n :ARG1 (s12x8 / 事实) :mod (s12x7 / 只) :quote s12i3 :aspect habitual)`.

**Why.** The annotator applied "never re-use a participant … every re-entrancy needs a pronoun or an overt word" and "a possessive 他们的 before an event noun adds no `:ARG0`." Here the slogan is a full clause, and its owner is overt as 他们的 on 标语 and inside the slogan itself (世界新闻周报).

**Change to the instruction.** Add an exception next to the control-verb exception:
> "The verb of a quoted slogan or motto whose owner is written (他们的标语：「只报导事实…」) takes that owner as `:ARG0` by re-entrancy."

Keep the existing rule for 他们的报导 (no `:ARG0`). The annotator got that one right on s12x2, which matches the gold.

## 3. Granularity mismatches (a_granularity: 3 missing and 3 extra units, mostly a matching problem)

**What happened.** The graphs here match the gold node for node:
- `(网络版 :part-of (周报))`
- `company :name "美国" "媒体" "公司"`
- `外星人 :name "P" "'" "Lod"`
- `individual-person :name "外星人" "P" "'" "Lod"`

The scored annotation has no alignment block, so umrjudge paired the gold short repeat 周报 with the wider `newspaper` node, and the gold P'Lod with the wider 外星人P'Lod span.

**Change to the instruction.** Section 6 should say the alignment block is **required output** for every sentence. It should also give these cases explicitly:
- a shortened repeat (周报) is aligned to its own single word;
- in 母公司美国媒体公司, `公司 :mod 母` is aligned to 母公司 and `company` to the name words only;
- in running text, 外星人 P'Lod's `外星人` node is aligned to the 外星人 word, apart from the name words.

## 4. Temporal parent of 出现 in snt13 (h_temporal: 1 extra and 1 missing unit, a gold error)

The gold writes `(s13x :overlap s13x6)`. s13x6 is 航天员, an entity, so this is almost certainly a mistyped variable for 出现. The annotator's `(s13x12 :overlap s13x14)` follows the instruction's rule that relative-clause events hang from their governing event. **Change nothing.**

## 5. Sense of 领养 (b_event_sense: 1 unit, a gold quirk)

The annotator wrote `领养-01`; the gold has `领养-00`. Chinese PropBank does have `领养-01` (ARG0 agent), so the annotator followed the "look the verb up first" rule correctly. **Do not add a rule.** Writing one to chase this gold label would cause errors on other documents.

## What to keep

- **The sentence-graph rules** worked perfectly here: concepts, aspect, core and peripheral roles, name tokens and coreference chains were all at 100%. In particular, keep:
  - the 改为 / 母公司 / apposition rules, and `网络版 :part-of (周报)` with the in-sentence `:same-entity`;
  - the slogan and quote structure (`have-mod-91 :quote 宣称`, `identity-91 :aspect state`);
  - `but-91 :ARG1 (and …)` for 虽然…不过;
  - the 算是 / `implicit-argument` / `have-degree-91 :ARG5 (其中)` pattern, with `(author :neutral-affirmative 算是)`;
  - the 被指 → `(consecutive :op1 有-03 :op2 领养)` structure, with the `and` subject as conceiver and `(有 :after 领养)`;
  - the list rules: `:example (and … :op6 (等))`, `individual-person` for the characters in a 如 list, and a bare `外星人 :name` in running text.
- **The temporal rules:**
  - for the date: `(document-creation-time :before date)` then `(date :overlap 停止)`;
  - for a purpose event: `:overlap`;
  - for snt14: `document-creation-time :before 算是`.
- **The coreference restraint:** only same-entity chains, no `:subset-of` from 其中. This gave 100%.