# s3 / a2 的系统性错误分类（附例子）

数据来源：`review/items/*.json` 里的逐条审阅判断，共 11675 个比较点、45 篇文档（审阅还在进行，这是 2026-11-20 下午的快照）。只统计 s3、a2 四份输出被判为「错」(bad) 或「轻微」(minor) 的选择，共 3972 条。分类是按条目的类别字段和关键词自动归的，边界上会有少量归错。

每条例子：文档和句号（哪几份输出，错／轻）比较点：系统的写法；较好的写法。审阅理由的第一句。最后是链接，点开是该输出里这一句（能定位时定位到出问题的那一行）和 gold 的同一句。

## 各类数量

| 类 | 错误 | 条目 | 涉及 s3（其中错） | 涉及 a2（其中错） | gold 同样写法 |
|---|---|---|---|---|---|
| M1 | 转述、引述的内容直接挂 author，丢掉说话人这一层 | 163 | 17（3） | 154（96） | 38 |
| M2 | 未实现的事件强度标错 | 320 | 112（14） | 243（84） | 48 |
| M3 | 每句机械地多写一条 modal 三元组 | 75 | 41（13） | 37（14） | 0 |
| C1 | 跨句共指漏连 | 304 | 111（6） | 216（58） | 145 |
| C2 | 共指连错 | 128 | 72（13） | 76（11） | 6 |
| T | 日期和时间词没有锚定或锚错 | 240 | 122（15） | 132（15） | 46 |
| Q | 量词没有保留为 :unit | 177 | 171（0） | 131（0） | 13 |
| NE | 命名实体的类型和名字 | 337 | 200（22） | 203（38） | 23 |
| S | 义项选错或把词拆开 | 157 | 104（5） | 68（13） | 15 |
| F | 给虚词立节点、过度谓词化、自造 -00 | 147 | 72（3） | 93（6） | 18 |
| N | 数值、序数、钟点、金额的写法 | 156 | 97（7） | 94（17） | 11 |
| R | 角色标签和论元分配 | 449 | 241（16） | 269（37） | 53 |
| D3 | 类别归属、职务、亲属名词的抽象谓词 | 185 | 113（10） | 105（13） | 30 |
| D2 | 小句之间的关系读错 | 161 | 98（9） | 81（12） | 6 |
| D1 | 小词或中心语没有进图 | 113 | 89（7） | 42（3） | 32 |
| A | aspect 取值 | 179 | 96（7） | 112（11） | 33 |
| P | 否定的位置和极性 | 23 | 12（3） | 14（2） | 1 |

另有 658 条是零散的单句结构问题（修饰语挂接、根的选择、另立节点不重入等），没有归成类。


## 一、文档级 modal

### M1　转述、引述的内容直接挂 author，丢掉说话人这一层

「X 表示／指出／认为／报道……」的内容应该挂在 X 这个 conceiver 下面，系统直接写成 `(author :full-affirmative 事件)`。这是 a2 最突出的系统性错误：逐句标注时文档级那一遍看不到完整的转述链。s3 很少犯。gold 自己也常这样写。

条目 163：涉及 s3 的 17 条（错 3），涉及 a2 的 154 条（错 96）；其中 gold 也是同样写法的 38 条。

- **zh-0001 第 15 句**（a2/r1、a2/r2，错）被指内容的 conceiver：`author :full-affirmative（领养、有关系）`。abridged 5.2：引述内容的 conceiver 是说话人；「被指」没有说出指称者，用 null-conceiver 或把「指」事件当 conceiver 都合规定。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0001.umr:819) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0001.umr:800) · [gold](data/gold/chinese_umr-0001.umr:897)
- **zh-0004 第 56 句**（a2/r1、a2/r2，错）「指」内容的 conceiver：`author :full-affirmative（不经过里昂斯）`；较好的写法：`里昂斯 :full-affirmative 为主、杀戮、逃跑、觉得`。guideline 5.2：转述内容的 conceiver 是说话人；「指这集以杀戮和逃跑为主，令人觉得沉闷」是里昂斯的看法（「令人觉得沉闷」归作者也说得通）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0004.umr:4366) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0004.umr:4321) · [gold](data/gold/chinese_umr-0004.umr:4234)
- **zh-0007 第 29 句**（a2/r1、a2/r2，错）声称内容（死者是三井）的 conceiver：`author :full-affirmative identity`；较好的写法：`说话人（日冲龙平等人）:full-affirmative identity`。guideline 5.2：引述内容以说话人为 conceiver，说话人由 author 确认。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:1864) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:1869) · [gold](data/gold/chinese_umr-0007.umr:1919)
- **zh-0008 第 5 句**（a2/r1、a2/r2，错）「认为」内容的 modal 父节点：`author :full-affirmative 内容事件`；较好的写法：`来源 :full-affirmative 为了（来源作认知者）`。guideline 5.2：引述或思想内容，作者确定认知者（来源），认知者确定内容，(来源 :full-affirmative 内容)。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0008.umr:351) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0008.umr:347) · [gold](data/gold/chinese_umr-0008.umr:321)
- **zh-0009 第 6 句**（a2/r1、a2/r2，错）引述内容（上市、价格）的 modal 父节点：`(author :full-affirmative 上市 …)`；较好的写法：`(苹果 :full-affirmative 上市 …)`。guideline 5.2：转述内容的 conceiver 是说话人，author 只对「指」本身确信；「会」是 predictive future，强度 full-affirmative。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0009.umr:352) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0009.umr:355) · [gold](data/gold/chinese_umr-0009.umr:357)
- **zh-0010 第 12 句**（a2/r1、a2/r2，错）网民认为的内容「本末倒置」的 modal：`author :full-affirmative identity/have-mod`；较好的写法：`网民 :full-affirmative 本末倒置`。精简版 5.2：引述的想法，作者确信说话人，说话人确信内容：(author :full-affirmative 网民)(网民 :full-affirmative 内容)。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0010.umr:1048) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0010.umr:1002) · [gold](data/gold/chinese_umr-0010.umr:1064)
- **zh-0014 第 2 句**（a2/r1、a2/r2，错）进行、出现 的 conceiver：`author`；较好的写法：`方济各`。这两条限制是方济各重申的内容，conceiver 是方济各（abridged 5.2）；a2 以 author 作 conceiver 丢了引述层。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0014.umr:176) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0014.umr:174) · [gold](data/gold/chinese_umr-0014.umr:88)
- **zh-0015 第 6 句**（a2/r1、a2/r2，错）表示 的内容（要求、酷似）的 modal：`author :full-affirmative 要求、酷似`；较好的写法：`学生 :full-affirmative 要求、酷似`。guideline 5.2：引述内容的 conceiver 是说话人（作者断言说话人，说话人断言内容）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0015.umr:421) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0015.umr:394) · [gold](data/gold/chinese_umr-0015.umr:376)
- **zh-0017 第 10 句**（a2/r1、a2/r2，错）指出内容的 modal：`author 直接 → 内容`；较好的写法：`author → 观察员 → 内容（高 neutral-affirmative）`。转述内容的 conceiver 是说话人（精简 guideline 5.2）；a2 两次都越过了观察员。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0017.umr:653) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0017.umr:663) · [gold](data/gold/chinese_umr-0017.umr:632)
- **zh-0018 第 8 句**（a2/r1、a2/r2，错）要求内容（保证、展开、进入）的模态父节点：`author :partial-affirmative 保证/展开`。guideline 5.2：要求一类谓词的补足语以该谓词（或要求者）为父节点，作者只确信「要求」本身。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0018.umr:790) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0018.umr:795) · [gold](data/gold/chinese_umr-0018.umr:619)
- **zh-0023 第 7 句**（a2/r1、a2/r2，错）「计划」内容的 modal：`(author :full-affirmative 航天)，计划的内容由作者直接断言`；较好的写法：`(计划 :unspecified 实施)`。精简 guideline 5.2：plan 一类谓词的补足语以该谓词为 modal 父节点，强度 unspecified。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0023.umr:727) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0023.umr:734) · [gold](data/gold/chinese_umr-0023.umr:563)
- **zh-0024 第 2 句**（a2/r1、a2/r2，错）被认为的内容的 modal 结构：`离开、访问 直接 author :full-affirmative`；较好的写法：`author → null-conceiver → 认为 :unspecified 离开（访问归 author）`。完整 guideline 4-1-2 (1a) 的 is believed to：(AUTH :FullAff NULL_BELIEVER)(NULL_BELIEVER :FullAff believe)(believe :Unsp worth)。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0024.umr:176) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0024.umr:172) · [gold](data/gold/chinese_umr-0024.umr:149)

### M2　未实现的事件强度标错

目的从句、补足语（试图、计划、要求、禁止、允许）、条件前件、被取消或被拒绝的事件，本该是 partial-affirmative、neutral、unspecified 或 negative，系统给了 author full-affirmative；s3 的问题更多是强度选得偏（用 unspecified 代替 partial，能力句给 neutral）。

条目 320：涉及 s3 的 112 条（错 14），涉及 a2 的 243 条（错 84）；其中 gold 也是同样写法的 48 条。

- **zh-0006 第 9 句**（s3/r1、s3/r2、a2/r1、a2/r2，错）「淘汰」的 modal：`author :full-affirmative 淘汰`。「淘汰豁免权」是免于被淘汰的权利，淘汰并没有被断言会发生；挂在 豁免 下或标否定/中性都可以，作者 full-affirmative 是错的。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0006.umr:590) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0006.umr:605) · [gold](data/gold/chinese_umr-0006.umr:606)
- **zh-0027 第 3 句**（s3/r2、a2/r1、a2/r2，错）「禁止」对「销售」的 modal 强度：`author :full-affirmative 销售`。完整 guideline 4-3-2：forbid / ban 一类的强否定义务对补足事件是 PrtNeg（partial-negative）。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0027.umr:161) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0027.umr:167) · [gold](data/gold/chinese_umr-0027.umr:178)
- **zh-0001 第 50 句**（a2/r1、a2/r2，错）目的「还债」的 modal：`author :full-affirmative 还债`；较好的写法：`卖 :unspecified 还债`。abridged 5.2：目的从句的事件挂在主事件（或 purpose 常量）下，强度 unspecified；作者并没有断言还债会发生，a2 的 full-affirmative 错得更远。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0001.umr:3761) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0001.umr:3760) · [gold](data/gold/chinese_umr-0001.umr:4044)
- **zh-0002 第 32 句**（a2/r1、a2/r2，错）「取得成功」的 modal：`author :full-affirmative 取得`；较好的写法：`不利 :unspecified 取得 / 成功`。「对调查行动取得成功不利」里成功是尚未实现的目标，作者没有断言成功；官员更不是 conceiver。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0002.umr:2316) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:2278) · [gold](data/gold/chinese_umr-0002.umr:2329)
- **zh-0005 第 9 句**（a2/r1、a2/r2，错）「参加」（目的）的 modal：`author :full-affirmative 参加`；较好的写法：`报名 :unspecified 参加`。参加工程兵是报名的目的，下一句说他没有被录取，作者并未断言参加发生；guideline 5.2 目的事件挂在主事件下（unspecified）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0005.umr:684) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0005.umr:682) · [gold](data/gold/chinese_umr-0005.umr:697)
- **zh-0007 第 3 句**（a2/r1、a2/r2，错）目的「调查」的 modal：`author :full-affirmative 调查`；较好的写法：`来到 :unspecified 调查`。目的小句的事件没有被断言发生，guideline 5.2 以主事件（或常量 purpose）为父节点、strength unspecified；partial-affirmative 说「大概会」，没有依据；a2 当作作者断言的事实。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:125) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:127) · [gold](data/gold/chinese_umr-0007.umr:135)
- **zh-0010 第 2 句**（a2/r1、a2/r2，错）被禁止的「收取」、被要求的「摒弃」的 modal：`author :full-affirmative 收取、摒弃`。精简版 5.2：补语事件以 modal 谓词（禁止、要求）为父节点、unspecified 或谓词蕴含的强度；gold 以政府为 conceiver，用禁止蕴含的负向、要求蕴含的正向强度，也说得通。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0010.umr:83) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0010.umr:85) · [gold](data/gold/chinese_umr-0010.umr:89)
- **zh-0012 第 6 句**（a2/r1、a2/r2，错）「为了缓解压力」的 modal：`author :full-affirmative 缓解`。目的事件只是意图，作者不断言它实现了（abridged 5.2：目的从句可用 purpose 常量作父节点；完整 guideline 4.3.1.1.3：意图为 partial 强度）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0012.umr:711) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0012.umr:744) · [gold](data/gold/chinese_umr-0012.umr:614)
- **zh-0014 第 1 句**（a2/r1、a2/r2，错）「受到」的 modal 父节点：`author :partial-negative 受到`。这是方济各「认为」的内容，conceiver 是方济各（或 认为 事件），abridged 5.2；「不应」是 partial-negative。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0014.umr:89) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0014.umr:86) · [gold](data/gold/chinese_umr-0014.umr:3)
- **zh-0015 第 6 句**（a2/r1、a2/r2，错）被要求的「着」的 modal：`author :full-affirmative 着`；较好的写法：`要求 :unspecified 着`。guideline 5.2：要求的补语以要求事件为父节点、强度 unspecified。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0015.umr:421) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0015.umr:394) · [gold](data/gold/chinese_umr-0015.umr:376)
- **zh-0016 第 14 句**（a2/r1、a2/r2，错）「返回工作地点」的 modal：`author :full-affirmative 返回`；较好的写法：`要求 :unspecified 返回`。返回是要求-02 的补语，abridged 5.2 应以要求为父节点；gold 越过要求直接挂指引。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0016.umr:1301) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0016.umr:1288) · [gold](data/gold/chinese_umr-0016.umr:1213)
- **zh-0018 第 8 句**（a2/r1、a2/r2，错）「不受任何阻碍」的模态：`author :full-negative 阻碍`。「不受任何阻碍地进入」是要求内容里被否定的事件，在其上级事件（进入/保证）下 full-negative 最直接；gold 挂在法官下用 neutral-negative，意思偏弱；a2 写成作者确信没有阻碍，错。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0018.umr:792) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0018.umr:798) · [gold](data/gold/chinese_umr-0018.umr:619)

### M3　每句机械地多写一条 modal 三元组

同一份输出里每一句都带 `(author :neutral-affirmative have-condition)` 或 `(author :full-affirmative null-conceiver)`，句子里并没有条件或匿名说话人。审阅时每篇只记一条，所以条目数远小于实际出现次数。s3/r2 在 zh-0007、zh-0021 全篇如此，a2/r1 在多篇如此。

条目 75：涉及 s3 的 41 条（错 13），涉及 a2 的 37 条（错 14）；其中 gold 也是同样写法的 0 条。

- **zh-0021 第 1 句**（s3/r1、s3/r2，错）多余的 conceiver 三元组：`(author :neutral-affirmative have-condition)`；较好的写法：`只有 author 及其断言`。这句没有条件句，have-condition 没有依据；null-conceiver 没有被任何事件用到，是多余的三元组。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0021.umr:72) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0021.umr:68) · [gold](data/gold/chinese_umr-0021.umr:3)
- **zh-0030 第 1 句**（s3/r1、s3/r2，错）多出的 (author :neutral-affirmative have-condition)：`有这条三元组`；较好的写法：`没有`。本句没有条件句；have-condition 常量只用作条件分句事件的父节点（guideline 5.2），s3 两次运行在每一句开头都加了这条空挂的三元组。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0030.umr:47) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0030.umr:47) · [gold](data/gold/chinese_umr-0030.umr:3)
- **zh-0033 第 1 句**（a2/r1、a2/r2，错）多余的 null-conceiver 三元组：`(author :full-affirmative null-conceiver)`；较好的写法：`没有这条`。null-conceiver 只用于文本里没有的 conceiver，author 下不需要挂一个 null-conceiver。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0033.umr:62) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0033.umr:62) · [gold](data/gold/chinese_umr-0033.umr:3)
- **zh-0001 第 1 句**（s3/r1，错）modal 里多余的三元组：`(author :full-affirmative 周报)：实体作 modal 子节点`；较好的写法：`没有多余三元组`。本句没有文本外的 conceiver，null-conceiver 下也没挂事件（s1f 两次运行几乎每句都加这一条）；modal 依存结构只管事件和 conceiver，周报不是 conceiver。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:2) · [gold](data/gold/chinese_umr-0001.umr:3)
- **zh-0007 第 1 句**（s3/r2，错）多出的非标准文档级三元组：`author :neutral-affirmative have-condition`；较好的写法：`没有这些三元组`。null-conceiver 只用于文本里没有的认知者，have-condition 只作条件小句事件的父节点（guideline 5.2），都不该由 author 直接支配；root :depends-on document-creation-time 等也不是 guideline 的结构。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0007.umr:72) · [gold](data/gold/chinese_umr-0007.umr:3)
- **zh-0026 第 1 句**（a2/r1，错）多余的 null-conceiver 三元组（全篇如此）：`(author :full-affirmative null-conceiver)`；较好的写法：`没有这条`。abridged 5.2：null-conceiver 只用于文本里没有出现的 conceiver；这几份标注每一句都加这一条，下面也不挂事件。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0026.umr:136) · [gold](data/gold/chinese_umr-0026.umr:3)
- **en-0008 第 1 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）多余的 null-conceiver：`(author :full-affirmative null-conceiver)，句中没有事件挂在它下面`；较好的写法：`不引入 null-conceiver`。guideline 5.2：null-conceiver 只用于文本中没有出现的 conceiver。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0008.umr:41) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0008.umr:41) · [gold](data/gold/en-0008.umr:3)
- **zh-0013 第 10 句**（s3/r1、a2/r1、a2/r2，轻）条件句前件「造口业」的 modal：`full-affirmative（傅崐萁 或 have-condition 作 conceiver）`。「造任何口业」是假设的前件，说话人并没有断言有人造了口业，不应是 full-affirmative。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0013.umr:898) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0013.umr:925) · [gold](data/gold/chinese_umr-0013.umr:689)
- **en-0005 第 2 句**（a2/r1、a2/r2，轻）a2 给 convict 另加 null-conceiver 父节点：`author 和 null-conceiver 两个父节点`；较好的写法：`只有 author :full-affirmative convict`。modal 依存每个事件一个父节点；a2 给 convict-01 多加一个 null-conceiver，多余。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0005.umr:145) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0005.umr:137) · [gold](data/gold/en-0005.umr:68)
- **en-0007 第 2 句**（a2/r1、a2/r2，轻）convict 多一个 null-conceiver 父节点：`author 和 null-conceiver 两个父节点`；较好的写法：`只有 author`。定罪是作者直接陈述的事实，modal 依存应是树，一个事件只挂一个父节点。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0007.umr:139) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0007.umr:137) · [gold](data/gold/en-0007.umr:74)
- **zh-0024 第 2 句**（s3/r1、s3/r2，轻）被认为的内容的 modal 结构：`author → 认为；null-conceiver :full-affirmative 离开（null-conceiver 无父节点）`；较好的写法：`author → null-conceiver → 认为 :unspecified 离开（访问归 author）`。完整 guideline 4-1-2 (1a) 的 is believed to：(AUTH :FullAff NULL_BELIEVER)(NULL_BELIEVER :FullAff believe)(believe :Unsp worth)。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0024.umr:241) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0024.umr:234) · [gold](data/gold/chinese_umr-0024.umr:149)
- **en-0006 第 1 句**（s3/r1，轻）fear 的 conceiver：`null-conceiver :full-affirmative fear（null-conceiver 没有挂到 author 下）`。害怕的人没有说出来。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0006.umr:46) · [gold](data/gold/en-0006.umr:3)


## 二、文档级共指

### C1　跨句共指漏连

a2 的文档级一遍只看前五句，超出窗口的专名、事件复述基本连不上；s3 漏的多是事件共指和普通名词。注意这一类里将近一半 gold 也没连。

条目 304：涉及 s3 的 111 条（错 6），涉及 a2 的 216 条（错 58）；其中 gold 也是同样写法的 145 条。

- **zh-0004 第 54 句**（a2/r1、a2/r2，错）「戴立克」「猪奴隶」与前文共指：`都不连`；较好的写法：`戴立克 连第 33 句，猪奴隶 连第 23 句`。guideline 5.3：连最近的前一个提及；第 33 句（及更近的第 40 句）都提到戴立克，gold 却连到第 3 句。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0004.umr:4025) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0004.umr:4019) · [gold](data/gold/chinese_umr-0004.umr:3929)
- **zh-0007 第 21 句**（a2/r1、a2/r2，错）金田一、一之濑惠一的跨句共指：`没有跨句共指`；较好的写法：`连到前文（s14 金田一、s11 惠一）`。两个人名都在前文出现过（第 14 句金田一、第 11 句一之濑惠一），guideline 5.3 要求连到最近的前一次提及。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:1294) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:1315) · [gold](data/gold/chinese_umr-0007.umr:1328)
- **zh-0010 第 9 句**（a2/r1、a2/r2，错）与第 1 句重复内容的共指：`没有连第 1 句`；较好的写法：`连了 发布、提及、整治（same-event）和 政府、文件（same-entity）`。第 9 句后半是第 1 句的复述，发布、提及、整治是同一事件，政府、文件是同一实体，应连。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0010.umr:624) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0010.umr:627) · [gold](data/gold/chinese_umr-0010.umr:661)
- **zh-0018 第 12 句**（a2/r1、a2/r2，错）以色列国防军与第 1 句的共指：`没有标`；较好的写法：`与第 1 句以色列国防军 :same-entity`。本句的以色列国防军就是第 1 句发动空袭的以色列国防军；a2 是逐句标注，文档级只看前五句，第 1 句已在范围外，可能因此漏标。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0018.umr:1039) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0018.umr:1040) · [gold](data/gold/chinese_umr-0018.umr:1026)
- **zh-0021 第 12 句**（a2/r1、a2/r2，错）基里巴斯、托克劳 的跨句共指：`没有连这两个专名`；较好的写法：`与第 1 句的基里巴斯、托克劳共指`。guideline 5.3：重复的专名连到前一个提及；基里巴斯、托克劳 见第 1 句。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0021.umr:1156) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0021.umr:1166) · [gold](data/gold/chinese_umr-0021.umr:1045)
- **zh-0001 第 13 句**（s3/r1，错）「他们」与周报的共指：`没有跨句 coref`。三处「他们」都指周报（编辑部），abridged 5.3 要求连到最近的前一次提及；句内多次出现应是一个变量（re-entrancy），不该另建节点再句内 coref。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:663) · [gold](data/gold/chinese_umr-0001.umr:756)
- **zh-0003 第 21 句**（a2/r1、a2/r2，错）总部、温哥华与前文同指：`都没有连`（gold 也这样写）；较好的写法：`总部连第 2 句，温哥华连第 11 句`。第 2 句「总部设于…列治文」说的就是这次迁到列治文的总部；温哥华是重复出现的地名，最近一次在第 11 句（温哥华华裔商人）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0003.umr:1905) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0003.umr:1925) · [gold](data/gold/chinese_umr-0003.umr:1938)
- **zh-0011 第 19 句**（a2/r1、a2/r2，错）「北洋政府」与第 9 句的共指：`没有连`（gold 也这样写）；较好的写法：`s9 北洋政府 :same-entity s19 北洋政府`。guideline 5.3：重复出现的专名要连共指；a2 逐句标注时第 9 句不在前五句的上下文里，所以没连上。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0011.umr:1212) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0011.umr:1205) · [gold](data/gold/chinese_umr-0011.umr:1160)
- **zh-0012 第 8 句**（a2/r1、a2/r2，错）「维基新闻」跨句共指：`没有共指`（gold 也这样写）；较好的写法：`第 2 句维基新闻 :same-entity 维基新闻`。同一专名重复出现，应链到上一次提及。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0012.umr:892) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0012.umr:927) · [gold](data/gold/chinese_umr-0012.umr:793)
- **zh-0027 第 15 句**（a2/r1、a2/r2，错）跨句共指：阿程、阿聪、中介、化学品：`没有共指`（gold 也这样写）；较好的写法：`连上前文的阿程、阿聪、中介、化学品等`。阿程、阿聪和「胶囊中的化学品」在第 4 句出现过，王姓中介最近在第 9 句出现，精简 guideline 5.3 要求连 :same-entity。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0027.umr:1406) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0027.umr:1395) · [gold](data/gold/chinese_umr-0027.umr:1299)
- **zh-0005 第 35 句**（s3/r1，错）人大常委会与第 31 句的共指：`没有连`（gold 也这样写）；较好的写法：`s31 全国人大常委会 :same-entity s35 全国人民代表大会常务委员会`。第 31 句「全国人大常委会」和本句全称是同一机构，名称重复也要连（guideline 5.3）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0005.umr:2680) · [gold](data/gold/chinese_umr-0005.umr:2653)
- **cs-0001 第 2 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）第 1 句「不可置信之事」与宣布停火共指：`没有这条共指`；较好的写法：`(s1 event :same-event s2 vyhlásit)`。标题说的「不可置信的事成真了」就是副标题里 IRA 宣布停火，gold 的跨句共指成立。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0001.umr:27) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0001.umr:28) · [gold](data/gold/cs-0001.umr:36)

### C2　共指连错

连到了错的先行语（另一个同名实体、引语里的「他」）、把类指或不同批次的东西当同一实体、把未发生的事件和已发生的事件连成 same-event、`:subset-of` 方向反、句内共指写成三元组而不是重入。

条目 128：涉及 s3 的 72 条（错 13），涉及 a2 的 76 条（错 11）；其中 gold 也是同样写法的 6 条。

- **cs-0001 第 21 句**（a2/r1、a2/r2，错）Irsko 的共指：`连到第 20 句的 Severní Irsko`；较好的写法：`连到第 16 句的 Irsko（irský premiér）`。第 16 句 irský premiér 的国家就是 Irsko；第 20 句是 Severní Irsko（北爱尔兰），与 Irsko 不是同一实体，a2 两份连错了。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/cs-0001.umr:1117) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/cs-0001.umr:1114) · [gold](data/gold/cs-0001.umr:1233)
- **cs-0004 第 12 句**（s3/r1、s3/r2，错）inzerenti 与前文：`连第 6 句别家杂志的 inzerenti`；较好的写法：`连第 2 句的 inzerentům`。这里的广告客户是 Time 的广告客户，第 1、2 句的 inzerentům 就是他们，最近的是第 2 句；第 6 句讲的是 Reader's Digest 等别家杂志的广告客户，不同指。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0004.umr:795) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0004.umr:791) · [gold](data/gold/cs-0004.umr:960)
- **zh-0002 第 7 句**（a2/r1、a2/r2，错）伤亡人数与第 2 句的同指：`23 人连对，另把第 2 句 119 伤者与本句 59 伤者连 same-entity`；较好的写法：`23 人 :same-entity 23 人`。第 2 句「23 人死亡」与本句「23 人在爆炸中身亡」是同一批死者，应连 same-entity。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0002.umr:427) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:410) · [gold](data/gold/chinese_umr-0002.umr:414)
- **zh-0003 第 12 句**（a2/r1、a2/r2，错）两项交易 / 两台 的 :subset-of：`(交易 :subset-of 收购)、(两台 :subset-of 公司)（方向反）`；较好的写法：`两个收购 :subset-of 交易（两台的成员也连或不连）`。guideline 5.3：(a :subset-of b) 表示 a 是 b 的一部分。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0003.umr:1068) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0003.umr:1089) · [gold](data/gold/chinese_umr-0003.umr:1092)
- **zh-0006 第 16 句**（a2/r1、a2/r2，错）「本次挑战」的事件共指：`(s14 挑战 :same-event 本次挑战)`；较好的写法：`(s15 下一场挑战 :same-event 本次挑战)`。第 15 句「获得下一场挑战的淘汰豁免权」的下一场挑战就是本句的这一轮；第 14 句的挑战是上一轮，a2 两次连错了。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0006.umr:1300) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0006.umr:1262) · [gold](data/gold/chinese_umr-0006.umr:1326)
- **zh-0007 第 41 句**（a2/r1、a2/r2，错）「岛屿」的共指：`连到第 39 句的夕闇岛（本岛）`；较好的写法：`连到第 35 句的（另一个）夕闇岛`。金田一他们所在的岛屿就是故事里的「另一个夕闇岛」（第 9、35 句），即日暮岛；连到第 35 句的另一个夕闇岛或日暮岛都对。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:2560) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:2554) · [gold](data/gold/chinese_umr-0007.umr:2580)
- **zh-0023 第 14 句**（a2/r1、a2/r2，错）宇航员与第 13 句的共指：`(s13 宇航员 :same-entity s14 宇航员)`；较好的写法：`(s13 宇航员 :subset-of s14 宇航员)`。精简 guideline 5.3：(a :subset-of b) 表示 a 是 b 的一部分。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0023.umr:1141) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0023.umr:1134) · [gold](data/gold/chinese_umr-0023.umr:1000)
- **en-0005 第 28 句**（s3/r2，错）thank 的 ARG0（采访者）的共指：`连到第 19 句的 I（Marsha）`；较好的写法：`连到第 27 句说话人（采访者）`。感谢 Marsha 的是采访者；第 19 句的 I 是 Marsha 本人（the institutions I mentioned），连过去就把采访者和 Marsha 当成了同一人。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0005.umr:1687) · [gold](data/gold/en-0005.umr:1838)
- **en-0007 第 19 句**（a2/r2，错）I（主持人）的共指：`I ≈ Marsha`。这一句还是主持人在说（the institutions I mentioned 指主持人第 12 句的话），I 是主持人，不是 Marsha。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0007.umr:1114) · [gold](data/gold/en-0007.umr:1198)
- **zh-0001 第 8 句**（s3/r1，错）「黑白」的共指：`(第 7 句黑白 :same-entity 黑白)`；较好的写法：`没有这条`。「黑白」在两句里都是修饰语（属性），不是实体，不该用 :same-entity 连接。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:447) · [gold](data/gold/chinese_umr-0001.umr:465)
- **zh-0004 第 47 句**（s3/r2，错）「拍摄」与前文拍摄事件：`第 42 句拍摄 :same-entity 拍摄`。本句是整集的拍摄，第 41–44 句的取景、外景拍摄、实景拍摄只是其中一部分，用 :subset-of 最准确；s3/r2 对事件用了 :same-entity，且第 42 句只是外景拍摄。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0004.umr:3455) · [gold](data/gold/chinese_umr-0004.umr:3482)
- **zh-0018 第 9 句**（s3/r2，错）「面临」与第 6 句的共指：`第 6 句面临 :same-event 本句面临`；较好的写法：`不做共指`。第 6 句说加沙「正面临饥荒」，本句说「不是正面临饥荒的危机」，被否定的面临不是第 6 句那件事；s3/r2 把两者做成同一事件不对。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0018.umr:815) · [gold](data/gold/chinese_umr-0018.umr:799)


## 三、文档级时间

### T　日期和时间词没有锚定或锚错

绝对日期应挂 root `:depends-on`，系统有时写成 `DCT :before 日期`，或者日期根本没有父节点；相对时间词（今后、同时、原先）参照点选错；个别事件先后标反。s3 和 a2 数量相当。

条目 240：涉及 s3 的 122 条（错 15），涉及 a2 的 132 条（错 15）；其中 gold 也是同样写法的 46 条。

- **en-0007 第 14 句**（a2/r1、a2/r2，错）know 与 responded 的先后：`(know :after respond)：回应在 know 之后`；较好的写法：`回应在 know 之前（(know :before respond) 或 (respond :after know)）`。(A :before B) 是 B 在 A 之前、(A :after B) 是 B 在 A 之后（guideline 5.1）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0007.umr:848) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0007.umr:838) · [gold](data/gold/en-0007.umr:888)
- **zh-0018 第 24 句**（s3/r1、s3/r2，错）移送相对前文的时间：`移送 after 第 17 句「身亡」（又和本句身亡 same-event）`；较好的写法：`移送 after 第三次袭击（第 17/23 句）`。本句身亡在移送和抢救之后；s3 把移送挂在第 17 句「身亡」之后，又把两个身亡连成 same-event，等于说移送既在身亡之前又在之后，自相矛盾。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0018.umr:2177) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0018.umr:2257) · [gold](data/gold/chinese_umr-0018.umr:2214)
- **zh-0001 第 6 句**（a2/r2，错）「1979 年」的时间父节点：`1979 没有父节点`；较好的写法：`root :depends-on 1979`。abridged 5.1：绝对日期（1998 之类）依附 root，用 :depends-on；gold 把绝对日期挂到 DCT 下并用 :before，意思没错但不合规定。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0001.umr:281) · [gold](data/gold/chinese_umr-0001.umr:305)
- **zh-0002 第 24 句**（a2/r2，错）两个日期的时间依存和逮捕的参照：`DCT :before 日期；(and 日期) :overlap 逮捕`；较好的写法：`root :depends-on 日期；日期 :contained 逮捕`。同第 15 句：abridged 5.1，日期挂 root（不带年份的日期也可以依存第 1 句的 2017 年 5 月 22 日），事件在日期之内用 :contained；把日期当成事件挂在 DCT 下不对。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:1737) · [gold](data/gold/chinese_umr-0002.umr:1683)
- **zh-0003 第 3 句**（s3/r2，错）启播初期播放的时间定位：`播放 :contained 初期，但 DCT :overlap 启播`。启播与启播初期的播放都在过去；s3/r2 让启播与文档时间重叠，错。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0003.umr:298) · [gold](data/gold/chinese_umr-0003.umr:198)
- **zh-0005 第 5 句**（s3/r2，错）「立法」的时间父节点：`提出 :overlap 立法`。被提议的立法在提议之后（如果发生）；guideline 5.1 目的、补足语事件以其主事件为参照，用 :after。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0005.umr:405) · [gold](data/gold/chinese_umr-0005.umr:369)
- **zh-0007 第 1 句**（s3/r2，错）开发与发布的时间关系：`document-creation-time :overlap 开发`。开发是发布之前完成的过去事件，以发布为参照 :before 或直接挂 DCT :before 都对；s3/r2 把开发和 DCT 标成 overlap，等于说现在还在开发。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0007.umr:2) · [gold](data/gold/chinese_umr-0007.umr:3)
- **zh-0026 第 1 句**（s3/r2，错）职务状态与会面的时间关系：`全部 overlap 会面`；较好的写法：`习的职务 overlap 会面，马的两个前职务在会面之前`。「时任」总书记与会面同时；「前」总统、「前」主席在会面之前（读法：(会面 :before X) 指 X 在会面之前）。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0026.umr:2) · [gold](data/gold/chinese_umr-0026.umr:3)
- **zh-0004 第 48 句**（a2/r2，错）打算与停泊的时间关系：`打算 :overlap 停泊`（gold 也这样写）；较好的写法：`打算 :after 停泊`。停泊是打算的内容，若实现也在打算之后；guideline 5.1 补足语以主事件为父节点，将来的内容用 :after。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0004.umr:3687) · [gold](data/gold/chinese_umr-0004.umr:3516)
- **zh-0008 第 3 句**（a2/r1，错）「今后」的参照时间：`future-reference :depends-on 今后`（gold 也这样写）；较好的写法：`1851 年 :depends-on 今后`。「以便人们今后……」的今后是从 1851 年授权时起算，相对 DCT 是过去；future-reference 表示相对文档时间的将来，错。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0008.umr:271) · [gold](data/gold/chinese_umr-0008.umr:169)
- **zh-0023 第 2 句**（a2/r2，错）「目前为止」与「有」的时间关系：`时间词没有时间父节点，只有 (DCT :overlap 有)`（gold 也这样写）；较好的写法：`时间词挂 DCT 或 present-reference :depends-on，事件挂时间词`。精简 guideline 5.1：每个时间词都要有父节点，相对时间词（今天、目前）挂 (document-creation-time :depends-on 时间词)，再让事件挂这个时间词。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0023.umr:85) · [gold](data/gold/chinese_umr-0023.umr:71)
- **en-0005 第 15 句**（s3/r1、a2/r1、a2/r2，轻）decision 相对说话时间：`decide 与 DCT 重叠`；较好的写法：`s15s :after s15d（决定在说话之后）`。第 14 句说普京还没回应，决定在说话时间之后；把决定标成与 DCT 重叠不对。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0005.umr:911) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0005.umr:936) · [gold](data/gold/en-0005.umr:966)


## 四、概念、义项、命名实体

### Q　量词没有保留为 :unit

按已定规则量词都要保留。四份输出几乎一律只写 `:quant N`，这是数量最多、最一致的一类（都判轻微）。精简版 guideline 里「普通量词省略」那句话直接导致了它。

条目 177：涉及 s3 的 171 条（错 0），涉及 a2 的 131 条（错 0）；其中 gold 也是同样写法的 13 条。

- **zh-0001 第 3 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「一个」的量词：`:quant 1，没有 :unit 个`；较好的写法：`:quant 1 :unit 个`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:139) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0001.umr:142) · [gold](data/gold/chinese_umr-0001.umr:151)
- **zh-0002 第 20 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）量词「个」「名」：`量词不立节点`；较好的写法：`地点、住址 :unit 个，人士 :unit 名`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0002.umr:1366) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0002.umr:1352) · [gold](data/gold/chinese_umr-0002.umr:1302)
- **zh-0003 第 1 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）量词「间」：`电视台 :quant 1（量词省去）`；较好的写法：`电视台 :quant 1 :unit 间`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0003.umr:14) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0003.umr:14) · [gold](data/gold/chinese_umr-0003.umr:3)
- **zh-0004 第 36 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「两个」的量词「个」：`系列 :quant 2`；较好的写法：`系列 :quant 2 :unit 个`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0004.umr:2501) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0004.umr:2633) · [gold](data/gold/chinese_umr-0004.umr:2650)
- **zh-0005 第 31 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）量词「位」「个」作 :unit：`省掉「位」「个」`；较好的写法：`音乐家 :unit 位、版本 :unit 个`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0005.umr:2346) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0005.umr:2434) · [gold](data/gold/chinese_umr-0005.umr:2311)
- **zh-0006 第 4 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「16位」的量词：`设计师 :quant 16（无 位）`；较好的写法：`设计师 :quant 16 :unit 位`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0006.umr:243) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0006.umr:258) · [gold](data/gold/chinese_umr-0006.umr:235)
- **zh-0007 第 9 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）量词「个」：`岛屿 :quant 1 或不标数量`；较好的写法：`岛屿 :quant 1 :unit 个`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0007.umr:521) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0007.umr:563) · [gold](data/gold/chinese_umr-0007.umr:571)
- **zh-0009 第 3 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）量词「个」：`省去「个」`；较好的写法：`传感器/镜头/眼睛 :unit 个`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0009.umr:112) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0009.umr:113) · [gold](data/gold/chinese_umr-0009.umr:109)
- **zh-0012 第 1 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「一位」的数量：`:quant 1`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0012.umr:29) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0012.umr:27) · [gold](data/gold/chinese_umr-0012.umr:3)
- **zh-0014 第 5 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「一份文件」的量词：`文件 :quant 1，不保留 份`；较好的写法：`文件 :quant 1 :unit 份`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0014.umr:383) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0014.umr:384) · [gold](data/gold/chinese_umr-0014.umr:332)
- **zh-0015 第 13 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「多所学校」的量词：`学校 :quant 多`；较好的写法：`学校 :unit 所 :quant 多`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0015.umr:931) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0015.umr:958) · [gold](data/gold/chinese_umr-0015.umr:865)
- **zh-0016 第 3 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「一个」的量词「个」：`重灾区 :quant 1（省掉 个）`；较好的写法：`重灾区 :quant 1 :unit 个`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0016.umr:195) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0016.umr:193) · [gold](data/gold/chinese_umr-0016.umr:199)

### NE　命名实体的类型和名字

类型不在类型表里（stadium、plaza、building）或直接写中文普通名词（站、杂志、商场）；形容词当国名（country "Russian"）；书名号、间隔号、括号、Mr. 写进 `:name`；专名被拆成普通名词加修饰语，或普通名词被当成专名；捷克文照抄变格形式。

条目 337：涉及 s3 的 200 条（错 22），涉及 a2 的 203 条（错 38）；其中 gold 也是同样写法的 23 条。

- **cs-0000 第 41 句**（s3/r1、s3/r2、a2/r1，错）Winston Churchill 的名字形式：`:op1 "Winstonu" :op2 "Churchillovi"（与格形式）`；较好的写法：`:op1 "Winston" :op2 "Churchill"`。名字的 :opN 应写原形（主格），Winstonu Churchillovi 是句中的与格变形，照抄进名字是错的。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0000.umr:2105) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0000.umr:2187) · [gold](data/gold/cs-0000.umr:2034)
- **cs-0001 第 3 句**（s3/r1、a2/r1、a2/r2，错）人名、地名作命名实体：`普通概念 Stuchlíková :mod Jarka、Belfast`；较好的写法：`person / 地名类型 + :name`。guideline 2.2：专名作命名实体（类型 + :name）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0001.umr:65) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/cs-0001.umr:68) · [gold](data/gold/cs-0001.umr:78)
- **zh-0023 第 10 句**（s3/r2、a2/r1、a2/r2，错）「月球」的实体类型：`planet`。月球是卫星，不是行星；句子本身就说「月球本身也是地球的卫星」。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0023.umr:879) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0023.umr:877) · [gold](data/gold/chinese_umr-0023.umr:762)
- **en-0000 第 62 句**（s3/r1、s3/r2，错）「Mps」：`organization :name "Mps"`；较好的写法：`person :ARG1-of have-org-role-92 :ARG2 parliament :ARG3 member`。MPs 是 members of parliament（议员，复数的人），按 guideline 2.3 的角色名词写法用 person + have-org-role-92；把缩写当成组织或政党的名字是错的。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0000.umr:3314) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0000.umr:3415) · [gold](data/gold/en-0000.umr:3014)
- **zh-0001 第 36 句**（s3/r1、s3/r2，错）「克芬德·路丁博士」的名字：`:op1 "克芬德" :op2 "·" :op3 "路丁"`；较好的写法：`:op1 "克芬德" :op2 "路丁"`。间隔号是标点；「博士」是头衔，不是名字的一部分，应另作 have-role-91 的 ARG3（系统都这样做）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:2410) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0001.umr:2343) · [gold](data/gold/chinese_umr-0001.umr:2599)
- **zh-0003 第 7 句**（a2/r1、a2/r2，错）「温哥华市甘比街」的命名实体：`road "市甘比街"`；较好的写法：`road 甘比街 + city 温哥华`。分词把「市」错并到了「甘比街」上，街名应是甘比街；「市」可以算进城市名，也可以当类型词去掉。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0003.umr:551) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0003.umr:559) · [gold](data/gold/chinese_umr-0003.umr:541)
- **zh-0004 第 48 句**（a2/r1、a2/r2，错）「自由神像」的实体类型：`building`；较好的写法：`work-of-art`。自由神像是雕像，类型表 cultural-artifact 下的 work-of-art 合适（gold 前文第 30、41、46 句也一直用它）；monument 不在类型表；雕像不是 building。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0004.umr:3651) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0004.umr:3644) · [gold](data/gold/chinese_umr-0004.umr:3516)
- **zh-0033 第 8 句**（a2/r1、a2/r2，错）《纽约时报》的名字：`name :op1 "《" :op2 "纽约时报" :op3 "》"`；较好的写法：`name :op1 "纽约时报"`。书名号是标点，不是名字的一部分。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0033.umr:571) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0033.umr:565) · [gold](data/gold/chinese_umr-0033.umr:526)
- **cs-0004 第 3 句**（a2/r1，错）「v roce 1990」的表示：`rok :name (1990)`；较好的写法：`date-entity :year 1990`。精简 guideline 2.2：日期写 date-entity :year。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/cs-0004.umr:268) · [gold](data/gold/cs-0004.umr:302)
- **zh-0002 第 18 句**（a2/r2，错）「法尔洛菲德」的实体类型：`city`；较好的写法：`city-district`。法尔洛菲德（Fallowfield）是曼彻斯特的一个区，AMR 类型表里对应 city-district；district 不在表里，city 错。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:1192) · [gold](data/gold/chinese_umr-0002.umr:1171)
- **zh-0005 第 12 句**（a2/r1，错）「临县」：`命名实体 city 临县`。这里「临县」是「邻近的县」，不是山西的临县；作普通名词，拆不拆都可以，作城市专名是错的。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0005.umr:896) · [gold](data/gold/chinese_umr-0005.umr:878)
- **zh-0007 第 41 句**（a2/r1，错）「金田一结局」中金田一的实体类型：`publication`；较好的写法：`person / individual-person`。「金田一结局」是以金田一为主角的结局，这里的金田一仍是人物，不是出版物；a2/r1 把它标成 publication，还另立了一个与主语无关的实体。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:2531) · [gold](data/gold/chinese_umr-0007.umr:2580)

### S　义项选错或把词拆开

PropBank 里有现成词条却选了别的义项（进行-04、spy-02、execute-01），把复合词拆成单字谓词（设在→设-01、写道→写-01、杀掉→杀-01），或照字面理解错别字（掉往）。s3 多是拆词和近义词条，a2 多是义项号。

条目 157：涉及 s3 的 104 条（错 5），涉及 a2 的 68 条（错 13）；其中 gold 也是同样写法的 15 条。

- **en-0007 第 2 句**（a2/r1、a2/r2，错）spying 的义项：`spy-02`；较好的写法：`spy-01`。PropBank 只有 spy-01（ARG0 secret agent）；spy-02 不存在，是照抄完整 guideline 例子的写法。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0007.umr:106) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0007.umr:103) · [gold](data/gold/en-0007.umr:74)
- **zh-0005 第 37 句**（a2/r1、a2/r2，错）「呼吁」的义项和内容论元：`呼吁-01 :ARG1 让`。PropBank 呼吁-01：ARG1 是被呼吁的一方（party appealed to），ARG2 是呼吁做的事；呼吁-02：ARG1 是呼吁的内容。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0005.umr:2917) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0005.umr:2924) · [gold](data/gold/chinese_umr-0005.umr:2820)
- **zh-0007 第 60 句**（a2/r1、a2/r2，错）「即」：`即-02 :ARG0 调查 :ARG1 利用`；较好的写法：`identity-91 :ARG1 俯视图调查 :ARG2 调查-01`。「X 即 Y」是下定义（X 就是 Y），identity-91 合适；PropBank 只有 即-01（reach），即-02 是编造的义项。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:3668) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:3637) · [gold](data/gold/chinese_umr-0007.umr:3773)
- **zh-0016 第 8 句**（a2/r1、a2/r2，错）「停驶」的概念与论元：`停驶-01 :ARG1 列车`；较好的写法：`停驶-00 :ARG1 列车`。PropBank 没有「停驶」，按 guideline 写 停驶-00（a2 两次和 s1f 两次写成不存在的 -01）；被停驶的列车用 :ARG1，:theme 不是 Stage 1 角色。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0016.umr:692) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0016.umr:680) · [gold](data/gold/chinese_umr-0016.umr:629)
- **zh-0029 第 7 句**（s3/r1、a2/r1，错）「搞不明白」的概念与否定：`搞-02 :polarity -`。PropBank 搞-02 的 ARG1 是 thing arg0 cannot figure out（例句「搞 不 清楚」，「不」算在谓词里），再加 :polarity - 就成了双重否定；搞-04 是 figures out，配 :polarity - 才对。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0029.umr:507) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0029.umr:509) · [gold](data/gold/chinese_umr-0029.umr:482)
- **en-0000 第 99 句**（s3/r1，错）execute his plan 的义项：`execute-01`；较好的写法：`execute-02`。PropBank execute-01 是 kill（处决，ARG1 corpse），execute-02 是 enact（实施，ARG1 thing done）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0000.umr:5446) · [gold](data/gold/en-0000.umr:4954)
- **en-0005 第 2 句**（a2/r2，错）spying 的义项：`spy-02`；较好的写法：`spy-01`。PropBank 只有 spy-01（clandestine observation）。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0005.umr:104) · [gold](data/gold/en-0005.umr:68)
- **zh-0006 第 13 句**（s3/r2，错）「穿着」的义项：`穿着-01`。PropBank 没有 穿着，只有 穿-01（ARG0 agent，ARG1 clothing）；「穿着」的「着」是体标记，用 穿-01 合理，按词写 穿着-00 也符合 guideline 2.1。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0006.umr:1028) · [gold](data/gold/chinese_umr-0006.umr:1040)
- **zh-0012 第 6 句**（a2/r2，错）「落下」的义项：`落下-02`；较好的写法：`落下-03`。PropBank 落下-03 是「落下、遗漏」（ARG1 things left by arg0），「工作一点没落下」正是这个意思；落下-01 是「落下（帷幕）」，落下-02 没有论元。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0012.umr:750) · [gold](data/gold/chinese_umr-0012.umr:614)
- **zh-0014 第 2 句**（a2/r1，错）「进行」的义项：`进行-04 :ARG0 仪式`；较好的写法：`进行-01 :ARG1 仪式`。PropBank 进行-01 ARG1 是 thing carried out，仪式被举行；进行-04 是「向前移动」（ARG0 entity that moves forward），义不合。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0014.umr:115) · [gold](data/gold/chinese_umr-0014.umr:88)
- **en-0008 第 2 句**（s3/r2、a2/r2，错）spying 的义项：`spy-02`（gold 也这样写）；较好的写法：`spy-01`。look.py pb --lang en spy 只有 spy-01（ARG0 secret agent，ARG1 entity spied）；spy-02 不存在，训练数据里 spy-02 只出现在这篇文档自己的旧版里。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0008.umr:66) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0008.umr:65) · [gold](data/gold/en-0008.umr:35)
- **zh-0026 第 27 句**（a2/r1、a2/r2，错）「进行」的义项和论元：`进行-04 :ARG0 开场词`（gold 也这样写）；较好的写法：`进行-01 :ARG1 开场词`。PropBank 进行-04 是「向前移动的实体」，不合此处；「开场词……在媒体拍摄下进行」是事件在进行，PropBank 进行-01 的例句「比赛 进行 五 轮」以事件为 ARG1，gold 第 28 句「座谈闭门进行」也用 进行-01 :ARG1。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0026.umr:2258) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0026.umr:2185) · [gold](data/gold/chinese_umr-0026.umr:1834)

### F　给虚词立节点、过度谓词化、自造 -00

「则、已、曾、就、不得不」写成 `:mod` 节点，「受到、进行、开始」这类轻动词和起始动词单独立事件，PropBank 有词条时另造 `-00`，凭空加 `implicit-predicate`。a2 比 s3 多一些，「错」的也更多。

条目 147：涉及 s3 的 72 条（错 3），涉及 a2 的 93 条（错 6）；其中 gold 也是同样写法的 18 条。

- **zh-0005 第 25 句**（a2/r1、a2/r2，错）「此外」的处理：`and :op1 implicit-predicate，并与第 24 句 :same-event`；较好的写法：`不立节点`。「此外」是篇章连接词，表示追加，不需要立节点；a2 两次立了一个空的 implicit-predicate 作并列项，还把它和上一句的 and 连成同一事件，没有依据。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0005.umr:1864) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0005.umr:1875) · [gold](data/gold/chinese_umr-0005.umr:1830)
- **zh-0007 第 59 句**（a2/r1、a2/r2，错）「除此以外……还」：`and :op1 implicit-predicate :op2 包含`；较好的写法：`不表示（靠「还」:mod）`。「除此以外，……还包含」是递加：在前面说的之外另外还有，不是从中减去；subtract-91 把意思弄反了。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:3598) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:3568) · [gold](data/gold/chinese_umr-0007.umr:3704)
- **zh-0021 第 6 句**（a2/r1、a2/r2，错）「相隔」的义项：`相隔-00`；较好的写法：`相隔-01`。PropBank 有 相隔-01（ARG0 entities described，ARG1 entity arg0 is separated by），不该写 -00。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0021.umr:516) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0021.umr:520) · [gold](data/gold/chinese_umr-0021.umr:463)
- **zh-0011 第 20 句**（a2/r1，错）句首「如」（举例）的表示：`have-example-91 :ARG1 (implicit-predicate) :ARG2 撰写`。「如……」举的是上一句「地方官员亦会亲撰碑文」的一个实例。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0011.umr:1309) · [gold](data/gold/chinese_umr-0011.umr:1245)
- **zh-0026 第 28 句**（a2/r2，错）「座谈闭门进行」：轻动词与事件名词：`进行-04 :ARG0 座谈-01`；较好的写法：`不要 进行，座谈-01 作事件`。guideline 2.1：轻动词不作节点（进行访问 → 访问-01），事件名词作事件；「座谈闭门进行」即「闭门进行座谈」，应以 座谈-01 为事件，闭门、之后挂在它下面。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0026.umr:2251) · [gold](data/gold/chinese_umr-0026.umr:1878)
- **zh-0023 第 17 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「开始迈向」的 开始：`开始-01 :ARG1 迈向`。完整 guideline 3-3-1-4 (3a)：He started playing the violin → 只标 play-01、aspect Activity，「开始」不成节点，起始义由 aspect 表达；inceptive 是更细的取值。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0023.umr:1316) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0023.umr:1305) · [gold](data/gold/chinese_umr-0023.umr:1180)
- **zh-0036 第 1 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「就」是否立节点：`立 就 节点（:mod / :temporal）`；较好的写法：`不立 就`。「一…就」是关联格式，先后已经由 consecutive / after / :temporal 表达，就 再立 :mod 节点是重复。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0036.umr:28) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0036.umr:32) · [gold](data/gold/chinese_umr-0036.umr:3)
- **zh-0004 第 9 句**（s3/r1、a2/r1、a2/r2，轻）「已」：`改造 :mod 已`；较好的写法：`不标`。「已」是体标记（已然），体现在 aspect 和时间关系上，guideline 2.1 不为助词、情态词立节点。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0004.umr:556) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0004.umr:587) · [gold](data/gold/chinese_umr-0004.umr:574)
- **zh-0027 第 14 句**（s3/r2、a2/r1、a2/r2，轻）「不得不」是否立节点：`获得 :mod 不得不`；较好的写法：`不立节点`。精简 guideline 2.1：能愿成分（会、能、必须）不是节点，体现在 modal 强度上。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0027.umr:1368) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0027.umr:1333) · [gold](data/gold/chinese_umr-0027.umr:1220)
- **en-0000 第 83 句**（s3/r1、s3/r2，轻）began 是否作节点：`begin-01 :ARG1 appear-01`；较好的写法：`不设 begin 节点，appear 作根`。完整 guideline 3-3-1-4 例 (3a)：He started playing the violin 只标 play-01（aspect Activity），起始类动词不作节点，起始义由 aspect 表达。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0000.umr:4446) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0000.umr:4569) · [gold](data/gold/en-0000.umr:4077)
- **zh-0001 第 10 句**（s3/r2、a2/r1，轻）「跌至」的义项：`跌至-00`；较好的写法：`跌-01`。PropBank 没有「跌至」，但有 跌-01（ARG3 end point），「至」正是引出终点的介词，用 跌-01 + ARG3 能完整表达；另造 跌至-00 丢掉了现成的论元框架。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0001.umr:489) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0001.umr:511) · [gold](data/gold/chinese_umr-0001.umr:549)
- **zh-0002 第 6 句**（a2/r1、a2/r2，轻）1996 年「爆炸案」的概念：`爆炸案-00`；较好的写法：`名词 爆炸案`。「爆炸案」是名词（案件），作 策动-01 的 ARG1（entity planned and motivated）；-00 是给 PropBank 外的谓词用的，名词不加。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0002.umr:361) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:346) · [gold](data/gold/chinese_umr-0002.umr:302)

### N　数值、序数、钟点、金额的写法

序数写成 `ordinal-entity :value N` 而丢掉量词或「最后」，钟点写成 `:time 19 :30`（图格式已坏），金额不换算（`:quant 250 :unit 万美元`），「超过／至少 N」把数字当概念节点，频率和年代的写法不规范。

条目 156：涉及 s3 的 97 条（错 7），涉及 a2 的 94 条（错 17）；其中 gold 也是同样写法的 11 条。

- **zh-0031 第 3 句**（s3/r1、a2/r1、a2/r2，错）「超过 1.3 万」「超过 20 万」的写法：`:quant (N :mod 超过)，数字当概念节点`。AMR 惯例 :quant (more-than :op1 N)，中文 gold 用「超过」作概念同样可以。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0031.umr:199) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0031.umr:192) · [gold](data/gold/chinese_umr-0031.umr:165)
- **zh-0008 第 7 句**（a2/r1、a2/r2，错）「超过 10 万」的表示：`金币 :quant (100000 :mod 超过)（数字作概念）`；较好的写法：`金币 :quant (more-than :op1 100000)`。数量的「超过」按 AMR 惯例写 more-than :op1 N；建成 超过-01 事件可以理解，但多出一个状态事件和文档级关系，略差。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0008.umr:513) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0008.umr:513) · [gold](data/gold/chinese_umr-0008.umr:477)
- **zh-0011 第 12 句**（a2/r1、a2/r2，错）「最后一座」的「最后」：`ordinal-entity :value 1 :mod 最后`；较好的写法：`牌坊 :ord (ordinal-entity :value -1)`。guideline 2.2 序数用 ordinal-entity；AMR 惯例「最后一个」是 :ord (ordinal-entity :value -1)。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0011.umr:754) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0011.umr:752) · [gold](data/gold/chinese_umr-0011.umr:687)
- **zh-0013 第 4 句**（a2/r1、a2/r2，错）时刻 11:45 的写法：`:time 11 :45（格式错）`；较好的写法：`:time "11:45"`。时刻是字符串常量，要加引号；不加引号时 PENMAN 解析成 :time 11 和非法角色 :45。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0013.umr:320) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0013.umr:308) · [gold](data/gold/chinese_umr-0013.umr:238)
- **zh-0016 第 13 句**（s3/r1、a2/r1，错）「五百年一遇」的频率写法：`遇 :frequency 1 :temporal 500年`。同第 12 句：rate-entity-91 用 ARG3 或 ARG2 表示间隔都能读通；:frequency 1 加 :temporal 500年 把「每五百年一次」变成「在五百年这段时间里发生」，意思错了。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0016.umr:1143) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0016.umr:1159) · [gold](data/gold/chinese_umr-0016.umr:1075)
- **cs-0000 第 14 句**（a2/r1，错）「24. října loňského roku」的表示：`říjen :mod 24 :possessor rok（没有 date-entity）`。:year 要填年份数字，「去年」是相对时间，不该塞进 :year；gold 把 loni 另挂一个 :temporal、s3/r2 把它挂在 date-entity 下都说得通。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/cs-0000.umr:692) · [gold](data/gold/cs-0000.umr:624)
- **zh-0002 第 59 句**（a2/r2，错）「250 万美元」：`monetary-quantity :quant 250 :unit 万美元`；较好的写法：`monetary-quantity :quant 2500000 :unit 美元`。abridged 2.2：金额写 (monetary-quantity :quant 500 :unit (dollar))，:value 是 ordinal-entity 的属性。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:4901) · [gold](data/gold/chinese_umr-0002.umr:4888)
- **zh-0003 第 28 句**（s3/r1，错）钟点时间（7:30、11:30 等）的写法：`:time 19 :30（冒号被拆成角色，格式坏了）`；较好的写法：`:time "19:30" 等字符串`。AMR / UMR 的 date-entity 用 :time "19:30" 这样的字符串常量；gold 和 a2 自造了 h19m30 这种概念节点，s1f/r1、s3/r1 写成 :time 19 :30，30 成了角色名，图已不合格式。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0003.umr:2463) · [gold](data/gold/chinese_umr-0003.umr:2460)
- **zh-0023 第 16 句**（a2/r2，错）「第一批」的序数：`批 :ord (第一)`；较好的写法：`ordinal-entity :value 1，批 作 :unit`。【更正】量词按规则保留为 :unit。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0023.umr:1276) · [gold](data/gold/chinese_umr-0023.umr:1143)
- **zh-0026 第 1 句**（a2/r2，错）「最后」的写法：`ordinal-entity :value 1 :mod 最后 :range 访问`。「最后」作 :mod 是中文训练数据的写法（chinese_umr-0006 第 33 句 时装周 :mod 最后）；:ord -1 是 AMR 的惯例，也可接受。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0026.umr:70) · [gold](data/gold/chinese_umr-0026.umr:3)
- **zh-0001 第 9 句**（a2/r1、a2/r2，错）「1980 年代」的写法：`date-entity :era 1980`（gold 也这样写）；较好的写法：`date-entity :decade 1980`。abridged 2.2 和完整 guideline 3-2-2-1 都有 :decade；「1980 年代」是一个十年，:era 是纪元（公元、民国之类）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0001.umr:483) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0001.umr:477) · [gold](data/gold/chinese_umr-0001.umr:503)
- **zh-0022 第 8 句**（a2/r1、a2/r2，错）「上千年」的数量：`temporal-quantity :quant (上千) 概念节点`（gold 也这样写）；较好的写法：`:quant (more-than :op1 1000)`。guideline 2.2：数量写成数字；「上千」是「一千以上」，AMR/UMR 惯例用 more-than :op1 1000。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0022.umr:712) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0022.umr:706) · [gold](data/gold/chinese_umr-0022.umr:652)


## 五、角色与结构

### R　角色标签和论元分配

有核心论元槽位却用 `:place`、`:source`、`:medium`、`:mod`；没有槽位时硬塞 `:ARG1`／`:ARG2`；`have-91` 套 ARG0/ARG1；`:part`、`:possessor-of` 方向写反。a2 的「错」比 s3 多一倍。

条目 449：涉及 s3 的 241 条（错 16），涉及 a2 的 269 条（错 37）；其中 gold 也是同样写法的 53 条。

- **cs-0004 第 3 句**（a2/r1、a2/r2，错）「V souvislosti s tím」：`prohlašovat :companion ten（丢了 souvislost）`。「与此相关」表示话题关联，:topic、:regard 或谓词化的 souviset 都说得通，指代对象（第 2 句的宣布或其内容）各家连得不同，都可以。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/cs-0004.umr:250) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/cs-0004.umr:248) · [gold](data/gold/cs-0004.umr:302)
- **en-0000 第 8 句**（s3/r1、s3/r2，错）where 从句与 app 的关系：`app :place receive-01（方向反）`；较好的写法：`app :place-of receive-01`。where 引出的关系从句：观众是在这个 app 上获得的，即 receive-01 :place app，挂在 app 下写反向 :place-of。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0000.umr:408) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0000.umr:412) · [gold](data/gold/en-0000.umr:341)
- **zh-0002 第 27 句**（a2/r1、a2/r2，错）「袭击者周围」：`周围 :possessor-of 袭击者`；较好的写法：`周围 :op1 袭击者`。方位词按训练数据的写法作 (周围 :op1 X)。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0002.umr:1957) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:1921) · [gold](data/gold/chinese_umr-0002.umr:1918)
- **zh-0003 第 4 句**（a2/r1、a2/r2，错）「不同」的论元：`不同-01 :ARG0 一方 :ARG1 另一方`；较好的写法：`不同-01 :ARG0 (and 新时代主频道 城市电视两频道)`。PropBank 不同-01 只有 ARG0（things which are different），「与 X」是 ARG0-CRD，比较双方都是 ARG0；ARG1 不在这个 roleset 里。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0003.umr:304) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0003.umr:312) · [gold](data/gold/chinese_umr-0003.umr:326)
- **zh-0004 第 40 句**（a2/r1、a2/r2，错）「改造戴立克人」中戴立克人的角色：`改造 :ARG1 戴立克人`；较好的写法：`改造 :ARG2 戴立克人`。PropBank 改造-01：ARG1 thing transformed，ARG2 transformed into。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0004.umr:3103) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0004.umr:3102) · [gold](data/gold/chinese_umr-0004.umr:2979)
- **zh-0006 第 9 句**（a2/r1、a2/r2，错）have-91 的论元：`have-91 :ARG0 设计师 :ARG1 预算和时间`；较好的写法：`have-91 :ARG1 设计师 :ARG2 预算和时间`。guideline 2.3：have-91 的 :ARG1 是领有者，:ARG2 是所有物。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0006.umr:623) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0006.umr:587) · [gold](data/gold/chinese_umr-0006.umr:606)
- **zh-0017 第 12 句**（a2/r1、a2/r2，错）「该邦的大部分地区」与钦邦的关系：`地区 :part 钦邦/邦（方向反）`。地区是邦的一部分：「钦邦 :part 地区」或领属 :possessor 都可以；s1f、a2 写成「地区 :part 钦邦」，意思成了地区包含钦邦。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0017.umr:801) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0017.umr:809) · [gold](data/gold/chinese_umr-0017.umr:780)
- **zh-0018 第 11 句**（a2/r1、a2/r2，错）「世界各地」：`各地 :part 世界（方向反了）`；较好的写法：`各地 :part-of 世界`。各地是世界的一部分，:part-of；a2 两次写成 :part，变成世界是各地的一部分。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0018.umr:975) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0018.umr:979) · [gold](data/gold/chinese_umr-0018.umr:924)
- **zh-0021 第 6 句**（a2/r1、a2/r2，错）「相隔」的论元编号：`:ARG1 美洲大日食 :ARG2 一年（另一方作 ARG0 或不标）`；较好的写法：`:ARG0 and(这次日食, 美洲大日食) :ARG1 一年`。PropBank 相隔-01：相隔的双方并列作 ARG0，相隔的距离/时间是 ARG1（例：中国和以色列 ARG0 相隔 万水千山 ARG1；…相隔 一段时间 ARG1）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0021.umr:526) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0021.umr:530) · [gold](data/gold/chinese_umr-0021.umr:463)
- **zh-0027 第 14 句**（s3/r1、s3/r2，错）「从非法渠道获得」的来源：`获得 :source 渠道`；较好的写法：`获得 :ARG2 渠道`。PropBank 获得-01：ARG2 received from。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0027.umr:1391) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0027.umr:1358) · [gold](data/gold/chinese_umr-0027.umr:1220)
- **zh-0028 第 3 句**（a2/r1、a2/r2，错）「方便」的论元编号：`方便-01 :ARG0 用户 :ARG1 连接`；较好的写法：`方便-01 :ARG1 用户 :ARG2 连接`。PropBank 方便-01：ARG0 agent，ARG1 theme，ARG2 predicate；例句「为方便公众购物」里施事是 *PRO*（零售商），公众是 ARG1。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0028.umr:85) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0028.umr:86) · [gold](data/gold/chinese_umr-0028.umr:100)
- **cs-0000 第 27 句**（s3/r2，错）两个世界与战争的关系：`válka :between svět（不存在的角色）`。mezi těmito dvěma světy 是交战双方。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0000.umr:1402) · [gold](data/gold/cs-0000.umr:1290)

### D3　类别归属、职务、亲属名词的抽象谓词

用了不存在的 `have-org-role-91`／`have-rel-role-91`，论元号放错（`:ARG3-of`），把 have-org-role-92 用在没有组织的身份上，同位语和「是一个……」在 identity-91 与 have-role-91 之间摇摆，或者干脆写成 `:mod`／`:possessor`。

条目 185：涉及 s3 的 113 条（错 10），涉及 a2 的 105 条（错 13）；其中 gold 也是同样写法的 30 条。

- **zh-0001 第 31 句**（a2/r2，错）「博物馆看守人」的表示：`看守人 :ARG3-of (have-org-role-92 :ARG2 博物馆)`。职务名词可以照 2.3 写成 have-org-role-92（:ARG1 人 :ARG2 机构 :ARG3 职务），也可以像 gold 那样分解成 看守-01（ARG0 agent，ARG1 entity guarded）或直接作名词。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0001.umr:2044) · [gold](data/gold/chinese_umr-0001.umr:2183)
- **zh-0002 第 24 句**（a2/r2，错）「袭击者的父亲 / 他的弟弟」的亲属结构：`person :ARG1-of have-rel-role-91 :ARG2 袭击者 :ARG3 父亲/弟弟`；较好的写法：`person :ARG1-of have-rel-role-92 :ARG2 袭击者 :ARG3 父亲/弟弟`。abridged 2.3：亲属角色用 have-rel-role-92，没有 -91。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0002.umr:1693) · [gold](data/gold/chinese_umr-0002.umr:1683)
- **zh-0005 第 1 句**（s3/r1，错）三个同位语身份用什么谓词：`have-rel-role-92（人）+ have-role-91`；较好的写法：`have-role-91 ×3`。「山东日照人」「军旅指挥家」「国家一级指挥」都是类别归属，guideline 3-1-3-6 表 8：object predication 用 have-role-91（ARG1 theme、ARG3 category），identity-91 只用于等同（she is the winner）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0005.umr:8) · [gold](data/gold/chinese_umr-0005.umr:3)
- **zh-0007 第 13 句**（a2/r2，错）「矿工领袖」的身份：`have-org-role-91（不存在的谓词）`；较好的写法：`have-org-role-92 :ARG2 矿工 :ARG3 领袖`。「矿工领袖」是一群人中的职位，guideline 2.3 用 have-org-role-92（ARG2 组织/群体，ARG3 职位）；identity-91 同位可以接受，但丢了领袖与矿工的组织关系。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:856) · [gold](data/gold/chinese_umr-0007.umr:847)
- **zh-0029 第 2 句**（s3/r2，错）「自己老公」的表示与在发放中的角色：`同样的 have-rel-role-92，但作 发放 :ARG0`；较好的写法：`person :ARG1-of have-rel-role-92（ARG2 网友，ARG3 老公），作 发放 :ARG2`。guideline 2.3：亲属称谓要具体化为 person :ARG1-of have-rel-role-92（his wife 的例子）。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0029.umr:83) · [gold](data/gold/chinese_umr-0029.umr:67)
- **zh-0035 第 15 句**（s3/r1，错）「以就职典礼为目标」：`have-rel-role-92 :ARG1 典礼 :ARG2 组织 :ARG3 目标`；较好的写法：`have-role-91 :ARG1 典礼 :ARG2 组织 :ARG3 目标`。「以 A 为目标」是 A 充当（组织的）目标：guideline 表 8 have-role-91，ARG1 theme、ARG2 reference point、ARG3 category。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0035.umr:1047) · [gold](data/gold/chinese_umr-0035.umr:915)
- **zh-0026 第 23 句**（a2/r1、a2/r2，错）职务关系的抽象谓词：`have-org-role-91`（gold 也这样写）；较好的写法：`have-org-role-92`。项目规则：have-org-role-92 是对的，-91 应改成 -92。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0026.umr:1929) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0026.umr:1878) · [gold](data/gold/chinese_umr-0026.umr:1592)
- **zh-0017 第 2 句**（s3/r1、a2/r1、a2/r2，轻）「将军」的角色名词结构：`将军 :ARG3-of have-org-role-92`；较好的写法：`person :ARG1-of (have-org-role-92 :ARG3 将军)`。精简 guideline 2.3：角色名词具体化为 person :ARG1-of (have-org-role-92 :ARG2 组织 :ARG3 头衔)；把「将军」本身作 ARG3-of 的头，实体就成了头衔，不合规范。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0017.umr:146) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0017.umr:136) · [gold](data/gold/chinese_umr-0017.umr:121)
- **en-0000 第 28 句**（s3/r1、s3/r2，轻）had been the site of 的结构：`have-role-91 :ARG3 (site :mod / :poss / :possessor orogeny)`。「西缘曾是多次造山运动发生的地方」：gold 的 have-place-91（造山运动发生在西缘）和 a2 的 site :place-of orogeny 都把地点关系表达出来了。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0000.umr:1502) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0000.umr:1530) · [gold](data/gold/en-0000.umr:1326)
- **en-0005 第 24 句**（s3/r1、s3/r2，轻）be a source of …（两处）：`have-role-91 :ARG1 Russia :ARG3 source`。PropBank source-02 是 provide, be a source of（ARG0 提供者，ARG1 所提供的），a2/r1 用得对；gold 把“成为麻烦 / 恐惧之源”直接改写为造成麻烦、令人恐惧，意思相同。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0005.umr:1383) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0005.umr:1392) · [gold](data/gold/en-0005.umr:1526)
- **zh-0003 第 2 句**（a2/r1、a2/r2，轻）「该台的最大股东」的角色结构：`identity-91 股东 :possessor 台`；较好的写法：`have-org-role-92 :ARG1 新时代传媒 :ARG2 台 :ARG3 股东`。guideline 2.3 / Table 8：have-org-role-92 是 ARG1 担任者、ARG2 机构、ARG3 职衔；gold 用的是 AMR 的 have-org-role-91 编号（ARG1 机构、ARG2 职衔），训练数据里也常见，但不合 UMR 0.9。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0003.umr:88) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0003.umr:88) · [gold](data/gold/chinese_umr-0003.umr:88)
- **zh-0006 第 8 句**（s3/r1、s3/r2，轻）「以纽约为灵感」：`have-role-91 :ARG1 纽约 :ARG3 灵感`。PropBank 为-02 的两个例句对「以 X 为 Y」给了两种标法（以-短语作 ARG0，或作 ARG2、主语作 ARG0），gold 和 a2 各合一种。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0006.umr:547) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0006.umr:562) · [gold](data/gold/chinese_umr-0006.umr:542)

### D2　小句之间的关系读错

「除了……外，还……」写成 `:concession` 或 `subtract-91`（应是并列／追加）；条件挂到主句的上一层谓词上；句首「但、然而、因为」丢掉，根变成 and；「否则」写成不存在的 `orx`。

条目 161：涉及 s3 的 98 条（错 9），涉及 a2 的 81 条（错 12）；其中 gold 也是同样写法的 6 条。

- **zh-0004 第 2 句**（s3/r1、s3/r2，错）「除了……外，……也」的结构：`have-91 :concession and(饰演, 扮演)`。「除了 X 外，Y 也……」是递加关系，管的是整个小句；训练数据 chinese_umr-0003 第 20 句「除了……外，……亦有」用 subtract-91，并列 and 也说得通。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0004.umr:92) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0004.umr:90) · [gold](data/gold/chinese_umr-0004.umr:81)
- **zh-0009 第 10 句**（a2/r1、a2/r2，错）「除开…外，苹果还…」的篇章关系：`subtract-91 :ARG1 推出 :ARG2 更新`；较好的写法：`and :op 更新 :op 推出`。「除开 X 外，还 Y」是追加（X 之外又有 Y），X 也发生了，and 合适。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0009.umr:749) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0009.umr:760) · [gold](data/gold/chinese_umr-0009.umr:767)
- **zh-0010 第 8 句**（s3/r2、a2/r2，错）「要求……否则拒绝」两部分的组合：`orx :op1 要求 :op2 拒绝`；较好的写法：`and :op1 要求 :op2 拒绝`。要求付钱和以拒绝婚事相威胁是同一情况的两部分，是并列 and；「否则」不是二选一的 or。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0010.umr:537) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0010.umr:536) · [gold](data/gold/chinese_umr-0010.umr:542)
- **zh-0003 第 27 句**（s3/r2，错）「除了…外，…亦…」的关系：`自制 :concession 购入`；较好的写法：`and 并列 购入、自制`。「除了从海外购入节目外，城市电视亦有自制节目」带「亦」，是加合（besides），不是排除（except）；guideline 3-1-6 的 subtraction 是「除…之外都…」那种排除。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0003.umr:2408) · [gold](data/gold/chinese_umr-0003.umr:2388)
- **zh-0007 第 58 句**（a2/r2，错）整句主干与「除了……外，还……」：`subtract-91 连接两个「让」`；较好的写法：`and :op1 使用 :op2 让(检查) :op3 让(结合)`。「此游戏使用关键词系统」是独立的主句断言，gold 把它降成系统的定语，略差。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:3485) · [gold](data/gold/chinese_umr-0007.umr:3625)
- **zh-0033 第 5 句**（s3/r2，错）「广播……的同时」的挂接：`广播 作根 and 的并列项，:temporal 同时 不带 op`。「国内广播纳斯鲁拉演讲的同时，以色列……」是时间从句，广播应作主句事件的 :temporal（直接挂或经「同时」挂都可以）。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0033.umr:344) · [gold](data/gold/chinese_umr-0033.umr:285)
- **en-0000 第 52 句**（s3/r2，错）If 条件挂在哪：`assure :condition elect`（gold 也这样写）；较好的写法：`investigate :condition elect`。「如果对手当选，她将被调查多年」：条件限定的是被担保的内容（调查），不是「他担保」这个已经发生的行为。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0000.umr:2924) · [gold](data/gold/en-0000.umr:2566)
- **zh-0023 第 7 句**（s3/r2、a2/r1、a2/r2，轻）「除…外」的表示：`and :subtraction 三国`。「除俄美中三国外，还有…也在计划」是加合（除此之外还有），不是排除。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0023.umr:667) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0023.umr:666) · [gold](data/gold/chinese_umr-0023.umr:563)
- **en-0005 第 8 句**（s3/r1、s3/r2，轻）whereas 的表示：`suspicious :concession (law 的规定)`；较好的写法：`contrast-91 :ARG1 sentence-01 :ARG2 (law 的规定)`。whereas 对比的是「判了最高刑」和「法律条文规定 10 到 20 年」，二者构成令人起疑的内容。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0005.umr:434) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0005.umr:444) · [gold](data/gold/en-0005.umr:373)
- **zh-0001 第 47 句**（s3/r1、s3/r2，轻）「然而」的表示：`不表示（and、消失或引起作根）`；较好的写法：`单论元 but-91 :ARG2 消失`。「然而」把本句和上一句（飞机机体完好）对立起来，可以用只有一个论元的 but-91 表示；「然而」引出的是转折后项，与第 46 句一致应作 ARG2。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:3409) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0001.umr:3343) · [gold](data/gold/chinese_umr-0001.umr:3702)
- **zh-0011 第 10 句**（s3/r1、s3/r2，轻）句首「但」的表示：`不标「但」`。精简 guideline 2.5：但 → but-91 或 contrast-91；转折的前项在上一句，可以只写 ARG2。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0011.umr:586) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0011.umr:619) · [gold](data/gold/chinese_umr-0011.umr:568)
- **zh-0021 第 11 句**（a2/r1、a2/r2，轻）「除了…之外」的结构：`subtract-91 :ARG1 看到 :ARG2 看见`。「除了全食带内能看见日全食之外，半影范围内都能看到日偏食」是追加（besides），不是排除；用 and 或 :pure-addition 都可以，subtract-91 表示「除去」，与原意不合。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0021.umr:935) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0021.umr:945) · [gold](data/gold/chinese_umr-0021.umr:842)

### D1　小词或中心语没有进图

「也、亦、其中、这条、等等、到」之类没有节点。主要是 s3（整篇一次输出时省略更多），a2 明显少。

条目 113：涉及 s3 的 89 条（错 7），涉及 a2 的 42 条（错 3）；其中 gold 也是同样写法的 32 条。

- **en-0000 第 90 句**（a2/r2，错）有没有 part 节点：`没有 part，south :part-of peninsula`；较好的写法：`part :part-of/:part peninsula`。the southern part of the peninsula 的中心词是 part，a2/r2 把 part 丢了，让 south 直接作 signify 的 ARG1。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0000.umr:5136) · [gold](data/gold/en-0000.umr:4431)
- **zh-0005 第 11 句**（s3/r2，错）「到山东」的节点：`没有 到，招生 :place 山东`；较好的写法：`到-01 :ARG1 山东 :purpose 招生`。「到山东招生」有两个事件：到（PropBank 到-01 ARG1 arriving at）和目的招生；s3/r2 漏掉了「到」。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0005.umr:852) · [gold](data/gold/chinese_umr-0005.umr:814)
- **zh-0018 第 1 句**（s3/r1，错）「人道主义组织」与世界中央厨房：`没有标「人道主义组织」`。同位语「人道主义组织世界中央厨房」用 identity-91 或把「组织」略去只留 :mod 都可以；s3/r1 把这个修饰整个漏掉了。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0018.umr:2) · [gold](data/gold/chinese_umr-0018.umr:3)
- **zh-0024 第 3 句**（s3/r2，错）「是否」（嵌入的是非问）：`不表示「是否」`；较好的写法：`清楚 :ARG0 (truth-value :polarity-of 离开)`。完整 guideline 3-2-1-3 (1b)（I didn't see whether he bought the sweater）：嵌入的 whether 小句写成 truth-value :polarity-of 事件。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0024.umr:244) · [gold](data/gold/chinese_umr-0024.umr:242)
- **en-0006 第 6 句**（s3/r1、s3/r2，轻）what had been lush green valley farmland：`直接覆盖 farmland（丢了 what had been）`；较好的写法：`thing :ARG1-of (have-role-91 :ARG3 farmland)`。精简 guideline 2.3：have-role-91 的类别是 ARG3（训练数据里 have-role-91 也都用 :ARG3 写类别）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0006.umr:346) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0006.umr:347) · [gold](data/gold/en-0006.umr:299)
- **en-0008 第 4 句**（a2/r1、a2/r2，轻）reasons 的 refer-number：`没有 refer-number`；较好的写法：`reason :refer-number plural`。reasons 是复数名词，guideline 2.4 加 :refer-number plural。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0008.umr:166) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/en-0008.umr:163) · [gold](data/gold/en-0008.umr:141)
- **zh-0001 第 23 句**（s3/r1、s3/r2，轻）「其中」：`没有标`；较好的写法：`新闻 :mod 其中`。「其中数百篇」说明这些新闻是该刊新闻的一部分，「其中」有实义，漏标丢了部分关系。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0001.umr:1398) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0001.umr:1366) · [gold](data/gold/chinese_umr-0001.umr:1500)
- **zh-0002 第 45 句**（s3/r1、s3/r2，轻）「这条」的表示：`没有标「这条」`；较好的写法：`推特 :mod 这 + :unit 条`。【更正】量词按规则保留为 :unit。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0002.umr:3298) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0002.umr:3247) · [gold](data/gold/chinese_umr-0002.umr:3278)
- **zh-0004 第 15 句**（s3/r1、s3/r2，轻）「到（新星球）」：`没有「到」，星球作重过的处所`。「到一个新的星球重过新生」有移动事件「到」（PropBank 到-01 ARG1 arriving at）；只保留重过 :place 星球 丢了这个事件。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0004.umr:954) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0004.umr:977) · [gold](data/gold/chinese_umr-0004.umr:1032)
- **zh-0015 第 5 句**（s3/r1、a2/r2，轻）「有校」「有中学生家长」的「有」：`不表示`。同第 2 句：「有 N VP」的「有」表示部分存在（有的学校、有的家长），exist-91 是 guideline 2.3 的写法；gold 用 :quant 有 不规范但保留了意思，不表示则丢了这层意思。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0015.umr:293) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0015.umr:299) · [gold](data/gold/chinese_umr-0015.umr:282)
- **zh-0028 第 3 句**（a2/r1、a2/r2，轻）「等等」：`不表示`。列举后的「等等」可以作 and 的一个 op（AMR 的 et-cetera 惯例），也可以作修饰语；丢掉则漏了「列举不完全」的信息。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0028.umr:85) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0028.umr:86) · [gold](data/gold/chinese_umr-0028.umr:100)
- **zh-0029 第 16 句**（s3/r1、s3/r2，轻）「因为」与句子顶层结构：`and :op1 存在 :op2 否认（丢了「因为」）`。「因为」引出原因（guideline 2.5，:cause 或 have-cause-91；训练数据里 have-cause-91 的 ARG1 是结果、ARG2 是原因）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0029.umr:1056) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0029.umr:1092) · [gold](data/gold/chinese_umr-0029.umr:1014)


## 六、属性

### A　aspect 取值

未实现的事件（试图杀死、计划发动）标 performance；能力句、一次性的状态变化（出任、暂停、停驶）标 state；持续一段时间的事件标 performance；s3 偏爱 activity；a2 的事件名词常常没有 aspect。

条目 179：涉及 s3 的 96 条（错 7），涉及 a2 的 112 条（错 11）；其中 gold 也是同样写法的 33 条。

- **zh-0004 第 26 句**（s3/r1、a2/r1、a2/r2，错）「试图」「杀死」的 aspect：`杀死 performance（试图 performance / state / endeavor）`；较好的写法：`试图 performance，杀死 process`。格拉斯救了博士，杀死没有发生，不能标 performance；试图 是没达到目的的尝试，endeavor 或 performance 都可（state 不对）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0004.umr:1770) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0004.umr:1923) · [gold](data/gold/chinese_umr-0004.umr:1887)
- **zh-0002 第 45 句**（s3/r2，错）未然事件（寻找、煽动、发动）的 aspect：`寻找、发动 performance`。寻找是「需要」的补足语、发动是被煽动去做的事，都没有发生，不能标 performance（abridged 4.1：performance 是完成并达到结果的事件）；process / activity 都可接受。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0002.umr:3269) · [gold](data/gold/chinese_umr-0002.umr:3278)
- **zh-0003 第 5 句**（a2/r1，错）「追溯」的 aspect：`performance`；较好的写法：`state`。「历史可追溯至…」描述一个现存的状态，不是完成的事件（guideline 4.1）。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0003.umr:412) · [gold](data/gold/chinese_umr-0003.umr:415)
- **zh-0005 第 20 句**（a2/r1、a2/r2，错）「出任」的 aspect：`state`（gold 也这样写）；较好的写法：`performance`。「2003 年 3 月出任团长」是在某一时点完成的就任事件，不是状态（担任才是状态）；应为 performance。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0005.umr:1424) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0005.umr:1423) · [gold](data/gold/chinese_umr-0005.umr:1398)
- **zh-0007 第 21 句**（a2/r1、a2/r2，错）「目睹」的 aspect：`state`（gold 也这样写）；较好的写法：`performance`。「目睹杀人事件」是已经发生并完成的感知事件，按 guideline 4.1 应为 performance；目睹不是状态谓词。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0007.umr:1294) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0007.umr:1315) · [gold](data/gold/chinese_umr-0007.umr:1328)
- **zh-0010 第 6 句**（a2/r2，错）「决定」的 aspect：`决定 performance`（gold 也这样写）；较好的写法：`决定 habitual`。「女方在结婚前也会视男方条件决定金额」是惯常描述（会 + 泛指主语），精简版 4.1：经常、反复发生的事件用 habitual；performance 是已经完成的具体事件，不合。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0010.umr:350) · [gold](data/gold/chinese_umr-0010.umr:381)
- **cs-0000 第 15 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）konat se 的 aspect 与 modal-strength：`:aspect activity`；较好的写法：`:aspect performance`。guideline 第 7 节：每个事件都要有 :aspect；gold 本文件每个事件也都写 :modal-strength，唯独 konat-se-001 两个都漏了。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0000.umr:730) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0000.umr:767) · [gold](data/gold/cs-0000.umr:705)
- **cs-0001 第 18 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）varovat 的 aspect：`activity`；较好的写法：`performance`。「varoval」是完成的过去言语行为，按精简版 4.1 是 performance。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0001.umr:852) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0001.umr:890) · [gold](data/gold/cs-0001.umr:984)
- **cs-0004 第 21 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）reprezentovat 的 aspect：`process`；较好的写法：`state`。「změny reprezentují nové zaměření」（变化代表新方向）是状态谓词，精简版 4.1 判 state。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/cs-0004.umr:1283) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/cs-0004.umr:1275) · [gold](data/gold/cs-0004.umr:1532)
- **zh-0009 第 7 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「售卖」的 aspect：`performance`。「刚推出时售卖 1,500 美元」说的是一段时间里的售价，不是一次完成的事件；activity、state 都说得通，performance 不合适。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0009.umr:412) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0009.umr:415) · [gold](data/gold/chinese_umr-0009.umr:420)
- **zh-0023 第 4 句**（s3/r1、s3/r2、a2/r1、a2/r2，轻）「停留了15分钟」的 aspect：`performance`。完整 guideline 3-3-1-5：时段状语（for thirty minutes）是 endeavor 的强证据，不该是 performance。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0023.umr:269) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0023.umr:269) · [gold](data/gold/chinese_umr-0023.umr:228)
- **en-0006 第 24 句**（s3/r1、a2/r1、a2/r2，轻）reach 的 aspect：`reach-01 :aspect state`；较好的写法：`reach-01 :aspect performance`。到达是已完成的达成事件，performance；标 state 是把 able 的能力当成了事件本身（guideline 4.1：明显完成的事件标 state 算错，这里因 able 的干扰只记 minor）。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0006.umr:1717) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0006.umr:1725) · [gold](data/gold/en-0006.umr:1623)

### P　否定的位置和极性

否定加在错的节点上（「不是所有人」否定了谓词，「说不清楚」两处都加），反问句「还不赶快」读成否定，「险被淘汰」另加 `:polarity -`，嵌入的是非问写成 `:polarity amr-unknown`。

条目 23：涉及 s3 的 12 条（错 3），涉及 a2 的 14 条（错 2）；其中 gold 也是同样写法的 1 条。

- **cs-0000 第 41 句**（a2/r2，错）bez … souhlasu（未经同意）的否定：`:companion souhlas，没有否定`；较好的写法：`:condition (souhlas :polarity -)`。bez 是“没有”：不经他同意就不授予。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/cs-0000.umr:2208) · [gold](data/gold/cs-0000.umr:2034)
- **en-0007 第 26 句**（s3/r1，错）not necessarily 的表示：`combine 本身 :polarity -（partial-negative）`。not necessarily 是「不一定（都和利益挂钩）」，否定的是必然性，不是 combine 本身。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0007.umr:1665) · [gold](data/gold/en-0007.umr:1707)
- **zh-0028 第 12 句**（s3/r2，错）「还不赶快」的极性：`带 :polarity -`；较好的写法：`不标 polarity（反问式催促）`。「还不赶快把福韵带回家！」是反问式催促，意思是「赶快带回家」，不是否定。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/zh-0028.umr:719) · [gold](data/gold/chinese_umr-0028.umr:616)
- **zh-0029 第 17 句**（s3/r1，错）「说不清楚」的否定位置：`说 和 清楚 都 :polarity -`。「说不清楚」是能性补语的否定（不能说清楚），否定放在 说 或 清楚 上都能表达；两处都标就成了双重否定。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0029.umr:1157) · [gold](data/gold/chinese_umr-0029.umr:1092)
- **zh-0036 第 14 句**（a2/r2，错）「不是所有人」否定的位置：`能 / 买 :polarity -（所有人都不能）`。「不是所有人都能买得起」是部分否定，否定落在「所有」上（not all）；否定放在 买 / 能 上意思变成「所有人都买不起」，错。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0036.umr:751) · [gold](data/gold/chinese_umr-0036.umr:768)
- **cs-0002 第 4 句**（a2/r1、a2/r2，轻）否定的表达（polarity、žádný）：`mít 和 žádný 都带 :polarity -`；较好的写法：`mít :polarity -，žádný 不带 polarity`。捷克文否定一致（ne- ... žádný）只表达一个否定：训练数据 wsj2106 第 25 句 nestřetává ... žádný 只在动词上标 :polarity -；a2 在 žádný 上再标一次是重复。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/cs-0002.umr:77) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/cs-0002.umr:78) · [gold](data/gold/cs-0002.umr:109)
- **en-0000 第 18 句**（s3/r1、s3/r2，轻）unclear whether 的结构：`clear-06 / have-mod-91 clear :polarity -，impact-01 :polarity amr-unknown`；较好的写法：`clear-06 :polarity - :ARG1/:theme (truth-value :polarity-of impact-01)`。完整 guideline 3-2-1-3 例 (1b)（I didn't see whether he bought the sweater）：whether 从句写成 (truth-value :polarity-of 事件)。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0000.umr:951) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0000.umr:961) · [gold](data/gold/en-0000.umr:815)
- **en-0005 第 18 句**（s3/r1、s3/r2，轻）附加问 doesn't he：`:mode interrogative + :polarity umr-unknown / amr-unknown`；较好的写法：`:ARG1-of (request-confirmation-91)`。附加问是在求证一个肯定的判断，AMR/UMR 用 request-confirmation-91（训练数据 863 处）；当成普通是非问会把说话人倾向肯定的意思丢掉。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/en-0005.umr:1084) · [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0005.umr:1079) · [gold](data/gold/en-0005.umr:1151)
- **zh-0015 第 13 句**（a2/r1、a2/r2，轻）「可以不必穿」的表示：`穿 :polarity -，author :neutral-negative 穿`；较好的写法：`穿 :polarity -，学校 :neutral-negative 穿`。guideline 2.1：情态词（可以、必、能、应该）不立节点，体现在 modal 强度上；「可以不必穿」＝不穿也可以，穿 :polarity -、强度 neutral-negative。 [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/zh-0015.umr:1007) · [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0015.umr:972) · [gold](data/gold/chinese_umr-0015.umr:865)
- **zh-0024 第 3 句**（s3/r1，轻）「是否」（嵌入的是非问）：`离开 :polarity umr-unknown / amr-unknown`；较好的写法：`清楚 :ARG0 (truth-value :polarity-of 离开)`。完整 guideline 3-2-1-3 (1b)（I didn't see whether he bought the sweater）：嵌入的 whether 小句写成 truth-value :polarity-of 事件。 [s3/r1](runs/s3-all/gpt-6.1-sol-medium-r1/zh-0024.umr:266) · [gold](data/gold/chinese_umr-0024.umr:242)
- **zh-0027 第 9 句**（a2/r2，轻）「无法再联系上」的否定：`联系 :polarity -，另留 :mod 无法`；较好的写法：`联系 :polarity -（不立「无法」）`。精简 guideline 4.2：否定用 :polarity -，事件的 modal 强度随之为 negative。 [a2/r2](runs/a2-sentence-all/gpt-6.1-sol-medium-r2/zh-0027.umr:886) · [gold](data/gold/chinese_umr-0027.umr:812)
- **en-0007 第 16 句**（s3/r2、a2/r1、a2/r2，轻）or not to say no：say 的极性与 no：`say-01 :polarity - :ARG1 no`。原话 whether to endorse it or not to say no 意思是在「批准」和「说不（拒绝）」之间选择；给 say 加 :polarity - 就成了「不说不」，与第一个选项相同，选择失去意义，所以不带 polarity 的读法更好。 [s3/r2](runs/s3-all/gpt-6.1-sol-medium-r2/en-0007.umr:962) · [a2/r1](runs/a2-sentence-all/gpt-6.1-sol-medium-r1/en-0007.umr:953) · [gold](data/gold/en-0007.umr:1016)
