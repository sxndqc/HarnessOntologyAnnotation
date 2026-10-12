## Test: 800 sentences (accuracy and macro-F1 over the eight domains, percent)

| system | accuracy | macro-F1 |
|---|---|---|
| R0 | 63.8 | 54.5 |
| B-few | 67.8 | 58.5 |
| B-majority | 33.4 | 6.3 |
| B-manifestoberta | 72.1 | 59.2 |
| B-tfidf | 42.9 | 22.9 |
| B-tfidf-full | 62.5 | 50.3 |
| B-zero | 65.0 | 56.0 |

## Learning curve: training document n (120 sentences) coded with the version that had not seen it

| n | document | version | accuracy | macro-F1 |
|---|---|---|---|---|
| 1 | train_01 | R0 | 70.8 | 66.9 |
| 2 | train_02 | R1 | 72.5 | 60.8 |
| 3 | train_03 | R2 | 64.2 | 60.3 |
| 4 | train_04 | R3 | 60.8 | 53.1 |
| 5 | train_05 | R4 | 72.5 | 60.4 |
| 6 | train_06 | R5 | 69.2 | 59.3 |
| 7 | train_07 | R6 | 73.3 | 70.7 |

## What each RSI round changed

| round | document | prompt edits | tools | rules | new steps | removed steps | registry | rejected | skill.md chars |
|---|---|---|---|---|---|---|---|---|---|
| R1 | train_01 | 9 | 1 | 0 | 0 | 0 | 0 | 0 | 11437 |
| R2 | train_02 | 13 | 1 | 0 | 0 | 0 | 0 | 0 | 16599 |
| R3 | train_03 | 25 | 1 | 0 | 0 | 0 | 0 | 0 | 21250 |
| R4 | train_04 | 20 | 1 | 0 | 0 | 0 | 0 | 0 | 24929 |
| R5 | train_05 | 16 | 1 | 0 | 0 | 0 | 0 | 1 | 26206 |
| R6 | train_06 | 30 | 1 | 0 | 0 | 0 | 0 | 0 | 27688 |
