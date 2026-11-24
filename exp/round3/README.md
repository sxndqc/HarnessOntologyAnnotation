# round3：Claude Sonnet 5.5 的五个设定，训练集审阅，parse skill 反思

先看 `analysis/report.html`（单文件汇报）。所有“gold 应改”“系统错”的判断都出自模型审阅，没有经过人工确认。

## 做了什么

1. **五个设定在测试集上各跑 10 次**（`runs/<设定>/p<措辞>r<次>/`）：4 篇文档（zh-0029、zh-0035、en-0005、en-0006，超过 25 句的截到 25 句），整篇放进一个 prompt。5 种意思相同的指令措辞，每种 2 次。
2. **s3 在 4 篇中文 clean 训练文档上跑 5 次**（zh-0003、zh-0011、zh-0016、zh-0018，共 100 句），按 umr-gold-review skill 逐句审阅（`review/`），得到 1,155 个条目、修订版 gold 和错误类型总结（`analysis/error-patterns.md`）。
3. **三种反思方法各做两轮**，写出 parse skill（`skills/m<方法>-r<轮>.md`），每轮之后在训练集和测试集上各测一次（5 种措辞各 1 次）。

## 设定

| 名字 | guideline | 工具 |
|---|---|---|
| `s0-oneline` | 一句话 | 无 |
| `s1-abridged` | 精简版（修订后） | 无 |
| `s2-guideline-search` | 一句话 | 查完整 guideline（修订后） |
| `s2-propbank-search` | 一句话 | 查 PropBank |
| `s3-full-two-tool` | 一句话 | 两个都有 |
| `s3-full-two-tool+m1-r1` 等 | 一句话，加 parse skill | 两个都有 |

模型是 `claude-sonnet-5-5`，effort medium，通过订阅的 `claude -p` 调用：没有内置工具、不读任何设置和项目文件，两个查询工具由 `mcp_tools.py` 提供。措辞、工具那一句话的三个版本都在 `config.json`。

## 文件

- `config.json`：模型、设定、5 种措辞、文档分组。`OUTPUT_FORMAT.md`：输出格式（各设定相同）。
- `run_claude.py`：运行。`mcp_tools.py`：两个查询工具的 MCP 服务。
- `score.py`：umrjudge 分项和 juːmæʧ，每个设定取各次运行的平均（`analysis/scores.json`）。
- `reflect.py`：整理错误证据（`analysis/evidence/`）、三种反思方法（`skills/*.prompt.md` 是完整的反思请求，`*.answer.md` 是原始回答）。
- `build_report.py`、`report_template.html`、`analysis/report_notes.json`：生成汇报页面。
- `data/input`、`data/gold`：输入和 gold（测试文档是 UMR 2.2 test-gold 的前 25 句；训练文档是 clean 训练数据原文件）。
- `review/`：审阅工作区（条目在 `review/review/items/`，修订版 gold 在 `review/data/gold_revised/`，说明在 `review/review/REVIEWER.md`）。
- `runs-trial/`：工具那一句话的前两个版本的试跑（模型一次都没有查）。

## 重新生成

```bash
pip install -r ../review-round2/requirements.txt
python3 run_claude.py --conds s0-oneline,s1-abridged,s2-guideline-search,s2-propbank-search,s3-full-two-tool --group test
python3 run_claude.py --conds s3-full-two-tool --group train --reps 1
python3 reflect.py evidence --tag "" && python3 reflect.py skill --method 1 --round 1
python3 run_claude.py --conds s3-full-two-tool --group train --reps 1 --skill skills/m1-r1.md --tag m1-r1
python3 score.py && python3 build_report.py
```
