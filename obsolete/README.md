# obsolete：不再是现行结果的旧数据（存档）

## `data/annoforge/`：2026 年 10 月 AnnoForge 实验的数据快照

论文（`main.tex`，AnnoForge）用的数据：从实验仓库 sxndqc/SkillParseUMR 抽出的各条件分数、逐句分数、每轮的反思与操作、
每个版本的结构和大小、SOTA 重打分、成本（2026-10-10 至 10-13）。`analysis/annoforge.py` 现在从这里读
（`make` 出 `tables/`、`figures/`，`extract` 也写到这里）；论文已经生成好的表和图不受影响。

## `exp/runs/`：`exp/` 里被后来的结果取代的运行

目录结构和 `exp/runs/` 一样：`obsolete/exp/runs/api/<sub>/<label>/`，文件也一样（回答原文、`.umr`、打分、实际发出的
prompt 和完整对话）。`exp/scripts/report.py` 在“已归档的旧结果”一节里还会读它们作对照。

| 标签 | 是什么 | 为什么归档 |
|---|---|---|
| `claude-opus-5-5` | Claude Opus 5.5（effort medium）用**第一版 prompt**跑的 5 个子实验，zh-0028、zh-0032 | 第一版 prompt 要模型自己写词对齐、没有强调尽量正确和多查资源；现在的 prompt（`make_subexps.py`）不写对齐（由 `lib/autoalign.py` 生成），结果在 `runs/api/<sub>/claude-opus-5-5-v2/`。这里的 `scores.json` 是当时按模型自己的对齐打的分 |
| `gpt-6-astra-medium` | OpenAI gpt-6-astra（reasoning effort medium），现在的 prompt，5 个子实验，zh-0028、zh-0032、en-0008 | GPT 改用 gpt-6.1-sol（`runs/api/<sub>/gpt-6.1-sol-medium/`） |

这些目录的 umrjudge 分数和 `runs/` 里的一样，已按每项检查的召回、精确、F1 重算过（`run.py rejudge`）。
