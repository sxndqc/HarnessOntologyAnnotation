# 第二轮运行记录

用户要求执行 v2 交接包，并发 10。只用订阅登录，模型 gpt-6.1-sol / medium。上一轮任务已停止，本轮属于新的明确授权。

## 环境

在 v2 自己的 .venv 中安装 penman、numpy 和本包 vendor/umrancast；共指 protected_divide 修复验证为 True。Node 使用 /Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node。未改任务说明、资源、工具或解析库。

## 启动前估算

新增 3464 会话：128 整篇 + 3336 逐句。按上一轮最终 meta 汇总外推，Standard 公开价用量等值中心约 14725 credits；规划范围 12000–22000 credits，不是实际扣费预测或硬上限。费率：gpt-6.1-sol 每百万非缓存输入50、缓存输入2.5、输出250 credits（https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing）。input_tokens 中缓存部分扣除后分别计价；reasoning_output_tokens 不再重复加到 output_tokens。

外推方法：s1/s3/a2 按新增834句与旧712句的比例；新 s0 无实测，用 s1 按1019/1424缩放再乘0.6作粗略代理。估算分别约941、807、12633、345 credits。多语言、工具查询、cache hit、重试和速度档位会改变实际值；若使用 Fast 付费credits费率为Standard的2倍，当前估算仅按Standard。

上一轮累计会话耗时外推后/10约7.8小时，实际规划标注10–16小时；不含无法预计的限流暂停和额外补跑，自动评分另外计时。账号状态查询仍为Business、unlimited=true、无可读余额；公司邮件说明12月11日前试用免费，不能将公开价折算等同实际账单。

## 进度

已准备环境；先跑 en-0008 与 arp-0005，验收通过才启动全量。

## 首次试跑环境问题与处理

新语言 search_annotations 缓存缺失，子会话无法写入 resources/training，出现工具失败与局部绕行代码。停止首次试跑并将所有该次结果移至 analysis/initial-smoke-cache-error，不作为正式结果。通过原 tools.cli.main 预先查询无匹配关键词，按工具自身逻辑生成各语言缓存；未直接读取训练文件、未改工具代码或提示词。预热日志在 analysis/preflight。随后重新试跑。

## 重新试跑未通过自动验收

[
  "s3/r1 arp-0005 audit flags [\"tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\"]",
  "s3/r2 arp-0005 audit flags ['tool not in this condition: /bin/zsh -lc \"rg --files -g \\'\"\\'!tools/*\\'\"\\'\"', \"tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\"]",
  "a2/r1 arp-0005 audit flags [\"g1: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g2: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g6: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g7: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g8: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g9: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g10: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g11: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\"]",
  "a2/r2 en-0008 audit flags [\"r2: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\"]",
  "a2/r2 arp-0005 audit flags [\"g1: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g3: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g4: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g5: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g6: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g7: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g8: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\", \"g10: tool not in this condition: /bin/zsh -lc 'cat tools/search_annotations.py'\"]"
]
全量尚未启动。

## 20条试跑审计标记核验与授权恢复

用户要求核验误报后以10并发继续。20条标记来自19个会话：19条读取本地search_annotations包装脚本，1条rg列文件时排除tools。逐条命令/输出核验并检查604条命令，未见越界读取、联网或绕过工具。包装脚本内容逐字匹配运行器STUB。原始meta、transcript和运行器audit函数保持不变；仅外层workflow对SHA-256绑定的20条记录豁免，未知标记不在本次放行范围内。完整证据见smoke-audit-reviewed.json与SMOKE-AUDIT-REVIEW.txt。恢复前全部smoke gate检查通过。

## 试跑自动验收通过

两篇、八系统、完整句数、无解析错误/未解决审计标记/失败（原20条审计标记保留，人工核验为误报，见SMOKE-AUDIT-REVIEW.txt）；工具语言与无PropBank响应证据均检查通过。

| condition | run | documents | sentences found | parse problems | audit flags | failed |
|---|---|---|---|---|---|---|
| s0-oneline | gpt-6.1-sol-medium-r1 | 2/2 | 20/20 | 0 | 0 | 0 |
| s0-oneline | gpt-6.1-sol-medium-r2 | 2/2 | 20/20 | 0 | 0 | 0 |
| s1-full | gpt-6.1-sol-medium-r1 | 2/2 | 20/20 | 0 | 0 | 0 |
| s1-full | gpt-6.1-sol-medium-r2 | 2/2 | 20/20 | 0 | 0 | 0 |
| s3-all | gpt-6.1-sol-medium-r1 | 2/2 | 20/20 | 0 | 1 | 0 |
| s3-all | gpt-6.1-sol-medium-r2 | 2/2 | 20/20 | 0 | 2 | 0 |
| a2-sentence-all | gpt-6.1-sol-medium-r1 | 2/2 | 20/20 | 0 | 8 | 0 |
| a2-sentence-all | gpt-6.1-sol-medium-r2 | 2/2 | 20/20 | 0 | 9 | 0 |

all done


## 全量结束

结束时间 2026-11-19T04:15:34.220908-05:00；本工作流墙钟 6.43 小时。

| condition | run | documents | sentences found | parse problems | audit flags | failed |
|---|---|---|---|---|---|---|
| s0-oneline | gpt-6.1-sol-medium-r1 | 30/30 | 1019/1019 | 0 | 0 | 0 |
| s0-oneline | gpt-6.1-sol-medium-r2 | 30/30 | 1019/1019 | 0 | 0 | 0 |
| s1-full | gpt-6.1-sol-medium-r1 | 48/48 | 1544/1546 | 34 | 0 | 0 |
| s1-full | gpt-6.1-sol-medium-r2 | 48/48 | 1546/1546 | 0 | 0 | 0 |
| s3-all | gpt-6.1-sol-medium-r1 | 48/48 | 1546/1546 | 0 | 59 | 0 |
| s3-all | gpt-6.1-sol-medium-r2 | 48/48 | 1546/1546 | 0 | 52 | 0 |
| a2-sentence-all | gpt-6.1-sol-medium-r1 | 48/48 | 1546/1546 | 0 | 332 | 0 |
| a2-sentence-all | gpt-6.1-sol-medium-r2 | 48/48 | 1546/1546 | 0 | 504 | 0 |

all done

审计标记见 audit-flags.json；旧 zh-0017 问题保留，不重复排查。

## 自动分析与交付

已执行 score.py、pairwise.py、tool_calls.py。各评分日志的FAILED仍需结合gold自评分判定；脚本成功退出不等于所有配对成功。PUD仅解读句子级；Czech无时间模态gold。所有审计标记保留。
