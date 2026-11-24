# 替换清单（第 1 步：拼写、取值、斜杠空格）

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

## umr_guidelines_abridged.md

| 条目 | 模式 | 改成 | 次数 |
|---|---|---|---|
| 2.12 | `\bamr-unknown\b` | `umr-unknown` | 2 |

