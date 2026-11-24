# 替换清单

由 `python3 pipeline/revise_guidelines.py` 生成。“条目”是 analysis/guideline-revision-checklist.md 的编号；数字是这条规则在该文件里替换的次数。

## umr_guidelines.md

| 条目 | 模式 | 改成 | 次数 |
|---|---|---|---|
| 2.1 | `:poss\b(?!essor)` | `:possessor` | 28 |
| 2.2 | `:(?:modstr\|MODSTR)\b` | `:modal-strength` | 337 |
| 2.2 | `\bmodstr:` | `:modal-strength` | 2 |
| 2.3 | `\b(FullAff\|PrtAff\|NeutAff\|FullNeg\|PrtNeg\|NeutNeg\|Unsp)\b` | `（见脚本）` | 484 |
| 2.3 | `(:modal-strength )Aff\b` | `\1full-affirmative` | 2 |
| 2.4 | `:ref-(number\|person)(?![a-z-])` | `:refer-\1` | 474 |
| 2.5 | `(:refer-(?:number\|person) )([A-Z][A-Za-z]+)` | `（见脚本）` | 305 |
| 2.7 | `:Aspect\b` | `:aspect` | 5 |
| 2.6 | `(:aspect )([A-Z][A-Za-z]+)` | `（见脚本）` | 351 |
| 2.8 | `:quot\b` | `:quote` | 16 |
| 2.9 | `\bDCT\b` | `document-creation-time` | 39 |
| 2.9 | `\bAUTH\b` | `author` | 87 |
| 2.9 | `\bROOT\b` | `root` | 8 |
| 2.10 | `\b(PAST\|PRESENT\|FUTURE\|Past\|Present\|Future)_R(?:EF\|ef)\b` | `（见脚本）` | 29 |
| 2.11 | `:MODAL\b` | `:modal` | 4 |
| 2.11 | `:AFF\b` | `:full-affirmative` | 3 |
| 2.11 | `:NEUT\b` | `:neutral-affirmative` | 1 |
| 2.13 | `:arg(\d)` | `:ARG\1` | 8 |
| 2.14 | `:(Actor\|Undergoer)\b` | `（见脚本）` | 2 |
| 3.1 | `:includes\b` | `:contained` | 4 |
| 3.6 | `:location\b` | `:place` | 5 |
| 4.2 | `\(([a-z][A-Za-z0-9]*)/ *(?=\S)` | `(\1 / ` | 1362 |

格式和结构（第 2 步）：

- example numbers as plain lines (4.8)：344
- HTML links turned into plain text (5.3)：263
- Markdown links to anchors turned into plain text (5.3)：281
- other HTML tags removed (4.7)：185
- headings repaired (leading space, level) (5.1, 5.2)：22
- :wiki removed from an example (4.9)：55
- graphs with variables renamed to s1x (4.1)：228
- graphs re-indented (4.5)：208
- graphs that do not parse, left as written：40
- glosses moved out of a graph (4.6)：72
- HTML tables turned into Markdown tables (4.7)：7
- table rows with the padding squeezed out：110
- side-by-side examples split (4.4)：10
- leftover :wiki or gloss removed line by line：13
- 示例里 `:part` 改 `:part-of`（3.2，都是部分为父节点）：6
- 示例里删掉 `:modpred`（3.10）：20

内容改写（第 3 步）：

| 条目 | 原文（开头） | 改成（开头） | 次数 |
|---|---|---|---|
| 5.4 | # Uniform Meaning Representation (UMR) 0.9 Specification ============= | # Uniform Meaning Representation (UMR) guidelines, local revised versi | 1 |
| 3.2 | UMR uses `:possessor` and `:part` relations with the possessum or part | UMR uses the `:possessor` and `:part-of` relations with the possessum  | 0 |
| 3.2 | **:possessor**, **:part**, or | **:possessor**, **:part-of** (the part is the parent; **:part** when t | 1 |
| 3.10 | ##### Part 4-3-1-2. modpred relation | ##### Part 4-3-1-2. Events under the scope of a modal event | 1 |
| 3.10 | * Part 4-3-1-2. modpred relation | * Part 4-3-1-2. Events under the scope of a modal event | 1 |
| 3.10 | Events under the scope of a modal identified as its own event are only | Events under the scope of a modal identified as its own event get no ` | 1 |
| 3.10 | Events that are linked with a `:modpred` relation in the sentence-leve | Events that are linked to a complement-taking predicate in the modal d | 1 |
| 3.10 | There are two dependency relations: `:modpred` for the link between a  | The link between a modal event and the event(s) that it modalizes is w | 1 |
| 3.10 | / Events under the scope of modals / `:modpred` relation to CPT / | / Events under the scope of modals / child of the modal event (CPT) in | 1 |
| 3.10 | a **:modpred** rela | a link to that modal event in the document-level modal dependency (for | 1 |
| 3.11 | (s2a :subset-of s1a2) | (s1a2 :subset-of s2a) | 1 |
| 3.11 | (s2a :subset-of s1a3) | (s1a3 :subset-of s2a) | 1 |
| 3.8 | :time (s1s / soon | :temporal (s1s / soon | 1 |
| 5.3 | Back to Table of Contents |  | 75 |
| 5.1 | **Table of Contents** | ## Table of Contents | 1 |

- 目录按正文标题重新生成（5.1）：85 项

## umr_guidelines_abridged.md

| 条目 | 模式 | 改成 | 次数 |
|---|---|---|---|
| 2.12 | `\bamr-unknown\b` | `umr-unknown` | 2 |

内容改写（第 3 步）：

| 条目 | 原文（开头） | 改成（开头） | 次数 |
|---|---|---|---|
| 3.2 | `:part` / `:part-of` | `:part-of` (the part is the parent: `(s / string :part-of (g / guitar) | 1 |
| 3.1 | `:contained` (child inside parent), `:contains`, `:depends-on` | `:contained` (child inside parent; `:contains` is not used), `:depends | 1 |
| 3.7 | `:instrument`, `:cause`, `:reason`, | `:instrument`, `:cause` (what brings the event about), `:reason` (the  | 1 |
| 3.9 | `:frequency`, `:extent`, `:degree`, | `:frequency`, `:extent` (how far or how much, a measure), `:degree` (i | 1 |
| 3.11 | `:subset-of`, `:name`, `:wiki`, | `:subset-of`, `:name`, | 1 |
| 4.9 | `(c / country :wiki "Russia" :name (n / name :op1 "Russia"))` | `(c / country :name (n / name :op1 "Russia"))` | 1 |

