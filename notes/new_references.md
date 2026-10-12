# New references for AnnoForge (2026-10-12)

This file goes with `notes/new_references.bib`, which holds 46 new entries. None of the keys collide with `references.bib`, and the file parses cleanly with pybtex. Entries already in `references.bib` and verified in `references_verification.md` were not re-verified. I only cite them here by key.

**Verification tags** (same convention as `references_verification.md`):
- `[ANTH]`: ACL Anthology `.bib`, read with curl.
- `[AX]`: arXiv API record.
- `[PDF]`: I read the full text.
- `[PMLR]`: PMLR v235 index page.
- `[OR]`: OpenReview search-API venue string.
- `[LINDAT]`: LINDAT repository record (citation meta tags).
- `[LDC]`: LDC catalog page.
- `[CR]`: Crossref.
- `[WEB]`: a web-search summary only, which is weaker evidence.

---

## Topic 1. "Kim 2026" and codebooks

**Summary of findings.**
- `kim2026refining` exists in `references.bib` and is correct. It is ACL 2026 main conference, Volume 1 (Long Papers), pp. 37951–37964, `2026.acl-long.1760` [ANTH, already verified]. It refines guideline text, not a codebook.
- I parsed every ACL 2026 Anthology volume (long, short, Findings, SRW, demo, industry). No paper first-authored by a "Kim" is about codebooks.
- The only Kim-authored ACL 2026 annotation paper besides `kim2026refining` is **DiZiNER** (Siun Kim and Hyung-Jin Yoon, ACL 2026 long). It refines instructions by simulating pilot annotation.
- The ACL 2026 paper that is actually about a **given codebook** is **Halterman and Keith** (2026.acl-long.92). "Keith" may have been misremembered as "Kim."
- Check the user's framing. If the cited claim is "LLMs are given a codebook and annotate," the right cite is probably `halterman2026what` (ACL 2026) and/or the existing `halterman2026codebook` (Political Analysis 2026).
- If the claim is "Kim 2026 refines guidelines through pilot annotation or moderation," cite `kim2026refining` and/or `kim2026diziner`.

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `kim2026diziner` | Siun Kim, Hyung-Jin Yoon. DiZiNER: Disagreement-guided Instruction Refinement via Simulating Pilot Annotation for Zero-shot Named Entity Recognition. ACL 2026 (Vol. 1: Long), pp. 17498–17519. doi:10.18653/v1/2026.acl-long.795 | https://aclanthology.org/2026.acl-long.795/ | Closest prior work to RSI-as-moderation. Several LLMs annotate, a supervisor LLM reads their disagreements and refines the task instructions; zero-shot SOTA on 14/18 NER benchmarks. It edits instructions only, not tools or steps, and has no gold-driven loop. | [ANTH] .bib and abstract |
| `halterman2026what` | Andrew Halterman, Katherine A. Keith. What is a protest anyway? Codebook conceptualization is still a first-order concern in LLM-era classification. ACL 2026 (Vol. 1: Long), pp. 2043–2059. doi:10.18653/v1/2026.acl-long.92 | https://aclanthology.org/2026.acl-long.92/ | LLMs silently accept underspecified codebook concepts. Conceptualization failures cause downstream bias that a more accurate LLM cannot fix. Motivates refining the guideline/ontology rather than only the model. | [ANTH] .bib and abstract |
| `gu2026large` | Feng Gu, Zongxia Li, Carlos R. Colon, Benjamin Evans, Ishani Mondal, Jordan Lee Boyd-Graber. Large Language Models Are Effective Human Annotation Assistants, But Not Good Independent Annotators. Findings of ACL 2026, pp. 71–89. doi:10.18653/v1/2026.findings-acl.4 | https://aclanthology.org/2026.findings-acl.4/ | Event annotation workflow: AI-only is far from expert-level, but experts adopt AI-extracted arguments 60% of the time (25% faster). Supports LLM-as-annotator caveats. | [ANTH] .bib and abstract |
| `kim2026how` | Jeongyeon Kim, John Mitchell. How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv:2609.11109, 2026 | https://arxiv.org/abs/2609.11109 | Multi-agent LLM coding with debate and reconciliation. Accuracy depends on **codebook length**, data similarity and agent disagreement. Preprint, not ACL. | [AX] |

Other ACL 2026 annotation papers seen in the volume scan but not added: Goyal et al., "Semantic Span Annotation: An Exploratory Study of LLM Annotation" (ACL 2026 SRW, 2026.acl-srw.39, pp. 438–449, [ANTH] .bib), and Amin et al., "From Fallback to Frontline..." (2026.findings-acl.2124, title only). Add the Goyal SRW paper if you need another ACL 2026 LLM-annotation cite.

---

## Topic 2. Long context and long-instruction following

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `liu2024lost` | Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang. Lost in the Middle: How Language Models Use Long Contexts. TACL 12:157–173, 2024. doi:10.1162/tacl_a_00638 | https://aclanthology.org/2024.tacl-1.9/ | Information in the middle of long contexts is used poorly. This is why one monolithic 100-page guideline prompt is fragile and a stepwise harness with targeted skills helps. | [ANTH] |
| `levy2024same` | Mosh Levy, Alon Jacoby, Yoav Goldberg. Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models. ACL 2024 (Vol. 1), pp. 15339–15353. doi:10.18653/v1/2024.acl-long.818 | https://aclanthology.org/2024.acl-long.818/ | Reasoning degrades as input length grows, even on the same task. | [ANTH] |
| `zhou2023instruction` | Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, Le Hou. Instruction-Following Evaluation for Large Language Models (IFEval). arXiv:2311.07911, 2023 | https://arxiv.org/abs/2311.07911 | The standard instruction-following benchmark, with verifiable instructions. | [AX]; no venue in the arXiv record |
| `jaroslawicz2025how` | Daniel Jaroslawicz, Brendan Whiting, Parth Shah, Karime Maamari. How Many Instructions Can LLMs Follow at Once? arXiv:2507.11538, 2025 | https://arxiv.org/abs/2507.11538 | IFScale: accuracy falls as instruction density grows to 500, and even the best frontier model reaches about 68% at 500 instructions. A dense annotation guideline is exactly this case. | [AX]. Shown as a poster at the NeurIPS 2025 workshop "Evaluating the Evolving LLM Lifecycle" (neurips.cc/virtual/2025/122417); kept as arXiv @misc |
| `wu2025lifbench` | Xiaodong Wu et al. LIFBench: Evaluating the Instruction Following Performance and Stability of Large Language Models in Long-Context Scenarios. ACL 2025 (Vol. 1), pp. 16445–16468. doi:10.18653/v1/2025.acl-long.803 | https://aclanthology.org/2025.acl-long.803/ | Instruction-following in long contexts, tested across input lengths. The user's "LongIFEval" lead turned out to be this paper. | [ANTH]; content from [WEB] |
| `panavas2026handbook` | Liudas Panavas, Sebastian Minus, Bradley Monton, Derek Ray, Suhaas Garre, Sushant Mehta, Edwin Chen. HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following. arXiv:2607.25398, 2026 (accepted to the COLM 2026 Workshop on Agent Behavior) | https://arxiv.org/abs/2607.25398 | Agents governed by a 20–124-page SOP: the best model passes 36.2% of trials, and agents "lose rule details over long horizons." This is a direct analogue of following a long annotation guideline. | [AX] |

I found no paper called "LongIFEval" on arXiv. Its stand-ins are LIFBench and HANDBOOK.md.

---

## Topic 3. Recursive self-improvement

These are already in `references.bib` and need no action: `zelikman2024self` (STOP), `zhang2026darwin` (DGM, ICLR 2026), `hu2025automated` (ADAS), `fernando2024promptbreeder`, `yang2024large` (OPRO), `yuksekgonul2025optimizing` (TextGrad, Nature), `agrawal2026gepa`, `zhang2026agentic` (ACE, ICLR 2026), `lee2026metaharness`, `robeyns2025self`, `zhang2026hyperagents`, `xia2026regularized`, `zhang2026self` and `hebbar2026sia`.

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `yin2025godel` | Xunjian Yin, Xinyi Wang, Liangming Pan, Li Lin, Xiaojun Wan, William Yang Wang. Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement. ACL 2025 (Vol. 1), pp. 27890–27913. doi:10.18653/v1/2025.acl-long.1354 | https://aclanthology.org/2025.acl-long.1354/ | An LLM agent that rewrites its own logic, guided only by high-level objectives. This is RSI in an ACL venue. The published title says "Recursively"; the arXiv v1 title says "Recursive." | [ANTH]; arXiv:2410.04444 |
| `novikov2025alphaevolve` | Alexander Novikov et al. (18 authors). AlphaEvolve: A coding agent for scientific and algorithmic discovery. arXiv:2506.13131, 2025 | https://arxiv.org/abs/2506.13131 | Evolutionary LLM code improvement with automatic evaluators. A propose-evaluate-select loop, like ours with gold F1 as the evaluator. | [AX] |
| `schmidhuber2003goedel` | Jürgen Schmidhuber. Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements. arXiv:cs/0309048, 2003 | https://arxiv.org/abs/cs/0309048 | The classical origin of RSI, which Gödel Agent and DGM both build on. The arXiv journal_ref lists variants in LNCS 3394 (2005) and ICANN 2005. | [AX] |
| `guo2024connecting` | Qingyan Guo et al. Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers (EvoPrompt). ICLR 2024 | https://arxiv.org/abs/2309.08532 | Evolutionary prompt optimization. Optional; Promptbreeder and GEPA already cover this. | [OR] "ICLR 2024 poster"; [AX] |

---

## Topic 4. Harness, tools and workflow optimization

These are already in `references.bib`: `anthropic2026agent` and `zhang2025equipping` (Agent Skills), `wang2025agent` (AWM), `zheng2025skillweaver`, `qian2023creator`, `cai2024large` (LATM), `wolflein2025llm` (ToolMaker), `zhang2025aflow`, `khattab2024dspy`, `lin2026agentic` and `wang2024voyager`.

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `yuan2024craft` | Lifan Yuan, Yangyi Chen, Xingyao Wang, Yi R. Fung, Hao Peng, Heng Ji. CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets. ICLR 2024 | https://arxiv.org/abs/2309.17428 | LLM-created, verified, reusable toolsets that are retrieved at inference. Analogous to AnnoForge's induced tools. | [AX] comment "Accepted to ICLR 2024"; [OR] "ICLR 2024 poster" |
| `wang2024trove` | Zhiruo Wang, Graham Neubig, Daniel Fried. TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks. ICML 2024, PMLR 235:51177–51191 | https://proceedings.mlr.press/v235/wang24az.html | Grows, verifies and trims a function toolbox, which is close to harness-tool curation. PMLR gives the author order Wang, Neubig, Fried (arXiv v1 lists Fried second). | [PMLR]; [AX] 2401.12869 |
| `zhuge2024gptswarm` | Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, Jürgen Schmidhuber. GPTSwarm: Language Agents as Optimizable Graphs. ICML 2024, PMLR 235:62743–62767 | https://proceedings.mlr.press/v235/zhuge24a.html | Optimizes both node prompts and graph connectivity of agent workflows. This is "steps" optimization. | [PMLR] |
| `cheng2024trace` | Ching-An Cheng, Allen Nie, Adith Swaminathan. Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs. NeurIPS 2024 | https://arxiv.org/abs/2406.16218 | Optimizes whole programs and workflows from execution traces plus feedback. Generalizes TextGrad to code/harness parameters. | [OR] "NeurIPS 2024 poster"; [AX] |

---

## Topic 5. LLM-as-annotator and LLM AMR/UMR parsing

These are already in `references.bib`: `gilardi2023chatgpt`, `he2024annollm`, `tan2024large`, `ziems2024can`, `ettinger2023you`, `sun2024chinese`, `chun2024pipeline`, `markle2026setup`, `bonn2024building`, `wein2025can` and `markle2025generating`.

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `wang2021want` | Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu, Michael Zeng. Want To Reduce Labeling Cost? GPT-3 Can Help. Findings of EMNLP 2021, pp. 4195–4205. doi:10.18653/v1/2021.findings-emnlp.354 | https://aclanthology.org/2021.findings-emnlp.354/ | The canonical early LLM-as-labeler paper. | [ANTH] |
| `wei2024llms` | Kangda Wei, Aayush Gautam, Ruihong Huang. Are LLMs Good Annotators for Discourse-level Event Relation Extraction? Findings of EMNLP 2024, pp. 1–19. doi:10.18653/v1/2024.findings-emnlp.1 | https://aclanthology.org/2024.findings-emnlp.1/ | LLMs underperform supervised baselines on document-level coreference, temporal, causal and subevent relations. They fail on transitivity and long-distance relations and fabricate event mentions. Directly relevant to TimeML TLINKs and the UMR document level. | [ANTH]; findings from [WEB] summary of the abstract |
| `barta2025enhancing` | Botond Barta, Endre Hamerlik, Milán Nyist, Masato Ito, Judit Acs. Enhancing AMR Parsing with Group Relative Policy Optimization. XLLM 2025, pp. 99–105. doi:10.18653/v1/2025.xllm-1.11 | https://aclanthology.org/2025.xllm-1.11/ | Fine-tuned Llama-3.2-1B plus GRPO gives a strong AMR parser. This is the fine-tuning alternative to harness bootstrapping. | [ANTH]; content from [WEB] |
| `lee2023amr` | Young-Suk Lee, Ramón Fernandez Astudillo, Radu Florian, Tahira Naseem, Salim Roukos. AMR Parsing with Instruction Fine-tuned Pre-trained Language Models. arXiv:2304.12272, 2023 | https://arxiv.org/abs/2304.12272 | FLAN-T5 fine-tuned for AMR reports SOTA on AMR 2.0/3.0/BioAMR. Fine-tuning needs large gold data, which UMR lacks. | [AX]; no venue in the record |
| `ho2025evaluation` | Shu Han Ho. Evaluation of Finetuned LLMs in AMR Parsing. arXiv:2508.05028, 2025 | https://arxiv.org/abs/2508.05028 | Fine-tuned LLaMA-3.2 reaches Smatch 0.804 on AMR 3.0. Optional, preprint. | [AX] |

I found no 2025–2026 paper on *prompting* or *agentic* (non-fine-tuned) full UMR parsing. The 2026 UMR parsers are SETUP (`markle2026setup`) and the two DMR 2026 shared-task systems (Topic 7). Both shared-task systems are fine-tuned models: Orange uses mT5/Flan-T5 plus Qwen3-8B, and Sema uses a LoRA-tuned Qwen3-4B.

**Correction for `markle2026setup`.** The existing entry in `references.bib` has `booktitle = {Proceedings of LREC 2026}` and no pages. The Anthology record [ANTH] is:
```bibtex
@inproceedings{markle2026setup,
  title = {{SETUP}: Sentence-level {English}-To-Uniform Meaning Representation Parser},
  author = {Markle, Emma and Gutierrez Bach, Javier and Wein, Shira},
  booktitle = {Proceedings of the Fifteenth Language Resources and Evaluation Conference},
  month = may, year = {2026}, address = {Palma de Mallorca, Spain},
  publisher = {ELRA Language Resource Association}, pages = {9710--9721},
  doi = {10.63317/3mhzy8cuhkaw}, url = {https://aclanthology.org/2026.lrec-1.762/}
}
```
I did not change `references.bib`; replace the entry there if you want this version.

---

## Topic 6. TimeML / TempEval

These are already in `references.bib`: `pustejovsky2003timeml`, `uzzaman2013semeval`, `strotgen2010heideltime`, `yuan2023zero` and `gautam2024discourse`.

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `sauri2006timeml` | Roser Saurí, Jessica Littman, Bob Knippen, Robert Gaizauskas, Andrea Setzer, James Pustejovsky. TimeML Annotation Guidelines, Version 1.2.1. January 31, 2006 | https://timeml.github.io/site/publications/timeMLdocs/annguide_1.2.1.pdf | The actual guideline AnnoForge consumes for TimeML. | [PDF] title page read. It is @misc because the title page names no institution or report number. A ResearchGate copy lists Jessica Moszkowicz as an extra author [WEB]; I followed the PDF title page. |
| `pustejovsky2006timebank` | James Pustejovsky, Marc Verhagen, Roser Saurí, Jessica Littman, Robert Gaizauskas, Graham Katz, Inderjeet Mani, Robert Knippen, Andrea Setzer. TimeBank 1.2. LDC2006T08. Linguistic Data Consortium, 2006. doi:10.35111/09b1-5n19 | https://catalog.ldc.upenn.edu/LDC2006T08 | Corpus: 183 English news articles annotated under TimeML 1.2.1. | [LDC] catalog page (authors, DOI and the TimeML 1.2.1 statement) |
| `verhagen2007semeval` | Marc Verhagen, Robert Gaizauskas, Frank Schilder, Mark Hepple, Graham Katz, James Pustejovsky. SemEval-2007 Task 15: TempEval Temporal Relation Identification. SemEval-2007, pp. 75–80 | https://aclanthology.org/S07-1014/ | TempEval-1 (TLINK subtasks A/B/C). | [ANTH] |
| `verhagen2010semeval` | Marc Verhagen, Roser Saurí, Tommaso Caselli, James Pustejovsky. SemEval-2010 Task 13: TempEval-2. SemEval 2010, pp. 57–62 | https://aclanthology.org/S10-1010/ | TempEval-2: fine-grained TLINK subtasks (event–timex, event–DCT, main events, subordinate events). | [ANTH] |
| `pustejovsky2010iso` | James Pustejovsky, Kiyong Lee, Harry Bunt, Laurent Romary. ISO-TimeML: An International Standard for Semantic Annotation. LREC 2010 | https://aclanthology.org/L10-1027/ | The ISO standardization of TimeML. Pages are not in the Anthology .bib; a Tilburg repository lists pp. 394–397 [WEB], which I left out of the .bib. | [ANTH] |
| `uzzaman2011temporal` | Naushad UzZaman, James Allen. Temporal Evaluation. ACL-HLT 2011 (short), pp. 351–356 | https://aclanthology.org/P11-2061/ | The temporal-closure-based "temporal awareness" metric used for TempEval-3 TLINK scoring. | [ANTH] |
| `bethard2013cleartk` | Steven Bethard. ClearTK-TimeML: A minimalist approach to TempEval 2013. SemEval 2013, pp. 10–14 | https://aclanthology.org/S13-2002/ | Best TempEval-3 participant on Task ABC (end-to-end TLINK) and Task C. | [ANTH]; scores [PDF] of S13-2001 |
| `laokulrat2013uttime` | Natsuda Laokulrat, Makoto Miwa, Yoshimasa Tsuruoka, Takashi Chikayama. UTTime: Temporal Relation Classification using Deep Syntactic Features. SemEval 2013, pp. 88–92 | https://aclanthology.org/S13-2015/ | Best on TempEval-3 "Task C – relation only." | [ANTH]; scores [PDF] |
| `jung2013att1` | Hyuckchul Jung, Amanda Stent. ATT1: Temporal Annotation Using Big Windows and Rich Syntactic and Semantic Features. SemEval 2013, pp. 20–24 | https://aclanthology.org/S13-2004/ | Best TempEval-3 participant on event extraction (Task B). | [ANTH]; scores [PDF] |
| `strotgen2013heideltime` | Jannik Strötgen, Julian Zell, Michael Gertz. HeidelTime: Tuning English and Developing Spanish Resources for TempEval-3. SemEval 2013, pp. 15–19 | https://aclanthology.org/S13-2003/ | Best TempEval-3 participant on TIMEX value (Task A). | [ANTH]; scores [PDF] |
| `chan2024exploring` | Chunkit Chan, Cheng Jiayang, Weiqi Wang, Yuxin Jiang, Tianqing Fang, Xin Liu, Yangqiu Song. Exploring the Potential of ChatGPT on Sentence Level Relations: A Focus on Temporal, Causal, and Discourse Relations. Findings of EACL 2024, pp. 684–721. doi:10.18653/v1/2024.findings-eacl.47 | https://aclanthology.org/2024.findings-eacl.47/ | ChatGPT is good at causal relations but weak at temporal ordering. It covers temporal relation datasets; I did not check which ones. | [ANTH]; content [WEB] |

**TempEval-3 best participant scores (English, platinum test).** These are copied from the S13-2001 PDF tables [PDF]:
- **Task A, timex value F1:** HeidelTime-t 77.61 (timex extraction relaxed F1 90.30). NavyTime-1,2 have the highest relaxed F1, 90.32.
- **Task B, event extraction:** ATT-1 event F1 81.05, class F1 71.88.
- **Task ABC, end-to-end TLINK temporal-awareness F1** (Table 7): ClearTK-2 30.98 (P 34.08, R 28.40), then ClearTK-1 29.77 and NavyTime-1 27.28. TIPSem (the TE2 system, listed separately because it was used for pre-labelling) scores 42.39.
- **Task C, TLINK identification and classification given gold entities** (Table 8): ClearTK-2 36.26 (P 37.32, R 35.25).
- **Task C, relation only** (Table 9): UTTime-1,4 56.45.

---

## Topic 7. UMR Parsing Shared Task at DMR 2026 (important)

**Primary sources.**
- I read the full overview PDF (2026.dmr-1.12) and both system papers (2026.dmr-1.13 and .14) [PDF].
- I parsed the official results page, https://ufal.mff.cuni.cz/umr-parsing/results.
- I read the task page https://ufal.mff.cuni.cz/umr-parsing and the umrtools README (github.com/ufal/umrtools, cloned).
- I read the LINDAT UMR 2.2 record [LINDAT].
- The DMR 2026 proceedings, "Proceedings of The Seventh International Workshop on Designing Meaning Representations (DMR 2026) @ LREC 2026," were edited by Jin Zhao, Claire Benet Post and Elizabeth Hoefer and published by ELRA. The workshop was held in Palma, Mallorca on 11 May 2026: https://aclanthology.org/volumes/2026.dmr-1/

| key | citation | URL | verified |
|---|---|---|---|
| `stepanek2026first` | Jan Štěpánek, Daniel Zeman, Markéta Lopatková, Federica Gamba, Hana Hledíková, Nianwen Xue. First Shared Task on UMR Parsing. DMR 2026 @ LREC 2026, pp. 136–147. doi:10.63317/3taoes4u6cmk | https://aclanthology.org/2026.dmr-1.12/ | [ANTH], [PDF] |
| `heinecke2026orange` | Johannes Heinecke, Munshi Asadullah. Orange @ UMR Parsing Shared Task. DMR 2026, pp. 148–154. doi:10.63317/2hztcweytj89 | https://aclanthology.org/2026.dmr-1.13/ | [ANTH], [PDF] |
| `devergnette2026sema` | Rémi de Vergnette, Maxime Amblard. Sema System for the DMR 2026 Shared Task: Multistage UMR Parsing with Qwen3-4B. DMR 2026, pp. 155–159. doi:10.63317/24cughzsw4ae | https://aclanthology.org/2026.dmr-1.14/ | [ANTH], [PDF] |
| `zeman2026word` | Daniel Zeman, Federica Gamba. Word Alignment-Based Evaluation of Uniform Meaning Representations. arXiv:2603.26401, 2026 | https://arxiv.org/abs/2603.26401 | [AX], [PDF] |
| `bonn2026uniform` | Julia Bonn, Claire Bonial, Matt Buchholz, et al. (60 authors). Uniform Meaning Representation 2.2. LINDAT/CLARIAH-CZ, published 2026-04-01 (publisher: UMR Consortium) | http://hdl.handle.net/11234/1-6132 | [LINDAT] |
| `bonn2025uniform` | Julia Bonn et al. Uniform Meaning Representation 2.0. LINDAT/CLARIAH-CZ, 2025-05-17 | http://hdl.handle.net/11234/1-5902 | [LINDAT] (title, first author and date only) |

**Task setup** (overview, Sections 2–4):
- **Languages.** There are 7 test languages: Arapaho, Chinese, Czech, English, Italian, Latin and Navajo. Italian has no training data, so it is zero-shot. Training data comes in "clean" and "dirty" splits, and Latin has no clean data.
- **English test set.** 5 files, 195 sentences, 4,092 tokens. One file, `en-0000`, is the 100-sentence PUD file, which uses Stage-0 roles and lacks document-level relations. The other four come from UMR 2.0: `en-0005`, `en-0006`, `en-0007`, `en-0008`. The overview notes that `en-0005` and `en-0007` contain identical sentences with non-identical gold annotation (about 82% similarity).
- **Chinese test set.** 15 files, 236 sentences, 6,467 tokens: 5 documents from UMR 2.0 plus 10 new Wikinews documents. The new documents were pre-annotated with the LLM-based parser of Sun et al. (2024) and then corrected by hand.
- **System input.** Systems receive tokenized, sentence-segmented raw text. They must output sentence graphs, node–token alignment and document-level relations in the `.umr` format. Earlier UMR releases were banned as training data because they overlap the test set.
- **Participation.** Twelve people registered and there were **2 submissions**: "orange" (Orange Research) and "sema" (LORIA). **The overview reports no official baseline system.**

**Metric.**
- The main metric is **juːmæʧ** (Zeman and Gamba 2026), an F1 over triples:
  - parent–relation–child, including document-level relations;
  - node–attribute–value, where node–concept counts as an attribute.
- Node mapping is driven by node–token alignment. Unaligned nodes are matched by concept identity, and nodes on both sides are reduced to a one-to-one mapping (the overview calls this symmetrization).
- The implementation is `compare_umr.pl` in github.com/ufal/umrtools; the README says it gives the "juːmæʧ F₁ score." The task page gives the call `perl compare_umr.pl GOLD gold.umr SYS sys.umr --quiet`. So "compare_umr.pl triple F1" and "juːmæʧ" are the same thing.
- Smatch is also reported, sentence-level only.
- Scores are **macro-averaged over languages** (overview footnote 14). Within a language, umrtools ships `micro_average.pl` ("counts summed up and P, R, F1 computed over sums"). Orange's per-file English scores average about 27.1, while its English language score is 22.19, which fits micro-averaging within a language. This within-language aggregation is my **inference** and is not stated in the overview.
- The submission and evaluation server stays open: https://ufal.mff.cuni.cz/umr-parsing/submission

**Official results, main juːmæʧ F1** (overview Table 2; identical to the results page, which gives full precision):

| Language | Orange | Sema |
|---|---|---|
| Arapaho | 0.0815 | 0.1115 |
| **Chinese** | **0.3651** (page: 0.365076703831) | 0.2585 (page: 0.258490958220744) |
| Czech | 0.1587 | 0.2652 |
| **English** | **0.2219** (page: 0.221921322690992) | 0.1919 (page: 0.191896351524782) |
| Italian | 0.1394 | 0.2137 |
| Latin | 0.1724 | 0.1918 |
| Navajo | 0.2155 | 0.1273 |
| Average (macro) | 0.1935 | **0.1943** |

**Who is best.**
- Sema wins the overall macro average by 0.0008 (0.1943 vs 0.1935; Orange's paper calls this "0.08 points behind").
- **Orange is best on both English (0.2219) and Chinese (0.3651)**. The best English and Chinese scores in the shared task are therefore Orange's.
- I found no stronger published system on this test set, so these are the current published SOTA on this benchmark as of today.

**Other tables in the overview, English and Chinese only:**

| Metric (overview table) | EN Orange | EN Sema | ZH Orange | ZH Sema |
|---|---|---|---|---|
| Smatch, sentence-level (T5) | 0.4625 | 0.4169 | 0.5194 | 0.4363 |
| juːmæʧ, no doc-level, with top (T6) | 0.2509 | 0.2057 | 0.3777 | 0.2471 |
| juːmæʧ, non-PUD files only (T4) | 0.2734 | 0.2146 | 0.3651 | 0.2585 |
| juːmæʧ, PUD file only (T3) | 0.1590 | 0.1641 | n/a | n/a |
| Aligned-token-set F1 (T7) | 0.7148 | 0.6457 | 0.7074 | 0.6122 |
| Mapped-node F1 (T8) | 0.5643 | 0.4856 | 0.6046 | 0.4521 |
| juːmæʧ, mapped governors only (T9) | 0.4198 | 0.4071 | 0.5965 | 0.5208 |
| Concept juːmæʧ (T10) | 0.3866 | 0.2957 | 0.5287 | 0.3503 |
| :ARGN / :ARGN-of (T11) | 0.1490 | 0.0777 | 0.2270 | 0.1369 |
| :aspect (T12) | 0.0031 | 0.3072 | 0.2828 | 0.3153 |
| Doc-level modal (T13) | 0.0000 | 0.1386 | 0.4261 | 0.4634 |
| :modal-strength (T14) | 0.0000 | 0.0195 | n/a | n/a |

- Document-level **coreference was 0 for both systems in every language**.
- The only non-zero document-level **temporal** score is Orange on Chinese, F1 = 0.0911.
- In other words, neither system really produces UMR's document level. This is the gap a guideline-driven harness could fill.

**Per-document scores.**
- Orange's paper (Table 7) gives per-file juːmæʧ F1:
  - English: en-0000 (PUD) 15.90, en-0005 24.34, en-0006 29.97, en-0007 24.18, en-0008 41.09.
  - Chinese: zh-0021 25.31, zh-0022 28.61, zh-0023 40.29, zh-0024 35.36, zh-0026 33.32, zh-0027 35.72, zh-0028 34.79, zh-0029 41.47, zh-0030 35.99, zh-0031 41.67, zh-0032 29.44, zh-0033 48.21, zh-0034 39.39, zh-0035 45.54, zh-0036 29.68.
  - Its per-file average is 27.49%.
- Sema reports no per-file scores.

**System outputs released.**
- **Yes.** The UMR 2.2 release (http://hdl.handle.net/11234/1-6132) is described as "New version of UMR data used in the First Shared Task on UMR Parsing (including submitted systems' outputs)."
- The file listing includes `system-outputs/orange/*.umr` (for example en-0006.umr, zh-0028.umr) and a matching sema folder.
- Together with the gold test files, this lets you re-score both systems per document with `compare_umr.pl`. I did not download the archive (license-gated LINDAT download).

**System summaries.**
- **Orange:** a two-step pipeline. A monolingual mT5/Flan-T5 or multilingual mT5 model is picked per language on dev data and predicts the intra-sentence graph plus intra-sentence document-level relations. A fine-tuned Qwen3-8B handles inter-sentence relations over sentence pairs at most 6 apart. Alignment is heuristic (UDParse lemma-to-concept). It used no AMR 3.0 data.
- **Sema:** LoRA fine-tuning of Qwen3-4B in 3 stages: capped dirty data (≤2000 per language), then clean data with document-level annotation, then a word-to-node alignment stage. Beam size 4, followed by rule-based PENMAN repair.

**Related UMR item** (Topic 9 too):
- `gamba2025bootstrapping`: Federica Gamba, Alexis Palmer, Daniel Zeman. Bootstrapping UMRs from Universal Dependencies for Scalable Multilingual Annotation. LAW-XIX 2025, pp. 126–136. doi:10.18653/v1/2025.law-1.10. https://aclanthology.org/2025.law-1.10/ [ANTH].
- It builds partial UMR graphs from UD trees as an annotation starting point, and it is the UD-to-UMR converter used by SETUP and in building the PUD test data.

---

## Topic 8. Moderation and adjudication in annotation projects

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `pustejovsky2012natural` | James Pustejovsky, Amber Stubbs. Natural Language Annotation for Machine Learning: A Guide to Corpus-Building for Applications. O'Reilly Media, 2012. ISBN 978-1-4493-0666-3 | https://www.oreilly.com/library/view/natural-language-annotation/9781449332693/ | The MATTER cycle (Model, Annotate, Train, Test, Evaluate, Revise) with guideline revision and adjudication. RSI is a machine-run MATTER/MAMA loop. | [WEB] only (O'Reilly pages return 403). Title, subtitle, ISBN and the MATTER expansion come from bookseller and catalog snippets. The release date is Oct–Dec 2012, but one library record says [2013]; I used 2012, the year usually cited. |
| `artstein2008survey` | Ron Artstein, Massimo Poesio. Survey Article: Inter-Coder Agreement for Computational Linguistics. Computational Linguistics 34(4):555–596, 2008. doi:10.1162/coli.07-034-R2 | https://aclanthology.org/J08-4004/ | The standard reference for agreement and reliability in annotation projects. | [ANTH] |
| `ide2017handbook` | Nancy Ide, James Pustejovsky (eds.). Handbook of Linguistic Annotation. Springer Netherlands, 2017. doi:10.1007/978-94-024-0881-2 | https://doi.org/10.1007/978-94-024-0881-2 | General reference on annotation-project lifecycle and scheme design (includes TimeML/ISO chapters; I did not check the table of contents). | [CR] |

`kim2026refining` and `kim2026diziner` both explicitly frame LLM guideline/instruction refinement as simulating the "moderation" or "pilot annotation" phase of an annotation project. Cite them next to MATTER.

---

## Topic 9. Bootstrapping complex annotation; structured prediction with code or guidelines

These are already in `references.bib`: `sainz2024gollie`, `pang2023guideline`, `delafuente2025guidex`, `srivastava2025instruction`, `huang2025guidener` and `sun2024chinese` (LLM-drafted Chinese UMR).

| key | citation | URL | supports | verified |
|---|---|---|---|---|
| `gamba2025bootstrapping` | see Topic 7 | https://aclanthology.org/2025.law-1.10/ | Rule-based bootstrapping of UMR from UD, which is the non-LLM bootstrapping baseline. | [ANTH] |
| `wang2023code4struct` | Xingyao Wang, Sha Li, Heng Ji. Code4Struct: Code Generation for Few-Shot Event Structure Prediction. ACL 2023 (Vol. 1), pp. 3640–3663. doi:10.18653/v1/2023.acl-long.202 | https://aclanthology.org/2023.acl-long.202/ | Represents an event ontology as code classes for few-shot structured prediction. A precursor of GoLLIE, and relevant to our ontology-as-code tools. | [ANTH]; content [WEB] |
| `kim2024meganno` | Hannah Kim, Kushan Mitra, Rafael Li Chen, Sajjadur Rahman, Dan Zhang. MEGAnno+: A Human-LLM Collaborative Annotation System. EACL 2024 System Demonstrations, pp. 168–176. doi:10.18653/v1/2024.eacl-demo.18 | https://aclanthology.org/2024.eacl-demo.18/ | Human-verified LLM annotation tooling. This is also a "Kim" annotation paper (2024, not 2026). | [ANTH] |

---

## Unverified or not added (not in the .bib)

1. **A separate "Kim et al. 2026, ACL" paper on codebooks:** not found in any ACL 2026 Anthology volume (Topic 1).
2. **"LongIFEval":** no paper by that name found on arXiv. LIFBench and HANDBOOK.md are used instead.
3. **Pustejovsky et al. 2003, "The TIMEBANK corpus"** (Corpus Linguistics 2003): the ucrel PDF URL now returns 404, so it is not verified. TimeBank 1.2 is cited through LDC instead.
4. **An official baseline for the DMR 2026 UMR shared task:** none is reported in the overview, the system papers or the results page.
5. **UMR 2.2 full contents:** the system-output folder names were seen in the LINDAT file listing. I did not download or open the archive.
6. **Within-language averaging in the shared task:** micro-averaging is inferred from `micro_average.pl` and Orange's numbers, not stated in the overview.
7. **Content summaries tagged [WEB]** (LIFBench, Wei et al. 2024, Barta et al. 2025, Chan et al. 2024, Code4Struct, the Pustejovsky and Stubbs MATTER expansion): the bibliographic data is verified, but the one-line content claims come from search summaries of abstracts.
8. **Goyal et al. 2026 (ACL SRW) "Semantic Span Annotation: An Exploratory Study of LLM Annotation":** the .bib was verified [ANTH], but I did not add it because I did not read the abstract.
