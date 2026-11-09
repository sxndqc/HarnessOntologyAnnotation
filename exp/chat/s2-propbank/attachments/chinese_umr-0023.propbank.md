# PropBank entries for the words of chinese_umr-0023

From ai-native-annotator.github.io data/skillparse/resources/propbank/zh.json: every roleset of every word of the document that PropBank has.

## 载人

### 载人-01

- ARG0: agent

Example 1: *pro* 以前 总 觉得 ， 中国 这么 一 个 *OP* *T*-1 能够 载人 航天 的 航天 大国 ， 间谍 卫星 、 侦查 卫星 总 该 有 几 颗 吧 ， 可能 数量 不 会 很 多 。
- ARG0: *T*-1(NP (NN 航天) (NN 大国))
- rel: 载人

## 航天

### 航天-01

- ARG0: agent

Example 1: *pro* 以前 总 觉得 ， 中国 这么 一 个 *OP* *T*-1 能够 载人 航天 的 航天 大国 ， 间谍 卫星 、 侦查 卫星 总 该 有 几 颗 吧 ， 可能 数量 不 会 很 多 。
- ARG0: *T*-1(NN 航天) (NN 大国)
- rel: 航天

## 是

### 是-01

- ARG0: entity being predicated
- ARG1: predicative

Example 1: 藏 羚羊 、 野 牦牛 、 藏 野 驴 、 雪豹 、 宗熊 、 盘羊 等 都 是 珍稀 动物
- ARG0: 藏 羚羊 、 野 牦牛 、 藏 野 驴 、 雪豹 、 宗熊 、 盘羊 等
- ARG1: 珍稀 动物
- ARGM-ADV: 都
- rel: 是

Example 2: 狮子会 的 宗旨 是 “ 我们 服务 ”
- ARG0: 狮子会 的 宗旨
- ARG1: “ 我们 服务 ”
- rel: 是

Example 3: 据悉 ， 中科院 设立 优秀 博士后 奖励 基金 和 王宽诚 博士后 奖励 基金 是 为了 *PRO* 吸引 更 多 优秀 博士 毕业生 *PRO* 到 中科院 做 博士后 ， 强化 *RNR*-1 和 激励 博士后 研究 人员 的 科学 创新 意识
- ARG0: 中科院 设立 优秀 博士后 奖励 基金 和 王宽诚 博士后 奖励 基金
- ARG1: 为了 *PRO* 吸引 更 多 优秀 博士 毕业生 *PRO* 到 中科院 做 博士后 ， 强化 *RNR*-1 和 激励 博士后 研究 人员 的 科学 创新 意识
- ARGM-ADV: 据悉
- rel: 是

### 是-02

- ARG0: location
- ARG1: entity exists

Example 1: 里面 都 是 水生 的 植物
- ARG0: 里面
- ARGM-ADV: 都
- ARG1: 水生 的 植物
- rel: 是

### 是-03

- ARG0: the entity that is confirmed (usually omitted by *pro*)

Example 1: *pro* 是
- ARG0: *pro*
- rel: 是

### 是-04

- ARG0: 

Example 1: 我 做事 呢 ［ ［ ＮＳ ］ ］ 应当 是 办 实业
- rel: 是

## 指

### 指-01

- ARG0: agent
- ARG1: thing arg0 uses
- ARG2: entity arg0 refers to with arg1

Example 1: 我们 并 不 单 指 一 年 的 开支 增长 ， 而 是 以 多 年 期 作 规划
- ARG0: 我们
- ARG2: 一 年 的 开支 增长
- ARGM-ADV: 单
- ARGM-ADV: 不
- ARGM-ADV: 并
- rel: 指

Example 2: 这 是 指 外企 的 中方 管理 人员
- ARG1: 这
- ARG2: 外企 的 中方 管理 人员
- rel: 指

Example 3: 所谓 「 长 多 」 ， 究竟 指 *PRO* 多 长
- ARG1: 所谓 「 长 多 」
- ARG2: *PRO* 多 长
- ARGM-ADV: 究竟
- rel: 指

### 指-02

- ARG0: agent
- ARG1: thing arg0 points out/claims

Example 1: 电视台 新闻 报道 指 由於 连场 大雨 ， 水务署 在 城门 水塘 开启 水闸 排洪
- ARG0: 电视台 新闻 报道
- ARG1: 由於 连场 大雨 ， 水务署 在 城门 水塘 开启 水闸 排洪
- rel: 指

Example 2: 该 两 名 中国 人士 在 三月 时 已 被 指 *-3 *PRO* 行使 *OP* *pro* 伪造 *T*-2 中国 护照 和 管有 *OP* *pro* 伪造 *T*-1 香港 旅行 证件 而 分别 被 判 *-3 入狱 六 个 月
- ARG1: *-3
- ARG1-PRD: *PRO* 行使 *OP* *pro* 伪造 *T*-2 中国 护照 和 管有 *OP* *pro* 伪造 *T*-1 香港 旅行 证件
- ARGM-ADV: 已
- ARGM-TMP: 在 三月 时
- rel: 指

### 指-03

- ARG0: agent
- ARG1: patient
- ARG2: predicate

Example 1: 

### 指-04

- ARG0: agent
- ARG1: expecation

Example 1: 

### 指-05

- ARG0: agent
- ARG1: entity Arg0 points at

Example 1: 
- ARG1: 他
- rel: 指

## 由

### 由-01

- ARG0: people described
- ARG1: people arg0 arg0 will let make decision
- ARG2: thing arg1 makes decision on

Example 1: 我 高兴 *PRO* 把 他 拉成 条 ， 围 在 腰 上 ， *pro* 也 由 我
- ARG2: *pro*
- ARG1: 我
- ARGM-ADV: 也
- ARGM-CND: 我 高兴 *PRO* 把 他 拉成 条 ， 围 在 腰 上
- rel: 由

## 执行

### 执行-01

- ARG0: agent
- ARG1: patient

Example 1: 过往 ， *OP* *T*-1 由 联合国 实施 *-2 的 经济 制裁 是 依靠 英国 的 枢密院 颁令 在 香港 执行
- ARG1: *OP* *T*-1 由 联合国 实施 *-2 的 经济 制裁
- ARGM-LOC: 在 香港
- ARGM-MNR: 依靠 英国 的 枢密院 颁令
- ARGM-TMP: 过往
- rel: 执行

Example 2: *OP* 中外 合作 经营 *T*-1 企业 和 *OP* 外商 独资 经营 *T*-2 企业 比照 本 规定 执行
- ARG0: *OP* 中外 合作 经营 *T*-1 企业 和 *OP* 外商 独资 经营 *T*-2 企业
- ARGM-ADV: 比照 本 规定
- rel: 执行

Example 3: 工作 重点 是 坚决 贯彻 执行 *pro* 按 保护价 敞开 收购 余粮
- ARG1: *pro* 按 保护价 敞开 收购 余粮
- ARGM-ADV: 坚决
- rel: 执行

Example 4: *pro* 坚定不移 地 执行 *PRO* 自力更生 、 艰苦 奋斗 、 勤俭 建 国 的 方针
- ARG0: *pro*
- ARG1: *PRO* 自力更生 、 艰苦 奋斗 、 勤俭 建 国 的 方针
- ARGM-ADV: 坚定不移 地
- rel: 执行

Example 5: *OP* *T*-1 由 美 、 英 、 法 三 国 共同 执行 *-2 的 对 伊 南部 的 空中 监视 行动
- ARG0: 由 美 、 英 、 法 三 国
- ARG1: *-2
- ARGM-ADV: 共同
- rel: 执行

## 探索

### 探索-01

- ARG0: agent
- ARG1: thing explored

Example 1: 此外 ， 各 地 还 在 进一步 探索 一些 新型 的 人才 引进 和 管理 办法
- ARG0: 各 地
- ARG1: 一些 新型 的 人才 引进 和 管理 办法
- ARGM-ADV: 进一步
- ARGM-ADV: 在
- ARGM-ADV: 还
- ARGM-ADV: 此外
- rel: 探索

Example 2: *OP* *T*-1 即将 过去 的 二十 世纪 ， 是 *OP* 中国人 *T*-2 百折不挠 地 寻觅 、 探索 的 世纪
- ARG0: 中国人
- ARGM-ADV: 百折不挠 地
- ARGM-TMP: *T*-2
- rel: 探索

Example 3: *pro* 围绕 *pro* 发挥 杭州 、 宁波 、 温州 等 中心 城市 对 外 开放 的 先导 作用 ， 加快 浙江 中西部 地区 和 农业 、 海岛 、 海洋 的 对 外 开放 力度 ， 探索 *pro* 扩大 金融 和 零售 商业 进行 中外 合资 、 合作 的 试点 ， 争取 *PRO* 在 长江 三角洲 经济带 的 开发 开放 中 创造 新 优势
- ARG0: *pro*
- ARG1: *pro* 扩大 金融 和 零售 商业 进行 中外 合资 、 合作 的 试点
- rel: 探索

### 探索-02

- ARG0: agent
- ARG1: thing found through exploration

Example 1: *pro* 探索 出 胶结 充填 采矿法
- ARG0: *pro*
- ARG1: 胶结 充填 采矿法
- rel: 探索

## 可以

### 可以-01

- ARG0: 

### 可以-02

- ARG0: thing that could pass, be feasible

Example 1: *PRO* 去 个 四 *RNR*-1 、 五 次 就 可以 了
- ARG0: *PRO* 去 个 四 *RNR*-1 、 五 次
- ARGM-DIS: 就
- rel: 可以

### 可以-03

- ARG0: agent
- ARG1: things Arg0 is capalbe of

Example 1: 
- rel: 可以

## 均

### 均-01

- ARG0: thing described

Example 1: 赌场 因 利益 不 均 ， 导致 帮派 火拼
- ARG0: 利益
- ARGM-ADV: 不
- rel: 均

Example 2: *PRO* 受热 不 均
- ARG0: *PRO*
- ARG0-PRD: 受热
- ARGM-ADV: 不
- rel: 均

## 需

### 需-01

- ARG0: agent
- ARG1: theme

Example 1: 首 期 先 建 两 台 ， 约 需 投资 四十亿 美元 。
- ARG0-: 首 期
- ARGM-ADV: 约
- rel: 需

Example 2: 美国 以 *PRO* 最终 控制 中亚 大部分 能源 为 目标 ， 瞄准 中亚 国家 急 需 外援 而 俄 无法 满足 它们 的 需要 这 一 缺口
- ARG0-: 中亚 国家
- ARGM-ADV: 急
- rel: 需

### 需-02

- ARG0: party in need
- ARG1: theme
- ARG2: predicate

Example 1: 但 整 个 峡谷 长度 、 平均 深度 和 最大 深度 仍 需 测绘 部门 *PRO* 进一步 核实 才 能 公布
- ARG0-: 整 个 峡谷 长度 、 平均 深度 和 最大 深度
- ARGM-ADV: 仍
- rel: 需

### 需-03

- (no roles)

## 使用

### 使用-01

- ARG0: agent
- ARG1: entity used
- ARG2: entity used for

Example 1: 电厂 使用 这 种 乳化油 已经 取得 了 *OP* *T*-1 令 人 *PRO* 满意 的 结果
- ARG0: 电厂
- ARG1: 这 种 乳化油
- rel: 使用

Example 2: 传统 的 发电 ， 一般 都 使用 煤 、 水 、 油 等
- ARG2: 传统 的 发电
- ARG1: 煤 、 水 、 油 等
- ARGM-ADV: 都
- ARGM-ADV: 一般
- rel: 使用

Example 3: *PRO* 将 *OP* *T*-1 可 盈利 百万 元 以上 的 一 整 套 “ 王码 软件 精品 ” ， 免 收 技术 费用 ， 全部 以 *OP* *T*-2 不 加密 的 软盘 方式 对 国内 “ 开放 ” ， 从而 使 国内 任何 微机 用户 *PRO* 都 可以 拷贝 使用
- ARG0: *PRO*
- ARGM-ADV: 都
- rel: 使用

Example 4: 它 会 对 用户 文件 进行 加密 ， 从而 使 这些 文件 *PRO* 变 得 无法 使用
- ARG1: *PRO*
- ARGM-ADV: 无法
- rel: 使用

Example 5: 此 车 相对 固定 给 崔广华 使用
- ARG0: 给 崔广华
- ARG1: 此 车
- ARGM-ADV: 固定
- ARGM-ADV: 相对
- rel: 使用

## 进行

### 进行-01

- ARG0: agent
- ARG1: thing arg0 carries out

Example 1: *pro* 然后 有 专门 队伍 进行 监督 检查
- ARG0: 专门 队伍
- ARG1: 监督 检查
- rel: 进行

Example 2: 新 技术 的 推广 应用 主要 由 企业 依靠 市场 机制 来 进行
- ARG0: 由 企业
- ARG1: 新 技术 的 推广 应用
- ARGM-ADV: 主要
- rel: 进行

Example 3: 据 介绍 ， 北仑港 二 期 集装箱 码头 目前 正在 进行 前期 筹备
- ARG1-PSE: 前期 筹备
- ARG1-PSR: 北仑港 二 期 集装箱 码头
- ARGM-ADV: 正在
- ARGM-TMP: 目前
- ARGM-MNR: 据 介绍
- rel: 进行

Example 4: 小浪底 水利 枢纽 工程 地下 厂房 的 引水洞 原 设计 要求 是 全部 进行 钢盘 混凝土 衬砌
- ARG1: 钢盘 混凝土 衬砌
- ARGM-ADV: 全部
- rel: 进行

Example 5: 据 介绍 ， 对 *OP* *T*-4 最 轻 的 男婴 的 抢救 进行 了 一 个 半 小时 ， 但 没有 成功
- ARG1: 对 *OP* *T*-4 最 轻 的 男婴 的 抢救
- ARGM-ADV: 一 个 半 小时
- ARGM-MNR: 据 介绍
- rel: 进行

Example 6: 市民 *PRO* 如 欲 *PRO* 竞投 债券 ， 可 透过 公布 名单 上 任何 一 名 市场 庄家 或 认可 交易商 进行
- ARG0: 市民
- ARGM-MNR: 透过 公布 名单 上 任何 一 名 市场 庄家 或 认可 交易商
- ARGM-CND: *PRO* 如 欲 *PRO* 竞投 债券
- rel: 进行

Example 7: 比赛 共 进行 五 轮
- ARG1: 比赛
- ARG1-QTY: 五 轮
- ARGM-ADV: 共
- rel: 进行

### 进行-02

- ARG0: agent
- ARG1: thing arg0 keeps going

Example 1: 中方 希望 这 一 会谈 能够 继续 进行 下去 并 不断 取得 进展
- ARG1: 这 一 会谈
- rel: 进行

### 进行-03

- ARG0: agent
- ARG1: thing arg0 carries out
- ARG2: time/place/state arg1 is carried on until 

Example 1: 可惜 省方 尚 未 进行 到 *PRO* 将 此 精神 扩大 至 其他 河川 上 实施
- ARG0: 省方
- ARG2: *PRO* 将 此 精神 扩大 至 其他 河川 上 实施
- ARGM-ADV: 未
- ARGM-ADV: 尚
- ARGM-ADV: 可惜
- rel: 进行

### 进行-04

- ARG0: entity that moves forward

## 为止

### 为止-01

- ARG0: agent/cause
- ARG1: thing arg0 stops
- ARG2: time arg1 stops

Example 1: *pro* 至 其 成年 为止
- ARG1: *pro*
- ARG2: 至 其 成年
- rel: 为止

Example 2: *PRO* 包括 产业 的 复苏 和 心灵 的 重建 ， *pro* 必须 做到 最後 一 人 的 照顾 、 最後 一 处 的 重建 完成 为止
- ARG0: *pro*
- ARG1: *PRO* 包括 产业 的 复苏 和 心灵 的 重建
- rel: 为止

## 只有

### 只有-01

- ARG0: entity that exists
- ARG1: agent/owner

Example 1: *OP* *T*-2 达到 室外 跳远 标准 的 选手 也 只有 １３ 人
- ARG0: *OP* *T*-2 达到 室外 跳远 标准 的 选手
- ARG0-QTY: １３ 人
- ARGM-ADV: 也
- rel: 只有

## 继承

### 继承-01

- ARG0: inheriter
- ARG1: thing inherited

Example 1: *PRO* 纪念 皖南 事变 ５０ 周年 ， 对于 *PRO* 继承 *RNR*-2 和 发扬 新四军 的 优良 传统 ， 吸取 历史 经验 ， 促进 部队 改革 和 建设 ， 具有 *OP* *T*-1 重要 的 现实 意义
- ARG0: *PRO*
- ARG1: 新四军 的 优良 传统
- rel: 继承

## 有

### 有-01

- ARG0: owner
- ARG1: entity owned

Example 1: 原 苏联 解体 后 ， 该 军队 集群 转归 俄罗斯 *PRO* 所 有
- ARG0-: *PRO*
- rel: 有

Example 2: *OP* *T*-1 统一 的 德国 能够 在 联合国 发挥 *OP* *T*-2 更 大 的 作用 ， 在 联合国 作出 决定 时 有 *OP* *T*-3 更 大 的 发言权
- rel: 有

### 有-02

- ARG0: entity described
- ARG1: predicative (often quantity of arg0)

Example 1: *OP* *T*-1 第五 个 出生 的 男婴 体重 最 轻 ， 只 有 四百九十五 克
- ARG0-PSE: 体重
- ARG0-PSR: *T*-1 第五 个 出生 的 男婴
- ARGM-ADV: 只
- rel: 有

### 有-03

- ARG0: location/domain described
- ARG1: entity that exists with respect to arg0

Example 1: 中国 现 有 保险 公司 二十六 家
- ARG0-: 中国
- ARGM-TMP: 现
- rel: 有

Example 2: 据 统计 ， 今年 全 省 高新区 的 技工贸 总 收入 、 *OP* *pro* 完成 *T*-3 的 工业 总 产值 均 比 去年 有 较大 幅度 增长
- ARG0-: 全 省 高新区的技工贸总收入 、 完成的工业总产值
- ARGM-ADV: 均
- ARGM-TMP: 今年
- rel: 有

Example 3: 随着 内地 贸易 、 金融 、 零售 等 服务业 有 步骤 地 对 外 开放
- ARG1-: 步骤
- rel: 有

### 有-04

- ARG0: 

Example 1: *OP* *T*-1 实际上 有 领取 奖金 的 传销商
- rel: 有

### 有-05

- ARG0: entity described
- ARG1: state/event that exists with respect to arg0

Example 1: *pro* 有 八 家 外资 银行 获准 *PRO* 在 上海 浦东 经办 人民币 业务
- ARG0-: *pro*
- ARG1-: 八 家 外资 银行 获准 *PRO* 在 上海 浦东 经办 人民币 业务
- rel: 有

### 有-06

- ARG0: entity described
- ARG1: entity owned by/exist with respect to arg0

Example 1: *PRO* 虽然 开发 有 整车 产品 三 个 系列 二十三 个 品种 ， 改装车 产品 三 个 系列 十二 个 品种
- ARG0-: *PRO*
- ARG1-: 整车 产品
- ARG1-QTY: 三 个 系列 二十三 个 品种
- ARG1-: 改装车 产品
- ARG1-QTY: 三 个 系列 十二 个 品种
- rel: 有

### 有-07

- ARG0: entity described
- ARG1: entities arg0 includes

Example 1: 据悉 ， 这些 新 措施 的 主要 内容 有 *PRO* 以 *PRO* 发展 规模 经营 、 组建 企业 集团 为 重点 ， 推进 省属 外贸 公司 的 战略性 重组 ； 加大 *OP* 支柱 产业 产品 *T*-1 出口 的 力度 ； 办好 *OP* *T*-2 在 香港 举办 的 外商 投资 招商会 和 九八 中国 投资 贸易 洽谈会 等
- ARG0-: 这些 新 措施 的 主要 内容
- ARG1-: 以发展规模经营 、组建企业集团为重点 ， 推进省属外贸公司的战略性重组 ；加大支柱产业产品出口的力度 ；办好在香港举办的外商投资招商会和九八中国投资贸易洽谈会等
- ARGM-ADV: 据悉
- rel: 有

### 有-08

- ARG0: entity described
- ARG1: activity

Example 1: 个别 企业 及 公司 的 业务 在 某些 环节 如 不 获 任何 协助 ， *pro* 就 难 有 贡献
- ARG0-: *pro*
- ARG1-: 贡献
- ARGM-DIS: 就
- ARGM-ADV: 难
- rel: 有

Example 2: 帛琉 则 成为 美国 的 托管 地 ， 并 於 一九八○ 年代 开始 与 我 国 有 了 政治 上 的 接触
- ARG0-CRD: 帛琉
- rel: 有

### 有-09

- ARG0: entity described
- ARG1: amount extra

Example 1: 古稀 有 二
- ARG0-: 古稀
- ARG1-: 二
- rel: 有

## 独立

### 独立-01

- ARG0: theme
- ARG1: independent of

Example 1: 吉尔吉斯 独立 以后 两 国 关系 发展 顺利
- ARG0: 吉尔吉斯
- rel: 独立

## 完成

### 完成-01

- ARG0: agent
- ARG1: theme

Example 1: 全 年 全 省 完成 工业 增加值 二百八十七点一亿 元
- ARG0: 全 省
- rel: 完成

Example 2: 声明 强调 俄罗斯 完成 撤军 应 促进 俄 同 波罗的海 国家 关系 的 发展 。
- ARG0: 俄罗斯
- rel: 完成

Example 3: 出口 创汇 完成 四亿 美元
- ARG1: 出口 创汇
- rel: 完成

Example 4: 改革 的 任务 才 能 顺利 完成
- ARG1: 改革 的 任务
- ARGM-ADV: 顺利
- rel: 完成

## 上

### 上-01

- ARG0: entity moving
- ARG1: place arg0 goes to, entity used or surfed(internet)

Example 1: *OP* *T*-1 上 因特网 的 个人 将 从 １９９６年 底 的 ８６００万 人 增加 到 ２．５亿 人
- ARG0-: *T*-1
- ARG1-: 因特网
- rel: 上

### 上-02

- ARG0: agent
- ARG1: school

Example 1: 丁豪 在 儿童 福利院 读完 小学 ， 随后 进入 附近 乡里 一 所 学校 上 初中
- ARG0-: 丁豪
- ARG1-: 初中
- ARGM-ADV: 随后
- rel: 上

### 上-03

- ARG0: entity described
- ARG1: place arg0 climbs onto

Example 1: 使 上海 经济 *PRO* 再 上 新 台阶
- ARG0-: *PRO*
- ARG1-: 新 台阶
- ARGM-ADV: 再
- rel: 上

### 上-04

- ARG0: thing described
- ARG1: level arg0 reaches

Example 1: *OP* *T*-1 产值 上 亿 元 人民币 的 已 达 五十多 个
- ARG0-PSE: 产值
- ARG0-PSR: *T*-1
- ARG1-: 亿 元 人民币
- rel: 上

### 上-05

- ARG0: agent
- ARG1: thing arg0 (hands to)
- ARG2: entity arg1 is handed to

Example 1: 汉 初 长安 少年 贾谊 上 〈 *PRO* 治安 策 〉 、 写 〈 *PRO* 过 秦 论 〉 ， 分析 *RNR*-1 、 批评 秦朝 的 错误 ， 提醒 汉朝 统治者 *PRO* 应 以 暴 秦 为 鉴戒 ， 施行 仁政 ， 以免 *PRO* 重蹈覆辙
- ARG0-: 长安 少年 贾谊
- ARG1-: 〈 *PRO* 治安 策 〉
- ARGM-TMP: 汉 初
- rel: 上

### 上-06

- ARG0: entity described
- ARG1: thing (trap) arg0 gets into

Example 1: *pro* 上 一 次 当 学 一 次 乖
- ARG0-: *pro*
- ARG1-: 一 次 当
- rel: 上

### 上-07

- ARG0: agent
- ARG1: lesson

Example 1: 戈尔 将 在 纽约 的 哥伦比亚 大学 给 研究生 上 新闻学 课 。
- ARG0-: 戈尔
- ARG1-: 新闻学 课
- ARGM-ADV: 将
- ARGM-LOC: 纽约 的 哥伦比亚 大学
- ARGM-BNF: 给 研究生
- rel: 上

### 上-08

- ARG0: agent
- ARG1: implement, start

Example 1: *pro* 基本 是 上 这么 三 大 功能
- ARG0-: *pro*
- ARGM-ADV: 基本
- ARG1-: 这么 三 大功能
- rel: 上

### 上-09

- (no roles)

### 上-010

- ARG0: entity described
- ARG1: registration
- ARG2: person who does the registration

Example 1: *OP* *T*-1 上 了 目录
- ARG0: *T*-1
- ARG1: 目录
- rel: 上

Example 2: 以前 小孩 的 户口 是 要 跟着 母亲 上 的
- ARGM-ADV: 以前
- rel: 上

### 上-011

- ARG0: agent
- ARG1: goods

Example 1: 红英 又 快 上 秋装 了
- ARG0: 红英
- ARGM-ADV: 又
- ARGM-ADV: 快
- ARG1: 秋装
- rel: 上

### 上-012

- ARG0: agent
- ARG1: MWE usage, work place

## 日

### 日-01

- ARG0: agent
- ARG1: patient

Example 1: 洋狗 爹 日 出来 *T*-1
- rel: 日

### 日-02

- (no roles)

## 发射

### 发射-01

- ARG0: shooter, launcher
- ARG1: thing launched
- ARG2: target

Example 1: 安盟 向 该 地 发射 了 *OP* *T*-1 密集 的 火箭炮
- ARG0: 安盟
- ARG1: *OP* *T*-1 密集 的 火箭炮
- ARG2: 向 该 地
- rel: 发射

Example 2: 俄 又 发射 三 颗 全球 定位 卫星
- ARG0: 俄
- ARG1: 三 颗 全球 定位 卫星
- ARGM-ADV: 又
- rel: 发射

## 号

### 号-01

- ARG0: agent
- ARG1: person arg0 names
- ARG2: name

Example 1: 耳顺 之 年 以後 ， 王壮为 自 号 「 渐斋 」 ， 自称 「 渐叟 」 ， 为 自己 刻 了 一 印
- ARG0: 王壮为
- ARG2: 「 渐斋 」
- ARGM-ADV: 自
- ARGM-TMP: 耳顺 之 年 以後
- rel: 号

## 在

### 在-01

- ARG0: entity that exists
- ARG1: location arg0 is located

Example 1: 该 项 展览 旨 在 *PRO* 向 雇主 及 求职者 推广 劳工处 的 免费 就业 选配 服务
- ARG0-PSE: 旨
- ARG0-PSR: 该 项 展览
- ARG1: *PRO* 向 雇主 及 求职者 推广 劳工处 的 免费 就业 选配 服务
- rel: 在

Example 2: 电子 工业 产值 前 七 名 的 市 均 在 三角洲 内
- ARG0: 电子 工业 产值 前 七 名 的 市
- ARG1: 三角洲 内
- ARGM-ADV: 均
- rel: 在

Example 3: *PRO* 只要 渡 过 眼前 价格 混乱 、 景气 浑沌 的 调整期 ， *OP* *T*-1 元气 饱满 的 台商 ， *PRO* 相较於 *OP* *T*-2 里 外 受创 的 对手 ， 优势 仍 在
- ARG0-PSE: 优势
- ARG0-PSR: *OP* *T*-1 元气 饱满 的 台商
- ARGM-ADV: 仍
- ARGM-ADV: *PRO* 相较於 *OP* *T*-2 里 外 受创 的 对手
- ARGM-CND: *PRO* 只要 渡 过 眼前 价格 混乱 、 景气 浑沌 的 调整期
- rel: 在

### 在-02

- ARG0: entity described
- ARG1: location determining factor of agr0 lies in

Example 1: 兵 不 在 多 而 在于 精
- ARG0: 兵
- ARG1: 多
- ARGM-ADV: 不
- rel: 在

### 在-03

- ARG0: 

Example 1: 我 几乎 把 眼睛 紧贴 在 了 车窗 玻璃 上 ， 朝 后面 仰望
- rel: 在

## 环绕

### 环绕-01

- ARG0: theme
- ARG1: circling around, focusing on

Example 1: 剧本 环绕 一 名 中四 学生 *PRO* 第一 日 前往 一 间 学校 插班 报到 时 接触 教师 和 校长 的 经历 及 *OP* *pro* 从 中 所 得到 *T*-2 的 启发
- ARG0: 剧本
- ARG1: 一 名 中四 学生 *PRO* 第一 日 前往 一 间 学校 插班 报到 时 接触 教师 和 校长 的 经历 及 *OP* *pro* 从 中 所 得到 *T*-2 的 启发
- rel: 环绕

## 安全

### 安全-01

- ARG0: theme

Example 1: 另外 ， 付款 安全 。
- ARG0: 付款
- rel: 安全

## 返回

### 返回-01

- ARG0: returner
- ARG1: return to

Example 1: 在 滇 部分 老挝 难民 顺利 返回 家园
- ARG0: 在 滇 部分 老挝 难民
- ARG1: 家园
- ARGM-ADV: 顺利
- rel: 返回

## 自由

### 自由-01

- ARG0: entity described

Example 1: 香港 已 连续 四 年 成为 *OP* *T*-1 全球 最 自由 的 经济 体系
- ARG0: *T*-1
- ARGM-ADV: 最
- ARGM-LOC: 全球
- rel: 自由

## 成为

### 成为-01

- ARG0: theme
- ARG1: result
- ARG2: cause

Example 1: 外商 投资 企业 成为 中国 外贸 重要 增长点
- ARG0: 外商 投资 企业
- rel: 成为

Example 2: *PRO* 通过 *PRO* 将 国际 人权 法典 国内化 ， 成为 台湾 人权 法典
- ARG0: 国际 人权 法典
- ARG1: 台湾 人权 法典
- ARG2: *PRO*
- rel: 成为

## 了

### 了-01

- ARG0: agent
- ARG1: patient

Example 1: *pro* 如此 轻巧 ， *pro* 四九年 怕 早 就 了 了
- rel: 了

### 了-02

- ARG0: entity described

Example 1: *T*-1 不 了 情
- ARGM-ADV: 不
- rel: 了

### 了-03

- (no roles)

## 进入

### 进入-01

- ARG0: theme
- ARG1: place, time, phase, domain entered

Example 1: 迄今 ， 呼伦贝尔盟 十三 个 旗 市 已 全部 进入 全 国 电话 直拨网 ， 并 成为 *OP* *T*-1 中国 最 大 的 电话 本地网 。
- ARG0: 呼伦贝尔盟 十三 个 旗 市
- ARG1: 全 国 电话 直拨网
- ARGM-TMP: 迄今
- ARGM-ADV: 已
- rel: 进入

Example 2: 因此 正规 业者 一定 鼓励 *OP* *T*-2 有 兴趣 者 *PRO* 以 「 兼职 」 、 *PRO* 「 赚 点 外快 」 的 心态 进入
- ARG0: *PRO*
- ARGM-MNR: 以 「 兼职 」 、 *PRO* 「 赚 点 外快 」 的 心态
- rel: 进入

Example 3: 由于 投资 环境 不断 改善 ， 外资 企业 效益 良好 ， 跨国 公司 在 山东 已 由 试探性 投资 阶段 进入 规模 投资 阶段 。
- ARG0: 跨国 公司
- ARG1: 规模 投资 阶段
- ARGM-PRP: 由于 投资 环境 不断 改善 ， 外资 企业 效益 良好
- ARGM-LOC: 在 山东
- ARGM-ADV: 已
- ARGM-DIR: 由 试探性 投资 阶段
- rel: 进入

## 停留

### 停留-01

- ARG0: entity described
- ARG1: location arg0 stays in
- ARG2: agent

Example 1: 教改 不 能 只 停留 在 教育 的 技术性 层面 ， 而 缺乏 对 人文 思想 的 真正 重视
- ARG0: 教改
- ARG1: 在 教育 的 技术性 层面
- ARGM-ADV: 只
- ARGM-ADV: 不
- rel: 停留

Example 2: *PRO* 来 得 越 多 、 停留 得 越 长
- ARG0: *PRO*
- ARGM-EXT: 越 长
- rel: 停留

Example 3: *OP* 你 曾经 伫足 停留 过 *T*-3 的 美好
- ARG0: 你
- ARG1: *T*-3
- ARGM-ADV: 曾经
- rel: 停留

Example 4: 而且 他们 没有 把 防震 措施 停留 在 文字 上
- ARGM-DIS: 而且
- ARG2: 他们
- ARGM-ADV: 没有
- ARG0: 防震 措施
- ARG1: 在 文字上
- rel: 停留

## 尝试

### 尝试-01

- ARG0: trier
- ARG1: thing tried

Example 1: 为 *PRO* 解决 庞大 资金 需求 ， 公司 正 争取 *PRO* 发行 股票 和 尝试 *OP* *T*-1 更 多 的 融资 渠道 。
- ARG0: *PRO*
- rel: 尝试

Example 2: 「 我们 需要 用 这 特快 程序 以 尽量 减少 任何 *pro* 尝试 *PRO* 利用 香港 作为 *PRO* 规避 联合国 有关 制裁 的 可能 。 」
- ARG0: *pro*
- rel: 尝试

## 追赶

### 追赶-01

- ARG0: agent
- ARG1: entity arg0 chases

Example 1: 日前 ， 哈尔滨 市宾县 摆渡乡 *OP* *T*-1 已 习惯于 “ 冬闲 ” 的 五十万 只 蜜蜂 告别 了 北方 ， 乘 麦道 飞机 南 下 福州市 “ 追赶 花季 ”
- ARG0: 哈尔滨 市宾县 摆渡乡 *OP* *T*-1 已 习惯于 “ 冬闲 ” 的 五十万 只 蜜蜂
- ARG1: 花季
- ARGM-TMP: 日前
- rel: 追赶

### 追赶-02

- ARG0: entity described
- ARG1: entity arg0 catches up with

Example 1: *pro* 怎样 才 能 变 冬闲 *PRO* 为 冬忙 ， 让 蜜蜂 *PRO* 能 追赶 上 花季
- ARG0: *PRO*
- ARG1: 花季
- rel: 追赶

## 美

### 美-01

- ARG0: entity described

Example 1: 词 曲 演唱 皆 美 ， 令 人 *PRO* 泫然欲泣
- ARG0: 词 曲 演唱
- ARGM-ADV: 皆
- rel: 美

## 计划

### 计划-01

- ARG0: planner
- ARG1: thing planned

Example 1: 陕西 计划 *PRO* 加速 发展 旅游业
- ARG0: 陕西
- ARG1: *PRO* 加速 发展 旅游业
- rel: 计划

Example 2: 年赛 计划 *PRO* 每 两 年 举行 一 次 。
- ARG1: 年赛
- ARG1-PRD: *PRO* 每 两 年 举行 一 次
- rel: 计划

## 取消

### 取消-01

- ARG0: agent
- ARG1: theme

Example 1: 有关 部门 还 取消 了 一些 收费 项目 ， 以 降低 住宅 建设 成本 。
- ARG0: 有关 部门
- ARGM-ADV: 还
- rel: 取消

Example 2: 美国 政府 的 对 华 制裁 至今 仍 未 完全 取消
- ARG1: 美国 政府 的 对 华 制裁
- ARGM-ADV: 至今
- ARGM-ADV: 仍
- ARGM-ADV: 未
- ARGM-ADV: 完全
- rel: 取消

## 直到

### 直到-01

- ARG0: agent

Example 1: 

## 乘坐

### 乘坐-01

- ARG0: passenger
- ARG1: means of transportation

Example 1: *OP* 我们 乘坐 *T*-1 的 旅游 大 轿车
- ARG0: 我们
- ARG1: *T*-1
- rel: 乘坐

## 成功

### 成功-01

- ARG0: entity that succeeds

Example 1: 这 一 新 货币 发行 和 使用 是否 成功
- ARG0-PSR: 这 一 新 货币
- ARG0-PSE: 发行 和 使用
- ARGM-ADV: 是否
- rel: 成功

## 围绕

### 围绕-01

- ARG0: entity described
- ARG1: entity arg0 revolves around/centers on

Example 1: 明年 中国 经贸 工作 将 围绕 三 年 改革 与 脱困 来 进行
- ARG0: 中国 经贸 工作
- ARG1: 三 年 改革 与 脱困
- ARGM-ADV: 将
- ARGM-TMP: 明年
- rel: 围绕

## 圈

### 圈-01

- ARG0: agent
- ARG1: theme, entity being circled up or grouped together

Example 1: 
- ARG1: 我
- rel: 圈

### 圈-02

- ARG0: agent
- ARG1: theme, entity whose physical presence is restricted
- ARG2: locative

Example 1: 
- ARG1: 我
- ARG2: 一座 高楼
- rel: 圈

### 圈-03

- ARG0: agent
- ARG1: theme

Example 1: 
- ARG0: 他们
- rel: 圈

## 并

### 并-01

- ARG0: agent
- ARG1: thing merged
- ARG2: something arg1 is merged into
- ARG3: result

Example 1: *OP* *T*-3 被 并 *T*-3 企业
- ARG1: 企业
- rel: 并

## 标志

### 标志-01

- ARG0: signal
- ARG1: significance

Example 1: 庄严 仪式 标志 回归
- ARG0: 庄严 仪式
- rel: 标志

Example 2: 它 标志 着 *OP* 美国 大型 跨国 集团 必纯士 公司 占有 *T*-2 六成 股份 的 厦门 福兰普利 超市 有限 公司 正式 启动 。
- ARG0: 它
- rel: 标志

## 着

### 着-01

- ARG0: agent
- ARG1: things arg0 wear

Example 1: *pro* 最后 着 便装 上台
- ARG0-: *pro*
- rel: 着

### 着-02

- (no roles)

### 着-03

- ARG0: agent
- ARG1: theme

Example 1: *pro* 着 什么 急
- ARG0-: *pro*
- rel: 着

### 着-04

- ARG0: entity described
- ARG1: place arg0 touches

Example 1: 他 整天 说话 不 着 边际
- ARG0: 他
- ARGM-ADV: 整天
- ARG0-PRD: 说话
- ARGM-ADV: 不
- ARG1: 边际
- rel: 着

## 除

### 除-01

- ARG0: agent/cause
- ARG1: entity arg0 removes

Example 1: 但 *pro* 如何 在 *PRO* 除 污 同时 不 伤害 *OP* *T*-1 复杂 多样 的 珊瑚礁 生态
- ARG0: *PRO*
- ARG1: 污
- rel: 除

### 除-02

- ARG0: agent
- ARG1: dividend
- ARG2: divisor

Example 1: 

## 中

### 中-01

- ARG0: entity described
- ARG1: thing arg0 is hit by

Example 1: 但 在 ２９日 的 卫冕战 中 ， 他 在 ２ 分 ５２ 秒钟 的 时间 内 ， 被 *OP* 威拉蓬 击倒 *T*-1 ６ 次 ， 脸 上 中 左刺拳 无数 ， *PRO* 可以 说 是 一败涂地
- ARG0: 他
- ARG1: 左刺拳
- ARG1-QTY: 无数
- ARGM-LOC: 脸 上
- ARGM-TMP: 在 ２ 分 ５２ 秒钟 的 时间 内
- ARGM-LOC: 在 ２９日 的 卫冕战 中
- ARGM-ADV: 但
- rel: 中

### 中-02

- ARG0: entity described
- ARG1: prize, award

Example 1: 只要 您 参加 这 项 活动 ， *pro* 就 有 机会 中 大奖
- ARGM-CND: 只要 您 参加 这 项 活动
- ARG0: *pro*
- ARG1: 大奖
- rel: 中

### 中-03

- ARG0: agent
- ARG1: instrument
- ARG2: target

Example 1: 去年 ４月 美国 一 架 海军 飞机 投弹 不 中 目标
- ARGM-TMP: 去年 ４月
- ARG0: 美国 一 架 海军 飞机
- ARGM-ADV: 不
- ARG1: 目标
- rel: 中

### 中-04

- ARG0: entity described

## 还有

### 还有-01

- ARG0: agent

## 等

### 等-01

- ARG0: party that waits
- ARG1: waiting for

Example 1: 但是 *pro* 现在 还 需要 等 体检 结果
- ARG0: *pro*
- ARG1: 体检 结果
- ARGM-ADV: 还
- rel: 等

Example 2: *pro* 如果 等 情势 完全 明朗
- ARG0: *pro*
- ARG1: 情势 完全 明朗
- rel: 等

Example 3: 宏基 可以 等
- ARG0: 宏基
- rel: 等

### 等-02

- ARG0: entities being equal to each other

Example 1: 彰化 地检署 侦办 *pro* 总统 大选 贿选 案 ， 将 员林 镇长 等 二百多 人 依 *PRO* 违反 选罢法 提起 公诉 ， 分别 求处 三 年 至 二 个 月 *OP* *T*-1 不 等 徒刑
- ARG0: *T*-1
- ARGM-ADV: 不
- rel: 等

## 和

### 和-01

- ARG0: agent
- ARG1: theme

Example 1: 
- ARG1: 音乐
- rel: 和

### 和-02

- ARG0: agent
- ARG1: co-arg0

Example 1: 
- rel: 和

## 实施

### 实施-01

- ARG0: agent
- ARG1: theme

Example 1: 中国 海关 总署 将 实施 对 知识 产权 的 保护 措施
- ARG0: 中国 海关 总署
- ARGM-ADV: 将
- rel: 实施

Example 2: 结售 制度 和 *OP* *T*-2 新 的 核销 制度 在 西藏 全面 实施
- ARG1: 结售 制度 和 *OP* (*T*-2)->(核销制度) 新 的 核销 制度
- ARGM-LOC: 在 西藏
- ARGM-ADV: 全面
- rel: 实施

## 创造

### 创造-01

- ARG0: generator, creator
- ARG1: thing created, generated

Example 1: *OP* 乡镇 企业 创造 *T*-1 的 国民 生产 总值
- ARG0: 乡镇 企业
- ARG1: *T*-1
- rel: 创造

Example 2: 机械 行业 仅 *pro* 推广 *RNR*-1 应用 楔横轧 一 项 技术 ， 创造 直接 经济 效益 四亿多 元
- ARG0: 机械 行业
- ARG0: 仅 *pro* 推广 *RNR*-1 应用 楔横轧 一 项 技术
- ARG1: 直接 经济 效益
- ARG1-PSE: 四亿多 元
- rel: 创造

## 记录

### 记录-01

- ARG0: entity doing recording
- ARG1: thing recorded
- ARG2: instrument
- ARG3: media

Example 1: 机读码 阅读机 自动 识别 证件 并 记录 证件 上 的 有关 资料
- ARG2: 机读码 阅读机
- ARG1: 证件 上 的 有关 资料
- rel: 记录

Example 2: 旨 在 *PRO* 借助 竞赛 的 形式 ， 记录 *RNR*-2 、 保存 *RNR*-2 、 研究 发掘 、 *OP* *T*-1 濒临 消失 的 各 种 民俗
- ARG0: *PRO*
- ARG1: *RNR*-2
- rel: 记录

Example 3: 一 组组 作品 忠实 地 记录 了 世界 各 地 *OP* *T*-1 独特 的 民俗 景观
- ARG3: 一 组组 作品
- ARG1: 世界 各 地 *OP* *T*-1 独特 的 民俗 景观
- ARGM-ADV: 忠实 地
- rel: 记录

## 飞行

### 飞行-01

- ARG0: entity flying

Example 1: 飞机 飞行 中 ， 旅客 必须 全程 关机 ， 以免 影响 飞航 安全
- ARG0: 飞机
- rel: 飞行

## 达

### 达-01

- ARG0: theme
- ARG1: point reached

Example 1: *OP* *pro* 承包 *T*-2 的 工程 达 一百四十一 项
- ARG0: *OP* *pro* 承包 *T*-2 的 工程
- ARG1: 一百四十一 项
- rel: 达

## 修理

### 修理-01

- ARG0: agent
- ARG1: entity arg0 repairs

Example 1: 要是 女儿 这 个 小 「 外国人 」 将来 *PRO* 上学 也 被 修理 ， *pro* 该 如何是好
- ARG1-: 女儿 这 个 小 「 外国人 」
- ARGM-ADV: 也
- ARGM-ADV: *PRO* 上学
- ARGM-TMP: 将来
- ARGM-ADV: 要是
- rel: 修理

### 修理-02

- (no roles)

### 修理-03

- ARG0: agent
- ARG1: entity

Example 1: *pro* “ 修理 老二
- ARG0-: *pro*
- ARG1-: 老二
- rel: 修理

## 达到

### 达到-01

- ARG0: theme
- ARG1: point reached

Example 1: 保税区 的 出口 加工 年 产值 将 达 一百五十亿 元
- ARG0: 保税区 的 出口 加工 年 产值
- ARG1: 一百五十亿 元
- ARGM-ADV: 将

## 左右

### 左右-01

- ARG0: entity described
- ARG1: entity arg0 controls

Example 1: *OP* *T*-2 不同 的 人 当选 将 左右 台湾 未来 的 政党 政治 与 宪政 走向
- ARG0: *OP* *T*-2 不同 的 人 当选
- ARG1: 台湾 未来 的 政党 政治 与 宪政 走向
- ARGM-ADV: 将
- rel: 左右

Example 2: *pro* *PRO* 争取 权益 时 须 六亲不认 ， 不 要 被 *OP* 大陆 亲朋好友 左右 *T*-6
- ARG0: 大陆 亲朋好友
- ARG1: *pro*
- ARGM-ADV: 不
- ARGM-TMP: *PRO* 争取 权益 时
- rel: 左右

## 限于

### 限于-01

- ARG0: theme
- ARG1: range

Example 1: 适用 范围 也 限于 民间
- ARG0: 适用 范围
- ARGM-ADV: 也
- rel: 限于

Example 2: 这 期间 ， *OP* *pro* 新 启用 *T*-1 的 欧元 仍 限于 *PRO* 在 非现金 交易 中 使用 ， 如 银行 记帐 、 支票 、 结算 等 。
- ARG0: *OP* *pro* 新 启用 (*T*-1)->(欧元) 的 欧元
- ARGM-ADV: 仍
- rel: 限于

### 限于-02

- ARG0: thing limited
- ARG1: theme
- ARG2: predicate

Example 1: *OP* *T*-1 仅 限于 主权 国家 *PRO* 参加 的 国际 金融 组织
- ARGM-ADV: 仅
- rel: 限于

## 去

### 去-01

- ARG0: entity going
- ARG1: goal

Example 1: *pro* 可以 用 *OP* *T*-3 更 低廉 的 价格 把 货品 卖到 *OP* *T*-2 以 美元 计价 的 国际 市场 去
- ARG0: 货品
- rel: 去

Example 2: 到时候 我 一定 要 去 现场 看看 这 位 世界 顶级 歌手 的 风采
- ARG0: 我
- ARG1: 现场
- ARGM-ADV: 一定
- ARGM-ADV: 到时候
- rel: 去

### 去-02

- ARG0: 

Example 1: *PRO* 要 寻常人 *PRO* 去 推销 这 类 商品
- rel: 去

Example 2: 我 会 把 吉姆 的 东西 扔出 屋 去
- rel: 去

### 去-03

- ARG0: agent, cause
- ARG1: thing got rid of

Example 1: 
- ARG1: 角质

### 去-04

- ARG0: agent
- ARG1: entity sent, ex. mail
- ARG2: receiver

Example 1: 因为 他 里面 确实 提到 了 一 句 ， 这 种 变异 可能 是 更 容易 从 动物 变异 到 人 ， 那 我们 为此 专门 去 了 一 封 信 给 世界 卫生 组织
- ARGM-PRP: 因为 他 里面 确实提到 了 一 句 ， 这 种 变异 可能 是 更 容易 从 动物 变异 到 人
- ARGM-DIS: 那
- ARGM-ADV: 为此
- ARGM-ADV: 专门
- ARG1: 一 封 信
- rel: 去

## 测试

### 测试-01

- ARG0: agent
- ARG1: entity arg0 tests
- ARG2: instrument

Example 1: 日本 技师 正在 测试 抗风 阻尼器
- ARG0: 日本 技师
- ARG1: 抗风 阻尼器
- ARGM-ADV: 正在
- rel: 测试

Example 2: 一 片 小小 的 生物 晶片 上 ， 可以 布放 数万 个 基因 片段 ， 同时 测试 数万 个 基因 的 表现
- ARG1: 数万 个 基因 的 表现
- ARG2: 一 片 小小 的 生物 晶片 上
- ARGM-ADV: 同时
- rel: 测试

Example 3: 晶宇 正 与 台北 荣总 合作 ， 取得 检体 测试 肠 病毒 晶片 的 准确度
- ARG1: 肠 病毒
- ARG2: 检体
- rel: 测试

Example 4: 人才 会 先 经过 专业 的 心理 谘询 顾问 筛选 ， 以 一 对 一 面谈 方式 测试 个性 ， *PRO* 是否 吻合 该 公司 的 企业 文化 ， 再 推荐 给 客户
- ARG1-PSR: 人才
- ARG1-PSE: 个性
- ARG1-PRD: *PRO* 是否 吻合 该 公司 的 企业 文化
- ARGM-MNR: 以 一 对 一 面谈 方式
- ARGM-ADV: 先
- rel: 测试

Example 5: 晶宇 与 长庚 、 成大 合作 测试 的 初步 结果
- ARG0: 晶宇
- rel: 测试

## 至

### 至-01

- ARG0: entity described
- ARG1: location/time/state arg0 reaches/arrives at
- ARG2: source

Example 1: 目前 厦门港 已 拥有 *PRO* 至 日本 、 新加坡 、 韩国 、 美国 、 地中海 等 五 条 国际 集装箱 运输 干线
- ARG0: *PRO*
- ARG1: 日本 、 新加坡 、 韩国 、 美国 、 地中海 等
- rel: 至

Example 2: *OP* *T*-1 由 教育署 辅导 视学处 美工组 举办 *-2 的 小学生 创作展 *pro* 今日 （ 星期四 ） 起 至 八月 二日 ， 在 北角 百福道 四 号 美工 教育 资源 中心 举行
- ARG0: *pro*
- ARG1: 八月 二日
- rel: 至

Example 3: １９８２年 ８月 １７日 ， 中 美 又 就 *PRO* *PRO* 分 步骤 直 至 *PRO* 最后 彻底 解决 美 售 台 武器 问题 发表 联合 公报
- ARG0: *PRO*
- ARG1: *PRO* 最后 彻底 解决 美 售 台 武器 问题
- ARGM-ADV: 直
- ARGM-ADV: *PRO* 分 步骤
- rel: 至

Example 4: 新春 将 至
- ARG0: 新春
- ARGM-ADV: 将
- rel: 至

Example 5: 一 辆 *OP* *T*-1 由 巢湖 至 蚌埠 的 中巴车
- ARG0: *T*-1
- ARG1: 蚌埠
- ARG2: 由 巢湖
- rel: 至

## 踏上

### 踏上-01

- ARG0: agent
- ARG1: location stepped onto

Example 1: 作为 中国 镍 工业 代表 的 这 家 企业 由 此 踏上 *PRO* 依靠 科技 进步 求 振兴 的 发展 之 路
- ARG0: 作为 中国 镍 工业 代表 的 这 家 企业
- ARG1: *PRO* 依靠 科技 进步 求 振兴 的 发展 之 路
- ARGM-DIR: 由 此
- rel: 踏上

## 下

### 下-01

- ARG0: entity moving
- ARG1: location arg0 moves to

Example 1: 日前 ， 哈尔滨 市宾县 摆渡乡 *OP* *T*-1 已 习惯于 “ 冬闲 ” 的 五十万 只 蜜蜂 告别 了 北方 ， 乘 麦道 飞机 南 下 福州市 “ 追赶 花季 ”
- ARG0: 哈尔滨 市宾县 摆渡乡 *OP* *T*-1 已 习惯于 “ 冬闲 ” 的 五十万 只 蜜蜂
- ARG1: 福州市
- ARGM-ADV: 南
- ARGM-TMP: 日前
- rel: 下

### 下-02

- ARG0: agent
- ARG1: thing(chess)played

Example 1: 以前 他 与 中国 棋手 下 过 九 盘 ， 全 都 获胜
- ARG0: 他
- ARG0: 与 中国 棋手
- ARG1: 九 盘
- ARGM-TMP: 以前
- rel: 下

### 下-03

- ARG0: agent
- ARG1: thing(efforts/decision) made

Example 1: *pro* 必须 紧紧 咬定 一 个 “ 新 ” 字 ， 要 在 知识 创新 、 科技 创新 和 体制 创新 上 下 功夫 ， 真正 搞出 中国 的 创新 体系 来
- ARG0: *pro*
- ARG1: 功夫
- ARGM-LOC: 在 知识 创新 、 科技 创新 和 体制 创新 上
- rel: 下

### 下-04

- ARG0: agent
- ARG1: location arg0 descends from

Example 1: 小 皇帝 孺子婴 由 师傅 搀扶 *-1 ， 下 了 殿
- ARG0: 小 皇帝 孺子婴
- ARG1: 殿
- rel: 下

Example 2: *PRO* 下 了 班
- ARG0: *PRO*
- ARG1: 班
- rel: 下

### 下-05

- ARG0: rain

Example 1: *pro* 现在 正在 下 大 雨
- ARG0: 大 雨
- ARGM-ADV: 正在
- rel: 下

### 下-06

- ARG0: entity described
- ARG1: entity arg0 is inferior to

Example 1: 而 有的 色情 内容 煸情 程度 不 下 限制级 电影
- ARG0-PSR: 有的色情 内容
- ARG0-PSE: 煸情 程度
- ARGM-ADV: 不
- ARG1: 限制级 电影
- rel: 下

### 下-07

- ARG0: agent
- ARG1: order, policy

Example 1: 新 政府 下 这 项 政令
- ARG0: 新 政府
- ARG1: 这 项 政令
- rel: 下

### 下-08

- ARG0: agent
- ARG1: entity uninstalled

Example 1: *OP* *T*-1 下 螺丝 的
- ARG0: *T*-1
- ARG1: 螺丝
- rel: 下

### 下-09

- ARG0: entity lost

Example 1: 这 面子 下 不 来
- ARG0: 这 面子
- rel: 下

### 下-010

- ARG0: agent
- ARG1: ptient

Example 1: 作为 教育 机构 *pro* 在 *OP* *pro* *T*-1 关注 升学率 的 同时 ， 在 孩子 成长 教育 过程 中 更 应 在 “ 知理 ” 上 下 功夫 。
- ARG0: *pro*
- ARGM-DGR: 更
- ARG1: 功夫
- rel: 下

### 下-011

- ARG0: agent
- ARG1: entity arg0 drops

Example 1: 我们 的 飞机 、 军舰 、 导弹 就 是 在 “ 下 饺子 ” 也 忙 不 过来 。
- ARGM-ADV: 就
- ARGM-ADV: 在
- ARG1: 饺子
- rel: 下

### 下-012

- ARG0: agent
- ARG1: entity downloaded from internet

### 下-013

- ARG0: agent
- ARG1: MWE usage, work place

## 过

### 过-01

- ARG0: experiencer
- ARG1: thing experienced

Example 1: 老板们 宁可 放弃 赛季 ， 也 不 肯 *PRO* 在 现存 的 劳工 系统 下 过 日子 。
- ARG0: *PRO*
- ARG1: 日子
- ARGM-LOC: 在 现存 的 劳工 系统 下
- rel: 过

### 过-02

- ARG0: theme
- ARG1: time frame, etc.

Example 1: 其他 四 个 孩子 还 没有 过 危险期
- ARG0: 其他 四 个 孩子
- ARG1: 危险期
- ARGM-ADV: 还
- rel: 过

Example 2: 水灾 过 后
- ARG1: 水灾
- rel: 过

### 过-03

- ARG0: thing expired

Example 1: *OP* *T*-2 未 持有 港 澳 同胞 回乡证 以及 *T*-2 回乡证 有效期 已 过 的 申请人 的 申请
- ARG0-PSR: *T*-2
- ARG0-PSE: 回乡证 有效期
- ARGM-ADV: 已
- rel: 过

### 过-04

- ARG0: entity described
- ARG1: thing arg0 does well in

Example 1: *PRO* 回顾 这 两 项 我 的 最爱 ， *pro* 都 可以 算 *PRO* 过 得 去
- ARG0: *PRO*
- rel: 过

### 过-05

- ARG0: entity described
- ARG1: place arg0 passes by/goes through

Example 1: 船 过 无 痕
- ARG0: 船
- rel: 过

### 过-06

- ARG0: entity described
- ARG1: entity arg0 surpasses

Example 1: 功 过 五 帝
- ARG0: 功
- ARG1: 五 帝
- rel: 过

### 过-07

- ARG0: entity described
- ARG1: test/exam arg0 passes

Example 1: *pro* 更 在 今年 九月 因 环评 未 过 停止 动工 计画
- ARG1: 环评
- ARGM-ADV: 未
- rel: 过

### 过-08

- ARG0: entity described
- ARG1: place arg0 comes over to

Example 1: 好莱坞 过 台湾 —— 大 鱼 吃 小 鱼
- ARG0: 好莱坞
- ARG1: 台湾
- rel: 过

## 批

### 批-01

- ARG0: agent
- ARG1: entity given permission to

Example 1: *OP* 中国 新 批 *T*-1 外商 投资 项目 数 和 合同 金额 比 上 年 同 期 分别 下降 百分之十五点三九 和 百分之三十三点五二
- ARG0: 中国
- ARG1: *T*-1
- ARGM-ADV: 新
- rel: 批

Example 2: 去年 ， 山东省 各 类 经济 开发区 新 批 *OP* *T*-2 利用 外资 项目 一千四百八十多 个 ， 占 全 省 总数 的 百分之二十四 以上
- ARG0: 山东省 各 类 经济 开发区
- ARG1: *OP* *T*-2 利用 外资 项目
- ARG1-QTY: 一千四百八十多 个
- ARGM-ADV: 新
- ARGM-TMP: 去年
- rel: 批

### 批-02

- ARG0: 

### 批-03

- ARG0: agent
- ARG1: entity criticized

Example 1: *pro* 批 邓
- ARG0: *pro*
- ARG1: 邓
- rel: 批

### 批-04

- ARG0: buyer
- ARG1: wholesaler

Example 1: *pro* 图书 城 去 批
- ARG0: *pro*
- rel: 批

## 哺乳

### 哺乳-01

- ARG0: agent
- ARG1: theme

Example 1: 
- ARG0: 不少 新 妈咪
- ARG1: 宝宝
- rel: 哺乳

## 随着 (found as 随)

### 随-01

- ARG0: follower
- ARG1: people followed

Example 1: *OP* *T*-1 这 次 随 我 来访 的 有 一 批 企业家
- ARG0: *T*-1
- ARG1: 我
- ARGM-ADV: 这 次
- rel: 随

### 随-02

- ARG0: thing described
- ARG1: entity arg0 is decided on by
- ARG2: agent

Example 1: 我 愿意 *PRO* 把 他 揉成 团 ， 装 在 口袋 里 ， *pro* 随 我
- ARG0: *pro*
- ARG1: 我
- ARGM-CND: 我 愿意 *PRO* 把 他 揉成 团 ， 装 在 口袋 里
- rel: 随

Example 2: 我 随 你 说 什么
- ARG2: 我
- ARG0: 你
- rel: 随

## 及

### 及-01

- ARG0: thing compared
- ARG1: thing compared with

Example 1: 虽然 四十 年 的 航天 投资 总额 还 不 及 前 苏联 、 美国 一 年 的 航天 投资 。
- ARG0: 四十 年 的 航天 投资 总额
- ARG1: 前 苏联 、 美国 一 年 的 航天 投资
- ARGM-ADV: 还
- ARGM-ADV: 不
- rel: 及

### 及-02

- ARG0: theme
- ARG1: place arg0 reached

Example 1: *PRO* 才 过 民权 大桥 或 麦帅 二 桥 ， *OP* 视线 所 及 *T*-1 就 是 *OP* *T*-6 招牌 高 挂 醒目 的 量贩 店 错落 其中
- ARG0: 视线
- ARG1: *T*-1
- rel: 及

## 公用

### 公用-01

- ARG0: agent

## 走入

### 走入-01

- ARG0: entity described
- ARG1: location arg0 gets into

Example 1: 调改会 成立 ， 政治 侦防 走入 历史
- ARG0: 政治 侦防
- ARG1: 历史
- rel: 走入

## 开始

### 开始-01

- ARG0: entity described
- ARG1: thing started

Example 1: 目前 ， 王翔 又 开始 了 九龙街 的 建设 。
- ARG0: 王翔
- ARG1: 九龙街 的 建设
- ARGM-ADV: 又
- ARGM-TMP: 目前
- rel: 开始

Example 2: 德国 统一 后 ， 原 驻德 苏军 *PRO* 从 １９９１年 开始 分批 撤离 。
- ARG1: *PRO*
- ARGM-TMP: 从 １９９１年
- rel: 开始

Example 3: 活动 将 于 元旦 上午 十时三十分 开始
- ARG1: 活动
- ARGM-TMP: 于 元旦 上午 十时三十分
- ARGM-ADV: 将
- rel: 开始

### 开始-02

- ARG0: entity started

Example 1: 二零零五年 的 夏天 ， 一 个 *OP* *T*-1 被 人们 期待 *T*-2 已 久 的 画面 开始 在 香港 的 各 大 媒体 频繁 出现
- ARGM-TMP: 二零零五年 的 夏天
- ARG0: 一 个 被 人们 期待 已 久 的 画面
- ARG0-PRD: 在 香港 的 各 大 媒体 频繁 出现
- rel: 开始

## 迈向

### 迈向-01

- ARG0: entity described
- ARG1: goal

Example 1: 开发区 建设 已 由 土地 开发 迈向 工业 项目 建设 的 新 阶段
- ARG0: 开发区 建设
- ARG1: 工业 项目 建设 的 新 阶段
- ARGM-DIR: 由 土地 开发
- ARGM-ADV: 已
- rel: 迈向

## 商业化

### 商业化-01

- ARG0: agent/cause
- ARG1: entity commercialized

Example 1: 国有 银行 商业化 进程 有待 进一步 加快
- ARG1: 国有 银行
- rel: 商业化

## 使

### 使-01

- ARG0: cause
- ARG1: theme
- ARG2: predicate

Example 1: *OP* *T*-1 良好 的 投资 环境 使 外商 在 沪 投资 的 成功率 *PRO* 达到 百分之八十 。
- ARG0-: *OP* (*T*-1)->(投资环境) 良好 的 投资 环境
- rel: 使

### 使-02

- (no roles)

### 使-03

- ARG0: agent
- ARG1: entity used by arg0

Example 1: 这样 *pro* 真的 是 把 *OP* *pro* *T*-1 当官 的 最高 境界 都 给 使 出来 *-2
- ARGM-DIS: 这样
- ARG0-: *pro*
- ARGM-ADV: 真的
- ARGM-ADV: 都
- rel: 使

## 包括

### 包括-01

- ARG0: thing including
- ARG1: thing included
- ARG2: agent

Example 1: 承保 范围 包括 财产 、 责任 、 信用 、 人身 四 大 类 主 、 副 六十多 个 险种
- ARG0: 承保 范围
- rel: 包括

Example 2: *pro* 包括 *pro* 在 用地 上 给予 *OP* *T*-1 较 低 的 地价 ， 在 税收 上 给予 减免 等 。
- ARG0: *pro*
- rel: 包括

Example 3: *pro* 包括 *pro* 在 用地 上 给予 *OP* *T*-1 较 低 的 地价 ， 在 税收 上 给予 减免 等 。
- ARG0: *pro*
- rel: 包括

Example 4: *OP* *T*-1 超过 １／３ 的 高中 将 在 第二 阶段 时 中考 包括 语文 能力 等 项目 的 纸笔 测验
- ARG2: 超过 １／３ 的 高中
- rel: 包括

## 现实

### 现实-01

- ARG0: entity described

Example 1: 这些 论调 是 *OP* “ *T*-1 不 现实 的 ”
- ARG0: *T*-1
- ARGM-ADV: 不
- rel: 现实
