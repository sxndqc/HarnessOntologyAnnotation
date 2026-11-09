# exp：整篇文档一次标 UMR（guideline 与资源的对照）

SkillParseUMR 的 skill 执行结构（`registry.yaml` + skill 目录里的 `skill.md`）的最简单版本：每个子实验一个 registry、
一个 skill（`annotate`），**输入是整篇文档，一行一句**，**输出是每句的 PENMAN 图和对齐，最后一张整篇文档的文档级关系图**
（时间、模态、共指）。输出转成标准 `.umr` 后，用 umrjudge（judges）逐项评分，再算 AnCast++、juːmæʧ 和 Smatch。

## 子实验

| 子实验 | 内容 | API：工具 | chat：附件 |
|---|---|---|---|
| `s1-abridged` | 第一步：缩略版 guideline | 无 | 无 |
| `s1-full` | 第一步：完整 guideline | 无 | `guidelines/umr_guidelines.md`（36.6 万字符，作为文件上传） |
| `s2-search` | 第二步：缩略版 + guideline 搜索 | `search_guidelines`（搜完整 guideline） | `guidelines/umr_guidelines.md` |
| `s2-propbank` | 第二步：缩略版 + PropBank | `propbank_lookup` | `chat/s2-propbank/attachments/<doc>.propbank.md` |
| `s2-gold` | 第二步：缩略版 + gold 数据（shared task 训练数据） | `search_annotations` | `chat/s2-gold/attachments/<doc>.gold.md` |

三种方法：

1. **直接调 API**（`api/<sub>/`）：`run.py api` 用 Messages API 跑 registry，工具在本地执行。
2. **chat 界面**（`chat/<sub>/`）：`chat/<sub>/prompts/<doc>.md` 是生成好的 prompt，复制到 chat 窗口；回答存成
   `chat/<sub>/answers/<doc>.txt`，再用 `run.py chat-score` 打分。chat 里没有工具，第二步的资源换成附件：
   搜索条件上传完整 guideline；PropBank 条件上传这篇文档每个词在 PropBank 里的全部条目（预先查好）；
   gold 条件上传每句最相似的训练句子（用 `search_annotations` 按每句的实词预先查好，每句 3 条、每篇最多 60 条）。
3. **Codex / Claude Code 的 harness**（`harness/<sub>/`）：留空，见 `harness/README.md`。

## 设定（和 DMR 2026 UMR parsing shared task 一致）

- **测试数据**：shared task 的官方测试集（UMR 2.2，http://hdl.handle.net/11234/1-6132，Štěpánek et al. 2026，
  "First Shared Task on UMR Parsing"）。默认跑中文和英文的**全部**测试文件：中文 15 个文件 236 句（zh-0021..0036），
  英文 5 个文件 195 句（en-0000 是 PUD，en-0005..0008）；`--langs all` 加上 cs、la、it、arp、nv（共 30 个文件 1,019 句）。
  不再用 AnnoForge 的子集和 newdata 的 gold。
- **输入**：官方 blind 输入 `test-blind/<file>.txt` 原样使用：一行一句、空格分词，句子和 token 都不改
  （shared task 要求输出保持同样的切分和 token）。给模型看的每一行是 `句号<TAB>tokens`。
- **gold 和打分**：官方 `test-gold/<file>.umr`。
  - **juːmæʧ**（主指标）：ufal/umrtools `compare_umr.pl`（`perl compare_umr.pl GOLD gold.umr SYS pred.umr --tsv`）；
    一种语言的分数是把该语言所有文件的 correct / gold / predicted 计数加起来再算 F1（umrtools `micro_average.pl` 的做法）。
  - **Smatch**：snowblink14/smatch（`pip install smatch`），只比句子图，同样按语言把计数加总。
  - **格式检查**：umrtools `validate.py --level 2`，结果记在每个文件的 `valid` 里。官方 gold 自己在 level 2 下也有
    forward reference 和 cycle 报错，比赛提交系统用的具体放宽设置没有公开，所以这里只记录、不把不通过的文件记 0 分；
    预测的图都重新排版过，不会有 forward reference。
  - 没交（没跑完）的文件按空输出计入该语言的总分，表里写明 `files` 是几/几。
  - **核对**：`python3 exp/run.py verify-st` 用同一套打分重算两支参赛队伍公开的系统输出（UMR 2.2 `system-outputs/`），
    和概述论文的表对照（`runs/shared-task/verify.md`）：

    | 系统 | 语言 | juːmæʧ（这里） | 论文表 2 | Smatch（这里） | 论文表 5 |
    |---|---|---|---|---|---|
    | Orange | zh | 36.34 | 36.51 | 52.08 | 51.94 |
    | Orange | en | 22.19 | 22.19 | 46.48 | 46.25 |
    | Sema | zh | 25.78 | 25.85 | 43.64 | 43.63 |
    | Sema | en | 18.71 | 19.19 | 41.57 | 41.69 |

    Smatch 差 0.2 以内（Smatch 本身有随机性）；juːmæʧ 差 0.5 以内。论文说比赛时对每个文件设置了"gold 里没标的关系不扣分"，
    具体配置没公开（试过"排除 gold 文件里没有的关系"，也对不齐），所以这里用公开的默认命令。要拿完全官方的数字，
    可以把输出交到比赛的提交网站（https://ufal.mff.cuni.cz/umr-parsing/submission，赛后仍然开放、同样的评测）。
  - AnCast++ 和 umrjudge 也照算（对 `lib/umrdoc.py` 读写一遍的官方 gold），只作补充，不是 shared task 的指标；
    en-0000（PUD，没有文档级标注）AnCast 算不了。
  - 自检：把官方 gold 按输出格式写成"回答"再解析、打分，juːmæʧ 99.5–100、Smatch 99.3–100（zh-0022 的 gold
    有一句的变量用错了句号，被改名）。
- **资源**：
  - 缩略版 guideline（`guidelines/umr_guidelines_abridged.md`，1.4 万字符）：这次写的，从完整 guideline 压缩，覆盖中英文
    Stage 1 标注需要的概念、角色、属性、文档级三种关系和对齐；完整版里的旧写法（`AUTH`、`DCT`、`FullAff`、`:modstr`）
    一律换成发布数据的写法（`author`、`document-creation-time`、`full-affirmative`、`:modal-strength`）。
    要换成别的缩略版，替换这个文件即可。
  - 完整 guideline（`guidelines/umr_guidelines.md`）：umr4nlp/umr-guidelines `guidelines.md`，sha256 f60deebf…，和网页 repo 同一份。
  - PropBank：网页 repo（ai-native-annotator/ai-native-annotator.github.io）`data/skillparse/resources/propbank/zh.json`、`en.json`
    （每个 roleset 带角色和全部例句），从同级目录的检出读取（或设 `SP_RESOURCES`）。
  - gold 数据：shared task 规定不能用之前的 UMR 发布版（里面有测试数据），只能用比赛给的训练数据，所以 `search_annotations`
    读 UMR 2.2 的 `training-clean` 和 `training-dirty`（中文 1,992 句、英文 30,052 句）；和任何测试句子原文相同的句子都不返回
    （英文训练数据里有 37 句和 en-0006、en-0008 相同）。设 `GOLD_SOURCE=web` 则改用网页 repo 的 `gold/<lang>/gold.json`。
  - 工具代码 `tools/search.py`、`tools/propbank.py` 拷自网页 repo 的 `web_tools/`，只改了读文件的方式和 gold 的来源。
- **输出格式**（每个 `skill.md` 的 Output format 一节）：每句 `# ::snt N`、`# sentence level graph:`、`# alignment:`；
  最后一次 `# document level relations:`，一张 `(d / document :temporal (...) :modal (...) :coref (...))`。
  对齐是必须的：juːmæʧ 靠对齐匹配节点。`lib/umrdoc.py` 把回答写成 shared task 的文件格式（每句四块：tokens、句子图、对齐、
  文档级图），每条文档级关系放进它提到的最后一句的文档级图，`(root :modal author)` 放进每句有模态关系的句子；
  旧写法自动换成发布写法，不带 `s<N>` 前缀的变量改名，括号不配对的修复，问题记在 `<doc>.trace.json` 的 `parse.problems`。
- **API**：默认 `claude-opus-5-5`，adaptive thinking，effort `high`，流式，`max_tokens` 128000；`skill.md` 在 `## Input`
  处切开，前面（说明 + guideline）是 system，带缓存断点；工具循环用自动缓存。默认不开服务端拒答回退，每个回答都出自指定的模型（拒答记为
  `stop_reason: refusal`）；设 `UMR_FALLBACKS=default` 才开（`fallbacks: "default"`），API 不接受时自动去掉。每个回答按完整请求存在 `.cache/answers/`（不进 git），重跑只问变了的部分。key 读 `UMR_MODEL_KEY`。

## 运行

```bash
pip install anthropic penman pyyaml smatch ancast regex
bash exp/data/fetch_umr22.sh      # UMR 2.2（官方测试数据和 gold）→ exp/.cache/umr22，umrtools → exp/.cache/umrtools
python3 exp/run.py verify-st      # 先核对打分：重算两支参赛队伍的输出
```

直接调 API（全部五个子实验，然后出总表 `results.md`）：

```bash
bash exp/run_api.sh                       # 默认 claude-opus-5-5、effort high
```

```bash
python3 exp/run.py api s1-abridged --model claude-sonnet-5-5 --docs zh-0032   # 单个子实验、单篇（总分里其余文件按空输出计）
```

chat：prompt 已经生成好（`chat/<sub>/prompts/<doc>.md`），改了 skill 或 guideline 之后重新生成：

```bash
python3 exp/run.py chat-prompts s1-abridged
```

在 chat 窗口里粘贴 `prompts/<doc>.md` 的全文；有附件的子实验同时上传表里列的文件。回答太长被截断时让它继续，
把各段原样接起来存成 `chat/<sub>/answers/<doc>.txt`（前后多出的说明文字没关系，代码块标记也会被去掉），然后：

```bash
python3 exp/run.py chat-score s1-abridged --label claude-ai-opus     # → runs/chat/s1-abridged/claude-ai-opus/
python3 exp/run.py table
```

## 文件

- `api/<sub>/registry.yaml`、`api/<sub>/annotate/skill.md`；`chat/<sub>/` 同样两个文件，加 `prompts/`、`attachments/`、`answers/`。
  这十个子实验由 `scripts/make_subexps.py` 生成，改 skill 时改这个脚本再运行，两种方法保持一致。
- `lib/registry.py`：registry 的最小子集（SkillParseUMR `skillsets/REGISTRY.md` 的 waves / skills / dispatcher；一波、
  没有 for_each，整篇文档一个 episode；skill 多两个键：`guideline` 填进 `{guideline}`，`tools` 列出可用工具）。
- `lib/llm.py`：Messages API 调用和工具循环；`lib/umrdoc.py`：读 gold、生成输入、解析回答；`lib/score.py`：四种打分。
- `tools/`：`search_guidelines`、`propbank_lookup`、`search_annotations`。
- `run.py`：命令行；`run_api.sh`：API 全部跑完；`results.md`：总表（`run.py table` 生成）。
- `data/docs.json`：测试文件列表（30 个文件，语言、句数、token 数）；`data/fetch_umr22.sh`：下载 UMR 2.2 和 umrtools。
  UMR 2.2 不进 git（中文 CC BY-NC-ND 4.0 等，各语言许可证见包里的 README.txt）；chat 的 prompt 里有测试句子的原文。
- `runs/shared-task/{orange,sema}/`：`verify-st` 的结果；`runs/<method>/<sub>/<label>/`：`<doc>.raw.txt`（回答原文）、`<doc>.umr`（打分用）、`<doc>.trace.json`（解析问题、用量、
  工具调用）、`scores.json`、`scores.md`。
