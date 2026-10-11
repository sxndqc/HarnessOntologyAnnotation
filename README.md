# HarnessOntologyAnnotation

论文 **Can LLMs Build Better Annotators? Self-Improving Harnesses for Ontology-Guided Annotation** 的稿子、数据快照和出表脚本。
原来 SkillParseUMR 里的 B 篇（`intro-B-instruction-rsi.md`、`paper-tex/B-instruction/`）移到了这里，按 harness + 自我改进的思路重写；
旧稿留在 `archive/`。实验代码和完整的实验记录仍在 [sxndqc/SkillParseUMR](https://github.com/sxndqc/SkillParseUMR)。

## 目录

仓库根目录就是 Overleaf 项目：在 Overleaf 里 New Project → Import from GitHub（或上传 zip），主文件 `main.tex`，编译器 pdfLaTeX。

- 根目录：`main.tex`、`references.bib`、`acl.sty`、`acl_natbib.bst`。
- `sections/`：正文各节和附录，`main.tex` 逐个 `\input`。
- `tables/`：表格和正文用的数字宏（`tables/numbers.tex`），由 `analysis/make_tables.py` 生成；不要手改，改数据后重新生成。
- `figures/`：`curve.pdf`、`category.pdf` 由脚本生成；`overview.tex` 是手写的 TikZ 总图。
- `preview/paper.pdf`：当前版本编译出来的 PDF，方便不开 Overleaf 时看。
- `data/`：从 SkillParseUMR 抽出来的小文件（分数、逐句 Smatch、每个版本的 skill 大小、每轮的编辑统计、130 条建议的人工编码）。
  来源和 commit 见 `data/PROVENANCE.md`。
- `analysis/extract_umr.py`：从 SkillParseUMR 的检出里把上面这些抽到 `data/`。
- `analysis/make_tables.py`：从 `data/` 生成 `tables/`、`figures/` 里的表、图和数字宏，并做统计检验。
- `notes/GAPS.md`：**数据空缺清单**，论文里每个红色 `[G…]` / `TBD` 要跑什么、怎么跑、填到哪里。
- `notes/references_verification.md`：参考文献逐条核实的记录（arXiv、ACL Anthology、Crossref、OpenReview）。
- `archive/`：旧的 B 篇（中文引言和 LaTeX 稿）。

## 编译

```bash
python3 analysis/make_tables.py            # 需要 numpy、scipy、matplotlib；数据没变就不用跑
latexmk -pdf main.tex                      # 本地；或者用 Overleaf
```

更新数据：`python3 analysis/extract_umr.py --src ../SkillParseUMR [--bold <bold-curie 分支的检出>]`，再跑 `make_tables.py`，
把新生成的 `tables/`、`figures/` 一起提交（Overleaf 不跑 Python）。

## 实验故事（一句话版）

LLM 能不能自己把一个标注器（harness：每一步的说明、工具、调用链）从几篇 gold 文档里"建"得更好？

1. **在这条单次序贯轨迹中有改善。** 逐篇先测后学（R(n-1) 测第 n 篇，同一篇用种子 R0 做配对对照）：中文 UMR 上没见过的文档 +9.0 F
   （95% CI 5.5–12.5，9 篇里 8 篇变好，Wilcoxon p=0.008）；涨幅集中在非核心角色、抽象谓词的论元、模态、代词属性这些对约定敏感的检查，
   义项、aspect、核心论元变化较小。这不能证明语义能力不变。阶段得分显示多数增益已在 generate 输出中，critique 再加 0.5；单轨迹区间不表示算法重复方差。
2. **对比基线**（G1–G4，待补）：zero-shot prompt、few-shot、只改 guideline 的 earlier work、人设计的流程 harness，同样的 gold、同一个留出集。
3. **它怎么失败**：只增不删（1060 条编辑里 1 条删除），harness 从 11 KB 长到 434 KB，这条轨迹未显示增益随文档数清晰增长；
   在训练文档上能到 84–99 F，但那是拟合，不是泛化；3 个工具提议全被审核拒绝；跟着最新一篇文档改规则，最后出现"只在传记里"这种按体裁的规则。
4. **它想做但不能做的**：130 条越权建议里 78 条指向 gold 本身的不一致（builder 顺带成了 gold 的审校员），27 条要代码，14 条要更多上下文。
5. **一个弱模型组合的失败**：Qwen3.5-9B 自己建自己用，平均 −1.4 F，越往后越差。
6. **别的 benchmark**（G10、G11，进行中）：TimeML（TempEval-3）和 Manifesto 编码，基线已有，学到的 harness 还没测完。

本次 ARR 模拟审稿修订、数据曝光与证据审计说明见 `notes/ARR_REVISION.md`；需要新增实验的结果仍留空。

本论文的[详细新增实验计划](https://github.com/sxndqc/SkillParseUMR/blob/main/docs/experiments-harness-ontology-annotation.md)保存在代码仓库：TimeML 新主实验的标注与对应基线使用 Haiku，反思构建/reviewer 使用 Opus；Manifesto 为可选边界实验。各条件独立运行和归档，未完成的结果不填入论文。
