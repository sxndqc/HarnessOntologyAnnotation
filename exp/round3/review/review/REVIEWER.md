# 审阅任务说明（每个审阅者负责一篇文档的一段句子）

## 背景

这里是四篇中文文档（UMR 2.2 clean 训练数据里的 chinese_umr-0003、-0011、-0016、-0018，在这里叫 zh-0003、zh-0011、zh-0016、zh-0018）。每篇有一份人工 gold，和同一个模型（Claude Sonnet 5.5）在同一个设定下跑 5 次得到的 5 份自动标注：

| 名字 | 设定 |
|---|---|
| `s3/r1` … `s3/r5` | 整篇一次标完；guideline 只有一句话；有两个工具（查完整 guideline、查 PropBank），没有训练数据搜索。5 次运行的任务说明措辞略有不同，意思相同 |

目的有两个：(1) **找出系统反复犯的错误**，之后要据此给这个标注器写一份"parse skill"，所以每个比较点上系统错在哪里、依据是什么要写清楚；(2) 找出 gold 里的错误，给出可以机械执行的修改方案，修订后的 gold 用来给系统打分。gold 不是标准答案，它会有错；系统也经常有错。你的判断依据是 UMR guideline（修订版）、中文训练数据的写法和 PropBank，不是"多数系统怎么标"：这 5 份标注出自同一个模型，它们一致不说明它们对。

你负责的文档和句子范围在给你的消息里。**只写两个文件**：`review/items/<doc>.<from>-<to>.json` 和 `review/items/<doc>.<from>-<to>.notes.md`（句号用两位数字，例如 `zh-0011.01-12.json`）。不要改别的任何文件，不要运行 `items.py build`、`score.py`、`build.py`。工作目录是这个包的根目录。

## 已经定下来的规则（项目负责人定的，照做）

- **量词都保留为 `:unit`**（`名词 :quant N :unit (量词)`）。gold 保留量词是对的；标注里省掉量词判 `minor`；gold 漏标量词也是 `minor`，写 fix 补上（`add_node`，role 写 `unit`）。
- **`have-org-role-92`、`have-rel-role-92` 是对的**，`-91` 应改成 `-92`（gold 里的 `-91` 写 fix 改掉，`conf` 给 `high`）。
- **部分和整体**：部分为父节点时用 `:part-of`（`(弦 :part-of 吉他)`），整体为父节点时用 `:part`（`(吉他 :part 弦)`）。方向和角色名配反了判 `bad`，gold 配反了写 fix。
- **`:subset-of` 成员在前**：`(成员或子集 :subset-of 集合)`。写反了判 `bad`，gold 写反了写 fix。
- **拼写按发布数据**：`:possessor`（不是 `:poss`）、`:modal-strength` 和全称小写的强度值、`:refer-person` / `:refer-number` 加小写取值、小写的 aspect 值、`:quote`、`document-creation-time` / `author` / `root`、`umr-unknown`（不是 `amr-unknown`）。系统写旧名字判 `minor`；全篇如此的只在第一次出现处写一条。
- **时间包含只用 `:contained`**：`(A :contained B)` 是 B 在 A 之内。`:contains`、`:includes` 不用。
- **地点用 `:place`**，不用 `:location`；时间用 `:temporal`，`:time` 只用在 `date-entity` 里的钟点。
- **`:cause` 是原因**（什么造成了这个事件），**`:reason` 是理由**（给出的动机或依据）。两个都可以用，按意思判。
- **`:degree` 是性质的强化或弱化**（很、非常、有点），**`:extent` 是事件或状态达到的幅度、数量**。
- **`:modpred` 不用**：情态事件和它辖域内的事件之间的关系写在文档级 modal 里（`(情态事件 :强度 事件)`）。
- **人的类型 `person` 和 `individual-person` 都对**；地名类型用 AMR 的（`city`、`state`、`country`）或 UMR 的（`human-settlement`、`country-partition`）都对。这两类差别不写条目。
- **每句的文档级 modal 都应有 `(root :modal author)`**；句子图里的 `:modal-strength` 不作为模态标注（模态看文档级）。gold 缺 `(root :modal author)` 不逐句写条目，在小结里提一句。
- **时间表达挂到元节点上**，用 `:depends-on` 或 `:overlap` / `(document-creation-time :before …)` 都接受。
- **方位词、时间方位词（上、中、时、后）建节点**是对的。
- **不比较 `:wiki`**：有没有 `:wiki` 都不写条目。
- **不比较重入的写法本身和节点切分的粒度评分**，但一个论元该不该由已有节点充当、一个词该不该拆开，仍然是结构问题，照常判断。

## 这次要注意的

- 查训练数据怎么写：`python3 pipeline/look.py ann <doc> KEYWORD --max 5`（不会返回这篇文档自己的句子）。训练数据只有 clean 部分。不要直接 grep `resources/training/` 下的文件：这四篇文档自己就在里面。
- 完整 guideline 用修订版：`resources/guidelines-revised/umr_guidelines.md`（开头有一节"Conventions of this revised version"），精简版是同目录的 `umr_guidelines_abridged.md`。`look.py gl` 搜的就是修订版。
- PropBank：`python3 pipeline/look.py pb 词`。
- **系统全篇重复的同一种习惯只写一次**：在你这一段里它第一次出现的那一句照实判，写明"全篇如此"，之后的句子里记 `open` 并注明"同一习惯，见第 N 句"，或者不再写。但要在小结文件的"系统的问题"里把这类习惯逐条列清楚（哪些运行、大约多少处、正确写法是什么），这是这次审阅最重要的产出。
- 系统是同一个模型的 5 次运行。5 份都一样而和 gold 不同的地方最值得看：可能是 gold 错，也可能是这个模型的固定错误。两种情况都要有依据才判。
- 对齐不比较。

## 怎么看标注

```bash
python3 pipeline/mechdiff.py zh-0005 3        # 第 3 句：gold 的图，然后是 6 份标注不一致的地方
python3 pipeline/mechdiff.py zh-0005 3-8      # 一段
python3 pipeline/show_sentence.py zh-0005 3 --only gold,s3/r1,a2/r2    # 某几份标注的原文
python3 pipeline/show_sentence.py zh-0005 --grep 发行-01               # 哪些标注的哪些句子里有这段文字
```

`mechdiff.py` 的输出：节点用它对齐的词命名（`19发挥` 是第 19 个词"发挥"上的节点），命名实体用名字（`«阿耀»`），没有对齐的抽象节点用"概念@挂在哪"（`and@8表示:ARG1`）。每个事实后面的 `⟵` 列出哪些标注有它；所有标注都有的事实不列。反向角色已经转正（`:ARG1-of` 写成正向的 `:ARG1`）。"gold 变量"一行给出 gold 每个变量对应的名字，写修改方案时要用 gold 的变量名。

读法上要注意：

- 文档级 temporal 的 `A :before B` 是 UMR 原文的写法 `(A :before B)`：A 是父节点，意思是 **B 在 A 之前**。很容易读反。
- 同一个节点两头相同的边（`2官媒 :mod 2官媒`）是 gold 把两个节点对齐到了同一个词造成的，不是自环；gold 的节点没有对齐而系统对齐了时，同一个节点会以两个名字出现（`15导致: 无节点 [gold]`，另有 `导致-01@…` 的边）。遇到这类情况看原图。
- 反向角色转正后，`:part` 和 `:part-of` 这类方向有意义的角色要回原图确认。
- `?变量名` 是文档级标注里引用了图中不存在的变量。
- 一份标注漏掉一个节点，会连带出很多行，不要逐行当成独立的差别。

这个列表是机械生成的，谁选了什么是准确的，但有噪音：gold 的对齐常有错（两个节点对到同一个词、命名实体没有对齐），抽象节点挂的位置不同会让意思相同的东西看起来不同。看不清的地方用 `show_sentence.py` 看原图。某份标注在某一句没有有效的图（`empty` 或解析失败）时，把它单独归成一个选择"没有有效标注"，status 写 `bad`。

一次不要读太多：建议每次看 2–4 句，写完这几句的条目再看后面的。

## 查依据

```bash
python3 pipeline/look.py pb 进口 恢复                 # PropBank 义项和论元
python3 pipeline/look.py gl modal strength --max 3    # 完整 guideline 里的段落
python3 pipeline/look.py ann zh-0005 进口-01 --max 5   # 训练数据里的先例（不会返回 zh-0005 自己）
```

完整 guideline 是 `resources/guidelines-revised/umr_guidelines.md`（可以直接 grep），精简版是同目录的 `umr_guidelines_abridged.md`，开始前先把精简版读一遍。义项和核心论元的判断必须查 PropBank，不要凭印象。

## 条目

一个条目是一个比较点：一个词的义项或概念、一个角色、一个结构选择、一个属性值（aspect、polarity、refer-number、quant 等）、一类文档级关系（时间、模态、共指）。

要写哪些：

1. **gold 可能有错的地方，一个都不要漏。** gold 和多数系统不同的每一处都要看过并判断。gold 和所有系统相同但明显违反 guideline 的地方，看到了也写。
2. 系统之间有实质分歧的地方。
3. 不写：变量命名、对齐（包括 gold 的对齐错误，只在小结文件里提一句）、同一内容挂在不同抽象节点位置造成的表面差别、op 的顺序。6 份标注完全相同的地方，只有明显违反 guideline 或 PropBank 时才写（单一选择，status `bad`，带 fix）；只是"值得商榷"的不写。
4. 相互连带的差别合成一个条目（例如一个词拆不拆开，连带出三条边的不同，只算一个比较点）。文档级 temporal 的三元组各系统选的事件对很不一样，不要逐条写，按现象归并，例如"报道事件相对文档时间""两个事件的先后"，重点是 gold 有错或缺失的关系，以及系统明显标反的关系。
5. 数量上，一个 30 词左右的句子通常有 10–20 个条目（含 aspect 和文档级）；不要为了凑数写无关紧要的差别，也不要因为嫌多漏掉 gold 的错。同一句里多个事件的 aspect、多个事件的 modal 强度，性质相同的可以合成一条（"三个将来事件的 modal 强度"）。
6. 一份标注漏掉一个节点、连带影响好几个比较点时：只在"有没有这个节点"那一条里判它 `bad`；其余受连带的条目里把它单独归成一个选择"（没有这个节点）"，status 写 `open`，免得同一个错被算好几次。

`review/items/<doc>.<from>-<to>.json` 是一个 JSON 数组，每个条目：

```json
{
  "sent": 3, "n": 1,
  "topic": "「进口」的来源国",
  "cat": "role",
  "choices": [
    {"label": "进口 :source 日本", "systems": ["gold", "s3/r1"], "status": "bad", "grep": ":source"},
    {"label": "进口 :ARG2 日本", "systems": ["s3/r2", "s3/r3", "s3/r4"], "status": "ok", "grep": ":ARG2"},
    {"label": "水产 :source 日本", "systems": ["s3/r5"], "status": "minor"}
  ],
  "best": "进口 :ARG2 日本",
  "text": "PropBank 进口-01 的 ARG2 是来源（entity arg1 is imported from），日本应是核心论元 ARG2，不该用非论元角色 :source。",
  "fix": {
    "title": "进口来源国：:source → :ARG2",
    "conf": "high",
    "why": "PropBank 进口-01：ARG2 是来源。日本是进口来源，应是核心论元 ARG2。",
    "ops": [{"op": "mod_rel", "s": "s3x15", "r": "source", "t": "s3c2", "r2": "ARG2"}]
  }
}
```

- `sent` 句子号；`n` 在这一句里从 1 开始编号。
- `topic`：这个比较点是什么，十来个字。
- `cat` 只能是：`sense`（义项编号或是否谓词化）、`role`（角色标签）、`concept`（概念、命名实体类型、抽象概念的选择）、`structure`（切分、挂接位置、并列与从属、有没有这个节点）、`attr`（aspect、polarity、mode、refer-*、quant、degree 等属性值）、`doc-temporal`、`doc-modal`、`doc-coref`。
- `choices`：把 `gold` 和 5 个系统分到各个选择里，**6 个名字每个必须出现且只出现一次**。某份标注在这里没有相应内容时，单独给一个选择（"没有标这个节点"）。`label` 要短而具体，用标注里的写法。
- `status`：`ok` 按 guideline 正确；`minor` 可以接受但略差；`bad` 错；`open` 定不了。几种做法都对时都写 `ok`。同一个选择里的标注 status 相同。
- `grep`（尽量写）：一段文字，或几段文字的数组，在这个选择里**每一份**标注的这一句（句子图加文档级标注，原文）里都能原样找到。检查脚本会核对，这是防止把一个系统的标注写到另一个系统名下的主要手段。要求和建议：
  - 必须在一行之内（图是一行一个节点或属性，跨行的"X :role (Y"找不到）。
  - 不能含变量名（各份标注的变量名不同）。`"进口-01"`、`"/ 恢复-02"`、`":ARG2 (s"`（只到变量名的开头）、`":polarity -"` 都可以。
  - 尽量选只有这个选择里的标注才有的文字。`":topic"` 这种每份标注都有的文字能通过检查，但证明不了什么。
  - "没有标"的选择、取值相同只是位置不同的选择（"节点 X 的 aspect 是 state"）没法 grep，不写，改为对着 `mechdiff.py` 的列表核对。
- `best`：最好的选择的 label；都可以或定不了时写 `null`。
- `text`：判断和依据，一到三句中文。写明依据（PropBank 哪个 roleset 的哪个论元、guideline 哪一节、训练数据先例）。`choices` 已经列了谁选了什么，这里不用重复。拿不准就说拿不准。
- `fix`：gold 应该改时写，否则写 `null`。
  - `conf`：`high` 依据明确；`mid` 有依据但存在另一种说得通的读法；`low` 值得商榷（不会进修订版 gold，只提示审阅人）。
  - `conf` 是 `high` 或 `mid` 时，gold 所在选择的 status 必须是 `bad` 或 `minor`。
  - `why` 是给审阅人看的理由，一两句，自成一体。
  - `ops` 是对 gold 的编辑，变量名用 gold 的，角色名不带冒号。修改尽量小：只改这个比较点涉及的东西。
  - 有 `fix` 时 `best` 不能是 gold 所在的选择。
  - 同一处有两种互斥的改法时，选你认为最好的一种。
  - **每个 fix 必须能单独接受**：审阅人是逐条接受或拒绝的。两处修改互相依赖时（例如"引入 conceiver"和"把事件挂到这个 conceiver 下"），合成一个条目、一个 fix。检查脚本对每个 fix 单独在原 gold 上执行一遍，再全部按顺序执行一遍。
  - gold 错了但改法没法用下面的操作表达（例如整句结构要重画）时，`fix` 写 `null`，gold 的 status 照实写 `bad`，在 `text` 里说明应该怎么改。

编辑操作的几个细节（检查脚本不会提示，写错了图会断开）：

- gold 里用反向角色写的边（`:ARG1-of`）在引擎里就存成反向角色：`del_rel`、`mod_rel` 的 `r` 要写 `ARG1-of`，`s` 是写着这条边的那个节点。
- `add_node` 的 `role` 写正向角色。要让新节点带一条反向边，先 `add_node` 挂在别处，或者用 `add_rel` 另加。
- 要在根上面再加一层（新根）：先 `add_node` 把新节点临时挂在旧根下，再 `add_rel` 加上"新节点 → 旧根"的边，`set_root` 换根，最后 `del_rel` 删掉临时那条边。
- 文档级的选择大多没法写 grep（三元组只有变量不同），对着 `mechdiff.py` 的列表核对即可。

编辑操作：

| op | 字段 | 含义 |
|---|---|---|
| `add_node` | `parent, role, var, concept, attrs?, align?` | 在 parent 下加新节点；var 用这一句里没用过的名字（如 `s3z1`）；attrs 如 `{"aspect": "state"}`；align 如 `"17-19"` |
| `del_node` | `var, subtree?` | 删节点（连同它的对齐和文档级三元组）；`"subtree": true` 连同只挂在它下面的子树一起删 |
| `rename` | `var, concept` | 改节点的概念（改义项、改命名实体类型都用它） |
| `add_rel` / `del_rel` | `s, r, t` | 加、删一条边；t 是变量 |
| `mod_rel` | `s, r, t, r2` | 把 s 到 t 的角色 r 改成 r2 |
| `set_attr` / `del_attr` | `var, attr, value` | 设、删属性值（aspect、polarity、quant 等常量）；`del_attr` 可以不带 value |
| `doc_add` / `doc_del` | `kind, triple` | 加、删文档级三元组；kind 是 `temporal`、`modal` 或 `coref`；triple 如 `["author", "full-affirmative", "s1x8"]` |
| `doc_mod` | `kind, triple, to` | 把一条文档级三元组改成另一条 |
| `align` / `del_align` | `var, span` | 改、删对齐 |
| `set_root` | `var` | 换根节点 |

条目文件的例子（只看格式，系统名字不同）：`../../review-round2/review/items/zh-0032.01-06.json`。

## 判断时常见的情况

- 义项：PropBank 有这个词时用它的编号；没有时写 `词-00`。带了某义项没有的论元（例如 `恢复-01` 带 ARG1）是错。
- 核心论元和非论元角色：PropBank 的论元能表达时用 `ARGn`，不要用 `:source`、`:goal`、`:topic` 之类替代。
- 副词性修饰事件用 `:manner`，名词性修饰用 `:mod`。
- aspect：未然事件、事件名词难定，几种合理取值都给 `ok`，不要硬判；状态谓词标 `performance`、明显完成的事件标 `state` 之类才算错。
- 文档级 modal：predictive future（将）是 full strength；引述内容的 conceiver 是说话人；否定的事件是 `full-negative`。
- 命名实体：专名整体作命名实体，类型用 guideline 的类型表。
- 两种做法都合理时都给 `ok`，`best` 写 `null`，不要写 `fix`。只有依据明确时才判 gold 错。

## 写完后的检查（必须做）

```bash
python3 pipeline/items.py check review/items/zh-0005.01-12.json
```

必须到 0 errors。在文件路径后面加 `--weak` 可以列出区分度不够的 grep。`grep` 写成数组时，每一段都要在每份标注里找到。它检查：格式、6 个名字是否各出现一次、每个 `grep` 是否真的在所列标注里、所有 `fix` 能否在 gold 上执行。warning 逐条看一下，有理由的可以留。建议每写完几句就跑一次，不要攒到最后。

`grep` 没法覆盖的归属（"没有标"、结构性的描述），请对着 `mechdiff.py` 的 `⟵` 列表再核一遍，这是上一轮出错最多的地方。

## 小结文件

`review/items/<doc>.<from>-<to>.notes.md`，不超过 25 行，中文，两部分：

- **gold 的问题**：这一段里 gold 反复出现的错误类型，每类一行，带一两个例子（第几句、哪个词）。
- **系统的问题**：各系统（特别是不同设定之间）反复出现的错误类型，每类一行，写明是哪些系统。

## 回复

最后只回几行：条目数、fix 数（high / mid / low 各多少）、检查是否 0 errors、有没有没做完的句子。不要把条目内容贴在回复里。
