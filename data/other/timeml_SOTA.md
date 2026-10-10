# TempEval-3 published results (literature check)

Collected by a research subagent that opened each paper or page and read the number in it; I did not re-read the
papers myself. The 2013 shared-task systems are not listed here: their outputs are in the TempEval-3 data, and
`sota2013.py` rescored them with our scorer (`sota2013.json`), reproducing the published numbers.

Every number was read in the PDF. Test set is TE3 platinum (20 docs, 138 timex) unless stated. Only timex results improved after 2013. I found no verified post-2013 event-extraction or end-to-end (ABC) TLINK result beating TIPSem on platinum, and no LLM result on TE3 events or TLINKs. ACL = aclanthology.org.

| System, year, venue | Task / metric | Number | Source and location | Verified |
|---|---|---|---|---|
| UWTime, 2014 ACL | timex e2e strict/relaxed/type/value F1; gold-span value acc | 83.1/91.4/85.4/82.4; 82.6 | ACL/P14-1135, Fig 4, 6 (HeidelTime row matches your official numbers) | yes |
| SynTime-I/E, 2017 ACL | extent strict/relaxed F1 | 92.09/94.96; 92.47/94.62 | ACL/P17-1039, Tab 4 | yes, caveat A |
| TOMN, 2018 WWW | extent strict/relaxed | 91.58/94.51 | Zhong NTU thesis Tab 5.2 (dr.ntu.edu.sg/server/api/core/bitstreams/1a0d4d5e-aefc-4712-99f2-e7ce4f05f892/content) | yes, via thesis |
| PTime, 2019 AAAI | extent strict/relaxed | 84.25/91.58 | ojs.aaai.org/index.php/AAAI/article/view/4595, Tab 3 | yes |
| ARTime + SynTime tagger, 2021 Findings EMNLP | e2e type F1 / value F1 | 90.1/81.3 | arxiv.org/abs/2108.13658, Tab 5 | yes |
| Escribano et al., 2023 arXiv | relaxed F1 / relaxed value F1 | 93.48/76.81 (XTN-D); 91.73/79.70 (XTN-N) | arxiv.org/abs/2304.14221, Tab 4 (own evaluator) | yes |
| tieval, 2023 SIGIR | HeidelTime F1; event baseline F1; CogCompTime2 TLINK F1 (TF1) | 81.8; 77.5; 39.7 (39.3) | arxiv.org/abs/2301.04643, Tab 2 | yes, caveat B |
| GATE-Time, 2016 LREC | event strict/class F1 | 75.9/62.2 | ACL/L16-1587, Tab 3 | yes |
| CATENA, 2016 COLING | TLINK Task C (gold entities) / relation-only, awareness F1 | .402/.619 (UTTime .565) | ACL/C16-1007, Tab 2 | yes |
| Ning et al., 2017 EMNLP | relation-only (gold E-E pairs) / Task C (gold events), awareness F1 | 67.2 (UTTime 56.5) / 40.3 (ClearTK 35.1) | ACL/D17-1108, Tab 3, 4 | yes, caveat C |

A: SynTime's table labels its data "TimeBank" (183 docs), but its baselines are platinum numbers and its recalls are multiples of 1/138; the thesis (Sec 4.4.1) says test = TE3-Platinum. Extent only. B: tieval re-implements the metrics (HeidelTime 81.8, not official 81.34); so does TEI2GO (CIKM 2023, arxiv.org/abs/2403.16804, Tab 3: strict/relaxed 82.4/90.6, no gain). C: E-T links come from a local classifier; CoDL+ILP uses unlabeled TE3-Silver; Task C is gold entities, not ABC.

Not comparable: Laparra 2018 (ACL/Q18-1025) uses a new interval metric on SCATE annotations. CogCompTime (ACL/D18-2013) scores against MATRES re-annotation and says its numbers are not comparable. Chrono (ACL/S18-1012): nothing on TE3. "BERT got a Date" (arXiv 2109.14927) was withdrawn as unreliable.

LLMs:

| Model, setting | Source | Task / metric | Number | Comparable? |
|---|---|---|---|---|
| GPT-3.5-turbo, few-shot (up to 15 retrieved examples) | Gautam et al., NAACL 2024 short, ACL/2024.naacl-short.27, Tab 1 | timex normalization, gold spans, "TempEval3" accuracy | 72.6 best; 18.2 guideline prompt; fine-tuned MLM 79.0; end-to-end (Tab 2) 52.1/40.5 vs HeidelTime 84.1/80.0 | Gold-span part is the same kind as UWTime's 82.6, not value F1; split not stated; end-to-end metric undefined |
| ChatGPT zero-shot (ZS/ranking/CoT) | Yuan et al., BioNLP 2023, arxiv.org/abs/2304.05454, Tab 2 | MATRES / TB-Dense F1 | 25.3/19.3/52.4; 17.8/36.6/37.0 | No |
| GPT-4o, DeepSeek-R1 zero-shot CoT | Eirew et al., EMNLP 2025, ACL/2025.emnlp-main.1601, Tab 2 | MATRES / TB-Dense F1 | 56.6/42.8; 70.3/50.8 | No |
| Llama2-70B, GPT-3.5 few-shot | Roccabruna et al., arxiv.org/abs/2410.10476, Tab 2 | micro-F1, VAGUE removed | 65.3/31.4; 61.2/12 | No |

Item 3. Supervised MATRES is about 82-84 F1 (SCS-EERE 83.4, via MulCo Tab 7, Tan et al. 82.7); TB-Dense about 65-70 (Tan et al. 65.0; DTRE 70.2, via Yuan Tab 2). MulCo (arxiv.org/abs/2209.00568) claims 90.4/85.6 but flags a non-standard F1 (Appendix A.2, unread). Best LLM: zero-shot DeepSeek-R1 CoT, 70.3 MATRES / 50.8 TB-Dense; best few-shot is Roccabruna's non-standard 65.3.

Could not verify:
- Any post-2013 event-class or ABC TLINK result with the official scorer.
- Any prompted LLM on TE3 events, TLINKs or extent extraction.
- TOMN's WWW paper itself (read via thesis); Escribano's strict F1 (88.28, prose only, ambiguous).
- Whether Gautam's split is platinum, or whether tieval matches the official scorer.
- ECAI 2024 LLM normalization paper (403 from publisher).
- Supervised TB-Dense/MATRES figures are second-hand.

(All downloaded PDFs and text extractions are in /tmp/claude-0/-home-user-SkillParseUMR/9a21e0b7-096b-5e31-aa3e-ef9c4342f133/scratchpad/lit/. Nothing outside that folder was touched, and no git commands were run.)
