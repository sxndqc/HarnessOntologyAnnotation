# guideline 修订清单（待填写）

填法：每一行最后一列“决定”里写选项字母（A、B……），或直接写你要的写法；不改就写“不改”。“建议”是我的意见，不是结论。

数字的来源：
- **完整版** = `resources/guidelines/umr_guidelines.md`（8,721 行）里出现的次数。
- **精简版** = `resources/guidelines/umr_guidelines_abridged.md` 里出现的次数。
- **clean** = `resources/training/training-clean/` 里出现的次数，按语言写成 中/英/捷/Arapaho/Navajo。
- 都是字符串计数，没有逐处看上下文。

修订对象是本地这两份文件，不管网上的版本。

---

## 一、clean 训练数据的现状

| 语言 | 文件 | 句 | 词 | 节点 | 时间关系 | 模态关系 | 共指关系 |
|---|---|---|---|---|---|---|---|
| 中文 | 20 | 557 | 15,375 | 11,304 | 2,388（535 句有） | 3,533（541 句有） | 647（359 句有） |
| 英语 | 4 | 180 | 2,023 | 1,222 | 218（131 句有） | 402（146 句有） | 337（164 句有） |
| 捷克语 | 6 | 103 | 1,587 | 1,336 | 0 | 0（改在图里写 `:modal-strength`，414 处） | 340（98 句有） |
| Arapaho | 1 | 53 | 274 | 299 | 87 | 113 | 135 |
| Navajo | 1 | 5 | 60 | 56 | 15 | 19 | 3 |
| 意大利语 | 0 | | | | | | |
| 拉丁语 | 0 | | | | | | |

要注意的几点：

1. **意大利语、拉丁语没有 clean 数据。** 只用 clean 之后，这两种语言的 `search_annotations` 没有任何结果。Navajo 只有 5 句，实际上也接近没有。
2. **中文 clean 的 20 个文件里有 18 个就是我们评测的 18 篇非测试中文文档**（chinese_umr-0001 到 0018，即 zh-0001 到 zh-0018）。工具标注某一篇时会跳过同名文件和原文相同的句子，所以不会直接泄漏答案；但 `data/gold` 里这 18 篇用的是第一轮给的在审版本，和 clean 里的同名文件内容不同（18 篇全部有差别，例如 0001 差 211 行、0010 差 864 行）。也就是说“训练数据”和“被评测的 gold”是同一批文档的两个版本。
3. **捷克语 clean 没有文档级时间和模态**，只有共指；模态强度写在句子图里。英语 clean 也有 75 处图内 `:modal-strength`，中文只有 2 处。
4. **英语 clean 很不均衡**：180 句里 141 句来自 english_umr-0004 一个文件，平均每句 8 个词。
5. **中文 clean 的对齐**：11,303 条对齐里 3,947 条是 0-0（没有对应的词），约 35%。
6. **clean 内部各语言写法不一样**（下面各表的 clean 一列能看到），例如 `have-org-role-91` 中文 51 处、捷克语 15 处，而英语全用 `-92`；`:contains` 只在 Arapaho（16）和英语（3）出现；`individual-person` 只有中文用（272 处）。所以“照 clean 数据统一”在有些条目上本身没有唯一答案。
7. **格式问题**：chinese_umr-0017 有一处 `:ratio-of 330`（打分器读不了），chinese_umr-0007 有一处重复的三元组；英语有 2 处 `:subset`（应为 `:subset-of`）；中文有 1 处 `strong-partial-affirmative`（不在取值表里）。

---

## 二、角色名、属性名、取值的拼写（guideline 和 clean 不同）

| 编号 | 问题 | 完整版 | 精简版 | clean（中/英/捷/Arp/Nv） | 选项 | 建议 | 决定 |
|---|---|---|---|---|---|---|---|
| 2.1 | 领属角色 | `:poss` 28 | `:possessor` 1 | `:possessor` 141/17/4/1/0；`:poss` 0 | A 全改 `:possessor`　B 保留 `:poss` | A | A |
| 2.2 | 模态强度属性名 | `:modstr` 336 | `:modal-strength` 2 | `:modal-strength` 2/75/414/0/7 | A 全改 `:modal-strength`　B 保留 `:modstr` | A | A |
| 2.3 | 模态强度取值 | `FullAff`、`PrtAff`、`NeutAff`、`FullNeg`、`PrtNeg`、`NeutNeg`、`Unsp` | 全称小写 | `full-affirmative` 等全称小写 | A 全改全称小写　B 保留缩写 | A | A |
| 2.4 | 人称、数属性名 | `:ref-number` 307、`:ref-person` 167；`:refer-*` 各 2 | `:refer-*` 8，`:ref-person` 1 | `:refer-number` 96/244/418/69/4；`:ref-*` 0 | A 全改 `:refer-*`　B 保留 `:ref-*` | A | A |
| 2.5 | 人称、数取值大小写 | `Singular`、`Plural`、`Dual` 等首字母大写 | 小写 | 小写 | A 全改小写　B 保留 | A | A |
| 2.6 | aspect 取值大小写 | `Performance`、`State` 等首字母大写（约 340 处） | 小写 | 小写（`performance` 1,575 等） | A 全改小写　B 保留 | A | A |
| 2.7 | aspect 属性名大小写 | `:Aspect` 5、`:aspect` 352 | `:aspect` | `:aspect` | A 全改 `:aspect` | A | A |
| 2.8 | 引语关系 | `:quot` 16 | `:quote` 1 | `:quote` 138/26/98/20/5 | A 全改 `:quote`　B 保留 `:quot` | A | A |
| 2.9 | 元节点名 | `DCT` 39、`AUTH` 87、`ROOT` 8 | 全称 | `document-creation-time` 509、`author`、`root` | A 全改全称小写　B 保留缩写 | A | A|
| 2.10 | 时间参照节点 | `PAST_REF` 20、`PRESENT_REF` 5、`FUTURE_REF` 2、`Future_Ref` 2 | 全称 | `present-reference` 25、`past-reference` 5 | A 全改 `past-reference` 等　B 保留但统一成一种大写写法 | A | A |
| 2.11 | 文档级模态里的旧标签 | `:MODAL` 4、`:AFF` 3、`:NEUT` 1 | 无 | `:modal` 598/137/0/0/3 | A 改成 `:modal`、`:full-affirmative`、`:neutral-affirmative`　B 保留 | A | A |
| 2.12 | 疑问 | `umr-unknown` 2 | `amr-unknown` 2 | `umr-unknown` 5/4/11/3/0；`amr-unknown` 0 | A 全用 `umr-unknown`（改精简版）　B 全用 `amr-unknown` | A | A |
| 2.13 | 核心角色大小写 | `:ARG0` 640、`:arg0` 8 | `:ARGn` | `:ARGn` | A 全改 `:ARGn` | A | A |
| 2.14 | `:MODSTR`、`:Actor`、`:Undergoer` 等零星大写 | 各 1 处 | 无 | 无 | A 全改小写 | A | A |

---

## 三、同一件事有两种角色或两种方向

| 编号 | 问题 | 完整版 | 精简版 | clean（中/英/捷/Arp/Nv） | 选项 | 建议 | 决定 |
|---|---|---|---|---|---|---|---|
| 3.1 | 时间包含关系 | `:contained` 34、`:includes` 4、`:contains` 0 | `:contained` 2、`:contains` 1 | `:contained` 60/9/0/3/3；`:contains` 0/3/0/16/0 | A 只留 `:contained`，`:includes`、`:contains` 改写成反方向的 `:contained`　B `:contained` 和 `:contains` 都留，`:includes` 改 `:contains`　C 三个都留 | 请你定 | A |
| 3.2 | 部分和整体 | `:part` 8（都是部分为父节点、指向整体），`:part-of` 0 | `:part` / `:part-of` 并列 | `:part` 164/9/10/7/3；`:part-of` 68/4/0/7/1 | A 只用 `:part`，部分为父节点（现在的处理）　B 只用 `:part`，整体为父节点　C `:part` 和 `:part-of` 都留，各写明方向 | 请你定 | 部分为父节点的情况全部改成part-of，整体为父节点保留part|
| 3.3 | 组织角色谓词 | `have-org-role-92` 8，`-91` 0 | `-92` 2 | `-91` 51/0/15/0/0；`-92` 3/9/1/0/0 | 已定：`-92` | 已定 | 已定 |
| 3.4 | 亲属、关系角色谓词 | `have-rel-role-92` 14，`-91` 0 | `-92` 2 | `-91` 28/0/0/0/0；`-92` 0/1/2/1/0 | 已定：`-92` | 已定 | 已定 |
| 3.5 | 量词 | `:unit` 31 | `:unit` 4 | `:unit` 331/9/21/0/0 | 已定：保留 `:unit`，漏标要补 | 已定 | 已定 |
| 3.6 | 地点角色 | `:place` 20、`:location` 5 | `:place` 1 | `:place` 402（合计）；`:location` 0 | A `:location` 全改 `:place`　B 保留 | A | A |
| 3.7 | 原因角色 | `:cause` 5、`:reason` 0 | `:cause` 4、`:reason` 1 | `:cause` 34/2/1/0/0；`:reason` 35/6/1/0/1 | A 只用 `:cause`　B 只用 `:reason`　C 两个都留并写明区别 | 请你定 | C, reason是理由，cause是原因 |
| 3.8 | 时间角色 | `:temporal` 92；`:time` 5（多在 date-entity 里） | `:temporal` 4 | `:time` 44/0/0/0/1 | A `:time` 只用于 date-entity 的钟点，别处一律 `:temporal`　B 保留现状 | A | A |
| 3.9 | 程度 | `:degree` 11 | `:degree` 3 | `:degree` 29/5/6/5/0；`:extent` 8/9/9/0/0 | A 只用 `:degree`　B 两个都留并写明区别 | 请你定 | B |
| 3.10 | `:modpred` | 26 处（Part 4-3-1-2 整节） | 0 | 0 | A 删掉这一节的写法，改成现行的文档级模态写法　B 保留，注明训练数据不用　C 保留不动 | 请你定 | A |
| 3.11 | `:subset-of` 的方向 | 7 处 | 2 处 | 32/43/37/4/0 | A 成员在前（`(成员 :subset-of 集合)`）　B 集合在前　C 两种都接受 | 请你定 | 成员在前 |
| 3.12 | 人的实体类型 | `individual-person` 1、`person` 多处 | `person` | `individual-person` 272/0/0/0/0；`person` 67/179/188/89/8 | A 全用 `person`　B 中文用 `individual-person`　C 两种都接受 | 请你定 | C |
| 3.13 | 地名类型 | AMR 类型（city、country 等） | AMR 类型表 | `human-settlement` 0/5/12/2/0；`city` 84/0/0/0/0 | A 用 AMR 类型（city、state……）　B 用 UMR 新类型（human-settlement、country-partition……）　C 两种都接受 | 请你定 | C |

---

## 四、示例的格式

| 编号 | 问题 | 现状（完整版） | 选项 | 建议 | 决定 |
|---|---|---|---|---|---|
| 4.1 | 变量命名 | 句子级示例多用 `x`、`p2`（约 54 处开头），文档级示例用 `s1x`（约 23 处开头）；clean 数据全是 `s1x` | A 全部改成 `s1x` 式　B 只在带文档级标注的示例里用 `s1x`　C 不改 | A | A |
| 4.2 | 斜杠两边的空格 | `(c/ car` 1,356 处，`(c / car` 77 处 | A 全改 `(c / car`　B 不改 | A | A |
| 4.3 | 文档级示例的写法 | 有的写成 `:temporal ((DCT :before s1x))` 的片段，有的只在正文里叙述 | A 全部改成 clean 数据的三段式（`:temporal`、`:modal`、`:coref` 各一段，套在 `(s1s0 / sentence ...)` 里）　B 只统一标签，不改结构 | A | A |
| 4.4 | 并排对照的示例 | 两个图用制表符并排（2,535 行含制表符），在纯文本里错位 | A 拆成上下两个代码块　B 不改 | A | A |
| 4.5 | 缩进 | 制表符和空格混用 | A 全改 4 个空格 | A | A |
| 4.6 | 概念后面的释义 | `(k/ kedam 'shoe')` 这类 75 处，不是合法的 UMR | A 把释义移到图外的注释行　B 保留 | A | A |
| 4.7 | HTML 标签 | `<span>` 387、`<a>` 263、`<pre>` 204、`<br>` 29、`<div>` 16、`<table>` 7 | A 全部去掉，示例编号改成纯文本，表格改 Markdown　B 只去掉 `<span>` 和 `<br>` | A | A |
| 4.8 | 示例编号 | `3-2-2-2 (1a)` 式的 `<span>` 锚点，另有 `Snt`、`snt`、`1.` 等写法 | A 统一成“例 3-2-2-2 (1a)”一行纯文本　B 不改 | A | A |
| 4.9 | 示例里的 `:wiki` | 66 处 | A 保留　B 全部删掉（judge 已不判 `:wiki`） | 请你定 | B |
| 4.10 | 非英语示例的词形 | 有的带词素切分和逐词释义，有的只有译文 | A 统一成“原文、逐词释义、译文、图”四行　B 不改 | B（工作量大） | B |

---

## 五、文档结构

| 编号 | 问题 | 现状（完整版） | 选项 | 建议 | 决定 |
|---|---|---|---|---|---|
| 5.1 | 目录和标题对不上 | 目录 87 项，正文只有 72 个“Part”标题（3-1-2、3-1-3、3-1-5、3-2-1、3-2-2、3-2-2-1、3-2-2-2 等缺标题） | A 按目录补齐标题　B 不改 | A | A |
| 5.2 | 标题层级 | 有的四级小节用了 `####`，有的同级用 `#####`（如 4-2-2-1） | A 按编号深度统一层级 | A | A |
| 5.3 | 内部链接 | 链接到 `#part-…`、`#3-2-2-2 (2a)` 等锚点，去掉 HTML 后会失效 | A 改成“见 Part x-x”纯文本　B 重建锚点 | A | A |
| 5.4 | 标题里的版本信息 | “UMR 0.9 Specification，August 8, 2022”，还有 `-AUTHORS-` 占位 | A 改成“本地修订版”并写明修订日期和依据　B 不改 | A | A |
| 5.5 | 第 7 部分的索引 | 按字母排列的类别索引，里面的角色名是旧写法 | A 跟着第二、三节的决定一起改　B 删掉索引 | A | A |
| 5.6 | 泄漏：en-0008 的句子在两份 guideline 里 | 精简版第 1 节直接含 en-0008 第 3 句的 gold 标注 | A 换成不在测试集里的句子　B 保留，评测时去掉 en-0008　C 不改 | 请你定 | C |
| 5.7 | 精简版要不要同步 | 精简版和完整版在 2.12、3.1、3.2 上写法不同 | A 完整版改完后同步精简版　B 只改完整版 | A | A |
| 5.8 | 已定规则写进 guideline | `:unit` 保留、`-91` 改 `-92` 目前只在我们的记录里 | A 写进两份 guideline　B 不写 | A | A |

---

## 六、还没定的标注规则（这部分放这里就行了，不用写进guideline）

这些来自 `analysis/error-patterns.md` 第四部分；上面已经列过的（`:poss`、`:modpred`、`:subset-of`、`individual-person`、实体类型、`umr-unknown`）不重复。

| 编号 | 问题 | 选项 | 决定 |
|---|---|---|---|
| 6.1 | Navajo 等语言的抽象谓词论元编号：训练数据 have-role-91、have-quant-91、identity-91 用 `:ARG0/:ARG1`，guideline 表是 `:ARG1/:ARG3`、`:ARG1/:ARG2` | A 按 guideline 表　B 按训练数据　C 两种都接受 | guideline是对的，把Navajo的数据全改好 |
| 6.2 | `(root :modal author)` 每句要不要写；图内 `:modal-strength` 和文档级模态是否等价 | A 每句必写，图内强度不用　B 两种都接受 | A |
| 6.3 | 时间表达挂在元节点上用 `:depends-on` 还是 `:overlap` / `DCT :before` | A `:depends-on`　B 两种都接受 | B |
| 6.4 | 捷克语、拉丁语的系词、情态动词、轻动词立不立节点（být-007、zona-07、lze-001） | A 按 guideline（have-mod-91 等，情态用强度）　B 按训练数据　C 两种都接受 | B |
| 6.5 | PDT 转来的角色（`:clausal-marker`、`:effect`、`:regard`、`:part-of-phraseme`、`:comparison`） | A 不接受，改成 UMR 角色　B 接受 | A |
| 6.6 | 捷克语旧写法：日期、数词、序数写成 `:mod`；专名不作命名实体；言说内容用 `:effect` | A 按 guideline　B 两种都接受 | |
| 6.7 | 事件名词、施事名词谓词化到什么程度 | A 能谓词化就谓词化　B 保留名词也算对　C 换了词义的不算对 | |
| 6.8 | Navajo nihił 加第三人称动词：按词素（飞机为主体、我们为 `:companion`）还是按译文（我们飞） | A 按词素　B 按译文　C 两种都接受 | |
| 6.9 | Arapaho、Navajo 的词干切分写法 | A 定一份规则（请说明）　B 不统一，差别不计 | |
| 6.10 | 中文方位词、时间方位词（上、中、时、后）建不建节点 | A 建　B 不建 | A |
| 6.11 | 名字里的书名号、引号 | A 去掉　B 保留 | |
| 6.12 | 间接转述加不加 `:quote` | A 只有直接引语加　B 间接转述也加 | |
| 6.13 | 嵌入的是非问“是否” | A `:polarity umr-unknown`　B `truth-value`　C 其他（请写） | |
| 6.14 | “是 X”的类别归属 | A identity-91　B have-role-91　C 按情况（请写规则） | |
| 6.15 | 指示词加量词（这种、此次）、频次里的“次”要不要补 `:unit` | A 补　B 不补 | |
| 6.16 | 中文复数名词标不标 `:refer-number plural` | A 标　B 不标　C 只在有“们”等标记时标 | |
| 6.17 | `:part` 以部分为父节点（上一个会话按完整版 3-2-2-1 的处理，未经你确认） | 见 3.2 | |
