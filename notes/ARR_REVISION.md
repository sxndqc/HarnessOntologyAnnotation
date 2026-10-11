# ARR 模拟评审后的修订

本轮为作者授权的 AI 模拟评审与作者侧修改，不是正式 ARR 评审。三位评审分别关注方法与统计、理论贡献与表达、复现与证据。规范来自 ACL 官方站点源码 `acl-org/aclrollingreview`，固定提交 `45188b86f0827fa8cb78ad64c2dd48337f37fbb9`；官网部署状态未验证，官方指南注明 August 2026 后将更新。

## 已修改

- 摘要、引言、结论收窄到单次固定顺序中文 UMR 轨迹；保留实测 +9.0 F，不再把未跑的强基线写成胜出。
- 将 trace 的 edit-target localization 与因果归因区分；注明归因和 anchored edits 的独立作用尚待消融。
- 用 convention-sensitive checks 的分数变化描述结果，不再推断 semantic competence 不变或达到上限。
- 区分 paired-document 条件性区间、Smatch complete-case 分母与 ±0.01 升降阈值，以及尚未测量的运行/顺序方差。
- 将留出集未见性限定于本条主 harness lineage，披露其他实验使用过部分文档及 overlap guard 访问测试原文。
- 修正 G9 完整方法行：原来把 0002–0010 的 +9.0 放进 0002–0005 的消融表，现改为空，待共同子集重算。
- 明确 TimeML/Manifesto 使用不同准入策略；9B 失败是 joint configuration 观察，不是普遍能力结论。
- 明确与 Decision Orchestration 共享的数据、judge 与复用预测，以及两篇的贡献边界。
- 新增 G14：数据版本/许可、历史参数、缺失分数分母、曝光 ledger 与匿名 artifact 核验。披露 AI 写作与模拟审稿协助。

## 实验继续留空

| 优先级 | 项目 | 待填结果 |
|---|---|---|
| 核心 | G1–G4 同数据/预算强基线与共同冻结留出集 | |
| 核心主张相关 | G9 归因/编辑方式消融 | |
| 稳健性 | G-var 重复运行/顺序 | |
| 离线核验 | G14 gold/scorer/参数与 complete-case 排除数 | |
| 扩展 | G5–G8、G10–G13 | |

更详细的协议仍在 `GAPS.md`。本轮没有新模型实验，没有改变数据、数字宏、生成表格或实验代码。

## 后续实验配置

本论文的[详细实验计划](https://github.com/sxndqc/SkillParseUMR/blob/main/docs/experiments-harness-ontology-annotation.md)独立维护。用户指定 TimeML 的四个标注阶段、主基线与消融统一使用冻结 Haiku 版本，构建/反思/reviewer 使用 Opus；既有 TimeML 数字不是这套新配置的结果，需要全部主条件重新运行。Manifesto 降为可选边界实验。实际模型 ID 和上下文设置执行前登记；本轮只更新计划，没有调用模型。

## 验证

- 数据→表格脚本在 checkout 外的副本运行，输出表格与仓库原表逐文件一致。
- 原 SkillParseUMR 的 64 项离线测试通过。
- 使用 pdfLaTeX/BibTeX/latexmk 编译，正文至 Conclusion 为 8 页；Limitations、伦理、参考文献与附录在其后。
- 本地增装字体/CJK 和 Python 依赖，环境初始化在 `/workspace/shared/arr-review/activate.sh`；生成文件写在 checkout 外。

规范：[Reviewer guidelines](https://aclrollingreview.org/reviewerguidelines)、[Review form](https://aclrollingreview.org/reviewform)、[Author checklist](https://aclrollingreview.org/authorchecklist)。提交前仍需补关键实验、核验事实/许可、完成匿名与 checklist。
