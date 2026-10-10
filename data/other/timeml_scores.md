## Test: TempEval-3 platinum, 20 documents, the official scorer (percent)

| system | timex strict | timex relaxed | timex value | timex type | event F1 | event class | TLINK F1 |
|---|---|---|---|---|---|---|---||
| R0 | 81.1 | 90.2 | 79.0 | 83.9 | 74.5 | 61.9 | 37.9 |
| B-zero | 85.4 | 92.9 | 84.6 | 88.4 | 80.7 | 65.5 | 39.8 |
| 2013: HeidelTime (unihd english-3) | 81.3 | 90.3 | 77.6 | 82.1 | 0.0 | 0.0 | 0.0 | TLINK 0 means the system makes none |
| 2013: ClearTK 1 | 82.7 | 90.2 | 64.7 | 84.2 | 77.3 | 65.4 | 29.8 |
| 2013: NavyTime 1 | 79.6 | 90.3 | 71.0 | 80.3 | 80.3 | 67.5 | 27.3 |
| 2013: ATT 1 | 79.0 | 85.6 | 65.0 | 78.2 | 81.0 | 71.9 | 0.0 | TLINK 0 means the system makes none |
| 2013: TIPSem (TE2) | 81.6 | 84.9 | 65.3 | 75.9 | 82.9 | 75.6 | 42.4 |
| 2013: JU-CSE | 75.5 | 86.4 | 63.8 | 75.5 | 78.6 | 52.7 | 24.6 |
| 2013: SUTime | 79.6 | 90.3 | 67.4 | 80.3 | 0.0 | 0.0 | 0.0 | TLINK 0 means the system makes none |

## TLINKs from the gold entities (TempEval-3 task C relation-only), temporal awareness F1 / P / R

| system | F1 | P | R |
|---|---|---|---|
| 2013: UTTime-1 | 56.5 | 55.6 | 57.3 |
| 2013: NavyTime 1 | 46.8 | 46.6 | 47.1 |
| 2013: JU-CSE | 34.8 | 35.1 | 34.5 |

## Learning curve: training document n scored with the version that had not seen it yet

| n | document | version | timex strict | timex relaxed | timex value | timex type | event F1 | event class | TLINK F1 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | wsj_0736 | R0 | 100.0 | 100.0 | 100.0 | 100.0 | 83.8 | 70.3 | 35.3 |
| 2 | APW20000401.0150 | R1 | 75.0 | 87.5 | 75.0 | 75.0 | 87.5 | 75.0 | 41.0 |
| 3 | wsj_0184 | R2 | 71.4 | 71.4 | 71.4 | 57.1 | 85.1 | 59.6 | 32.9 |
| 4 | wsj_0189 | R3 | 96.0 | 96.0 | 64.0 | 72.0 | 86.8 | 69.9 | 13.6 |

## What each RSI round changed

| round | document | prompt edits | tools | rules | new steps | removed steps | registry | rejected | skill.md chars |
|---|---|---|---|---|---|---|---|---|---|
| R1 | wsj_0736 | 17 | 0 | 1 | 0 | 0 | 0 | 0 | 20031 |
| R2 | APW20000401.0150 | 24 | 0 | 2 | 0 | 0 | 0 | 0 | 25660 |
| R3 | wsj_0184 | 24 | 0 | 2 | 0 | 0 | 0 | 0 | 32457 |

(skill.md characters of R0, the seed: 13758)
