# 方法三：Codex / Claude Code 的 harness（留空）

这个方法先不做。五个子实验（`s1-abridged`、`s1-full`、`s2-search`、`s2-propbank`、`s2-gold`）的目录先空着。

打算的做法：同样的五个条件，同样的输入（整篇文档，一行一句）和输出格式（每句 PENMAN 图和对齐，最后一张文档级关系图，
见 `exp/api/<sub>/annotate/skill.md` 的 Output format），但由 Codex 或 Claude Code 在一个工作目录里完成：
guideline、PropBank、gold 作为文件放进目录（或者用 `exp/tools/` 的函数做成命令行工具），agent 自己决定读什么、查什么，
最后把答案写到 `answers/<doc>.txt`。打分和 chat 一样：

```bash
python3 exp/run.py harness-score <sub> --label <codex 或 claude-code>   # 读 exp/harness/<sub>/answers/<doc>.txt
```
