# 方法三：Claude Code 的 harness

同样的五个条件（`s1-abridged`、`s1-full`、`s2-search`、`s2-propbank`、`s2-gold`）、同样的输入和输出格式，
但由 Claude Code 在一个工作目录里完成：guideline 是目录里的文件，工具是命令，agent 自己决定读什么、查什么，
最后把答案写到 `answer.txt`。Codex 版还没做。

## 运行

要装 `claude` 命令行（Claude Code），并有 UMR 2.2（`bash exp/data/fetch_umr22.sh`）和网页 repo 的检出（PropBank、guideline 搜索用）。

```bash
python3 exp/harness/claude_code.py s1-abridged --docs zh-0028,zh-0032     # 一个子实验、两篇
python3 exp/harness/claude_code.py all --docs zh-0028,zh-0032             # 五个子实验
python3 exp/harness/claude_code.py s2-gold --docs zh-0028 --prepare-only  # 只搭目录，不跑（看看 agent 拿到什么）
```

选项：`--model`（默认 `claude-opus-5-5`）、`--effort`（默认 `medium`）、`--label`（默认 `claude-code`）、
`--work`（工作目录的位置，默认 `/tmp/umr-harness`；必须在本仓库和 home 目录之外）、`--jobs`（同时跑几篇，默认 1）、
`--max-budget-usd`（每篇的花费上限）、`--login`（见下）。

默认用 `--bare` 跑：不读这台机器的 CLAUDE.md、hooks、插件、记忆和 MCP 服务器，key 用 `$UMR_MODEL_KEY`（作为
`ANTHROPIC_API_KEY` 传给它，和 API 实验同一个 key、同样计费）。加 `--login` 则用这台机器上 `claude` 的登录
（这时也会读这台机器的用户设置和 CLAUDE.md）。

## 每篇文档的工作目录

`<work>/<sub>/<doc>/`，每次重建：

| 文件 | 内容 |
|---|---|
| `TASK.md` | `harness/<sub>/TASK.md` 填上这篇文档（由 `scripts/make_subexps.py` 生成，和 API、chat 的 prompt 同一套说明） |
| `guidelines/` | s1-abridged、s2-propbank、s2-gold：缩略版；s1-full：完整版；s2-search：两份都有 |
| `tools/<tool>.py` | 这个子实验的工具：`search_guidelines.py`、`propbank_lookup.py` 或 `search_annotations.py`（`harness/cc_tools.py`，和 API 的工具同一份代码、同一份数据；`search_annotations` 不返回测试句子） |
| `notes/` | 给 agent 记笔记 |
| `.claude/settings.json` | 权限，见下 |

给 agent 的指令只有一句："Do the task described in TASK.md …, write the answer to answer.txt."

**权限**（`--permission-mode dontAsk`：设置里没允许的一律拒绝，不会停下来问）：

- 允许：读这个目录（Read、Glob、Grep），运行 `python3 tools/<tool>.py …`，写 `answer.txt` 和 `notes/`，TodoWrite。
- 禁止：其他所有命令，读本仓库、网页 repo 和 home 目录（所以读不到测试 gold），WebFetch、WebSearch，
  子 agent（Agent/Task：子 agent 可能用别的模型）。

## 结果

- `harness/<sub>/answers/<label>/<doc>.txt`：`answer.txt` 原样；`<doc>.meta.json`：花费、轮数、用时、每个模型的用量、
  被拒绝的操作、每一次工具调用。
- `.cache/harness-logs/<sub>/<label>/<doc>.jsonl`：完整对话记录（stream-json，不进 git）。
- `runs/harness/<sub>/<label>/`：打分，和 API、chat 一样（跑完自动打；也可以 `python3 exp/run.py harness-score <sub> --label <label>`）。
  然后 `python3 exp/run.py table` 更新总表。

`meta.json` 的 `models` 列出这篇用到的所有模型：Claude Code 有时会用小模型做后台的小事，如果不只是 `claude-opus-5-5`，会在这里看到。
