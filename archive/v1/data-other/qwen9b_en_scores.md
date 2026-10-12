# qwen-en: scores

AnCast++ sentence F and Comprehensive. seed = the document parsed with R0; before = parsed with R(k-1), the skills after the k-1 documents before it (never this one); Δ = before − seed (k = 1 is the seed itself); after = parsed with Rk, after its own round; generate = generate-guidelines with the same model, one call per sentence; detailed = umr-refine's generate prompt (Chinese: with its Chinese UMR section) and document skill, same model. RSI: problems found / edits applied / rejected.

| k | document | version | seed F | before F | Δ F | seed Comp | before Comp | Δ Comp | after F | generate F | detailed F | detailed Comp | RSI problems / applied / rejected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | english_umr-0001 | R0 | 20.0 | 20.0 | - | 19.7 | 19.7 | - | - | 0.0 | 20.3 | 16.9 | 632 / 24 / 1 |
| 2 | english_umr-0002 | R1 | 55.3 | 65.8 | 10.5 | 55.8 | 58.9 | 3.2 | - | 0.0 | 66.8 | 50.4 | 18 / 4 / 2 |
| 3 | english_umr-0003 | R2 | 27.2 | 24.4 | -2.9 | 26.3 | 24.3 | -2.0 | - | 0.0 | 12.0 | 13.3 | 172 / 1 / 0 |
| 4 | english_umr-0005 | R3 | 17.4 | 16.2 | -1.1 | 14.1 | 12.7 | -1.4 | - | 0.0 | 9.6 | 7.3 | 538 / 8 / 0 |
| 5 | english_umr-0009 | R4 | 37.9 | 22.5 | -15.4 | 33.2 | 19.4 | -13.8 | - | 0.0 | 0.0 | 0.0 | 112 / 6 / 2 |
| 6 | english_umr-0004 | R5 | 15.4 | 17.6 | 2.2 | 16.9 | 18.6 | 1.7 | - | 0.0 | 23.0 | 17.6 | 1566 / 6 / 0 |

Predicted graphs AnCast could not match (placeholder concepts, undeclared variables), scored as empty sentences: english_umr-0001 seed: [1, 11, 17, 19, 21]; english_umr-0001 before: [1, 11, 17, 19, 21]; english_umr-0005 before: [1, 23, 24, 27]; english_umr-0004 before: [15, 141]; english_umr-0004 detailed: [2, 5, 11, 12, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27, 30, 32, 38, 40, 41, 42, 47, 51, 53, 54, 55, 56, 63, 68, 69, 70, 71, 72, 73, 74, 77, 78, 80, 81, 83, 85, 86, 89, 90, 95, 98, 99, 103, 106, 107, 110, 114, 116, 117, 122, 125, 126, 127, 130, 131, 133, 135, 137, 139, 141].

Mean Δ F over the 5 documents with both parses (k ≥ 2): -1.3; mean Δ Comp: -2.5.
First half of them: 3.8, second half: -4.7 (does the gain grow as more documents are seen?).

Noise: the seed parsed twice, independently (seed2/, its own answer cache):
- english_umr-0003: 27.2 vs 29.0 (difference 1.8)
- english_umr-0005: 17.4 vs 19.4 (difference 2.0)
- english_umr-0009: 37.9 vs 33.3 (difference -4.6)
Mean absolute difference: 2.8 F.
