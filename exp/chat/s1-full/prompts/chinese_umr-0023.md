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
Document: chinese_umr-0023 (17 sentences)

The document, one sentence per line: the sentence number, a tab, then its words separated by spaces
(the alignment refers to these word positions, counted from 1 in each sentence).

1	载人 航天 是 指 由 宇航员 执行 的 太空 探索 ， 可以 由 单人 或 多人 执行 ， 惟 均 需 使用 载人 航天器 进行 。
2	目前 为止 只有 苏联 及其 继承 国 俄罗斯 、 美国 、 中华人民共和国 三个 国家 有 能力 独立 完成 载人 航天 。
3	历史 上 首次 载人 航天 任务 是 1961 年 4 月 12 日 苏联 发射 的 东方 1 号 ， 苏联 宇航员 尤里 · 加加林 在 环绕 地球 轨道 一周 后 安全 返回 地球 。
4	5 月 5 日 ， 艾伦 · 雪帕德 执行 自由 7 号 时 成为 了 第一个 进入 太空 的 美国 宇航员 ， 也 是 人类 历史 上 第二 人 ， 航天器 在 太空 停留 了 15 分钟 。
5	1963 年 6 月 16 日 ， 苏联 宇航员 瓦莲京娜 · 捷列什科娃 执行 东方 6 号 任务 时 成为 了 第一 名 进入 太空 的 女性 。
6	中国 则 是 第三个 尝试 追赶 美 苏 的 国家 ， 但 载人 计划 在 1973 年 被 中途 取消 ， 直到 三十 年 后 的 2003 年 ， 中国 的 航天员 杨利伟 乘坐 神舟五号 ， 成功 围绕 地球 十四 圈 并 安全 返回 地球 ， 标志 着 中国 成为 第三个 有 能力 独立 完成 载人 航天 的 国家 。
7	目前 除 俄 美 中 三国 外 ， 还有 欧洲 空间局 、 日本 、 印度 、 伊朗 、 马来西亚 等 国家 和 机构 也 在 计划 实施 载人 航天 。
8	1966 年 ， 美国 的 双子星 11 号 创造 了 最高 地球 轨道 记录 ， 飞行 高度 达 1374 公里 。
9	发射 和 修理 哈勃 太空 望远镜 的 两次 航天 飞机 任务 也 曾 达到 600 公里 左右 的 飞行 高度 。
10	迄今为止 ， 载人 航天 飞行 目标 在 地球 轨道 之外 的 任务 只 限于 月球 ， 尽管 月球 本身 也 是 地球 的 卫星 。
11	第一次 去 月球 的 载人 任务 阿波罗8号 中 ， 三位 宇航员 曾 进入 月球 轨道 。
12	阿波罗10号 第二次 环绕 了 月球 ， 在 月球 轨道 进行 了 登月 航天器 的 测试 。
13	阿波罗 11 号 至 17 号 中 除了 13 号 的 六 次 任务 都 成功 登月 ， 每次 都 有 两 名 宇航员 踏上 了 月球 。
14	于是 有 十二 名 宇航员 在 执行 阿波罗 计划 任务 时 完成 了 登月 的 壮举 ， 并 全部 安全 返回 。
15	某些 情况 下 ， 人类 以外 的 动物 也 曾 乘坐 航天器 进入 太空 ， 也 曾 有 过 多次 没能 返回 地球 的 情况 。
16	狗 是 第一 批 进入 太空 的 大型 哺乳 动物 。
17	随着 航天技术 从 学术 及 公用 领域 走入 民间 ， 载人航天 也 开始 迈向 商业化 ， 并 使 包括 太空旅游 在内 的 商业 太空 飞行 成为 现实 。
