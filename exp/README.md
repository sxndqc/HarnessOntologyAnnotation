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
| `s2-gold` | 第二步：缩略版 + gold 数据 | `search_annotations` | `chat/s2-gold/attachments/<doc>.gold.md` |

三种方法：

1. **直接调 API**（`api/<sub>/`）：`run.py api` 用 Messages API 跑 registry，工具在本地执行。
2. **chat 界面**（`chat/<sub>/`）：`chat/<sub>/prompts/<doc>.md` 是生成好的 prompt，复制到 chat 窗口；回答存成
   `chat/<sub>/answers/<doc>.txt`，再用 `run.py chat-score` 打分。chat 里没有工具，第二步的资源换成附件：
   搜索条件上传完整 guideline；PropBank 条件上传这篇文档每个词在 PropBank 里的全部条目（预先查好）；
   gold 条件上传每句最相似的 gold 句子（用 `search_annotations` 按每句的实词预先查好，每句 3 条、每篇最多 60 条）。
3. **Codex / Claude Code 的 harness**（`harness/<sub>/`）：留空，见 `harness/README.md`。

## 设定

- **数据**：和 AnnoForge 一样的测试文档（SkillParseUMR `experiment/annoforge/data/splits.json`，种子 20261012）：
  中文 7 篇 99 句（chinese_umr-0023 0027 0028 0030 0031 0032 0035），英文 4 篇 95 句（english_umr-0005..0008；
  0005 和 0007 是同一篇文本的两份标注）。gold 是 SkillParseUMR `newdata/` 的拷贝（`data/gold/`），输入用 gold 的 `Words:` 分词。
- **缩略版 guideline**（`guidelines/umr_guidelines_abridged.md`，1.4 万字符）：这次写的，从完整 guideline 压缩，覆盖中英文
  Stage 1 标注需要的概念、角色、属性、文档级三种关系和对齐；完整版里的旧写法（`AUTH`、`DCT`、`FullAff`、`:modstr`）
  一律换成 UMR 发布数据的写法（`author`、`document-creation-time`、`full-affirmative`、`:modal-strength`）。
  要换成别的缩略版，替换这个文件即可（所有用缩略版的子实验都读它）。
- **完整 guideline**（`guidelines/umr_guidelines.md`）：umr4nlp/umr-guidelines `guidelines.md`，sha256 f60deebf…，
  和网页 repo、AnnoForge 用的是同一份。
- **PropBank 和 gold**：网页 repo（ai-native-annotator/ai-native-annotator.github.io）`data/skillparse/resources/` 里的版本：
  `propbank/zh.json`、`en.json`（每个 roleset 带角色和全部例句），`gold/zh/gold.json`（2,278 句）、`gold/en/gold.json`（31,147 句）。
  默认从同级目录的检出读取，或设 `SP_RESOURCES`。工具代码 `tools/search.py`、`tools/propbank.py` 拷自网页 repo 的
  `web_tools/`，只改了读文件的方式。`search_annotations` 不返回任何测试文档的句子（按文档名和句子原文排除）。
- **输出格式**（每个 `skill.md` 的 Output format 一节）：每句 `# ::snt N`、`# sentence level graph:`、`# alignment:`；
  最后一次 `# document level relations:`，一张 `(d / document :temporal (...) :modal (...) :coref (...))`。
  对齐是必须的：juːmæʧ 靠对齐匹配节点。`lib/umrdoc.py` 把每条文档级关系放进它提到的最后一句的文档级图
  （发布数据就是这样写的；`(root :modal author)` 放进每句有模态关系的句子），旧写法自动换成发布写法，
  变量名不带 `s<N>` 前缀的改名，括号不配对的修复，问题记在 `<doc>.trace.json` 的 `parse.problems`。
- **API**：默认 `claude-opus-5-5`，adaptive thinking，effort `high`，流式，`max_tokens` 128000；`skill.md` 在 `## Input`
  处切开，前面（说明 + guideline）是 system，带缓存断点，所以同一子实验的 11 篇文档只写一次缓存；工具循环用自动缓存。
  开了服务端拒答回退（`fallbacks: "default"`），API 不接受这个参数时自动去掉。每个回答按完整请求存在 `.cache/answers/`
  （不进 git），重跑只问变了的部分。key 读 `UMR_MODEL_KEY`（和 SkillParseUMR 一样）。
- **打分**（`lib/score.py`，对象都是 `lib/umrdoc.py` 写出的 gold 和预测）：
  - AnCast++（`pip install ancast`）：句子图 P/R/F，Modal、Temporal、Coref、Comprehensive，按 Chun & Xue 的清理
    （句子图里的 `:modal-strength` 移到文档级），和 AnnoForge 的 `af/score.py` 一样；文档平均。
  - juːmæʧ（ufal/umrtools `compare_umr.pl`，需要 perl，放在 `.cache/umrtools`）：对 newdata 的 gold 算，
    **不是**共享任务官方测试 gold 上的分数（官方 gold 不在 git 里）。句子合计。
  - Smatch（`pip install smatch`）：只比句子图，句子合计。
  - umrjudge（`judges/umrjudge.py`、`umrjudge.yaml`，拷自 SkillParseUMR `judges/`）：逐项分数，表里的 judge 是各项的平均，
    每个运行目录的 `scores.md` 有逐项表。
  - 自检：gold 和自己比，AnCast++、Smatch 都是 100；把 gold 按输出格式写成"回答"再解析，分数也是 100。

## 运行

```bash
pip install anthropic penman pyyaml smatch ancast
git clone --depth 1 https://github.com/ufal/umrtools exp/.cache/umrtools     # juːmæʧ
```

直接调 API（全部五个子实验，然后出总表 `results.md`）：

```bash
bash exp/run_api.sh                       # 默认 claude-opus-5-5、effort high
```

```bash
python3 exp/run.py api s1-abridged --model claude-sonnet-5-5 --docs chinese_umr-0032   # 单个子实验、单篇
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
- `runs/<method>/<sub>/<label>/`：`<doc>.raw.txt`（回答原文）、`<doc>.umr`（打分用）、`<doc>.trace.json`（解析问题、用量、
  工具调用）、`scores.json`、`scores.md`。
