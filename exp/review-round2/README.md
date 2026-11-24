# review-round2：GPT-6.1-sol 四个设定的输出、逐句审阅和修订版 gold

48 篇文档、7 种语言（中文 33、英语 5、捷克语 5、意大利语 1、拉丁语 1、Arapaho 2、Navajo 1），其中 30 篇是 DMR 2026 UMR parsing shared task 的测试集。Codex（gpt-6.1-sol，effort medium）在四个设定下各跑两次，Claude Opus 子代理逐句比较 gold 和各系统的标注，提出 gold 的修改方案。

**所有“gold 应改”“系统正确”都是模型审阅的判断，没有经过人工确认。**

先读 `analysis/SUMMARY.md`。

## 设定

| 键 | 目录 | 内容 |
|---|---|---|
| `s0` | `runs/s0-oneline` | baseline：guideline 只有一句话，无工具，整篇一次标完。只跑 30 篇测试文档。 |
| `s1f` | `runs/s1-full` | 完整 guideline，无工具，整篇。 |
| `s3` | `runs/s3-all` | 精简 guideline 加三个查询工具（guideline 搜索、PropBank、训练数据），整篇。 |
| `a2` | `runs/a2-sentence-all` | 逐句标图，再写文档级关系；精简 guideline 加三个工具。 |

每个设定两次运行：`r1` 用 `prompts/`，`r2` 用 `prompts-r2/`（同样内容，换了措辞）。

## 目录

- `analysis/SUMMARY.md`：总结。`error-patterns.md`：错误类型，末尾是需要决定的规则清单。
- `analysis/gold-errors.md`、`points.md`：gold 错误统计；各系统在比较点上的正确率、一致度、voting。
- `analysis/scores.md`、`scores-by-language.md`、`jumach.md`、`pairwise.md`：AnCast++、juːmæʧ、两两分数。`scores-codex.*` 是 Codex 交回时自己算的分数。
- `analysis/breakdown.html`、`breakdown.md`：分项 F1 在各设定下的变化（热力图和表）。分项由 `pipeline/breakdown.py` 计算，和 `exp/scripts/breakdown.py`（umrjudge）不是同一个打分器。
- `review/umr-gold-review.html`：审阅页面（单文件，浏览器直接打开；逐句看各标注，接受或拒绝每条修改方案，导出修订版 gold）。
- `review/items/`：审阅条目，每个比较点一条，格式见 `review/REVIEWER.md`。`reports/`、`points/`、`proposals/` 由 `pipeline/items.py build` 从条目生成。
- `data/gold/`：审阅所针对的 gold。`data/gold_revised/`：应用 high、mid 修改方案后的 gold。`data/gold_st22/`：UMR 2.2 test-gold。`data/gold_official/`：13 篇旧中文测试文件的发布版 gold。
- `runs/`：系统输出（`.umr`）和每次运行的 meta、trace。
- `pipeline/`、`lib/`、`tools/`、`vendor/`：打分、统计、审阅用的脚本；`vendor/umrancast` 改了一行（共指召回的除零）。

## gold 的版本

- 13 篇旧中文测试文件（zh-0021–0024、0027–0035）和 18 篇非测试中文文件用的是第一轮拿到的在审版本，和发布版不同。
- zh-0026、zh-0036 和所有非中文文件用 UMR 2.2 test-gold；捷克语 3 个文件修了 4 处 `/` 后缺空格（`data/gold_spacing_fixes.json`）。
- `data/gold_text_repairs.json` 记录了 gold 文件里审阅工具读不了、显示时做了修补的几处。

## resources

- `resources/guidelines/`：完整版和精简版 guideline。
- `resources/propbank/`：中文、英文的 PropBank 词表（JSON）。
- `resources/training/training-clean/`：shared task 的 clean 训练数据（UMR 2.2），许可见 `resources/training/README.txt`。

没有放进来的：dirty 训练数据（约 244 MB，在 UMR 2.2 发布包里，http://hdl.handle.net/11234/1-6132）和 `search_annotations` 工具的搜索缓存（`.records-*.jsonl`，运行时自动重建）。运行时 `search_annotations` 用的是 clean 和 dirty 两部分；要复现带工具的设定，需要把 dirty 数据放回 `resources/training/training-dirty/`。

## 重新生成

```bash
python3 pipeline/items.py build          # 条目 -> reports、points、proposals
node review/apply_proposals.js --all     # -> data/gold_revised
python3 pipeline/score.py                # AnCast++（需要 penman 等，见 requirements.txt）
python3 pipeline/jumach.py               # juːmæʧ（需要 perl）
python3 pipeline/points.py && python3 pipeline/errors.py
python3 pipeline/breakdown.py && python3 pipeline/breakdown_chart.py
python3 review/build.py                  # 审阅页面
```
