# 量词规则更正（给重判者）

## 背景

`review/items/<doc>.<from>-<to>.json` 是 31 篇中文 UMR 文档的审阅条目：每个条目是 gold 和 6 份系统标注（s1f/r1、s1f/r2、s3/r1、s3/r2、a2/r1、a2/r2）的一个比较点，`choices` 里记着谁选了什么、status（ok / minor / bad / open），`fix` 是对 gold 的修改方案（conf 为 high / mid / low；low 不进修订版 gold）。格式、编辑操作、检查方法见 `review/REVIEWER.md`，先读它的"条目"和"写完后的检查"两节。

第一轮审阅按精简版 guideline 的一句话（"普通量词省略，三本书 → 书 :quant 3"）把 gold 里保留量词的写法判成了错，提了大量"删掉量词节点"的方案。**项目负责人已经明确：量词都要保留**，写成 `名词 :quant N :unit (量词)`；gold 里没标量词的地方是 gold 漏标。你的任务是按这条规则把你负责的文档里和量词有关的条目重判一遍，并补上 gold 漏标的地方。

## 规则

1. 数量短语里的量词（个、位、名、条、种、篇、架、辆、款、次、届、场、轮……以及年、美元、公里等度量单位）都保留为 `:unit` 节点，挂在被计数的名词（或 temporal-quantity 之类的量节点、ordinal-entity）上，和 `:quant` 并列。
2. 标注里有这个量词节点：`ok`。
3. 标注里省掉了量词节点：`minor`（漏了一个节点；系统拿到的精简版说明让它们省略，所以不判 `bad`）。gold 省掉了也是 `minor`，并且要写 fix 补上。
4. 量词用法本身不对的仍然是错，不因为这条规则变成对的：把量词挂错了节点、把不是量词的词写成 `:unit`（例如 `飞机 :unit 机`）、用 `:unit` 表示别的关系、量词节点进了文档级共指等。
5. "多轮""几次"这类，整词作一个概念和拆成数量加 `:unit` 都可以（都 `ok`）；完全没有表示的是 `minor`。
6. 只动和量词有关的判断。同一个条目里别的问题（角色、义项、结构）不要改。

## 怎么做

```bash
python3 pipeline/unit_scan.py zh-0005
```

第 1 部分列出每句各标注里的 `:unit`（`量词←所挂的节点`），第 2 部分列出提到量词或 `:unit` 的条目（文件名、在文件里的位置 `#i`、选择、fix）。细节用 `python3 pipeline/mechdiff.py <doc> <句号>` 和 `python3 pipeline/show_sentence.py <doc> <句号> --only gold,...` 看。

对第 2 部分的每个条目：

- **和量词无关**（只是文字里碰巧有 `:unit`，或讲的是别的事）：不动。
- **fix 只是删量词节点 / 删 `:unit`**：`fix` 改成 `null`；gold 所在选择的 status 改 `ok`；省掉量词的选择改 `minor`；`best` 改成保留量词的那个选择的 label。
- **fix 里除了删量词还有别的修改**：把删量词的那些 op 去掉，其余保留；title、why 相应改掉；status 按上面的规则重判。去掉后 ops 为空就把 fix 改成 `null`。
- **条目里有系统保留了量词而被判 minor / bad**（常见于 a2）：改 `ok`；省掉量词的改 `minor`。如果 gold 在省掉的一边，gold 改 `minor`，并写 fix 补上量词（见下）。
- 改过的条目：加一个字段 `"before_unit_correction"`，值是 `{"status": [原来各选择的 status，按顺序], "best": 原 best, "fix": 原 fix（整个对象或 null）}`；在 `text` 开头加上 `【更正】量词按规则保留为 :unit。`，后面接修改后的说明（原说明里"量词应省略"之类的话改掉）。

**gold 漏标的量词**：看第 1 部分里 gold 一栏比系统少量词的句子，再把你负责的文档的每一句原文扫一遍（`unit_scan.py` 只列了有 `:unit` 或有条目的句子；其余句子用 `python3 pipeline/show_sentence.py <doc> <句号> --only gold` 看），找"数词 + 量词"而 gold 没有 `:unit` 的地方。每处：

- 如果已有条目讲这个量词，就在那个条目里加 fix；否则新建一个条目：`cat` 写 `structure`，`n` 接着这一句已有的最大编号，`choices` 按 7 份标注有没有这个量词节点分成两组（有 = `ok`，没有 = `minor`），`best` 是"有"的那组的 label；7 份都没有时只有一个选择（status `minor`），`best` 写 `null`。
- fix：`conf` 写 `mid`；ops 用 `add_node`：`{"op": "add_node", "parent": "<gold 里被计数名词或量节点的变量>", "role": "unit", "var": "<这一句没用过的变量名，如 s3u1>", "concept": "<量词>", "align": "<量词所在的词号>-<词号>"}`。如果 gold 连 `:quant` 也没有，同一个 fix 里用 `set_attr` 补上 `quant`。量词和数词粘在同一个词里（如"30万吨"是一个词）时 align 写那个词的词号。
- 新条目的 `text` 写明原文是什么、gold 少了什么。

不要为了凑数硬找：gold 把"数词+量词"整体当成一个概念且说得通的（"多轮"），不算漏标。

## 检查

每个改过的文件都要过：

```bash
python3 pipeline/items.py check review/items/zh-0005.01-16.json
```

必须 0 errors。注意几条会触发报错的规则：有 fix 且 conf 不是 low 时 gold 所在选择不能是 `ok`；有 fix 时 `best` 不能是 gold 所在的选择；7 个名字每个条目里各出现一次。

只改你负责的文档的 `review/items/<doc>.*.json`，不改别的文件，不运行 `items.py build`、`score.py`、`build.py`。临时脚本放在会话临时目录下你自己新建的子目录 `unit-<第一篇文档号>/` 里。直接改 JSON 文件即可（建议用小脚本按 `#i` 定位修改，改完重新读一遍确认）。

## 回复

几行即可：每篇文档改了多少条目、撤掉或缩减了多少条 fix、为 gold 漏标新增了多少条 fix（其中新建条目多少）、各文件检查是否 0 errors、有没有拿不准的情况。
