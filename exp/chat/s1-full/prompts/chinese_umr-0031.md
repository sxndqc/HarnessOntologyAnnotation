# Skill: the UMR of a whole document

You annotate a whole document in Uniform Meaning Representation (UMR): every sentence's sentence-level
graph and alignment, then all the document-level relations (temporal, modal, coreference) of the
document. Follow the guidelines below. The document is under **Input** at the end, one sentence per line.

## Guidelines

The full UMR guidelines (umr4nlp/umr-guidelines `guidelines.md`, about 366,000 characters) are
attached to this message as `umr_guidelines.md`. Read them before you annotate. They often write the older
short names (AUTH, DCT, FullAff, :modstr); your answer uses the release names listed under Output format.


## Output format

Write plain text only (no JSON, no commentary). For every sentence, in order:

    # ::snt 1
    # sentence level graph:
    (s1t / taste-01
        :ARG0 (s1p / person
            :name (s1n / name :op1 "Edmund" :op2 "Pope"))
        :ARG1 (s1f / free-04
            :ARG1 s1p
            :aspect state)
        :temporal (s1t2 / today)
        :aspect performance)
    # alignment:
    s1t: 3-3
    s1p: 1-2
    s1n: 0-0
    s1f: 4-4
    s1t2: 5-5

then, once, after the last sentence, every document-level relation of the whole document in one graph:

    # document level relations:
    (d / document
        :temporal ((document-creation-time :depends-on s1t2)
                   (s1t2 :contained s1t)
                   (s1t :before s2c))
        :modal ((root :modal author)
                (author :full-affirmative s1t)
                (author :full-affirmative s2c))
        :coref ((s1p :same-entity s2p)))

- `# ::snt N` uses the sentence number of the input line. Every sentence gets a graph, even a short one.
- Variables of sentence N start with `s` + N and a letter (`s3p`, `s3x2`), all different. A node that
  fills two roles in one sentence is written once and then named by its variable.
- Alignment: one line per variable, `variable: first-last` with the word positions of the input line
  (counted from 1); `0-0` for a node with no word.
- Document level: `(parent :relation child)` triples, grouped under `:temporal`, `:modal`, `:coref`;
  each end is a variable of a sentence graph or a constant (`author`, `root`, `document-creation-time`,
  `past-reference`, `present-reference`, `future-reference`, `null-conceiver`).
- Use the names of the UMR release data: `author` (not AUTH), `document-creation-time` (not DCT),
  `full-affirmative`, `partial-affirmative`, `neutral-affirmative`, `neutral-negative`,
  `partial-negative`, `full-negative`, `unspecified` (not FullAff, ...), `:modal-strength` (not
  :modstr), `:refer-person` / `:refer-number` with lower-case values (`3rd`, `singular`), and lower-case
  aspect values (`performance`, `state`, ...).
- Write the whole document: do not stop early, do not summarise, do not skip sentences.

## Input

Language: zh
Document: chinese_umr-0031 (13 sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces
(the alignment refers to these word positions, counted from 1 in each sentence).

1	自 2025 年 1 月 7 日起 ， 一系列 持续 的 野火 影响 了 美国 加利福尼亚州 洛杉矶 都会区 及 周边 地区
2	这些 火灾 包括 帕利塞兹 火灾 、 伊顿 火灾 、 赫斯特 火灾 和 日落 火灾 ， 火势 因 极 低 的 湿度 、 长期 干旱 以及 飓风 块别 的 圣塔 安那 风 加剧 ， 某些 地区 的 风速 甚至 超过 每小时 80 英里 （ 130 公里 / 小时 ）
3	截至 1 月 15 日 ， 这些 野火 已 造成 25 人 死亡 ， 超过 1.3 万栋 建筑物 受损 ， 并 迫使 超过 20 万人 撤离
4	此次 风暴 及其 引发 的 火灾 危险 早 有 预兆
5	早在 1 月 2 日 ， 美国 国家 跨 部门 消防 中心 即 警告 南加州 将 出现 “ 高于 正常 水平 的 重大 火灾 潜力 ”
6	同日 ， 国家 气象局 在 地方 预报 中 也 提及 可能 发生 强烈 火灾
7	到 1 月 3 日 ， 风暴 预测 中心 进一步 预测 1 月 8 日 的 火灾 天气 将 达到 “ 严重 风险 ” 级别 ， 并 在 1 月 7 日 — — 首个 关键 火灾 天气 日 — — 将 1 月 8 日 的 风险级别 提升 至 “ 极端 关键 ”
8	针对 洛杉矶 及 文图拉 县 ， 国家 气象局 发布 了 红旗 警告 ， 指出 火灾 风险 极高 ， 并 形容 这 是 一种 “ 特别 危险 的 情况 ” ， 对 生命 及 财产 构成 重大 威胁
9	该 警告 强调 ， 强风 与 低 湿度 的 结合 将 导致 火灾 迅速 蔓延
10	自 2024 年 夏末 以来 ， 南加州 逐渐 进入 干燥 状态 ， 因为 风暴 系统 主要 影响 太平洋 西北部 及 北加州 ， 未 对 南加州 带来 有效 降雨
11	这 一 现象 是 厄尔尼诺 - 南方 涛动 现象 从 圣婴 向 拉尼娜 过渡 的 结果
12	2025 年 1 月 ， 拉尼娜 现象 已 形成 弱势 模式
13	到 2024 年 12 月 下旬 ， 洛杉矶 县 大部分 地区 已 陷入 中度 干旱 ， 这种 情况 导致 火灾 风险 在 雨季 中 持续 攀升
