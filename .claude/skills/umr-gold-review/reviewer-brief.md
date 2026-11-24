# 给审阅子代理的简报（模板）

把尖括号里的内容换掉再发。简报是子代理知道的全部背景，不要省略。

---

工作目录：`<工作区的绝对路径>`。这是一个 UMR（Uniform Meaning Representation）标注审阅项目：每篇文档有一份人工 gold 和 <N> 份自动标注，要逐句比较，找出 gold 的错误并记录每个不一致处谁对。

你负责 **<doc> 的第 <from>–<to> 句**。

先完整读 `review/REVIEWER.md`，它是这项工作的说明：背景、已经定下来的规则、怎么看标注、怎么查依据、条目的格式、编辑操作、判断标准、写完后的检查。照它做。

你只写两个文件：

- `review/items/<doc>.<from>-<to>.json`
- `review/items/<doc>.<from>-<to>.notes.md`

要求：

- 范围内每一句都要有条目；每个条目里 gold 和每个系统各出现一次。
- 写完必须运行 `python3 pipeline/items.py check review/items/<doc>.<from>-<to>.json`，到 0 errors 为止。建议每写完几句就跑一次。
- 义项和核心论元查 PropBank（`python3 pipeline/look.py pb <词>`），不要凭印象；guideline 和训练数据先例用 `look.py gl`、`look.py ann` 查。
- 遇到 guideline 和训练数据互相矛盾、说明里又没有定规则的地方，不要自己定：gold 一侧记 `open` 或只提 `low` 的 fix，并在回复里列出来。
- 不改别的任何文件；不运行 `items.py build`、`score.py`、`build.py`、`apply_proposals.js`。
- 临时脚本放在 `<临时目录>/<doc>.<from>-<to>/`（自己新建），不要用别人的目录。

回复只要几行：条目数；fix 数（high / mid / low 各多少）；检查是否 0 errors；有没有没做完的句子；有没有需要项目负责人决定的规则冲突。不要把条目内容贴在回复里。
