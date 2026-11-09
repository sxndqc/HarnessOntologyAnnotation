# PropBank entries for the words of chinese_umr-0030

From ai-native-annotator.github.io data/skillparse/resources/propbank/zh.json: every roleset of every word of the document that PropBank has.

## 据

### 据-01

- ARG0: entity described
- ARG1: thing arg0 occupies/owns

Example 1: 三 强 各 据 一 方
- ARG0: 三 强
- ARG1: 一 方
- ARGM-ADV: 各
- rel: 据

### 据-02

- ARG0: agent
- ARG1: thing arg0 uses as basis

Example 1: 陈水扁 总统 如何 据 *pro* 以 作为 两 岸 政策 的 参考 ， 实在 令 人 *PRO* 怀疑
- ARG0: 陈水扁 总统
- ARG1: *pro*
- ARGM-ADV: 如何
- rel: 据

### 据-03

- ARG0: agent
- ARG1: thing arg0 owns

Example 1: *T*-1 各 据 特色
- ARG0: *T*
- ARG1: 特色
- rel: 据

## 报道

### 报道-01

- ARG0: reporter
- ARG1: thing reported

Example 1: 眼下 ， 西班牙 大众 传媒 每 天 都 在 连篇累牍 地 报道 欧元 及 其 相关 情况
- ARGM-ADV: 眼下
- ARG0: 西班牙 大众 传媒
- ARGM-TMP: 每 天
- ARGM-ADV: 都
- ARGM-ADV: 在
- ARGM-ADV: 连篇累牍 地
- rel: 报道

Example 2: 媒介 报道 ， 沿海 地区 仅 苏 、 浙 、 沪 三 地 国际 集装箱 码头 已 达到 二十多 个 。
- ARG0: 媒介
- rel: 报道

## 服务

### 服务-01

- ARG0: service provider
- ARG1: party receiving service

Example 1: *OP* *T*-1 服务 三峡 工程 的 专业 机构
- ARG0: *T*-1
- ARG1: 三峡 工程
- rel: 服务

Example 2: 天津市 *OP* *T*-1 专门 为 台商 服务 的 主要 官员
- ARG0: *T*-1
- ARG1: 为 台商
- ARGM-ADV: 专门
- rel: 服务

## 故障

### 故障-01

- ARG0: thing which malfunctions

Example 1: 百分之二十 则 因为 设备 故障
- ARG0: 设备
- rel: 故障

## 出

### 出-01

- ARG0: entity going out
- ARG1: going out of

Example 1: 随着 崇明 海关 办事处 的 设立 ， 崇明县 内 的 单位 足 不 出 岛 就 可以 办理 一切 海关 手续
- ARG0-: 足
- ARG1-: 岛
- ARGM-ADV: 不
- rel: 出

Example 2: *OP* *T*-4 大 进 大 出 的 加工业
- ARG0-: *T*-4
- ARGM-ADV: 大
- rel: 出

Example 3: *pro* 真是 出 我 *PRO* 不 意 ， 攻 我 *PRO* 不 备
- ARG0-: *pro*
- ARG1-: 我
- ARG1-PRD: *PRO* 不 意
- ARGM-ADV: 真是
- rel: 出

Example 4: 美浓 的 *PRO* 反 水库 运动 ， 不仅 让 客家 妇女 *PRO* 出 了 头
- ARG0-PSR: *PRO*
- ARG0-PSE: 头
- rel: 出

Example 5: *OP* 日本 新力 出产 *T*-1 的 机器 狗 「 爱宝 」 ， 在 台北 国际 资讯展 中 大 出 锋头
- ARG0-PSR: *OP* 日本 新力 出产 *T*-1 的 机器 狗 「 爱宝 」
- ARG0-PSE: 锋头
- ARGM-ADV: 大
- ARGM-LOC: 在 台北 国际 资讯展 中
- rel: 出

### 出-02

- ARG0: agent
- ARG1: thing given
- ARG2: beneficiary

Example 1: *OP* *T*-1 第二 个 出生 的 女婴 不断 给 医生们 出 难题
- ARG0-: *OP* *T*-1 第二 个 出生 的 女婴
- ARG1-: 难题
- ARG2-: 给 医生们
- ARGM-ADV: 不断
- rel: 出

Example 2: 一九九三年 李安 以 《 喜宴 》 赢得 柏林 影展 金 熊 奖 ， 一九九四年 与 一九九七年 蔡明亮 以 《 爱情 万 岁 》 与 《 河流 》 分别 获得 威尼斯 的 金 狮 奖 及 柏林 的 银 熊 奖 ， 为 *OP* *T*-1 低迷 的 本土 电影 工业 出 了 一 口 气
- ARG0-: 一九九三年 李安 以 《 喜宴 》 赢得 柏林 影展 金 熊 奖 ， 一九九四年 与 一九九七年 蔡明亮 以 《 爱情 万 岁 》 与 《 河流 》 分别 获得 威尼斯 的 金 狮 奖 及 柏林 的 银 熊 奖
- ARG1-: 一 口 气
- ARG2-: 为 *OP* *T*-1 低迷 的 本土 电影 工业
- rel: 出

### 出-03

- ARG0: publisher, writer
- ARG1: work, policy

Example 1: “ 这 几 年 有关 证券 的 法规 、 政策 出 了 不少
- ARG1-: 有关 证券 的 法规 、 政策
- ARGM-TMP: 这 几 年
- ARGM-EXT: 不少
- rel: 出

### 出-04

- ARG0: location
- ARG1: theme

Example 1: 农村 政策 和 工作 指导 上 出 了 问题
- ARG0-: 农村 政策 和 工作 指导 上
- ARG1-: 问题
- rel: 出

### 出-05

- ARG0: theme
- ARG1: bound exceeded by arg0

Example 1: 仅 由 邢台 到 内丘 六十 里 的 铁路 ， *pro* 不 出 几 天 就 被 剥光 *-1
- ARG0-: *pro*
- ARGM-ADV: 不
- ARG1-: 几 天
- rel: 出

### 出-06

- ARG0: agent
- ARG1: task

Example 1: 我 给 你 免费 出 了 一 趟 诊
- ARG0-: 我
- ARGM-BNF: 给 你
- ARGM-ADV: 免费
- ARG1-: 一 趟诊
- rel: 出

### 出-07

- (no roles)

## 表示

### 表示-01

- ARG0: agent
- ARG1: message expressed
- ARG2: party receiving the message
- ARG3: topic of message

Example 1: 香港 特区 行政 长官 董建华 今天 对 *OP* 美国 传统 基金会 发表 *T*-1 的 《 一九九八年 经济 自由 指数 报告 》 表示 欢迎
- ARG0: 香港 特区 行政 长官 董建华
- ARGM-TMP: 今天
- ARG3: 对 *OP* 美国 传统 基金会 发表 (*T*-1)->(《一九九八年经济自由指数报告》) 的 《 一九九八年 经济 自由 指数 报告 》
- rel: 表示

Example 2: 拉美 一体化 协会 常设 政治 机构 “ 代表 委员会 ” 对 中国 *OP* *T*-1 常 驻 该 协会 观察员 、 中国 *OP* *T*-2 驻 乌拉圭 大使 谢汝茂 表示 欢迎 。
- ARG0: 拉美 一体化 协会 常设 政治 机构 “ 代表 委员会 ”
- ARG2: 对 中国 *OP* (*T*-1)->(观察员) 常 驻 该 协会 观察员 、 中国 *OP* (*T*-2)->(大使) 驻 乌拉圭 大使 谢汝茂
- rel: 表示

Example 3: 电力 工业部 国际 合作司 司长 谭艾幸 今天 就 此 事 对 新华社 记者 表示 ， 这 个 电厂 如果 *pro* 成功 的话 ， 将 作为 *OP* *pro* 沿海 地区 *T*-1 建设 同 类 电厂 的 样板 。
- ARG0: 电力 工业部 国际 合作司 司长 谭艾幸
- ARGM-TMP: 今天
- ARG3: 就 此 事
- ARG2: 对 新华社 记者
- rel: 表示

Example 4: 传统 基金会 表示 ， 该 指数 也 有 被 投资者 用作 投资 指南 。
- ARG0: 传统 基金会
- ARG1: 该 指数 也 有 被 投资者 用作 投资 指南
- rel: 表示

### 表示-02

- ARG0: thing described
- ARG1: thing arg0 means/shows

Example 1: 这 表示 大部份 人 都 不 以 *PRO* 大学 毕业 为 满足 ， 还 想 *PRO* 在 知识 的 领域 中 更上一层楼
- ARG0: 这
- ARG1: 大部份 人 都 不 以 *PRO* 大学 毕业 为 满足 ， 还 想 *PRO* 在 知识 的 领域 中 更上一层楼
- rel: 表示

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

## 为

### 为-01

- ARG0: entity being predicated
- ARG1: predicative

Example 1: 乡镇 企业 贷款 增幅 为 百分之六十一点八三
- ARG0: 乡镇 企业 贷款 增幅
- ARG1: 百分之六十一点八三
- rel: 为

Example 2: 图 为 １２日 李鹏 总理 在 马六甲州 参观
- ARG0: 图
- ARG1: １２日 李鹏 总理 在 马六甲州 参观
- rel: 为

### 为-02

- ARG0: a role of arg0
- ARG1: entity playing the role of arg1

Example 1: *OP* *T*-2 以 澳大利亚 国际 发展局 援助局 总局长 弗拉德 为 团长 的 澳大利亚 代表团
- ARG1: 团长
- ARG0: 以 澳大利亚 国际 发展局 援助局 总局长 弗拉德
- rel: 为

Example 2: *pro* 在 *OP* *pro* 与 中国 缔结 *T*-2 友好 城市 中 ， 以 日本 为 最 多
- ARG0: *pro*
- ARG1: 最 多
- ARG2: 以 日本
- ARGM-LOC: 在 *OP* *pro* 与 中国 缔结 *T*-2 友好 城市 中
- rel: 为

### 为-03

- ARG0: entity being predicated
- ARG1: predicate

Example 1: 巴格瓦特 是 *OP* *T*-1 １９９６年 ９月 被 任命 为 印度 海军 参谋长 的
- ARG0: *T*-1
- ARG1: 印度 海军 参谋长
- ARGM-TMP: １９９６年 ９月
- rel: 为

### 为-04

- ARG0: agent/doer
- ARG1: thing done

Example 1: *PRO* “ 有 所 为 ， 有 所 不 为 ” 的 原则
- ARG0: *PRO*
- rel: 为

### 为-05

- ARG0: agent/doer
- ARG1: reason/purpose

Example 1: 我们 学 电影 ， 嗯 ， 写 东西 是 为 什么
- ARG0: 我们 学 电影 ， 写 东西
- ARG1: 什么
- rel: 为

## 备

### 备-01

- ARG0: entity described
- ARG1: thing arg0 is prepared for

Example 1: *pro* 真是 出 我 *PRO* 不 意 ， 攻 我 *PRO* 不 备
- ARG0: *PRO*
- ARGM-ADV: 不
- rel: 备

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

## 应

### 应-01

- ARG0: agent
- ARG1: thing arg0 responds to

Example 1: 日本 还 应 中国 有关 部门 之 邀 ， 对 中国 长春 至 珲春 的 铁路 沿线 地区 综合 开发 进行 调查
- ARG0: 日本
- ARG1: 中国 有关 部门 之 邀
- ARGM-ADV: 还
- rel: 应

### 应-02

- ARG0: 

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

## 非

### 非-01

- ARG0: entity described
- ARG1: entity arg0 is not

Example 1: 英 一 记者 说 所 炸 绝 非 军事 目标
- ARG0-: 所 炸
- ARG1-: 军事 目标
- ARGM-ADV: 绝
- rel: 非

### 非-02

- (no roles)

## 按

### 按-01

- ARG0: agent
- ARG1: entity arg0 holds down

Example 1: 散文 名 作家 潘人木 则 再 也 按 不 住 情绪 说 ： *PRO* 看 《 涨潮日 》 我 眼镜 都 哭掉 了 ！ 因为 他 把 我们 早年 的 愁苦 、 困顿 都 写 出来 了 *-1
- ARG0: 散文 名 作家 潘人木
- ARG1: 情绪
- ARGM-ADV: 也
- ARGM-ADV: 再
- ARGM-ADV: 则
- rel: 按

### 按-02

- ARG0: agent
- ARG1: rule/standard

Example 1: 

## 规定

### 规定-01

- ARG0: law, authority
- ARG1: thing specified

Example 1: 法律 详细 规定 了 证券 发行 的 核准 、 审批 程序
- ARG0: 法律
- ARG1: 证券 发行 的 核准 、 审批 程序
- ARGM-ADV: 详细
- rel: 规定

Example 2: 现行 的 《 森林法 》 规定 ， 林地 的 所有权 和 使用权 证书 由 县级 以上 地方 人民 政府 核发 *-1 。
- ARG0: 现行 的 《 森林法 》
- ARG1: 林地 的 所有权 和 使用权 证书 由 县级 以上 地方 人民 政府 核发 *-1
- rel: 规定

## 能

### 能-01

- ARG0: 

### 能-02

- ARG0: entity described

Example 1: *OP* *T*-3 「 小 而 能 」 政府
- ARG0: *T*-3
- rel: 能

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

## 经营

### 经营-01

- ARG0: agent
- ARG1: patient

Example 1: 深圳 高速 公路 股份 有限 公司 曾 开发 经营 国内 第一 条 合资 公路 －－ 梅观 高速 公路
- ARG0: 深圳 高速 公路 股份 有限 公司
- ARG1: 国内 第一 条 合资 公路 －－ 梅观 高速 公路
- ARGM-ADV: 曾
- rel: 经营

Example 2: 他们 村 实行 土地 股份制 后 ， 土地 由 村里 统一 经营 *-2
- ARG0: 由 村里
- ARG1: *-2
- ARGM-ADV: 统一
- ARGM-TMP: 他们 村 实行 土地 股份制 后
- rel: 经营

Example 3: *PRO* 逐步 成为 *OP* *T*-1 自主 经营 、 自 负 盈亏 的 市场 经济 主体
- ARG0: *T*-1
- ARGM-ADV: 自主
- rel: 经营

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

## 售票

### 售票-01

- ARG0: agent
- ARG1: receipient

Example 1: 
- ARG1: 球迷
- rel: 售票

Example 2: 
- rel: 售票

## 有关

### 有关-01

- ARG0: entity described
- ARG1: entity arg0 is relevant to

Example 1: *PRO* 由 *OP* *T*-1 直接 有关 的 各 方 通过 对话 来 解决 问题
- ARG0: *T*-1
- ARGM-ADV: 直接
- rel: 有关

Example 2: *pro* 举行 *OP* *T*-2 与 香港 有关 的 问题 磋商
- ARG0: *T*-2
- ARG1: 与 香港
- rel: 有关

## 建议

### 建议-01

- ARG0: proposer
- ARG1: proposal
- ARG2: proposing to

Example 1: 二 、 海协 一贯 主张 *pro* 全面 落实 *OP* *pro* 《 汪 辜 会谈 共同 协议 》 中 规定 *T*-1 的 事务性 和 经济 、 科技 议题 商谈 ， 多 次 向 海基会 建议 *pro* 及早 开始 “ 台商 在 大陆 投资 权益 及 相关 问题 ” 的 商谈 。
- ARG0: 海协
- ARG1: *pro* 及早 开始 “ 台商 在 大陆 投资 权益 及 相关 问题 ” 的 商谈
- ARG2: 向 海基会
- ARGM-ADV: 多 次
- rel: 建议

Example 2: ” 田中真纪子 还 建议 宇宙 开发 事业团 成立 一 个 检查 小组 ， 彻底 查明 *OP* 卫星 *T*-1 进 不 了 同步 轨道 的 原因 。
- ARG0: 田中真纪子
- ARG1: 宇宙 开发 事业团 成立 一 个 检查 小组 ， 彻底 查明 *OP* 卫星 *T*-1 进 不 了 同步 轨道 的 原因
- ARGM-ADV: 还
- rel: 建议

Example 3: 央行 还 作好 了 *PRO* 随时 向 欧洲 中央 银行 通报 和 建议 的 准备 ， 以便 纠正 *OP* *T*-1 可能 出现 的 毛病 。
- ARG0: *PRO*
- ARG2: 向 欧洲 中央 银行
- ARGM-ADV: 随时
- rel: 建议

## 尽快

### 尽快-01

- ARG0: entity described

## 完善

### 完善-01

- ARG0: agent
- ARG1: theme

Example 1: *pro* 要 总结 经验 ， 完善 政策 ， 妥善 安置 库区 移民 ， 改善 库区 生态 环境
- ARG0: *pro*
- rel: 完善

Example 2: 其它 设施 也 日趋 完善
- ARG1: 其它 设施
- ARGM-ADV: 也
- ARGM-ADV: 日趋
- rel: 完善

## 作为

### 作为-01

- ARG0: agent
- ARG1: entity arg0 uses
- ARG2: entity arg1 is used as

Example 1: 此 次 活动 在 广州 赛马会 举行 起步 仪式 ， 它 将 揭开 一九九九 中国 （ 广州 ） 生态 环境 游 活动 的 序幕 ， 同时 也 作为 广州市 迎接 澳门 *PRO* 回归 祖国 系列 活动 中 的 首 项 活动
- ARG1-: 它
- ARG2-: 广州市 迎接 澳门 *PRO* 回归 祖国 系列 活动 中 的 首 项 活动
- ARGM-ADV: 也
- ARGM-ADV: 同时
- rel: 作为

Example 2: 他 正好 以 此 作为 *OP* *pro* *T*-1 庆祝 他 ２０ 岁 生日 的 贺礼
- ARG0-: 他
- ARG1-: 以 此
- ARG2-: *OP* *pro* *T*-1 庆祝 他 ２０ 岁 生日 的 贺礼
- ARGM-ADV: 正好
- rel: 作为

Example 3: 美方 仅 将 此 作为 一 个 *OP* *pro* *T*-1 观察 中国 市场 的 小小 窗口
- ARG0-: 美方
- ARG1-: 此
- ARG2-: 一 个 *OP* *pro* *T*-1 观察 中国 市场 的 小小 窗口
- ARGM-ADV: 仅
- rel: 作为

Example 4: 初级 产品 作为 主力 出口 产品 的 局面 有 了 改观
- ARG1-: 初级 产品
- ARG2-: 主力 出口 产品
- rel: 作为

Example 5: 以色列 和 约旦 决定 *PRO* 开通 两 国 共同 边界 北段 的 侯赛因 大 桥 作为 两 国 间 第二 个 边界 口岸
- ARG0-: *PRO*
- ARG2-: 两 国 间 第二 个 边界 口岸
- rel: 作为

Example 6: 「 我们 需要 用 这 特快 程序 以 尽量 减少 任何 *pro* 尝试 *PRO* 利用 香港 作为 *PRO* 规避 联合国 有关 制裁 的 可能
- ARG0-: *PRO*
- ARG2-: *PRO* 规避 联合国 有关 制裁
- rel: 作为

### 作为-02

- ARG0: entity described
- ARG1: entity arg0 serves/functions as
- ARG2: entity of which arg1 is a function

Example 1: *pro* 由 日本 野村 证券 株式会社 和 日本 兴业 银行 证券 株式会社 作为 联合 主干事
- ARG0-: 由 日本 野村 证券 株式会社 和 日本 兴业 银行 证券 株式会社
- ARG1-: 联合 主干事
- ARG2-: *pro*
- rel: 作为

Example 2: 这 项 工程 是 *OP* 国家 计委 确定 *T*-1 的 全 国 重点 项目 投资 体制 改革 试点 ， *PRO* 于 一九九四年 底 动工 后 ， 在 河南省 重点 项目 中 率先 改变 了 非基础性 建设 依赖 政府 投资 的 模式 ， 由 神马 集团 作为 投资 主体 实行 “ 一 条 龙 ” 负责
- ARG0-: 由 神马 集团
- ARG1-: 投资 主体
- ARG2-: 这 项 工程
- rel: 作为

Example 3: *OP* *T*-1 原来 作为 世界 政治 大 国 的 英国 和 法国
- ARG0-: *T*-1
- ARG1-: 世界 政治 大 国
- ARGM-ADV: 原来
- rel: 作为

### 作为-03

- ARG0: entity described
- ARG1: entity arg0 considers
- ARG2: entity arg1 is considered as

Example 1: 此外 ， *pro* 将 *OP* 目前 银行 *T*-1 披露 资料 的 指引 ， 纳入 条例 内 作为 法定 权力
- ARG0-: *pro*
- ARG1-: *OP* 目前 银行 *T*-1 披露 资料 的 指引
- ARG2-: 法定 权力
- ARGM-ADV: 此外
- rel: 作为

### 作为-04

- (no roles)

### 作为-05

- ARG0: agent

Example 1: 我们 既 要 理性 看待 ， 也 要 有所 作为
- rel: 作为

## 设置

### 设置-01

- ARG0: agent
- ARG1: thing set up
- ARG2: location

Example 1: 海湾 战争 结束 后 ， 美 、 英 仍 在 伊拉克 南部 和 北部 设置 禁飞区
- ARG0: 美 、 英
- ARG1: 禁飞区
- ARG2: 在 伊拉克 南部 和 北部
- ARGM-ADV: 仍
- ARGM-TMP: 海湾 战争 结束 后
- rel: 设置

Example 2: 新疆 建设 兵团 设置 法院 和 检察院
- ARG0: 新疆 建设 兵团
- ARG1: 法院 和 检察院
- rel: 设置

## 可能

### 可能-01

- ARG0: thing possible

Example 1: 并 非 *OP* *T*-2 不 可能 的 事
- ARG0: *T*-2
- ARGM-ADV: 不
- rel: 可能

### 可能-02

- ARG0: 

Example 1: 平壤 可能 推行 改革 开放 政策
- rel: 可能

## 搞

### 搞-01

- ARG0: agent
- ARG1: theme

Example 1: *PRO* 搞 市场 经济 以来 的 这 几 年
- ARG0: *PRO*
- ARG1: 市场 经济
- rel: 搞

### 搞-02

- ARG0: person described
- ARG1: thing arg0 cannot figure out

Example 1: 但 他 一 句 *OP* *pro* *PRO* 忘情 喊出 *T*-1 的 「 台湾 主权 独立 万万 岁 」 ， 却 让 人 *PRO* 搞 不 清楚 *PRO* 该 相信 哪 一 个 阿扁
- ARG0: *PRO*
- ARG1: *PRO* 该 相信 哪 一 个 阿扁
- rel: 搞

### 搞-03

- ARG0: agent
- ARG1: entity arg0 obtains

Example 1: 「 *pro* 能 搞 得 到 食 ？ 」 是 *OP* *T*-1 普遍 的 怀疑
- ARG0: *pro*
- ARG1: 食
- rel: 搞

### 搞-04

- ARG0: agent
- ARG1: entity arg0 figures out

Example 1: 直 到 那 一 天 ， 我 才 搞 清楚 自己 是 中国人 ， 不 是 日本人
- ARGM-TMP: 直 到 那 一 天
- ARG0: 我
- ARGM-ADV: 才
- ARG1: 自己 是 中国人 ， 不 是日本人
- rel: 搞

### 搞-05

- ARG0: agent
- ARG1: theme
- ARG2: result

Example 1: *OP* *T*-1 缺乏 公德心 的 市民 却 把 台北 街头 搞 成 这 副 德性
- ARG0: 缺乏 公德心 的 市民
- ARGM-DIS: 却
- ARG1: 台北 街头
- ARG2: 这 副 德性
- rel: 搞

## 要

### 要-01

- ARG0: asker
- ARG1: thing asked for
- ARG2: party asked from

Example 1: 内地 不 会 向 香港 伸手 要 一 分 钱
- ARG0: 内地
- ARG2: 向 香港
- rel: 要

Example 2: 各 国 人民 要 和平 、 求 发展
- ARG0: 各 国 人民
- rel: 要

### 要-02

- ARG0: theme
- ARG1: cost,time
- ARG2: predicate

Example 1: *OP* *T*-2 原来 要 二 *RNR*-1 至 三 天 办 完 的 出入境 手续
- ARG0: *T*-2
- ARGM-ADV: 原来
- rel: 要

Example 2: 原先 成本 要 二千多 盾
- ARG0: 成本
- ARG1: 二千多 盾
- ARGM-ADV: 原先
- rel: 要

### 要-03

- ARG0: 

Example 1: *OP* *T*-3 将 要 负起 重任 的 文官 团队 接棒 太 晚
- rel: 要

### 要-04

- ARG0: wanter
- ARG1: doer
- ARG2: predicate

Example 1: *PRO* 要 寻常人 *PRO* 去 推销 这 类 商品
- ARG0: *PRO*
- rel: 要

Example 2: *PRO* 如 要 *pro* *PRO* 送货 上门
- ARG0: *PRO*
- ARGM-ADV: 如
- rel: 要

### 要-05

- ARG0: intender
- ARG1: thing intended

Example 1: *OP* 台湾 媒体 处心积虑 要 采访 *T*-2 的 区文龙 司长
- ARGM-MNR: 处心积虑
- ARG1: 采访
- rel: 要

### 要-06

- ARG0: predicate, condition

Example 1: 那么 他 要 *PRO* 想 *PRO* 亚洲 发展
- ARGM-DIS: 那么
- ARG0: 他 想 亚洲 发展
- rel: 要

## 知道

### 知道-01

- ARG0: people described
- ARG1: entity arg0 knows

Example 1: 我 清楚 地 知道 香港人 的 需要 和 期望
- ARG0: 我
- ARG1: 香港人 的 需要 和 期望
- ARGM-ADV: 清楚 地
- rel: 知道

Example 2: 那时 谁 也 不 知道 韩国 即将 卷入 金融 风暴
- ARG0: 谁
- ARG1: 韩国 即将 卷入 金融 风暴
- ARGM-ADV: 不
- ARGM-ADV: 也
- ARGM-TMP: 那时
- rel: 知道

## 一

### 一-01

- ARG0: entity described

Example 1: *pro* 有 此 之 名 典故 不 一
- ARG0-PSR: *pro* 有 此 之 名
- ARG0-PSE: 典故
- ARGM-ADV: 不
- rel: 一

## 开放

### 开放-01

- ARG0: agent
- ARG1: area opened
- ARG2: to whom

Example 1: 加之 中国 在 浦东 率先 对 外资 开放 外贸 领域 ， 成立 了 三 家 中外 合资 贸易 公司
- ARG0: 中国
- ARGM-LOC: 在 浦东
- ARGM-ADV: 率先
- ARG2: 对 外资
- rel: 开放

Example 2: 缅甸 政府 于 昨天 和 今天 重新 开放 了 *OP* *T*-1 去年 关闭 的 缅 泰 边境 地区 的 ３ 个 主要 通商 口岸 。
- ARG0: 缅甸 政府
- ARGM-TMP: 于 昨天 和 今天
- ARGM-ADV: 重新
- rel: 开放

Example 3: 沿海 、 沿边 、 沿江 进一步 开放
- ARGM-ADV: 进一步
- rel: 开放

### 开放-02

- ARG0: agent
- ARG1: theme
- ARG2: predicate

Example 1: 目前 为止 ， 中国 只 开放 了 五 个 经济 特区 和 北京 、 上海 、 天津 等 六 个 城市 *PRO* 作为 试点 。
- ARG0: 中国
- ARGM-ADV: 只
- rel: 开放

Example 2: 台湾 当局 应 尽快 开放 *PRO* 采认 祖国 大陆 学历 ， 维护 广大 学子 的 利益 。
- ARG0: 台湾 当局
- ARGM-ADV: 尽快
- rel: 开放

### 开放-03

- ARG0: theme

Example 1: *OP* *T*-1 更加 开放 的 政策
- ARGM-ADV: 更加
- rel: 开放

### 开放-04

- ARG0: flower, etc. that blossoms

Example 1: 据 观察 ， 不少 公园 的 桂花 现在 也 已经 结出 花蕾 ， 不日 也 将 开放 。
- ARG0: 不少 公园 的 桂花
- ARGM-ADV: 据 观察
- ARGM-TMP: 不日
- ARGM-ADV: 也
- ARGM-ADV: 将
- rel: 开放

## 必然

### 必然-01

- ARG0: thing described

Example 1: 宋楚瑜 若 当选 ， 其 支持 势力 组党 几乎 被 认为 是 *OP* *T*-1 必然 的
- ARG0: *T*-1
- rel: 必然

## 承受

### 承受-01

- ARG0: endurer, bearer
- ARG1: pain, disease, or burden

Example 1: *OP* *T*-2 昂贵 的 干扰素 大多数 患者 难以 承受 *T*-3
- ARG0: 大多数 患者
- ARG1: *T*-3
- ARGM-ADV: 难以
- rel: 承受

## 巨大

### 巨大-01

- ARG0: thing described

Example 1: 中 日 经贸 合作 潜力 巨大
- ARG0-PSE: 潜力
- ARG0-PSR: 中 日 经贸 合作
- rel: 巨大

## 具备

### 具备-01

- ARG0: entity described
- ARG1: thing arg0 is in possession of

Example 1: 码头 已 具备 各 种 杂货 、 散货 、 滚装 货物 、 集装箱 、 石化 产品 装卸 功能
- ARG0: 码头
- ARG1: 各 种 杂货 、 散货 、 滚装 货物 、 集装箱 、 石化 产品 装卸 功能
- ARGM-ADV: 已
- rel: 具备

Example 2: *OP* 纺织 工业 *T*-1 摆脱 困境 的 条件 已 基本 具备
- ARG1: *OP* 纺织 工业 *T*-1 摆脱 困境 的 条件
- ARGM-ADV: 基本
- ARGM-ADV: 已
- rel: 具备

## 承载

### 承载-01

- ARG0: entity described
- ARG1: thing arg0 carries

Example 1: *OP* *T*-1 因 *PRO* 盛产 绿竹笋 ， 被 誉为 「 绿竹笋 的 故乡 」 的 八里 ， 就 像 台湾 许多 大大小小 *OP* *T*-2 遥远 的 乡镇 ， 在 期待 与 失落 中 ， 承载 著 *OP* *T*-3 生活 必需 的 悲苦 与 欢乐 ， 并 由於 *PRO* 位处 边陲 ， 担负 著 *OP* 众人 不 愿 *PRO* 承受 *T*-4 之 重
- ARG0: *OP* *T*-1 因 *PRO* 盛产 绿竹笋 ， 被 誉为 「 绿竹笋 的 故乡 」 的 八里
- ARG1: *OP* *T*-3 生活 必需 的 悲苦 与 欢乐
- ARGM-LOC: 在 期待 与 失落 中
- ARGM-ADV: 就 像 台湾 许多 大大小小 *OP* *T*-2 遥远 的 乡镇
- rel: 承载

## 冲击

### 冲击-01

- ARG0: challenger
- ARG1: thing challenged

Example 1: 在 非 大奖赛 项目 中 ， 乌克兰 名将 布勃卡 三 次 冲击 ６ 米 １５ 的 男子 撑杆 跳高 世界 纪录 未果
- ARG0: 乌克兰 名将 布勃卡
- ARG1: ６ 米 １５ 的 男子 撑杆 跳高 世界 纪录
- ARGM-LOC: 在 非 大奖赛 项目 中
- ARGM-ADV: 三 次
- rel: 冲击

Example 2: 亚洲 金融 危机 冲击 的 困难 环境
- ARG0: 亚洲 金融 危机
- rel: 冲击

## 会

### 会-01

- ARG0: agent
- ARG1: capable of

Example 1: *OP* *T*-1 只 会 ＡＢＣ 的 人
- ARG0-: (*T*-1) 人
- ARGM-ADV: 只
- rel: 会

### 会-02

- ARG0: 

Example 1: *pro* 不 会 吧
- rel: 会

### 会-03

- (no roles)

### 会-04

- ARG0: agent
- ARG1: entity arg0 meets

Example 1: 那 你 就 去 会 好了
- ARGM-DIS: 那
- ARG0: 你
- ARGM-ADV: 就
- rel: 会

## 轻易

### 轻易-01

- ARG0: entity described

Example 1: *pro* 可以 轻易 引进 国外 各 类 排行榜 上 的 畅销 书
- ARG0: *pro*
- rel: 轻易

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

## 运营

### 运营-01

- ARG0: thing in operation and business

Example 1: 据 铁道部 总 工程师 华茂昆 介绍 ， 京九 铁路 *pro* 开通 运营 一 年 来 ， 经受 了 严冬 盛夏 和 洪水 的 考验 ， 保证 了 运输 的 安全 畅通 ， 发挥 了 社会 经济 效益
- ARG0-: *pro*
- ARGM-ADV: 一 年
- rel: 运营

### 运营-02

- (no roles)

### 运营-03

- ARG0: agent
- ARG1: entity arg0 operates

Example 1: *pro* 如果 不 基本 具备 *pro* 承载 这 个 巨大 压力 的 冲击 ， 想必 铁道部 不 会 轻易 开始 运营 网站 。
- ARGM-ADV: 想必
- ARG0-: 铁道部
- ARGM-ADV: 不
- ARGM-ADV: 轻易
- ARG1-: 网站
- rel: 运营

## 为了

### 为了-01

- ARG0: entity described
- ARG1: reason/purpose

Example 1: 出发点 却 完全 为了 她 好
- ARG0: 出发点
- ARGM-DIS: 却
- ARGM-ADV: 完全
- ARG1: 她 好
- rel: 为了

## 分流

### 分流-01

- ARG0: agent
- ARG1: theme

Example 1: 兼并 破产 和 减员增效 共 分流 人员 一百一十三万 人
- ARG0: 兼并 破产 和 减员增效
- ARG1: 人员
- ARG1-QTY: 一百一十三万 人
- ARGM-ADV: 共
- rel: 分流

Example 2: 大量 富余 人员 下岗 分流 和 再 就业
- ARG1: 大量 富余 人员
- rel: 分流

## 对

### 对-01

- ARG0: agent
- ARG1: thing confronted
- ARG2: instrument

Example 1: 同时 ， *OP* *T*-1 在 *pro* 与 ＣＩＰＭ 合作 中 逐渐 成长 的 中方 管理 人员 ， 也 变得 善于 *PRO* “ 以 中 对 洋 ” 。
- ARG0-: *PRO*
- ARG1-: 洋
- ARG2-: 以 中
- rel: 对

### 对-02

- ARG0: thing described

Example 1: 这 种 看法 是 *OP* *T*-1 不 对 的 。 ”
- ARG0-: *T*-1
- ARGM-ADV: 不
- rel: 对

Example 2: 

### 对-03

- ARG0: person described
- ARG1: entity arg0 hasn't done enough for

Example 1: *pro* 有时 看到 他们 *PRO* 睡觉 的 可爱 脸蛋 ， 会 觉得 *PRO* 有点 对 不 起 他们
- ARG0-: *PRO*
- ARG1-: 他们
- ARGM-ADV: 有点
- rel: 对

### 对-04

- ARG0: person described
- ARG1: to check (lottery, numbers, etc)

Example 1: 号码 对 奖
- ARGM-MNR: 号码
- ARG1-: 奖
- rel: 对

### 对-05

- ARG0: person described
- ARG1: entity arg0 has done enough for

Example 1: 这样子 政党 领导人 才 能够 对 得 起 过去
- ARGM-ADV: 这样子
- ARG0-: 政党 领导人
- ARGM-DIS: 才
- ARG1-: 过去
- rel: 对

### 对-06

- ARG0: agent
- ARG1: entity arg0 treats

Example 1: *pro* 不 光是 对 别人 ， 自己 也 是 ， 你 的 手机 从来 不 关机 。
- ARG0-: *pro*
- ARG1-: 别人
- rel: 对

### 对-07

- (no roles)

### 对-08

- ARG0: agent
- ARG1: entity mixed

Example 1: *pro* 香油精 对 *T*-1 的 油水
- ARG0: *pro*
- ARGM-ADV: 香油精
- ARG1: *T*-1 油水
- rel: 对

### 对-09

- ARG0: participants match each other

Example 1: 
- ARG0: 美国队
- rel: 对

### 对-010

- ARG0: 

## 合法

### 合法-01

- ARG0: theme

Example 1: 这 对 *OP* *T*-1 合法 的 老 夫 少 妻
- ARG0: *T*-1
- rel: 合法

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

## 含糊

### 含糊-01

- ARG0: entity described

## 全

### 全-01

- ARG0: thing described

Example 1: *PRO* 成为 *OP* *T*-1 国内 运输 方式 最 全 的 港口
- ARG0-PSE: 运输 方式
- ARG0-PSR: *T*-1
- ARGM-ADV: 最
- ARGM-LOC: 国内
- rel: 全

## 搬起

### 搬起-01

- ARG0: agent/cause
- ARG1: thing lifted

Example 1: *pro* 搬起 石头
- ARG0: *pro*
- ARG1: 石头
- rel: 搬起

## 砸

### 砸-01

- ARG0: agent
- ARG1: thing arg0 puts down/dumps
- ARG2: target

Example 1: 但 另 一 方面 ， 当 *PRO* 面临 *PRO* 升级 发展 的 契机 时 ， 叶进泰 可以 毫不 犹豫 地 砸 钱 投资
- ARG0: 叶进泰
- ARG1: 钱
- ARGM-ADV: 毫不 犹豫 地
- ARGM-TMP: 当 *PRO* 面临 *PRO* 升级 发展 的 契机 时
- ARGM-DIS: 另 一 方面
- ARGM-DIS: 但
- rel: 砸

Example 2: 他 早点 懂得 理财 ， 七十九 年 股市 暴跌 时 把 所有 积蓄 「 全部 砸 下去 」
- ARG0: 他
- ARG1: 所有 积蓄
- ARGM-ADV: 全部
- ARGM-TMP: 七十九 年 股市 暴跌 时
- rel: 砸

Example 3: 台电 中山 营业处 被 鸡蛋 砸 得 战痕累累
- ARG2: 台电 中山 营业处
- ARG1: 鸡蛋
- ARGM-EXT: 战痕累累
- rel: 砸

## 宁愿

### 宁愿-01

- ARG0: 

## 相信

### 相信-01

- ARG0: entity described
- ARG1: entity believed in

Example 1: 中国 还 相信 *OP* 自己 所 特有 *T*-1 的 道路
- ARG0: 中国
- ARG1: *OP* 自己 所 特有 *T*-1 的 道路
- ARGM-ADV: 还
- rel: 相信

Example 2: 他 相信 ， 在 *OP* *T*-1 新 的 一 年 里 ， *OP* 中国 在 国际 政治 和 经济 中 起 *T*-2 的 作用 将 越来越 大
- ARG0: 他
- ARG1: 在 *OP* *T*-1 新 的 一 年 里 ， *OP* 中国 在 国际 政治 和 经济 中 起 *T*-2 的 作用 将 越来越 大
- rel: 相信

## 不实

### 不实-01

- ARG0: thing described

Example 1: 正派 经营 和 *OP* *T*-1 浮夸 不实 的 坑人 陷阱
- rel: 不实

## 主动

### 主动-01

- ARG0: entity described

## 站

### 站-01

- ARG0: entity described
- ARG1: location arg0 stands

Example 1: “ 三 *RNR*-3 到 四 位 ” 站 在 资方 一 边
- ARG0: “ 三 *RNR*-3 到 四 位 ”
- ARG1: 在 资方 一 边
- rel: 站

### 站-02

- ARG0: entity described

Example 1: 首先 ， 美国 的 这 次 行动 没有 任何 *OP* *T*-1 站 得 住 脚 的 理由
- ARG0: *T*-1
- rel: 站

## 出来

### 出来-01

- ARG0: entity

Example 1: 太阳 从 西边 出来
- ARG0-: 太阳
- rel: 出来

### 出来-02

- (no roles)

## 澄清

### 澄清-01

- ARG0: agent
- ARG1: thing arg0 clarifies
- ARG2: party that arg0 clarifies arg1 to

Example 1: 北京 社科院 近史所 研究员 耿云志 仍 须 澄清 史实
- ARG0: 北京 社科院 近史所 研究员 耿云志
- ARG1: 史实
- ARGM-ADV: 仍
- rel: 澄清

Example 2: 法国 官员 １６号 从 慎重 的 向 新闻界 澄清
- ARG0: 法国 官员
- ARGM-TMP: １６号
- ARG2: 向 新闻界
- rel: 澄清

## 拿出

### 拿出-01

- ARG0: agent
- ARG1: thing taken out

Example 1: 但是 ， 联合国 特委会 至今 并 没有 拿出 *OP* *T*-1 令 人 *PRO* 信服 的 证据 ， 证明 伊 仍 拥有 大 规模 杀伤性 武器
- ARG0: 联合国 特委会
- ARG1: *OP* *T*-1 令 人 *PRO* 信服 的 证据
- ARGM-ADV: 并
- ARGM-ADV: 至今
- ARGM-ADV: 但是
- rel: 拿出

Example 2: 为 *PRO* 推动 图们江 地区 开发 ， 韩国 捐款 一百万 美元 设立 了 图们江 发展 基金 ， 目前 从 该 基金 中 拿出 十万 美元 正在 进行 中国 珲春 边境 合作区 环境 评估 项目 ， 以 期 *PRO* 对 外资 大规模 进入 这 个 地区 提供 环境 方面 的 咨询
- ARG0: 韩国
- ARG1: 十万 美元
- ARGM-LOC: 从 该 基金 中
- ARGM-TMP: 目前
- ARGM-PRP: 为 *PRO* 推动 图们江 地区 开发
- rel: 拿出

## 充分

### 充分-01

- ARG0: thing described

Example 1: 事实 清楚 ， 证据 充分
- ARG0: 证据
- rel: 充分

## 来

### 来-01

- ARG0: comer
- ARG1: place come to
- ARG2: place come from

Example 1: 龙永图 是 *OP* *T*-1 于 １８日 从 波士顿 来 华盛顿 参加 演讲 的
- ARG0: *T*-1
- ARG1: 华盛顿
- ARG2: 从 波士顿
- ARGM-TMP: 于 １８日
- rel: 来

Example 2: *OP* *T*-1 实力 雄厚 的 日本 伊藤忠 株式会社 、 韩国 大宇 集团 和 香港 长江 实业 集团 等 大型 公司 纷纷 来 广西 投资
- ARG0: *OP* *T*-1 实力 雄厚 的 日本 伊藤忠 株式会社 、 韩国 大宇 集团 和 香港 长江 实业 集团 等 大型 公司
- ARG1: 广西
- ARGM-ADV: 纷纷
- rel: 来

Example 3: 她 每 天 早上 七 点 就 要 到 大棚 来 ， 一直 要 忙 到 晚上 六点
- ARG0: 她
- ARG1: 到 大棚
- ARGM-ADV: 就
- ARGM-TMP: 每 天 早上 七 点
- rel: 来

Example 4: 知识 经济 大 潮 迅猛 而 来
- ARG0: 知识 经济 大 潮
- ARGM-ADV: 迅猛
- rel: 来

Example 5: *T*-1 从 该 地方 来
- ARG0: *T*-1
- ARG2: 从 该 地方
- rel: 来

### 来-02

- ARG0: entity described
- ARG1: thing to be in time for

Example 1: 一些 *OP* *T*-2 未 来 得 及 *PRO* 赶上 报名 的 市民们 则 表示 十分 遗憾
- ARG0: *T*-2
- ARG1: *PRO* 赶上 报名
- ARGM-ADV: 未
- rel: 来

### 来-03

- ARG0: entity described
- ARG1: thing can't be in time for

Example 1: *pro* 虽然 说 电视 演员 不 能 *PRO* 像 电影 一样 慢慢 酝酿 情绪 ， 必须 以 对白 及 肢体 动作 吸引 观众 ， 但 *OP* *T*-1 热腾腾 的 剧本 ， *PRO* 不 要 说 *PRO* 琢磨 角色 了 ， *pro* 连 *OP* *pro* *T*-55 背 剧本 的 时间 都 来 不 及
- ARGM-ADV: 虽然说电视演员 不 能 像 电影 一样 慢慢 酝酿 情绪 ， 必须 以 对白 及 肢体 动作 吸引 观众
- ARGM-DIS: 但
- ARGM-ADV: 热腾腾 的 剧本
- ARGM-ADV: 不 要 说 琢磨 角色 了
- ARG0: *pro*
- ARG1: 连 背 剧本 的 时间
- ARGM-ADV: 都
- rel: 来

### 来-04

- ARG0: agent
- ARG1: thing, entity or effort presented

Example 1: *PRO* 不管 是 专业 新闻 工作者 ， 还是 业余 爱好者 ； 不管 报喜 ， 还是 报忧 ， 都 得 来 真的
- ARG0: *PRO*
- ARG1: 真的
- ARGM-ADV: 都
- rel: 来

### 来-05

- ARG0: people described
- ARG1: thing come around to do

Example 1: 当前 双方 应 首先 商定 *OP* *pro* *T*-1 交换 意见 的 议题 和 内容 ， 再 来 考虑 人员 层级 及 时间 、 地点 等 问题
- ARG0: 双方
- ARG1: 考虑 人员 层级 及 时间 、 地点 等 问题
- ARGM-ADV: 再
- ARGM-TMP: 当前
- rel: 来

### 来-06

- ARG0: 

Example 1: 真正 搞出 中国 的 创新 体系 来
- rel: 来

### 来-07

- ARG0: cause
- ARG1: entity arg0 causes to come/sends over

Example 1: 「 远 人 不 服 ， *pro* 则 修 文德 以 来 之 」
- ARG0: *pro*
- ARG1: 之
- ARGM-ADV: 则
- ARGM-ADV: 远 人 不 服
- rel: 来

### 来-08

- ARG0: agent
- ARG1: the entity in MWE,usually letter/call
- ARG2: receiver

Example 1: 

## 有力

### 有力-01

- ARG0: entity described

Example 1: 亚洲 地区 经济 发展 依然 强劲 有力
- ARG0: 亚洲 地区 经济 发展
- ARGM-ADV: 依然
- rel: 有力

## 还击

### 还击-01

- ARG0: agent
- ARG1: entity arg0 retaliates upon

Example 1: 有的 扛 著 迫击 重 炮 ， 有的 举起 机关枪 ， *pro* 一 连串 对著 他 还击
- ARG0: *pro*
- ARG1: 对著 他
- ARGM-ADV: 一 连串
- ARGM-ADV: 有的 举起 机关枪
- ARGM-ADV: 有的 扛 著 迫击 重 炮
- rel: 还击

## 种

### 种-01

- ARG0: agent
- ARG1: thing arg0 grows

Example 1: *OP* *T*-1 昔日 以 *PRO* 种 粗粮 为主 的 山 间 梯田
- ARG0: *PRO*
- ARG1: 粗粮
- rel: 种

Example 2: 赫风英 承包 了 六百 平方米 的 蔬菜 大棚 ， 种植 葫芦 ， *pro* 每 年 可以 种 三 季 ， 年 收入 可 达 三万 元 ； 王德莲 承包 了 一 个 大棚 ， 种植 以色列 番茄 ， 这 种 番茄 年 产量 可 达 四万 公斤 ， 主要 供应 给 各 大 宾馆 ， 年 盈利 三万五千 元
- ARG1: *pro*
- ARGM-ADV: 三 季
- ARGM-TMP: 每 年
- rel: 种

## 指责

### 指责-01

- ARG0: accuser
- ARG1: activity

Example 1: 美国 今年 ８月 以来 多 次 提出 *pro* 要 检查 朝鲜 的 所谓 “ 地下 核 设施 ” ， 指责 朝鲜 的 所谓 “ 导弹 威胁 ”
- ARG0: 美国
- rel: 指责

### 指责-02

- ARG0: accuser
- ARG1: accusee
- ARG2: predicate

Example 1: 事 发 后 ， 刚果 （ 布 ） 政府 指责 某 国 *PRO* 为 之 提供 了 基地 。
- ARGM-TMP: 事 发 后
- ARG0: 刚果 （ 布 ） 政府
- rel: 指责

## 解释

### 解释-01

- ARG0: agent/cause
- ARG1: thing explained
- ARG2: entity explanation is offered to
- ARG3: explanation arg0 offers

Example 1: 国民党 方面 ， 在 这 次 选战 中 ， 国民党 *OP* *T*-3 公开 「 投 宋 」 者 ， 还 可 被 解释 为 国民党 中 的 「 失意人 」
- ARG1: 国民党 *OP* *T*-3 公开 「 投 宋 」 者
- ARG3: 国民党 中 的 「 失意人 」
- ARGM-ADV: 还
- ARGM-LOC: 在 这 次 选战 中
- ARGM-TPC: 国民党 方面
- rel: 解释

Example 2: “ 千岛湖 事件 ” 发生 以来 ， 海协 依据 协议 向 海基会 通报 了 情况 ， 解释 *RNR*-2 并 回答 *OP* 海基会 所 提 *T*-1 的 若干 问题 与 要求
- ARG0: 海协
- ARG1: *RNR*-2
- ARGM-MNR: 依据 协议
- ARGM-TMP: “ 千岛湖 事件 ” 发生 以来
- rel: 解释

Example 3: 陈元 还 向 与会者 解释 了 香港 在 国际 金融 关系 中 的 定位
- ARG0: 陈元
- ARG1: 香港 在 国际 金融 关系 中 的 定位
- ARG2: 向 与会者
- ARGM-ADV: 还
- rel: 解释

Example 4: 特区 政府 发言人 解释 ， 虽然 香港 特别 行政区 政府 已 获 中央 人民 政府 授权 签发 香港 特别 行政区 护照 ， 香港 仍 需要 本地 法例 *PRO* 规定 有关 *pro* 签发 特区 护照 的 实际 事宜
- ARG0: 特区 政府 发言人
- ARG3: 虽然 香港 特别 行政区 政府 已 获 中央 人民 政府 授权 签发 香港 特别 行政区 护照 ， 香港 仍 需要 本地 法例 *PRO* 规定 有关 *pro* 签发 特区 护照 的 实际 事宜
- rel: 解释

Example 5: 著名 经济学家 厉以宁 今天 针对 中国 第一 部 证券法 即将 出台 ， 但 股市 却 持续 下泻 的 情况 解释 说 ： 证券法 出台 不 是 “ 利空 ” 消息
- ARG0: 著名 经济学家 厉以宁
- ARG3: 证券法 出台 不 是 “ 利空 ” 消息
- ARG1: 针对 中国 第一 部 证券法 即将 出台 ， 但 股市 却 持续 下泻 的 情况
- ARGM-TMP: 今天
- rel: 解释

Example 6: 这 位 诺贝尔 和平 奖 获得者 解释 说 ， 近 十 年 来 ， 她 “ 特别 关注 ” 有关 哥 武装 冲突 双方 的 接近 和 对话 的 各 种 创议
- ARG0: 这 位 诺贝尔 和平 奖 获得者
- ARG3: 近 十 年 来 ， 她 “ 特别 关注 ” 有关 哥 武装 冲突 双方 的 接近 和 对话 的 各 种 创议
- rel: 解释

## 原来

### 原来-01

- ARG0: the original entity

Example 1: 后来 她 figureout 之后 ， 在 *pro* 原先 工作 的 基础 上 ， *pro* 连 发 了 几 篇 顶级 杂志 的 文章 ， 又 继续 *OP* *T*-1 原来 的 工作 ， 出 了 一 本 *OP* *T*-2 非常 有 影响 的 书 ， *pro* 不 用 说 ， *pro* 拿到 名校 的 tenure 。
- ARG0: *T*-1 工作
- rel: 原来

## 真

### 真-01

- ARG0: entity described

Example 1: 连 *OP* 屋 前 挂 *T*-1 的 鱼乾 都 是 *OP* *T*-2 真 的
- ARG0: *T*-2
- rel: 真

## 出面

### 出面-01

- ARG0: agent
- ARG1: thing arg0 takes charge of

Example 1: *pro* 九八年 由 石 处长 出面 ， 促使 华夏 协会 与 亚协 *PRO* 联合 主办
- ARG0: 由 石 处长
- ARG1: *pro*
- ARGM-TMP: 九八年
- rel: 出面

Example 2: 後来 中影 前 任 副 董事长 徐立功 出面 *PRO* 协调
- ARG0: 中影 前 任 副 董事长 徐立功
- ARG1: *PRO* 协调
- ARGM-TMP: 後来
- rel: 出面

Example 3: *pro* 由 政府 出面 *PRO* 与 他国 及 国际 组织 谈判 *PRO* 建构 市场 ， 扩展 商机 ， 并 由 企业 集体 至 第一 线 布桩
- ARG0: 由 政府
- ARG1: *PRO* 与 他国 及 国际 组织 谈判 *PRO* 建构 市场 ， 扩展 商机
- rel: 出面

## 补办

### 补办-01

- ARG0: agent
- ARG1: theme

Example 1: *pro* 出面 补办 一 个 *OP* *T*-1 正规 的 互联网 证件
- ARG0: *pro*
- rel: 补办

## 正规

### 正规-01

- ARG0: thing described

Example 1: *OP* *T*-2 正规 的 传销 公司 不 会 要求 加入者 一定 要 一 次 买足 大量 的 货 ， 或是 缴交 *OP* *T*-1 昂贵 的 入会费
- ARG0: *T*-2
- rel: 正规

## 并

### 并-01

- ARG0: agent
- ARG1: thing merged
- ARG2: something arg1 is merged into
- ARG3: result

Example 1: *OP* *T*-3 被 并 *T*-3 企业
- ARG1: 企业
- rel: 并

## 难

### 难-01

- ARG0: thing described

Example 1: *PRO* 联系 到 美国 这 次 对 伊拉克 的 军事 行动 ， 人们 不 难 *PRO* 看出 ， 美国 是 想 *PRO* 利用 其 对 北约 的 控制权 ， 把 北约 作为 *OP* 其 *T*-2 推行 全球 战略 、 为所欲为 的 *OP* *T*-1 得心应手 的 工具
- ARG0: 人们
- ARG0-PRD: *PRO* 看出 ， 美国 是 想 *PRO* 利用 其 对 北约 的 控制权 ， 把 北约 作为 *OP* 其 *T*-2 推行 全球 战略 、 为所欲为 的 *OP* *T*-1 得心应手 的 工具
- ARGM-ADV: 不
- ARGM-ADV: *PRO* 联系 到 美国 这 次 对 伊拉克 的 军事 行动
- rel: 难

## 补偿

### 补偿-01

- ARG0: agent
- ARG1: entity arg0 compensates
- ARG2: thing arg0 compensates for
- ARG3: thing arg0 compensates with

Example 1: 六家 的 居民 在 区段 徵收 後 ， 虽然 可 配还 四成 的 土地 ， 但 *OP* *pro* 补偿 *T*-1 的 钱 只 足够 *PRO* 买 地
- ARG0: *pro*
- ARG3: *T*-1
- rel: 补偿

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

## 众多

### 众多-01

- ARG0: entity described

Example 1: 它 与 “ 箱根 八 里 ” 的 雄关 古道 和 千条瀑 、 九头龙 、 仙石原 以及 *OP* *T*-2 众多 的 石佛群 等 景观 构成 一 个 大 景点
- ARG0: *T*-2
- rel: 众多

## 信任

### 信任-01

- ARG0: people described
- ARG1: people trusted

Example 1: 俄 网球 协会 不 再 信任 库尔尼科娃
- ARG0: 俄 网球 协会
- ARG1: 库尔尼科娃
- ARGM-ADV: 再
- ARGM-ADV: 不
- rel: 信任

## 如此

### 如此-01

- ARG0: entity described

Example 1: *pro* 真 会 如此
- ARG0: *pro*
- rel: 如此

## 匆匆

### 匆匆-01

- ARG0: entity described

Example 1: 不管 路人 行脚 匆匆 ， 隐地 依然 坚持 *PRO* 驻足 在 文学 花园 里 耕耘
- ARG0: 路人 行脚
- ARGM-ADV: 不管
- rel: 匆匆

## 上马

### 上马-01

- ARG0: agent

Example 1: *pro* 如此 匆匆 上马
- ARG0-: *pro*
- rel: 上马

### 上马-02

- ARG0: project starting

Example 1: 怒江 工程 是否 上马
- ARG0-: 怒江 工程
- rel: 上马

### 上马-03

- (no roles)

## 运行

### 运行-01

- ARG0: thing in operation
- ARG1: agent

Example 1: 作为 金关 工程 的 广东省 无纸 贸易 中心 已 正式 运行
- ARG0: 作为 金关 工程 的 广东省 无纸 贸易 中心
- ARGM-ADV: 正式
- ARGM-ADV: 已
- rel: 运行

Example 2: *OP* 目前 日本 、 德国 投入 运行 *T*-1 的 长岛 磁悬浮 车
- ARG1: 日本 、 德国
- ARGM-TMP: 目前
- ARG0: *T*-1 -> 车
- rel: 运行

### 运行-02

- ARG0: thing described
- ARG1: location arg0 is moving to

Example 1: 苏梅克 — 列维 九 号 彗星 是 *OP* 美国 天文学家 在 一九九三年 三月 发现 *T*-1 的 ， 现 已 分裂 成 二十一 颗 彗核 ， 正 高速 向 木星 运行 ， 将 于 七月份 与 木星 碰撞 爆炸
- ARG0: 苏梅克 — 列维 九 号 彗星
- ARG1: 向 木星
- ARGM-ADV: 高速
- ARGM-ADV: 正
- rel: 运行

## 如何

### 如何-01

- ARG0: entity state of which asked about

Example 1: 各 行业 的 国际 竞争力 如何
- ARG0: 各 行业 的 国际 竞争力
- rel: 如何

## 保证

### 保证-01

- ARG0: ensurer
- ARG1: thing ensured
- ARG2: party to whom the promise is made

Example 1: 各 金融 机构 要 认真 做好 资金 调度 工作 ， 对 合法 存款 要 保证 及时 支付 ， 切实 维护 存款人 的 合法 利益 。
- ARG0: 各 金融 机构
- rel: 保证

Example 2: 中国 人民 银行 副行长 尚福林 今天 说 ， 中国 今后 的 货币 政策 走向 仍 将 适度 从紧 ， 以 控制 通货膨胀 ， 保证 国民 经济 持续 、 稳定 、 健康 地 发展 。
- ARG0: 中国 今后 的 货币 政策 走向
- rel: 保证

Example 3: 他们 信心 满满 地 向 股东 保证 ， *pro* 有 把握 让 会员 *PRO* 感受 到 收费 的 价值
- ARG0: 他们
- rel: 保证

## 修补

### 修补-01

- ARG0: agent/cause
- ARG1: thing arg0 mends

Example 1: 但 *PRO* 有 桧木 *OP* *T*-2 与生俱来 的 生命 力量 庇佑 ， 大地 终 能 逐渐 修补 、 稳定
- ARG1: 大地
- ARGM-ADV: 逐渐
- ARGM-ADV: 终
- ARGM-ADV: *PRO* 有 桧木 *OP* *T*-2 与生俱来 的 生命 力量 庇佑
- ARGM-DIS: 但
- rel: 修补

## 再

### 再-01

- ARG0: thing repeating itself

Example 1: 悲剧 不 再
- ARG0: 悲剧
- ARGM-ADV: 不
- rel: 再
