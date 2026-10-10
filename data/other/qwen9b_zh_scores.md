# qwen-zh: scores

AnCast++ sentence F and Comprehensive. seed = the document parsed with R0; before = parsed with R(k-1), the skills after the k-1 documents before it (never this one); Δ = before − seed (k = 1 is the seed itself); after = parsed with Rk, after its own round; generate = generate-guidelines with the same model, one call per sentence; detailed = umr-refine's generate prompt (Chinese: with its Chinese UMR section) and document skill, same model. RSI: problems found / edits applied / rejected.

| k | document | version | seed F | before F | Δ F | seed Comp | before Comp | Δ Comp | after F | generate F | detailed F | detailed Comp | RSI problems / applied / rejected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | chinese_umr-0008 | R0 | 21.5 | 21.5 | - | 21.4 | 21.4 | - | - | 0.0 | 8.2 | 7.2 | 276 / 8 / 2 |
| 2 | chinese_umr-0009 | R1 | 21.1 | 28.7 | 7.6 | 19.0 | 24.9 | 5.8 | - | 0.0 | 12.9 | 10.6 | 228 / 5 / 4 |
| 3 | chinese_umr-0010 | R2 | 21.2 | 20.5 | -0.7 | 19.8 | 20.2 | 0.5 | - | 0.0 | 3.0 | 4.2 | 230 / 3 / 2 |
| 4 | chinese_umr-0011 | R3 | 16.4 | 14.1 | -2.4 | 17.4 | 15.8 | -1.5 | - | 0.0 | 6.5 | 5.7 | 554 / 3 / 1 |
| 5 | chinese_umr-0012 | R4 | 19.1 | 19.8 | 0.7 | 19.6 | 20.1 | 0.5 | - | 0.0 | 3.1 | 4.2 | 211 / 8 / 3 |
| 6 | chinese_umr-0013 | R5 | 12.7 | 12.5 | -0.2 | 13.6 | 14.0 | 0.3 | - | 0.0 | 3.3 | 3.2 | 203 / 11 / 3 |
| 7 | chinese_umr-0014 | R6 | 21.3 | 19.8 | -1.5 | 21.1 | 19.0 | -2.1 | - | 0.0 | 4.0 | 4.5 | 282 / 8 / 5 |
| 8 | chinese_umr-0015 | R7 | 19.4 | 16.4 | -3.0 | 18.3 | 15.2 | -3.1 | - | 0.0 | 12.1 | 10.1 | 370 / 17 / 4 |
| 9 | chinese_umr-0016 | R8 | 16.5 | 11.2 | -5.3 | 17.2 | 12.6 | -4.6 | - | 0.0 | 3.7 | 3.7 | 314 / 7 / 3 |
| 10 | chinese_umr-0017 | R9 | 18.4 | 12.2 | -6.3 | 18.6 | 14.4 | -4.2 | - | 0.0 | 3.9 | 5.3 | 331 / 9 / 4 |
| 11 | chinese_umr-0018 | R10 | 16.7 | 11.9 | -4.8 | 17.0 | 12.5 | -4.5 | - | 0.0 | 2.8 | 3.1 | 617 / 8 / 0 |
| 12 | chinese_umr-0021 | R11 | 15.8 | 13.2 | -2.6 | 18.3 | 15.6 | -2.8 | - | 0.0 | 4.8 | 6.5 | 298 / 10 / 6 |
| 13 | chinese_umr-0022 | R12 | 14.3 | 13.1 | -1.2 | 16.6 | 14.8 | -1.8 | - | 0.0 | 2.0 | 2.7 | 227 / 6 / 1 |
| 14 | chinese_umr-0023 | R13 | 16.1 | 18.0 | 1.9 | 19.5 | 20.5 | 1.0 | - | 0.0 | 4.3 | 5.4 | 373 / 11 / 2 |
| 15 | chinese_umr-0024 | R14 | 23.3 | - | - | 22.2 | - | - | - | 0.0 | 5.5 | 5.3 | - |
| 16 | chinese_umr-0027 | R15 | 13.1 | - | - | 14.7 | - | - | - | 0.0 | 3.7 | 4.4 | - |
| 17 | chinese_umr-0028 | R16 | 20.5 | - | - | 23.0 | - | - | - | 0.0 | 7.6 | 8.8 | - |
| 18 | chinese_umr-0029 | R17 | 16.5 | - | - | 17.1 | - | - | - | 0.0 | 6.1 | 7.5 | - |
| 19 | chinese_umr-0030 | R18 | 11.8 | - | - | 10.4 | - | - | - | 0.0 | 4.4 | 4.9 | - |
| 20 | chinese_umr-0031 | R19 | 23.7 | - | - | 23.7 | - | - | - | 0.0 | 16.7 | 16.2 | - |
| 21 | chinese_umr-0032 | R20 | 18.9 | - | - | 19.7 | - | - | - | 0.0 | 12.1 | 10.3 | - |
| 22 | chinese_umr-0033 | R21 | - | - | - | - | - | - | - | 0.0 | 15.8 | 13.2 | - |
| 23 | chinese_umr-0034 | R22 | - | - | - | - | - | - | - | 0.0 | 2.2 | 3.1 | - |
| 24 | chinese_umr-0035 | R23 | - | - | - | - | - | - | - | 0.0 | 5.9 | 7.2 | - |

Predicted graphs AnCast could not match (placeholder concepts, undeclared variables), scored as empty sentences: chinese_umr-0009 before: [4]; chinese_umr-0010 seed: [8, 12]; chinese_umr-0010 before: [4]; chinese_umr-0011 seed: [25]; chinese_umr-0011 before: [12, 19]; chinese_umr-0013 seed: [11, 12]; chinese_umr-0013 before: [5]; chinese_umr-0015 seed: [10, 16]; chinese_umr-0016 seed: [11]; chinese_umr-0016 before: [2, 5]; chinese_umr-0017 seed: ['6', '11', 'gold 11']; chinese_umr-0017 before: ['9', '11', '14', 'gold 11']; chinese_umr-0018 seed: [3, 4, 9, 28]; chinese_umr-0018 before: [8, 29]; chinese_umr-0022 before: [1, 9, 11]; chinese_umr-0024 seed: [11]; chinese_umr-0027 seed: [11]; chinese_umr-0029 seed: [10]; chinese_umr-0032 seed: [5].

Mean Δ F over the 13 documents with both parses (k ≥ 2): -1.4; mean Δ Comp: -1.3.
First half of them: 0.6, second half: -3.0 (does the gain grow as more documents are seen?).

Noise: the seed parsed twice, independently (seed2/, its own answer cache):
- chinese_umr-0008: 21.5 vs 20.6 (difference -0.9)
- chinese_umr-0009: 21.1 vs 25.2 (difference 4.1)
- chinese_umr-0010: 21.2 vs 22.3 (difference 1.1)
- chinese_umr-0012: 19.1 vs 20.2 (difference 1.1)
- chinese_umr-0013: 12.7 vs 13.7 (difference 1.0)
- chinese_umr-0014: 21.3 vs 15.8 (difference -5.6)
Mean absolute difference: 2.3 F.
