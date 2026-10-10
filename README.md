# HarnessOntologyAnnotation

论文 **Can LLMs Build Better Annotators? Self-Improving Harnesses for Ontology-Guided Annotation** 的稿子、数据快照和出表脚本。
原来 SkillParseUMR 里的 B 篇（`intro-B-instruction-rsi.md`、`paper-tex/B-instruction/`）移到了这里，按 harness + 自我改进的思路重写；
旧稿留在 `archive/`。实验代码和完整的实验记录仍在 [sxndqc/SkillParseUMR](https://github.com/sxndqc/SkillParseUMR)。

## 目录

- `paper/`：ACL 模板的 LaTeX。`main.tex` 引入 `sections/*.tex`；`tables/` 和 `figures/curve.pdf`、`figures/category.pdf`
  由脚本生成，`figures/overview.tex` 是手写的 TikZ 总图。`main.pdf` 是当前版本编译出来的。
- `data/`：从 SkillParseUMR 抽出来的小文件（分数、逐句 Smatch、每个版本的 skill 大小、每轮的编辑统计、130 条建议的人工编码）。
  来源和 commit 见 `data/PROVENANCE.md`。
- `analysis/extract_umr.py`：从 SkillParseUMR 的检出里把上面这些抽到 `data/`。
- `analysis/make_tables.py`：从 `data/` 生成表格、图和正文用的数字宏（`paper/tables/numbers.tex`），并做统计检验。
- `notes/GAPS.md`：**数据空缺清单**，论文里每个红色 `[G…]` / `TBD` 要跑什么、怎么跑、填到哪里。
- `notes/references_verification.md`：参考文献逐条核实的记录（arXiv、ACL Anthology、Crossref、OpenReview）。
- `archive/`：旧的 B 篇（中文引言和 LaTeX 稿）。

## 编译

```bash
python3 analysis/make_tables.py            # 需要 numpy、scipy、matplotlib
cd paper && latexmk -pdf main.tex          # 或者把 paper/ 上传到 Overleaf（pdfLaTeX + BibTeX）
```

更新数据：`python3 analysis/extract_umr.py --src ../SkillParseUMR [--bold <bold-curie 分支的检出>]`，再跑 `make_tables.py`。

## 实验故事（一句话版）

LLM 能不能自己把一个标注器（harness：每一步的说明、工具、调用链）从几篇 gold 文档里"建"得更好？

1. **能，但学到的是约定，不是能力。** 逐篇先测后学（R(n-1) 测第 n 篇，同一篇用种子 R0 做配对对照）：中文 UMR 上没见过的文档 +9.0 F
   （95% CI 5.5–12.5，9 篇里 8 篇变好，Wilcoxon p=0.008）；涨的是非核心角色、抽象谓词的论元、模态、代词属性这些"写法约定"，
   义项、aspect、核心论元不动。几乎全部来自 generate 的说明，critique 只加 0.5。
2. **对比基线**（G1–G4，待补）：zero-shot prompt、few-shot、只改 guideline 的 earlier work、人设计的流程 harness，同样的 gold、同一个留出集。
3. **它怎么失败**：只增不删（1060 条编辑里 1 条删除），harness 从 11 KB 长到 434 KB，增益却不随文档数增长；
   在训练文档上能到 84–99 F，但那是拟合，不是泛化；3 个工具提议全被审核拒绝；跟着最新一篇文档改规则，最后出现"只在传记里"这种按体裁的规则。
4. **它想做但不能做的**：130 条越权建议里 78 条指向 gold 本身的不一致（builder 顺带成了 gold 的审校员），27 条要代码，14 条要更多上下文。
5. **模型要够强**：Qwen3.5-9B 自己建自己用，平均 −1.4 F，越往后越差。
6. **别的 benchmark**（G10、G11，进行中）：TimeML（TempEval-3）和 Manifesto 编码，基线已有，学到的 harness 还没测完。
