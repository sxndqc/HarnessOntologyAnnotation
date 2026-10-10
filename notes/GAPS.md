# 数据空缺清单

论文里红色的 `[...]` 和表格里的红色 `TBD` 都是这里的条目。编号和论文里的 `G1`…`G13`、`G-var` 一一对应。
命令里的 `run.sh` 都指 SkillParseUMR 里对应实验目录的脚本；Sonnet 解析、Opus 反思（默认值）。

数字怎么进论文：跑完的结果放进 SkillParseUMR 对应实验目录，`python analysis/extract_umr.py --src <SkillParseUMR>` 重新抽数据到 `data/`，
`python analysis/make_tables.py` 重新生成 `tables/*.tex`、`figures/*.pdf` 和正文用的数字宏 `tables/numbers.tex`。
正文里的数字都是宏（`\gainF` 之类），数据变了不用手改正文。新类型的实验（G1–G4、G9）要在 `make_tables.py` 里加一个读数和出表的函数，
现在这几张表（`tab:heldout`、`tab:ablation`）是手写在 `sections/results.tex` 里的，填好后也可以直接手改。

## 优先级

1. **G1–G4（主对比）**：没有它们，摘要和引言里"比 few-shot、比只改 guideline、比人设计的流程更好"这句话不能写。
2. **G10、G11（另外两个 benchmark）**：现有的半成品数字有风险，见下。
3. **G9（消融）**，尤其是"不做归因"和"整篇重写"两行：这是我们和 earlier work 区别的直接证据。
4. **G-var（方差）**：审稿人一定会问，成本低。
5. 其余。

---

## 表 1 里的 TBD（序列评测）

- **0011 的种子**：`experiment/rsi-zh-critique/run.sh train R0 chinese_umr-0011`，之后 `run.sh score`。补上后配对文档从 9 篇变 10 篇。
- **0008–0011 的 zero-shot prompt**：rsi-zh2 的 baseline `generate-guidelines`（每句一次调用，只给语言、UMR、guideline 链接），
  现在只跑了 0001–0007。对 0008–0011 用同一个 skill 跑（rsi-zh2 的 `run.sh test-generate`，或 `scripts/run_experiment.py`
  指向 `experiment/rsi-zh2/baselines/umr-generate-guidelines/registry.yaml`）。结果放进 `data/umr/tree_scores.json` 的
  `test.generate-guidelines.docs`（或改 `make_tables.py` 读新文件）。

## G1 留出集上的主结果（表 2 `tab:heldout`）

- 留出集：从没给任何 builder 看过的 20 篇，0012–0018、0021–0024、0027–0035，共 297 句。
  （注意：qwen-zh 用 0008–0035 做过 Qwen 的训练序列，但那是另一个 harness、另一个模型，不影响 Sonnet/Opus 这条线；
  rsi-jev2 拿 0027–0029 当过 dev，也是另一个 harness。如果想更干净，可以只用 0012–0026 的 15 篇，论文里写清楚。）
- 要跑：种子 R0，以及学到的 H1=R13、H4=R43、H10=R103（可加 H7=R73），在 20 篇上各一遍。
  `experiment/rsi-zh-critique/run.sh test R13 chinese_umr-0012 chinese_umr-0013 ...`（`test` 不改 skill，可以和别的并行）。
- 这同时就是 **G5**（固定测试集上的学习曲线：更多文档到底有没有用）。

## G2 Few-shot 基线

- 种子 harness H0，`generate` 里加入训练文档（0001–0004）中与输入句最相似的 k 句的 gold 图（字符级 TF-IDF），k=10 和 30；
  `document` 可加 gold 的文档级关系做例子。
- 现成的模板：manifesto 的 `scripts/baseline_manifesto.py --mode few`（bold-curie 分支），TimeML 的 `scripts/baseline_timeml.py --mode few`。
  UMR 还没有这个脚本，要写。
- 在留出集上测；同时最好在 0005 上测一次，填进附录 `tab:matched` 的 Few-shot 列。

## G3 只改 guideline 的基线（earlier work 的对应物）

- 同一个 builder（Opus）、同样的 gold（0001–0004，每篇三轮），但 harness 只有一个 guideline prompt（每句一次调用），
  每轮：找最常见的错误模式 → 写一条原则 → 整篇重写 guideline → 训练文档上变好才保留（照 Kim et al. 2026 的流程）。
- 需要新写一个脚本（可以从 `rsi/rsi_critique.py` 改：把 plan 换成"整篇重写"，加一个保留判断）。
- 这是论文和 earlier work 区别的核心实证，优先级很高。

## G4 人设计的流程 harness（umr-tree）同预算对比

- rsi-zh2 的 R42 只有 10 轮（0003、0004 各两轮），我们的 H4 有 12 轮。补 `experiment/rsi-zh2/run.sh round chinese_umr-0004 3` 得到 R43 最公平；
  或者拿我们的 R42 对它的 R42。
- 在留出集上测 R43（或 R42）。
- 附录 `tab:matched` 里我们在 0006、0007 上的 TBD：`experiment/rsi-zh-critique/run.sh test R43 chinese_umr-0006 chinese_umr-0007`
  （R43 没见过 0006、0007；后来的版本见过，但 R43 本身冻结了）。

## G5、G6 增长与整合（`sec:growth`）

- G5 = G1 的学习曲线部分（H1、H4、H7、H10 在同一留出集上）。
- G6 整合：让 Opus 在大小预算下（比如压到 50% 和 25% 的 KB）重写 H10 的三个 skill，规则不变，只合并、删除重复和矛盾；
  在留出集上和 H10 比。需要一个新的小脚本。

## G7 准入：审核是在挡坏东西，还是挡住了好东西

- 同样的 0001–0005，审核关掉（只做机器检查），其余不变；或者审核保留但被拒的提议下一轮带着审核意见重提。
- 比较：被接受的工具数、序列增益、留出集增益。TimeML/manifesto 的分支（无审核）已经在每轮加或改工具和规则，可以作为旁证，但任务不同。

## G8 builder 和 annotator 分开

- Opus 建的 harness（H4、H10）给弱的解析模型用（Qwen3.5-27B、DeepSeek 开 thinking、或 Haiku），在留出集上测；
- 弱的 builder（Qwen-27B 或 DeepSeek）+ Sonnet 解析，序列跑 0001–0005。
- Qwen-27B 的序列实验（`experiment/qwen27-zh`）只跑到 0001，表 `tab:models` 里那一行要它补完。
- DeepSeek 那几个数是 thinking 关着跑的（种子开 thinking 49.1、关 35.9），最好开 thinking 重跑种子和 R42。论文里要写清 DeepSeek 的具体型号
  （Handoff 里是 `deepseek-flash`，即 V4.1 Flash）。

## G9 消融（表 `tab:ablation`）

都在 0001–0005 上做（序列增益看 0002–0005），再在留出集上测最后的版本：

| 行 | 怎么改 |
|---|---|
| no attribution (one list) | find 照旧，但 plan 拿到的问题不按 skill / 类别分组，也不给"该改哪个 skill"这一栏 |
| whole-skill rewrites | plan 不出 modify/add/delete，而是每个 skill 输出整篇新文本 |
| generate only | 链上去掉 critique，RSI 只改 generate 和 document |
| no reviewer | 同 G7 |
| + test edits on held-in docs | 每条编辑在之前的训练文档上重跑，不降才保留（rsi-jev2 的 `trials` 是现成的实现，可以照搬到这个 harness） |
| + consolidation | 同 G6，每篇文档后做一次 |
| other document orders | 两个随机顺序重跑 0001–0005 |

## G10 TimeML（附录 `tab:timeml`，bold-curie 分支 `experiment/timeml`）

- 现在有：测试集上的 R0 和 zero-shot，2013 年系统的重算分数；训练序列做到第 4 篇。
- 缺：学到的 harness 在测试集上的分数（`test/R-final` 这一行）、ten-shot 基线（`test/B-few`）、训练文档上 seed / zero-shot 的配对对照
  （分支最后一个提交说正在跑）。把 key 写成 `test/R-final`、`test/B-few` 放进 `data/other/timeml_scores.json`，表会自动填上。
- **风险**：测试集上种子 R0 低于 zero-shot（event F1 74.5 vs 80.7，timex strict 81.1 vs 85.4），序列曲线也很吵（TLINK 35.3 → 41.0 → 32.9 → 13.6）。
  如果学到的 harness 追不上 zero-shot，论文这一节要改写成"harness 结构本身在这个任务上不占优"的诚实结果。

## G11 Manifesto（附录 `tab:manifesto`，bold-curie 分支 `experiment/manifesto`）

- 现在有：测试集 800 句上的 majority、TF-IDF（同样 1200 句 / 3.3 万句）、ManifestoBERTa（见过这些句子，只作参考）、zero-shot、few-shot（30 句检索）、种子 R0。
- 缺：学到的 harness（R3、R5、R7 等，分支上正在重跑）。key 写成 `test/R-final`。
- **风险**：种子 63.8 < zero-shot 65.0 < few-shot 67.8；训练序列 70.8 / 72.5 / 64.2 / 60.8 / 72.5 / 69.2 / 73.3，看不出上升。
  另外这里的"文档"是随机抽的 120 句一批（数据集没有文档 id），论文附录已经写明。

## G12 成本

- H1、H4、H10 每句的成本和延迟（API 价；缓存命中率）；每轮、每篇的 builder 成本；写种子花了多少人时。
- critique 实验是用订阅（claude-sdk）跑的，没有现成账单；可以用 `.previous_answers/` 或日志里的 usage 估算，或用 API key 抽几篇重跑。
- 论文里的 "$0.08 每句"来自 `experiment/rsi-zh-critique/README.md`（种子版本、API 价），需要确认。

## G13 建议编码的一致性

- `data/umr/suggestions_coded.csv` 里 130 条建议是我（写稿时）一个人按 gold / rule_code / context / evaluator / other 编的码。
  请再找一个人独立编一遍，报 Cohen's kappa；有分歧的条目改码，`make_tables.py` 会自动更新论文里的数字。

## G14 跨模型 generate / critique，按整篇文档反思，每轮压缩（SkillParseUMR `experiment/rsi-zh-cross`）

- 两组：gpt-6.1-sol generate + Sonnet 5.5 critique（`gpt-sonnet`），Sonnet 5.5 generate + gpt-6.1-sol critique（`sonnet-gpt`）；
  document 跟 generate 同一个模型，builder 都是 Opus。0001–0010 顺序跑，每篇**两轮**（R11 → R12 → R21 …，论文是三轮），
  每篇先跑 R0 配对对照，最后一轮之后再测 after。每组约 4650 次 skill 调用（GPT 两组合计 4527 次，反思每轮 4～8 次）。
- 反思（`rsi/rsi_compact.py`）按整篇文档做，不再每句调一次 find：整篇所有句子的全部错误放在一起（judge 单元、两边的图、
  critique 的改动）→ 先总结成模式 → 再提建议（generate 文本、critique 常见错误、带关键词的例子、最多一个工具、最多一个新 skill，
  新 skill 用链上前一步的模型）→ 改 skill，工具和新 skill 过机器检查和审核（被拒可修改一次再审）→ 每轮压缩 generate 和 critique
  （合并共性、删细节、细节挪进例子）。例子用 `search_examples` 按关键词取（关键词出现在句子里就返回）。
- 对应论文：§5.3（换一个模型做检查是否比同模型的 +0.5 F 有用）、§5.5 / G6（压缩能否挡住只增不删、增益是否随文档数增长）、
  §5.4 / G7（修改一次后有没有工具能进来）、G8 的一部分（标注和检查用不同模型）。
- 状态：代码和测试已就绪；OpenAI 账户没有额度（429 `credit_balance_exhausted`），充值后按 README 跑。
  结果在 `experiment/rsi-zh-cross/scores.md`；进论文要在 `analysis/extract_umr.py`、`make_tables.py` 里加读数和表。

## G-var 方差

- 解析方差：同一个版本（R0 和 H4）在 3 篇文档上用新缓存各跑两次（Qwen 那边两次种子平均差 2.3 F，Sonnet 还没有）。
- 建造方差：0001–0003 换一个顺序或重跑一遍（缓存要换），看 H3 的增益差多少。

---

## 写作上要补或核实的

- `experiments.tex`："cleaned version of the gold"——Chun & Xue 的清理出自哪篇文章（或者写成私下交流 / 数据版本号）。
- `limitations.tex`：中文 UMR 的 gold 是否已经公开（决定预训练污染那句怎么写）。
- `chun2024pipeline` 的标题已按 ACL Anthology 改为 "Uniform Meaning Representation Parsing as a Pipelined Approach"（TextGraphs-17）；
  旧 bib 里的标题不对。如果 cleanup 其实出自别处，引用要换。
- 模型设置：正文写的是 "adaptive thinking at default effort"（Handoff：Sonnet high、Opus medium，claude-sdk 后端），请确认 critique 实验确实如此。
- "procedural harness ... dozens of calls per sentence"、成本约 $0.7/句：来自旧稿和 A 篇的说法，正文现在只写了 dozens，没写钱数。
- `anon2026orchestration` 是 A 篇（Decision Orchestration），匿名引用；如果 A 篇不投或换名字，要改。
- 方法里说 builder 每轮"最多一个工具、一个步骤"，critique 实验是每轮都允许提；refine 变体是三篇文档一次（附录没写细，需要的话补）。
- 人工改过一次规则（R13 起补括号），正文脚注和 Limitations 都写了。
