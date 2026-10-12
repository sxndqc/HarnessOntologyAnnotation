# HarnessOntologyAnnotation

论文 **AnnoForge: Bootstrapping Complex Annotation from Guidelines by Recursive Self-Improvement of the Annotation Harness** 的稿子、数据快照和出表脚本（2026-10-12 按统一重做的实验全面重写；之前的版本在 `archive/`）。实验代码和完整的实验记录仍在 [sxndqc/SkillParseUMR](https://github.com/sxndqc/SkillParseUMR)。

## 目录

仓库根目录就是 Overleaf 项目：主文件 `main.tex`，编译器 pdfLaTeX。

- `sections/`：正文（intro、related、method（AnnoForge）、experiments、results、conclusion、limitations）和附录。
- `tables/`、`figures/curves.pdf`、`figures/judge.pdf`、`figures/ops.pdf`、`tables/numbers.tex`（正文用的数字宏）：
  由 `analysis/annoforge.py make` 从 `data/annoforge/` 生成，不要手改。`figures/overview.tex` 是手写的 TikZ 总图。
- `data/annoforge/`：从实验仓库抽出来的小文件（各条件分数、逐句分数、每轮的反思与操作、每个版本的结构和大小、SOTA 重打分、成本）。
- `analysis/annoforge.py`：`extract --src ../SkillParseUMR` 抽数据，`make` 出表、图、宏和统计检验。
- `notes/new_references.md`、`notes/new_references.bib`：这次新增的 46 条参考文献及核实记录（已并入 `references.bib`）；
  `notes/references_verification.md`：之前的核实记录。
- `archive/`：旧版本（v1：单轨迹中文 UMR 的稿子、表、数据和脚本；更早的 B 篇）。

## 编译

```bash
python3 analysis/annoforge.py extract --src ../SkillParseUMR   # 需要实验仓库的检出；数据没变就不用跑
python3 analysis/annoforge.py make                             # numpy、scipy、matplotlib
latexmk -pdf main.tex
```

## 实验（一句话版）

AnnoForge：只给 guideline 和少量例子，LLM 不经微调自己搭出标注器。Sonnet 只读 guideline 写出三步的种子 harness（generate、critique、finalize），
然后在 10 组、每组 5 句的 gold 上做递归自我改进（改 skill、加规则步骤、自己写工具读 PropBank），Haiku 标注。
在 UMR 共享任务的中英文测试文档上，H10 比种子高 6.1 / 11.3 AnCast++ F，官方 juːmæʧ 达到 42.9 / 38.0，超过共享任务最好的微调系统
（同样文档上 38.8 / 27.3）；TimeML 上学会了"哪些事件该连"，但没学会时间关系本身。实验代码、全部版本和记录在
[sxndqc/SkillParseUMR](https://github.com/sxndqc/SkillParseUMR) 的 `experiment/annoforge/`（中文说明见那里的 README）。

GPT-6.1-sol：种子 2x2 全部完成，H10 迁移到 GPT/GPT 完成了中文和英文两篇；中英文的 GPT guideline baseline 和其余迁移因 API 余额没跑，论文里标 n/a（补跑方法见实验仓库 README）。
