---
name: umr-gold-review
description: Compare UMR gold annotations with parser outputs sentence by sentence — find every difference, judge which side is right, propose mechanical fixes to the gold, build a revised gold, rescore, and produce statistics and a single-file HTML review page. Use when the user asks to review or audit a UMR gold against system/parser outputs, find errors in a UMR gold, "对比 gold 和 parse 输出", "找 gold 的错误", "审校 gold", "修订 gold", or wants per-system accuracy and agreement at the points where annotations differ. Not for running a parser and not for plain scoring (AnCast/juːmæʧ alone need only pipeline/score.py and pipeline/jumach.py).
---

# UMR gold 与 parse 输出的逐句对比审阅

把一份 UMR gold 和若干份自动标注逐句比较，得到：每个不一致处的判断（谁对）、对 gold 的可机械执行的修改方案、修订版 gold、各系统的正确率和相互一致度、分数，以及一个给人逐条确认用的单文件 HTML 页面。

工具在本仓库的 `exp/review-round2/`（脚本 `pipeline/`、`lib/`、`tools/`，页面 `review/`，资源 `resources/`）。那个目录本身是第二轮审阅的完整结果，可以当例子看：`README.md`、`analysis/SUMMARY.md`、`review/items/`。

所有判断来自模型审阅。向用户报告时每次都要说明这一点；修订版 gold 在人工过一遍之前不是定稿。

## 你是组织者，审阅交给子代理

一篇文档约 10 到 20 句的一段交给一个审阅子代理；你负责搭工作区、写说明、分段、派发、检查交回的文件、合并、打分、写总结。不要自己逐句审，也不要让一个子代理审整篇长文档。

审阅子代理的模型按用户的偏好选（上两轮用户指定 Opus，原因是成本）。同时运行的子代理上限约 20 个。

## 步骤

### 1. 建工作区

新数据不要在 `exp/review-round2/` 里做，另建一个：

```bash
python3 .claude/skills/umr-gold-review/scripts/new_workspace.py --to <工作区> \
    --gold <gold 目录> --run s3/r1=<输出目录> --run s3/r2=<输出目录> --run a2/r1=<输出目录>
```

`--run` 的键是"设定/运行"，同一设定的多次运行用 r1、r2；输出目录里每篇一个 `.umr`，文件名和 gold 一样。脚本复制工具、链接 `resources/`、生成 `data/docs.json`、`config.json` 和 `runs/`。之后的命令都在工作区根目录运行。

先确认每个文件读得进来：

```bash
python3 pipeline/mechdiff.py <doc> 1      # 第 1 句：gold 的图，加各标注不一致的地方
python3 pipeline/show_sentence.py <doc> 1 # 各标注的原文
```

gold 文件本身格式坏了（括号不配、`/` 后缺空格）读不进来时，不改 gold 文件：把修补写进 `data/gold_text_repairs.json`（`{"<doc>": [{"line": N, "from": "原行", "to": "新行", "why": "..."}]}`），并在总结里列出来。

### 2. 改审阅说明

`review/REVIEWER.md` 是给审阅子代理的完整说明（条目格式、编辑操作、判断标准、检查方法）。它是按第二轮的 8 个系统、7 种语言写的，开工前改三处：

- **背景**里的系统表，换成这次的系统和设定。
- **已经定下来的规则**。现有三条：量词都保留为 `:unit`；`have-org-role-92`、`have-rel-role-92` 是对的；`:part` 以部分为父节点。前两条是项目负责人定的，第三条是按完整版 guideline 3-2-2-1 的处理。沿用还是改，问用户。
- **各语言要注意的**，删掉这次没有的语言，新语言补上你知道的情况。

### 3. 先做一段试点

挑一篇短文档的一段，派一个子代理（简报见 `reviewer-brief.md`）。交回后你自己核对几条：归属对不对（对着 `mechdiff.py` 的 `⟵` 列表）、fix 是否真的有依据、status 的宽严。说明里有歧义的地方现在改，比全部派出去以后统一返工便宜得多。

### 4. 分段派发

按句数分段，文件名 `review/items/<doc>.<from>-<to>.json`（句号两位，超过 99 句的文档三位）。每个子代理的简报里写明：文档、句子范围、先读 `review/REVIEWER.md`、只写自己的两个文件、临时脚本放在自己新建的子目录里、不运行 `items.py build` / `score.py` / `build.py`。

这几条是出过问题才加的，不要省：

- **临时目录各用各的。** 子代理共用一个临时目录时互相覆盖过脚本。
- **审阅进行中不要生成 `data/gold_revised/`。** `show_sentence.py` 会把它显示给还在工作的审阅者，他们会把修订版当成另一份标注。
- **规则冲突不让审阅者定。** guideline、精简版 guideline、训练数据互相矛盾的地方，审阅者会各判各的。发现一类冲突就停下来问用户，定了以后写进"已经定下来的规则"，再让受影响的段重判。
- **系统全篇重复的同一种习惯只计一次**：在这篇文档里第一次出现处按实际判，之后记 `open` 并注明"同一习惯，见第 N 句"，否则一个习惯会被算几百次。

### 5. 收回并检查

每个交回的文件都要过，必须 0 errors：

```bash
python3 pipeline/items.py check review/items/<doc>.<from>-<to>.json
```

它检查格式、每个名字是否在每个条目里各出现一次、每个 `grep` 是否真的在所列标注里、每个 fix 能否在 gold 上单独执行以及合并执行。有 errors 就把输出发回给那个子代理改，不要自己猜着改。

全部交回后看一遍有没有系统性的误判（同一类问题各段判法相反）。有就写一份更正说明，派子代理按规则统一重判；改过的条目保留原判断。上一轮的两份更正说明可以当模板：`exp/review-round2/review/UNIT-RULE.md`（按一条规则重判）和 `exp/review-round2/review/S0-EXTENSION.md`（给已有条目补上后来才跑的系统）。

### 6. 合并、修订、打分、统计

```bash
python3 pipeline/items.py build          # 条目 -> review/reports、points、proposals
node review/apply_proposals.js --all     # high、mid 的方案 -> data/gold_revised
python3 pipeline/score.py                # AnCast++：对原 gold 和修订版
python3 pipeline/jumach.py               # juːmæʧ（需要 perl）
python3 pipeline/points.py               # 比较点上的正确率、一致度、voting
python3 pipeline/errors.py               # gold 错误按类别、语言、文档
python3 pipeline/pairwise.py             # 标注两两之间的 AnCast++
python3 pipeline/breakdown.py && python3 pipeline/breakdown_chart.py   # 分项 F1 和热力图
```

依赖：`pip install -r requirements.txt`，node，perl。AnCast 用的是 `vendor/umrancast`（改过一行，避免共指召回除零），不是系统里装的那个。`apply_proposals.js` 报 skipped 说明有方案在合并后执行不了，回到第 5 步。

### 7. 总结和页面

写 `analysis/SUMMARY.md`（先说结论，再给数字和注意事项）和 `analysis/error-patterns.md`（gold 的错误类型、各系统的错误类型、审阅的局限、需要用户决定的规则）。后者可以交给一个子代理从各段的 `.notes.md` 和条目里归纳，数字必须来自脚本计数。然后：

```bash
python3 review/build.py                  # -> review/umr-gold-review.html
```

在浏览器里打开检查：文档能切换、各份标注和修改方案显示正常、控制台没有报错。页面是自包含的单文件，用户在里面接受或拒绝每条方案，导出决定后用 `node review/apply_proposals.js --all --decisions <导出的 json>` 生成只含已接受修改的 gold。

## 条目是什么

一个条目是一个比较点：`sent`、`n`、`topic`、`cat`（sense、role、concept、structure、attr、doc-temporal、doc-modal、doc-coref）、`choices`（每个选择有 `label`、`systems`、`status`：ok 正确 / minor 可接受但略差 / bad 错 / open 定不了，可选 `grep`）、`best`、`text`、`fix`（`title`、`conf`：high / mid / low、`why`、`ops`；没有就是 null）。gold 和每个系统在每个条目里各出现一次。low 的 fix 只作提示，不进修订版。完整格式和编辑操作表在 `review/REVIEWER.md` 的"条目"一节。

## 向用户报告时必须带上的说明

- 判断来自模型，没有经过人工确认。
- 比较点只取各标注不一致的地方，所以"gold 在比较点上的正确率"不能读成 gold 整体的正确率；整体改动幅度看原 gold 对修订版 gold 的分数。
- 审阅者拿 gold 和几份同源的系统标注比，系统之间一致而 gold 不同的地方容易被判成 gold 的问题；gold 修订后系统分数上升，有一部分是这个原因。
- 审阅者不熟悉的语言（上一轮是 Arapaho、Navajo、拉丁语、捷克语）只能依靠词素释义和训练数据先例，把握更低；训练数据没有文档级标注的语言，文档级判断只能靠 guideline。
- 打不了分的文档、有泄漏的文档（测试文档的句子出现在 guideline 或示例里）、用了哪个版本的 gold，都要列出来。

## 资源

`resources/` 里有完整版和精简版 guideline、中英文 PropBank、shared task 的 clean 训练数据。`pipeline/look.py`（`pb`、`gl`、`ann` 三个子命令）是审阅者查依据的入口。dirty 训练数据不在仓库里；没有它，`ann` 只搜 clean 数据。
