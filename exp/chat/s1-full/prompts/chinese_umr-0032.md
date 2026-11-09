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
Document: chinese_umr-0032 (6 sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces
(the alignment refers to these word positions, counted from 1 in each sentence).

1	中国 和 日本 就 福岛 核电站 废水 排海 问题 达成 共识 ， 中国 将 参与 独立 国际 监测 ， 并 逐步 恢复 日本 水产 进口
2	中国 官媒 报道 ， 中国 和 日本 主管 部门 持续 多轮 磋商 福岛 “ 核 污染 水 ” 排海 问题 后 ， 日本 欢迎 在 国际 原子能 机构 框架 下 设立 确保 中国 等 利益 相关 国家 有效 参与 ， 并 确保 独立 采样 和 实验室 分析 的 长期 国际 监测 安排 ， 中国 将 在 实施 监测 措施 后 ， 基于 科学 证据 逐步 恢复 符合 标准 的 日本 水产 进口
3	日本 首相 岸田 文雄 表示 ， 国际 原子能 机构 将 扩展 对 “ 处理 水 ” 排海 的 监测 计划 ， 而 目前 他 不知道 中国 具体 何时 会 恢复 进口 日本 水产
4	福岛 第一 核电厂 受 2011 年 东日本 大地震 及 引发 的 海啸 损毁 ， 导致 冷却 系统 停止 运作 ， 东京 电力公司 注入 海水 直接 冷却
5	使用 后 的 核废水 经 12 年 已 储存 30万吨 ，于 去年 开始 分批 排放 ，预计需时 40 年
6	日本 称呼 核废水 为 “ 处理水 ” ， 中国 称为 “ 核污染水 ”
