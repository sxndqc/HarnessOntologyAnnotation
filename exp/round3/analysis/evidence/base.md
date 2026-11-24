# Errors on the training documents (s3-full-two-tool)

## Document zh-0003 (5 runs)

### Sentence 1: 城市 电视 是 加拿大 一间 收费 电视台 ， 大部分 时段 以  普通话 广播 ，  并设 韩语 及  越南语 节目 时段 。

Reviewer's notes on the annotator's choices:
- [concept] 「是」字句的抽象谓词: 电视台 :domain 城市电视（无谓词） (wrong, 1 of 5 runs); 是-01 :ARG0/:ARG1 (wrong, 1 of 5 runs). 「城市电视是加拿大一间收费电视台」是类属判断（object predication），guideline 3-1-1-3 / 3-2-1-1-1（Panda is a cat → have-role-91 :ARG3 类属）应写 have-role-91；但中文训练数据里这类句子几乎都写 identity-91（如 chinese_umr-0018 第 11 句「世界中央厨房是……人道主义组织」），两者冲突、规则未定，gold 一侧记 open。系词「是」不建节点（guideline 2.1/3-1-3-6），r4 的 是-01 和 r3 的 :domain 都不对。
- [concept] 「城市电视」的实体类型: 电视台 :name（中文词作类型） (acceptable but worse, 2 of 5 runs). 命名实体类型应取 guideline 3-1-2 的类型表（company、organization 都在表里）；把普通名词「电视台」当类型不在类型表里。r3、r4 全篇都把中文普通名词当命名实体类型（电视台、集团、公司）。
- [attr] 「一间」的数量和量词: :quant 1（无量词） (acceptable but worse, 1 of 5 runs); 无 quant 无量词 (acceptable but worse, 1 of 5 runs); :refer-number singular（无 quant、无量词） (acceptable but worse, 1 of 5 runs). Better: :quant 1 :unit 间. 项目规则：量词一律保留为 :unit，数量写 :quant。省掉量词或数量判 minor。
- [role] 「以普通话」的角色: 广播 :manner 普通话 (acceptable but worse, 5 of 5 runs). Better: 广播 :medium 普通话. guideline 3-2-2-2 (2g)：语言作为传播渠道用 :medium（a French song → :medium language）。5 份系统都写 :manner，是固定习惯（本句和第 4 句「以同一讯号」、第 3 句「以有线电视……接收」同类）。
- [concept] 语言名是否作命名实体: 普通话、韩语、越南语作普通概念 (acceptable but worse, 1 of 5 runs). Better: language :name 普通话/韩语/越南语. guideline 3-1-2 类型表有 language，语言名是专名，应作命名实体。
- [role] 「大部分时段」的「大部分」: 时段 :quant 大部分（字符串常量） (acceptable but worse, 1 of 5 runs). 非数字的量化词可作 :quant 概念（guideline 4.2 :quant (a / all)），也可作 :mod；但 :quant 后接未加括号的汉字常量不合格式，常量只能是数字。
- [sense] 「并设」的义项: 设有-01 (acceptable but worse, 1 of 5 runs). Better: 设-01. 原文是「设」，PropBank 设-01（ARG0 agent、ARG1 thing set up）。设有-01 是另一个词条，原文没有「有」。
- [role] 「韩语及越南语节目时段」中语言的角色: 一个 时段 :mod 节目 :mod (and 韩语 越南语) (acceptable but worse, 4 of 5 runs); 时段 :mod (节目 :mod (and 韩语 越南语)) (acceptable but worse, 1 of 5 runs). Better: 两个 时段 各带 :mod 节目 :medium 语言. 按 guideline 3-2-2-2 (2g)，节目的语言是 :medium，不是 :mod。gold 把并列拆成两个时段、系统用一个时段带并列修饰，这个切分差别两种都可以；r5 把语言挂在节目上意思更贴切，但角色仍应是 :medium。
- [doc-temporal] 三个状态相对文档时间: 只给 电视台、广播 两个，设-01 没有时间父节点 (acceptable but worse, 1 of 5 runs). 三个都是现在的状态或习惯，挂 DCT :overlap 或彼此 :overlap 都可以。guideline 5.1/7：每个事件都要有时间父节点，r3 漏了 设-01。

### Sentence 2: 该台 的 最大 股东 为 新 时代 集团 子公司 新  时代 传媒 集团 ，  总部 设于 卑诗省 大  温哥华 地区 的  列治文 ，  并  于  安大略省 大  多伦多 地区 的  列治文山 设有 分部 。

Reviewer's notes on the annotator's choices:
- [concept] 「为」字句的谓词: 为-01 :ARG1 股东 :ARG2 集团 (wrong, 1 of 5 runs); have-org-role-92 :ARG0 集团 :ARG1 电视台 :ARG2 股东 (wrong, 1 of 5 runs). Better: identity-91 :ARG1 股东 :ARG2 新时代传媒集团. 「最大股东为X」是等同句（定指的最大股东 = X），用 identity-91。系词「为」不建节点；而且 PropBank 为-01 只有 ARG0（主语）和 ARG1（表语），r3 用的 ARG2 不存在。r4 的 have-org-role-92 用了不存在的 ARG0，ARG1/ARG2 也配错（ARG1 应是集团，ARG2 电视台，ARG3 股东）。
- [structure] 「该台的股东」的关系: 股东 :possessor 台 (acceptable but worse, 4 of 5 runs). 项目规则：have-org-role-91 应写 -92。guideline 表 8：have-org-role-92 的 ARG1 是担任角色者（theme）、ARG2 是组织，gold 把股东放在 ARG2、该台放在 ARG1，方向反了。应为 股东 :ARG1-of (have-org-role-92 :ARG2 台)。系统用 :possessor 意思能表达但不如 have-org-role-92（guideline 3-2-1-3 组织内的角色名词用 have-org-role）。
- [structure] 「最大」的表示: 股东 :mod 最大 (acceptable but worse, 5 of 5 runs). Better: 股东 :ARG1-of have-degree-91 :ARG2 大 :ARG3 最. 训练数据里「最 X」一律写 have-degree-91 :ARG2 性质 :ARG3 最（chinese_umr-0019 第 3 句「最低温」、chinese_umr-0016 第 9 句「新高」、chinese_umr-0001 第 30 句「最著名」）。系统全篇把「最大」当一个 :mod 词。
- [concept] 「该台」的表示: 该台（一个节点） (acceptable but worse, 1 of 5 runs); 电视台（丢了「该」） (acceptable but worse, 3 of 5 runs). 指示词「该」按 guideline 3-2-2-2 作 :mod；不该和中心词合成一个概念，也不该丢掉。
- [concept] 「大温哥华地区」「大多伦多地区」的实体: 地区 :name 大/温哥华（「地区」作类型） (acceptable but worse, 2 of 5 runs). guideline 3-1-2 类型表 region 类下有 local-region；「大温哥华地区」是整体专名。把「地区」当类型、名字里去掉「地区」，类型不在表里。
- [role] 「设于」的处所论元: 设-01 :place 列治文 (wrong, 1 of 5 runs). Better: 设-01 :ARG3 列治文. PropBank 设-01 的 ARG3 是 location of set up（例句「总部仍设在法兰克福」ARG3 在法兰克福），核心论元能表达时不用 :place。
- [sense] 「设有」的义项: 设-01 :ARG3 列治文山 (acceptable but worse, 1 of 5 runs). Better: 设有-01 :ARG2 列治文山. 原文是「设有」，PropBank 有 设有-01（ARG0 agent、ARG1 thing set up、ARG2 location）。gold 用 设-01 加 ARG3 意思一样，但词条不对（gold 还把这个节点错对齐到第 16 词）。
- [role] 「总部」的所属: 总部 :poss 新时代传媒集团（旧名） (acceptable but worse, 1 of 5 runs). Better: 总部 :possessor 新时代传媒集团. 「总部设于列治文」的总部是新时代传媒集团的总部，系统用重入补出所属更完整。r3 全篇用旧名 :poss（应为 :possessor，规则判 minor，只记这一处）。
- [doc-coref] 本句的共指: 另把新时代传媒集团和新时代集团标成同一实体，且前后顺序反写 (wrong, 1 of 5 runs); 另有自指 (设-01 :same-event 自己)、(集团 :same-entity 自己) (wrong, 1 of 5 runs). Better: (城市电视 :same-entity 该台). 子公司和母集团不是同一实体；节点不能和自己共指；guideline 5.3 先写前面的提及。
- [doc-temporal] 「为」句的时间父节点: 只给「为」，两个 设 没有时间父节点 (acceptable but worse, 1 of 5 runs). guideline 5.1：每个事件只有一个参照时间。gold 给 s2i2 挂了两个父节点，其中 DCT 那条已足够。r3 漏了两个 设-01 的时间关系。

### Sentence 3: 该台 现时 设有 两条 频道 ， 分别 是 以 标清 播放 的  主  频道 （  1  台  ）  和  以  高清 播放 的  城市 2  高清 台  ：  前者 可  于  全国 以  有线 电视 、  宽带 电视 和  卫星 电视 接收 ，  后者 于  启播 初期 则  在  贝尔 公司 的  宽带 电视 系统 播放 。

Reviewer's notes on the annotator's choices:
- [concept] 「分别是」的表示: 只有 (and 主频道 城市2高清台)，没有等同谓词 (acceptable but worse, 1 of 5 runs); 是-01 :ARG1 两条频道 :ARG2 (and …) (wrong, 1 of 5 runs). 「两条频道分别是A和B」是等同句，用 identity-91（训练数据通行写法）。系词不建节点（guideline 3-1-3-6）；r3 还给 是-01 用了 PropBank 没有的 ARG2（是-01 只有 ARG0/ARG1）。r4 用 是-01 是同一习惯，见第 1 句。r2 丢了谓词，只靠文档级 :subset-of 表示关系。
- [structure] 「主频道（1台）」的「1台」: 没有标「1台」 (acceptable but worse, 3 of 5 runs). 括号里的「1台」是主频道的别名，可作名字（与「城市2高清台」平行），也可如 gold 读作第 1 台。丢掉不标是信息缺失。
- [concept] 「城市2高清台」的实体类型: 频道 :name（中文词作类型） (acceptable but worse, 5 of 5 runs). guideline 3-1-2 类型表没有「频道」；最接近的是 cultural-artifact 下的 broadcast-program（也有人会取 organization），拿不准哪个最好，但中文普通名词不应作命名实体类型。
- [attr] 两个关系从句「播放」的 aspect: state (acceptable but worse, 3 of 5 runs). Better: habitual. 以标清/高清播放是经常性的播出过程，guideline 4.1 用 habitual；播放是过程动词，标 state 不准确。
- [role] 「以有线电视……接收」的角色: 接收 :manner (and …) (acceptable but worse, 3 of 5 runs). 接收所凭借的渠道或手段，:medium（guideline 3-2-2-2 的传播渠道）或 :instrument 都合适；:manner 是方式，不准确。gold 拆成 电视 :mod 有线 等、用 or，系统用 有线电视 等整词、用 and，这个差别两种都可以。
- [doc-modal] 「可……接收」的模态强度: (author :full-affirmative 接收) (acceptable but worse, 3 of 5 runs). Better: (author :neutral-affirmative 接收). guideline 5.2：can / 可以 / 能 表可能，强度 neutral-affirmative。
- [sense] 「启播」的概念: 启播-01 (wrong, 5 of 5 runs). PropBank 没有「启播」，按 guideline 2.1 应写 启播-00；启播-01 是凭空编号。gold 把一个词拆成 启-01 + 播-01，而 PropBank 启-01 只有 ARG0，ARG1 不存在（gold 还把 播-01 错对齐到第 11 词）。
- [role] 「启播初期」中初期与启播的关系: 初期 :poss 启播 (acceptable but worse, 1 of 5 runs). 时间方位名词带所属事件，按项目规则建节点，:op1 或 :mod 都可以；:poss 是旧名，且所属关系不合这里的意思。
- [attr] 「后者于启播初期……播放」的 aspect: state (acceptable but worse, 2 of 5 runs). 启播初期在贝尔系统上的播出是过去一段时间里经常性的过程，habitual 或（作为已结束的一段）performance 都说得通；播放是过程动词，state 不准确。
- [doc-temporal] 「后者于启播初期……播放」的时间: (document-creation-time :overlap 播放) (acceptable but worse, 1 of 5 runs); (document-creation-time :after 播放)（方向反写：按 UMR 读法是将来） (wrong, 2 of 5 runs); 没有时间父节点 (acceptable but worse, 2 of 5 runs). Better: 在 接收 之前（过去）. 句首「现时设有两条频道」说明频道已经启播，「于启播初期」指过去的一段时间，应在 DCT 之前：(document-creation-time :before 播放)。r2、r4 想表达的是「DCT 在播放之后」，但 UMR 的 (A :after B) 是 B 在 A 之后，写出来成了将来（这个方向错误在第 6 句等处反复出现）。guideline 5.1/7 每个事件都要有时间父节点。
- [doc-temporal] 「现时设有」相对文档时间: 只给根上的 and 挂 DCT (acceptable but worse, 1 of 5 runs). Better: (现时 :contained 设有)，现时挂 DCT. 「现时」明说是现在的状态，与 DCT 重叠；gold 的 :before 表示过去，错。guideline 5.1 时间表达优先：有「现时」时最好让事件挂在它下面。

### Sentence 4: 与 其 姊妹台 新 时代 电视 的 主 频道 不同 ，  城市 电视 的  两条 频道 于  全国 各自 以  同一 讯号 播放 ，  不设 加东 版  和  加西 版  。

Reviewer's notes on the annotator's choices:
- [sense] 「与……不同」的义项和论元: 不同（无义项）:ARG1 两条频道 :ARG2 主频道 (wrong, 1 of 5 runs); 不同-01 :ARG1 两条频道 :ARG2 主频道 (wrong, 2 of 5 runs); 播放 :ARG1-of (不同-01 :ARG2 主频道) (wrong, 2 of 5 runs). Better: 不同-01 :ARG0 (and 新时代电视主频道 城市电视两条频道). PropBank 不同-01 只有 ARG0（things which are different），「与X不同」的比较对象是 ARG0-CRD，并入 ARG0，所以 gold 用 and 作 ARG0 是对的；ARG1/ARG2 都不存在。r1 还丢了义项号。r3、r5 把不同挂在播放上，拿播放事件和频道比较，类型也不对。
- [role] 新时代电视主频道与新时代电视的部分整体方向: 频道 :poss 新时代电视（旧名） (acceptable but worse, 1 of 5 runs). Better: 频道 :possessor 新时代电视. 项目规则：部分为父节点用 :part-of。gold 以频道（部分）为父节点却写 :part，方向反了（同句城市电视的两条频道 gold 写的是 :part-of，正确）。系统用 :possessor 也可以。
- [structure] 「其姊妹台新时代电视」的同位关系: 新时代电视 :mod 姊妹台（丢了「其」） (acceptable but worse, 3 of 5 runs). Better: 新时代电视 :ARG1-of have-rel-role-92 :ARG2 城市电视 :ARG3 姊妹台. 「其姊妹台新时代电视」中姊妹台是新时代电视（电视台），不是它的主频道；gold 把 identity-91 挂在主频道上，等同对象错了。姊妹关系用 have-rel-role-92（规则认可 -92）最清楚，:mod 也可以。
- [structure] 「各自」: 没有标「各自」 (acceptable but worse, 1 of 5 runs). Better: 播放 :mod 各自. 「各自以同一讯号播放」的「各自」表示两条频道分别播出，有实际意义，不应丢。
- [attr] 「播放」的 aspect: state (acceptable but worse, 1 of 5 runs). Better: habitual. 经常性的播出，guideline 4.1 用 habitual；过程动词不标 state。
- [doc-modal] 否定事件「不设」的模态: (author :full-affirmative 设) (wrong, 1 of 5 runs). Better: (author :full-negative 设). guideline 5.2：带 :polarity - 的事件，模态强度是 full-negative。
- [doc-coref] 「城市电视的两条频道」与第 3 句的共指: 没有标 (acceptable but worse, 1 of 5 runs); (第3句主频道 :same-entity 新时代电视主频道) (wrong, 1 of 5 runs). Better: (第3句两条频道 :same-entity 本句两条频道). 本句「城市电视的两条频道」就是第 3 句「设有两条频道」的那两条（guideline 5.3 重复提及要连共指）。r5 把城市电视的主频道和新时代电视的主频道连成同一实体，错。
- [doc-temporal] 三个事件的时间父节点: 只给 播放，不同、设 没有时间父节点 (acceptable but worse, 1 of 5 runs); 不同-01 没有时间父节点 (acceptable but worse, 1 of 5 runs). 三个都是现在的状态或习惯，与 DCT 或彼此重叠均可；guideline 5.1/7 每个事件都要有时间父节点。

### Sentence 5: 城市 电视 的 历史 可 追溯 至 温哥华 的 世界 电视 。

Reviewer's notes on the annotator's choices:
- [sense] 「追溯」的义项和论元: 追溯-03 :ARG0 历史 :ARG2 世界电视 (wrong, 1 of 5 runs); 追溯-01 :ARG1 历史 :ARG2 世界电视 (wrong, 2 of 5 runs). Better: 追溯-02 :ARG0 历史 :ARG1 世界电视. PropBank 追溯-02：ARG0 thing described、ARG1 time arg0 goes back to，正是「历史可追溯至……」。追溯-01 是 review（只有 ARG0/ARG1，没有 ARG2）；追溯-03 是 attribute to，ARG2 是 ARG1 归因的对象，这里没有 ARG1。

### Sentence 6: 该台 由 刘天均 创办 ， 于 1982 年 获 加拿大 视讯 委员会 （  CRTC ）  发放 地区性 收费 电视 牌照 ，  并  于  同年 启播 。

Reviewer's notes on the annotator's choices:
- [structure] 「获……发放……牌照」的主谓词: 丢掉「获」，发放-01 :ARG2 台 (acceptable but worse, 3 of 5 runs). Better: 获-01 :ARG0 台 :ARG1 (牌照 :ARG1-of 发放-01). 原文主干是「该台获……牌照」，PropBank 获-01（ARG0 obtainer、ARG1 thing obtained），「CRTC 发放」是牌照的修饰。改成 发放-01 :ARG2 台 意思接近，但丢了原文的谓词。
- [structure] 「加拿大视讯委员会（CRTC）」的缩写: CRTC 并入名字作 :op4 (acceptable but worse, 1 of 5 runs); 名字不分词 + :mod CRTC (acceptable but worse, 1 of 5 runs); :alias (name CRTC) (acceptable but worse, 2 of 5 runs). 括注的缩写可用 identity-91 等同，也可仿训练数据（chinese_umr-0018 第 7 句「简称」→ 简称-01 :ARG2）。:alias 不在 guideline 的角色表里；把缩写并进名字或把名字写成一个 op 不合 guideline 2.2（名字按词分 op）。
- [concept] 「同年」: 年 :mod 同 (acceptable but worse, 1 of 5 runs); 同年（一个概念） (acceptable but worse, 1 of 5 runs). 「同年」指上文的 1982 年，重入或另写 :year 1982 都把指称落实了；只写字面「同年」没有落实所指。
- [doc-temporal] 事件先后和相对 DCT 的方向: (创办 :before 发放)、(发放 :before 启播)：先后反写 (wrong, 1 of 5 runs); (… :before …) 先后反写，且相对 DCT 也反写（DCT :after 事件 或 date :before DCT） (wrong, 4 of 5 runs). Better: (DCT :before 创办)、(创办 :after 获)、获与启播 :overlap. UMR 的 (A :before B) 是 B 在 A 之前（guideline 5.1：关系说的是子节点相对父节点）。创办在先、1982 年获牌照、同年启播：应写 (创办 :after 获) 或 (获 :before 创办)。5 个系统都把 (创办 :before 获) 当成「创办在获之前」，方向全反；r2、r4、r5 的 (document-creation-time :after 事件/1982) 和 r3 的 (1982 :before document-creation-time) 也把过去写成了将来。

### Sentence 7: 世界 电视 的 广播 范围 限于 卑诗省 ， 以 粤语 、  国语 和  旁遮普语 等  语言 服务 省内 的  少数 族裔 社群 ，  总部 设  于  温哥华 市甘比街 。

Reviewer's notes on the annotator's choices:
- [sense] 「限于」的义项和论元: 限于-01 :ARG1 范围 :ARG2 卑诗省 (wrong, 2 of 5 runs); 限-01 :ARG1 范围 :ARG2 卑诗省 (acceptable but worse, 2 of 5 runs). Better: 限于-01 :ARG0 X :ARG1 卑诗省. PropBank 限于-01：ARG0 theme、ARG1 range，没有 ARG2。原文是「限于」，PropBank 有这个词条，用 限-01（ARG1 entity limited、ARG2 limitation）论元自洽但词条不对。系统常按「ARG1 受事、ARG2 其他」的印象给论元编号而不查 roleset（又见第 4 句 不同-01、第 5 句 追溯-01、第 8 句 来自-01）。
- [attr] 「服务」的 aspect: state (acceptable but worse, 2 of 5 runs). Better: habitual. 电视台经常性地以多种语言提供服务，guideline 4.1 用 habitual。
- [concept] 「温哥华市甘比街」的实体: street :name 甘比街 (acceptable but worse, 2 of 5 runs); city-district :name 甘比街 (acceptable but worse, 1 of 5 runs); 街 :name 甘比街 (acceptable but worse, 1 of 5 runs); street :name 市甘比街（切分错） (wrong, 1 of 5 runs). Better: road :name 甘比街. guideline 3-1-2 类型表 facility 下有 road，没有 street；甘比街是街道不是城区；中文「街」不应作类型。「温哥华市甘比街」是温哥华市 + 甘比街，r4 切成「市甘比街」是错的。
- [doc-temporal] 三个过去状态的时间: 没有任何时间关系 (wrong, 2 of 5 runs). 本句描述的是世界电视（城市电视的前身）当时的状况，是过去的状态。UMR (A :before B) 是 B 在 A 之前、(A :after B) 是 B 在 A 之后：r2 的写法表示限于发生在启播之前，r4 的写法表示将来。guideline 5.1/7 每个事件都要有时间父节点，r1、r3 整句没有 :temporal。（系统的方向反写是同一习惯，见第 6 句，这里记 open。）
- [doc-coref] 卑诗省、温哥华与前文的共指: 只连了世界电视，地名没有连 (acceptable but worse, 5 of 5 runs). Better: 卑诗省、温哥华都连到前文. guideline 5.3：重复提及的专名也要连共指（卑诗省见第 2 句，温哥华见第 5 句）。系统一般只连电视台，不连地名。

### Sentence 8: 该台 当年 并 不 被 允许 播放 广告 ， 收入 来自 定义 户  收费 ；  此  限制 于  1992 年  取消 。

Reviewer's notes on the annotator's choices:
- [role] 「不被允许播放广告」的论元: 允许-01 :ARG1 播放（无被允许者） (wrong, 1 of 5 runs). Better: 允许-01 :ARG1 台 :ARG2 播放. PropBank 允许-01：ARG1 allowed party、ARG2 predicate。被允许的行为是 ARG2，台是 ARG1。
- [doc-modal] 否定的「允许」的模态强度: (author :full-affirmative 允许)，图里有 :polarity - (wrong, 3 of 5 runs). Better: (author :full-negative 允许). guideline 5.2：带 :polarity - 的事件强度是 full-negative。
- [doc-modal] 「播放广告」在「不允许」下的模态: (允许 :partial-negative 播放) (acceptable but worse, 1 of 5 runs). guideline 5.2：补足语事件以情态谓词为父节点，强度 unspecified 或谓词蕴含的强度（不被允许 → 实际没有播放，full-negative 也说得通）。gold 另给作者 full-affirmative 播放，等于断言播放了广告，与原文相反，且一个事件有两个模态父节点。
- [role] 「收入来自……收费」的论元: 来自-01 :ARG1 收入 :ARG2 收费 (wrong, 4 of 5 runs). Better: 来自-01 :ARG0 收入 :ARG1 收费. PropBank 来自-01：ARG0 entity described、ARG1 source，没有 ARG2。
- [structure] 「定义户收费」: 收费-01 :mod 定义户 (acceptable but worse, 1 of 5 runs); 收费（非事件）:mod 定义户 (acceptable but worse, 3 of 5 runs); 收费 :mod 订户（改了原词） (acceptable but worse, 1 of 5 runs). Better: 收费-01 :ARG3 定义户. PropBank 收费-01 的 ARG3 是 collected from，向订户收费正是 ARG3。原文「定义户」疑为「订户」之误，但概念应照原文写。
- [doc-coref] 「此限制」与「不允许」的共指: (限制 :same-event 允许)：后者在前 (acceptable but worse, 2 of 5 runs); 没有标 (acceptable but worse, 3 of 5 runs). Better: (允许 :same-event 限制). 「此限制」回指前面的「不被允许播放广告」，guideline 5.3 应连 same-event，并且先写前面的提及。

### Sentence 9: 世界 电视 于 1983 年 向 CRTC 申请 全国性 中文 收费 电视 牌照 ，  但  当局 于  1984 年  将  此  牌照 批予 由  章建国 （  即  章小蕙 之父 ）  于  多伦多 创办 的  加拿大 中文 电视 有限 公司 （  简称 「  中文 电视 」  ）  。

Reviewer's notes on the annotator's choices:
- [concept] 「但」的话语关系: contrast-01 (acceptable but worse, 4 of 5 runs). guideline 2.5（精简版）：转折「但是、却、然而」用 but-91，对比用 contrast-91；中文训练数据里 but-91 有 63 句、contrast-91 有 8 句。contrast-01 是英语 PropBank 的框架，不是 UMR 的抽象谓词。
- [sense] 「批予」的概念: 批予-01 (wrong, 3 of 5 runs); 批准-01 :ARG2 公司 (wrong, 1 of 5 runs); 批准-02 :ARG2 公司 (wrong, 1 of 5 runs). Better: 批-01 :ARG1 (予-01 :ARG0 当局 :ARG1 牌照 :ARG2 公司). PropBank 没有「批予」，作整词应写 批予-00，批予-01 是凭空编号；gold 拆成 批-01（ARG1 entity given permission to）+ 予-01（ARG0 giver、ARG1 thing given、ARG2 receiver），各部分都合 PropBank，可以接受。批准-01 没有 ARG2；批准-02 的 ARG2 是 predicate，不是接受者；而且原文不是「批准」。
- [structure] 「章小蕙之父」的亲属关系: 章建国 :ARG0-of have-rel-role-92 :ARG1 章小蕙 :ARG2 父 (wrong, 3 of 5 runs); 章建国 :ARG0-of have-rel-role-92 :ARG1 章建国 :ARG2 章小蕙 :ARG3 父 (wrong, 1 of 5 runs). Better: 章建国 :ARG1-of have-rel-role-92 :ARG2 章小蕙 :ARG3 父亲. 项目规则：-91 改 -92。guideline 表 8：have-rel-role-92 ARG1 是本人、ARG2 是亲属、ARG3 是本人的角色，没有 ARG0。gold 的论元配置是对的，只是编号 -91。r1、r3、r4 用了不存在的 ARG0，ARG1/ARG2 也整体错位；r2 还让章建国同时作 ARG0 和 ARG1。
- [structure] 「简称『中文电视』」: :alias (name "中文" "电视") (acceptable but worse, 1 of 5 runs); 没有标简称 (acceptable but worse, 2 of 5 runs). Better: 简称-01 :ARG2 (name :op1 "中文" :op2 "电视"). 原文有「简称」，训练数据写 简称-01 :ARG2 name（chinese_umr-0018 第 7 句）。name 的 :opN 必须是带引号的字符串（guideline 2.2），gold 写成了概念节点。:alias 不在 guideline 的角色表里。
- [doc-coref] 「当局」与 CRTC 的共指: 没有标 (acceptable but worse, 5 of 5 runs). Better: (CRTC :same-entity 当局). 「当局于1984年将此牌照批予……」中的当局就是前面受理申请的 CRTC，guideline 5.3 应连共指。

### Sentence 10: 而 又 见 当年 加拿大 中文 电视 广播 业正 处于 起步 阶段 ，  当局 认为 温哥华 地区 难以 支持 两间 相互 竞争 的  中文 电视台 ，  因此 在  中文 电视 的  牌照 上  加入 条款 ，  限制 该台 于  启播 两年 内  不能 于卑诗省 落地 ，  令  世界 电视 得以 维持 其  省内 唯一 中文 电视台 的  地位 。

Reviewer's notes on the annotator's choices:
- [structure] 「又见……认为……因此……」的因果关系: 用 cause-01 表示因果 (acceptable but worse, 5 of 5 runs). Better: have-reason-91 :ARG1 (加入、限制) :ARG2 (见、认为). 当局的判断是加入条款的理由（项目规则：理由用 reason），中文训练数据用 have-reason-91（33 句，ARG1 结果、ARG2 理由），没有一句用 cause-01；cause-01 是英语 PropBank 框架。5 个系统的 cause-01 挂法也各不相同。
- [structure] 「又见」: 见-01 :ARG1 处于（无 ARG0） (acceptable but worse, 1 of 5 runs); 没有「见」，处于 作 认为 的 :reason/:cause 或并列项 (acceptable but worse, 3 of 5 runs). Better: 见-01 :ARG0 当局 :ARG1 处于. PropBank 见-01：ARG0 person who sees、ARG1 theme。「当局又见……」的见是当局的认知，应保留，ARG0 是当局。
- [sense] 「处于」的义项和论元: 处于-01 :ARG1 业 :ARG2 阶段 (wrong, 3 of 5 runs); 处-01 :ARG1 业 :ARG2 阶段 (wrong, 1 of 5 runs). Better: 处于-01 :ARG0 X :ARG1 阶段. PropBank 处于-01：ARG0 theme、ARG1 location/state/status，没有 ARG2。原文是「处于」，有这个词条，不应换成「处」。
- [sense] 「加入条款」的义项和牌照的角色: 加入-01 :ARG1 条款 :ARG2 牌照 (wrong, 2 of 5 runs); 加入-01 :ARG1 条款 :place 牌照 (wrong, 3 of 5 runs). Better: 加入-02 :ARG1 条款 :ARG2 牌照. PropBank 加入-01 是 joiner 加入组织（只有 ARG0/ARG1），加入-02 是把 ARG1 加进 ARG2（entity arg0 adds arg1 into），在牌照上加入条款是 加入-02，牌照是 ARG2，不该用 :place。
- [sense] 「限制」的义项: 限制-01 :ARG1 被限制者 :ARG2 落地 (wrong, 2 of 5 runs); 限制-01 :ARG1 落地 (acceptable but worse, 1 of 5 runs). Better: 限制-02 :ARG1 被限制者 :ARG2 落地. PropBank 限制-02：ARG0 imposer、ARG1 person restriction is imposed on、ARG2 action，正合「限制该台……不能落地」；限制-01 只有 ARG0/ARG1，带 ARG2 是错。
- [structure] 「启播两年内」: :duration 两年，没有「启播」 (acceptable but worse, 1 of 5 runs). Better: 内 / after :op1 启播-01，两年. 期限是「启播（之后）两年内」，起点是启播，应有启播事件（概念按 PropBank 应为 启播-00，见第 3 句）。gold 和 r5 都丢了启播；gold 把时间范围记为 :range 也不如 :temporal。
- [role] 「维持其……地位」的论元和「其」: 维持-01 :ARG0 世界电视 :ARG1 地位，没有标「其」 (acceptable but worse, 3 of 5 runs). Better: 维持-01 :ARG0 世界电视 :ARG1 地位，地位 :possessor 世界电视. 「令世界电视得以维持其省内唯一中文电视台的地位」，其 = 世界电视；gold 让地位属于 s10c（它当作该台/中文电视的节点），错。PropBank 维持-01：ARG0 maintainer、ARG1 entity maintained、ARG2 level，世界电视作 ARG0、地位作 ARG1 更自然，gold 的 ARG1/ARG2 读法也勉强说得通，这里只改领属。
- [doc-modal] 「认为……难以支持」的模态: (认为 :unspecified 支持)，难以 只作 :mod (acceptable but worse, 2 of 5 runs). Better: (认为 :partial-negative 支持). guideline 5.2：引述的想法，作者确定说话人/思考者，思考内容挂在思考者（或认为事件）之下；gold 把 支持 直接挂在 author 下，概念者错了。「难以」使强度偏否定，unspecified 丢了这层意思。
- [structure] 「令」的表示: 令-01 :ARG0 加入/条款 :ARG1 维持 (acceptable but worse, 3 of 5 runs); cause-01 :ARG0 加入/条款 :ARG1 维持 (acceptable but worse, 2 of 5 runs). PropBank 令-01：ARG0 causer、ARG1 causee、ARG2 predicate；用 令-01 时世界电视应是 ARG1、维持是 ARG2，系统把维持放在 ARG1。gold 用 have-reason-91 表达因果也可以。

### Sentence 11: 温哥华 华裔 商人 冯永发 旗下 的 新 时代 集团 联同 电视 广播 国际 有限 公司 于  1992 年  宣布 斥资 925 万  加元 收购 中文 电视 的  资产 ，  并  同时 以  380 万元 收购 国泰 电视 。

Reviewer's notes on the annotator's choices:
- [role] 「联同」的另一家公司: 宣布 :accompanier 电视广播国际 (acceptable but worse, 1 of 5 runs). 「联同」两家公司一起宣布；guideline 3-1-1（:companion）说分开表达的同伴可以用 :companion，合在一起的作单一施事，两种都说得通。:accompanier 是 AMR 的旧名，UMR 用 :companion。
- [structure] 「斥资」是否作谓词: 收购 :ARG2 斥资-01，斥资 :ARG1 金额 (wrong, 1 of 5 runs); 没有斥资节点，金额直接挂在收购上 (acceptable but worse, 4 of 5 runs). Better: 斥资-01 :ARG1 收购 :ARG2 金额. PropBank 斥资-01：ARG0 invester、ARG1 project、ARG2 fund，gold 的写法正好符合框架。s3/r3 把金额作 ARG1（应为 ARG2），又给收购-01 加了框架里没有的 ARG2。省掉斥资保住了金额，但丢了一个谓词。
- [role] 收购的金额（以380万元）的角色: :manner monetary-quantity (acceptable but worse, 2 of 5 runs); :cost monetary-quantity (wrong, 1 of 5 runs); 收购 :ARG3 monetary-quantity (wrong, 1 of 5 runs). PropBank 收购-01 只有 ARG0、ARG1，没有价格论元，ARG3 不能用；:cost 不在 UMR 的角色表里（3-2-2）。「以X元」是凭借的手段，:instrument 可以，:manner 勉强。系统对 925 万加元（没有斥资节点时）也是同样的角色。
- [structure] 「商人」与冯永发的关系: 冯永发 :ARG0-of (have-org-role-92 :ARG2 商人) (wrong, 1 of 5 runs); 冯永发 :ARG0-of 商人 (wrong, 1 of 5 runs). 同位语「商人冯永发」：训练数据（chinese_umr-0001 第7句「小报《国家询问报》」）用 identity-91，作 :mod 也能表达。have-org-role-92 的人是 ARG1、头衔是 ARG3（abridged 2.3），s3/r1 用了 ARG0-of 和 ARG2，两处都错；商人不是谓词，s3/r5 的 :ARG0-of 没有意义。华裔、温哥华挂在商人还是人名上是位置差别，不另记。
- [concept] 「旗下」的表示: 旗下-01 谓词 (wrong, 1 of 5 runs); 没有旗下节点，只用 :possessor/:poss (acceptable but worse, 4 of 5 runs). Better: 集团 :mod 旗下（另有 :possessor 冯永发）. PropBank 没有「旗下」，不能编 -01；训练数据 chinese_umr-0001 第7句「旗下的八卦小报」写 :mod 旗下 加 :possessor。只用领属关系意思也在，略差。
- [role] 集团与冯永发的领属方向: 集团 :poss-of 冯永发（成了集团领有冯永发） (wrong, 1 of 5 runs). 冯永发旗下的集团：集团是领属物，冯永发是领有者，应为 (集团 :possessor 冯永发)（guideline 3-2-2-2）。s3/r3 用反向 :poss-of，方向反了。s3/r4 的问题记在「旗下」一条。
- [role] 领有者的角色名 :poss: :poss（旧名） (acceptable but worse, 2 of 5 runs). Better: :possessor. 按发布数据写 :possessor，不是 AMR 的 :poss（Conventions 一节）。s3/r3 全篇如此（第2–21句大多数句子都有），s3/r1 只在本句。
- [concept] 新时代集团的实体类型: 集团（中文词作类型） (wrong, 1 of 5 runs). 命名实体的类型用英文类型词（abridged 2.1、2.2：entity types 用英文），company 或 organization 都可以；「集团」是中文普通名词，不是实体类型。
- [concept] 电视广播国际有限公司的名字切分: :op1 "电视广播国际" 不拆 (acceptable but worse, 1 of 5 runs). 中文名字按词拆成 :opN（abridged 2.2：欧洲议会 → 欧洲 / 议会），「电视广播国际」是三个词。
- [structure] 「同时」: 没有同时节点 (acceptable but worse, 2 of 5 runs). Better: 第二次收购 :temporal 同时. 原文有「同时」，应作节点；漏了丢掉一个时间修饰（两笔收购同时）。
- [structure] 第二笔收购是否在宣布之下: 根为 and(宣布, 收购2) (acceptable but worse, 1 of 5 runs). Better: 宣布 :ARG1 (and 收购1 收购2). 「宣布斥资……收购……，并同时以……收购……」，「并同时」连接的是宣布的两项内容，读成和宣布并列的事件较勉强。
- [doc-temporal] 宣布与收购的先后: 宣布 :overlap 斥资/收购 (acceptable but worse, 1 of 5 runs); 宣布 :before 收购（收购在宣布之前） (wrong, 3 of 5 runs); 收购没有时间父节点 (acceptable but worse, 1 of 5 runs). (A :before B) 是 B 在 A 之前；宣布的是将要进行的收购（第12句 1993 年才获批），收购在宣布之后，应为 (宣布 :after 收购)。s3/r1、r2、r5 方向写反：5 个系统全篇都把 (A :before B) 当成「A 在 B 之前」，这里是本段第一次出现，之后记 open。overlap 太粗但不算错。
- [doc-temporal] 宣布相对第10句事件: (s10 加入 :before 宣布)：宣布在 1984 年的加入条款之前 (wrong, 2 of 5 runs). Better: 不和前句事件相连. (A :before B) 是 B 在 A 之前；1992 年的宣布在第10句（1984 年前后）加入条款之后，s3/r2、r4 读反了 :before 的方向。
- [doc-modal] 收购的模态 conceiver: 新时代集团 :partial-affirmative 收购 (wrong, 1 of 5 runs). 宣布的内容可以以宣布事件为 conceiver（abridged 5.2 报道内容），训练数据 chinese_umr-0002 第42句两种都有；作者也把收购当事实陈述（第12句获批）。公司作 conceiver 再给 partial 没有依据。
- [doc-coref] 新时代集团与第2句的共指: 没有共指 (wrong, 1 of 5 runs); 另把 s2 的子公司也连进来 (wrong, 1 of 5 runs). Better: s2 新时代集团 :same-entity 新时代集团. 第2句「新时代集团子公司新时代传媒集团」里有新时代集团（gold s2c5），本句是同一实体，应连到最近的前一处提及（abridged 5.3）。子公司是新时代传媒集团，另一个实体。
- [doc-coref] 中文电视的共指: 连到第9句，另把 name 节点也连上 (acceptable but worse, 1 of 5 runs); 方向写反（本句在前） (acceptable but worse, 1 of 5 runs). 共指连实体节点、不连 name 节点，前一处提及在前（abridged 5.3）。gold 的 s10c 在第10句标成了「加拿大中文电视广播」，但它在 gold 里和第9句的公司是同一条链，本句连它是一致的。
- [doc-coref] 温哥华的共指: 没有共指 (acceptable but worse, 5 of 5 runs). Better: s5 温哥华 :same-entity 温哥华. 温哥华在前文多次出现（第5、7句），系统都没有连。

### Sentence 12: 两项 交易 分别 于 1993 年 10 月 和 12 月  获  CRTC 批准 ，  而  两台 随后 亦  进行 改组 ：  原  属  国泰 电视 的  地区性 电视 牌照 改组 为  城市 电视 ，  而  原属 中文 电视 的  全国性 电视 牌照 则  改组 为  新  时代 电视 。

Reviewer's notes on the annotator's choices:
- [attr] 「两项交易」的量词: 交易 :quant 2，没有 :unit (acceptable but worse, 3 of 5 runs). Better: 交易 :quant 2 :unit 项. 项目规则：量词都保留为 :unit，省掉判 minor。
- [structure] 「分别」「亦」: 两个都没有节点 (acceptable but worse, 5 of 5 runs). Better: 批准 :mod 分别、改组 :mod 亦. 「分别」说明两项交易各在一个月份获批，「亦」表示两台也改组；系统都略去了，丢了一点意思。
- [structure] 「两台随后亦进行改组」的表示: 没有这个总的改组，「两台」没有节点 (acceptable but worse, 2 of 5 runs); 进行-01 :ARG1 (and 改组 改组) (wrong, 1 of 5 runs). 冒号后的两项是对「两台进行改组」的说明，用 :subevent 最贴切，平列加文档级关系也可以。「进行」是轻动词，应直接用改组-01（abridged 2.1：进行访问 → 访问-01）。
- [attr] 「两台」的写法: 台 :quant 2 :unit 两 (wrong, 1 of 5 runs). 「两台」是数词加「台」（这里兼指电视台）；把数词「两」当作 :unit 是错的。
- [role] 「改组为X」的结果: 改组 :ARG2 城市电视/新时代电视 (wrong, 5 of 5 runs). Better: 改组 :end-state 城市电视/新时代电视. PropBank 改组-01 只有 ARG0、ARG1，没有 ARG2（REVIEWER：带了义项没有的论元是错）。训练数据里框架没有结果论元的「X为Y」用 :end-state（chinese_umr-0007 第48句「更改为夕闇岛」、chinese_umr-0005 第29句「篡改为」）。
- [sense] 「原属」的义项和论元: 牌照 :ARG1-of (属-01 :ARG2 公司) (wrong, 3 of 5 runs); 牌照 :ARG1-of (属于-01 :ARG2 公司) (wrong, 1 of 5 runs); 牌照 :poss 公司 (acceptable but worse, 1 of 5 runs). Better: 牌照 :ARG0-of (属-02 :ARG1 公司). PropBank 属-01 是「属于某类」（ARG0 entity predicated、ARG1 predicative），没有 ARG2；属-02 是归属（ARG0 被描述的东西、ARG1 它所属的一方），gold 正确。属于-01 同样是 ARG0 被描述者、ARG1 所属，s3/r5 的 ARG1/ARG2 都错。:poss 丢了「原」的时间意义；s3/r1、r2、r4 的属-01 也没有 :aspect。
- [structure] 「原」: 没有原节点 (acceptable but worse, 3 of 5 runs). Better: 属 :mod 原. 「原属」说明牌照原来属于国泰电视、改组后不再属于，「原」是有意义的修饰。
- [concept] 电视台名的实体类型: 电视台（中文词作类型） (wrong, 2 of 5 runs). 命名实体的类型用英文类型词（abridged 2.1/2.2），「电视台」不是实体类型；company、organization、broadcast 类都可以。s3/r3、s3/r4 从本句起多数电视台名都写成 电视台 类型（全篇如此，之后不再记）。
- [doc-temporal] 两个日期的时间关系: 只连了一个日期 (acceptable but worse, 1 of 5 runs); 两个日期都没有时间关系 (acceptable but worse, 1 of 5 runs). 每个时间表达都要有时间父节点（abridged 5.1）；gold 用 and 节点 :overlap 批准，日期挂在 document-creation-time 下，可以。
- [doc-coref] 两项交易的成员（subset-of）: 没有 (acceptable but worse, 5 of 5 runs). 两项交易是第11句的两笔收购；gold 的第一条用了 s11x4（华裔），应是第一笔收购 s11x7，是变量写错。
- [doc-coref] 两台的成员（subset-of）: 没有 (acceptable but worse, 5 of 5 runs). 两台是中文电视和国泰电视；gold 的 s11c2 是温哥华，应是中文电视 s11c3。
- [doc-coref] 国泰电视、中文电视与第11句的共指: 国泰连第11句但方向反，中文电视跳到第9句 (acceptable but worse, 1 of 5 runs). Better: 连到第11句的同名公司. 本句「原属国泰电视」「原属中文电视」与第11句是同一实体，应连到最近的前一处（abridged 5.3），前一处在前。gold 只有 subset-of，缺 same-entity。
- [doc-coref] 城市电视、新时代电视与前文的共指: 新时代电视连第4句（方向反），城市电视没有 (acceptable but worse, 1 of 5 runs); 城市电视连第1句（方向反），新时代电视没有 (acceptable but worse, 1 of 5 runs); 城市电视连到第6句的「电视」 (wrong, 1 of 5 runs). 改组成的城市电视、新时代电视就是第4、5句提到的两台（gold s5c、s4c）；应连最近的前一处，前一处在前（abridged 5.3）。s3/r4 连到第6句的普通名词「电视」，不是同一实体。
- [doc-coref] CRTC 的共指: 没有 (acceptable but worse, 1 of 5 runs). 第9句的 CRTC 更近，连最近的更好；gold 连第6句也能形成链，差别不大。

### Sentence 13: 改组 后 ， 城市 电视 继续 限于 卑诗省 以内 广播 ，  主要 服务 语言 为  粤语 和  普通话 ，  并  开始 播放 亚洲 电视 的  节目 ，  但  也  会  制作 一些 本地 节目 。

Reviewer's notes on the annotator's choices:
- [sense] 「限于」的义项和论元: 限于-01 :ARG1 广播 :ARG2 以内/卑诗省 (wrong, 2 of 5 runs); 限-01 :ARG1 广播 :ARG2 卑诗省 (acceptable but worse, 1 of 5 runs); 广播 :ARG1-of 限-01，范围只作 :place (acceptable but worse, 1 of 5 runs). PropBank 限于-01：ARG0 theme、ARG1 range；限于-02：ARG0 thing limited、ARG1 theme、ARG2 predicate。gold 和 s3/r1 各按一个义项写对了；限于-01 没有 ARG2，s3/r3、r5 编号错。原词是「限于」，用 限-01 换了词条（限-01 的 ARG1/ARG2 本身对）；s3/r4 的限-01 没有限制范围。
- [structure] 「继续」: :mod 继续（非谓词） (acceptable but worse, 1 of 5 runs); 没有继续节点 (acceptable but worse, 1 of 5 runs). PropBank 有继续-01（ARG1 thing that continues），应作谓词；作 :mod 或省掉都丢了「继续」的事件结构。
- [structure] 「卑诗省以内」: 一个普通概念 卑诗省以内 (wrong, 1 of 5 runs). 卑诗省是地名，应作 province 命名实体（abridged 2.2）；「以内」是方位词，项目规则可建节点。s3/r4 把专名和方位词合成一个普通概念。
- [doc-coref] 「改组后」与第12句改组的共指: 连到第12句第一项具体改组（国泰→城市电视） (acceptable but worse, 1 of 5 runs); 连到第12句总的改组（方向反） (acceptable but worse, 2 of 5 runs); 没有 (acceptable but worse, 1 of 5 runs). 「改组后」指第12句「两台随后亦进行改组」的整体，gold 应连 s12x6，而不是其中一项 s12x10；s3/r1、r4 连对了节点但前一处应在前（abridged 5.3）。
- [concept] 「为」（服务语言为粤语和普通话）: 为-01 :ARG1 :ARG2 (wrong, 1 of 5 runs); 是-01 (wrong, 1 of 5 runs). Better: identity-91. 系词「为/是」不是事件节点，X 为 Y 用 identity-91（abridged 2.1、2.3）；s3/r3 的为-01 还用了框架没有的 ARG2（为-01 只有 ARG0、ARG1）。
- [role] 「服务语言」里服务与语言的关系: 语言 :ARG1-of 服务-01 (wrong, 3 of 5 runs); 语言 :mod 服务（非谓词） (acceptable but worse, 2 of 5 runs). Better: 语言 :medium-of 服务-01. PropBank 服务-01 的 ARG1 是接受服务的一方，语言不是；语言是服务所用的媒介，:medium 合适（UMR 3-2-2 非参与者角色）。
- [concept] 粤语、普通话的表示: 普通概念 粤语、普通话 (acceptable but worse, 1 of 5 runs). 语言名是命名实体，类型 language（abridged 2.2 的类型表）。
- [structure] 「开始」: 播放 :mod 开始（非谓词） (acceptable but worse, 1 of 5 runs). PropBank 开始-01：ARG0 entity described、ARG1 thing started，「开始播放」应以开始-01 为谓词。
- [structure] 「但也会制作」的转折: contrast-01 :ARG1 (and …) :ARG2 制作 (acceptable but worse, 2 of 5 runs); 平列 and，没有转折 (acceptable but worse, 1 of 5 runs). Better: contrast-91 :ARG1 (and …) :ARG2 制作. guideline 3-3（话语关系）：but-91 用 :ARG1、:ARG2 连接两个对比项；gold 的 but-91 只有一个论元，没有和前面的分句相连。英语 contrast-01 不是抽象谓词，应写 contrast-91。
- [attr] 广播、播放的 aspect: 广播 state (acceptable but worse, 1 of 5 runs). 持续的播出可以是 habitual、activity 或 process；广播是过程不是状态（abridged 4.1）。
- [doc-coref] 卑诗省的共指: 没有 (acceptable but worse, 5 of 5 runs). Better: s10 卑诗省 :same-entity 卑诗省. 卑诗省第10句出现过，应连到最近的前一处（abridged 5.3）。

### Sentence 14: 新 时代集团 于 1995 年 计划 将 城市 电视 售予 罗渣士 通讯 集团 ，  以  集中 发展 新  时代 电视 。

Reviewer's notes on the annotator's choices:
- [sense] 「售予」的义项: 售予-01 (wrong, 2 of 5 runs). Better: 售-01 :ARG2 罗渣士. PropBank 没有「售予」，不能编 -01；售-01 的 ARG2 是 entity sold to，「售予X」正好用售-01 表达（否则写 售予-00）。
- [doc-modal] 被计划的「售」的模态: 计划 :partial-affirmative 售 (acceptable but worse, 3 of 5 runs). Better: 计划 :unspecified 售. abridged 5.2：计划、打算一类谓词的补足事件以该谓词为父节点，强度 unspecified（或谓词蕴含的强度）；第16句说这个计划告吹，出售没有发生，gold 写成作者确认的事实是错的。计划并不蕴含「很可能」，partial-affirmative 略差。
- [doc-modal] 目的「发展」的模态: 售 :partial-affirmative 发展 (acceptable but worse, 1 of 5 runs); author :partial-affirmative 集中/发展 (acceptable but worse, 1 of 5 runs); 没有模态 (acceptable but worse, 1 of 5 runs). 目的事件是没有实现的意图，应挂在主事件或 purpose 下，不是作者确认的事实（abridged 5.2：Purpose 从句可用常量 purpose）。
- [doc-temporal] 计划与售的先后: 售没有时间关系 (acceptable but worse, 1 of 5 runs). 计划中的出售在计划之后，应为 (计划 :after 售)（训练数据 chinese_umr-0018 第29句 (计划 :after 被计划事件)）。系统的 :before 方向反，同一习惯，见第11句；s3/r2、r4、r5 另把计划挂在第13句事件下也用了反向的 :before。
- [doc-temporal] 1995年与计划: 日期没有时间关系 (acceptable but worse, 1 of 5 runs). 事件在日期之内用 :contained 更准确，overlap 也可接受；每个时间表达都要有时间父节点（abridged 5.1）。

### Sentence 15: 罗渣士 当时 计划 将 之 从 有线 电视 台 转型 为  地面 广播 频道 ，  并  加入 11 种  语言 的  电视节目 。

Reviewer's notes on the annotator's choices:
- [concept] 代词「之」: 普通概念 之 (wrong, 1 of 5 runs). 代词作 thing（或相应的实体类型）加 :refer-person / :refer-number（abridged 2.4），不能把「之」当概念。
- [sense] 「加入」的义项和论元: 加入-01 :ARG1 电视节目 (wrong, 5 of 5 runs). 「加入11种语言的电视节目」是把节目加进频道：PropBank 加入-02（ARG0 agent、ARG1 theme、ARG2 entity arg0 adds arg1 into），节目是 ARG1。加入-01 是加入组织（joiner、organization joined），义项错；gold 义项对但节目写成了 ARG2。
- [attr] 「11种语言」: language（英文）:quant 11 :unit 种 (acceptable but worse, 1 of 5 runs); 语言 :quant 11，没有 :unit (acceptable but worse, 2 of 5 runs); 种 :quant 11 :mod language (wrong, 1 of 5 runs). Better: 语言 :quant 11 :unit 种. 量词保留为 :unit（项目规则）。普通名词用中文词（abridged 2.1），没有名字的 language 是把实体类型当普通名词用；s3/r3 把量词当中心语，结构颠倒。
- [doc-modal] 被计划的转型、加入的模态: 计划 :partial-affirmative 转型/加入 (acceptable but worse, 3 of 5 runs). Better: 计划 :unspecified 转型/加入. abridged 5.2：计划的内容以计划为父节点、强度 unspecified；这个计划没有实现（第16句告吹），不能写作者确认。partial 没有依据，略差（同第14句）。
- [doc-temporal] 计划与被计划事件的先后: (计划 :overlap 转型/加入) (acceptable but worse, 1 of 5 runs); 被计划事件没有时间关系 (acceptable but worse, 1 of 5 runs). 被计划的事件在计划之后，应写 (计划 :after 转型)（训练数据 chinese_umr-0018 第29句）；系统的 :before 是方向反的习惯，见第11句。
- [doc-coref] 「之」「罗渣士」的共指: 两个都连了，另把本句计划和第14句的计划连成同一事件 (wrong, 1 of 5 runs); 只连了之 (acceptable but worse, 1 of 5 runs); 都没有 (acceptable but worse, 2 of 5 runs). 「之」指第14句的城市电视，罗渣士就是第14句的罗渣士通讯集团（abridged 5.3）。第14句是新时代集团的出售计划，本句是罗渣士自己的计划，不是同一事件。

### Sentence 16: 然而 ， 新 时代 后来 改变 初衷 ， 并于 CRTC 听证会 上  表示 无意 放弃 城市 电视 的  牌照 ，  计划 因此 告吹 。

Reviewer's notes on the annotator's choices:
- [sense] 「告吹」的义项和论元: 告吹-01 :ARG1 计划 (wrong, 3 of 5 runs). Better: 告吹-01 :ARG0 计划. PropBank 有告吹-01，只有 ARG0（theme），不该写 -00；计划是 ARG0，告吹-01 没有 ARG1。
- [structure] 「因此」的因果关系: cause-01 :ARG1 原因 :ARG2 告吹 (wrong, 1 of 5 runs). 新时代表示不放弃牌照，造成计划告吹，是原因（项目规则 :cause）；guideline 3-3 因果关系用 cause-01（ARG0 原因、ARG1 结果）或 :cause。训练数据「因此」却常写 have-reason-91（chinese_umr-0007 第50句），两者冲突，gold 一侧记 open。s3/r2 的 cause-01 原因、结果论元错位，ARG2 不存在。
- [concept] 「无意」: 没有无意，放弃 :polarity - (acceptable but worse, 1 of 5 runs). PropBank 有无意-01（ARG0 entity described、ARG1 thing arg0 doesn't intend to do），用有意-01 加否定也能表达；s3/r1 把「无意放弃」改成「不放弃」，丢了意愿。
- [doc-modal] 无意、放弃的模态: 表示 :unspecified 无意 (acceptable but worse, 1 of 5 runs); 新时代 :partial-negative 放弃 (acceptable but worse, 1 of 5 runs). 「计划」不是说话者，不能作无意的 conceiver；新时代无意放弃牌照，放弃没有发生，不能是作者确认的 full-affirmative（abridged 5.2：意愿谓词的补足事件挂在谓词下）。gold 同时有 (无意 :unspecified 放弃)，放弃有两个互相矛盾的父节点。gold 还把 (author :full-affirmative 计划) 重复写了四遍。
- [doc-coref] 告吹的计划与第14句的共指: 没有 (acceptable but worse, 2 of 5 runs). 告吹的就是第14句出售城市电视的计划（连带第15句罗渣士的计划），应有共指（abridged 5.3）。gold 的「计划」是名词节点，连事件的方式拿不准，只作提示。
- [doc-coref] CRTC 的共指: 连到第6句 (acceptable but worse, 1 of 5 runs); 没有 (acceptable but worse, 1 of 5 runs). 应连最近的前一处提及（abridged 5.3），第12句就有 CRTC；连得更远也能成链，差别小，不写 fix。

### Sentence 17: 有见于 来自 中国 和 台湾 而 操 普通话 的 移民 逐渐 增加 ，  城市 电视 再度 进行 改革 ，  于  1998 年  6  月  1  日  转型 为  一个 全  普通话 频道 ，  对象 由  讲  粤语 的  香港 移民 转移 为  讲  普通话 的  中国 移民 和  台湾 移民 ，  并  改为 播放 中国 大陆 和  台湾 电视台 制作 的  节目 。

Reviewer's notes on the annotator's choices:
- [structure] 「有见于」的因果关系: 有见于-01 谓词 + :reason (wrong, 1 of 5 runs); 改革 :cause 增加 (acceptable but worse, 1 of 5 runs); cause-01 :ARG0 增加 :ARG1 (and …) (acceptable but worse, 1 of 5 runs); cause-01 :ARG1 增加 :ARG2 (and …) (wrong, 1 of 5 runs). 「有见于移民增加」是城市电视改革给出的依据，是理由（项目规则 :reason），have-reason-91 或 :reason 都合适，:cause 略差。PropBank 没有「有见于」，不能编 -01。cause-01 是 ARG0 原因、ARG1 结果，s3/r2 把原因放在 ARG1、结果放在不存在的 ARG2。
- [structure] 「来自中国和台湾」的挂接: 移民 :ARG1-of (来自-01 :ARG2 中国和台湾) (wrong, 3 of 5 runs); 移民 :source (and 中国 台湾) (acceptable but worse, 2 of 5 runs). 「来自中国和台湾而操普通话的移民」，「来自…」和「操普通话」是并列的两个定语，都修饰移民；gold 把来自当成「操」的理由。PropBank 来自-01：ARG0 entity described（移民）、ARG1 source（中国、台湾），系统的 ARG1/ARG2 编号错；用 :source 意思在但没用框架。
- [structure] 「改革」: 进行-01 :ARG1 改革（名词） (wrong, 1 of 5 runs). PropBank 改革-01：ARG0 cause/agent、ARG1 theme，城市电视改革自身，作 ARG0 或 ARG1 都说得通。「进行」是轻动词，应直接用改革-01（abridged 2.1）。
- [attr] 「一个全普通话频道」的量词: 频道 :quant 1，没有 :unit (acceptable but worse, 3 of 5 runs). Better: 频道 :quant 1 :unit 个. 项目规则：量词都保留为 :unit。
- [structure] 「改为播放」: 改为-01 :ARG1 播放 (wrong, 2 of 5 runs); 改-01 :ARG1 播放 (wrong, 1 of 5 runs); 只有播放，没有改为 (acceptable but worse, 2 of 5 runs). Better: 改为-01 :ARG2 播放. PropBank 改为-01：ARG1 thing changed、ARG2 changing to；改为播放的新节目是变成的状态，应是 ARG2（改-01 同样是 ARG2 entity arg1 is changed into）。省掉改为丢了「改变」的意思。
- [concept] 「中国大陆」「台湾」作地点: 中国大陆 作普通概念 (acceptable but worse, 5 of 5 runs). 中国大陆是地名，应作命名实体（abridged 2.2：专名整体作命名实体），不是普通概念；系统里台湾也有时写成普通概念（s3/r1、r4）。
- [concept] 「普通话」等语言名: 普通概念 普通话、粤语 (acceptable but worse, 1 of 5 runs). 语言名作 language 命名实体（abridged 2.2），s3/r4 第13句起就这样写（全篇如此）。
- [doc-coref] 句内共指写成 :coref: 句内重复提及用三元组 :same-entity (acceptable but worse, 1 of 5 runs). abridged 5.3：同一句里的共指用重入（一个变量），不写 :coref 三元组。
- [doc-temporal] 日期与转型: 日期没有时间关系 (acceptable but worse, 1 of 5 runs). Better: (date :contained 转型). abridged 5.1：有时间表达时它是事件的参照时间（父节点），(date :contained 事件)；gold 把日期写成转型的子节点。
- [doc-temporal] 增加与改革等的先后: 增加没有时间关系 (acceptable but worse, 1 of 5 runs). 移民增加在改革之前，gold 对。s3/r1 的 :before 方向反（同一习惯，见第11句）。s3/r2 另有 (document-creation-time :after 转型)，把 1998 年的转型放到文档时间之后，是错的。

### Sentence 18: 粤语 香港 移民 的 电视 市场 则 由 新 时代 电视 顶替 ，  而  小  部分 香港 亚洲 电视 的  节目 亦  掉  往  新  时代 电视 播放 。

Reviewer's notes on the annotator's choices:
- [role] 「顶替」中新时代电视的角色: 顶替-01 :ARG0 新时代电视 (wrong, 3 of 5 runs). Better: 顶替-01 :ARG1 新时代电视. PropBank 顶替-01：ARG0 inducer、ARG1 replacer、ARG2 party replaced。「由新时代电视顶替」，新时代电视是顶替者 ARG1，不是促成者 ARG0。
- [role] 「电视市场」与被顶替方: 顶替 :ARG2 市场 (acceptable but worse, 1 of 5 runs); 顶替 :ARG1 市场 (wrong, 3 of 5 runs). Better: 顶替 :ARG2 城市电视，市场作 :place. 顶替-01 的 ARG2 是被顶替的一方，句意是新时代电视在这个市场里顶替了城市电视（上一句城市电视改为普通话）；市场不是被顶替者，ARG1（顶替者）更不对。s3/r1 补出城市电视最贴切。
- [sense] 「掉往」（调往）的义项: 掉-01 (wrong, 2 of 5 runs); 调-01 :ARG2 新时代电视 (wrong, 1 of 5 runs); 掉往-01 :ARG2 播放 (wrong, 1 of 5 runs); 没有这个事件，只有播放 (acceptable but worse, 1 of 5 runs). Better: 调往-01 :ARG1 节目 :ARG2 新时代电视. 「掉往」是「调往」的错字，PropBank 调往-01：ARG1 被调的东西、ARG2 destination。掉-01 是丢失（entity described / entity drops），调-01 是调整，都没有目的地论元；PropBank 没有「掉往」，不能编 -01，目的地也不是播放。
- [structure] 新时代电视的第二次提及: 另建节点，再用句内 :coref 相连 (acceptable but worse, 1 of 5 runs). Better: 重入同一个节点. abridged 5.3：同一句里的共指用重入，不写 :coref 三元组。
- [role] 市场的领有者写 :poss: :poss (acceptable but worse, 2 of 5 runs). 按发布数据写 :possessor（Conventions）。s3/r3 全篇如此，见第11句；s3/r4、r5 只在本句。
- [doc-coref] 亚洲电视的共指: 没有 (acceptable but worse, 5 of 5 runs). Better: 连到第13句的亚洲电视. 第13句「播放亚洲电视的节目」与本句的香港亚洲电视是同一实体（abridged 5.3）。

### Sentence 19: 城市 电视 于 2000 年 向 CRTC 申请 将 其  牌照 从  地区性 收费 电视 改为 全国性 收费 电视 。

Reviewer's notes on the annotator's choices:
- [sense] 「改为」的义项: 改-01 (acceptable but worse, 3 of 5 runs); 改变-01 (acceptable but worse, 1 of 5 runs). Better: 改为-01. 原词是「改为」，PropBank 有改为-01（ARG0 agent、ARG1 thing changed、ARG2 changing to），不必换成别的词条。
- [role] 原来的牌照类型（从地区性收费电视）: :ARG3 地区性收费电视 (wrong, 5 of 5 runs). Better: 改为 :source 地区性收费电视. PropBank 改为-01、改-01、改变-01 都只有 ARG0–ARG2，没有 ARG3（REVIEWER：带了义项没有的论元是错）；「从…」的原状态框架里没有论元，用 :source。
- [doc-modal] 被申请的「改为」的模态: author :full-affirmative 改为 (wrong, 2 of 5 runs); 改为没有模态 (acceptable but worse, 1 of 5 runs). Better: 申请 :unspecified 改. 申请的内容在申请时还没有实现（第20句 2001 年才获批），是申请事件下的未然事件（abridged 5.2：补足事件以谓词为父节点，unspecified）。
- [doc-temporal] 申请与改为的先后: 改为没有时间关系 (acceptable but worse, 3 of 5 runs). 申请的改变在申请之后，应写 (申请 :after 改为)；系统的 :before 方向反，同一习惯，见第11句。
- [doc-coref] 城市电视的共指: 连到第1句，方向反 (acceptable but worse, 1 of 5 runs). 应连最近的前一处（abridged 5.3）；第17句就有城市电视（gold s17c3），gold 跳过了它，但链条仍然连通，只作提示。

### Sentence 20: 申请 于 2001 年 5 月 获批 ， 城市 电视 亦  于  同年 秋季 开始 全国 播放 。

Reviewer's notes on the annotator's choices:
- [sense] 「获批」的义项: 获批-01 (wrong, 2 of 5 runs). PropBank 没有「获批」，不能编 -01；批-01（ARG0 agent、ARG1 entity given permission）或批准-01（ARG0 agent、ARG1 theme）都能表达「申请获批」。
- [doc-coref] 申请与第19句的共指: 方向反（本句在前） (acceptable but worse, 2 of 5 runs); 另连到第9句世界电视的申请 (wrong, 1 of 5 runs); 没有 (acceptable but worse, 1 of 5 runs). Better: s19 申请 :same-event 申请. 获批的是第19句城市电视 2000 年的申请；前一处在前（abridged 5.3）。第9句是 1983 年世界电视的另一次申请，不是同一事件。
- [structure] 「开始全国播放」: 播放 :mod 开始 (acceptable but worse, 1 of 5 runs). 同第13句：PropBank 开始-01（ARG1 thing started）应作谓词。
- [concept] 「同年秋季」: 秋季 :mod 同年（普通概念） (acceptable but worse, 2 of 5 runs). 「同年」指 2001 年，日期用 date-entity，季节用 :season（abridged 2.2、guideline 3-2-2-1）；写成普通概念丢了年份。
- [structure] 「亦」: 没有亦 (acceptable but worse, 3 of 5 runs). 「亦」是原文的副词，系统常把它略去（第12、18、20句）。
- [doc-modal] 播放的模态: 播放没有模态 (acceptable but worse, 2 of 5 runs). 每个事件都要有模态父节点（abridged 5.2）；开始播放已经发生，播放是作者断言的事实。

### Sentence 21: 该台 的 加西 温哥华 总部 于 2006 年 2 月  联同 新  时代 电视 从  温哥华 市  百老汇 西街 的  旧址 迁至 同属 新  时代 集团 的  列治文 时代坊 商场 ，  全面 采用 了  数码制式 的  摄影 用具 。

Reviewer's notes on the annotator's choices:
- [structure] 整句有没有有效的图: 没有有效标注（empty） (wrong, 1 of 5 runs). Better: 有有效的图. r4 第 21 句输出 (s21x0 / empty)，文档级也是空的，整句没有标注。下面各条把 r4 归为"没有有效标注"，记 open，不重复计错。
- [sense] 「迁至」的义项: 迁-01 (acceptable but worse, 4 of 5 runs). Better: 迁至-01. PropBank 有 迁至-01（ARG1 entity moved，ARG2 location moved to），「迁至」在这里是一个词（第 22 词），应按原词取 迁至-01。迁-01 论元相同，意思没丢，算略差。
- [structure] 「同属新时代集团」挂在哪、义项与论元: 商场 :ARG1-of (属-01 :ARG2 集团) (wrong, 1 of 5 runs); 商场 :ARG1-of (同属-01 :ARG2 集团) (wrong, 1 of 5 runs); 商场 :ARG1-of (属于-01 :ARG2 集团) (wrong, 1 of 5 runs); 商场 :possessor 集团（不建谓词） (acceptable but worse, 1 of 5 runs). 「同属新时代集团的」是「列治文时代坊商场」的定语，被领属的是商场，gold 挂到了伴随者新时代电视上。PropBank 属-02：ARG0 是领有者（国内贸易部所属…），ARG1 是归属物，所以应为 (商场 :ARG1-of (属-02 :ARG0 集团))；属-01 是判断义，没有 ARG2；同属 不在 PropBank，应写 同属-00；属于-01 的归属物是 ARG0、所属是 ARG1，r5 的 ARG1/ARG2 都错。
- [role] 「从…旧址」的角色: 迁-01 :ARG3 旧址 (wrong, 1 of 5 runs). Better: 迁 :source 旧址. PropBank 迁-01 / 迁至-01 只有 ARG0、ARG1、ARG2（终点），没有 ARG3；起点没有核心论元，用 :source。
- [role] 「联同新时代电视」的表示: 迁 :accompanier 新时代电视 (acceptable but worse, 1 of 5 runs); 总部 :ARG1-of (联同-01 :ARG2 新时代电视) (wrong, 1 of 5 runs). Better: 迁 :companion 新时代电视. 「联同」是介词性的"连同"，UMR 用非论元角色 :companion（guideline 角色表）；:accompanier 是 AMR 的旧名，UMR 角色表里没有。联同 不在 PropBank，r3 编了 联同-01 并把总部当 ARG1，错。
- [structure] 「加西温哥华总部」的处所: 总部 :mod 加西 :mod (city 温哥华) (acceptable but worse, 2 of 5 runs); 一个普通概念 加西温哥华 (wrong, 2 of 5 runs). Better: 总部 :place (city 温哥华 :place (country-region 加西)). 「加西」（加拿大西部）和「温哥华」是两个地名，温哥华在加西之内；总部所在地用 :place（规则：地点用 :place）。r3、r5 把两个专名并成一个普通概念，丢了命名实体；r1、r2 用 :mod 挂地名，略差。
- [role] 领属角色的写法: :poss（旧名） (acceptable but worse, 1 of 5 runs). Better: :possessor. 规则：拼写按发布数据用 :possessor。r3 全篇都写 :poss（约 24 处），只在这里记一次。
- [concept] 「列治文时代坊商场」的实体类型: 商场 作类型，名字含「商场」 (acceptable but worse, 1 of 5 runs); 商场 作类型 :name "列治文" "时代坊" (acceptable but worse, 3 of 5 runs). Better: building :name "列治文" "时代坊" "商场". 实体类型应取 guideline 命名实体类型表（facility 类下有 building、market），不用中文普通名词「商场」作类型。
- [concept] 「温哥华市百老汇西街」的类型与切分: street :name "百老汇" "西街" (acceptable but worse, 1 of 5 runs); street :name "百老汇西街"（名字不切词） (acceptable but worse, 1 of 5 runs); 街 :name "百老汇" "西街" :part-of city (acceptable but worse, 1 of 5 runs); 一个 street，名字 "温哥华" "市" "百老汇" "西街" (wrong, 1 of 5 runs). Better: road :name "百老汇" "西街" :place (city 温哥华市). guideline 类型表 facility 类下是 road，没有 street；中文类型词「街」也不在表里。r3 把城市并进街名，丢了 温哥华市 这个实体，错。r2 名字没有按词切成 op1/op2（guideline 2.2），略差。
- [role] 「全面」修饰「采用」的角色: 采用 :mod 全面 (acceptable but worse, 2 of 5 runs); 采用 :degree 全面 (acceptable but worse, 1 of 5 runs). Better: 采用 :manner 全面. 说明里定的原则是副词性修饰事件用 :manner；:degree 只用于性质的强化或弱化（规则），不用于修饰动作。但训练数据「全面」两处都写 :mod（chinese_umr-0013 第 5 句 停驶 :mod 全面，0010 第 10 句 推进 :mod 全面），所以只给 low。
- [doc-temporal] 日期本身在时间树里的父节点: 日期没有父节点 (acceptable but worse, 3 of 5 runs). guideline 4-2-1-2：时间表达都要进时间上层结构，绝对日期挂 root；规则接受挂到元节点的几种写法。r2、r3、r5 全篇的日期都不挂父节点（训练数据也常省），只在这里记一次。
- [doc-temporal] 事件先后 :before 的方向: (迁 :before 采用)：读作"迁在采用之前" (wrong, 1 of 5 runs); (第20句 开始 :before 迁)：读作"开始在迁之前" (wrong, 2 of 5 runs). guideline 4-2-2-1："labels characterize the relation from child to parent"，(A :before B) 是 B 在 A 之前。r1 的三元组说的是采用早于迁址，r2、r5 说的是 2006 年的迁址早于 2001 年的「开始全国播放」，都反了；应写 (开始 :after 迁)。这是系统全篇的习惯（事件间 :before 都按"父在前"写），见小结。
- [doc-coref] 新时代电视、新时代集团的跨句共指: 只连新时代电视（第 18 句），集团没连 (acceptable but worse, 1 of 5 runs); 连到较远的第 12、14 句 (acceptable but worse, 1 of 5 runs); 新时代电视倒着连到第 12 句，集团没连 (acceptable but worse, 1 of 5 runs). Better: 连到最近的提及（第 18 句电视、第 16 句集团）. guideline 5.3：每个提及连到最近的前一个提及，前面的在前。r3 方向写反并且漏了集团。

### Sentence 22: 城市 电视 于 2008 年 以 「 Talentvision II 」  的  名义 向  CRTC 申请 创办 另  一条 全国性 收费 电视 频道 ，  主要 播放 普通话 节目 。

Reviewer's notes on the annotator's choices:
- [role] 「以…的名义」的角色与挂接: 不建名义，名字挂在 频道 上 (acceptable but worse, 2 of 5 runs). Better: 申请 :manner 名义. 「以 X 的名义」是修饰「申请」的介词短语，副词性修饰事件用 :manner。r1、r3 把名字给了要创办的频道（第 24 句「重新申请创办「Talentvision II」」可佐证这是频道名），意思通，但丢了「名义」。
- [attr] 「另一条」的量词: 一个概念 另一条，没有 :quant / :unit (acceptable but worse, 1 of 5 runs); 一个概念 另一 (acceptable but worse, 1 of 5 runs); 只有 另，没有数和量词 (acceptable but worse, 1 of 5 runs). Better: 频道 :mod 另 :quant 1 :unit 条. 规则：量词都保留为 :unit（名词 :quant N :unit 量词）。「另一条」= 另 + 一 + 条，应为 频道 :mod 另 :quant 1 :unit 条。
- [structure] 「收费电视」的切分: 只有 收费，丢了「电视」 (acceptable but worse, 1 of 5 runs). 「收费电视」是固定说法，整体作一个概念或拆成两层修饰都可以；r3 丢了「电视」。
- [role] 「普通话节目」的关系: 节目 :mod 普通话（不作命名实体） (acceptable but worse, 1 of 5 runs). 语言名按 guideline 2.2 作 language 命名实体；用 :medium 还是 :mod 都说得通。r4 把普通话写成普通概念，略差。
- [concept] 「城市电视」的实体类型: 中文普通名词 电视台 作类型 (acceptable but worse, 2 of 5 runs). 命名实体类型应取 guideline 类型表（organization 及其下位 company 等），不用中文普通名词「电视台」作类型。r3、r4 全篇都这样写城市电视、新时代电视，只在这里记一次。
- [doc-modal] 「创办」的 modal: (author :full-affirmative 创办) (wrong, 2 of 5 runs). Better: (申请 :unspecified 创办). 创办是「申请」的内容，并未实现（第 23 句：一直未能启播）；guideline 5.2 / 4-3-1-2：补足语谓词下的事件挂在该谓词下，强度 unspecified。
- [doc-modal] 「播放」的 modal: (author :full-affirmative 播放) (wrong, 5 of 5 runs). 「主要播放普通话节目」是申请中新频道的计划内容，第 23 句说该频道一直未能启播，作者并没有断言播放发生。应挂在申请（或创办）下，unspecified。6 份都错。
- [doc-temporal] 2008 年相对文档时间: 日期没有父节点（r4 本段第一次） (acceptable but worse, 1 of 5 runs). Better: (root :contained 2008年). 文档写到 2013 年以后的事（第 24 句），2008 年在文档时间之前，:overlap 错；规则接受 (document-creation-time :before 日期) 或挂 root。r2–r5 不给日期父节点是同一习惯，见第 21 句。
- [doc-temporal] 2008 年与「申请」的关系: 申请没有时间父节点 (acceptable but worse, 1 of 5 runs). Better: (日期 :contained 申请). 申请发生在 2008 年之内，用 :contained 更精确（guideline 4-2-2-1）；r4 只写了申请与创办、播放的关系，申请本身没有挂到日期或元节点上。
- [doc-temporal] 申请与创办、播放的先后: 申请与创办、播放之间没有关系 (acceptable but worse, 2 of 5 runs); (申请 :overlap 创办) (acceptable but worse, 1 of 5 runs); (申请 :before 创办)：读作"申请在创办之前"（r4 在本段第一次出现） (wrong, 1 of 5 runs). guideline 4-2-2-1-1：补足语谓词作补足语的参照时间，计划中的事件在其后，写 (申请 :after 创办)（参照 want :after cook 的例子）。r4、r5 的 (申请 :before 创办) 按定义是"创办在申请之前"，方向反（同第 21 句的系统习惯）；r5 还有 (创办 :before 播放)、r2/r5 还有 (第21句 迁 :before 申请)，同样反。
- [doc-coref] 城市电视、CRTC 的跨句共指: 城市电视连到第 1 句，CRTC 没连 (acceptable but worse, 1 of 5 runs); 只连 CRTC，城市电视没连 (acceptable but worse, 1 of 5 runs). Better: 城市电视连第 20/21 句，CRTC 连第 19 句. guideline 5.3：每个提及连到最近的前一个提及；r3 连到第 1 句并且方向是后者在前，r4 漏了城市电视。

### Sentence 23: 申请 曾于 2009 年 获批 ， 但 该台 一直 未能 启播 。

Reviewer's notes on the annotator's choices:
- [concept] 「但」的连接概念: contrast-91 (acceptable but worse, 1 of 5 runs); contrast-01（AMR 英文框架） (acceptable but worse, 4 of 5 runs). Better: but-91. guideline 3-1-6 / 精简版 2.5：但是、却、然而用 but-91；训练数据「但」绝大多数是 but-91（0007、0005、0008、0014 多处）。contrast-01 是英文 PropBank 框架，不是 UMR 的抽象概念；r1、r3、r4、r5 全篇都这样写，见小结。
- [sense] 「获批」的义项: 获批-01（PropBank 没有） (wrong, 2 of 5 runs); 换成 批准-01 (acceptable but worse, 3 of 5 runs). Better: 拆出 批-01 :ARG1 申请. 「获批」不在 PropBank，整词应写 获批-00；r1、r4 编了 -01，错。gold 取 批-01（ARG1 entity given permission to），论元合适；系统改用近义的 批准-01 不按原词（guideline 2.1），略差。
- [sense] 「启播」的义项与切分: 启播-01（PropBank 没有） (wrong, 5 of 5 runs). 「启播」是一个词，不在 PropBank，按 guideline 2.1 写 启播-00。系统编了 -01，错。gold 把一个词拆成 启-01（"打开"义，ARG1 thing arg0 opens up）+ 播-01，两个节点对齐到同一个词，且 启-01 的 ARG1 并不是被打开的东西。
- [role] 「启播」的参与者: 启播 :ARG1 电视台 (acceptable but worse, 2 of 5 runs). Better: 启播 :ARG0 该台. 启播 不在 PropBank，参照 播-01（ARG0 broadcaster），开播的台是施事 ARG0；ARG1 略差。
- [doc-coref] 「该台」指谁: 该台 = 城市电视（连第 22 句城市电视） (wrong, 2 of 5 runs); 没有连 (acceptable but worse, 2 of 5 runs). Better: 该台 = 第 22 句申请创办的频道. 「申请获批，但该台一直未能启播」：未能启播的是申请创办的新频道（Talentvision II，第 24 句 2013 年才以「城市2高清台」启播），城市电视本身早已在播（第 20 句）。该台应与第 22 句的「频道」共指。
- [doc-coref] 「申请」与第 22 句的共指: (申请 :same-event 第22句申请)，后者在前 (acceptable but worse, 3 of 5 runs); (申请 :same-entity 第22句申请) (acceptable but worse, 1 of 5 runs). Better: (第22句申请 :same-event 申请). guideline 5.3：前面的提及在前；事件之间用 :same-event。
- [doc-temporal] 2009 年与「获批」的关系: 获批没有挂到日期上 (acceptable but worse, 1 of 5 runs). Better: (日期 :contained 获批). 获批发生在 2009 年之内，用 :contained（guideline 4-2-2-1 步骤 1）。
- [doc-temporal] 获批与未能启播的先后: (获批 :overlap 启播) (acceptable but worse, 1 of 5 runs). 「未能启播」的状态从获批以后一直持续，应是 (获批 :after 启播)。(A :before B) 按 guideline 4-2-2-1 是"B 在 A 之前"，r1、r2、r5 写反，与第 21 句是同一习惯，记 open。

### Sentence 24: 新 时代 遂 于 2012 年 6 月 重新 申请 创办 「  Talentvision II 」  ，  并于 2013 年  2  月  再次 获批 ，  再  于  同年 5  月  23 日以 「  城市 2  高清 台  」  的  名义 启播 。

Reviewer's notes on the annotator's choices:
- [structure] 「获批」的 ARG1: 另建一个 申请-01 节点作 ARG1 (acceptable but worse, 3 of 5 runs). Better: 批准 :ARG1 申请（重入本句的申请）. PropBank 批-01 ARG1 是 entity given permission to；获批的就是本句前一分句的「重新申请」，句内应重入同一节点（guideline 5.3：句内共指用重入），r1、r2、r5 另建节点再用 coref 连，略差。
- [structure] 谁「启播」: 另建「城市2高清台」频道作参与者 (acceptable but worse, 2 of 5 runs). Better: 启播 :ARG0 Talentvision II 频道（重入）. 开播的是前面申请创办的 Talentvision II 频道（以「城市2高清台」为名），句内已有该节点，应重入作启播的参与者（参照 播-01 ARG0 broadcaster）。r1、r3 另建一个以新名字命名的频道节点，丢了「名义」，再用 coref 连回去，略差。
- [role] 「以…的名义启播」的角色: 不建名义（名字给了另建的频道） (acceptable but worse, 2 of 5 runs). Better: 启播 :manner 名义. 同第 22 句：「以 X 的名义」是状语，副词性修饰事件用 :manner。
- [structure] 「再于同年…启播」的「再」: 启播 :mod 再 (acceptable but worse, 2 of 5 runs). Better: 不建节点. 这里的「再」表示接续（然后），不是重复；先后关系由时间标注表达，:mod 再 容易误读为"再次启播"。
- [doc-modal] 「创办」的 modal: 创办没有 modal 父节点 (acceptable but worse, 3 of 5 runs). Better: (申请 :unspecified 创办). 创办是申请的内容，按 guideline 4-3-1-2 挂在申请下，强度 unspecified；不挂就是漏标（每个事件都要有 modal 父节点）。
- [doc-temporal] 三个日期与事件的关系: 事件没有挂到日期上 (acceptable but worse, 1 of 5 runs). Better: (日期 :contained 事件). 申请、获批、启播各自发生在所给日期之内，用 :contained（guideline 4-2-2-1 步骤 1）。r4 全句没有日期–事件关系。
- [doc-temporal] 已然的启播相对文档时间: (document-creation-time :after 启播) (wrong, 4 of 5 runs); (document-creation-time :after 2013年5月23日) (wrong, 1 of 5 runs). Better: 不写（由日期定位）. guideline 5.1 / 4-2-2-1：(document-creation-time :after X) 是"X 在文档时间之后"，即将来；2013 年的启播是过去的事，应为 (document-creation-time :before …)。这是系统全篇的习惯：过去事件一律写成 DCT :after（与事件间 :before 的反向是同一个误解），见小结。
- [doc-coref] 「重新申请」与前面的申请是否同一事件: (重新申请 :same-event 第22句申请) (wrong, 1 of 5 runs); (第23句申请 :same-event 本句获批的申请) (wrong, 1 of 5 runs). Better: 不连. 2012 年的「重新申请」是另一次申请，不是第 22 句 2008 年的申请；本句 2013 年获批的是重新申请，不是第 23 句 2009 年获批的那次。
- [doc-coref] 新时代的跨句共指: 连第 16 句 (acceptable but worse, 3 of 5 runs); 倒着连第 14 句 (acceptable but worse, 1 of 5 runs); 连第 2 句 (acceptable but worse, 1 of 5 runs). Better: 连第 21 句新时代集团（最近）. guideline 5.3：连到最近的前一个提及（第 21 句的新时代集团）。

### Sentence 25: 城市 电视 的 主 频道 现时 每天 重点 播放 三套 电视剧 ，  主要 购自 中国 大陆 和  台湾 。

Reviewer's notes on the annotator's choices:
- [sense] 「购自」的义项: 购-01 (acceptable but worse, 5 of 5 runs). Better: 购自-01. PropBank 有 购自-01（ARG0 buyer，ARG1 thing bought，ARG2 place bought from），「购自」在这里是一个词（第 14 词），应按原词取 购自-01。
- [role] 购买来源的角色: 购 :source (and 中国大陆 台湾) (acceptable but worse, 3 of 5 runs). Better: 购 :ARG2 (and 中国大陆 台湾). PropBank 购自-01 ARG2 是购买来源（place arg1 is bought from），购-01 ARG2 是 seller；核心论元能表达时不用 :source。
- [concept] 「中国大陆」「台湾」的命名实体: 中国大陆 普通概念，台湾 作 country 命名实体 (acceptable but worse, 2 of 5 runs); 中国大陆 普通概念，台湾 作 place 命名实体 (acceptable but worse, 1 of 5 runs); 两个都是普通概念 (wrong, 2 of 5 runs). Better: 两个都是 country-region 命名实体. 地名是专名，按 guideline 2.2 作命名实体，名字按词切分（"中国" "大陆"），类型取类型表（region 类有 country-region）；place 不在类型表里。
- [attr] 「三套」的量词: 电视剧 :quant 3，丢了量词 (acceptable but worse, 3 of 5 runs). Better: 电视剧 :quant 3 :unit 套. 规则：量词都保留为 :unit。
- [structure] 「每天」的表示: :frequency (rate-entity-91 :ARG1 1 :ARG2 每天) (acceptable but worse, 1 of 5 runs); :frequency (rate-entity-91 :ARG4 (temporal-quantity 1 天)) (acceptable but worse, 1 of 5 runs). 训练数据有 :frequency 每天 的先例（chinese_umr-0005 第 17 句）；按 AMR 的 rate-entity-91 写法每天是 :ARG3 (temporal-quantity :quant 1 :unit 天)。r1 把「每天」整个放进 ARG2，r4 用 ARG4，都不合 rate-entity-91 的论元。
- [role] 「重点播放」的「重点」: 播放 :mod 重点 (acceptable but worse, 3 of 5 runs); 电视剧 :mod 重点 (acceptable but worse, 1 of 5 runs); 播放 :degree 重点 (acceptable but worse, 1 of 5 runs). 「重点」修饰动作「播放」（着重地播），副词性修饰事件用 :manner（说明中的原则）；:degree 只用于性质的强化或弱化（规则）。训练数据对这类副词多用 :mod，所以只给 low。
- [doc-temporal] 「购自」的时间: 没有时间父节点 (acceptable but worse, 1 of 5 runs). Better: (播放 :before 购自)：购入在播放之前. 按 guideline 4-2-2-1，gold 的 (播放 :before 购自) 是"购入早于播放"，合理。r5 的写法按定义是"播放早于购入"，是系统 :before 方向的同一习惯。r3 购没有时间父节点。
- [doc-coref] 「城市电视」的跨句共指: 连到第 23 句的「该台」 (wrong, 1 of 5 runs); 倒着连到第 1 句 (acceptable but worse, 1 of 5 runs). Better: 连到第 22 句城市电视. 第 23 句的「该台」是未能启播的新频道，不是城市电视（见第 23 句条目）；城市电视最近的提及是第 22 句。
- [doc-coref] 「主频道」的跨句共指: 没有连 (acceptable but worse, 1 of 5 runs). Better: 连到第 3 句的主频道. 第 3 句已提到城市电视的「主频道（1台）」，本句「城市电视的主频道」与之共指（guideline 5.3）。r1 另加了 (主频道 :subset-of 第3句两条频道)，也对。

### Sentence 26: 为 配合 该台 以 单一 讯号 覆盖 东西 两岸 ，  该  三  文件 电视剧 亦  每天 播放 两次 以  迎合 不同 时区 的  观众 。

Reviewer's notes on the annotator's choices:
- [structure] 「每天播放两次」的 rate-entity-91: :ARG1 2 :ARG2 每天（普通概念） (acceptable but worse, 1 of 5 runs); :ARG3 (temporal-quantity 1 天) :ARG4 2 (wrong, 1 of 5 runs); :ARG3 2 :ARG4 (temporal-quantity 1 天) (wrong, 1 of 5 runs). rate-entity-91（AMR）：ARG1 是次数，ARG2 是每多少单位（twice a day = :ARG1 2 :ARG2 (1 天)），ARG3 是间隔，ARG4 是日期类实体（guideline 3-2-2-3 例 1e 的 :ARG4 date-entity）。次数 2 不能放在 ARG3 / ARG4。
- [attr] 「该三文件电视剧」的量词与指示词: :quant 3 :mod 该（无量词） (acceptable but worse, 2 of 5 runs); :quant 3（无量词、无「该」） (acceptable but worse, 1 of 5 runs). 原文「三 文件」是分词 / 录入噪音（上一句是「三套」），量词写 件、文件 或按上句写 套 都可接受；按规则量词保留为 :unit，丢掉量词略差。指示词「该」可作 :mod，也可只靠共指表达。
- [structure] 「配合」的论元: 配合 :ARG0 电视剧 :ARG1 覆盖 (acceptable but worse, 1 of 5 runs). Better: 配合 :ARG1 覆盖（覆盖 :ARG0 该台）. 「为配合该台以单一讯号覆盖东西两岸」：要配合的是"该台用一个讯号覆盖两岸"这件事，不是该台本身；PropBank 配合-01 ARG1 entity cooperate with。r2 让电视剧作配合的 ARG0，没有依据。
- [role] 「以单一讯号」的角色: 覆盖 :manner 讯号 (acceptable but worse, 3 of 5 runs). 「以 X」表示凭借的手段，讯号是工具 / 媒介，:instrument、:medium 都说得通；:manner 是方式，不如前两者。
- [doc-modal] 目的事件（配合、迎合）的 modal: (author :partial-affirmative 配合 / 迎合) (acceptable but worse, 1 of 5 runs); 配合 没有 modal，迎合 full-affirmative (acceptable but worse, 1 of 5 runs). Better: (author :full-affirmative 配合 / 迎合). 训练数据里 :purpose 事件大多是 (author :full-affirmative …)（11 处，另有 unspecified 2 处、partial 2 处）；partial-affirmative 表示推测，这里没有依据。r4 漏了配合。
- [doc-modal] 「覆盖」的 modal: (author :partial-affirmative 覆盖) (wrong, 1 of 5 runs); 覆盖没有 modal 父节点 (acceptable but worse, 3 of 5 runs). Better: (author :full-affirmative 覆盖). 该台以单一讯号覆盖两岸是作者陈述的事实（第 4 句也说两条频道全国用同一讯号播放），应 full-affirmative；每个事件都要有 modal 父节点。
- [doc-coref] 「该台」的跨句共指: 倒着连到第 1 句 (acceptable but worse, 1 of 5 runs); 没有连 (acceptable but worse, 1 of 5 runs). Better: 连第 25 句城市电视. guideline 5.3：连到最近的前一个提及。

### Sentence 27: 除了 从 海外 购入 电视 节目 外 ， 城市 电视 亦  有  自制 电视 节目 以  满足 CRTC 所  定下 的  本地 制作 条款 。

Reviewer's notes on the annotator's choices:
- [role] 「从海外」的角色: 购入 :ARG2 海外 (wrong, 1 of 5 runs); 购-01 :ARG2 海外 (acceptable but worse, 1 of 5 runs). Better: 购入 :source 海外. 「从海外购入」的海外是来源：PropBank 购入-01 只有 ARG0、ARG1，没有 ARG2（r1 错）；没有核心论元时用 :source。r2 改用 购-01（ARG2 seller），不按原词，海外也不是卖方。
- [role] 「满足…条款」的论元: 满足 :ARG0 城市电视 :ARG1 条款 (wrong, 2 of 5 runs); 满足 :ARG0 电视节目 :ARG1 条款 (wrong, 1 of 5 runs). Better: 满足 :ARG0 城市电视 :ARG2 条款. PropBank 满足-01：ARG0 agent，ARG1 things entity satisfied with，ARG2 entity satisfied（例：满足 国内市场的需求 → ARG2）。被满足的条款是 ARG2；满足者是城市电视（目的从句承主句主语），gold 漏了 ARG0。
- [attr] 购入、自制的 aspect: 自制 habitual，购入 performance (acceptable but worse, 1 of 5 runs). Better: habitual. 「城市电视亦有自制电视节目」说的是电视台经常性的做法（现时一贯如此），不是一次完成的事件；guideline 4.1：经常、反复发生的事件用 habitual。
- [doc-modal] 「定下」的 modal: 定下没有 modal 父节点 (acceptable but worse, 4 of 5 runs). Better: (author :full-affirmative 定下). guideline 5.2：每个事件都要有 modal 父节点；关系从句里的事件（CRTC 所定下的）也一样。系统常漏掉修饰性事件的 modal，见小结。
- [doc-coref] CRTC、城市电视的跨句共指: CRTC 没连，城市电视倒着连第 1 句 (acceptable but worse, 1 of 5 runs). Better: CRTC 连第 22 句. guideline 5.3：每个提及连到最近的前一个提及；CRTC 最近的提及在第 22 句。gold 的链仍然正确，只是跳了一环，所以 low。

### Sentence 28: 城市 电视 的 自制 新闻 节目 《 晚间 新闻 》  现时 于  每晚 7  :  30 播放 ，  工作日 节目 长度 为  一  小时 ，  周末 则  为  半小时 ，  并  于  当晚 11 :  30 （  星期六 11 :  40 、  星期日 11 :  50 ）  回放 。

Reviewer's notes on the annotator's choices:
- [attr] 钟点的写法: :time "7:30" / "11:30"（12 小时制，晚间时间错成上午） (acceptable but worse, 2 of 5 runs); :time 19 :30（「:30」成了一个角色，格式错） (wrong, 2 of 5 runs). 训练数据钟点写成概念节点（chinese_umr-0002 第 2 句 h22m33、0016 第 11 句 23h44m），AMR 写字符串 "19:30"，两种都可以。「每晚 7:30」「当晚 11:30」是晚上，写成 "7:30"、"11:30" 就成了上午。r1、r2 把 7:30 拆成 :time 19 和一个不存在的角色 :30，图不合格式。
- [structure] 「每晚 7:30 播放」的频率与时间: :temporal 7:30 + :frequency (rate-entity-91 :ARG4 (1 晚)) (acceptable but worse, 1 of 5 runs); :temporal (date-entity :time 19 :mod 每晚) (acceptable but worse, 1 of 5 runs). rate-entity-91：ARG2 是"每多少单位"，ARG3 是间隔（temporal-quantity），ARG4 是日期类实体（guideline 3-2-2-3 例 1e：every December → :ARG4 (date-entity :month 12)）。gold 把钟点放进 ARG2，应为 ARG4。r4 把间隔放进 ARG4，r1 不用 rate-entity，略差。
- [structure] 《晚间新闻》的类型与「自制」: 节目 作类型 :ARG1-of (自制-01 :ARG0 城市电视) (acceptable but worse, 1 of 5 runs); broadcast-program :mod 自制（非事件）:possessor 城市电视 (acceptable but worse, 1 of 5 runs); 节目 作类型 :mod 自制（非事件）:possessor 城市电视 (acceptable but worse, 2 of 5 runs). 节目名按 guideline 类型表用 show 或 broadcast-program；中文「节目」不是类型。「城市电视的自制新闻节目」里「自制」是定语从句式的动词（PropBank 自制-01 ARG0 agent），按 guideline 2.1 作事件，城市电视是它的 ARG0；写成 :mod 自制 + :possessor 丢了施事关系。
- [concept] 「长度为一小时」的谓词: 为-01 :ARG1 长度 :ARG2 (and 两个时长) (acceptable but worse, 1 of 5 runs); 是-01 :ARG0 长度 :ARG1 时长 (acceptable but worse, 1 of 5 runs). Better: identity-91 :ARG1 长度 :ARG2 时长. 系动词结构按 guideline 2.3 用抽象谓词 identity-91。r3 用 为-01（PropBank 为-01 ARG0 entity being predicated、ARG1 predicative），论元号写成 ARG1/ARG2 不对，还把工作日、周末两个时长并进一个 and；r4 用原文没有的「是」并取 是-01。
- [structure] 回放时间的结构: 三个并列的 :temporal date-entity (acceptable but worse, 1 of 5 runs); 当晚 :op1 date + 回放 :ARG1-of (contrast-01 :ARG2 星期六/日) (wrong, 1 of 5 runs). 括号里是星期六、星期日的例外时间，并列成 and 可以接受。r3 用 contrast-01 让回放作 ARG1，结构没有依据；「当晚」带 :op1 也不合格式。
- [doc-coref] 回放与播放的共指: (回放 :same-event 播放) (wrong, 1 of 5 runs). Better: 不连. 回放是另一次播出，不是同一事件。

### Sentence 29: 节目 于 列治文 时代坊 直播室 制作 ， 主播 由 邱荣 、  叶一滔 和  成松子 轮流 担任 。

Reviewer's notes on the annotator's choices:
- [doc-temporal] 「担任」的时间父节点: 担任没有时间父节点 (acceptable but worse, 2 of 5 runs). guideline 5.1：每个事件都要有时间父节点。

### Sentence 30: 此外 ， 城市 电视 亦 以 卫星 技术 引入 中国 中央 电视台 和  台湾 TVBS 的  新闻节目 ，  于  下列 时间 播出 ：  城市 电视 亦  自制 其它 种类 的  节目 ，  包括 《  在  加  学  英语 》  、  《  城市 大  视界 》  、  《  专家 来  开讲 》  、  《  枫华 博览 》  、  《  都市 有约 》  、  《  新  枫采 》  、  《  家国 纵横 》  和  《  两岸 三地 加国 情  》  。

Reviewer's notes on the annotator's choices:
- [concept] 「台湾 TVBS」的命名实体: organization :name "台湾" "TVBS"（地名并进机构名） (acceptable but worse, 4 of 5 runs). Better: TVBS :place (台湾). 「台湾 TVBS」里「台湾」是所在地，不是机构名称的一部分；应分成两个命名实体（TVBS :place 台湾）。「中国中央电视台」是正式全称，整体作名字或拆出中国都可以。
- [role] 「以卫星技术」的角色: 引入 :manner 技术 (acceptable but worse, 2 of 5 runs). Better: 引入 :instrument 技术. 「以卫星技术引入」表凭借的工具，用 :instrument。
- [doc-coref] 新闻节目的错误共指: (新闻节目 :same-entity 新闻节目)（同一变量连自己） (wrong, 1 of 5 runs); (新闻节目 :same-entity 播出)（实体连事件） (wrong, 1 of 5 runs). Better: 没有这类三元组. r4 写了一个节点和它自己的共指，没有意义；r5 把新闻节目（实体）和播出（事件）标成同一实体。

### Sentence 31: 城市 电视 的 韩语 节目 时段 介乎 10 : 00 和  12 :  00 ，  越南语 节目 则  介乎 01 :  30 和  04 :  00 播放 。

Reviewer's notes on the annotator's choices:
- [role] 「介乎」的论元: 介乎-01 :ARG1 时段 :ARG2 (between/and 两个钟点) (wrong, 4 of 5 runs); 不用 介乎，改成 播放 :temporal (between …) (acceptable but worse, 1 of 5 runs). Better: 介乎-01 :ARG0 时段 :ARG1 (range 10:00 12:00). PropBank 介乎-01：ARG0 entity described，ARG1 entities arg0 lies between；没有 ARG2。系统把时段写成 ARG1、钟点写成 ARG2，两个论元号都错。
- [structure] 越南语节目分句的谓语: 介乎 :ARG1 时段 :ARG2 … :manner 播放 (acceptable but worse, 1 of 5 runs); 播放 :temporal (介乎-01 :ARG2 …) (acceptable but worse, 1 of 5 runs). 「越南语节目则介乎 01:30 和 04:00 播放」可以以介乎为谓语、播放修饰节目，也可以以播放为谓语、时间段作 :temporal。r3 用 :manner 连播放，r4 把一个谓词放在 :temporal 里且没有 ARG0/ARG1，略差。
- [doc-coref] 错误的共指三元组: (date-entity :same-entity 自己) (wrong, 1 of 5 runs); (越南语节目 :subset-of 第28句《晚间新闻》) (wrong, 1 of 5 runs). Better: 没有. r3 把一个日期节点和自己共指；r5 说越南语节目是《晚间新闻》的一部分，没有依据。

## Document zh-0011 (5 runs)

### Sentence 1: 贞孝   节烈   牌坊   为  牌坊   的  一种   ，  是  中国   古代   的  文化   产物   。

Reviewer's notes on the annotator's choices:
- [concept] 系词「为」「是」的概念与论元: 为-01 / 是-01 :ARG0 牌坊 :ARG1 … (acceptable but worse, 1 of 5 runs); 为-03 / 是-01 :ARG0 牌坊 :ARG1 … (acceptable but worse, 1 of 5 runs); 为-01 / 是-01 :ARG1 牌坊 :ARG2 … (wrong, 1 of 5 runs). Better: identity-91 :ARG1 牌坊 :ARG2 …. guideline 2.1 / Part 3-1-1-3：系词（是、为）不是事件，判断句用非动词谓词 identity-91（ARG1 theme，ARG2 equated referent）；中文训练数据判断句 identity-91 有一百多句，是-01 只有 2 句。r1、r2 用了 PropBank 的系词义项，论元按框架（ARG0 entity being predicated / ARG1 predicative）不算硬错，r2 的 为-03 是「被任命为」义，不贴切；r4 给 为-01、是-01 用 ARG1/ARG2，两个框架都没有 ARG2。全篇如此（r1、r2、r4 每个判断句都用 是-01 / 为-01）。
- [attr] 「牌坊的一种」的数量与量词: 种 :mod 牌坊（种作中心词） (acceptable but worse, 1 of 5 runs); 牌坊 :mod (一种) (acceptable but worse, 1 of 5 runs); 牌坊 :quant (一种) (acceptable but worse, 1 of 5 runs). Better: 牌坊 :quant 1 :unit (种). 按项目规则量词保留为 :unit，数目写成数字常量（abridged 2.2 Numbers are written as digits）：牌坊 :quant 1 :unit 种。gold 把「一」写成概念节点；r3、r4 把「一种」整个当一个节点，r2 把「种」当中心词。
- [doc-temporal] 两个判断相对文档时间: document-creation-time :after 第一个判断（将来），第二个没有 (wrong, 1 of 5 runs); :depends-on + :overlap 「是」，「为」没有 (wrong, 1 of 5 runs). Better: document-creation-time :overlap 两个判断. 类属判断是现在成立的状态，:overlap 文档时间（guideline 5.1）。r3 的 :after 表示判断在文档时间之后（将来），反了；r4 给事件用 :depends-on（只用于时间节点之间），且「为」没有时间父节点。
- [doc-coref] 文档级 coref: (牌坊 :same-entity 为-01) (wrong, 1 of 5 runs). Better: 没有 coref. 句内同指用重入，不写 :coref（guideline 5.3）；gold 把实体「产物」写成判断事件的子集，r4 把实体「牌坊」和「为」事件写成同一实体，都没有意义。

### Sentence 2: 贞孝   节烈   牌坊   是  因为   中国   封建   社会   的  贞节   旌表   制度   而  衍生   的  产物   。

Reviewer's notes on the annotator's choices:
- [role] 「因为制度而衍生」：制度的角色: cause-01 :ARG0 制度 :ARG1 衍生（把「因为」谓词化） (acceptable but worse, 1 of 5 runs). abridged 2.5：因为 → :cause；衍生-01 的 ARG0 是生出者，说「制度衍生出产物」也通，两种都接受。r3 把没有谓词化的「因为」建成 cause-01 事件，guideline Part 3-1-1-3 说不谓词化的因果关系不作事件，略差。
- [sense] 「旌表」的概念: 旌表-01（事件） (wrong, 2 of 5 runs); 贞节旌表 合成一个节点 (acceptable but worse, 1 of 5 runs). Better: 旌表（名词修饰，非事件）. PropBank 没有「旌表」，作事件也应写 旌表-00（guideline 2.1），旌表-01 是编出来的编号。这里「贞节旌表制度」里的旌表是名词性修饰，不作事件也可以。r2 把「贞节」「旌表」两个词合成一个概念，略差。
- [role] 「社会」与「制度」的关系: 制度 :poss 社会 (acceptable but worse, 2 of 5 runs). 「中国封建社会的…制度」，所属、处所、修饰都说得通。:poss 是旧名，按项目规则应写 :possessor（判 minor）；r2、r4 全篇都写 :poss（第 3、4 句等还有），r1 在第 3、4 句也用 :poss，后面不再写。
- [attr] 判断谓语与「衍生」的 aspect: 判断 state，衍生 state (acceptable but worse, 1 of 5 runs). Better: 判断 state，衍生 performance. 判断句是状态（guideline 4.1）；「衍生」是过去已经完成的产生过程，performance 合适，r3 标 state 略差。gold 的 identity-91 又漏了 aspect（同第 1 句）。
- [doc-temporal] 「衍生」相对文档时间: document-creation-time :after 衍生（将来） (wrong, 1 of 5 runs); (衍生 :before document-creation-time)（文档时间在衍生之前，即衍生为将来） (wrong, 1 of 5 runs); 衍生没有时间父节点 (acceptable but worse, 2 of 5 runs). Better: past-reference :contained 衍生. 「衍生」发生在封建时代，是过去事件，应为 (document-creation-time :before 衍生) 或挂 past-reference。r1 的 :after 和 r4 把 DCT 写成子节点的 (衍生 :before DCT) 都表示衍生在文档时间之后，方向反了。r3 这一句整个没有 temporal。
- [doc-modal] 文档级 modal: 只挂判断，衍生、cause-01 没有 modal 父节点 (acceptable but worse, 1 of 5 runs). Better: author 挂判断和衍生. gold 的「旌表」是没有 aspect 的名词修饰节点，不是事件，不应有 modal 父节点（guideline 5.2）。r5 把旌表建成事件并挂 author，与它自己的图一致，归在 ok 里（旌表-01 的问题另条）。
- [doc-coref] 「牌坊」跨句共指的方向: (本句牌坊 :same-entity 第 1 句牌坊) (acceptable but worse, 3 of 5 runs). Better: (第 1 句牌坊 :same-entity 本句牌坊). guideline 5.3：先出现的在前，(earlier :same-entity later)。r2、r4、r5 写反，意思不变，判 minor；r2、r4、r5 全篇的跨句 coref 大多如此，后面不再写方向。

### Sentence 3: 由于   中国   社会   在  封建   时代   对  妇女   贞操   和  孝义   非常   看重   ，  所以   贞孝   节烈   牌坊   则  是  用于   表扬   女性   守节   守孝   行为   的  奖励   。

Reviewer's notes on the annotator's choices:
- [structure] 「由于…所以」的因果表达: cause-01 :ARG0 看重 :ARG1 identity-91 (acceptable but worse, 2 of 5 runs). Better: 主谓语 :cause 看重. abridged 2.5：因为/由于 → :cause（或 have-cause-91）；guideline Part 3-1-1-3 说没有谓词化的因果关系不作事件，r3、r5 的 cause-01 略差。have-cause-91 的论元 guideline 没有定义；训练数据 3 例中 2 例（zh-0018「致使」、zh-0017「因…而升级」）是 ARG1 结果、ARG2 原因，gold 自己第 4 句也是 ARG1 结果，而这里 ARG1 是原因，与之相反。论元方向没有明确规则，记 open。
- [role] 「在封建时代」的角色: 看重 :temporal (封建时代) 合成一个节点 (acceptable but worse, 1 of 5 runs). Better: 看重 :temporal (时代 :mod 封建). 「在封建时代」是事件的时间状语，用 :temporal（项目规则：时间用 :temporal）；:era 是 date-entity 的规范化角色（guideline Part 3-3）。r4 把两个词合成一个概念。
- [role] 「妇女」与「贞操和孝义」的所属方向: 只有 贞操 :mod 妇女 (acceptable but worse, 1 of 5 runs). 「妇女贞操和孝义」是妇女的贞操和孝义，所属者是妇女：(贞操 :possessor 妇女)。gold 写成 :possessor-of，方向反了，变成贞操和孝义拥有妇女。r1、r2、r4 用旧名 :poss（第 2 句已记），所属方向是对的；r3 只给贞操挂了妇女。
- [sense] 「奖励」是实体还是事件: 奖励-01（事件） (acceptable but worse, 4 of 5 runs). Better: 奖励（名词）. 「牌坊…是…的奖励」里奖励指作为奖赏的东西（牌坊本身），是实体；作 奖励-01 事件就成了「牌坊等于奖励这一事件」。PropBank 奖励-01 有这个义项，但这里不是谓词用法，略差。
- [role] 「用于表扬」与奖励的关系: 奖励-01 :ARG2 表扬 (wrong, 1 of 5 runs). Better: 奖励 :purpose 表扬. 「用于表扬…」是奖励的用途，:purpose 合适（不建「用于」节点也可以）。PropBank 奖励-01 的 ARG2 是 thing arg0 rewards arg1 for（因什么而奖励），不是用途，r1 用错。
- [sense] 「守节」「守孝」的概念: 守节-01、守孝-01（事件） (wrong, 5 of 5 runs). Better: 守节、守孝（名词修饰，非事件）. PropBank 有 守节-01（ARG0 agent，ARG1 cause），没有「守孝」，作事件应写 守孝-00（guideline 2.1），五个系统都编了 守孝-01。作事件（守节-01 + 守孝-00，ARG0 女性）本身也是好的写法；gold 作修饰「行为」的名词也可以。
- [role] 「女性」的角色: 守节、守孝 :ARG0 女性，另加 行为 :ARG0 女性 (acceptable but worse, 1 of 5 runs). Better: 守节、守孝 :ARG0 女性. 「表扬女性守节守孝行为」是表扬女性的守节守孝行为，女性是守节守孝的施事（行为的所有者），表扬的对象是行为。PropBank 表扬-01：ARG0 praiser，ARG1 party praised，ARG2 只是介词标记，女性不是表扬的 ARG2。r5 给非事件的「行为」加 ARG0，多余。
- [structure] 「行为」节点: 行为 :ARG0-of 守节-01、守孝-01 (wrong, 1 of 5 runs); 没有 行为，表扬 :ARG1 (and 守节 守孝) (acceptable but worse, 2 of 5 runs). 表扬的对象是「行为」，守节守孝是它的类型修饰。r3 写成行为是守节、守孝的施事（ARG0-of），语义错；r1、r4 丢了「行为」，以事件直接作表扬的对象，意思差不多但漏词。r5 的 ARG0 问题已在上一条记。
- [doc-temporal] 「看重」（封建时代）相对文档时间: 看重只通过 :overlap 连到现在的判断（r1 看重 :overlap 表扬，r2 看重 :overlap 是） (acceptable but worse, 2 of 5 runs); 看重没有时间父节点（r5 只有判断） (acceptable but worse, 1 of 5 runs); 整句没有 temporal (wrong, 2 of 5 runs). Better: document-creation-time :before 看重. 「在封建时代…看重」明确是过去，应为 (document-creation-time :before 看重)（guideline 5.1）。r1、r2 用 overlap 把它和「牌坊是奖励」这一现在的状态连起来，没有表达过去；r3、r4 整句缺 temporal。
- [doc-coref] 「牌坊」共指连到哪一句: 连第 1 句（且方向反） (acceptable but worse, 1 of 5 runs). Better: 连第 2 句（最近的提及）. guideline 5.3：每个提及连到最近的前一个提及。gold 全篇把牌坊都连回第 1 句（星形），等价但不合规定，后面不再写；r2、r5 方向反已在第 2 句记。

### Sentence 4: 因为   每个   被  表扬   人士   的  生平   事迹   均  有  不同   ，  所以   贞孝节烈     牌坊   亦  会  被  区分   为  贞节   、  贞寿   、  贞烈   、  节孝   、  节烈   等  牌坊   。

Reviewer's notes on the annotator's choices:
- [structure] 「等」: 没有「等」 (acceptable but worse, 2 of 5 runs). 「等」表示列举未尽，训练数据的写法是把「等」作为并列 and 的最后一个 :opN（zh-0001、zh-0005、zh-0007 等多例）；:mod 等 也表达了列举未完。gold、r2、r3 漏掉，略差。
- [role] 「不同」的论元编号: :ARG1 事迹 (wrong, 5 of 5 runs). Better: :ARG0 事迹. PropBank 不同-01 只有 ARG0（things which are different），事迹应是 ARG0；五个系统都写成 ARG1，是凭印象没查框架。
- [attr] 「每个」: 人士 :quant (每个) (acceptable but worse, 2 of 5 runs); 人士 :mod (每个) (acceptable but worse, 3 of 5 runs). Better: 人士 :quant (每) :unit (个). 量词按项目规则保留为 :unit；「每」是量化词，abridged 4.2 用 :quant (all) 这类概念表示。系统把「每个」当一个节点、丢了量词，判 minor。
- [structure] 副词「均」「亦」: 只有 区分 :mod 亦，没有 均 (acceptable but worse, 2 of 5 runs); 两个都没有 (acceptable but worse, 3 of 5 runs). Better: 不同 :mod 均，区分 :mod 亦. 「均」（都）、「亦」（也）在训练数据里都作 :mod 节点（zh-0013、zh-0020 :mod (均)，「都」「也」同样）。系统普遍漏掉这类范围副词。
- [doc-temporal] 区分与不同的时间关系: (不同 :before 区分)：区分在不同之前 (wrong, 1 of 5 runs); 只有 DCT :overlap 区分 (acceptable but worse, 1 of 5 runs). 原因「事迹不同」是区分的依据，应与区分同时或在其前；r2 写的 (不同 :before 区分) 按 UMR 读法是区分在不同之前，反了。r3、r4 缺整句 temporal 是同一习惯，见第 3 句。

### Sentence 5: 虽然   旌表   贞节   制度   早于   秦代   就  已经   存在   ，  但  最  早  有关   贞孝   节烈   牌坊   的  记载   则  追溯   到  明代   ，  而  贞孝   节烈   牌坊   亦  在  明代   年间   得到   法制   保证   。

Reviewer's notes on the annotator's choices:
- [structure] 「虽然…但…而」的分句关系: and :op1 (contrast 存在 追溯) :op2 保证 (acceptable but worse, 2 of 5 runs); and 三个分句，没有转折 (wrong, 1 of 5 runs). Better: but-91 :ARG1 存在 :ARG2 (and 追溯 保证). 训练数据「虽然…但…」多用 but-91（7 例，contrast-01 1 例），but-91 的论元多是 :ARG1/:ARG2。「而…亦…」是并列追加，不是时间先后，gold 的 consecutive 不对，且 consecutive 在训练数据里用 :op1/:op2。r1 丢了转折；r3、r5 把第三个分句放到转折之外，略差。
- [structure] 「早于秦代」: :temporal (早于 :op1 秦代) (acceptable but worse, 3 of 5 runs). Better: :temporal (before :op1 秦代). 「早于秦代就已经存在」是在秦代之前就存在，gold 写成「存在于秦代」并多出一个挂在存在上的「早」（对齐到第 13 个词，实为「早于」），意思变了。abridged 2.5：时间先后用 :temporal (before :op1 …)。系统 r1、r2、r4 用「早于」当带 :op1 的普通概念，PropBank 早于-01 是谓词（ARG0/ARG1），写法不规范。
- [attr] 「最早」: 一个节点 最早 (acceptable but worse, 4 of 5 runs). Better: 早 :degree 最. 「最早」是「早」被「最」强化，(早 :degree 最)（abridged 4.2 :degree 最）。gold 用反向角色 :degree-of 写成了「最」被「早」修饰，方向反。系统多把「最早」合成一个概念。
- [structure] 「得到法制保证」: 保证-01 :ARG1 牌坊 :ARG2 法制 (wrong, 1 of 5 runs). 「得到…保证」可以照字面建 得到-01，也可以把「得到」看作轻动词、以 保证-01 为谓语（PropBank 保证-01：ARG0 ensurer，ARG1 thing ensured，ARG2 party to whom the promise is made）。r4 的 ARG2 是承诺对象，法制不是。
- [structure] 副词「已经」「亦」: 两个都没有 (acceptable but worse, 3 of 5 runs). Better: 已经、亦 都有. 训练数据把「已经」作 :mod 节点（zh-0001 多例），「亦」「也」同样作 :mod。gold 漏了第 29 个词「亦」；r1、r2、r3 两个都漏（同第 4 句）。
- [structure] 第二次出现的「贞孝节烈牌坊」: 另建一个牌坊节点，不连 (acceptable but worse, 1 of 5 runs); 另建一个牌坊节点，句内用 :coref 连 (acceptable but worse, 1 of 5 runs). Better: 重入，用同一个牌坊节点. guideline 5.3：句内同指用重入，不另建节点、也不写 :coref 三元组。
- [doc-temporal] 三个过去事件相对文档时间: document-creation-time :after 存在（及其他）：过去事件写成将来 (wrong, 2 of 5 runs); (存在 :before DCT)、(追溯 :before DCT)：文档时间在前，同样是将来 (wrong, 1 of 5 runs). Better: past-reference :contained 存在（和其他事件）. 秦代以前就存在的封建制度、明代得到的法制保证都是过去事件，应为 (document-creation-time :before X) 或挂 past-reference。r1、r3 的 (DCT :after X) 和 r4 的 (X :before DCT) 按 UMR 读法都表示 X 在文档时间之后。gold 把「存在」标 overlap（封建制度今天并不存在），略差；追溯是状态，overlap 可以。
- [doc-coref] 「制度」与第 2 句的共指: 有，方向反 (acceptable but worse, 1 of 5 runs); 没有连制度 (acceptable but worse, 4 of 5 runs). Better: (第 2 句制度 :same-entity 本句制度). 第 2 句「贞节旌表制度」和本句「旌表贞节制度」是同一制度，应连 coref（guideline 5.3）。r4 只连了旌表事件（same-event），没连制度。

### Sentence 6: 贞孝节烈     牌坊   在  明清   二代   在  中国   各地   大肆   兴建   。

Reviewer's notes on the annotator's choices:
- [attr] 「明清二代」: and 明代 清代（没有数量和量词） (acceptable but worse, 2 of 5 runs); and dynasty "明" "清"（没有数量和量词） (acceptable but worse, 2 of 5 runs); and dynasty "明" "清" :quant 2（没有量词） (acceptable but worse, 1 of 5 runs). 「明清二代」是明、清两个朝代。按项目规则量词「代」保留为 :unit，数目写成数字常量（:quant 2）；gold 的结构对，但「二」写成了概念节点。系统都丢了量词「代」，r1、r2 还造了原文没有的「清代」一词。
- [role] 「中国各地」的部分整体方向: 地 :mod 各 :part-of 中国（拆开「各地」） (acceptable but worse, 1 of 5 runs); 各地 :mod 中国 (acceptable but worse, 1 of 5 runs). Better: 各地 :part-of 中国. 项目规则：部分作父节点时用 :part-of。「各地」是中国的各个部分，父节点是各地，应为 (各地 :part-of 中国)；gold 用 :part 方向配反。r5 把一个词「各地」拆成两个节点，r1 用泛的 :mod。
- [doc-temporal] 「兴建」（明清）相对文档时间: document-creation-time :after 兴建（将来） (wrong, 1 of 5 runs); (兴建 :before document-creation-time)（文档时间在前，即将来） (wrong, 1 of 5 runs); 只连到第 5 句的追溯（兴建在追溯之前），不连文档时间 (acceptable but worse, 1 of 5 runs). 明清两代的兴建是过去事件，(document-creation-time :before 兴建) 或 past-reference 都对。r1、r4 又把过去写成将来（同第 5 句的习惯）。r3 挂到上一句的状态「追溯」上，参照时间不清楚。

### Sentence 7: 在  清代   ，  政府   当局   拨发   银两   用以   兴建   贞孝   节烈   牌坊   是  朝廷   表扬   贞节   旌表   三  种  方法   的  其中   一种   。

Reviewer's notes on the annotator's choices:
- [structure] 「三种方法的其中一种」: 方法 :quant 1 :unit 种 :part-of (方法 :quant 3 :unit 种) (acceptable but worse, 1 of 5 runs); 方法 :quant 1 :part-of (方法 :quant 3) (acceptable but worse, 2 of 5 runs); 其中一种 :part-of (方法 :quant 3) (acceptable but worse, 1 of 5 runs). Better: 方法 :quant 1 :subset-of (方法 :quant 3 :mod 种). 「三种方法的其中一种」是三种方法中的一种，成员关系，按项目规则用 (成员 :subset-of 集合)；:part-of 是部分整体，略差。数目写数字、量词「种」保留为 :unit。gold 用了 UMR 不用的 :domain，数目写成字符串 "三"，把「一种」「其中」当成概念，丢了量词。
- [role] 「表扬」与「方法」的关系: 方法 :ARG1-of 表扬（方法是被表扬者） (wrong, 2 of 5 runs). 「朝廷表扬…的方法」是用来表扬的方法，:purpose 或 :manner 都对。PropBank 表扬-01 的 ARG1 是 party praised，方法不是被表扬的对象，r3、r4 错。
- [doc-temporal] 拨发与兴建（目的）的先后: (拨发 :before 兴建)：兴建在拨发之前 (wrong, 2 of 5 runs); 没有这条 (acceptable but worse, 3 of 5 runs). Better: (拨发 :after 兴建)：兴建在拨发之后. abridged 5.1：目的事件 :after 主事件，(拨发 :after 兴建)。r1、r2 写的 (拨发 :before 兴建) 按 UMR 读法（子节点相对父节点）是兴建在拨发之前，反了；看得出系统是按「拨发在兴建之前」的英文语序写的。
- [doc-temporal] 清代事件相对文档时间: document-creation-time :after 是（将来） (wrong, 1 of 5 runs); (拨发 :before document-creation-time)（将来） (wrong, 1 of 5 runs); 只连到第 6 句的兴建 (acceptable but worse, 1 of 5 runs). 清代的拨发是过去事件。r1、r4 再次把过去事件写成文档时间之后（同第 5 句）。

### Sentence 8: 清代   当局   最后   由于   拨发   建  牌坊   的  银两   数目   有限   而  达不到    彰显   守节   守孝   的  效果   ，  所以   在  中国   各地   设立   节孝祠    。

Reviewer's notes on the annotator's choices:
- [structure] 「由于有限而达不到…所以设立」的因果链: cause-01 :ARG0 达不到 :ARG1 设立，有限作 数目 的 :mod (acceptable but worse, 1 of 5 runs). Better: 设立 :cause (达不到 :cause 有限). 「由于…有限而达不到…」是因果（由于 → :cause，abridged 2.5），不是时间先后；gold 用 consecutive 连「有限」和「达到」，丢了因果。r5 的 cause-01 是同一习惯（见第 3 句）；r3 把谓语「有限」降成修饰语，丢了一层原因。
- [sense] 「达不到」的概念: 达不到-01 (wrong, 4 of 5 runs). Better: 达到-01 :polarity -. PropBank 没有「达不到」，有 达到-01（ARG0 theme，ARG1 point reached）。可能补语「达不到」= 达到 + 否定，写 达到-01 :polarity -；作一个词也只能是 达不到-00，达不到-01 是编出来的编号。
- [role] 「有限」的论元: 有限-01 :ARG1 数目 (wrong, 3 of 5 runs); 有限（无义项）:ARG1 数目 (wrong, 1 of 5 runs); 数目 :mod 有限（非谓词） (acceptable but worse, 1 of 5 runs). Better: 有限-01 :ARG0 数目. PropBank 有限-01 只有 ARG0（entity described），「数目有限」的数目是 ARG0。r1、r4、r5 写 ARG1，是凭印象；r2 的事件概念没有义项编号；r3 把谓语「有限」当修饰语。
- [structure] 「彰显守节守孝的效果」挂在哪: 效果 :ARG1-of 彰显（效果是被彰显之物） (wrong, 3 of 5 runs). Better: 效果 :mod 彰显. 「彰显守节守孝的效果」是修饰「效果」的定语，彰显应挂在效果下。PropBank 彰显-01：ARG0 entity described，ARG1 thing arg0 displays，被彰显的是守节守孝（and），效果不是 ARG1；r1、r4 因此让彰显带了两个 ARG1。gold 把彰显挂成「达到」的修饰。
- [structure] 「最后」挂在哪: 达不到 :mod 最后 (acceptable but worse, 1 of 5 runs). Better: 设立 :temporal 最后. 「清代当局最后…所以…设立节孝祠」，「最后」说的是当局最终采取的做法（设立），不是银两数目「有限」的时间。
- [doc-temporal] 原因与「设立」的先后: (达不到 :before 设立)：按 UMR 读法设立在达不到之前 (wrong, 3 of 5 runs); 只有 (第 7 句拨发/判断 :before 设立)：设立在第 7 句之前 (wrong, 2 of 5 runs). Better: (有限 :after 设立)：设立在有限之后. 设立节孝祠是「达不到效果」的结果，在其后；也在第 7 句的拨发之后。(A :before B) 表示 B 在 A 之前：r1、r2、r4 的 (达不到 :before 设立)、r3、r5 的 (拨发 :before 设立) 都把设立放到了原因之前。系统一贯把 (A :before B) 当作「A 在 B 之前」来写。
- [doc-temporal] 「设立」相对文档时间: document-creation-time :after 设立（将来） (wrong, 1 of 5 runs); (设立 :before document-creation-time)（将来） (wrong, 1 of 5 runs); 不连文档时间，只连第 7 句 (acceptable but worse, 2 of 5 runs). 清代的设立是过去事件；r1、r4 同第 5 句的习惯，写成了将来。
- [doc-coref] 「清代当局」与第 7 句的共指: 没有 (acceptable but worse, 3 of 5 runs). Better: (第 7 句当局 :same-entity 本句当局). 第 7 句「政府当局」和本句「清代当局」是同一个当局，应连 coref（guideline 5.3）。gold 这一句没有任何 coref。r2 方向反（第 2 句已记）。

### Sentence 9: 中华民国     建立   后  ，  北洋   政府   仍  实行   贞节   旌表   。

Reviewer's notes on the annotator's choices:
- [attr] 「实行」的 aspect: state (acceptable but worse, 1 of 5 runs). Better: activity. 「仍实行贞节旌表」是持续进行的做法，activity（或 habitual）合适；实行是动作，不是状态。
- [doc-temporal] 实行与「建立」的先后: (建立 :before 实行)：按 UMR 读法实行在建立之前 (wrong, 4 of 5 runs); 只有 (第 8 句设立 :before 实行) (wrong, 1 of 5 runs). Better: (建立 :after 实行)：实行在建立之后. 句子明说「建立后…仍实行」，实行在建立之后，应为 (建立 :after 实行)。系统把 (A :before B) 当成「A 在 B 之前」来写，结果全部反了；r1 还写了 (DCT :after 实行)。

### Sentence 10: 但  不久   ，  要求   女性   恪守   贞节   的  风俗   习惯   即  因  新文化    运动   引发   的  女性   解放   和  男女   平等   倡议   而  遭到   冲击   。

Reviewer's notes on the annotator's choices:
- [structure] 句首「但」: 没有「但」 (acceptable but worse, 5 of 5 runs). Better: but-91 :ARG2 （遭到冲击）. 句首「但」与上一句（北洋政府仍实行旌表）构成转折，训练数据用 but-91 表示；只有本句一侧时写 :ARG2 可以。系统全部丢了这个转折。
- [sense] 「要求」的义项与论元: 要求-01 :ARG1 (恪守 :ARG0 女性) (acceptable but worse, 4 of 5 runs); 要求-02 :ARG1 (恪守 :ARG0 女性) (wrong, 1 of 5 runs). Better: 要求-02 :ARG1 女性 :ARG2 恪守. PropBank 要求-02：ARG0 asker，ARG1 askee，ARG2 predicate，正是「要求女性恪守贞节」的结构；要求-03（ARG1 predicate）也可以。要求-01 的 ARG1 是 things asked for，用于名词性的索取物，略差。r4 选了 -02 却把谓语放在 ARG1（-02 的 ARG1 是被要求的人）。
- [role] 「男女平等」: 平等 :ARG1 男女（无义项） (wrong, 1 of 5 runs); 一个节点 男女平等 (acceptable but worse, 2 of 5 runs). Better: 平等 :mod 男女（非谓词）. PropBank 平等-01 只有 ARG0（entity described）；作事件应为 平等-01 :ARG0 男女。gold 用了框架里没有的 ARG1；r2 给没有义项编号的概念加 ARG1。作「倡议」内容的名词 平等 :mod 男女 也可以。
- [structure] 「新文化运动引发的女性解放和男女平等倡议」的切分: and (倡议 :mod 女性解放) (倡议 :mod 男女平等) :ARG1-of 引发 (acceptable but worse, 1 of 5 runs); 倡议 :mod (and 女性解放 男女平等) :ARG1-of 引发 (acceptable but worse, 1 of 5 runs). 可以读作「女性解放」和「男女平等倡议」并列，也可以读作两项倡议；「引发」管到哪一项也有歧义，都接受。r1、r4 把两个词合成「女性解放」「男女平等」一个概念，丢了 解放-01 的论元结构，略差。
- [doc-temporal] 「冲击」相对上一句和文档时间: (第 9 句实行 :before 冲击)：按 UMR 读法冲击在实行之前 (wrong, 4 of 5 runs); 同上，另加 (DCT :after 冲击) (wrong, 1 of 5 runs). Better: document-creation-time :before 冲击（及其他事件）. 「但不久…遭到冲击」在北洋政府实行旌表之后，应为 (实行 :after 冲击) 或 (DCT :before 冲击)。系统全部写成 (实行 :before 冲击)，即冲击在实行之前，方向反（同一习惯，见第 5、7、8、9 句）。
- [doc-modal] 「恪守」「平等」（被要求、被倡议的内容）的 modal: 没有 modal 父节点 (acceptable but worse, 4 of 5 runs). Better: (要求 :partial-affirmative 恪守). guideline 5.2：补足语谓词（要求、倡议）下的事件以该谓词为父节点，强度用 unspecified 或谓词蕴含的强度；被要求做的恪守、被倡议的平等不是作者断言为事实的事件，gold 都挂成 author full-affirmative。
- [doc-modal] 从属事件有没有 modal 父节点: 只有部分事件（r2 冲击+要求，r4 冲击+引发+要求） (acceptable but worse, 2 of 5 runs); 只有根事件 冲击 (wrong, 2 of 5 runs). Better: 每个事件都有. guideline 5.2 / checklist：每个事件都要有 modal 父节点。r1、r3 只给根事件写了 modal，解放、倡议、引发、要求、恪守全缺。

### Sentence 11: 国民政府     执政   后  ，  废除   贞节   旌表   。

Reviewer's notes on the annotator's choices:
- [concept] 「国民政府」: 政府 :mod 国民（拆开一个词） (acceptable but worse, 1 of 5 runs). 「国民政府」是一个政府的专名，作 government-organization 命名实体更好，作一个普通概念也可以；r1 把一个词拆成两个节点。
- [doc-temporal] 废除与执政的先后: (执政 :before 废除)：按 UMR 读法废除在执政之前 (wrong, 4 of 5 runs); 没有这条 (acceptable but worse, 1 of 5 runs). 「执政后废除」，废除在执政之后，应为 (执政 :after 废除)。系统再次按英文语序写成 (执政 :before 废除)，方向反。
- [doc-temporal] 废除与上一句的关系: (第 10 句冲击 :before 废除或执政)：方向反 (wrong, 5 of 5 runs). 废除在第 10 句的冲击之后，应为 (冲击 :after 废除)。gold 的子节点是 but-91（篇章节点，不是事件），而且 (废除 :after X) 表示 X 在废除之后，反了；系统的 (冲击 :before 废除) 也表示废除在冲击之前。
- [doc-coref] 「贞节旌表」与第 9 句的共指: 没有 (acceptable but worse, 1 of 5 runs). 第 9 句「实行贞节旌表」和本句「废除贞节旌表」是同一个制度/做法，应连 coref（guideline 5.3）。r2、r5 方向反已在第 2 句记。

### Sentence 12: 2015 年  ，  中华   人民   共和国    湖南省    衡阳县    文物局    考查   发现   中国   现存   、  可  考证   时间   的  最后   一座   贞孝   节烈   牌坊   。

Reviewer's notes on the annotator's choices:
- [structure] 「考查发现」的组织: 文物局 :ARG0-of 考查（考查作机构的修饰） (acceptable but worse, 1 of 5 runs). 「考查发现」可以看作两个相继的动作，也可以看作通过考查而发现；两种都接受。r3 把考查挂成文物局的关系从句，和发现脱了钩。
- [concept] 机构名的切分: :op1 "中华人民共和国"（未按词切分） (acceptable but worse, 1 of 5 runs). abridged 2.2：中文名字按词切分为多个 :opN（中华 / 人民 / 共和国）。把国名、省、县、局层层嵌套（各自作命名实体、用 :part-of 连）可能更好，但六份标注都没有这样做，不判。
- [attr] 「一座」: 牌坊 :quant 1（没有量词） (acceptable but worse, 2 of 5 runs); 最后 :quant 1（挂错节点，没有量词） (wrong, 1 of 5 runs). Better: 牌坊 :quant 1 :unit (座). 同第 1 句：数目写数字常量，量词「座」保留为 :unit。r3 把数量挂到「最后」上。
- [role] 「最后（一座）」: 牌坊 :ord (最后)（:ord 下不是 ordinal-entity） (acceptable but worse, 1 of 5 runs). 「最后一座」可以作 :mod 最后，或按 AMR 惯例作 :ord (ordinal-entity :value -1)；:ord 的值应是 ordinal-entity，r5 直接挂概念「最后」，略差。训练数据「最后」多作 :mod 或 :temporal。
- [sense] 「现存」的概念: 存在-01 :temporal 现（把一个词拆开改写） (acceptable but worse, 3 of 5 runs). Better: 现存-01. PropBank 有 现存-01（ARG0 entity described，ARG1 thing arg0 keeps now），应按原词用它；r2、r4、r5 把一个词改写成「现」+「存在」。
- [structure] 「现存」「可考证」与牌坊的关系: 牌坊 :ARG1-of (and 现存 考证) (acceptable but worse, 1 of 5 runs); 牌坊 :ARG1-of (and 存在 考证)，另有 存在 :ARG1 牌坊 (acceptable but worse, 1 of 5 runs). Better: 牌坊 :ARG1-of 现存/存在（及 考证）. 「中国现存、可考证时间的…牌坊」是两个关系从句修饰牌坊，牌坊应是 现存-01 的 ARG1（thing arg0 keeps now），用 :ARG1-of 表示。gold 用 :mod 挂一个 and，丢了论元关系；r1 让 and 充当 ARG1 的事件，r4 同一条边写了两遍。
- [attr] 「可考证时间」: 考证-01 :ARG1 时间 :mod 可 (acceptable but worse, 1 of 5 runs); 考证-01 :ARG2 时间（可 → neutral-affirmative） (wrong, 1 of 5 runs); 考证-01 :ARG2 时间（丢了「可」） (wrong, 1 of 5 runs); 可能-01 :ARG1 考证-01 :ARG1 时间 (acceptable but worse, 1 of 5 runs). Better: 考证-01 :ARG1 时间，可 → (author :neutral-affirmative 考证). PropBank 考证-01：ARG0 agent，ARG1 thing arg0 researches，没有 ARG2，时间应是 ARG1。情态词「可」不建节点，表现为 modal 强度 neutral-affirmative（abridged 2.1、5.2：can → neutral-affirmative）；gold、r1 把它作 :mod，r5 建成 可能-01 事件。
- [doc-temporal] 2015 年事件相对文档时间: (2015 :contained 考查/发现)，但 (DCT :after 2015)：2015 年在文档时间之后 (acceptable but worse, 1 of 5 runs); document-creation-time :after 发现（将来） (wrong, 2 of 5 runs); (发现 :before document-creation-time)（将来） (wrong, 1 of 5 runs). 2015 年的发现在文档时间之前。r5 把事件放进 2015 年是对的，但 (DCT :after 2015) 表示 2015 年在文档时间之后；r1、r3、r4 又把过去写成将来。r2 的 (考查 :before 发现) 按 UMR 读法是发现在考查之前，也反了，这里不单列。
- [doc-coref] 这座牌坊与「贞孝节烈牌坊」类的关系: 没有 (acceptable but worse, 3 of 5 runs). Better: (本句牌坊 :subset-of 前文牌坊). 项目规则：(成员 :subset-of 集合)，成员在前。本句的这一座牌坊是前文所说贞孝节烈牌坊这一类的成员，应为 (本句牌坊 :subset-of 第 1 句牌坊)。gold 方向反，而且另一端挂到了修饰语节点「贞孝节烈」上。

### Sentence 13: 这座   牌坊   位于   该  县  台源   镇  柳树   村  ，  是  当地   村民   为  守节   寡妇   廖黄氏    于  1921 年  所  建  。

Reviewer's notes on the annotator's choices:
- [concept] 「位于」的概念: have-place-91 (acceptable but worse, 1 of 5 runs). Better: 位于-01. PropBank 有 位于-01（ARG0 entity described，ARG1 location），有词汇动词时不用抽象谓词 have-place-91（guideline 2.3 只在没有动词时用）。训练数据 chinese_umr-0004 第43句、-0016 第8句都用 位于-01。
- [role] 「这座」的写法: 牌坊 :mod 这（量词省掉） (acceptable but worse, 3 of 5 runs); 牌坊 :mod 这座（不拆） (acceptable but worse, 2 of 5 runs). Better: 牌坊 :mod 这（量词省掉）. 指示词是 :mod（guideline 3 非论元角色：:mod 含 demonstrative），不是 :quant；量词按项目规则保留为 :unit，所以 gold 的 :unit 座 是对的，只是 这 的角色错。系统省掉量词判 minor（全篇如此）。
- [concept] 「该县」是否带名字: county :name "衡阳县"（从上文补名字） (acceptable but worse, 1 of 5 runs). 「县」是普通名词不是专名，gold 把它写成 name 的 :op1 是错的；「该县」指上一句的衡阳县，应靠共指表达，不该在本句图里凭空补出名字（r4）。
- [concept] 柳树村、台源镇的命名实体写法: village/town :name "柳树村"（一个 op） (acceptable but worse, 3 of 5 runs); 村/镇 :name (name :op1 "柳树")（类型用中文词） (acceptable but worse, 1 of 5 runs). Better: village :name :op1 "柳树" :op2 "村". guideline 2.2：命名实体是类型概念 + :name (name :op1 … :op2 …)，按词切分；训练数据 胡佛 村 → city-district :op1 "胡佛" :op2 "村"（chinese_umr-0004 第43句）。gold 的 :name 指向一个概念为「柳树」的普通节点，格式不合法。
- [role] 村—镇—县的层级关系: 村 :place 镇 :place 县 (acceptable but worse, 1 of 5 runs). Better: 村 :part-of 镇 :part-of 县. 行政区划的包含是部分—整体，部分为父节点用 :part-of（项目规则）；:place 是事件发生的处所，不适合表示实体之间的从属。
- [structure] 廖黄氏与寡妇的组合: 寡妇 :name 廖黄氏（寡妇作类型） (acceptable but worse, 1 of 5 runs). Better: person :name 廖黄氏 :mod 寡妇. 命名实体的类型取 guideline 类型表（person）；「寡妇」是对这个人的描述，应作 :mod，不作实体类型。
- [role] 「为廖黄氏」的角色: 建 :ARG2 廖黄氏 (wrong, 2 of 5 runs). Better: 建 :affectee 廖黄氏. PropBank 建-01 只有 ARG0 constructor、ARG1 thing constructed，没有 ARG2；受益者用非论元角色 :affectee（guideline 表9：beneficiary or maleficiary）。训练数据 chinese_umr-0005 第5句等用 :affectee。
- [doc-temporal] 「建」相对文档时间、相对「发现」的先后: 方向写反：(DCT :after 建)、(建 :before 发现) (wrong, 1 of 5 runs); 方向写反：(1921 :before 2015)、(建 :before 发现) (wrong, 1 of 5 runs); 方向写反：(发现 :after 建)、(建 :before 发现) (wrong, 1 of 5 runs); 方向写反：(建 :before 发现)、(建 :before DCT) (wrong, 1 of 5 runs); 方向写反：(DCT :after 1921)、(建 :before 发现) (wrong, 1 of 5 runs). Better: (document-creation-time :before 建)：建在文档时间之前. guideline Part 4-2-2-1：关系是子对父，(A :before B) 表示 B 在 A 之前。建（1921）在发现（2015）和文档时间之前，应写 (document-creation-time :before 建) 或 (发现 :before 建)。5 个系统都按英语语序把 (A :before B) 读成「A 在 B 前」，全部写反；全篇如此，之后的句子不再逐一判。
- [doc-temporal] 「位于」的时间: 没有标位于的时间 (acceptable but worse, 2 of 5 runs). Better: (document-creation-time :overlap 位于). 牌坊现在仍位于该村，是现在的状态，与文档时间 overlap；guideline 5.1 每个事件都要有时间父节点。
- [doc-coref] 牌坊与上句的共指: (本句牌坊 :same-entity s12 牌坊)：顺序后者在前 (acceptable but worse, 4 of 5 runs). Better: (s12 牌坊 :same-entity 本句牌坊). 「这座牌坊」指上句发现的那座牌坊，应连到 s12 的 牌坊 节点（s12x3），gold 连到了修饰词 贞孝节烈（s12x4）。guideline 5.3：较早的提及在前。
- [doc-coref] 「该县」的共指: (s12 文物局 :same-entity 本句县) (wrong, 1 of 5 runs). 上句的衡阳县只出现在机构名 government-organization 的名字里，没有单独的县节点；r4 把县和文物局连成同一实体，是错的。

### Sentence 14: 牌坊   上  放  上  石匾   ，  而  石匾   上  则  刻  有  由  第二   任  中华民国     大  总统   徐世昌    题写   的  “  节励   松筠   ”  四字   。

Reviewer's notes on the annotator's choices:
- [sense] 「放上」的义项: 放-01 :place 牌坊 (acceptable but worse, 1 of 5 runs). PropBank 有 放上-01（ARG0 agent、ARG1 entity placed，没有处所论元），也有 放-01（ARG2 location）。gold 取 放上-01，处所只能用 :place；系统取 放-01，处所应为 ARG2，r5 取 放-01 却用 :place 略差。
- [structure] 「牌坊上」「石匾上」的方位词: 两个「上」都不建节点 (acceptable but worse, 5 of 5 runs). 项目规则：方位词建节点。训练数据写法是 (上 :op1 X)（chinese_umr-0001 第46句 机身上 → (上 :op1 机身)）。gold 用 :direction 不合这个先例，且漏了「石匾上」；系统全篇不给方位词建节点（全篇如此）。
- [role] have-org-role-92 的论元: 徐 :ARG0-of，:ARG2 中华民国，:ARG3 大总统 (wrong, 1 of 5 runs); 徐 :ARG0-of，:ARG1 中华民国，:ARG2 大总统 (wrong, 1 of 5 runs); 徐 :ARG0-of，:ARG2 大总统，:ARG3 中华民国 (wrong, 1 of 5 runs); 徐 :ARG0-of，:ARG2 总统 :mod 中华民国 (wrong, 1 of 5 runs). Better: 徐 :ARG1-of，:ARG2 中华民国，:ARG3 大总统. guideline 2.3 与 Part 1 例 (4)：have-org-role-92 的 ARG1 是任职者、ARG2 是机构、ARG3 是职位；训练数据 chinese_umr-0001 第39句同样是 ARG2 country / ARG3 总统。gold 把 ARG2/ARG3 对调；r1–r4 按 AMR have-org-role-91 的习惯用 ARG0 作任职者（全篇如此）。
- [structure] 「第二任」的写法: 总统 :ord 2（没有 ordinal-entity） (acceptable but worse, 1 of 5 runs). Better: 总统 :ord (ordinal-entity :value 2). guideline Part 3-2-2-5：序数用 :ord，下面必须是 (ordinal-entity :value N)；「第二」是序数不是数量，而且修饰的是「总统」不是职位关系。量词「任」按项目规则可留作 :unit，系统省掉判略差（全篇习惯，见第13句）。
- [structure] 「四字」是否拆开: 四字 :quant 4 (acceptable but worse, 1 of 5 runs). Better: 字 :quant 4. 「四字」是数词 + 名词，guideline 2.2：数字写成 :quant；不拆就丢了数量。r3 拆了数量又保留「四」在概念里，重复。
- [concept] 字的内容「节励松筠」: 字 :mod ("节励松筠")：字符串作概念 (wrong, 1 of 5 runs). 字的内容是一段引文，guideline 没有专门规定；用 name 或 thing+name 表达都说得通。:mod 的取值应是概念，gold 用字符串常量不规范；r2 把字符串当概念，格式不合法。
- [doc-temporal] 徐世昌题写在先、刻在后: (题写 :before 刻)：按 UMR 读法是刻在题写之前 (wrong, 4 of 5 runs); 没有标题写与刻的关系 (acceptable but worse, 1 of 5 runs). guideline Part 4-2-2-1：(A :before B) 是 B 在 A 之前。题写是刻字的前提，应写 (刻 :before 题写)。系统是英语语序读法写反（全篇如此，见第13句），gold 这里也写反了。
- [doc-modal] 「题写」的 modal: 没有标题写 (acceptable but worse, 1 of 5 runs). Better: (author :full-affirmative 题写). guideline 5.2：每个事件都要有 modal 父节点。
- [doc-coref] 牌坊与上句的共指: (石匾 :same-entity 石匾)：自指；牌坊没连 (wrong, 1 of 5 runs). Better: (s13 牌坊 :same-entity 本句牌坊). r2/r3/r5 的顺序问题与第13句同一习惯，不另判。r4 写了一个变量和自己的共指，没有意义，并漏了牌坊与上句的共指。

### Sentence 15: 建筑   形式   因应   各  地区   而  略有   不同   ，  但  一般   为  牌楼   形式   ，  少数   则  为  墓碑   形式   。

Reviewer's notes on the annotator's choices:
- [concept] 「但」的话语关系: contrast-01（根） (acceptable but worse, 2 of 5 runs); and :op1 :op2 :op3，没有转折 (wrong, 1 of 5 runs); and(不同, contrast-91(为, 为))：转折放到「则」上，「但」丢失 (acceptable but worse, 1 of 5 runs). Better: but-91（根）. guideline 2.5：但是/却 → but-91（或 contrast-91）；contrast-01 是英语 PropBank 义项，训练数据里只出现 1 次，contrast-91 8 次、but-91 10 次。r1 把转折写成并列，丢了「但」。
- [role] 「一般……少数则……」两分句的连接: 与第一分句一起拍平成 and 的 :op2 :op3 (acceptable but worse, 1 of 5 runs). guideline Part 3-1-6：and-contrast 这类合并概念取 :opX，不取 :ARGn。gold 选 and-contrast 表达「则」的对比本身可以，但角色错了。
- [role] 「不同」的论元: 不同-01 :ARG1 建筑形式 (wrong, 5 of 5 runs). Better: 不同/同 :ARG0 建筑形式. PropBank 不同-01 只有 ARG0（things which are different），没有 ARG1；训练数据也是 :ARG0。系统把形容词性谓词的唯一论元习惯写成 ARG1。
- [structure] 「因应各地区」的表达: 不同 :cause 地区（不建 因应） (acceptable but worse, 3 of 5 runs); 不同 :ARG2 地区 (wrong, 1 of 5 runs). Better: 不同 :cause (因应-01 :ARG1 地区). PropBank 因应-01 ARG1 thing responded to，因应是动词，保留节点更完整。地区差异造成了形式不同，是原因不是动机，按项目规则用 :cause 更合适；不同-01 没有 ARG2。
- [concept] 「一般为」「少数则为」的谓词: have-mod-91 (acceptable but worse, 1 of 5 runs); 为-01 :ARG0 主语 :ARG1 表语 (acceptable but worse, 1 of 5 runs); 为-03 (acceptable but worse, 1 of 5 runs); 为-01 :ARG1 主语 :ARG2 表语（为-01 没有 ARG2） (wrong, 1 of 5 runs). Better: identity-91. 这里的「为」是系词（=是），guideline 2.1：系词不是事件，转成 2.3 的抽象谓词；「形式为牌楼形式」是等同，用 identity-91。用 为-01 有 PropBank 依据但不合 guideline，判略差；r4 的论元在 为-01（ARG0 entity、ARG1 predicative）里没有 ARG2。
- [structure] 「一般」的挂接: identity :ARG1 (建筑 :mod 一般) (acceptable but worse, 1 of 5 runs); 为-03 :ARG0 (thing :quant 一般) (wrong, 1 of 5 runs). Better: 谓词 :frequency 一般，主语是建筑形式. 「一般为牌楼形式」= 建筑形式通常是牌楼形式；「一般」是频度副词，修饰谓词，主语是前一分句的建筑形式（重入）。gold 把「一般」当成等同的一方，又把它挂成主分句「建筑形式」的修饰语。
- [structure] 「少数」分句的主语: 少数（单独的节点） (acceptable but worse, 2 of 5 runs). 「少数则为墓碑形式」的主语是「少数（建筑）」。gold 的 :mod-of 让主分句的「建筑形式」带上修饰语「少数」，意思错了。
- [doc-temporal] 三个状态相对文档时间: 只标了「不同」 (acceptable but worse, 1 of 5 runs); 没有 temporal (wrong, 2 of 5 runs). Better: 三个状态都 (DCT :overlap). guideline 5.1：每个事件都要有时间父节点；泛指的现在状态与 DCT overlap。r3、r4 整句没有文档级 temporal。

### Sentence 16: 上面   常用   的  四  大  字  为  “ 钦  旌  节  孝  ”  等  ，  其下   可能   记载   节妇   相  资料   事迹   ，  或  两侧   附  相关   对联   诗句   。

Reviewer's notes on the annotator's choices:
- [sense] 「常用」的切分: 用-01 :frequency 常 (acceptable but worse, 5 of 5 runs). Better: 常用-01. PropBank 有 常用-01（ARG0 user、ARG1 entity that is often used），整词有义项时不拆开。
- [attr] 「四」的写法: 大字 :quant 4（大字合成一个概念） (acceptable but worse, 1 of 5 runs). Better: 字 :quant 4. guideline 2.2：数字写成阿拉伯数字常量 :quant 4，不建概念节点。
- [concept] 「四大字为『钦旌节孝』」的谓词: 为-01 :ARG0 字 :ARG1 钦旌节孝 (acceptable but worse, 1 of 5 runs); 为-01 :ARG0 字 :ARG1 ("钦旌节孝")：字符串作概念 (wrong, 1 of 5 runs); 为-01 :ARG1 字 :ARG2 钦旌节孝（为-01 没有 ARG2） (wrong, 1 of 5 runs). Better: identity-91. 系词「为」按 guideline 2.1 转成抽象谓词 identity-91（同第15句）。PropBank 为-01 只有 ARG0 entity、ARG1 predicative，r4 用 ARG1/ARG2 错；r2 把引号字符串当概念，格式不合法（同第14句）。
- [structure] 「等」的表达: 没有表达「等」 (acceptable but worse, 2 of 5 runs). 「为『钦旌节孝』等」= 例如钦旌节孝。:mod 等 是常见写法；gold 用 have-example-91 也表达了举例，但让 identity 的 ARG2 成了一个谓词，结构绕。漏掉「等」会把例子说成全部。
- [structure] 「上面」的挂接: 大字 :mod 上面 (acceptable but worse, 1 of 5 runs). 「上面」是处所，挂在谓词或「字」上都说得通；gold 用隐含整体 + :part 也合规则（整体为父用 :part），训练数据有 implicit-argument 的用例。r3 用 :mod 表处所不合适。
- [role] 「其下」「两侧」的角色: 记载、附都用 :place（gold 经 implicit-argument） (acceptable but worse, 3 of 5 runs); 记载 :place 其下，附 :ARG2 两侧 (acceptable but worse, 1 of 5 runs). Better: 记载 :ARG2 其下，附 :ARG2 两侧. PropBank 记载-01 ARG2 location arg1 is recorded，附-01 ARG2 place arg0 attached arg1；处所是核心论元时用 ARG2，不用 :place（REVIEWER「核心论元和非论元角色」）。
- [role] 节妇与资料事迹的关系: and(资料, 事迹) :mod 节妇 (acceptable but worse, 1 of 5 runs); … :poss 节妇（旧名） (acceptable but worse, 3 of 5 runs). 「节妇相（关）资料事迹」：关于节妇的资料用 :topic、节妇的事迹用 :possessor 都说得通。项目规则拼写用 :possessor，:poss 判 minor（这几个运行全篇如此）。:mod 表达不出这层关系。
- [structure] 「相关」修饰谁: 对联诗句 :ARG1-of 相关-01 (acceptable but worse, 2 of 5 runs). Better: 对联诗句 :mod 相关. 「相关对联诗句」里「相关」修饰对联诗句，不是「附」这个事件。PropBank 相关-01 只有 ARG0（entities which are relevant），r3、r4 用 ARG1-of 角色号错；作修饰语用 :mod 也可（guideline 2.1 修饰性的性质词）。
- [attr] 记载、附的 aspect: performance (acceptable but worse, 1 of 5 runs). Better: state. 这是对牌坊通常样式的描写（下面可能记有……，两侧附有……），是存续的状态，不是已完成的具体事件；guideline 4.1 performance 用于完成的过去事件。属难定的类型，故 gold 只给 low。
- [doc-modal] 「可能」的 modal 强度: 记载 full-affirmative，附 neutral-affirmative (wrong, 1 of 5 runs); 记载、附都 partial-affirmative (wrong, 1 of 5 runs). Better: 记载、附都 neutral-affirmative. guideline 5.2：可能、也许 → neutral-affirmative；「可能」管到「或」连接的两个分句。
- [concept] 「可能」是否建节点: 记载、附 :mod 可能 (acceptable but worse, 1 of 5 runs). Better: 不建节点. guideline 2.1：情态词（能、可以、应该、可能）不是节点，只影响 modal 强度。
- [doc-temporal] 「常用」的时间: 没有标「用」的时间 (acceptable but worse, 5 of 5 runs). 「常用」是现在仍成立的惯常事件（habitual），guideline 5.1 现在的状态/惯常与 DCT overlap，不是 before。
- [doc-temporal] 其余事件相对文档时间: 只标了 identity (acceptable but worse, 1 of 5 runs); 没有 temporal (wrong, 2 of 5 runs). Better: 为/identity、记载、附都 overlap. guideline 5.1：每个事件都要有时间父节点。r3、r4 整句没有文档级 temporal（r3、r4 在第15句也一样）。

### Sentence 17: 贞孝节烈     牌坊   必须   得到   官方   准许   才能   兴建   。

Reviewer's notes on the annotator's choices:
- [structure] 条件分句的结构: 兴建 :ARG1-of (cause-01 :ARG0 得到) (wrong, 1 of 5 runs). 「必须得到官方准许才能兴建」是条件关系（guideline 2.5：只有……才 → :condition）。得到-01（ARG0 obtainer、ARG1 thing obtained）保留时得到者是牌坊（被准许建的对象），gold 漏了 ARG0 且让 准许 作条件、得到 挂在下面，结构绕但意思还在；「得到准许」也可视为接近被动的轻动词结构而省掉。r3 把条件写成原因，错。
- [role] 准许的对象（被准许的事）: 准许 没有 ARG2 (acceptable but worse, 3 of 5 runs). Better: 准许 :ARG2 兴建（重入）. PropBank 准许-01 ARG2 predicate（被准许做的事），这里就是「兴建」。r5 另把牌坊作 ARG1 party allowed 不妥（牌坊不是被准许的一方），见原图。
- [doc-temporal] 得到/准许与兴建的先后: 没有标 (acceptable but worse, 3 of 5 runs). Better: (兴建 :before 得到)：得到在兴建之前. 先得到准许才兴建，(A :before B) = B 在 A 之前，gold 写对了。r1、r2 是英语语序读法的同一习惯（见第13句）。
- [doc-temporal] 兴建相对文档时间: 没有与 DCT 的关系 (acceptable but worse, 2 of 5 runs). 这句说的是旧时（明清）的制度，可当过去看（before），也可当泛指的规则（overlap）。r1 方向问题同第13句。

### Sentence 18: 建造   程序   由  地方   官  掌控   ，  在  查访   后  向  直省   督抚   报告   ，  然后   在  上报   礼部   奏请   旌表   。

Reviewer's notes on the annotator's choices:
- [sense] 「奏请」的义项: 奏请-01 (wrong, 5 of 5 runs). Better: 奏请-00. PropBank 没有「奏请」，guideline 2.1：不在 PropBank 的谓词写 词-00。系统凭空编了 -01（全篇如此）。
- [sense] 「旌表」的概念: 旌表-01 (wrong, 2 of 5 runs). Better: 旌表（名词）. PropBank 没有「旌表」；作事件时应写 旌表-00，-01 是凭空编号。这里作「奏请」的对象，名词也可。
- [structure] 上报与奏请的关系: 上报、奏请平列为 and 的两项 (acceptable but worse, 1 of 5 runs); 礼部 :ARG1-of 上报（礼部作报告内容） (wrong, 1 of 5 runs); 没有「上报」 (wrong, 1 of 5 runs). 「然后在上报礼部（时）奏请旌表」：上报是为了奏请，或奏请在上报之后，两种都说得通。PropBank 上报-01 ARG1 是 information、ARG2 是 reported to，r3 把礼部作 ARG1 错；r4 漏了上报这个事件。
- [concept] 「礼部」是否命名实体: 礼部（普通概念） (acceptable but worse, 4 of 5 runs). Better: government-organization :name "礼部". 礼部是清代具体的中央机构名，按 guideline 2.2 作命名实体（government-organization）。
- [attr] 程序各步骤的 aspect: 掌控 state，报告/查访/上报/奏请 performance (acceptable but worse, 2 of 5 runs); 掌控 activity，其余 performance (acceptable but worse, 1 of 5 runs); 掌控 state，查访/上报 process，报告/奏请 performance (acceptable but worse, 1 of 5 runs). Better: 全部 habitual. 这是对旧时一般程序的描写，每一步对每个牌坊都重复发生，guideline 4.1 habitual：经常或重复发生的事件。performance 指一次完成的具体事件。属难定的情况，只提 low。
- [doc-modal] 查访、上报的 modal: 漏了查访 (acceptable but worse, 1 of 5 runs); 查访、上报都漏了 (acceptable but worse, 2 of 5 runs). Better: 查访、上报都有 author full-affirmative. guideline 5.2：每个事件都要有 modal 父节点。r4 没有上报节点，只看查访。

### Sentence 19: 北洋   政府   时期   ，  政府   允许   贞节   旌表   受  褒扬   人  、  家属   ，  及  同乡   为  其  建  坊  立  碑  ，  地方   官员   亦  会  亲  撰  碑文   。

Reviewer's notes on the annotator's choices:
- [role] 「贞节旌表」与「褒扬」的关系: 褒扬 :ARG2 旌表 (wrong, 1 of 5 runs); 人 :mod 旌表/贞节旌表 (acceptable but worse, 3 of 5 runs); 没有旌表 (acceptable but worse, 1 of 5 runs). 「受贞节旌表褒扬（的）人」：旌表是褒扬的方式或来源，:source、:instrument、:manner 都有人用，拿不准。PropBank 褒扬-01 只有 ARG0、ARG1，没有 ARG2；把旌表挂成「人」的修饰语丢了它和褒扬的关系。
- [structure] 家属、同乡与受褒扬人的关系: 家属/同乡 :poss 人（旧名） (acceptable but worse, 3 of 5 runs); 不表达 (acceptable but worse, 2 of 5 runs). guideline 2.3：亲属等关系用 have-rel-role-92，ARG1 是这个人（家属），ARG2 是对方（受褒扬人），ARG3 是关系；-91 按项目规则改 -92，have-rel-role 没有 ARG4。系统用 :poss（旧拼写）只是近似。
- [sense] 「撰」的概念: 撰-01 (wrong, 2 of 5 runs); 撰写-01（换成了另一个词） (acceptable but worse, 3 of 5 runs). Better: 撰-00. PropBank 没有「撰」，按 guideline 2.1 写 撰-00；-01 是凭空编号。撰写-01 存在，但概念应是原文的词。
- [concept] 「亦」: 没有 (acceptable but worse, 3 of 5 runs). Better: 撰 :mod 亦. 「亦」（也）是有内容的副词，通常作 :mod 保留。
- [attr] 「亦会亲撰」的 aspect: performance (acceptable but worse, 3 of 5 runs). Better: habitual. 「会」在这里表示通常会这样做，是惯常的事（guideline 4.1 habitual）；performance 指一次完成的具体事件。
- [doc-modal] 被允许的事的 modal: 建/立 没有 modal (acceptable but worse, 2 of 5 runs). Better: (允许 :neutral-affirmative 建/立). guideline Part 4-3-1-6：许可类（allow）给补足事件 neutral-affirmative，父节点是 允许；gold 直接让作者断言建坊发生。
- [doc-modal] 「撰」的 modal: (author :neutral-affirmative 撰) (acceptable but worse, 1 of 5 runs). Better: (author :full-affirmative 撰). 「会」在这里是惯常义，不表示可能；guideline 5.2 will/惯常 不降低强度。
- [doc-temporal] 「北洋政府时期」作时间框架: 时间表达没有进文档级 temporal (acceptable but worse, 3 of 5 runs). Better: (past-reference :contained 时期)，时期 :contained 允许/撰. guideline 5.1：先给时间表达找父节点，事件再以它为参照（(时期 :contained 事件)）。
- [doc-temporal] 允许相对文档时间: 没有 (acceptable but worse, 1 of 5 runs). r1、r4 的方向是同一习惯（见第13句）。
- [doc-coref] 「政府」与第9句北洋政府的共指: 没有 (acceptable but worse, 4 of 5 runs). Better: (s9 政府 :same-entity 本句政府). 「北洋政府时期，政府允许……」的政府就是第9句的北洋政府（gold s9x2）。

### Sentence 20: 如  民国   十三   年  十一   月  ，  四川   高等   检察厅    检察长    黄绶   为  成都   惨死   的  寡妇   牛萧福贞     撰写   碑文   。

Reviewer's notes on the annotator's choices:
- [structure] 「如」（举例）的表达: 根 撰写，不表达「如」 (acceptable but worse, 4 of 5 runs). 「如……」举上句「地方官员亲撰碑文」的一个例子。训练数据 chinese_umr-0014 第13句用 have-example-91 作根；用 :subset-of 把本句事件连到上句也表达了例子关系。完全不表达会丢掉这层话语关系。
- [structure] 「民国十三年十一月」: date-entity :year 13 :month 11 :mod 民国 (acceptable but worse, 1 of 5 runs). Better: 撰写 :temporal (date-entity :year 1924 :month 11). guideline 2.2：日期写成 date-entity，数字用阿拉伯数字；它是撰写的时间（:temporal），不该挂在 have-example-91 上，:year/:month 也不能挂在普通概念「民国」上。民国十三年 = 1924 年；用 :calendar 标纪年也可，:mod 民国 不规范。
- [concept] 检察厅的实体类型: 检察厅（中文词作类型） (acceptable but worse, 1 of 5 runs). Better: government-organization. 四川高等检察厅是国家司法机关，guideline 2.2 类型表有 government-organization，比上位的 organization 具体。
- [sense] 「惨死」的义项: 死-01 :manner 惨 (acceptable but worse, 4 of 5 runs). Better: 惨死-01. PropBank 有 惨死-01（ARG0 entity described），整词有义项时不拆开。
- [role] 惨死/死的论元号: 惨死/死 :ARG1 人 (wrong, 5 of 5 runs). Better: 惨死-01 :ARG0 人. PropBank 惨死-01、死-01 都只有 ARG0（entity described / entity who die），没有 ARG1。系统把一元谓词的唯一论元写成 ARG1（同第15句「不同」）。
- [structure] 「寡妇」: 人 :ARG0-of (have-role-91 :ARG3 寡妇) (acceptable but worse, 1 of 5 runs). Better: 人 :mod 寡妇. guideline 2.3：have-role-91 的 ARG1 是这个人，r3 用 ARG0-of 不对；直接 :mod 也可。
- [doc-modal] 「惨死」的 modal: 没有 (acceptable but worse, 2 of 5 runs). Better: (author :full-affirmative 惨死/死). guideline 5.2：每个事件都要有 modal 父节点。
- [doc-coref] 跨句的共指: (s19 碑文 :same-entity 本句碑文) (wrong, 1 of 5 runs); 没有 (acceptable but worse, 3 of 5 runs). 上句说的是地方官员一般会撰碑文，本句是一个具体例子：事件是上句的一例（subset），但本句的碑文不是上句泛指的碑文，r1 的 same-entity 错。

### Sentence 21: 台金   地区   内  有  至少   10 座  贞孝   节烈   牌坊   ，  其中   位于   金门   县  的  邱良功    母  节孝坊    更  被  列为   国定   古迹   。

Reviewer's notes on the annotator's choices:
- [concept] 存在句「有」的谓词: 有-03 (acceptable but worse, 4 of 5 runs). Better: exist-91. guideline 2.3：「there is X (in L)」用 exist-91；训练数据 exist-91 有 23 句、有-03 只有 3 句。有-03（ARG0 location、ARG1 entity）也是 PropBank 里对应的义项，判略差。
- [structure] 「台金地区内」: 地区 :name 台金，「内」不建节点 (acceptable but worse, 5 of 5 runs). 台金（台湾、金门）可作专名也可作修饰语，都接受。「内」是方位词，项目规则要建节点（系统全篇不建，见第14句）；gold 建了节点但用 :direction 不合训练数据 (方位词 :op1 X) 的写法。
- [attr] 「至少 10 座」: at-least 或 :mod 至少，量词省掉 (acceptable but worse, 3 of 5 runs). at-least 是 AMR 写法，训练数据有 (钱 :mod 至少 :quant 50)（chinese_umr-0020 第8句），两种都接受。量词「座」按项目规则保留为 :unit，省掉判 minor。
- [concept] 「邱良功母节孝坊」的名字: building/节孝坊/坊 :name "邱良功母节孝坊"（一个 op） (acceptable but worse, 3 of 5 runs). Better: 牌坊 :name :op1 "邱良功" :op2 "母" :op3 "节孝坊". guideline 2.2：中文名字按词切分为 :op1 :op2 …，不整串写成一个 op。
- [role] 「位于金门县」的论元: 节孝坊 :ARG1-of 位于-01 :ARG1 县（两个 ARG1） (wrong, 4 of 5 runs); 节孝坊 :ARG1-of 位于-01，位于又 :ARG0 节孝坊 (wrong, 1 of 5 runs). Better: 节孝坊 :ARG0-of 位于-01 :ARG1 金门. PropBank 位于-01：ARG0 entity described，ARG1 location。被定位的牌坊是 ARG0；系统在第13句写对了，这里把关系从句的中心语写成了 ARG1-of。
- [concept] 「金门县」的名字: 县 :name "金门" (acceptable but worse, 1 of 5 runs); county :name "金门县" (acceptable but worse, 4 of 5 runs). Better: county :name "金门". 「县」已由类型 county 表达，名字是「金门」；guideline 类型用英语类型词。
- [role] 「更」: 列为 :degree 更 (acceptable but worse, 3 of 5 runs). Better: 列为 :mod 更. 「更被列为国定古迹」的「更」是递进（还、甚至），修饰整个事件，不是性质的程度；项目规则 :degree 只用于性质的强化或弱化。
- [doc-modal] 存在与位于的 modal: 有/exist 有，位于 没有 (acceptable but worse, 3 of 5 runs). Better: 有、位于 都有. guideline 5.2：每个事件都要有 modal 父节点。
- [doc-temporal] 「列为」的时间: (DCT :overlap 列为) (acceptable but worse, 1 of 5 runs); 没有标 (acceptable but worse, 2 of 5 runs). 被列为古迹是过去完成的事件（gold 自己也标 performance），应为 (DCT :before 列为)；overlap 与 performance 不协调。r1、r4 的方向是同一习惯（见第13句）。
- [doc-coref] 「其中」：邱良功母节孝坊属于这 10 座: 图里 牌坊 :subset 节孝坊 (acceptable but worse, 1 of 5 runs); 图里 牌坊 :part 节孝坊；另有自指的共指 (wrong, 1 of 5 runs). Better: (节孝坊 :subset-of 10 座牌坊). 「其中」表示成员关系，项目规则 :subset-of 成员在前；:subset 不是 UMR 角色，:part 是部分—整体，不是成员关系；r4 还写了 (X :same-entity X)。

### Sentence 22: 其他   有名   的  贞孝   节烈   牌坊   包括   位于   台中市    大甲区    的  林氏   贞孝坊    ，  和  位于   台北市    二二八    和平   纪念   公园   内  的  黄氏   节孝坊    。

Reviewer's notes on the annotator's choices:
- [concept] 林氏贞孝坊、黄氏节孝坊: building/贞孝坊/坊 :name "林氏贞孝坊"（一个 op） (acceptable but worse, 3 of 5 runs). Better: 牌坊 :name :op1 "林氏" :op2 "贞孝坊". 「林氏贞孝坊」是一座具体牌坊的名称，与第21句「邱良功母节孝坊」同类，gold 在第21句把后者作命名实体，这里却拆成「林氏（人）的贞孝坊」，前后不一致。名字按词切分（guideline 2.2）。
- [concept] 二二八和平纪念公园的名字: park :name "二二八和平纪念公园"（一个 op） (acceptable but worse, 2 of 5 runs). Better: :op1 "二二八" :op2 "和平" :op3 "纪念" :op4 "公园". guideline 2.2：中文名字按词切分，每个词一个 :opN（欧洲议会 → :op1 "欧洲" :op2 "议会"）；原文分词是 二二八 / 和平 / 纪念 / 公园。
- [doc-coref] 「其他牌坊」与两座坊的成员关系: (林氏坊 :subset-of s21 10 座牌坊) (acceptable but worse, 1 of 5 runs). Better: (林氏坊/黄氏坊 :subset-of 其他牌坊). 项目规则：:subset-of 成员在前。两座坊是「其他有名牌坊」中的成员，gold 写反了。r3 把它归入上句台金的 10 座，原文说的是「其他」的，不对。
- [doc-temporal] 「包括」的时间: 没有 temporal (acceptable but worse, 2 of 5 runs). Better: (DCT :overlap 包括). 现在成立的状态，与文档时间 overlap。r3、r4 在第15、16句也整句漏标。

### Sentence 23: 根据   2013 年  厦门   晚报   的  报道   ，  福建省    厦门市    内  现在   还  有  总共   11 座  贞孝   节烈   牌坊   ，  而  湖南省    则  至少   有  1  座  。

Reviewer's notes on the annotator's choices:
- [structure] 「根据……报道」的结构: and :ARG1-of (根据-01 :ARG2 (报道 :poss 晚报)) (wrong, 1 of 5 runs). Better: 报道-01 作根：:ARG0 晚报 :ARG1 and(有, 有). PropBank 报道-01：ARG0 reporter、ARG1 thing reported；guideline 3：被报道的内容是报道动词的 ARG1，报道是事件名词，应作事件（guideline 2.1）。gold 用两层 :source 表达不了报道者与内容的关系。PropBank 根据-01 只有 ARG0、ARG1，r3 的 ARG2 错。
- [structure] 「福建省厦门市」: city :name :op1 "福建省" :op2 "厦门市" (acceptable but worse, 1 of 5 runs). Better: city 厦门市 :part-of province 福建省. guideline 2.2：name 的 :opN 只取字符串，不能是实体节点；「福建省厦门市」是两个地名，城市是省的一部分，用 :part-of（项目规则）。r1 把两个地名并成一个名字略差。
- [structure] 「还」「总共」: 没有「还」 (acceptable but worse, 1 of 5 runs); 没有「总共」 (acceptable but worse, 1 of 5 runs); 两个都没有 (acceptable but worse, 1 of 5 runs). 「还」（仍然）和「总共」都是有内容的副词，作 :mod 保留；漏掉会丢信息。
- [doc-modal] 两个「有」的 modal 父节点: (author :full-affirmative 有) ×2 (acceptable but worse, 1 of 5 runs). guideline 5.2：转述的内容以说话者为 conceiver（作者确信报道者，报道者确信内容）；「根据厦门晚报的报道」把信息来源交给报道，用报道事件或晚报作 conceiver 都可。gold 直接由作者断言略差，但 gold 没有报道事件，不单独改。
- [doc-temporal] 报道的时间: 没有标 (acceptable but worse, 1 of 5 runs). 2013 年的报道在文档时间之前，应为 (DCT :before 报道)（已并入本句第1条的 fix）。系统的方向是同一习惯（见第13句）。
- [doc-coref] 厦门、湖南的牌坊与第1句「牌坊」: (s21 10 座 :subset-of 11 座) (wrong, 1 of 5 runs). 项目规则：(成员或子集 :subset-of 集合)。厦门的 11 座、湖南的 1 座都是全部贞孝节烈牌坊的一部分，gold 写反了。台金的 10 座和厦门的 11 座没有包含关系，r3 错。

### Sentence 24: 现代   社会   普遍   认为   ，  贞节   牌坊   束缚   女子   的  自由   ，  是  封建   社会   的  糟粕   。

Reviewer's notes on the annotator's choices:
- [concept] 「是封建社会的糟粕」的谓词: 是-01 :ARG0 牌坊 :ARG1 糟粕 (acceptable but worse, 2 of 5 runs); 是-01 :ARG1 牌坊 :ARG2 糟粕（是-01 没有 ARG2） (wrong, 1 of 5 runs). Better: identity-91. guideline 2.1：系词「是」不是事件，转成 2.3 的抽象谓词（identity-91）。PropBank 是-01 为 ARG0 entity、ARG1 predicative，r4 的 ARG2 不存在。
- [role] 「普遍」的角色: 认为 :mod 普遍 (acceptable but worse, 1 of 5 runs); 认为 :degree 普遍 (acceptable but worse, 2 of 5 runs). Better: 认为 :manner 普遍. 「普遍认为」的普遍是副词性修饰事件，用 :manner（REVIEWER 判断标准）；它不是性质的强化或弱化，不用 :degree（项目规则）。
- [doc-modal] 「认为」内容的 modal 父节点: (社会 :full-affirmative 认为)(认为 :unspecified 内容) (acceptable but worse, 1 of 5 runs). guideline 5.2：转述的言语或想法，作者确信说话者/想法事件，内容的 conceiver 是持这个看法的人（或认为事件）。这是「现代社会」的看法，作者没有直接断言；gold 写成作者的断言。认为是确信的看法，r5 的 unspecified 偏弱。
- [doc-temporal] 内容事件的时间: 只标了「认为」 (acceptable but worse, 2 of 5 runs). guideline 5.1：每个事件都要有时间父节点；补足语事件也可以以认为为父节点。
- [doc-coref] 贞节牌坊的共指: 没有 (acceptable but worse, 2 of 5 runs). 这里的贞节牌坊是泛指这一类，与第1句的泛指同指；连到最近的泛指提及更好（guideline 5.3），先后顺序的问题同第13句。

### Sentence 25: 有  现代   学者   亦  认为   贞节牌坊     其实   是  富有   的  大户   人家   炫耀   其  显赫   地位   的  工具   ，  并未   对  守节   妇女   真正   进行   关怀   。

Reviewer's notes on the annotator's choices:
- [role] 「真正」的角色: 关怀 :degree 真正 (acceptable but worse, 3 of 5 runs). Better: 关怀 :mod 真正. 「真正进行关怀」的真正修饰事件，不是性质的强化或弱化，项目规则下不用 :degree。
- [concept] 「有现代学者」的「有」: 学者 :quant 有 (acceptable but worse, 2 of 5 runs). Better: 不建节点. 「有现代学者认为」的「有」是引入不定指主语的存在用法（= 一些），不是数量词；:quant 只放数字或量化词。
- [doc-modal] 「认为」内容的 modal: (认为 :unspecified identity)、(认为 :full-negative 关怀) (acceptable but worse, 1 of 5 runs). Better: (认为 :full-affirmative 是)、(认为 :full-negative 关怀). guideline 5.2：否定事件是 full-negative；被认为的内容以认为（或学者）为 conceiver，作者不直接断言（同第24句）。
- [doc-temporal] 内容事件的时间: 只标了 是 或 认为 (acceptable but worse, 3 of 5 runs). guideline 5.1：每个事件都要有时间父节点。r3、r5 只标了认为，r4 漏了关怀。

## Document zh-0016 (5 runs)

### Sentence 1: 香港   及  深圳   受  暴雨   重创   ，  多地   出现   水浸   和  山泥   倾泻   。  香港   启动   为期   16 小时   的  “  极端   情况   ”  ，  当局   形容   雨势   “  五百年    一  遇  ”  。

Reviewer's notes on the annotator's choices:
- [role] 「多地」在出现-01 里的角色: 出现 :place 地 (acceptable but worse, 1 of 5 runs). Better: 出现 :ARG0 地. PropBank 出现-01 ARG0 是 possessor,location（例：香港也会出现更多的中国基金，香港 是 ARG0），处所应作 ARG0，不用 :place。
- [sense] 「水浸」的概念: 水浸-01 (wrong, 1 of 5 runs); 水浸（无义项的事件） (acceptable but worse, 4 of 5 runs). Better: 拆开：浸-01 :ARG2 (水). PropBank 没有「水浸」，作事件时按 guideline 2.1 应写 水浸-00；r1 的 -01 是凭空编号。r2–r5 不带义项号，却把它当事件（r2–r4 还带 aspect），概念名不合规范。gold 拆成 浸-01（ARG2 是浸在什么里）+ 水，说得通。
- [sense] 「山泥倾泻」的概念: 整词 山泥倾泻（无义项） (acceptable but worse, 4 of 5 runs). Better: 倾泻-01 :ARG1 (山泥). PropBank 有 倾泻-01（ARG1 是倾泻的东西），山泥倾泻可以按它标；要整词处理就应写 山泥倾泻-00，系统写成不带义项号的事件。
- [sense] 「形容」的义项和「五百年一遇」的角色: 形容-01 :ARG1 遇（雨势作遇的论元） (acceptable but worse, 1 of 5 runs); 形容-01，雨势 :mod 五百年一遇 (acceptable but worse, 1 of 5 runs); 形容-01 带 :ARG2 (wrong, 1 of 5 runs). Better: 形容-03 :ARG2 遇/五百年一遇. PropBank 形容-03 有 ARG2「depicted as」，「形容雨势五百年一遇」正是这个用法；形容-01 只有 ARG0、ARG1，r5 用 -01 又带 ARG2 是论元越界。r2 把评语降成雨势的修饰语，丢了「形容为」。
- [structure] 「五百年一遇」拆不拆: 整体概念 五百年一遇（无义项） (acceptable but worse, 3 of 5 runs). Better: 遇-01 + :frequency 500 年. PropBank 遇-01 的例句把「百年不遇」拆开标（遇 是 rel，百年 是 ARGM）；要整体当固定说法，作谓语时也应是 五百年一遇-00，系统写成不带义项号的概念（r4 还带 aspect）。
- [role] 「遇」的 ARG1（雨势）: 遇 :ARG0 雨势 (wrong, 1 of 5 runs). Better: 遇 :ARG1 雨势. PropBank 遇-01：ARG1 是碰上的事物，例 2「百年不遇的特大洪水」中洪水是 ARG1；被「遇」的是这场雨势，应是 ARG1。ARG0 是遇上的人/地方，r3 用错。
- [concept] 「五百年一遇」的频率写法: :frequency (temporal-quantity 500 年) (acceptable but worse, 1 of 5 runs). Better: :frequency (rate-entity-91 :ARG1 1 :ARG2 500 年). 「五百年一遇」是每 500 年 1 次，训练数据的频率用 rate-entity-91（chinese_umr-0003 第 26 句「每天播 2 集」:ARG1 2 :ARG2 (temporal-quantity 1 天)）；只写 500 年丢了「一次」，意思不完整。
- [attr] 「暴雨」带 aspect: 暴雨 :aspect process (acceptable but worse, 1 of 5 runs). Better: 暴雨 不带 aspect. 这里「暴雨」是重创-01 的 ARG0，是实体名词（概念也没有义项号），不是事件，不该带 aspect。r4 第 2 句也如此。
- [doc-modal] 当局作为「五百年一遇」的 conceiver: (当局 :full-affirmative 形容) (形容 :unspecified 遇) (wrong, 1 of 5 runs); (当局 :full-affirmative 五百年一遇)，没有 author→当局 (acceptable but worse, 1 of 5 runs). Better: (author :full-affirmative 当局) (当局 :full-affirmative 遇). 「五百年一遇」加了引号，是当局的说法。guideline 5.2：引述内容的 conceiver 是说话人，author 确信说话人，说话人确信内容。r3 把作者陈述的「形容」挂到当局下，又把内容标成 unspecified，都不对。
- [doc-temporal] 已发生事件相对文档时间（方向）: (document-creation-time :after 事件) (wrong, 4 of 5 runs); (事件 :before document-creation-time) (wrong, 1 of 5 runs). Better: (document-creation-time :before 重创). (A :after B) 是 B 在 A 之后：(document-creation-time :after 重创) 和 (重创 :before document-creation-time) 都说重创在文档时间之后，把已经发生的事标成将来。guideline 5.1：过去事件写 (document-creation-time :before e)。5 次运行全篇都这样标反（r2 用另一种写法），后面的句子不再逐句写。
- [doc-temporal] 启动、形容与重创的先后: (重创 :before 启动)：启动在重创之前 (acceptable but worse, 2 of 5 runs). 「香港启动极端情况」「当局形容」是对暴雨的反应，在重创之后或与之重叠都说得通；r4、r5 写成启动在重创之前，不合常理。guideline 5.1 事件之间的关系不清楚时可以不标。

### Sentence 2: 受  风暴   海葵   残留   云带   影响   ，  香港   各区   7  日  起  普遍   降  暴雨   ，  洪水   涌入   港铁   黄大仙    站  的  大堂   和  月台   。

Reviewer's notes on the annotator's choices:
- [concept] 根节点：and-91: 降-03 作根，涌入挂 :modifier (wrong, 1 of 5 runs). Better: and. guideline 2.5 并列用 and；and-91 不是 guideline 里的概念，但训练数据里有先例（chinese_umr-0010/0020 第 6 句），规则未定，fix 只给 low。:modifier 不是 UMR 的角色，r5 把并列的第二个小句挂成了不存在的角色。
- [role] 「各区」在降-03 里的角色: 降 :ARG0 各区 (acceptable but worse, 1 of 5 runs). Better: 降 :place 各区. PropBank 降-03 的 ARG0 是 source or agent（降雨的来源），各区是降雨的地点，用 :place。
- [structure] 「7日起」的「起」: date-entity 直接作 :temporal，没有「起」 (acceptable but worse, 5 of 5 runs). Better: 起 :op1 (date-entity :day 7). 「起」表示从 7 日开始，按项目规则时间方位词建节点；系统只写 7 日，丢了「从……起」的意思。
- [role] 「残留」的论元: 云带 :ARG1-of 残留-01 (wrong, 3 of 5 runs); 云带 :ARG1-of 残留-01，残留 :ARG0 风暴 (wrong, 1 of 5 runs); 残留 作 :mod 修饰语（无义项） (acceptable but worse, 1 of 5 runs). Better: 云带 :ARG0-of 残留-01. PropBank 残留-01 只有 ARG0（entity left over），残留下来的云带是 ARG0；ARG1 不在这个 roleset 里，r5 还把风暴当成残留的 ARG0。
- [role] 海葵和云带的关系: 云带 :poss 风暴 (acceptable but worse, 1 of 5 runs). Better: 云带 :part-of 风暴. 「风暴海葵残留云带」是海葵的残余云带：云带是风暴的一部分（或来自风暴），不是风暴造成了「残留」这件事。r2 的 :poss 是旧名（应为 :possessor），全篇如此。
- [structure] 「普遍」: 没有这个节点 (wrong, 1 of 5 runs). Better: 降 :manner 普遍. r5 漏了「普遍」。
- [role] 港铁和黄大仙站的关系: 站 :poss (organization 港铁) (acceptable but worse, 1 of 5 runs); 港铁并进站名 (acceptable but worse, 2 of 5 runs). Better: 站 :mod (organization 港铁). 黄大仙站是港铁的一个车站：站 :part 港铁 是说港铁是站的一部分，方向反了，按项目规则应为 站 :part-of 港铁（或 :mod）。「港铁」不是站名的一部分。
- [concept] 黄大仙站的实体类型: 站 作实体类型 (acceptable but worse, 4 of 5 runs). Better: station. guideline 2.1 实体类型用英文；训练数据 chinese_umr-0002 第 39 句「维多利亚站」用 station。
- [doc-coref] 第 1、2 句「暴雨」的共指: (暴雨 :same-event 暴雨) (acceptable but worse, 1 of 5 runs); 暴雨 :same-event，另有 (重创 :same-event 降) (wrong, 1 of 5 runs). Better: (s1 暴雨 :same-entity s2 暴雨). 两句说的是同一场暴雨，可以连共指；暴雨在图里是实体节点，用 :same-entity。r5 把「重创」和「降」当成同一事件，不对。
- [doc-temporal] 「7日」的时间锚定: (日期 :contained 降)，日期没有挂 (acceptable but worse, 3 of 5 runs); (日期 :before document-creation-time) (wrong, 1 of 5 runs). Better: (DCT :depends-on 日期) (日期 :contained 降). guideline 5.1：相对日期（只有日）依赖文档时间 (document-creation-time :depends-on 日期)，事件挂在它所在小句的时间表达下。gold 反过来让时间表达作降的子节点，日期本身没有锚定。r2 的写法说文档时间在 7 日之前，不对。

### Sentence 3: 邻近   地铁站    的  黄大仙    中心   是  另  一个   重灾区    ，  地下   底层   的  餐厅   8  日  被  淹没   ，  洪水   浸泡   著  扶手   电梯   ，  漂浮   着  桌椅   等  杂物   。

Reviewer's notes on the annotator's choices:
- [role] 「邻近」的论元: 中心 :ARG1-of 邻近-01 :ARG2 地铁站 (wrong, 5 of 5 runs). Better: 中心 :ARG0-of 邻近-01 :ARG1 地铁站. PropBank 邻近-01：ARG0 entity described，ARG1 entity arg0 is close to（例：邻近沙田中文大学的路轨，大学是 ARG1）。邻近-01 没有 ARG2。
- [concept] 黄大仙中心的实体类型: 中心 作实体类型 (acceptable but worse, 3 of 5 runs); 普通概念 黄大仙中心（不作命名实体） (acceptable but worse, 1 of 5 runs). Better: building :name 黄大仙 中心. 黄大仙中心是一座商场建筑，是专名，按 guideline 2.2 作命名实体，类型用英文的 building。
- [concept] 「另一个」: 重灾区 :mod 另一个（一个概念） (acceptable but worse, 4 of 5 runs); 另 :quant 1，无量词 (acceptable but worse, 1 of 5 runs). Better: 重灾区 :mod 另 :quant 1 :unit 个. 项目规则：数量写 :quant，量词保留为 :unit；「另一个」不该合成一个修饰语概念。
- [structure] 「是另一个重灾区」的判断句: 重灾区 :domain 中心 (wrong, 1 of 5 runs). Better: identity-91 :ARG1 中心 :ARG2 重灾区. guideline 2.3：X 是 Y 用 identity-91（或 have-role-91），:domain 是 AMR 的写法，UMR 不用，r4 这个节点也因此没有 aspect 和 modal。
- [role] 餐厅的处所角色名: 餐厅 :location 底层 (acceptable but worse, 1 of 5 runs). Better: 餐厅 :place 底层. 项目规则：地点用 :place，不用 :location。
- [role] 「浸泡」的论元: 浸泡 :ARG0 洪水 :ARG1 扶手电梯 (acceptable but worse, 5 of 5 runs). Better: 浸泡 :ARG1 电梯 :ARG2 洪水. PropBank 浸泡-01：ARG0 agent，ARG1 patient，ARG2 thing arg0 soaks arg1 in。洪水是电梯泡在里面的东西，是 ARG2；当成施事 ARG0 略差。
- [attr] 「浸泡着」「漂浮着」的 aspect: process (acceptable but worse, 3 of 5 runs). 「着」表示持续，guideline 4.1 表里「着」对应 activity；描写场景的「V着」也可看作状态。process 是给事件名词或类型不明的事件的，这里不合适。
- [role] 「漂浮」的处所论元: 漂浮 :place 餐厅 (acceptable but worse, 1 of 5 runs). PropBank 漂浮-01 ARG1 是处所（例：漂浮于宇宙），r1 的处所应写 ARG1 而不是 :place；处所在原文里没有明说，不写也可以。
- [structure] 「桌椅等杂物」: 杂物 :example (and :op1 桌椅)，只有一个 op (acceptable but worse, 1 of 5 runs). 训练数据两种写法都有（chinese_umr-0007 第 49 句 include-91 + and(…, 等)，chinese_umr-0001 第 13 句 :example (and … 等)）。r5 的 and 只有一个成员，没有意义。
- [doc-temporal] 「8日」的时间锚定: (8日 :contained 淹没)，日期没有挂 (acceptable but worse, 3 of 5 runs); (8日 :before document-creation-time) (wrong, 1 of 5 runs). Better: (DCT :depends-on 8日) (8日 :contained 淹没). guideline 5.1：相对日期依赖文档时间。gold 把 8 日挂在上一句的涌入下，说得通但不是首选；r2 的写法说文档时间在 8 日之前。

### Sentence 4: 香港   几乎   所有   巴士   和  电车   服务   都  暂停   数  小时   ，  直至   下午   恢复   ，  港铁   多个   站点   需要   关闭   。

Reviewer's notes on the annotator's choices:
- [concept] 「几乎所有」的写法和挂接: 服务 :quant 几乎所有（常量） (acceptable but worse, 1 of 5 runs); 服务 :quant (几乎所有)（一个概念） (acceptable but worse, 2 of 5 runs). 「几乎」修饰「所有」，拆成两个概念（AMR 的 almost :op1 all，或 所有 :mod/:degree 几乎）都可以；把「几乎所有」合成一个概念或常量不好。挂在服务还是挂在 and 上意思一样。
- [role] 香港和服务的关系: 服务 :part-of 香港 (wrong, 1 of 5 runs). Better: :place 香港. 巴士电车服务不是香港的一部分，是在香港的服务，应为 :place。
- [attr] 「暂停」的 aspect: process (acceptable but worse, 1 of 5 runs). 「暂停数小时，直至下午恢复」是已经结束的事件，performance 或 endeavor（结束而状态被撤销）都说得通；process 用于事件名词或类型不明的事件，这里不合适。
- [sense] 「恢复」的义项和论元: 恢复-01 :ARG1 服务 (wrong, 1 of 5 runs). Better: 恢复-01 :ARG0 服务. PropBank 恢复-01 只有 ARG0（例：经济增长已明显恢复，增长 是 ARG0）；恢复-02 是使恢复，ARG1 是被恢复的东西（例：牲畜头数要恢复到……，头数 是 ARG1）。恢复-01 带 ARG1 是论元越界。
- [doc-modal] 「关闭」在「需要」下的 modal: (author :full-affirmative 关闭) (acceptable but worse, 1 of 5 runs). Better: (需要 :unspecified 关闭). guideline 5.2 明确把 需要 列为带补足事件的谓词：补足事件以 需要 为父节点，强度 unspecified 或 需要 所蕴含的强度；直接写 author 肯定关闭跳过了「需要」。
- [attr] 「多个站点」的数量和量词: 站点 :quant 多 / 多个（无 :unit） (acceptable but worse, 4 of 5 runs); 站点 :quant (many) (acceptable but worse, 1 of 5 runs). Better: 站点 :quant "多" :unit 个. 项目规则：量词保留为 :unit，「多个」是 :quant 多 :unit 个；系统省掉量词（r1、r5 还把「多个」当成一个取值）。
- [doc-temporal] 暂停与恢复、需要与关闭的先后: (暂停 :before 恢复)：恢复在暂停之前 (wrong, 2 of 5 runs); (暂停 :before 恢复) (需要 :before 关闭)：两处都标反 (wrong, 3 of 5 runs). Better: (暂停 :after 恢复)：恢复在暂停之后. (A :before B) 是 B 在 A 之前。系统把「先暂停后恢复」「需要在前、关闭在后」都写成 (前 :before 后)，读法反了，和文档时间的标反是同一个习惯（全篇如此）。
- [doc-coref] 「香港」「港铁」的跨句共指: 没有共指 (wrong, 1 of 5 runs); 连香港，另有 (站点 :subset-of 黄大仙站) (acceptable but worse, 1 of 5 runs). Better: 香港、港铁都连. guideline 5.3：重复的专名连 :same-entity。r4 的 :subset-of 方向反了（是黄大仙站属于这些站点之一，而且拿不准），r3 这一句漏了共指。
- [doc-coref] 「港铁」的跨句共指: 没有共指 (acceptable but worse, 4 of 5 runs). Better: (s2 港铁 :same-entity s4 港铁). 港铁在第 2 句已经出现，按 guideline 5.3 应连共指。

### Sentence 5: 气象   机构   天文台    两小时    内  相继   发出   黄色   、  红色   和  最  高  级别   的  黑色   暴雨   警告   信号   ，  “  黑雨   ”  一共   维持   超过   16 小时   。

Reviewer's notes on the annotator's choices:
- [concept] 「气象机构天文台」: 气象机构 / 机构 作实体类型 (acceptable but worse, 3 of 5 runs). Better: organization :name 天文台 :mod 气象. 「气象机构」是同位语，说明天文台是什么机构；guideline 2.1 实体类型用英文（organization，或 government-organization），不用中文普通名词。
- [structure] 「两小时内」: :duration (temporal-quantity 2 小时) (acceptable but worse, 3 of 5 runs). Better: :temporal (within :op1 (temporal-quantity 2 小时)). 「两小时内」是一个以两小时为长度的时段：时长应是 temporal-quantity，再由「内」统领；gold 把 :quant、:unit 直接挂在「内」上，「内」本身成了数量。系统写 :duration 是说发出这件事持续两小时，意思偏了。
- [structure] 「相继」: 没有这个节点 (acceptable but worse, 2 of 5 runs). Better: 发出 :manner 相继. r3、r5 漏了「相继」。
- [structure] 三种警告信号的结构: 警告信号 :topic 暴雨 :mod (and …) (acceptable but worse, 1 of 5 runs). 「暴雨警告信号」可以拆开也可以作一个概念；r2 写成三个信号的并列最贴近原意。r4 用 :topic 连「暴雨」不对，暴雨是信号的类别，用 :mod。
- [structure] 「最高级别的黑色」: 黑色 :mod (级别 :degree 最高) (acceptable but worse, 1 of 5 runs); 最高级别（一个概念） (acceptable but worse, 2 of 5 runs). 「最高」的最高级在 AMR/UMR 里拆成 have-degree-91（ARG3 最）或 高 :degree 最；合成「最高」「最高级别」一个概念丢了结构。gold 和 r1、r4 都可以。
- [concept] 「黑雨」: 雨 :mod 黑 (acceptable but worse, 1 of 5 runs). Better: 普通概念 黑雨. 这里「黑雨」是「黑色暴雨警告信号」的简称（维持的是信号），不是一场自然灾害的专名，作命名实体不合适；r1 拆成「黑色的雨」也偏离了意思。
- [attr] 「维持」的 aspect: activity (acceptable but worse, 1 of 5 runs); endeavor (acceptable but worse, 1 of 5 runs); process (acceptable but worse, 1 of 5 runs). 「黑雨一共维持超过 16 小时」是已经结束的持续状态，state 或 performance 都说得通；activity 说它还在进行，endeavor 说它没达成结果，都不合适。
- [structure] 「超过16小时」: temporal-quantity :quant (超过 :op1 16) (acceptable but worse, 1 of 5 runs). guideline 的例子用 more-than（Part 1 例 1「more than eight months」），训练数据（chinese_umr-0002 第 59 句）用 超过-01，都可以；r4 的「超过」既不带义项又用 :op1，不规范。

### Sentence 6: 政府   又  首次   启动   极端   情况   ，  全  港  学校   停课   ，  大部分    上班族    无需   上班   。  公立   医疗   机构   医管局    指  ，  星期五    下午   有  110 人  在  暴雨   中  受伤   送院   ，  四人   情况   严重   。

Reviewer's notes on the annotator's choices:
- [structure] 「又」: 没有这个节点 (acceptable but worse, 5 of 5 runs). Better: 启动 :mod 又. 系统都漏了「又」。
- [concept] 「首次」: :ord (ordinal-entity :value 1)，无 :unit (acceptable but worse, 3 of 5 runs); :mod (ordinal-entity :value 1) (acceptable but worse, 1 of 5 runs); :mod 首次 (acceptable but worse, 1 of 5 runs). Better: :ord (ordinal-entity :value 1 :unit 次). 序数用 :ord (ordinal-entity :value 1)（guideline 2.2、Part 1 例 1），按项目规则量词「次」保留为 :unit；用 :mod 不对。
- [role] 「全港学校」: 学校 :location 港 (acceptable but worse, 1 of 5 runs); 学校 :mod 全港 (acceptable but worse, 2 of 5 runs). Better: 学校 :mod 全 :place 港. 「全港学校」是香港的所有学校：港是处所（:place），「全」是全称量。gold 的 :possessor-of 说学校拥有港，方向和角色都不对。
- [doc-modal] 「无需/不需要」的 modal: (author :full-negative 需要)，上班无 modal (acceptable but worse, 1 of 5 runs); (author :full-affirmative 需要)，需要带 :polarity - (wrong, 2 of 5 runs); (author :full-affirmative 无需)，上班无 modal (acceptable but worse, 1 of 5 runs). Better: (author :full-negative 需要) (需要 :unspecified 上班). guideline 5.2：被否定的事件是 full-negative；需要带 :polarity - 却标 full-affirmative 自相矛盾（r3、r4）。补足事件 上班 应以 需要/无需 为父节点（r1、r5 漏了）。
- [concept] 医管局的命名实体: 机构 作实体类型 (acceptable but worse, 2 of 5 runs); 普通概念 医管局 :ARG1-of (have-org-role-91 :ARG2 公立医疗机构) (wrong, 1 of 5 runs). Better: government-organization :name 医管局 + identity-91 机构. 医管局是专名，按 guideline 2.2 作命名实体，类型用英文。r5 没有作命名实体，又用 have-org-role-91（应为 -92，而且这里是同位语「公立医疗机构医管局」，不是任职关系）。
- [doc-modal] 医管局作为伤亡情况的 conceiver: (医管局 :full-affirmative 指) (指 :full-affirmative 受伤…) (acceptable but worse, 1 of 5 runs). Better: (author :full-affirmative 医管局) (医管局 :full-affirmative 受伤…). 「医管局指，……」是转述，guideline 5.2：author 确信说话人，说话人确信内容（说话人可以是人，也可以用报道事件作 conceiver）。r3 把作者陈述的「指」挂到医管局下不对。
- [sense] 「送院」的义项: 送院-01 (wrong, 5 of 5 runs). Better: 送院-00. PropBank 没有「送院」，按 guideline 2.1 写 送院-00；-01 是凭空编号。系统全篇都有这类不在 PropBank 的词编 -01 的习惯。
- [role] 「在暴雨中」受伤: 受伤 :place 暴雨 (acceptable but worse, 2 of 5 runs). 「在暴雨中受伤」既是时间（暴雨期间）也有原因义，:temporal、:cause 都可以；暴雨不是处所，:place 不合适。
- [concept] 「星期五下午」: 下午 :mod (date-entity :weekday 5) (acceptable but worse, 1 of 5 runs); 星期五 :mod 下午（不用 date-entity） (acceptable but worse, 1 of 5 runs). Better: date-entity :weekday 星期五 :dayperiod 下午. guideline 2.2：日期写 date-entity，星期用 :weekday，时段用 :dayperiod，放在同一个 date-entity 里。
- [role] 「四人情况严重」: 严重-01 :ARG1 (情况 :poss person) (wrong, 3 of 5 runs); 严重-01 :ARG1 (情况 :possessor 人) (acceptable but worse, 1 of 5 runs); have-mod-91 :ARG1 (情况 :poss person) :ARG2 严重 (acceptable but worse, 1 of 5 runs). PropBank 严重-01 只有 ARG0（thing described），情况应是 ARG0，系统的 ARG1 越界。「四人的情况」是 情况 :possessor 人；gold 的 :possessor-of 说情况领有人，方向反了。r1、r2、r5、r3 的 :poss 是旧名。
- [doc-coref] 第 1、6 句「启动极端情况」的共指: 没有共指 (acceptable but worse, 2 of 5 runs). Better: (s1 启动 :same-event s6 启动)，极端情况 :same-entity. 第 1 句「香港启动为期 16 小时的极端情况」和这句「政府又首次启动极端情况」是同一件事，按 guideline 5.3 连 :same-event，极端情况连 :same-entity。r3 只连了极端/情况，r4 把实体「极端情况」连成 :same-event。

### Sentence 7: 天文台    在  星期四    晚  十一   时  至  午夜   录得   158.1 毫米   的  每  小时   雨量   ，  创下   1884 年  有  纪录   以来   的  最高   。

Reviewer's notes on the annotator's choices:
- [concept] 「最高」: 最高（一个概念） (acceptable but worse, 5 of 5 runs). Better: have-degree-91 :ARG2 高 :ARG3 最. 最高级在 UMR/AMR 里拆成 have-degree-91 + 最（ARG3）；系统把「最高」作一个概念，丢了比较结构。
- [structure] 「星期四晚十一时至午夜」: :time 23 :00（格式断开） (wrong, 2 of 5 runs); 星期四 :mod 晚十一时至午夜（不用 date-entity） (wrong, 1 of 5 runs). Better: :temporal (date-entity :weekday 星期四 :time "23:00-24:00"). 这一小时是录得雨量的时间，是 :temporal 不是 :duration（钟点写成概念节点 23h00m 是训练数据的写法，和 guideline 不一致，这里不判）。r3、r4 的「:time 23 :00」解析成了一个空角色 :00，图坏了；r5 把整个时间短语当一个概念。

### Sentence 8: 一  河  之  隔  的  深圳   同样   受到   暴雨   影响   ，  位于   罗湖   的  深圳   火车站    ，  出入口    同样   遭遇   水浸   ，  约  一百   人  被  困  于  站内   ，  由  深圳   开往   多  地  的  列车   要  停驶   。

Reviewer's notes on the annotator's choices:
- [role] 「一河之隔」：隔-01 的论元: 深圳 :ARG1-of 隔-01，河 :ARG2 (wrong, 2 of 5 runs); 隔-01 :ARG1 深圳，河 :instrument (wrong, 2 of 5 runs); 深圳 :mod 一河之隔（一个概念） (acceptable but worse, 1 of 5 runs). Better: 深圳 :ARG0-of (隔-01 :ARG1 河). PropBank 隔-01：ARG0 theme（被隔开的一方），ARG1 entity separating members of arg0（起分隔作用的东西）。深圳是 ARG0，河是 ARG1；隔-01 没有 ARG2，:instrument 也不是论元。
- [role] 「位于罗湖」: 站 :ARG1-of 位于-01，罗湖 :ARG2 (wrong, 2 of 5 runs); 站 :place 罗湖 (acceptable but worse, 3 of 5 runs). Better: 站 :ARG0-of (位于-01 :ARG1 罗湖). PropBank 位于-01：ARG0 entity described，ARG1 location。处所是 ARG1，没有 ARG2。只写 :place 丢了谓词，可以接受。
- [concept] 罗湖的实体类型: 地名 (acceptable but worse, 1 of 5 runs). 罗湖是深圳的一个区，city-district、district 都可以；类型用英文，「地名」不是实体类型。
- [role] 「站内」和火车站: 困 :ARG2 站（没有「内」） (acceptable but worse, 1 of 5 runs); 站内 没有连到火车站 (acceptable but worse, 1 of 5 runs). Better: 站内/内 :part-of 站. 「站内」是站的内部，它作父节点时应是 :part-of 站；gold 的 :part 方向反了。
- [concept] 深圳火车站的实体类型: 火车站 / 站 作实体类型 (acceptable but worse, 3 of 5 runs); 普通概念 深圳火车站 (acceptable but worse, 1 of 5 runs). Better: station. 同第 2 句：实体类型用英文 station，专名应作命名实体。
- [role] 「开往」的论元: 列车 :ARG1-of 开往-01，深圳/地 作 ARG2–ARG4 (wrong, 2 of 5 runs); 开往-01 用 :source / :destination 或 :goal (wrong, 2 of 5 runs); 没有开往节点，列车 :source :destination (wrong, 1 of 5 runs). Better: 列车 :ARG0-of (开往-01 :ARG1 深圳 :ARG2 地). PropBank 开往-01：ARG0 theme（列车），ARG1 source（深圳），ARG2 goal（多地）。系统把列车当 ARG1、编出 ARG3/ARG4，或用 :source、:destination（不是 UMR 的角色）替代核心论元。
- [sense] 「停驶」的义项: 停驶-01 (wrong, 4 of 5 runs). Better: 停驶-00. PropBank 没有「停驶」，应为 停驶-00；-01 是凭空编号（同第 6 句「送院」）。
- [structure] 「同样」: 没有这个节点 (acceptable but worse, 1 of 5 runs). Better: 影响、遭遇各带 :mod 同样. r5 漏了两个「同样」。

### Sentence 9: 8 日  录得   465.5 毫米   的  12 小时   降雨量    ，  在  是  当地   同样   创下   有  纪录   以来   的  新高   。

Reviewer's notes on the annotator's choices:
- [doc-coref] 跨句把第 7、9 句的雨量和「创下」连成共指: (s7 雨量 :same-entity s9 降雨量) (s7 创下 :same-event s9 创下) (wrong, 1 of 5 runs). Better: 没有这类共指. 第 7 句是香港天文台的每小时雨量，第 9 句是深圳的 12 小时降雨量，是两个不同的量、两次不同的创纪录，不能连共指。

### Sentence 10: 深圳   在  星期五    午夜   表示   会  在  0 时  15 分  开始   排洪   ，  并  在  三  小时   后  加大   排洪   流量   。

Reviewer's notes on the annotator's choices:
- [structure] 「开始排洪」的「开始」: 没有 开始，排洪 直接带时间 (acceptable but worse, 1 of 5 runs). Better: 开始-01 :ARG1 排洪. 训练数据里「开始 V」都标 开始-01 :ARG1 V（chinese_umr-0005 第 14 句、chinese_umr-0003 第 20 句）；省掉开始，0 时 15 分就成了整个排洪的时间。也可以用 inceptive aspect 表达，所以只给 low。
- [concept] 「0时15分」的写法: :time 0 :15（格式断开） (wrong, 2 of 5 runs). 钟点的写法 guideline 和训练数据不一致：guideline（Part 3 date-entity 一节）写 :time 15:30 取值，训练数据写概念节点（chinese_umr-0003 第 28、31 句 :time (h19m30)），gold 跟训练数据，系统跟 guideline，规则未定，gold 记 open。r3、r4 把「0:15」拆成 :time 0 和一个空角色 :15，图坏了（第 7、11 句同样），是错。
- [structure] 「排洪流量」: 流量 :poss (新的 排洪-01 节点) (acceptable but worse, 1 of 5 runs). Better: 流量 :mod 重入前面的排洪. 「流量」是实体，不该有 aspect，也不该进 modal（gold 有 author :full-affirmative 流量）。修饰它的「排洪」可以重入前面的排洪事件或用名词。
- [doc-modal] 深圳表示的将来事件的 modal: (深圳 :partial-affirmative 开始/加大) (acceptable but worse, 3 of 5 runs); (表示 :partial-affirmative 开始/加大) (acceptable but worse, 1 of 5 runs); (深圳 :full-affirmative 表示) (表示 :full-affirmative 排洪/加大) (acceptable but worse, 1 of 5 runs). 「深圳表示会……」是转述：conceiver 应是深圳（或用「表示」作 conceiver），guideline 5.2；「会」是预测性将来，按说明是 full strength，不是 partial。r3 把作者陈述的「表示」挂在深圳下不对。最好是 (author :full-affirmative 深圳) (深圳 :full-affirmative 排洪/加大)。

### Sentence 11: 港府   在  7 日  23 时  44 分  预告   零时   排洪   ，  官员   指  是  提早   45 分钟   接获   深圳   通知   ，  并  联络   各  部门   作  准备   ，  又  表示   多区   水浸   似乎   和  排洪   没有   直接   关系   。

Reviewer's notes on the annotator's choices:
- [concept] 港府的命名实体: 普通概念 港府 (acceptable but worse, 2 of 5 runs). Better: government-organization :name 港府. 港府（香港特区政府）是一个具体机构，按 guideline 2.2 作命名实体（government-organization）。
- [concept] 钟点（23时44分、零时）的写法: :time 23 :44（格式断开） (wrong, 2 of 5 runs). 同第 10 句：钟点写成取值（guideline）还是概念节点（训练数据）未定，gold 记 open；r3、r4 的格式把图弄坏了。
- [structure] 「提早45分钟」: 提早-01 :ARG1 接获 :extent 45分钟 (acceptable but worse, 1 of 5 runs); 提早（无义项）:quant 45分钟，作 :manner / :temporal (acceptable but worse, 3 of 5 runs). PropBank 提早-01：ARG1 提前的事，ARG2 提前的量。r4 的提前量应是 ARG2 而不是 :extent；r1–r3 把「提早」当无义项的修饰语，又挂 :quant，不规范。
- [structure] 「作准备」的施事: 准备 没有 ARG0 (acceptable but worse, 1 of 5 runs). Better: 准备 :ARG0 部门. 作准备的是各部门，gold 的重入 (s11s / s11x15) 指向了修饰语「各」而不是「部门」(s11x14)。
- [structure] 「水浸和排洪没有直接关系」: 关系-01 :ARG1 水浸 :ARG2 排洪 :polarity - (wrong, 4 of 5 runs); 关联-01 :ARG1 水浸 :ARG2 排洪 (wrong, 1 of 5 runs). Better: exist-91 :ARG1 (and 水浸 排洪) :ARG2 关系 :polarity -. PropBank 关系-01：ARG0 factor，ARG1 thing influenced；应是 关系-01 :ARG0 排洪 :ARG1 水浸，系统的 ARG2 越界。gold 用 exist-91 绕开谓词，意思能表达但 exist-91 的 ARG1 应是处所，不是两件事的并列。改法要重画这部分，不写 fix。

### Sentence 12: 港府   形容   香港   的  雨势   是  “ 五百   年  一  遇  ”  ，  即  按照   过往   的  记载   雨量   ，  每年   达到   如此   雨势   的  概率   在  千分之二     ，  难  以  大幅   提早   应对   。

Reviewer's notes on the annotator's choices:
- [sense] 「形容」的义项: 形容-01 带 :ARG2 (wrong, 1 of 5 runs); 形容-01 :ARG1 遇（雨势作遇的论元） (acceptable but worse, 1 of 5 runs); 形容-01，雨势 :mod 五百年一遇 (acceptable but worse, 1 of 5 runs). Better: 形容-03 :ARG2 遇/五百年一遇. PropBank 形容-01 只有 ARG0、ARG1，形容-03 才有 ARG2「depicted as」；gold 第 1 句同一说法用的是 形容-03，这里用 -01 带 ARG2 是论元越界。
- [role] 「香港的雨势」的领属方向: 雨势 :poss 香港 (acceptable but worse, 4 of 5 runs). Better: 雨势 :possessor 香港. 「香港的雨势」是 雨势 :possessor 香港；gold 的 :possessor-of 说雨势领有香港，方向反了。:poss 是旧名（全篇如此）。
- [role] 「遇」的 ARG1（雨势）: 遇 :ARG0 雨势 (wrong, 1 of 5 runs). Better: 遇 :ARG1 雨势. 同第 1 句：PropBank 遇-01 例句「百年不遇的特大洪水」中洪水是 ARG1，这里被「遇」的是雨势。
- [doc-modal] 「五百年一遇」的 conceiver: (形容 :unspecified 遇) (wrong, 1 of 5 runs). Better: (港府 :full-affirmative 遇). 同第 1 句：「五百年一遇」是港府的说法，guideline 5.2 内容的 conceiver 是说话人。
- [structure] 「即……」与前文的关系: 三个小句平铺 and (acceptable but worse, 4 of 5 runs); 形容 :ARG1-of (cause-01 :ARG0 难) (wrong, 1 of 5 runs). Better: 形容 :ARG1-of (have-reason-91 :ARG2 (概率……)). 「即按照过往记载，每年达到如此雨势的概率在千分之二」是对「五百年一遇」的解释和依据，gold 用 have-reason-91（训练数据常用）表示；平铺丢了这层关系。r5 说「难以应对」造成了「形容」，因果颠倒。
- [concept] 「千分之二」的写法: have-mod-91 :ARG2 千分之二 / 概率 :quant 千分之二 (acceptable but worse, 2 of 5 runs). Better: percentage-entity :value 0.2. 千分之二是 0.2%，AMR/UMR 的百分比写 percentage-entity :value 0.2；rate-entity-91 是频率（每多少时间几次），不是概率值。
- [role] 「达到」的论元: 达到 :ARG0 雨势 (wrong, 2 of 5 runs). Better: 达到 :ARG1 雨势. PropBank 达到-01：ARG0 theme（达到者），ARG1 point reached（达到的程度）；「达到如此雨势」里「如此雨势」是达到的点，应为 ARG1。
- [structure] 「难以大幅提早应对」: 难-01 :ARG1 应对 (wrong, 5 of 5 runs). PropBank 难-01 只有 ARG0（thing described），应为 难-01 :ARG0 应对；系统都用了不存在的 ARG1。gold 把「难以」写成否定，说成「不能应对」过头了，「难」的事件 modal 也应以 难 为父节点（partial-negative 一类）。
- [doc-coref] 第 1、12 句「形容雨势五百年一遇」的共指: 没有共指 (acceptable but worse, 2 of 5 runs). Better: 形容 :same-event，雨势 :same-entity. 第 1 句「当局形容雨势五百年一遇」和这句是同一次表态，雨势也是同一个（guideline 5.3）。r3、r4 只连了雨势。

### Sentence 13: 政务司    司长   陈国基    说  ，  “ 对于   这场   大雨   ，  雨势   非常   非常   大  ，  正如   同事   提及   ，  它  是  五百   年  一  遇  ，  雨  又  大  又  突然   ，  可  预测   程度   很  低  ，  所以   我们   无法   如  应对   之前   的  台风   苏拉   般  大幅   提早   预告   。”

Reviewer's notes on the annotator's choices:
- [concept] 「政务司司长」的任职结构: have-org-role-92，陈国基作 :ARG0，:ARG2 政务司 :ARG3 司长 (acceptable but worse, 1 of 5 runs); have-org-role-92，陈国基作 :ARG0，司长作 :ARG2 (wrong, 3 of 5 runs); have-org-role-91 :ARG2 政务司司长 (wrong, 1 of 5 runs). 项目规则：用 have-org-role-92；guideline 2.3：ARG1 是任职者，ARG2 是机构，ARG3 是职位。系统（r1–r4）一律把人写成 :ARG0-of，又常把职位放进 ARG2，这是全篇反复的错误；gold 的结构对，只是用了 -91。
- [structure] 「雨势非常非常大」: 大-01 :ARG1 雨势 :degree 非常 (wrong, 4 of 5 runs). PropBank 大-01：ARG0 thing described，ARG1 size of arg0；雨势是 ARG0，系统用 ARG1 不对。程度副词「非常」按项目规则是 :degree；gold 的 have-degree-92 不是 guideline 里的概念。正确写法是 大-01 :ARG0 雨势 :degree 非常。
- [role] 雨势和「这场大雨」的关系: 雨势 :mod 这场大雨（一个概念） (acceptable but worse, 1 of 5 runs). 「对于这场大雨，雨势非常非常大」：雨势是这场大雨的雨势（雨势 :possessor 大雨），或把大雨作话题 :topic。gold 的 :possessor-of 说雨势领有大雨，方向反了。
- [concept] 「五百年一遇」的频率概念: :frequency (temporal-quantity 500 年) (acceptable but worse, 1 of 5 runs). Better: :frequency (rate-entity-91 :ARG1 1 :ARG2 500 年). 频率的抽象概念是 rate-entity-91（训练数据 chinese_umr-0003 第 26 句），gold 漏了 -91；第 12 句 gold 自己写的是 rate-entity-91。
- [role] 单论元形容词谓语（大、突然、低）的论元: :ARG1 (wrong, 4 of 5 runs). Better: :ARG0. PropBank 大-01、突然-01、低-01 的描述对象都是 ARG0（thing / entity described），只有 低-01 另有 ARG1「比什么低」。系统一律写 ARG1，第 6 句 严重-01、第 2 句 残留-01 也是这样，是全篇反复的错误。
- [structure] 「无法」: 预告 :polarity - (acceptable but worse, 2 of 5 runs). PropBank 有 无法-01（ARG0 entity，ARG1 content）；「无法预告」是不能预告，直接否定预告丢了能力义。可以接受但略差。
- [role] 「如应对之前的台风苏拉般」: :compared-to 应对 (acceptable but worse, 3 of 5 runs); 预告 :ARG1-of 应对 (wrong, 1 of 5 runs); 预告 :manner 应对 (acceptable but worse, 1 of 5 runs). 「如……般」是比较：不像应对苏拉时那样大幅提早。:compared-to 不在 UMR 的角色表里，:example 也不贴切；r4 把预告当成应对的 ARG1 是错的。拿不准哪个最好。
- [doc-modal] 引语内容的 conceiver: (陈国基 :full-affirmative 说) (说 :… 事件) (acceptable but worse, 1 of 5 runs). Better: (author :full-affirmative 陈国基) (陈国基 :… 事件). 引号里是陈国基的话，guideline 5.2：引述内容的 conceiver 是说话人。r3 把作者陈述的「说」挂到陈国基下不对。

### Sentence 14: 政府   清晨   五时半    宣布   启动   “极端   状况   ” ，  要求   所有   学校   停课   ，  但  只  “  呼吁   ”  雇主   要  “  参考   ”  台风   情况   作  弹性   工作   安排   ，  直至   早上   七时   许  才  另发   指引   指  不  应  要求   必要   人员   外  的  雇员   返回   工作   地点   。  当局   解释   指引   是  “  补充   资料   ”  ，  又  指  机制   行之有效     ，  没有   正面   回应   为何   不  在  启动   极端   情况   时  一并   作出   要求   。

Reviewer's notes on the annotator's choices:
- [concept] 「但」的概念: contrast-01 (acceptable but worse, 3 of 5 runs); but :op1 :op2 (acceptable but worse, 1 of 5 runs). guideline 2.5：转折用 contrast-91 :ARG1 :ARG2，「但是」也可以写 but-91；contrast-01 是 AMR 的写法，UMR 里没有；but 带 :op 也不合格式。
- [sense] 「要求所有学校停课」的义项: 要求-02 :ARG1 停课 (wrong, 1 of 5 runs). PropBank 要求-02：ARG1 是被要求的一方，ARG2 是要求做的事（predicate）；要求-01 的 ARG1 是要求的事物。r2 用 -02 却把事件放在 ARG1，论元错位。
- [doc-modal] 呼吁内容的 modal: (author :neutral-affirmative 参考) (acceptable but worse, 1 of 5 runs); 没有标参考的 modal (acceptable but worse, 2 of 5 runs). Better: (呼吁 :unspecified 参考) 一类. guideline 5.2：呼吁（希望、要求一类）的内容以呼吁为父节点，强度 unspecified 或它蕴含的强度；作者并没有说雇主真的参考、作了安排。
- [sense] 「另发指引」的义项: 发出-01 (acceptable but worse, 3 of 5 runs); 发-02 (acceptable but worse, 1 of 5 runs); 另发-01 (wrong, 1 of 5 runs). Better: 发-01 :mod 另. 原文是「另发」：PropBank 发-01（issuer / article）最合适；发出-01 换了词；发-02 是寄送（有接收者）；「另发」不在 PropBank，r5 的 -01 是编的。
- [structure] 「指引指……」: 指引 :topic 要求 (acceptable but worse, 1 of 5 runs); 指引 :ARG1-of 指-02 (wrong, 1 of 5 runs). Better: 指引 :ARG0-of (指-02 :ARG1 要求). 「另发指引指不应要求……」的「指」是指出（PropBank 指-02 ARG0 agent，ARG1 thing pointed out），指引是 ARG0；gold 用 identity-91 说指引「就是」这个要求，丢了谓词，r5 把指引当成被指出的内容。
- [doc-modal] 「不应要求」的 modal: 应-01 :polarity -，(author :full-negative 要求) (acceptable but worse, 1 of 5 runs). Better: partial-negative（挂在政府/指/作者下）. guideline 5.2：「应该」类是 partial-affirmative，「不应」是 partial-negative；gold 写成作者断定没有要求（full-negative），丢了「应」。
- [role] 「必要人员外的雇员」: 雇员 :ARG1-of (except-01/exclude-01 :ARG2 人员) (acceptable but worse, 3 of 5 runs); 雇员 :mod (外 :op1 人员) (acceptable but worse, 1 of 5 runs); 雇员 :exception 人员 (wrong, 1 of 5 runs). Better: 雇员 :subtraction 人员. 完整 guideline（contrast 一节）用 :subtraction 表示「除……外」，训练数据 chinese_umr-0004 第 2 句「除了……外」也用 :subtraction。except-01 是英文 roleset，:exception 不是 UMR 角色。
- [role] 「返回工作地点」的论元: 返回 :ARG4 地点 (wrong, 4 of 5 runs). PropBank 返回-01：ARG0 returner，ARG1 return to。:ARG4 是英文 return-01 的终点论元，中文 返回-01 没有；r2、r3、r5 还把返回者放在 ARG1。
- [role] 当局「解释」的论元: 解释 :ARG1 (identity-91 …) (acceptable but worse, 1 of 5 runs); 解释 :ARG1 (资料 :domain 指引) (wrong, 2 of 5 runs). PropBank 解释-01 ARG1 是被解释的事物（指引），ARG3 是给出的解释（「是补充资料」）。:domain 不是 UMR 的角色，判断句应写 identity-91（guideline 2.3）。
- [role] 「行之有效」的论元: 行之有效-01 :ARG1 机制 (wrong, 4 of 5 runs). Better: 行之有效-01 :ARG0 机制. PropBank 行之有效-01 只有 ARG0（thing described）。同第 13 句：单论元谓词系统一律写 ARG1。
- [role] 「没有正面回应为何……」: 回应 :ARG1 为何（概念） :mod 正面 (acceptable but worse, 1 of 5 runs). PropBank 回应-01：ARG1 是回应的对象（「为何不……」这个问题），ARG2 是回应的内容；没有回应的是这个问题，ARG1 更合适。「正面」修饰动作，用 :manner（r1、r4、r5 用 :mod）。r2 写 amr-unknown 是旧名，应为 umr-unknown。

### Sentence 15: 使用   一亿五千万      港元   搭建   的  紧急   短讯   系统   ，  在  暴雨   中  没有   被  使用   ，  政务司    副  司长   卓永兴    说  ，  “  我  认为   所有   清醒   的  公众   都  知道   下  暴雨   ，  所以   没有   必要   用  紧急   短讯   系统   发信   告知   市民   如此   明显   的  情况   。”

Reviewer's notes on the annotator's choices:
- [role] 「搭建」与费用的关系: 搭建 :ARG2 (monetary-quantity …) (wrong, 1 of 5 runs). PropBank 搭建-01 只有 ARG0、ARG1，r5 的 ARG2 越界。r4 用「钱」代替 monetary-quantity 也不规范。
- [concept] 「政务司副司长」的任职结构: have-org-role-91 :ARG2 政务司副司长 (wrong, 1 of 5 runs). 项目规则：用 have-org-role-92，ARG1 任职者、ARG2 机构、ARG3 职位。系统把人写成 ARG0 的习惯见第 13 句。
- [sense] 「下暴雨」的谓词: 降-03 :ARG1 暴雨 (wrong, 5 of 5 runs). Better: 下-05 :ARG0 暴雨. 原文是「下暴雨」，PropBank 有 下-05（ARG0 rain），应按原词标；系统换成第 2 句的 降-03，概念和原文不符。
- [sense] 「没有必要」: 必要-01 :ARG1 发信/使用 :polarity - (wrong, 2 of 5 runs); 需要-01 / 需要-02 :polarity - (acceptable but worse, 2 of 5 runs); 没有必要-01 (wrong, 1 of 5 runs). Better: 必要-01 :ARG0 告知 :polarity -. PropBank 必要-01 只有 ARG0（what is necessary），系统用 ARG1 越界；「没有」是否定，应写 :polarity -，「没有必要-01」不是 PropBank 的词条；换成 需要 改了原词。
- [structure] 「用紧急短讯系统发信告知」: 发信-01 :ARG1 系统 (wrong, 1 of 5 runs). Better: 发信-01 :instrument 系统 :purpose 告知. 原文「用紧急短讯系统发信告知市民」有发信这个动作；gold 省掉了。PropBank 发信-01 的 ARG1 是收信人，r5 把系统放在 ARG1 不对。
- [role] 「告知」的论元: 告知 :ARG1 市民 :ARG2 情况 (wrong, 1 of 5 runs). Better: 告知 :ARG1 情况 :ARG2 市民. PropBank 告知-01：ARG1 是告知的内容，ARG2 是被告知的人。
- [role] 「清醒的公众」「明显的情况」: :ARG1-of 清醒-01 / 明显-01 (wrong, 3 of 5 runs). PropBank 清醒-01、明显-01 只有 ARG0（entity / thing described），作修饰时写 :ARG0-of 或直接 :mod；系统写 :ARG1-of 越界（同第 13 句的习惯）。「如此明显」的「如此」是程度，按项目规则用 :degree，gold 用 :mod。
- [doc-modal] 卓永兴的话的 modal: (卓永兴 :full-affirmative 说) (acceptable but worse, 1 of 5 runs). Better: (author 说)(author 卓永兴)(卓永兴 认为)…. guideline 5.2：author 确信说话人和「说」，说话人确信引语内容。gold 漏了「说」「认为」的 modal，又把「知道」「没有必要」同时挂在 author 和卓永兴下，conceiver 重复。
- [role] 「在暴雨中」没有被使用: 使用 :place 暴雨 (acceptable but worse, 2 of 5 runs). Better: 使用 :temporal 暴雨. 同第 6 句：「在暴雨中」是时间，暴雨不是处所。

## Document zh-0018 (5 runs)

### Sentence 1: 世界   中央   厨房   车队   加沙   遇袭   案  是  指  2024 年  4  月  1  日  晚  以色列    国防军    对  人道主义     组织   世界   中央   厨房   的  车队   连续   进行   的  3  次  无人机    空袭   事件   ，  当时   该  车队   正在   加沙   地带   中部   城市   代尔拜莱赫      提供   人道   粮食   援助   。

Reviewer's notes on the annotator's choices:
- [concept] 「是指」的根概念: 指-01 :ARG0 遇袭 :ARG1 空袭 (wrong, 1 of 5 runs). Better: 指-01 :ARG1 案/遇袭 :ARG2 空袭. 「是指」是「指」的用法，PropBank 指-01 的例句「这是指外企的中方管理人员」正是 ARG1 = 被解释的东西、ARG2 = 所指对象；用 identity-91 把「指」丢掉不算错，但不如直接用 指-01。r5 把 ARG0（agent）给了「遇袭」，不合 指-01 的论元。
- [structure] 「遇袭案」中「案」的处理: 案 :ARG1-of 遇袭-01 (wrong, 2 of 5 runs); 不建 案 节点，遇袭 直接作 指 的论元 (acceptable but worse, 3 of 5 runs). 训练数据 chinese_umr-0002 第 25 句「爆炸案」写作 (案 :mod 爆炸-01)，「遇袭案」同理应为 案 :mod 遇袭。r3/r4 让「案」做遇袭的 ARG1，而遇袭已有 ARG1 车队，「案」不是被袭击的对象，错；gold 用 identity-91 连接也不是同位关系，略差；系统丢掉「案」略差。
- [sense] 「遇袭」的义项: 遇袭-01 (wrong, 5 of 5 runs). Better: 遇袭-00. PropBank 没有「遇袭」（look.py pb 遇袭：Not in PropBank），按 guideline 2.1 写 遇袭-00；-01 是凭空编号。
- [role] 车队与「世界中央厨房」的所属关系: 车队 :mod 机构 (acceptable but worse, 3 of 5 runs); 车队 :poss 机构 (acceptable but worse, 2 of 5 runs). guideline 4062 行：所属关系「possessum 作父节点、possessor 作子节点」，应为 (车队 :possessor 机构)，gold 的 :possessor-of 方向相反；但中文训练数据普遍写「被领有者 :possessor-of 领有者」（zh-0011 第 24 句 自由 :possessor-of 女子、zh-0017 第 12 句 地区 :possessor-of 该邦等），guideline 与训练数据冲突，说明里没有定规则，gold 记 open。系统 :poss 方向对但是旧拼写；:mod 把所属当类型修饰，略差。
- [structure] 同位语「人道主义组织」: 机构 :mod (组织 :mod 人道主义) (acceptable but worse, 1 of 5 runs); 机构 :mod 人道主义（丢掉 组织） (acceptable but worse, 2 of 5 runs); 没有标「人道主义组织」 (wrong, 2 of 5 runs). Better: 机构 :ARG1-of (identity-91 :ARG2 (组织 :mod 人道主义)). 同位语用 identity-91 是中文训练数据的写法（chinese_umr-0007 第 4 句 剑持勇 :ARG1-of (identity-91 :ARG2 刑事)）。r4 用 :mod 挂同位名词略差，r3/r5 丢掉「组织」，r1/r2 整个同位语都没标。
- [attr] 「3次」空袭的数量与量词: 空袭 :frequency 3（无量词） (acceptable but worse, 1 of 5 runs); 空袭 :quant 3（无量词） (acceptable but worse, 4 of 5 runs). Better: 空袭 :frequency 3 :unit 次. 项目规则：量词一律保留为 :unit，省掉判 minor（5 个系统全篇都省量词，这里第一次出现，之后同一习惯不再逐条判）。:frequency 与 :quant 计事件次数都说得通。
- [role] 「无人机」与空袭的关系: 空袭 :mod 无人机 (acceptable but worse, 2 of 5 runs); 没有标「无人机」 (wrong, 1 of 5 runs). Better: 空袭 :instrument 无人机. 无人机空袭中无人机是实施空袭的工具，用 :instrument（guideline 非论元角色表）；:mod 只表达类型修饰，略差；r3 漏掉。
- [role] 「连续」的处理: 空袭 :mod 连续 (acceptable but worse, 1 of 5 runs); 没有标「连续」 (wrong, 3 of 5 runs). Better: 空袭 :manner 连续. 「连续进行」是副词性修饰事件，按说明用 :manner；r5 用 :mod 略差，r1/r2/r4 漏标。
- [structure] 「当时…提供援助」的挂接: 空袭 :temporal 提供，提供 :mod 当时 (acceptable but worse, 1 of 5 runs); 指 :other-role 提供，提供 :temporal 当时 (wrong, 1 of 5 runs); 指 :temporal (当时 :mod 提供) (wrong, 1 of 5 runs). Better: 空袭 :temporal 提供（不建 当时）. 「当时该车队正在…提供援助」说明的是空袭发生时的背景，应挂在空袭上（:temporal 事件）。「当时」回指空袭时间，由 :temporal 关系本身表达；r2 另把它挂成 :mod 多余；r1 用 :other-role 挂在「指」上、r4 把它作为「指」的时间，都挂错了事件。
- [attr] 「正在提供」的 aspect: process (acceptable but worse, 2 of 5 runs). Better: activity. 「正在」表进行，abridged 4.1：正在、着 → activity；谓语性事件不该用事件名词的 process。
- [sense] 「人道粮食援助」: 援助-01 :mod 粮食 (acceptable but worse, 2 of 5 runs); 援助（不带义项）:mod 粮食 (acceptable but worse, 3 of 5 runs). Better: 援助-01 :ARG1 粮食 :mod 人道. PropBank 援助-01 ARG1 theme，粮食是援助的内容，应作 ARG1；guideline 2.1 事件名词按事件标，带义项更好。
- [role] 代尔拜莱赫、中部、加沙地带的部分整体关系: 城市 :place 中部 :part-of 加沙 (acceptable but worse, 1 of 5 runs); 城市 :place (加沙地带 :mod 中部) (acceptable but worse, 1 of 5 runs); 城市 :part-of (加沙地带 :mod 中部) (acceptable but worse, 1 of 5 runs); 城市 :mod 中部 :part-of 加沙地带 (acceptable but worse, 1 of 5 runs). Better: 城市 :part-of 中部 :part-of 加沙地带. 项目规则：部分作父节点用 :part-of。城市在中部之内、中部是加沙地带的一部分，gold 写成 :part 方向配反（训练数据 chinese_umr-0003 第 2 句 city :part-of local-region）。r2–r5 把「中部」挂成 :mod 或用 :place 表达包含，略差。
- [concept] 「加沙」的实体类型: place (acceptable but worse, 3 of 5 runs); geographic-entity (acceptable but worse, 1 of 5 runs); 地区（中文类型名） (wrong, 1 of 5 runs). Better: local-region. guideline Table 5：region 类下有 local-region；place 不在类型表，geographic-entity 是自然地理实体的类；abridged 2.1 实体类型要用英文，r1 用中文「地区」作类型错。
- [concept] 「加沙地带」的实体类型: region (acceptable but worse, 1 of 5 runs); place (acceptable but worse, 1 of 5 runs); 地带（中文类型名） (wrong, 2 of 5 runs); 没有单独的加沙地带节点（借用加沙） (acceptable but worse, 1 of 5 runs). Better: local-region. 同上：local-region 在类型表内；region 是上位类，place 不在表内；用中文「地带」作类型且它又是名字的一部分，错。
- [doc-temporal] 日期相对文档时间: (document-creation-time :after 日期) (wrong, 3 of 5 runs). (A :after B) 表示 B 在 A 之后，r1/r2/r5 的写法说 2024年4月1日在文档时间之后，读反了（abridged 5.1：关系说的是子节点相对父节点）。项目规则接受日期挂 root 或 (document-creation-time :before …)。
- [doc-coref] 句内 coref: (遇袭 :same-event 空袭) (acceptable but worse, 2 of 5 runs); (遇袭 :same-event 空袭) 外加 (空袭 :same-entity 空袭) 自指 (wrong, 1 of 5 runs); 两份重复的 车队、机构 节点之间 :same-entity (acceptable but worse, 1 of 5 runs). abridged 5.3：句内共指用重入，不写 :coref 三元组；遇袭与空袭的等同已由「是指」的论元结构表达。r3 还写了节点指向自身的三元组，错。

### Sentence 2: 这场   袭击   致使   车队   的  7 名  人道   工作者    全员   身亡   。

Reviewer's notes on the annotator's choices:
- [structure] 「致使」的表达: 致使-01 :ARG0 袭击 :ARG1 身亡 (acceptable but worse, 1 of 5 runs). 训练数据 chinese_umr-0002 第 2 句把「致使」写成因果关系、不建节点；have-cause-91 :ARG1 结果 :ARG2 原因 是 chinese_umr-0011 的写法；用 PropBank 致使-01（ARG0 causer / ARG1 causee / ARG2 proposition）也对。r5 把命题放在 ARG1（causee）上，略差。
- [concept] 「工作者」的概念: person :ARG0-of 工作-01 (acceptable but worse, 2 of 5 runs). Better: 工作者. abridged 2.1：实体名词按原词作概念；「工作者」是普通名词，拆成 person + 工作-01 是过度分解。
- [role] 工作者与车队的关系: 工作者 :poss 车队 (acceptable but worse, 1 of 5 runs). 工作者是车队的成员，部分作父节点应用 :part-of（项目规则），gold 方向配反；:possessor 也可接受；:poss 是旧拼写。
- [structure] 「全员」: 身亡 :mod 全员 (acceptable but worse, 3 of 5 runs); 身亡 :extent 全员 (acceptable but worse, 1 of 5 runs). Better: 工作者 :mod 全员. 「全员身亡」说的是 7 人全部，是对参与者的全称量化，挂在工作者上（如 AMR all 作 :mod）；挂在事件上用 :mod 或 :extent 都不如前者。gold 漏掉这个词。
- [role] 「身亡」的论元: 身亡 :ARG1 工作者 (wrong, 1 of 5 runs). Better: 身亡 :ARG0 工作者. PropBank 身亡-01 只有 ARG0（entity described）。
- [doc-temporal] 身亡与袭击（第 1 句空袭）的先后: (空袭 :before 身亡/致使)：身亡在空袭之前 (wrong, 3 of 5 runs); (空袭 :after 袭击)：同一事件排成先后 (wrong, 1 of 5 runs). (A :before B) 表示 B 在 A 之前；r1/r4/r5 的写法说身亡发生在空袭之前，读反了。r2 把与第 1 句空袭同指的「这场袭击」排在空袭之后，与它自己的 same-event 矛盾。

### Sentence 3: 事件   发生   后  ，  世界   中央   厨房   宣布   暂停   其  在  加沙   地带   的  人道   援助   行动   ，  并  指出   ，  “  将  粮食   作为   战争   武器   ”  以及   “  对  人道   援助者    进行   袭击   ”  的  行为   是  不可   饶恕   的  ，  世界   各国   领袖   表示   震惊   并  谴责   空袭   事件   。

Reviewer's notes on the annotator's choices:
- [structure] 「人道援助行动」: 行动 :mod (援助 :mod 人道) (acceptable but worse, 2 of 5 runs); 行动 :mod 人道 :mod 援助 (acceptable but worse, 1 of 5 runs); 行动 :mod 人道援助（合为一个节点） (acceptable but worse, 1 of 5 runs). abridged 2.1：事件名词按事件标，「行动」「援助」都在 PropBank（行动-01、援助-01）；不带义项的写法略差。r2 把两个词合成一个概念「人道援助」也不合切分。
- [structure] 「事件发生后」: 宣布 :temporal 发生（没有 后/after） (acceptable but worse, 1 of 5 runs). 项目规则：时间方位词「后」建节点是对的；用抽象概念 after 表达同样的先后也可接受。r2 丢了「后」，只剩时间重叠的含义。
- [role] 「发生」的论元: 发生 :ARG1 事件 (wrong, 4 of 5 runs). Better: 发生 :ARG0 事件. PropBank 发生-01：ARG0 accident, event（发生的事），ARG1 happening to（事情发生在谁身上）。「事件发生」的事件是 ARG0。
- [structure] 「…的行为」的结构: 行为 :mod (and 作为 袭击) (acceptable but worse, 1 of 5 runs); 行为 :ARG1-of 作为、:ARG1-of 袭击 (wrong, 1 of 5 runs). 「行为」是类名中心词，用 identity-91 把两个行为与它等同，或省去中心词都可以；r3 用 :mod 略差；r2 让「行为」做 作为-01 和 袭击-01 的 ARG1，但这两个事件的 ARG1 分别是粮食和援助者，错。
- [concept] 「人道援助者」: person :ARG0-of 援助-01 (acceptable but worse, 3 of 5 runs). Better: 援助者 :mod 人道. abridged 2.1：实体名词按原词作概念，「援助者」不必拆成 person + 援助-01（同第 2 句「工作者」）；r4 还丢了「人道」。
- [structure] 「不可」是否建节点: 饶恕 :mod 可 + :polarity - (acceptable but worse, 1 of 5 runs). Better: 不建节点，只在饶恕上标 :polarity -. abridged 2.1：情态助词（能、可以、应该）不建节点，只影响 modal 强度。
- [doc-modal] 「指出」内容的 conceiver 与强度: (指出 :full-affirmative 饶恕)，与 :polarity - 矛盾 (wrong, 1 of 5 runs); (机构 :full-affirmative 饶恕)，与 :polarity - 矛盾；作为/袭击 没有 modal (wrong, 1 of 5 runs). abridged 5.2：引述内容由说话人作 conceiver（author 确信说话人，说话人对内容），否定的事件是 full-negative。gold 把「指出」的内容直接挂在 author 下；r4/r5 对带 :polarity - 的饶恕给了 full-affirmative。
- [doc-modal] 「暂停」的 modal: (宣布 :partial-affirmative 暂停) (acceptable but worse, 1 of 5 runs). 宣布暂停是施为性的宣告，作者当作事实陈述或由宣布者作 conceiver 都可以；没有依据把它降为 partial-affirmative。
- [concept] 「领袖」的概念: person :ARG0-of 领导-01 (acceptable but worse, 1 of 5 runs); person :ARG0-of 领袖-01 (wrong, 1 of 5 runs). Better: 领袖. PropBank 没有「领袖」（Not in PropBank），训练数据（chinese_umr-0007 第 13 句、chinese_umr-0004 第 55 句）都把「领袖」作普通名词概念；r4 的 领袖-01 是凭空编号。
- [role] 「世界各国」中世界与国的关系: 国 :mod 世界 / 领袖 :mod 世界 (acceptable but worse, 5 of 5 runs). 国是世界的一部分，部分作父节点应用 :part-of（项目规则），gold 方向配反；系统都用 :mod，也没表达出部分整体关系。
- [role] 领袖与各国的所属关系: 领袖 :poss 国 (acceptable but worse, 1 of 5 runs); 领袖 :mod 各国 (acceptable but worse, 3 of 5 runs). 与第 1 句同一问题：guideline 要求 (领袖 :possessor 国)，gold 的 :possessor-of 方向相反，但训练数据普遍写 :possessor-of，待项目负责人定。系统 :mod 略差，:poss 是旧拼写。
- [structure] 「表示震惊」中的「震惊」: 表示 :ARG1 (and 震惊-01 谴责)，震惊 另带 :ARG2 空袭 (acceptable but worse, 1 of 5 runs). Better: 表示 :ARG1 (震惊-01 :ARG1 领袖). PropBank 表示-01 ARG1 message expressed，震惊-01 ARG1 people shocked by arg0（ARG0 是令人震惊的事物，没有 ARG2）。gold 漏掉「震惊」这个事件。
- [doc-temporal] 宣布、暂停、表示相对事件发生的先后: 先后对，但 (document-creation-time :after 表示) 把表示放到文档时间之后 (wrong, 1 of 5 runs); (发生 :before 宣布)、(宣布 :before 暂停)：宣布在发生前、暂停在宣布前 (wrong, 2 of 5 runs); (宣布 :after 发生)、(宣布 :before 暂停/指出/表示) (wrong, 1 of 5 runs). (A :before B) 表示 B 在 A 之前。r1/r5/r4 的写法都说宣布在事件发生之前、暂停在宣布之前，与原文「事件发生后…宣布暂停」相反，是把 :before/:after 读反的习惯；r2 的主体关系对，但把已发生的「表示」放到了文档时间之后。
- [doc-coref] 跨句共指：机构、加沙地带、空袭: 机构、空袭 连上，但把「发生」也当作与空袭同一事件 (acceptable but worse, 2 of 5 runs); 机构、加沙、空袭 连上，空袭三元组正反写了两遍 (acceptable but worse, 1 of 5 runs); 连上，但有 (宣布 :same-event 宣布) 自指 (wrong, 1 of 5 runs). abridged 5.3：重复提到的实体、事件要连 :same-entity / :same-event。gold 第 3 句一条 coref 都没有；r2/r3 把「发生-01」与空袭同指不对（同指的是「事件」）；r5 有指向自身的三元组。

### Sentence 4: 虽然   以色列    立刻   承认   责任   并  道歉   ，  但  以方   坚持   这次   空袭   是  因为   误  以为   车队   中  混入   了  哈马斯    武装   成员   而  导致   的  “  不幸   意外   ”  。

Reviewer's notes on the annotator's choices:
- [concept] 「虽然…但」的概念: contrast-91 (acceptable but worse, 2 of 5 runs). guideline 第 2473 行：「虽然」表示让步（unexpected co-occurrence），用 have-concession-91 或 :concession；训练数据的「虽然…但」多写 but-91（chinese_umr-0005 第 10 句、chinese_umr-0001 第 17 句）；guideline 例句也用 contrast-01 表 but。contrast-91 是没有意外义的纯对比（第 2423 行），不合本句。
- [structure] 「以方」的处理: 以方 :refer-to 以色列（自造角色） (wrong, 1 of 5 runs); 另建命名实体 country「以方」 (acceptable but worse, 1 of 5 runs); 方 :mod 以，再用句内 coref 连 以色列 (acceptable but worse, 1 of 5 runs). Better: 不另建节点，坚持 :ARG0 重入 以色列. 「以方」就是以色列，句内同指用重入（abridged 5.3）。:refer-to 不是 UMR 角色；「以方」不是专名，作 name 不对；r5 拆成 方 :mod 以 并写句内 coref 也不合规范。
- [structure] 「因为…而导致」的表达与挂接: 意外 :ARG1-of (cause-01 :ARG0 误以为) (acceptable but worse, 1 of 5 runs); identity-91 :ARG1-of (cause-01 :ARG0 以为) (acceptable but worse, 1 of 5 runs); 坚持 :ARG1 (意外 :ARG1-of (cause-01 :ARG0 以为 :ARG1 空袭))，cause-01 有两个 ARG1 (wrong, 1 of 5 runs). Better: 意外 :ARG1-of (导致-01 :ARG0 以为). 原文有「导致」，PropBank 导致-01（ARG0 cause / ARG1 result）在列，应用中文义项而不是英文 cause-01。r1 把原因挂在 identity-91 上而不是被导致的「意外」；r4 去掉了 identity-91，cause-01 同时带了两个 ARG1。
- [sense] 「误以为」的切分与义项: 以为-01 :mod 误 (acceptable but worse, 2 of 5 runs); 误以为-01 (wrong, 3 of 5 runs). Better: 以为-01 :manner 误. 分词是「误 / 以为」两个词，PropBank 有 以为-01（ARG1 thing arg0 thinks to be true），没有「误以为」；合成一个概念就该写 -00，误以为-01 是凭空编号（与 遇袭-01 同一习惯）。「误」是副词性修饰，用 :manner。
- [role] 「混入」的论元: 混入 :ARG1 成员 :place 车队 (wrong, 3 of 5 runs); 混入 :ARG1 成员 :ARG2 车队 (wrong, 2 of 5 runs). Better: 混入 :ARG0 成员 :ARG1 车队. PropBank 混入-01：ARG0 enterer（混进去的人），ARG1 thing entered（被混进的地方）。5 个系统都把成员当 ARG1，车队用 :place 或不存在的 ARG2。
- [structure] 「哈马斯武装成员」中成员与组织的关系: 成员/person :part-of 组织 (acceptable but worse, 2 of 5 runs); 成员/person :mod 组织 (acceptable but worse, 2 of 5 runs); 成员 :poss 组织 (acceptable but worse, 1 of 5 runs). Better: 成员 :ARG1-of (have-org-role-92 :ARG2 哈马斯). abridged 2.3：角色名词用 have-org-role-92 具体化（ARG1 人，ARG2 组织）。:part-of、:mod、:poss 都没有表达出组织成员关系。r2/r4 还把「成员」换成了 person。
- [concept] 「武装」的处理: person :ARG0-of 武装-01 (acceptable but worse, 1 of 5 runs). 「哈马斯武装成员」里的「武装」可读作名词（哈马斯的武装力量）或「被武装的」，两种都说得通；但按 PropBank 武装-01（ARG1 entity armed），成员是被武装者，r2 用 ARG0-of（施事）不对。
- [doc-temporal] 承认、以为、空袭之间的先后: 承认、坚持的先后对，但 (坚持 :after 以为) 把以为放到坚持之后 (acceptable but worse, 1 of 5 runs); (空袭 :before 承认)：承认在空袭之前；(以为 :before 空袭)：空袭在以为之前 (wrong, 2 of 5 runs); (空袭 :before 承认)、(坚持 :after 以为) (wrong, 1 of 5 runs). (A :before B) 表示 B 在 A 之前。r1/r4/r5 写的「承认在空袭之前」「空袭在误以为之前」都把方向读反了；以色列误以为车队有武装人员才发动空袭，以为应在空袭之前、坚持之前。
- [doc-modal] 「坚持」内容和「误以为」内容的 modal: 以方 作 conceiver，(以方 :partial-affirmative 混入) (acceptable but worse, 1 of 5 runs); (坚持 :unspecified 内容)，(author :full-negative 混入) (acceptable but worse, 1 of 5 runs). abridged 5.2：引述内容以说话人（以色列）为 conceiver；「误以为」说明作者不认为「混入」属实，gold 让 author 对它 full-affirmative 是错的。r5 用 author full-negative 表达「误」有道理，但把坚持的内容标 unspecified 不对（坚持表示说话人确信）。
- [doc-coref] 跨句共指：空袭、车队: 连上，另把 混入 与 以为 标成同一事件 (wrong, 1 of 5 runs); 只连了空袭，没有车队 (acceptable but worse, 1 of 5 runs); 连上，但三元组次序颠倒，并有句内 (以方 :same-entity 以色列) (acceptable but worse, 1 of 5 runs). 「这次空袭」「车队」都是前文提过的；abridged 5.3 要求连到最近的前一次提及，早的在前。r2 把「混入」和「以为」当同一事件，错。

### Sentence 5: 2023 年  10 月  7 日  ，  哈马斯    发动   阿克萨    洪水   行动   ，  以色列    方面   随即   予以   反击   并  对  哈马斯    宣战   ，  以色列    —  哈马斯    战争   爆发   。

Reviewer's notes on the annotator's choices:
- [role] 「宣战」的对象: 宣战 :ARG2 哈马斯 (wrong, 1 of 5 runs). Better: 宣战 :ARG1 哈马斯. 原文「对哈马斯宣战」，PropBank 宣战-01：ARG1 entity that Arg0 fight a war against，应是哈马斯。gold 把 ARG1 指向了包含宣战自身的 and 节点（形成环），显然是变量写错；宣战-01 没有 ARG2。
- [structure] 「随即」与句子的连接方式: and 连接，反击 :mod 随即 (acceptable but worse, 1 of 5 runs). gold 用 consecutive 表达「随即」的先后承接（训练数据 chinese_umr-0007 第 4 句也这样用）；系统用 and 加「随即」节点也表达了同样的意思。时间副词作 :mod 略差。
- [concept] 「阿克萨洪水行动」「以色列—哈马斯战争」的实体类型: 行动（中文类型名）/ war (wrong, 1 of 5 runs); 行动 / 战争（都用中文类型名） (wrong, 3 of 5 runs). Better: event / war. abridged 2.1、2.2：实体类型用英文（event、war 都在类型表里），不用中文词作类型；这与第 1 句 r1/r3 的「地区」「地带」是同一习惯。
- [doc-temporal] 各事件之间及与文档时间的先后: 事件先后对，但 (document-creation-time :after 日期) (wrong, 1 of 5 runs); (document-creation-time :after 日期)、(发动 :before 反击)、(宣战 :before 爆发) 等 (wrong, 2 of 5 runs); (发动 :before 反击)、(反击 :before 宣战)、(宣战 :before 爆发) (wrong, 1 of 5 runs). (A :before B) 表示 B 在 A 之前。r1/r4/r5 写成反击在发动之前、爆发在宣战之前，r1 还写了 (2023年日期 :before 2024年日期)，即 2024 年在 2023 年之前；r1/r2/r5 又把 2023 年的日期放在文档时间之后。都是同一个读反方向的习惯。
- [doc-coref] 跨句共指：以色列、哈马斯: 哈马斯 连到第 4 句的「武装成员」（person） (wrong, 1 of 5 runs); 连上，另加句内 coref 和 (爆发 :same-event 战争) (acceptable but worse, 1 of 5 runs); 连上，但三元组次序颠倒 (acceptable but worse, 1 of 5 runs). 以色列、哈马斯第 4 句都出现过（abridged 5.3）。r2 把组织哈马斯与第 4 句的武装成员当成同一实体，错；r4 把「爆发」和「战争」当同一事件也不对。

### Sentence 6: 此后   ，  由于   以色列    对  加沙   地带   进行   封锁   等  缘故   ，  加沙   地带   正  面临   人为   的  大  饥荒   。

Reviewer's notes on the annotator's choices:
- [structure] 「由于…封锁等缘故」: 面临 :cause 封锁（丢掉「等」） (acceptable but worse, 1 of 5 runs); 面临 :ARG1-of (cause-01 :ARG0 封锁) (acceptable but worse, 2 of 5 runs); 根为 cause-01 :ARG0 封锁 :ARG1 面临，封锁 :mod 等 (acceptable but worse, 1 of 5 runs). abridged 2.5：「由于」→ :cause。gold 用 include-91 表达「封锁等缘故」中封锁只是原因之一，最完整；r5 用 :mod 等也保留了这层意思。其余丢掉「等」，或把 :cause 展开成英文 cause-01，略差。
- [doc-temporal] 面临相对前一事件和文档时间: (爆发 :before 面临)：面临在爆发之前 (wrong, 2 of 5 runs); (爆发 :before 面临)、(面临 :after 封锁)：封锁在面临之后 (wrong, 1 of 5 runs); (爆发 :before 封锁)、(封锁 :before 面临) (wrong, 1 of 5 runs). 「此后…正面临饥荒」：面临在战争爆发之后。(A :before B) 表示 B 在 A 之前，r1/r2/r4/r5 都写反了。gold 没有给「正面临」直接标 (document-creation-time :overlap 面临)，以「此」为参照也可以接受。
- [doc-coref] 跨句共指：以色列、加沙地带: 连上，但三元组次序颠倒 (acceptable but worse, 1 of 5 runs); 没有任何 coref (wrong, 1 of 5 runs). 以色列、加沙地带前文都出现过，abridged 5.3 要求连上；gold 只连了「此」。

### Sentence 7: 至  2024 年  4 月  2 日  ，  为  加沙   平民   提供   人道主义     援助   的  联合国    近东   巴勒斯坦     难民   救济   和  工程   处  （  简称   UNRWA ）  已  有  173 名  工作   人员   在  行动   中  身亡   。

Reviewer's notes on the annotator's choices:
- [structure] 「工作人员」与 UNRWA 的关系: person :ARG0-of 工作-01 :ARG1-of (have-org-role-91 :ARG2 UNRWA) (acceptable but worse, 1 of 5 runs); 人员 :mod 工作 :poss UNRWA (acceptable but worse, 1 of 5 runs). 几种写法都表达了「UNRWA 的工作人员」。项目规则 have-org-role 用 -92，r4 的 -91 略差；:poss 是旧拼写。
- [structure] 「简称 UNRWA」: UNRWA :alias (name :op1 "UNRWA") (acceptable but worse, 1 of 5 runs); 没有标简称 (acceptable but worse, 4 of 5 runs). 训练数据 chinese_umr-0003 第 9 句「（简称「中文电视」）」写作 :ARG1-of (简称-01 :ARG2 (name :op1 …))，gold 结构对，但缩写写成了小写普通概念 unrwa，应是 name。:alias 不在 UMR 角色表里；系统漏标都略差。
- [role] 「在行动中」: 身亡 :place 行动-01 (acceptable but worse, 1 of 5 runs); 身亡 :place 行动（不带义项） (acceptable but worse, 4 of 5 runs). Better: 身亡 :temporal 行动-01. 「在行动中身亡」指在执行任务期间，行动是事件（PropBank 行动-01），作时间背景 :temporal 比 :place 合适。
- [structure] 「加沙平民」: person :mod 平民 :place 加沙 (acceptable but worse, 1 of 5 runs); person :ARG1-of 平民 :mod 加沙（加沙不是命名实体） (wrong, 1 of 5 runs). 「平民」是普通名词，直接作概念；r2 拆成 person + :mod 平民 多余；r4 把名词「平民」当作谓词（:ARG1-of），又把「加沙」写成普通概念而不是命名实体，错。
- [attr] 「提供」的 aspect: process (acceptable but worse, 1 of 5 runs); state (wrong, 1 of 5 runs). Better: activity. 「为加沙平民提供援助」是持续进行的活动（activity）；提供不是状态谓词，标 state 错。
- [doc-temporal] 身亡相对日期和文档时间: (document-creation-time :after 日期/until) (wrong, 3 of 5 runs). 「至2024年4月2日已有…身亡」：身亡在这个日期之前。r1/r2/r5 把这个过去日期放在文档时间之后（读反），r1 还写了 (日期 :before 身亡)，即日期在身亡之前。gold 没把身亡和日期连起来，只说身亡在「工作」之后，参照不当。
- [doc-coref] 跨句共指：加沙: 没有任何 coref (wrong, 3 of 5 runs); 加沙连上（次序颠倒），另把本句援助与第 1 句援助标为同一事件 (wrong, 1 of 5 runs). 「加沙」前文多次出现，应连 :same-entity。r5 把 UNRWA 的援助与第 1 句世界中央厨房车队的援助当成同一事件，错。

### Sentence 8: 事发   前  3 天  ，  参与   审理   南非   诉  以色列    犯下   种族   灭绝   罪  的  联合国    国际法院     法官   一致   通过   临时   裁决   ，  要求   以色列    必须   保证   救援   物资   能够   不受   任何   阻碍   地  进入   加沙   ，  保证   加沙   地带   的  基本   生活   所需   水电   供应   ，  并  展开   人道主义     救援   。

Reviewer's notes on the annotator's choices:
- [structure] 「联合国国际法院法官」: person :ARG0-of (have-org-role-92 :ARG2 国际法院 :ARG3 法官) (acceptable but worse, 2 of 5 runs); 法官 :mod 国际法院 (acceptable but worse, 2 of 5 runs); person :ARG0-of 法官-01 :part-of 国际法院 (wrong, 1 of 5 runs). Better: 法官 :ARG3-of (have-org-role-92 :ARG2 国际法院). abridged 2.3：职务名词用 have-org-role-92（ARG1 人、ARG2 组织、ARG3 职务）；训练数据 chinese_umr-0005 第 20 句「演奏员 :ARG3-of have-org-role :ARG2 军乐团」与 gold 同。r2/r5 把人放在 ARG0 上（have-org-role-92 没有 ARG0）；:mod 没表达出职务关系；r4 的 法官-01 不在 PropBank。
- [structure] 「参与」是否建节点: 没有 参与，法官直接作审理的 ARG0 (acceptable but worse, 2 of 5 runs). Better: 法官 :ARG0-of (参与-01 :ARG1 审理). 「参与审理」的「参与」是实义动词（PropBank 参与-01 ARG0 participant / ARG1 activity），丢掉略差。
- [sense] 「诉」的义项: 诉（不带义项） (acceptable but worse, 1 of 5 runs). Better: 诉-01. PropBank 有 诉-01（ARG0 prosecutor / ARG1 patient being prosecuted），不该写 -00。
- [role] 诉的指控内容「犯下种族灭绝罪」: 诉 :ARG1 以色列 :ARG2 犯下 (acceptable but worse, 4 of 5 runs); 诉 :ARG1 犯下 :ARG2 以色列 (wrong, 1 of 5 runs). PropBank 诉-01 只有 ARG0、ARG1（被诉方是以色列），没有 ARG2；指控内容用非论元角色（如 :topic）更合框架，但这一点拿不准。r5 把被诉方放到不存在的 ARG2、把指控放到 ARG1，错。
- [concept] 「种族灭绝罪」: 种族灭绝罪（一个概念） (acceptable but worse, 1 of 5 runs). 分词把「种族 / 灭绝」分开，gold 按 灭绝-01（ARG1 thing extinct）展开说得通；把「种族灭绝」当固定术语作一个概念也可以（abridged 2.6）。r5 把三个词合成一个概念略差。
- [structure] 「事发前3天」的结构: before :op1 (发生-01 :ARG1 事) :quant …（把「事发」拆开） (acceptable but worse, 1 of 5 runs). AMR/UMR 的「X 前 N 天」写作 (before :op1 X :quant (temporal-quantity …))；gold 让时长作中心、「前」作 :mod，层次颠倒，并把 :aspect performance 标在非事件的「前」上，而 事发-01 反而没有 aspect。r1 把 PropBank 已有的 事发-01 拆成「发生 + 事」。
- [structure] 「要求」的挂接与论元: 通过 :purpose 要求-02 (acceptable but worse, 1 of 5 runs); 裁决 :ARG0-of 要求-02，同时 :ARG0 法官（两个 ARG0） (wrong, 1 of 5 runs). PropBank 要求-02：ARG0 asker / ARG1 askee / ARG2 predicate；要求-01：ARG1 things asked for / ARG2 entity asked from。以法官或裁决为要求者都通。r2 把「要求」当通过的目的，不合原文；r4 让要求-02 同时有两个 ARG0。
- [role] 「进入」的论元: 进入 :ARG1 物资 :ARG2 加沙 (wrong, 1 of 5 runs); 进入 :ARG1 物资 :ARG4 加沙 (wrong, 3 of 5 runs). Better: 进入 :ARG0 物资 :ARG1 加沙. PropBank 进入-01：ARG0 theme（进入者），ARG1 place entered。r1–r4 套用了英文 enter 类框架（ARG1 进入者、ARG4 终点），与第 4 句「混入」同一习惯：不查中文 PropBank 的论元。
- [structure] 「不受任何阻碍」: 阻碍（不带义项）:polarity - (acceptable but worse, 2 of 5 runs). 阻碍在 PropBank（阻碍-01 ARG1 thing hindered），按事件标；进入作阻碍的 ARG1（gold）或阻碍作进入的 :manner 都说得通。
- [sense] 「供应」的义项与对象: 供应（不带义项）:mod 水电 (acceptable but worse, 2 of 5 runs). PropBank 供应-01：ARG1 thing provided，水电是供应的东西，应作 ARG1；作名词并用 :mod 挂水电略差。
- [structure] 「基本生活所需」: 水电 :mod 基本 :mod 生活所需 (acceptable but worse, 1 of 5 runs); 「基本生活所需」合成一个概念 (acceptable but worse, 2 of 5 runs); 供应 :poss (所需 :mod 基本生活) (acceptable but worse, 1 of 5 runs); 供应 :mod (所需 :mod 基本 :mod 生活) (acceptable but worse, 1 of 5 runs). Better: 水电 :ARG1-of (需-01 :ARG0 (生活 :mod 基本)). 「所需」是「需」的名词化，PropBank 有 需-01（ARG0 / ARG1 theme），gold 的展开最完整；系统把几个词合成一个概念（不合分词）或把「所需」当名词挂在供应上，都略差。
- [role] 加沙地带作为供应对象: 供应 :place 加沙地带 (acceptable but worse, 5 of 5 runs). Better: 供应 :ARG2 加沙. PropBank 供应-01 ARG2 providing to；「保证加沙地带的…水电供应」是对加沙的供应，用核心论元 ARG2 好于 :place。
- [structure] 「必须」是否建节点: 保证 :mod 必须 (acceptable but worse, 1 of 5 runs). Better: 不建节点. abridged 2.1：情态动词（必须、应该）不建节点，只影响 modal 强度。
- [doc-modal] 被要求事件的 modal: (法官 :partial-affirmative 要求)，要求本身也降为 partial (wrong, 1 of 5 runs). abridged 5.2：被要求、尚未发生的事件挂在要求类谓词下，用 unspecified 或「必须」对应的 partial-affirmative；gold 让作者断言这些事件已经发生，错。r4 把作者直接陈述的「要求」也降成 partial。
- [doc-modal] 被指控的「犯下种族灭绝罪」的 modal: (author :full-affirmative 犯下) (wrong, 1 of 5 runs); 犯下 没有 modal (acceptable but worse, 2 of 5 runs). 「南非诉以色列犯下种族灭绝罪」是南非的指控，作者并未断言以色列犯下了这一罪行；按 guideline 5.2 应以「诉」（或南非）为 conceiver，不应是 author full-affirmative。
- [doc-temporal] 通过、审理、要求与事发的先后: (审理 :before 通过)、(通过 :before 空袭)、(要求 :before 保证) (wrong, 1 of 5 runs); (通过 :before 空袭)、(通过 :before 保证) (wrong, 1 of 5 runs); (通过 :before 事发)、(要求 :before 保证) (wrong, 1 of 5 runs). (A :before B) 表示 B 在 A 之前。通过在事发（空袭）前 3 天，被要求的保证在要求之后。r1/r4/r5 写成空袭在通过之前、保证在要求之前，方向读反。
- [doc-coref] 跨句共指：事发、以色列、加沙: 事发、以色列 连上，没有加沙 (acceptable but worse, 2 of 5 runs); 以色列、加沙地带 连上，没有事发 (acceptable but worse, 1 of 5 runs); 三者都连上，但三元组次序颠倒 (acceptable but worse, 1 of 5 runs); 没有任何 coref (wrong, 1 of 5 runs). 以色列、加沙前文都出现过，「事发」指第 1 句的空袭；abridged 5.3 要求都连上。

### Sentence 9: 临时   裁决   中  写道   ：  “ 加沙   不  是  正  面临   大饥荒    的  危机   ，  而是   正在   发生   大饥荒    。  ”

Reviewer's notes on the annotator's choices:
- [sense] 「写道」的义项: 写-01 (acceptable but worse, 3 of 5 runs). Better: 写道-01. 「写道」在 PropBank 里有自己的 roleset（写道-01：ARG0 author / ARG1 thing written / ARG2 place arg1 is written），不必退到 写-01。
- [role] 「临时裁决中」的角色: 写道 :ARG0 裁决 (acceptable but worse, 4 of 5 runs). Better: 写道 :ARG2 裁决. 「裁决中写道」：裁决是写的处所，PropBank 写道-01 ARG2 place arg1 is written；把裁决当作者（ARG0）是转喻，略差。
- [structure] 「大饥荒的危机」: 危机 :mod (饥荒 :mod 大)（拆开「大饥荒」） (acceptable but worse, 2 of 5 runs). 「大饥荒」是一个词，拆成 饥荒 :mod 大 不合分词；危机与大饥荒用 identity-91 或 :mod 都可以。
- [role] 「发生大饥荒」的论元: 发生 :ARG0 大饥荒 :place 加沙 (acceptable but worse, 1 of 5 runs); 发生 :ARG1 饥荒 (wrong, 4 of 5 runs). Better: 发生 :ARG0 大饥荒 :ARG1 加沙. PropBank 发生-01：ARG0 accident, event（发生的事），ARG1 happening to（发生在谁身上）。饥荒是 ARG0，加沙是 ARG1；与第 3 句「事件发生」同一错误（全篇如此）。
- [doc-modal] 引文内容的 conceiver: (author :full-negative 面临)、(author :full-affirmative 发生) (wrong, 1 of 5 runs). 引号里是裁决中写的话，abridged 5.2：引述内容由说话人（这里是裁决，或写道事件）作 conceiver，不由 author 直接断言。
- [doc-temporal] 写道相对文档时间和第 8 句: (第8句通过 :before 写道)、(document-creation-time :after 写道) (wrong, 1 of 5 runs). 写道与第 8 句通过裁决同时，都在文档时间之前；r2 把它放到文档时间之后、通过之前，方向读反。
- [doc-coref] 跨句共指：裁决、加沙: 没有任何 coref (wrong, 2 of 5 runs); 只连了裁决 (acceptable but worse, 1 of 5 runs); 连了加沙，但把第 8 句的「通过」当成裁决 (acceptable but worse, 1 of 5 runs); 连了加沙、裁决（次序颠倒），另把「发生」与「饥荒」标为同一事件 (wrong, 1 of 5 runs). 「临时裁决」就是第 8 句的临时裁决，「加沙」前文多次出现。r5 句内把「发生-01」和「饥荒」当同一事件，错。

### Sentence 10: 据  联合国    观察员    报告   ，  加沙   已经   有  31 人  因为   营养   不  良  或  脱水   而  死亡   ，  其中   27 人  为  儿童   。

Reviewer's notes on the annotator's choices:
- [structure] 「联合国观察员」: 观察员 :mod 联合国 (acceptable but worse, 2 of 5 runs); person :ARG0-of 观察-01 :ARG1-of (have-org-role-92 :ARG2 联合国) (acceptable but worse, 1 of 5 runs); person :ARG0-of 观察-01 :part-of 联合国 (acceptable but worse, 1 of 5 runs); person :ARG0-of (have-org-role-92 :ARG2 联合国 :ARG3 观察员) (acceptable but worse, 1 of 5 runs). Better: 观察员 :ARG3-of (have-org-role-92 :ARG2 联合国). 与第 8 句「法官」相同：职务名词按 abridged 2.3 用 have-org-role-92，持有人是 ARG1（不是 ARG0）；:mod、:part-of 没表达出职务关系；把「观察员」拆成 person + 观察-01 也不必要。
- [sense] 「营养不良」「脱水」的概念: 营养不良、脱水（都不带义项） (acceptable but worse, 2 of 5 runs); 良-01 :polarity - :ARG1 营养 (acceptable but worse, 1 of 5 runs). Better: 营养不良-01、脱水-01. PropBank 有 营养不良-01、脱水-01，作原因的事件按事件标；r3 按分词拆成 不 + 良，失去了固定词「营养不良」。
- [role] 死亡的原因: 死亡 :cause (or …) (acceptable but worse, 3 of 5 runs); 死亡 :ARG1-of (cause-01 :ARG0 (or …)) (acceptable but worse, 2 of 5 runs). Better: 死亡 :ARG0 (or 营养不良 脱水). PropBank 死亡-01 ARG0 是 cause，原因有核心论元可用，不该用非论元 :cause 或另加英文 cause-01（审阅说明：PropBank 论元能表达时用 ARGn）。
- [role] 「死亡」的死者: 死亡 :ARG0 人 (wrong, 1 of 5 runs). Better: 死亡 :ARG1 人. PropBank 死亡-01：ARG1 entity who die，ARG0 是原因。
- [structure] 「其中27人为儿童」: include-91 :ARG1 27人 :ARG2 31人，27人 :ARG1-of (have-role-91 :ARG2 自身) (acceptable but worse, 1 of 5 runs); identity-91 27人 儿童，没有和 31人 连起来 (acceptable but worse, 2 of 5 runs); 27人 :ARG2-of (include-91 :ARG1 31人)：方向颠倒 (wrong, 1 of 5 runs). 「其中」表示 27 人是 31 人的一部分：include-91 的 ARG1 是被包含者、ARG2 是整体（gold 的写法），或文档级 :subset-of（成员在前）。r3 把包含关系写反；r1/r4 丢了「其中」；r2 的 have-role-91 让 ARG2 指向自己。
- [doc-temporal] 报告、死亡相对文档时间: (document-creation-time :after 报告) 或 (报告 :before document-creation-time)，(死亡 :before 报告) (wrong, 3 of 5 runs); (document-creation-time :after 报告)，(报告 :after 死亡) (wrong, 1 of 5 runs). (A :before B) 表示 B 在 A 之前。报告是过去的事件，在文档时间之前，死亡又在报告之前；r1/r2/r4/r5 把报告放到文档时间之后，r1/r4/r5 还写成报告在死亡之前，都是同一个读反方向的习惯。
- [doc-modal] 「据…报告」内容的 conceiver: (报告 :full-affirmative 死亡)，但 include 挂 author (acceptable but worse, 1 of 5 runs); (观察员 :full-affirmative 死亡)，但没有 (author … 观察员) (acceptable but worse, 1 of 5 runs). 「据联合国观察员报告」，死亡人数是观察员报告的内容，abridged 5.2：author 确信报告者，报告者对内容。gold 把内容直接挂在 author 下。
- [doc-coref] 跨句共指：加沙: 没有任何 coref (wrong, 3 of 5 runs); 连上，但次序颠倒；另有 :subset-of (acceptable but worse, 1 of 5 runs). 「加沙」前文多次出现，应连到最近一次提及（第 9 句）。

### Sentence 11: 世界   中央   厨房   是  由  著名   厨师   和  餐馆   老板   何塞   ·  安德烈斯     创办   的  人道主义     组织   ，  致力   于  为  世界   各地   受到   自然   灾害   或  武装   冲突   影响   的  灾民   和  难民   提供   食品   援助   。

Reviewer's notes on the annotator's choices:
- [concept] 「何塞·安德烈斯」的 name: :op1 "何塞" :op2 "安德烈斯"（丢了间隔号） (acceptable but worse, 1 of 5 runs). Better: :op1 "何塞" :op2 "·" :op3 "安德烈斯". 训练数据（chinese_umr-0002 第 5 句「凯蒂 · 佩芮」、chinese_umr-0004）把间隔号作为单独的 :opN 保留。
- [structure] 「厨师和餐馆老板」的表达: person :ARG0-of (have-role-91 :ARG2 …) (wrong, 2 of 5 runs); person :ARG1-of (identity-91 :ARG2 (and …)) (acceptable but worse, 1 of 5 runs); person :mod (and 厨师 老板) (acceptable but worse, 1 of 5 runs). Better: person :ARG1-of (have-role-91 :ARG3 (and 厨师 老板)). guideline 2.3：X 属于某一类别用 have-role-91，:ARG1 是 X，:ARG3 是类别；r2、r4 把人放在 ARG0、类别放在 ARG2，角色号错。identity-91 表示等同，用来说人的身份不如 have-role-91；直接 :mod 丢了谓词。著名挂在人、厨师或并列节点上意思差别不大，不单列。
- [role] 「餐馆老板」的内部关系: 一个概念 餐馆老板 (acceptable but worse, 2 of 5 runs). 「餐馆」「老板」是两个词，合成一个概念丢了结构；:possessor 与 :mod 都可接受（更细的写法是 have-org-role-92 :ARG2 餐馆 :ARG3 老板，没有标注这样写）。
- [concept] 「组织」的概念: organization（英文） (acceptable but worse, 2 of 5 runs). Better: 组织. guideline 2.1：中文的实体名词写原词，英文只用于抽象概念和命名实体类型；这里的「组织」是普通名词，不是命名实体。
- [concept] 「援助」是不是事件: 援助（名词） (acceptable but worse, 3 of 5 runs). Better: 援助-01. guideline 2.1：有过程义的事件名词按事件标；PropBank 有 援助-01（ARG0 helper）。
- [structure] 「自然灾害」「武装冲突」拆不拆: 合成一个概念 自然灾害、武装冲突 (acceptable but worse, 2 of 5 runs). Better: 拆开：灾害 :mod 自然，冲突 :mod 武装. 分词把两者各分成两个词，修饰语应建 :mod；合成一个概念丢了修饰结构。冲突 当事件名词（冲突-01，ARG0 entities conflicting）也说得通。
- [attr] 「影响」的 aspect: 没有 aspect (wrong, 1 of 5 runs). 「受到……影响的灾民」可以理解为受影响的状态，也可以理解为已发生的影响事件，两者都接受；guideline 7 节要求每个事件都有 :aspect，r4 漏了。
- [structure] 灾民、难民作谓词: person :ARG0-of 灾民 / person :ARG0-of 难民，影响 只挂在灾民上 (wrong, 1 of 5 runs). Better: and :op1 灾民 :op2 难民，整体 :ARG1-of 影响. 灾民、难民是名词，PropBank 没有这样的 roleset，不能作 :ARG0-of 的谓词；r4 还把「受……影响」只挂在灾民上，而原文修饰的是「灾民和难民」。
- [role] 「世界各地」的内部关系: 一个概念 世界各地 (acceptable but worse, 2 of 5 runs); place :mod 各 :mod 世界 (acceptable but worse, 1 of 5 runs). Better: 各地 :mod 世界. 项目规则：部分为父节点时用 :part-of。各地是世界的部分，gold 用 :part 方向配反（训练数据 chinese_umr-0011 第 6 句「中国各地」也这样写，但项目规则已定）。
- [doc-temporal] 创办 相对文档时间: identity-91 :overlap 创办 (acceptable but worse, 1 of 5 runs); (document-creation-time :after 创办)：创办 在 DCT 之后 (wrong, 1 of 5 runs); (创办 :before document-creation-time)：DCT 在创办之前 (wrong, 1 of 5 runs). Better: 创办 在 DCT 之前（DCT :before 创办 / past-reference :contained 创办）. 创办是过去完成的事件；(A :after B) 是 B 在 A 之后，r1、r4 都把方向写反成创办在文档时间之后。创办与现在的身份状态只是先后，不是重叠。
- [doc-temporal] 身份状态 identity-91 的时间父节点: 没有时间关系 (acceptable but worse, 1 of 5 runs). Better: document-creation-time :overlap identity-91. guideline 5.1：每个事件都要有时间父节点；现在的状态用 (document-creation-time :overlap …)。
- [doc-coref] 世界中央厨房的跨句共指: 链到第 1 句，但新提及写在前 (acceptable but worse, 1 of 5 runs). Better: 链到第 3 句（或第 1、3 句）的世界中央厨房. guideline 5.3：同一实体的重复提及要建 :same-entity，链到最近的前一次提及、前者在前；最近的是第 3 句 gold 的 s3i2。gold 全篇对世界中央厨房几乎没有共指。
- [doc-coref] 提供 的事件共指: 链到第 1 句的提供、第 3 句的行动 (wrong, 1 of 5 runs). Better: 没有. 这里是组织宗旨里泛指的「提供食品援助」，和第 1 句代尔拜莱赫那一次具体援助、第 3 句暂停的援助行动不是同一事件。

### Sentence 12: 事发   前  两天   ，  以色列    国防军    的  狙击手    曾  向  世界   中央   厨房   的  汽车   开火   ，  世界   中央   厨房   立刻   向  以色列    投诉   并  要求   保障   人道   工作   人员   的  安全   。

Reviewer's notes on the annotator's choices:
- [role] :poss 的拼写: :poss (acceptable but worse, 3 of 5 runs). Better: :possessor. 项目规则：拼写按发布数据，用 :possessor 不用 :poss。r3、r4、r5 全篇如此，以后不再写。
- [role] 「汽车」在开火中的角色: 开火 :ARG2 汽车 (wrong, 2 of 5 runs). Better: 开火 :ARG1 汽车. PropBank 开火-01 只有 ARG0 agent 和 ARG1 target that arg0 opens fire on，没有 ARG2。
- [sense] 「事发」的概念: 事发（名词） (acceptable but worse, 2 of 5 runs); 发生-01 :ARG1 事 (acceptable but worse, 1 of 5 runs). Better: 事发-01. PropBank 有 事发-01（ARG0 entity described），应用这个 roleset；拆成 发生-01 + 事 是凭语义改写原词。aspect（performance / process）都可以。
- [role] 「以色列」在投诉中的角色: 投诉 :ARG1 以色列 (wrong, 1 of 5 runs). Better: 投诉 :ARG2 以色列. PropBank 投诉-01：ARG1 是投诉的事由，ARG2 是投诉的对象（complains to）；「向以色列投诉」是 ARG2。
- [sense] 「要求」的义项与论元: 要求-01 :ARG1 保障（没有 ARG2） (acceptable but worse, 1 of 5 runs). Better: 要求-02 :ARG1 以色列 :ARG2 保障. PropBank 要求-01：ARG1 所求之事、ARG2 向谁要求；要求-02：ARG1 被要求者、ARG2 谓词。gold 的论元配置是 要求-02 的，义项却写 -01，于是成了「向保障要求以色列」。r3 漏了被要求者以色列。
- [role] 「保障」的施事: 保障 没有 :ARG0 (acceptable but worse, 4 of 5 runs). Better: 保障 :ARG0 以色列. 要求-02 的 ARG1（被要求者以色列）就是去保障安全的一方，PropBank 保障-01 ARG0 maintainer；重入补上更完整，但不补也不算错。
- [structure] 「人道工作人员」: person :ARG0-of (工作-01 :mod 人道)，工作-01 没有 aspect (acceptable but worse, 2 of 5 runs). 「人道工作人员」可以把工作作谓词（工作-01 ARG0 worker），也可以当名词修饰语，都可以；r2、r4 用 person 代替了原词「人员」，事件 工作-01 也没有 :aspect（guideline 7 节）。
- [doc-temporal] 开火与投诉的先后: (开火 :before 投诉)：投诉在开火之前 (wrong, 3 of 5 runs). Better: (开火 :after 投诉)：投诉在开火之后. (A :before B) 是 B 在 A 之前；投诉是对开火的反应，发生在开火之后，r1、r4、r5 写反了。
- [doc-temporal] 开火相对「事发」（第 1 句空袭）: (开火 :before 空袭/事发)：空袭在开火之前 (wrong, 3 of 5 runs). Better: 开火 在事发之前（事发 :before 两天 :contained 开火 / 事发 :before 开火 / 空袭 :before 开火）. 开火在事发前两天；(A :before B) 是 B 在 A 之前，r1、r4（对第 1 句空袭）和 r5（对事发）把方向写反成空袭先发生。
- [doc-temporal] 要求与保障的时间关系: (要求 :overlap 保障) (acceptable but worse, 1 of 5 runs); (要求 :before 保障)：保障在要求之前 (wrong, 1 of 5 runs); 没有标 (acceptable but worse, 2 of 5 runs). Better: (要求 :after 保障)：保障在要求之后. 被要求的事在要求之后；guideline 5.1 每个事件要有时间父节点。r5 方向写反。
- [doc-modal] 被要求的「保障」的 modal: 要求 :unspecified 保障 (acceptable but worse, 1 of 5 runs); 没有 modal (wrong, 1 of 5 runs). Better: 要求 :partial-affirmative 保障. guideline Part 4-3-1-6：强义务类情态（need, demand）给补足语 partial-affirmative，补足语挂在情态事件下；被要求的保障并未被作者断言为事实。
- [doc-coref] 世界中央厨房、国防军、以色列的跨句共指: 链了世界中央厨房和国防军，没链以色列 (acceptable but worse, 1 of 5 runs). Better: 三者都链到前文. guideline 5.3：同一实体的重复提及都要 :same-entity；世界中央厨房见第 11 句，以色列国防军见第 1 句，以色列见第 8 句。gold 本句里两个 以色列 country 节点也该是一个（句内重入）。r5 把新提及写在前（全篇如此）。r4 把第 8 句法院的「要求」和本句的要求作同一事件，错。

### Sentence 13: 空袭   发生   前  一  小时   ，  世界   中央   厨房   从  加沙   地带   北部   港口   的  货船   卸下   约  100 公吨   用于   人道   主义   救援   的  粮食   。

Reviewer's notes on the annotator's choices:
- [role] 「空袭发生」中 发生 的论元: 发生-01 :ARG1 空袭 (wrong, 2 of 5 runs); 没有 发生 节点 (acceptable but worse, 3 of 5 runs). Better: 发生-01 :ARG0 空袭. PropBank 发生-01：ARG0 是发生的事件（accident, event），ARG1 是 happening to（受影响者）；发生的空袭应是 ARG0。r3–r5 直接省掉动词「发生」，丢了一个谓词，算小问题。
- [attr] 「约 100 公吨」: 漏了「约」 (acceptable but worse, 2 of 5 runs). 训练数据（「约 100 人」：人 :quant (约 :quant 100)）把「约」作节点；几种写法都保留了约数。r2、r3 丢了「约」。
- [structure] 「用于人道主义救援」: 卸下 :purpose 救援（没有 用于） (acceptable but worse, 1 of 5 runs); 粮食 :purpose 救援（没有 用于） (acceptable but worse, 1 of 5 runs). Better: 粮食 :ARG1-of (用于-01 :ARG2 救援). PropBank 用于-01：ARG1 entity used，ARG2 thing arg1 is used for；原文有动词「用于」，应作谓词；改写成 :purpose 丢了谓词，r1 还把用途挂到卸下上。
- [concept] 「救援」是不是事件: 救援（名词） (acceptable but worse, 2 of 5 runs). Better: 救援-01. PropBank 有 救援-01；事件名词按事件标（guideline 2.1）。
- [role] 「加沙地带北部港口」的部分关系: 港口 :place/:location (加沙地带 :mod 北部) (acceptable but worse, 2 of 5 runs). Better: 港口 :part-of 北部 :part-of 加沙地带. 项目规则：部分为父节点用 :part-of；港口在北部之内、北部是加沙地带的一部分，gold 两处都用 :part，方向配反。r3、r4 把「北部」挂成加沙的修饰，r4 还用了不用的 :location（项目规则用 :place）。
- [concept] 加沙地带的命名实体类型: 地带（中文词作类型） (acceptable but worse, 1 of 5 runs). 地名类型 AMR、UMR 的都接受（项目规则）；r1 拿中文的「地带」当实体类型，不在类型表里。
- [doc-temporal] 卸下与空袭的先后: (卸下 :before 空袭)：空袭在卸下之前 (wrong, 3 of 5 runs). Better: 卸下在空袭之前（经 前一小时 / 空袭 :before 卸下 / s1 空袭 :before 卸下）. (A :before B) 是 B 在 A 之前；卸货在空袭前一小时，r1、r4、r5 把方向写反（同第 12 句）。r5 还写了救援在卸下之前。
- [doc-modal] 救援（用途）的 modal: 没有标 (acceptable but worse, 3 of 5 runs). Better: 卸下 :partial-affirmative 救援. 救援是粮食预定的用途，作者没有断言它已发生；guideline 5.2 目的事件挂在主事件（或 purpose）下而不是作者直接断言。
- [doc-modal] 空袭、发生、用于 的 modal: 只标了 卸下，其他事件没有 modal 父节点 (wrong, 3 of 5 runs). Better: 都有 author :full-affirmative. guideline 5.2 / 7 节：每个事件都要有 modal 父节点；r2、r3、r4 只标了主事件。
- [doc-coref] 世界中央厨房、空袭、加沙地带的共指: 只链了世界中央厨房 (acceptable but worse, 1 of 5 runs). Better: 链了世界中央厨房和空袭（r3 还有加沙地带）. guideline 5.3：世界中央厨房见第 12 句，空袭就是第 1 句以来的那次空袭（gold 已把第 4、8、12 句的事发连成一串），加沙地带见第 6 句。

### Sentence 14: 尔后   ，  该  组织   的  一辆   运送   救援   物资   的  货车   在  一个   由  3  辆  汽车   组成   的  车队   的  护送   下  ，  前往   位于   代尔拜莱赫      的  用以   存放   救援   粮食   的  仓库   。

Reviewer's notes on the annotator's choices:
- [attr] 量词「辆」「个」: 省掉量词（保留 :quant） (acceptable but worse, 3 of 5 runs); 省掉量词，货车 的 :quant 1 也丢了 (acceptable but worse, 2 of 5 runs). Better: 货车 :quant 1 :unit 辆，车队 :quant 1 :unit 个，汽车 :quant 3 :unit 辆. 项目规则：量词都保留为 :unit；省掉判 minor。系统全篇如此，以后不再写。
- [structure] 「该组织」: 组织 :refer-to (organization :name 世界中央厨房) (acceptable but worse, 1 of 5 runs); organization :refer-number singular（丢了「该」） (acceptable but worse, 1 of 5 runs); 货车 :mod organization（丢了「该」） (acceptable but worse, 1 of 5 runs). Better: 组织 :mod 该（共指世界中央厨房）. :refer-to 不是 UMR 的角色，指代应通过跨句共指表达；r3、r4 丢了指示词「该」，r4 还把领属写成 :mod。领属方向（gold :possessor-of）同第 12 句，不再写。
- [role] 「由 3 辆汽车组成的车队」: 组成-01 :ARG0 汽车，车队 :ARG1-of (wrong, 1 of 5 runs); 组成-01 :ARG2 汽车，车队 :ARG1-of (wrong, 4 of 5 runs). Better: 组成-01 :ARG0 车队 :ARG1 汽车. PropBank 组成-01：ARG0 entity described（整体，车队），ARG1 entities arg0 consists of（组成部分，汽车），没有 ARG2。r1 两个论元配反，r2–r5 用了不存在的 ARG2。r4 的 组成-01 还没有 aspect。
- [role] 「护送」的受护送者: 护送 没有 :ARG1 (acceptable but worse, 1 of 5 runs). Better: 护送 :ARG1 货车. PropBank 护送-01 ARG1 是 entity that arg0 escorts；「在车队的护送下」被护送的是货车，句中已有节点，应重入。
- [role] 「前往」的目的地: 前往 :ARG4 仓库 (wrong, 1 of 5 runs). Better: 前往 :ARG1 仓库. PropBank 前往-01 只有 ARG0 agent、ARG1 goal。
- [structure] 「位于代尔拜莱赫」: 仓库 :place 代尔拜莱赫 (acceptable but worse, 5 of 5 runs). Better: 仓库 :ARG0-of (位于-01 :ARG1 代尔拜莱赫). 原文有动词「位于」，PropBank 位于-01：ARG0 entity described，ARG1 location；系统改写成 :place，意思不错，但丢了谓词。
- [structure] 「用以存放」: 仓库 :ARG1-of (用以-01 :ARG2 存放) (wrong, 1 of 5 runs); 仓库 :purpose 存放（没有 用以） (acceptable but worse, 2 of 5 runs); 仓库 :ARG1-of 存放（没有 用以） (acceptable but worse, 2 of 5 runs). Better: 仓库 :ARG0-of (用以-01 :ARG1 存放). PropBank 用以-01：ARG0 thing used，ARG1 thing arg0 is used for；r4 套用了 用于-01 的论元号（ARG1/ARG2），用以-01 没有 ARG2。
- [role] 「存放」的论元: 仓库 作 存放 的 :ARG1，粮食 也是 :ARG1 (wrong, 1 of 5 runs); 仓库 作 :ARG1，粮食 作 :ARG2 (wrong, 1 of 5 runs). Better: 存放 :ARG1 粮食（仓库 不作论元）. PropBank 存放-01：ARG1 thing placed，ARG2 location；仓库是处所，应是 ARG2（或不出现），r2、r3 把仓库当成被存放物，r2 还把粮食放到 ARG2。gold 可以再加 存放 :ARG2 仓库 的重入，不加也可以。
- [doc-temporal] 前往相对第 13 句卸下: (卸下 :before 前往)：前往在卸下之前 (wrong, 3 of 5 runs). Better: 卸下 :after 前往/护送：前往在卸下之后. 「尔后」：前往发生在第 13 句卸货之后；(A :before B) 是 B 在 A 之前，r1、r4、r5 把方向写反（r5 还把存放写在前往之前）。
- [doc-modal] 各事件的 modal 父节点: 只标了部分事件 (wrong, 2 of 5 runs). Better: 各事件都有 modal. guideline 5.2 / 7 节每个事件都要有 modal 父节点；r4 只标了 前往，r3 漏了 组成、存放。存放 作用途挂在 前往 下（r1、r5 partial-affirmative）还是作者直接断言（gold、r2）都可以。
- [doc-coref] 车队、代尔拜莱赫的共指: 代尔拜莱赫 链第 1 句，另把 city 和 name 节点链成共指 (wrong, 1 of 5 runs); 把货车链到第 12 句被开火的汽车，护送 链到 车队 (wrong, 1 of 5 runs). Better: 车队、代尔拜莱赫 都链到第 1 句（新提及写在前）. 这支由 3 辆车组成的车队就是第 1、2、4 句遭空袭的车队，代尔拜莱赫见第 1 句（guideline 5.3）。共指只连实体节点，不连 name 节点；第 12 句被开火的汽车与这辆货车不是同一辆，护送 是事件不能和车队共指。

### Sentence 15: 在  车队   卸下   粮食   并  离开   仓库   后  ，  第一   辆  汽车   首先   被  以军   无人机    小型   精确   制导   导弹   命中   ，  存活   下来   的  人员   移动   到  第二   辆  车  上  逃跑   并  用  无线电    向  上级   呼救   。

Reviewer's notes on the annotator's choices:
- [attr] 序数「第一辆」「第二辆」: :ord 1（常量） (acceptable but worse, 1 of 5 runs). Better: :ord (ordinal-entity :value 1). guideline 2.2：序数写成 (ordinal-entity :value N)。量词「辆」gold 保留为 :unit，系统省掉，同第 14 句。
- [role] 「存活下来的人员」: person :ARG1-of 存活-01 (wrong, 2 of 5 runs). Better: 人员/person :ARG0-of 存活-01. PropBank 存活-01 只有 ARG0 survivor。r2、r4（以及 r5）还用 person 代替了原词「人员」。存活 的 aspect（state / performance）都可以。
- [role] 「移动到第二辆车上」: 移动 :ARG2 车 (wrong, 1 of 5 runs); 移动 :ARG4 车 (wrong, 3 of 5 runs). Better: 移动 :goal 车. PropBank 移动-01 只有 ARG0 agent/cause 和 ARG1 entity moved，没有终点论元，终点用非论元角色 :goal。
- [role] 「向上级呼救」: 呼救 :ARG2 上级 (wrong, 1 of 5 runs). Better: 呼救 :ARG1 上级. PropBank 呼救-01：ARG1 recipient，ARG2 content；上级是求救的对象。
- [role] 「用无线电」: :manner 无线电 (acceptable but worse, 2 of 5 runs). Better: :instrument 无线电. 「用无线电」是工具，用 :instrument。
- [doc-temporal] 本句事件的先后: 用 (A :before B) 串成链，实际意思是 B 在 A 之前，整条顺序写反 (wrong, 4 of 5 runs). Better: 卸下 → 离开 → 命中 → 存活/移动，用 :after 写对. (A :before B) 是 B 在 A 之前。r1、r4、r5 写成 (卸下 :before 离开) (离开 :before 命中) (命中 :before 移动)…，意思成了离开在卸下之前、命中在离开之前，整条反了；r2 前一半对（前往 :after 卸下），后面也反了。
- [doc-coref] 车队、仓库、以军、命中的共指: 只有 命中 :subset-of 空袭 (acceptable but worse, 1 of 5 runs); 同样没有共指 (wrong, 1 of 5 runs). Better: 车队、仓库 链前文（r1、r5 还有以军和 命中 :subset-of 空袭）. guideline 5.3：车队、仓库就是第 14 句的车队、仓库，以军即前文的以色列国防军；第一辆车被命中是整场空袭的一部分，可用 :subset-of。

### Sentence 16: 第二   辆  车  在  行驶   了  数十   秒钟   后  也  被  导弹   命中   ，  离  第一   辆  汽车   被  击毁   的  位置   仅有   约  900 米  。

Reviewer's notes on the annotator's choices:
- [sense] 「离……约 900 米」的义项与论元: 离-01 + :extent distance-quantity (wrong, 3 of 5 runs); 离-01 :ARG1 车 :ARG2 位置 :ARG3 distance-quantity (wrong, 1 of 5 runs); 相隔-01 :ARG1 车 :ARG2 位置 :extent … (wrong, 1 of 5 runs). Better: 离-02 :ARG0 车 :ARG1 位置 :ARG2 (distance-quantity 900 米). PropBank 离-02：ARG0 entity described，ARG1 entity distance measured from，ARG2 distance；离-01 是「离开」（ARG0 entity leaving，ARG1 place leave from），没有 ARG2/ARG3。r1 改用原文没有的「相隔」，而且 相隔-01 只有 ARG0、ARG1。
- [structure] 「仅有」: 没有标 (acceptable but worse, 3 of 5 runs). Better: distance-quantity :mod 仅有 / 仅. 「仅有约 900 米」的「仅」是限制性修饰，应作 :mod 保留。
- [structure] 「也」: 没有标 (wrong, 1 of 5 runs). Better: 命中 :mod 也. 训练数据把「也」「亦」标成事件的 :mod（chinese_umr-0003 第 12 句 :mod (亦)、chinese_umr-0007 第 40 句）；gold 漏了。
- [role] 「击毁」与「位置」: 位置 :ARG1-of 击毁（位置被击毁） (wrong, 2 of 5 runs); place :location-of 击毁 (acceptable but worse, 1 of 5 runs). Better: 位置 :place-of 击毁（击毁 :place 位置）. PropBank 击毁-01 ARG1 是被击毁物，被击毁的是第一辆汽车，位置是击毁发生的地点，应为 :place。项目规则用 :place 不用 :location。
- [doc-temporal] 行驶与命中的先后: (行驶 :before 命中)：命中在行驶之前 (wrong, 4 of 5 runs). Better: (行驶 :after 命中)：命中在行驶之后. 「行驶了数十秒钟后也被命中」：命中在行驶之后（或行驶的终点）；(A :before B) 是 B 在 A 之前，r1、r2、r4、r5 写反。r5 还写了第一辆车被击毁在第 15 句命中之后，二者其实是同一事件。gold 的 :contained 可以接受，但 :after 更贴原文「后」。
- [doc-coref] 车、击毁的跨句共指: 只有 击毁 同指第 15 句命中 (acceptable but worse, 1 of 5 runs); 链了两辆车，另有自己链自己的三元组 (wrong, 1 of 5 runs). Better: 两辆车链到第 15 句，击毁 同指第 15 句的命中. guideline 5.3：第一辆、第二辆车就是第 15 句的两辆车，「第一辆汽车被击毁」就是第 15 句的第一次命中。r2 写了 (X :same-entity X)，无意义。

### Sentence 17: 幸存者    移动   到  第三   辆  汽车   继续   逃命   ，  但  在  驶离   第二   辆  车  被  袭击   地点   约  1.6 公里   后  遭到   无人机    第三次    袭击   ，  车队   的  7  名  人道   工作者    全员   身亡   。

Reviewer's notes on the annotator's choices:
- [structure] 「但」的转折概念和角色: contrast-01 :ARG1 … :ARG2 … (acceptable but worse, 3 of 5 runs). Better: contrast-91 :ARG1 … :ARG2 …. guideline 2.5 / 精简版：转折用 (contrast-91 :ARG1 … :ARG2 …)（或 but-91），训练数据（chinese_umr-0014 第 13 句等）的 contrast-91 都用 :ARG1/:ARG2；gold 用 :op1/:op2。contrast-01 是英语 PropBank 的 roleset，训练数据只有一处，不如 contrast-91。
- [role] 「移动到第三辆汽车」: 移动 :ARG2 汽车 (wrong, 1 of 5 runs); 移动 :ARG4 汽车 (wrong, 3 of 5 runs). Better: 移动 :goal 汽车. PropBank 移动-01 只有 ARG0、ARG1，终点用 :goal（gold 第 15 句也用 :goal）。
- [structure] 「继续逃命」: 逃命 :mod 继续 (acceptable but worse, 2 of 5 runs); 漏了「继续」 (acceptable but worse, 2 of 5 runs). Better: 继续-01 :ARG1 逃命（移动 :purpose 继续 / 并列）. PropBank 有 继续-01（ARG1 thing that continues），「继续逃命」应以 继续-01 带 逃命 作 ARG1；作 :mod 丢了谓词，r2、r3 丢了这个词。
- [role] 「驶离……地点」的论元: 驶离 :ARG1 地点（:ARG0 幸存者） (wrong, 5 of 5 runs). PropBank 驶离-01：ARG0 agent，ARG1 vehicle，ARG2 location；驶离的地点是 ARG2，ARG1 是车辆，系统都把地点放成 ARG1。gold 的论元号对，但没有 ARG0/ARG1，可补 驶离 :ARG1 第三辆汽车。
- [structure] 「遭到……袭击」: 省去 遭到，袭击 没有被袭者，作 身亡 的 :cause (acceptable but worse, 1 of 5 runs). PropBank 遭到-01：ARG0 entity described，ARG1 thing arg0 suffers；保留遭到或把它当被动标记省去都可以，被袭者是第三辆车还是幸存者都说得通。r4 丢了被袭者，把转折的后半句改成了因果。
- [role] 「第二辆车被袭击的地点」: place :location-of 袭击 (acceptable but worse, 1 of 5 runs); 地点 :ARG1-of 袭击 (wrong, 1 of 5 runs). Better: 地点 :place-of 袭击（袭击 :ARG1 车）. PropBank 袭击-01 ARG1 是被袭击者（第二辆车），地点是 :place；r4 把地点当成被袭击者（第 16 句同样的错）。项目规则不用 :location。
- [role] 「身亡」的论元: 身亡 :ARG1 工作者 (wrong, 1 of 5 runs). Better: 身亡 :ARG0 工作者. PropBank 身亡-01 只有 ARG0 entity described。r2、r4 用 person :ARG0-of 工作-01 代替「工作者」，也可以。
- [doc-temporal] 本句事件的先后: 用 (A :before B) 串链，方向全反 (wrong, 4 of 5 runs). Better: 命中 → 移动 → 驶离 → 袭击 → 身亡，用 :after 写对. (A :before B) 是 B 在 A 之前。r1、r2、r4、r5 写 (命中 :before 移动) (移动 :before 驶离) (袭击 :before 身亡)…，意思都成了后发生的在前（同第 12–16 句）。gold 的 (遭到 :after 袭击) 把同一事件的两个节点排成先后，小问题。

### Sentence 18: 整个   逃离   追杀   的  距离   长达   2.43 公里   ，  过程   中  几乎   每  一  辆  车  都  被  精确   命中   ，  其中   第二   辆  车  更  被  直接   命中   。

Reviewer's notes on the annotator's choices:
- [sense] 「长达」的义项与论元: 长-01 :ARG1 距离 + :ARG2/:extent 距离量 (wrong, 4 of 5 runs); 长-03 :ARG1 距离 :ARG2 距离量 (wrong, 1 of 5 runs). Better: 长达-01 :ARG0 距离 :ARG1 2.43 公里. PropBank 有 长达-01（ARG0 thing described，ARG1 length），正对「距离长达 2.43 公里」；长-01 是「生长」（ARG1 thing that grow），长-03 是「增长到」，都不对，且都没有 ARG2。
- [role] 「逃离追杀」的论元: 逃离 :ARG2 追杀 (wrong, 1 of 5 runs). Better: 逃离 :ARG1 追杀. PropBank 逃离-01 只有 ARG0 agent、ARG1 location left，没有 ARG2。
- [attr] 「更」: 命中 :degree intensifier（常量） (acceptable but worse, 1 of 5 runs). Better: 命中 :degree 更. guideline 4.2：程度副词作 :degree 概念节点（:degree (v / very)）；gold 漏了「更」，r5 写成常量。
- [doc-modal] 各事件的 modal 父节点: 漏了追杀（r4 还漏了逃离） (wrong, 3 of 5 runs). Better: 逃离、追杀都有 modal. guideline 5.2 / 7 节：每个事件都要有 modal 父节点（同第 13、14 句）。
- [doc-coref] 第二辆车与它被命中的共指: 只链第二辆车（r5 另把逃跑/逃命作逃离的子集） (acceptable but worse, 2 of 5 runs); 只有 命中 同指第 16 句 (acceptable but worse, 1 of 5 runs). Better: 第二辆车 链前文，命中 同指第 16 句的命中. guideline 5.3：第二辆车就是第 16、17 句的车，它被直接命中就是第 16 句的命中。r2 还写了 (导弹 :subset-of 命中)，把实体当成事件的子集，错。

### Sentence 19: 根据   以军   的  说法   ，  他们   得到   情报   称  当时   发现   有  一名   持有   枪械   的  武装   人员   混  在  该  货车   中  ，  该名   武装   人员   和  货车   停留   在  仓库   中  ，  而  世界   中央   厨房   的  车队   则  按照   事先   获得   以军   批准   的  路线   离开   仓库   ，  但  负责   确保   世界   中央   厨房   车队   行驶   路线   安全   的  部门   “为了确保交通路线安全”，            还是   向  无人机    操作员    下达   了  攻击   命令   。

Reviewer's notes on the annotator's choices:
- [structure] 「情报称……」: 情报 :ARG1-of (称-01 :ARG1 …) (wrong, 1 of 5 runs). Better: 情报 :topic 发现. 情报的内容不是和情报「等同」，:topic（或 称-02 :ARG0 情报 :ARG1 内容）更合适。PropBank 称-01 是「称呼」（name assigner / receiver / name），「情报称」的「称」是 称-02（claimer, thing claimed），r5 义项错。
- [sense] 「混在该货车中」的义项: 混-01 :ARG1 人员 / person :ARG0-of 混-01 (wrong, 5 of 5 runs). Better: 混-03 :ARG0 人员. PropBank 混-03 是 entity sneaking in（混入），正是这里的意思；混-01 是 mix together（ARG0 agent，ARG1 entity arg0 mixes together），不对。
- [role] 「停留在仓库中」的论元: 停留 :ARG1 (人员 和 货车) :place 仓库 (wrong, 4 of 5 runs). Better: 停留 :ARG0 (人员 和 货车) :ARG1 仓库. PropBank 停留-01：ARG0 entity described，ARG1 location arg0 stays in；停留者是 ARG0，处所是核心论元 ARG1，不应降为 :place。
- [structure] 「按照……路线离开」: 离开 :manner 路线（没有 按照） (acceptable but worse, 1 of 5 runs); 离开 :path 路线（没有 按照） (acceptable but worse, 1 of 5 runs). Better: 离开 :manner (按照-01 :ARG1 路线). PropBank 按照-01：ARG1 prototype；原文有动词「按照」，应保留为谓词。
- [concept] 「确保……安全」的 安全: 安全（名词）:poss/:mod 路线 (acceptable but worse, 5 of 5 runs). Better: 安全-01 :ARG0 路线. 「确保路线安全」里安全是谓词性状态，PropBank 有 安全-01（ARG0 theme）。作名词也能理解，算小问题。
- [structure] 「为了确保交通路线安全」: 没有标这一小句 (wrong, 2 of 5 runs). Better: 下达 :purpose 确保-01. 原文用引号括出的「为了确保交通路线安全」是下达命令的目的（guideline 2.5 为了 → :purpose），r2、r4 整句漏掉。
- [role] 「攻击命令」: 命令-01 :ARG1 攻击-01 (wrong, 2 of 5 runs). Better: 命令 :mod 攻击-01 / 命令 :topic 攻击-01 / 命令 :mod 攻击. PropBank 命令-01：ARG1 order receiver，ARG2 predicate；作事件时攻击应是 ARG2（受令者操作员是 ARG1），r1、r5 把攻击放到 ARG1。作名词时 :mod / :topic 都可以。
- [structure] 「还是」: 没有标 (acceptable but worse, 4 of 5 runs). Better: 下达 :mod 还是. 「还是下达了攻击命令」的「还是」表示让步（尽管如此仍然），可作 :mod 保留；转折本身已由 contrast/but 表达，漏掉影响不大。
- [doc-temporal] 本句的时间关系: 说 写成在 DCT 之后或 DCT 在说之前；离开、下达、攻击用 :before 串链写反 (wrong, 4 of 5 runs). Better: 得到在 DCT 前；批准 → 离开 → 下达 → 攻击，方向写对. (A :before B) 是 B 在 A 之前，(A :after B) 是 B 在 A 之后。r2、r5 的 (document-creation-time :after 说) 表示说在文档时间之后，r4 的 (说 :before document-creation-time) 表示文档时间在说之前，r1 的 (第 1 句空袭 :before 说) 表示说在空袭之前，都反了；(离开 :before 下达) (下达 :before 攻击) 等也都写反（同第 12–17 句）。
- [doc-coref] 车队、世界中央厨房、以军、货车、仓库的共指: 只链了一个 (acceptable but worse, 2 of 5 runs). Better: 链了其中多数. guideline 5.3：这些实体前文都出现过（车队第 17 句、世界中央厨房第 14 句「该组织」、以色列军队第 15 句、该货车第 14 句、仓库第 15 句）。r5 把句内同一路线写成 :coref 三元组，句内应用重入。

### Sentence 20: 世界   中央   厨房   指出   ，  即使   车队   汽车   的  车顶   和  侧面   清楚   印有   该  团体   的  标志   ，  以军   还是   在  受  他们   控制   的  “  去  冲突   地带   （  deconflicted zone ）  ”  对  车队   发动   了  袭击   。

Reviewer's notes on the annotator's choices:
- [sense] 「印有」的义项与论元: 印-01 :ARG1 标志 :place (车顶 和 侧面) (acceptable but worse, 3 of 5 runs); 印有-01 :ARG1 标志 :ARG2 (车顶 和 侧面) (wrong, 1 of 5 runs); 印有-01 :ARG1 (车顶 和 侧面) :ARG2 标志 (wrong, 1 of 5 runs). Better: 印有-01 :ARG0 标志 :ARG1 (车顶 和 侧面). PropBank 印有-01：ARG0 thing printed，ARG1 location where arg0 is printed，没有 ARG2；r2、r5 的论元号错。原词是「印有」，PropBank 正好有 印有-01，改用 印-01 + :place 意思不错但不如原词。
- [concept] 「去冲突地带（deconflicted zone）」: 命名实体 地带/zone/place :name "去" "冲突" "地带" (acceptable but worse, 5 of 5 runs). Better: 去冲突地带 :ARG1-of (identity-91 :ARG2 deconflicted-zone). 「去冲突地带」是军事术语，不是专名，按普通名词处理更合适（guideline 2.2 命名实体只用于专名）；括注的英文原文 gold 用 identity-91 保留，可接受。系统作命名实体，r1 还用了英文类型 zone、r2/r3/r5 用中文「地带」作类型。
- [structure] 「还是」: 没有标 (acceptable but worse, 4 of 5 runs). Better: 发动 :mod 还是. 同第 19 句：「还是」表示尽管如此仍然，可作 :mod 保留；让步已由 :concession 表达，漏掉影响不大。
- [doc-modal] 世界中央厨房「指出」的内容的 conceiver: 挂在世界中央厨房下，但漏了 袭击、控制 (acceptable but worse, 1 of 5 runs). Better: 内容挂在 世界中央厨房 下. guideline 5.2：转述的内容，作者确信说话人，说话人确信内容：(author :full-affirmative 世界中央厨房) (世界中央厨房 :full-affirmative 发动 …)。gold 把世界中央厨房所指出的事都写成作者直接断言。
- [doc-temporal] 指出与袭击的先后: (指出 :after 发动) 等：发动在指出之后 (wrong, 2 of 5 runs); (发动 :before 指出)、(指出 :before DCT)：方向都反 (wrong, 1 of 5 runs); (第 1 句空袭 :before 指出)：指出在空袭之前 (wrong, 1 of 5 runs). Better: (指出 :before 发动)：发动在指出之前；DCT :before 指出. (A :before B) 是 B 在 A 之前。袭击在世界中央厨房指出之前发生；r1、r2、r4、r5 都按「A 在 B 之前/之后」写，方向反了（r5 还写了 DCT :after 指出）。gold 没写错，但袭击和指出的先后只靠 overlap 链间接连接，不清楚。
- [doc-coref] 世界中央厨房、车队、以军、袭击的共指: 没有共指 (wrong, 1 of 5 runs). Better: 链了大部分. guideline 5.3：世界中央厨房、车队、以色列军队见第 19 句，这次袭击就是前文的空袭；句内同一实体（该团体 = 世界中央厨房；gold 两个车队节点）应是同一个变量（重入），r5 把句内的该团体写成 :coref 三元组也不对。

### Sentence 21: 调查   报导   组织   啤令猫    进行   影像   分析   并  报导   这次   空袭   具有   “  以色列    的  精准   空袭   的  特征   ”  ，  第一次    空袭   的  全球   定位   坐标   是  北纬   31.4118 °  东经   34.3231 °  [  坐标   1  ]  ，  第二次    是  北纬   31.4168 °  东经   34.3290 °  [  坐标   2  ]  ，  而  第三次    是  北纬   31.4005 °  东经   34.3115 °  [  坐标   3  ]  。

Reviewer's notes on the annotator's choices:
- [role] 「影像」与「分析」的关系: 分析 :mod 影像 (acceptable but worse, 4 of 5 runs). Better: 分析 :ARG1 影像. PropBank 分析-01：ARG0 analyzer，ARG1 thing analyzed。「影像分析」是分析影像，影像是被分析的对象，应作 ARG1，不是类型修饰 :mod。
- [concept] 「啤令猫」的实体类型: 组织（中文词作类型） (acceptable but worse, 2 of 5 runs). Better: organization. guideline 2.1/2.2：命名实体的类型用英文类型词（organization），中文普通名词「组织」不作实体类型；原文的「组织」可作同位修饰另立节点。
- [structure] 「调查报导组织」的表示: :mod 调查报导组织（三个词合成一个概念） (acceptable but worse, 1 of 5 runs). 同位的类别描述作修饰或 identity-91 都说得通。s3/r1 把「调查 报导 组织」三个词连同类型词并成一个概念，不合 guideline 2.1 按原词立概念的做法，略差。
- [structure] 「精准空袭的特征」中特征与空袭的关系: 特征 :poss 空袭（旧角色名） (acceptable but worse, 4 of 5 runs). Better: 特征 :possessor 空袭. 「（以色列的精准）空袭的特征」是空袭所有的特征，特征 :possessor 空袭；gold 用 identity-91 把特征等同于空袭，意思错。:poss 是旧名，按发布数据应为 :possessor（本段第一次出现，全篇如此）。
- [structure] 「以色列的精准空袭」中以色列挂在哪: 空袭 :poss 以色列（旧角色名） (acceptable but worse, 4 of 5 runs). Better: 空袭 :possessor 以色列. 「以色列的精准空袭」中以色列修饰空袭（空袭的发动者，也可写 空袭-01 的 ARG0 agent）；gold 把以色列挂到「特征」下且方向反了（:possessor-of 表示特征是以色列的所有者）。
- [concept] 坐标值的写法: 坐标 :name "北纬" "31.4118" "°" … (acceptable but worse, 1 of 5 runs); thing :name "北纬" "31.4118" "°" … (acceptable but worse, 1 of 5 runs). guideline 没有规定经纬度的写法；训练数据 chinese_umr-0013 第 2 句「北纬 23.77 度、东经 121.66 度」写作 and (location :direction 北 :quant 23.77 :unit 度) …，与 s3/r1、r2、r5 的 :quant + :unit 接近，gold 的 :lat/:long 也表达了数值。把坐标当作专名、逐个字符串写进 :name（s3/r3、s3/r4）不合 guideline 2.2 命名实体的用法，数值也成了字符串。
- [structure] 「全球定位」修饰坐标: （没有标全球定位） (acceptable but worse, 2 of 5 runs). Better: 坐标 :mod 全球定位. 原文「全球定位坐标」有修饰语，漏标只是丢了一点信息；gold 没有「坐标」节点，无处挂，不写 fix。s3/r5 三个坐标都加了「全球定位」，原文只在第一个出现，算可接受。
- [doc-modal] 报导内容（具有）的 modal conceiver: 啤令猫 → 具有，但缺 author → 啤令猫 (acceptable but worse, 1 of 5 runs). Better: author → 啤令猫 → 具有. guideline 5.2（abridged）：转述内容 author 对说话人确定、说话人对内容确定，「这次空袭具有以色列精准空袭的特征」是啤令猫报导的内容，应挂在啤令猫（或报导事件）下。gold 全挂 author，且「具有」节点完全没有 modal 父节点。
- [doc-temporal] 报导、分析相对文档时间和先后: 方向反：(DCT :after 报导)/(报导 :after 进行) 等，读成「A 在 B 之前」 (wrong, 3 of 5 runs); 方向反：(报导 :before DCT)(进行 :before 报导) (wrong, 1 of 5 runs). Better: (DCT :before 报导)(报导 :before 进行)，方向对. 文档级 (A :before B) 是 B 在 A 之前（abridged 5.1：过去事件写 (document-creation-time :before e)）。s3/r1、r2、r5 全篇把过去事件写成 (document-creation-time :after e)，s3/r4 写成 (e :before document-creation-time)，都是把父子读反，全篇如此（第 21–29 句同一习惯）；只有 s3/r3 方向对。gold 的事件先后对，但分析只经修饰语「调查」(DCT :overlap) 一路 :overlap 接上来，等于说分析与文档时间重合，应为 DCT :before 分析。
- [doc-coref] 空袭与前文的共指: 同上，但写成 (后提及 :same-event 前提及) (acceptable but worse, 2 of 5 runs). Better: 这次空袭 ↔ 第 1 句空袭，三次空袭 ↔ 第 15–17 句命中/袭击，前者在前（个别反向）. 「这次空袭」就是前文的袭击事件，第一、二、三次空袭分别是第 15、16、17 句的命中/袭击；guideline 5.3 要连到最近的前文提及，前面的写在前。s3/r1、r5 把本句的变量写在前（s3/r2 也有一条），方向不合 5.3。gold 这里一条都没有（全篇 coref 都极少）。

### Sentence 22: 第二次    空袭   发生   位置   离  第一次    相隔   了  800 米  ，  第三次    空袭   离  第二次    的  位置   隔  了  1.6 公里   。

Reviewer's notes on the annotator's choices:
- [sense] 「隔」的概念与义项: 相隔-01（不按原词） (acceptable but worse, 2 of 5 runs). Better: 隔-01. 原词是「隔」，PropBank 有 隔-01（ARG0 theme，ARG1 entity separating members of arg0），应写 隔-01；s3/r1、r5 换成前一分句的「相隔」，不合 guideline 2.1 按原词立概念。
- [role] 「相隔了800米」的论元: ARG1 位置2/空袭2，ARG2 位置1/空袭1，:extent 800米 (wrong, 5 of 5 runs). PropBank 相隔-01 只有 ARG0（相隔的两方）和 ARG1（隔开它们的东西，例「中国和以色列相隔万水千山」「相隔一段时间」）。两个位置合起来是 ARG0，800 米是 ARG1；gold 用了不存在的 ARG2，系统用了不存在的 ARG2，并把距离放进 :extent。
- [role] 「隔了1.6公里」的论元: ARG1 空袭3，ARG2 位置2，:extent 1.6公里 (wrong, 5 of 5 runs). PropBank 隔-01 只有 ARG0（被隔开的成员）和 ARG1（隔开它们的东西）。第三次空袭（的位置）与第二次的位置合为 ARG0，1.6 公里是 ARG1。gold 和系统都用了不存在的 ARG2（s3/r1、r5 用的是 相隔-01，同样没有 ARG2）。
- [structure] 「第二次空袭发生位置」的表示: 位置 :location-of 空袭（旧角色名） (acceptable but worse, 1 of 5 runs); 位置 :ARG1-of 发生-01 :ARG1 空袭（两个 ARG1） (wrong, 1 of 5 runs). Better: 位置 :place-of 空袭（不立发生）. 「空袭发生（的）位置」即空袭的地点，空袭 :place 位置。保留「发生」也可以，但 PropBank 发生-01 的 ARG0 是发生的事件、ARG1 是受影响者，s3/r4 让发生同时以位置和空袭作 ARG1，错。:location 按项目规则应为 :place（s3/r3 全篇如此，只在这里写一次）。
- [structure] 省略的「第一次」与「第二次的位置」: 第一次直接作 空袭-01（无位置）；第二次的位置另立 (acceptable but worse, 1 of 5 runs). 「离第一次相隔」省略了「（空袭发生的）位置」，补成 位置 :place-of (空袭-01 :ord 1) 最完整；gold 的 implicit-argument 不是 guideline 里的概念，丢了空袭；s3/r1 拿空袭本身和位置比距离。第二次的位置复用已有节点（gold、s3/r2）或另立再共指都可以。
- [doc-temporal] 「相隔」「隔」两个状态的时间: 挂在空袭下 :overlap，另有 (空袭3 :after 空袭2) 等方向反 (acceptable but worse, 1 of 5 runs). abridged 5.1 每个事件都要有 temporal 父节点；距离是地点之间的恒定状态，DCT :overlap 或 :overlap 空袭都说得通。gold 只给两次空袭定了时间。s3/r2 的 (空袭3 :after 空袭2)(空袭2 :after 空袭1) 说的是空袭2 在空袭3 之后，方向反（同第 21 句的读反习惯）。
- [doc-coref] 第二、三次空袭与第 21 句的共指: same-event 第 21 句各次空袭，但本句变量写在前 (acceptable but worse, 3 of 5 runs); same-event 第 15–17 句（跳过第 21 句），本句变量写在前 (acceptable but worse, 1 of 5 runs). Better: same-event 第 21 句各次空袭，前文在前. 项目规则 :subset-of 成员在前（成员 :subset-of 集合），gold 把整体「这次空袭」写在前，方向反；而且第二、三次空袭在第 21 句已有提及，按 guideline 5.3 应 :same-event 连到最近的提及（前文在前）。

### Sentence 23: 根据   联合国    人道   事务   协调   厅  （  OCHA ）  ，  头  两次   遇袭   地点   的  道路   获  以色列    指定   为  “  人道主义     援助   可用   道路   （  accessible road for humanitarian aid ）  ”  ，  第  三次   遇袭   地点   则  在  这条   公路   的  旁边   。

Reviewer's notes on the annotator's choices:
- [sense] 「遇袭」的义项: 遇袭-01 (wrong, 5 of 5 runs). Better: 遇袭-00. PropBank 没有「遇袭」（look.py pb 查无义项），按 guideline 2.1 不在 PropBank 的谓词写 -00；系统凭空编号 -01。
- [attr] 「头两次」的表示: 遇袭 :quant 2（丢「头」） (acceptable but worse, 1 of 5 runs); 遇袭 :ord (ordinal-entity :value 2)（第二次） (wrong, 2 of 5 runs). Better: 遇袭 :quant 2 :mod 头. 「头两次」是前两次遇袭，数量 2、限定为最前面的；s3/r2、r4 写成序数 2（第二次），意思错。gold 造了一个 have-frequency-91 再加序数 1，绕但大致表达了意思。
- [concept] 「人道主义援助可用道路」（指定的 ARG2）: 道路/thing :name "人道主义" "援助" "可用" "道路" (acceptable but worse, 3 of 5 runs); 道路 :name "人道主义援助可用道路" (acceptable but worse, 1 of 5 runs); 人道主义援助可用道路 :name "accessible" "road" … (acceptable but worse, 1 of 5 runs). 引号里的「人道主义援助可用道路」是以色列给道路定的类别，不是专名；gold 按词分解（PropBank 可用-01 ARG0 entity with the property）合理，括号里的英文译名可以不标。系统把它当命名实体写进 :name，不合 guideline 2.2。
- [concept] 第三分句「位于旁边」的谓词: be-located-at-91（AMR 写法） (acceptable but worse, 1 of 5 runs); 位于-01 :ARG1 地点 :ARG2 旁边 (wrong, 2 of 5 runs); 旁边-01 :ARG1 地点 :ARG2 公路 (wrong, 1 of 5 runs). Better: have-place-91 :ARG1 地点 :ARG2 旁边. 「（地点）在公路旁边」是处所类非动词句，guideline 2.3 用 have-place-91（ARG1 theme，ARG2 place）。PropBank 位于-01 是 ARG0 entity described、ARG1 location，s3/r2、r3 的 ARG1/ARG2 错位（且原文是「在」不是「位于」）；PropBank 没有 旁边-01，s3/r1 凭空造义项；be-located-at-91 是 AMR 名称。
- [structure] 「这条公路的旁边」: 旁边 :part-of 公路，公路 :refer-to 道路 + 句内 coref (acceptable but worse, 1 of 5 runs); 旁边 :poss 公路，无同指 (acceptable but worse, 1 of 5 runs); 旁边 :poss (公路 :mod 这条)，句内 coref 连道路 (acceptable but worse, 1 of 5 runs); 旁边 :op1 (公路 :mod 这条)，无同指 (acceptable but worse, 1 of 5 runs). 「这条公路」就是前一分句的道路，guideline 5.3 句内同指写成重入；旁边是公路的一部分（:part-of 公路，或 :possessor 公路）。gold 的 :possessor-of 表示旁边拥有道路，方向反。系统没有一份完全对：:poss 是旧名，:refer-to 不是 UMR 角色，:op1 不合，句内同指写成了 :coref 三元组。s3/r1 的谓词问题已在上一条判。
- [doc-coref] 遇袭、以色列与前文的共指: 第三次遇袭 same-event 前文、头两次 subset-of 第 1 句空袭等，但多为本句变量写在前 (acceptable but worse, 5 of 5 runs). 第三次遇袭＝第 22 句第三次空袭，头两次遇袭是整个空袭事件的一部分，以色列与前文同指；gold 一条没有。系统都连了，但普遍把本句变量写在前（guideline 5.3 前文在前），s3/r4 一对还正反各写一遍。

### Sentence 24: 世界   中央   厨房   的  7 名  穿着   保护   装备   的  人道   工作者    由  巴勒斯坦     红  新月   会  移送   到  代尔   拜莱赫    市  的  舒哈达    阿克萨    医院   进行   抢救   ，  但  最终   全员   不治   身亡   。

Reviewer's notes on the annotator's choices:
- [concept] 「但」的概念与角色: contrast-01 :ARG1 :ARG2（AMR 写法） (acceptable but worse, 3 of 5 runs). Better: contrast-91 :ARG1 :ARG2. abridged 2.5：转折「但」用 but-91（或 contrast-91），论元是 :ARG1/:ARG2（训练数据 but-91 都带 :ARG1/:ARG2），gold 用了 :op1/:op2。contrast-01 是 AMR 的写法，UMR 的抽象谓词是 contrast-91。
- [sense] 「穿着」的义项: 穿着-01 (wrong, 5 of 5 runs). Better: 穿着-00. PropBank 没有「穿着」（查询回落到「穿」：穿-01 ARG0 agent，ARG1 clothing），按 guideline 2.1 写 穿着-00 或按 穿-01 立概念都可以；穿着-01 是凭空的编号。
- [role] 「世界中央厨房的」工作者: 工作者 :poss WCK（旧角色名） (acceptable but worse, 2 of 5 runs). Better: 工作者/person :part-of WCK. 项目规则：部分为父节点用 :part-of，整体为父节点用 :part。gold 以工作者为父写 :part，等于说 WCK 是工作者的一部分，方向反。
- [attr] 「7名」的量词: 只有 :quant 7，丢量词 (acceptable but worse, 5 of 5 runs). Better: 工作者 :quant 7 :unit 名. 项目规则：量词都保留为 :unit。五份系统都丢了「名」（全篇如此，系统里只在这里写一次）。
- [concept] 医院的实体类型: 医院（中文词作类型） (acceptable but worse, 2 of 5 runs). facility、hospital 都在 AMR 的命名实体类型表里；中文普通名词「医院」不作实体类型（guideline 2.2）。
- [concept] 专名的分词: 代尔/拜莱赫；红/新月会 (acceptable but worse, 1 of 5 runs); 代尔/拜莱赫/市；红/新月会 (acceptable but worse, 1 of 5 runs). guideline 2.2：专名按词拆成 :opN（原文切成 代尔 拜莱赫 市、红 新月 会）。gold 把「代尔拜莱赫」并成一个 :op，s3/r1、r4 把「新月会」并成一个 :op，都与切词不符。名字里带不带「市」两可。
- [role] 「抢救」的 ARG1 与 aspect: 抢救-01 无 ARG1，aspect process (acceptable but worse, 2 of 5 runs). Better: 抢救-01 :ARG1 工作者，aspect process. PropBank 抢救-01：ARG0 agent，ARG1 entity try to save；被抢救的就是这 7 名工作者，句内可以重入。抢救进行了但没有救活，performance（完成并达到结果）不贴切，process 或 endeavor 更合适。
- [sense] 「不治身亡」的概念: 身亡-01 :ARG0 …（丢「不治」） (acceptable but worse, 1 of 5 runs); 不治-01 :ARG0-of 身亡-01（身亡的 ARG0 成了不治） (wrong, 1 of 5 runs); 身亡-01 :ARG1 …（身亡-01 没有 ARG1）:manner 不治 (wrong, 1 of 5 runs). PropBank 有 身亡-01（ARG0 entity described）和 不治-01（ARG0 entity described），没有「不治身亡」，合成概念只能写 -00（若作固定说法，guideline 2.6），gold 的 -01 是凭空编号；拆成 身亡-01 加 不治 也可以。s3/r2 让「不治」作身亡的 ARG0，s3/r5 给身亡加了不存在的 ARG1。

### Sentence 25: 遗体   被  运  至  加沙   南部   的  医院   。

Reviewer's notes on the annotator's choices:
- [sense] 「运至」的义项与终点论元: 运-01 :ARG2 医院（运-01 没有 ARG2） (wrong, 2 of 5 runs); 运-01 :ARG4 医院 (wrong, 1 of 5 runs); 运送-01 :ARG2 医院（换了原词） (acceptable but worse, 2 of 5 runs). Better: 运-02 :ARG2 医院. PropBank 运-01 只有 ARG0/ARG1，运-02 才有 ARG2 destination、ARG3 origin；「运至医院」有终点，应选 运-02。s3/r1、r3、r5 用 运-01 再加 ARG2/ARG4，论元不在该义项里；运送-01 的论元对，但原词是「运」。
- [role] 「加沙南部的医院」的处所结构: 医院 :place (加沙 :mod 南部) (acceptable but worse, 2 of 5 runs). Better: 医院 :place (南部 :part-of 加沙). 医院位于加沙南部：医院 :place 南部；南部是加沙的一部分，以南部为父应写 :part-of（项目规则）。gold 的 医院 :part 南部 说南部是医院的一部分，南部 :part 加沙 说加沙是南部的一部分，两处都反。
- [concept] 「加沙」的实体类型: place (acceptable but worse, 3 of 5 runs); geographic-entity (acceptable but worse, 1 of 5 runs); 地区（中文词作类型） (acceptable but worse, 1 of 5 runs). Better: local-region. 加沙地带是地区，AMR 类型表有 local-region（gold 全篇如此）；place、geographic-entity 太泛，中文普通名词「地区」不作类型（guideline 2.2）。第 26 句「加沙地带」各系统同样如此，不再另写。
- [doc-coref] 「加沙」与前文的共指: 没有 coref (acceptable but worse, 4 of 5 runs). 「加沙」前文多次出现，guideline 5.3 应连；gold 全篇地名都不连，只在小结里提，这里不写 fix。

### Sentence 26: 4 月  3 日  ，  6 名  外籍   工作   人员   遗体   经  埃及   运回   原居国    ，  而  巴勒斯坦     雇员   则  葬  在  加沙   地带   。

Reviewer's notes on the annotator's choices:
- [concept] 「而」连接两个分句: and (acceptable but worse, 3 of 5 runs). Better: contrast-91 :ARG1 :ARG2. 「外籍人员遗体运回原居国，而巴勒斯坦雇员则葬在加沙」是对比，abridged 2.5 用 contrast-91，论元是 :ARG1/:ARG2，gold 用了 :op1/:op2。and 丢了对比义。
- [role] 「运回」的概念与终点论元: 运回-01 :ARG4 原居国（运回-01 没有 ARG4） (wrong, 1 of 5 runs); 运送-01 :ARG2 (国 :ARG1-of 原居-01)（换了原词，原居-01 无此义项） (acceptable but worse, 1 of 5 runs). Better: 运回-01 :ARG2 原居国. PropBank 运回-01：ARG0 agent，ARG1 entity transported，ARG2 destination；原居国是终点 ARG2。PropBank 没有「原居」，s3/r4 的 原居-01 是凭空编号，且把「运回」换成了「运送」。
- [sense] 「葬」的义项: 葬-01 (wrong, 5 of 5 runs). Better: 葬-00. PropBank 没有「葬」，按 guideline 2.1 写 葬-00；系统凭空编号 -01（与第 23 句 遇袭-01、第 24 句 穿着-01 同类）。
- [concept] 「巴勒斯坦雇员」的表示: 雇员 :mod 巴勒斯坦（不作命名实体） (acceptable but worse, 2 of 5 runs); person :ARG0-of 雇-01（雇-01 的 ARG0 是雇主） (wrong, 1 of 5 runs); person :ARG0-of 雇员-01（无此义项） (wrong, 1 of 5 runs). Better: 雇员 :mod (country :name 巴勒斯坦). PropBank 雇-01：ARG0 employer，ARG1 employee，雇员应是 :ARG1-of 雇-01，s3/r2 的 ARG0-of 把雇员说成雇主；PropBank 没有「雇员」谓词，s3/r4 的 雇员-01 凭空。巴勒斯坦是专名，应作命名实体（guideline 2.2）。
- [doc-temporal] 日期与事件的时间挂接: 日期没有时间父节点 (acceptable but worse, 2 of 5 runs). 按项目规则，时间表达挂元节点，:depends-on、:overlap、(DCT :before …) 都接受；s3/r2、r5 的日期没有父节点。葬与运回的先后原文没有说，gold 的 :after 与系统的 :overlap 都缺乏明确依据，不判。
- [doc-coref] 遗体、人员与前文的共指: 没有 coref (wrong, 2 of 5 runs); 6 名人员 :same-entity 第 24 句 7 名工作者（应为 subset） (acceptable but worse, 1 of 5 runs); 遗体 :subset-of 工作者 / 第 25 句遗体 (acceptable but worse, 2 of 5 runs). 6 名外籍工作人员和巴勒斯坦雇员都是第 24 句 7 名工作者的一部分，遗体是第 25 句遗体的一部分，应写 :subset-of（成员在前）；s3/r3 写成 same-entity 不对（6≠7），s3/r4 把遗体当作工作者的子集，s3/r5 只连了遗体。

### Sentence 27: 遇难者    中  1 人  为  原居   于  加沙   南部   拉法   市  的  巴勒斯坦     人  ，  1  人  来自   波兰   ，  1  人  来自   澳大利亚     ，  1  人  具有   美国   和  加拿大    双重   国籍   ，  另外   3  人  来自   英国   ，  其中   两名   遇难   的  英国   人  道工作者     曾  在  英国   皇家   海军   陆战队    服役   。

Reviewer's notes on the annotator's choices:
- [role] 「来自」的论元: 来自-01 :ARG1 person :ARG2 国家 (wrong, 5 of 5 runs). Better: person :ARG0-of (来自-01 :ARG1 国家). PropBank 来自-01：ARG0 entity described，ARG1 source；人是 ARG0，国家是 ARG1。五份系统都把人写成 ARG1、国家写成不存在的 ARG2（三处「来自」都是）。
- [sense] 「原居于」的义项: 居-01 :ARG1 拉法（居-01 是占据位置） (wrong, 1 of 5 runs); 居-01 :place 拉法 (wrong, 2 of 5 runs); 居于-01 :place 拉法（无此义项） (wrong, 1 of 5 runs); 原居-01 :place 拉法（无此义项） (wrong, 1 of 5 runs). Better: 居-02 :ARG0 person :ARG1 拉法 :mod 原. PropBank 居-01 是 position arg0 occupies，居-02 才是 place arg0 lives（ARG1 居住地）；「原居于拉法市」应选 居-02，居住地是 ARG1。PropBank 没有「居于」「原居」，-01 是凭空编号。
- [role] 「加沙南部拉法市」的处所结构: 拉法 :place/:part-of (加沙 :mod 南部) 或 (南部 :mod 加沙) (acceptable but worse, 3 of 5 runs). Better: 拉法 :part-of (南部 :part-of 加沙). 拉法市是加沙南部的一部分，南部是加沙的一部分，部分为父节点用 :part-of（项目规则）；gold 两处 :part 方向都反（与第 25 句同）。
- [concept] 「巴勒斯坦人」的表示: 巴勒斯坦人（合成一个概念） (acceptable but worse, 2 of 5 runs). Better: person :mod (country/nationality :name 巴勒斯坦). 「巴勒斯坦 人」是两个词，巴勒斯坦是专名，应作命名实体修饰 person（guideline 2.2）；合成「巴勒斯坦人」丢了命名实体。
- [structure] 「美国和加拿大双重国籍」: 国籍 :op1 美国 :op2 加拿大（:op 挂在名词上） (wrong, 1 of 5 runs); 国籍 :ARG1-of and（and 没有 ARG1） (wrong, 1 of 5 runs). :opN 只用于 and/or 之类的并列概念，and 也没有 ARG1；s3/r2、r4 的写法不合 guideline 2.5。gold 的 include-91 和 :mod 都说得通。
- [doc-temporal] 第 27 句的时间: 实体（遇难者、person）作时间节点 (wrong, 1 of 5 runs). 「曾在……服役」「原居于」是过去，国籍、来自是现在的状态，gold 的写法对。s3/r2 的 (遇难者 :after 遇难)(person :after 服役) 拿实体作时间节点，没有意义。
- [doc-coref] 遇难者、巴勒斯坦人与前文的共指: 遇难者 same-entity 前文 7 名工作者，但本句变量写在前 (acceptable but worse, 2 of 5 runs); 只有句内 subset-of，没有连前文 (acceptable but worse, 1 of 5 runs). Better: 遇难者 same-entity 前文 7 名工作者，各组人 subset-of 遇难者. 遇难者就是第 24 句的 7 名工作者，1 名巴勒斯坦人就是第 26 句葬在加沙的巴勒斯坦雇员；gold 一条没有。s3/r2、r4 把本句变量写在前（guideline 5.3 前文在前）。

### Sentence 28: 澳大利亚     籍  的  人道   工作者    家属   要求   调查   事件   是否   涉及   战争   罪行   ，  美加   籍  的  人道   工作者    家属   则  拒绝   接受   以色列    的  道歉   ，  他们   要求   展开   独立   调查   并  要求   美国   停止   为  以色列    提供   武器   。

Reviewer's notes on the annotator's choices:
- [sense] 三个「要求」的义项与论元: 要求-01 ×3，第三个只有 :ARG1 停止（美国不是要求的论元） (acceptable but worse, 1 of 5 runs); 要求-02 :ARG1 调查/展开（ARG1 是被要求者） (wrong, 1 of 5 runs). PropBank 要求-01：ARG1 things asked for，ARG2 entity asked from；要求-02：ARG1 askee，ARG2 predicate；要求-03：ARG1 predicate。「要求调查」「要求展开调查」没有被要求者，-01/-03 都合适，gold 的 要求-02 只带 ARG2 也合论元表；「要求美国停止」用 要求-02（ARG1 美国、ARG2 停止）或 要求-01（ARG2 美国）都对。s3/r2 用 要求-02 却把调查放 ARG1（被要求者），错。
- [structure] 「工作者家属」的表示: person :ARG0-of (have-rel-role-91 :ARG1 工作者 :ARG2 家属)（-91，论元错位） (wrong, 1 of 5 runs); person :ARG0-of 家属-01（无此义项） (wrong, 1 of 5 runs). Better: person :ARG1-of (have-rel-role-92 :ARG2 工作者 :ARG3 家属). abridged 2.3：亲属关系名词按 have-rel-role-92 重新表示（ARG1 本人，ARG2 对方，ARG3 关系），也可用 :possessor。gold 的 家属 :possessor-of 工作者 表示家属拥有工作者，方向反（gold 全段 :possessor-of 都这样反用）。s3/r4 用了 -91 且 ARG 错位，s3/r2 造了 家属-01。
- [concept] 「澳大利亚籍」「美加籍」: nationality "澳大利亚"；美加籍 写成 nationality :name "美加" (acceptable but worse, 1 of 5 runs); 澳大利亚籍 / 美加籍 作普通概念 (acceptable but worse, 2 of 5 runs). 国籍里的国名是专名，应作命名实体（guideline 2.2）；「美加」是美国和加拿大的合称（第 27 句「美国和加拿大双重国籍」），拆成两国更准确。
- [structure] 「是否涉及战争罪行」的表示: 涉及 :polarity umr-unknown (acceptable but worse, 1 of 5 runs); 涉及 :polarity (amr-unknown)（旧名、作节点） (acceptable but worse, 1 of 5 runs); 丢了「是否」 (acceptable but worse, 2 of 5 runs). Better: 调查 :ARG1 (truth-value :polarity-of 涉及). guideline 3-2-1-3 例 (1b)「whether he bought the sweater」写作 truth-value :polarity-of；:polarity umr-unknown 是直接是非问句的写法。amr-unknown 按项目规则应为 umr-unknown，也不该立成节点。
- [role] 「涉及」的论元: 涉及-01 :ARG1 事件 :ARG2 罪行 (wrong, 2 of 5 runs). Better: 涉及-01 :ARG0 事件 :ARG1 罪行. PropBank 涉及-01：ARG0 thing described，ARG1 entity involved；没有 ARG2。（s3/r2、r4 还把「战争 罪行」两个词并成一个概念。）
- [structure] 「他们」的处理: 另立 person 3rd plural，句内再用 :coref 连 (acceptable but worse, 2 of 5 runs). 「他们」指美加籍工作者家属，guideline 5.3 句内同指写成重入（或代词节点加重入），不用句内 :coref 三元组。
- [structure] 两个「以色列」节点: 道歉的以色列、提供的以色列各立一个 country 节点 (acceptable but worse, 1 of 5 runs). Better: 一个以色列节点重入. 同句里两次提到以色列，guideline 5.3 句内同指用重入；s3/r5 另立后又用 :coref 连，也不合。
- [concept] 「则」的对比关系: and (acceptable but worse, 2 of 5 runs); contrast-01 (acceptable but worse, 2 of 5 runs). Better: contrast-91 :ARG1 :ARG2. 「澳大利亚籍家属要求……，美加籍家属则拒绝……」用「则」对比两组家属的不同态度，abridged 2.5 用 contrast-91；and 丢了对比，可接受但略差。contrast-01 是 AMR 名称。
- [doc-modal] 「要求」补足事件和「是否涉及」的 modal: 只给主事件 modal，补足事件大多没有 modal 父节点 (acceptable but worse, 1 of 5 runs). Better: 补足事件挂在要求下 unspecified/partial-affirmative，涉及再挂在调查下. guideline 5.2：要求、希望之类补足语事件挂在该谓词下，强度 unspecified（或谓词所含的强度）；被要求的调查、展开调查、停止供武器都还没发生，author 不能断言；「是否涉及战争罪行」是未决的问题（guideline 3-2-1-3 例 (1b) 给 neutral-affirmative）。gold 全部写成 author 确定发生。
- [doc-modal] 「拒绝接受」中接受的 modal: author :full-affirmative 接受 (wrong, 1 of 5 runs); 接受没有 modal 父节点 (acceptable but worse, 1 of 5 runs). Better: 拒绝（或家属）:full-negative 接受. 被拒绝的事件没有发生：abridged 5.2 否定（deny 之类）是 full-negative；家属拒绝接受道歉，接受应挂在拒绝下 full-negative，不能由 author 断言发生。
- [doc-coref] 家属、以色列、道歉与前文的共指: 只连以色列 (acceptable but worse, 1 of 5 runs); 以色列、道歉、美国、加拿大连前文，但多为本句变量写在前 (acceptable but worse, 1 of 5 runs). 以色列的道歉＝第 4 句「以色列……道歉」，以色列、美国与前文同指，澳大利亚籍、美加籍工作者就是第 27 句那两位；gold 一条没有。

### Sentence 29: 世界   中央   厨房   原本   计划   协调   供应   给  加沙   平民   340 公吨   粮食   ，  但  在  其  宣布   暂停   在  加沙   的  人道主义     行动   后  ，  第二   队  前往   加沙   运送   救援   粮食   的  货船   船队   于  4  月  3  日  折返回    塞浦路斯     ，  该  船队   运载   的  约  240 公吨   粮食   即是   援助   粮  中  的  第二   批  ，  而  第一   批次   的  100 公吨   即是   本次   空袭   事件   前  经  加沙   北部   港口   卸下   的  那  一  批  。

Reviewer's notes on the annotator's choices:
- [structure] 全句的转折与对比结构: contrast-01 :ARG1 计划 :ARG2 (and …)，或 and (contrast-01 …) (acceptable but worse, 2 of 5 runs); contrast-01 :ARG1 计划 :ARG2 折返 :ARG3 第二个 identity-91 (wrong, 1 of 5 runs). 「原本计划……，但……折返」是转折（abridged 2.5：but-91 / contrast-91），后面两个「即是」句是补充说明，并列即可。contrast-01 是 AMR 名称；s3/r2 给 contrast 加了不存在的 ARG3。
- [doc-modal] 「计划」补足事件的 modal: 协调、供应没有 modal 父节点 (acceptable but worse, 1 of 5 runs). Better: 计划 → 协调 → 供应（partial-affirmative / unspecified）. guideline 5.2：计划（plan）类谓词的补足语挂在该谓词下，强度 unspecified；「原本计划……但……」表明计划没有实现，author 更不能断言协调、供应发生了。
- [attr] 「第二队」船队的序数: 船队 :ord 2（数字，不是 ordinal-entity） (acceptable but worse, 1 of 5 runs). Better: 船队 :ord (ordinal-entity :value 2). 「第二队……船队」有序数，guideline 2.2 序数写 :ord (ordinal-entity :value 2)；gold 漏了。
- [structure] 「前往加沙运送」: 前往-01 :ARG4 加沙（前往-01 没有 ARG4） (wrong, 1 of 5 runs). Better: 前往-01 :ARG1 加沙 :purpose 运送. PropBank 前往-01：ARG0 agent，ARG1 goal；运送-01 有 ARG2 destination。gold 丢了谓词「前往」，又把终点写成非论元角色 :goal（PropBank 论元能表达时用 ARGn）。
- [role] 「折返回塞浦路斯」的论元: 折返-01 :ARG0 船队 :ARG2 塞浦路斯 (wrong, 1 of 5 runs); 折返-01 :ARG1 船队 :ARG2 塞浦路斯 (wrong, 1 of 5 runs); 折返-01 :ARG0/:ARG1 船队 :ARG4 塞浦路斯 (wrong, 2 of 5 runs). Better: 折返-01 :ARG0 船队 :ARG1 塞浦路斯. PropBank 折返-01：ARG0 agent，ARG1 locative, destination；塞浦路斯是 ARG1，没有 ARG2、ARG4。（s3/r3、r4 还把塞浦路斯标成泛的 place，应为 country。）
- [role] 「加沙北部港口」的处所结构: 港口 :place/:location/:mod，北部与加沙用 :mod 连或丢北部 (acceptable but worse, 3 of 5 runs). Better: 港口 :part-of (北部 :part-of 加沙). 港口在加沙北部：部分为父节点用 :part-of（项目规则），或 :place。gold 两处 :part 方向都反（同第 25、27 句）。
- [doc-coref] WCK、宣布暂停、卸下与前文的共指: 同上，多为本句变量写在前 (acceptable but worse, 2 of 5 runs); 连了部分，另有 (船队 :same-entity 船队) 自环 (acceptable but worse, 1 of 5 runs). Better: 连 WCK、宣布、暂停、卸下、第一批粮食、空袭，前文在前. 宣布暂停人道行动＝第 3 句，经北部港口卸下 100 公吨粮食＝第 13 句，WCK 前文多次出现；gold 只有空袭一条。
