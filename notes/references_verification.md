# Verified bibliography for the annotation-harness related-work section

**Verification tags.**
- `[AX]` means I read the arXiv API record (export.arxiv.org) for the arxiv.org/abs/<id> page. It gives title, authors, date, comment and abstract.
- `[ANTH]` means I read the ACL Anthology page or its .bib file.
- `[CR]` means I read the Crossref record for the DOI.
- `[OR]` means I read the OpenReview search-API metadata for the venue string. OpenReview forum pages return a bot challenge, so I could not open the pages themselves.
- `[PDF]` means I read the full text.

**Key rule.** Keys are firstauthorlastname + year + first title word (a leading article is dropped). The year is the venue year where a venue exists. Items with no venue are `@misc` with an arXiv eprint.

**Corrections to your descriptions.**
- **Wang/Qu/Ye (arXiv 2411.05050)** is titled "Selecting Between BERT and GPT for Text Classification in Political Science Research." Manifesto classification (8-class, GPT-4o) is one of several tasks, and the data comes from Laurer et al. (see F).
- **MIPROv2.** The Opsahl-Ong paper's abstract calls the algorithm "MIPRO"; I saw no "MIPROv2" in the abstract.
- **DSPy.** The ICLR 2024 record is titled "...into State-of-the-Art Pipelines." The arXiv v1 title says "...Self-Improving Pipelines."
- **TextGrad.** The Nature version is titled "Optimizing generative AI by backpropagating language model feedback."
- **AnCast.** It has two authors (Sun and Xue), not "Sun et al."
- **TempEval-3.** The arXiv proposal-stage paper and the SemEval paper have different titles and author orders. I cite the Anthology version.

---

## A. LLM-assisted refinement of annotation guidelines / codebooks

### A1. "Refining and Reusing Annotation Guidelines for LLM Annotation" (ACL 2026 main, long)
```bibtex
@inproceedings{kim2026refining,
  title = {Refining and Reusing Annotation Guidelines for {LLM} Annotation},
  author = {Kim, Kon Woo and Kim, Jin-Dong and Aizawa, Akiko},
  booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month = jul, year = {2026}, address = {San Diego, California, United States},
  publisher = {Association for Computational Linguistics}, pages = {37951--37964},
  doi = {10.18653/v1/2026.acl-long.1760}, url = {https://aclanthology.org/2026.acl-long.1760/},
  note = {arXiv:2605.20809}
}
```
- **What it does:** It proposes an iterative "moderation" framework that simulates the early phases of an annotation project, to align LLM annotators with gold-benchmark conventions (abstract). It is tested on biomedical NER: NCBI Disease, BC5CDR and BioRED, with GPT, Gemini and DeepSeek.
- **What it edits [PDF]:**
  - **Guideline text only.** It inserts or rewrites rules inside the existing human-written guideline document, and the model re-emits the full guideline. It does not change tools, code, pipeline structure or the chain of calls.
  - **Loop.** An LLM annotates a dev set, and strict span+type F1 is computed against gold. The most frequent discrepancy group is chosen (label mismatch, boundary mismatch, FN, FP). Three LLM steps follow: pattern explanation, then an IF/THEN/EXCEPT principle, then a guideline rewrite.
  - **Stopping and checks.** The loop stops at a threshold or when a refinement does not improve the score, and that last refinement is discarded. Verified true positives are put in the prompt as "don't flip these" checks.
  - **Supervision and leakage.** Refinement uses only 10 documents sampled from the training split. Evaluation is on a distinct 100-document dev set. The original test sets are withheld "to preserve their integrity."
  - **Code.** The authors' code is at github.com/KonWooKim/llm-guideline-moderation. I saw the link in the PDF but did not open the repository.
- VERIFIED: https://aclanthology.org/2026.acl-long.1760/ [ANTH]; https://arxiv.org/pdf/2605.20809 [PDF]

### A1b. Same group, earlier version
```bibtex
@inproceedings{kim2025repurposing,
  title = {Repurposing Annotation Guidelines to Instruct {LLM} Annotators: A Case Study},
  author = {Kim, Kon Woo and Islamaj, Rezarta and Kim, Jin-Dong and Boudin, Florian and Aizawa, Akiko},
  booktitle = {International Conference on Applications of Natural Language to Information Systems (NLDB 2025), Springer LNCS},
  year = {2025}, pages = {140--151}, doi = {10.1007/978-3-031-97144-0_13}, note = {arXiv:2510.12835}
}
```
- **What it does:** It proposes a moderation-oriented method that turns human guidelines into clear directives for LLMs, using the NCBI Disease Corpus as the case study.
- VERIFIED: https://arxiv.org/abs/2510.12835 [AX]. Venue, pages and DOI come from the arXiv comment and journal_ref field, not a Springer page.

### A1c. Bibal et al.
```bibtex
@inproceedings{bibal2025automating,
  title = {Automating Annotation Guideline Improvements using {LLM}s: A Case Study},
  author = {Bibal, Adrien and Gerlek, Nathaniel and Muric, Goran and Boschee, Elizabeth and Fincke, Steven C. and Ross, Mike and Minton, Steven N.},
  booktitle = {Proceedings of Context and Meaning: Navigating Disagreements in NLP Annotation},
  month = jan, year = {2025}, address = {Abu Dhabi, UAE}, publisher = {International Committee on Computational Linguistics},
  pages = {129--144}, url = {https://aclanthology.org/2025.comedi-1.13/}
}
```
- **What it does:** An entity-recognition case study suggesting LLMs can help produce high-quality guidelines (inter-annotator agreement rising from 0.593 to 0.84 on WNUT-17's guidelines) faster and more cheaply than crowd workers.
- VERIFIED: https://aclanthology.org/2025.comedi-1.13/ [ANTH]

### A2. Guideline Learning (Pang et al.)
```bibtex
@inproceedings{pang2023guideline,
  title = {Guideline Learning for In-Context Information Extraction},
  author = {Pang, Chaoxu and Cao, Yixuan and Ding, Qiang and Luo, Ping},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  month = dec, year = {2023}, address = {Singapore}, publisher = {Association for Computational Linguistics},
  pages = {15372--15389}, doi = {10.18653/v1/2023.emnlp-main.950}, url = {https://aclanthology.org/2023.emnlp-main.950/}
}
```
- **What it does:** Its Guideline Learning framework synthesizes guidelines from a few error cases during learning and retrieves helpful guidelines at inference for in-context IE. It also adds a self-consistency-based active learning method, evaluated on event and relation extraction.
- VERIFIED: https://aclanthology.org/2023.emnlp-main.950/ [ANTH]

### A3. GoLLIE
```bibtex
@inproceedings{sainz2024gollie,
  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
  author = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
  booktitle = {The Twelfth International Conference on Learning Representations (ICLR)}, year = {2024},
  url = {https://arxiv.org/abs/2310.03668}, note = {arXiv:2310.03668; OpenReview forum Y3wpuxd7u9 (ICLR 2024 poster)}
}
```
- **What it does:** It fine-tunes an LLM to comply with annotation guidelines so that zero-shot IE improves on unseen tasks, and its ablation shows detailed guidelines are key. It consumes human guidelines; it does not refine them.
- VERIFIED: https://arxiv.org/abs/2310.03668 [AX; comment "ICLR 2024"]; venue string "ICLR 2024 poster" [OR]

### A4. Codebook / guideline revision, LLM-as-coder, concept induction
```bibtex
@article{halterman2026codebook,
  title = {Codebook {LLM}s: Evaluating {LLM}s as Measurement Tools for Political Science Concepts},
  author = {Halterman, Andrew and Keith, Katherine A.},
  journal = {Political Analysis}, volume = {34}, number = {2}, pages = {188--204}, year = {2026},
  doi = {10.1017/pan.2025.10017}, note = {online 2025-09-19 per Crossref; arXiv:2407.10747}
}
```
- **What it does:** It curates three real political-science codebooks (protest events, political violence and manifestos), proposes a five-stage codebook-LLM measurement framework, and finds off-the-shelf open-weight 7-12B LLMs follow codebooks poorly zero-shot while supervised instruction tuning helps. It evaluates codebooks as given, with no automatic codebook revision, and one of its codebooks is a manifesto codebook.
- VERIFIED: https://arxiv.org/abs/2407.10747 [AX]; https://doi.org/10.1017/pan.2025.10017 [CR]

```bibtex
@misc{he2026experts,
  title = {Experts Rise Where {LLM}s Disagree: Using Cross-Model Disagreement to Target Expert Effort in {LLM} Codebook Revision for Large-Scale Annotation},
  author = {He, Zeyu and Zhou, Zhuqian and Vanacore, Kirk and Kizilcec, Rene F. and Huang, Ting-Hao 'Kenneth'},
  year = {2026}, eprint = {2609.26926}, archivePrefix = {arXiv}
}
```
- **What it does:** It compares three ways experts can give feedback for LLM codebook revision driven by cross-LLM disagreement; on tutoring transcripts, Rationale Labeling gave the best LLM-labeling accuracy (64.9% vs 57.8% for the expert-revised codebook).
- VERIFIED: https://arxiv.org/abs/2609.26926 [AX]. It is a preprint, and it uses disagreement among LLMs rather than gold labels.

```bibtex
@misc{yuan2026calico,
  title = {{CALICO}: A Human-Centered, Codebook-Aligned System for Annotation},
  author = {Yuan, Boqin and Gu, Xiaoyi and Li, Fiona and Wan, Chang and Hwang, Angel Hsing-Chi and Zhao, Jieyu},
  year = {2026}, eprint = {2609.14726}, archivePrefix = {arXiv}
}
```
- **What it does:** It is a codebook-to-prompt annotation workflow that treats prompts as editable, versioned, optimizable artifacts, with label-supervised prompt optimization via GEPA, MIPROv2, OPRO and its own ReflectAgent. It reports +13.0 and +7.4 absolute held-out points for two coders on AI-companion chatbot-conversation codebooks. This is the closest annotation-side prompt-artifact optimizer I found, and it edits prompts only.
- VERIFIED: https://arxiv.org/abs/2609.14726 [AX]. It is a preprint.

```bibtex
@misc{kucuk2026llm,
  title = {{LLM}-Assisted Stance Detection in Scientific Discourse: A Test Case in Bayesian Cognitive Science},
  author = {Kucuk, Eyup Engin and Kelestemur, Tarik and Tanrikulu, {\"O}mer Da{\u g}lar},
  year = {2026}, eprint = {2606.15566}, archivePrefix = {arXiv}
}
```
- **What it does:** It combines a theory-driven codebook, expert-coded reference annotations and a "diagnostic-gated prompt-optimization search," then reports a held-out combined reliability of 0.76.
- VERIFIED: https://arxiv.org/abs/2606.15566 [AX]. It is a preprint.

```bibtex
@misc{dunivin2026self,
  title = {Self-reflection in Automated Qualitative Coding: Improving Text Annotation through Secondary {LLM} Critique},
  author = {Dunivin, Zackary Okun and Noori, Mobina and Frey, Seth and Atkinson, Curtis},
  year = {2026}, eprint = {2601.09905}, archivePrefix = {arXiv}
}
```
- **What it does:** It uses a two-stage workflow where a secondary LLM critic re-reads each positive label with the first model's rationale, and code-specific critic clauses address observed failure modes (F1 improved by 0.04 to 0.25).
- VERIFIED: https://arxiv.org/abs/2601.09905 [AX]. It is a preprint.

```bibtex
@misc{nakamura2026observational,
  title = {Observational Equivalence of {LLM} and Human Annotation},
  author = {Nakamura, Kentaro and Tan, Jing Ling and Yean, George},
  year = {2026}, eprint = {2609.22133}, archivePrefix = {arXiv}
}
```
- **What it does:** It replicates 14 political-science text-classification studies and finds LLM-expert agreement comparable to expert-expert agreement. It proposes using cross-LLM disagreement to find difficult cases and refine codebooks.
- VERIFIED: https://arxiv.org/abs/2609.22133 [AX]. It is a preprint.

```bibtex
@misc{gomezzara2026revisiting,
  title = {Revisiting Framing Codebooks with {AI}: Employing Large Language Models as Analytical Collaborators in Deductive Content Analysis},
  author = {Gomez-Zara, Diego and Valdivieso, Hern{\'a}n and P{\'e}rez, Jorge and Parra, Denis and Valenzuela, Sebasti{\'a}n},
  year = {2026}, eprint = {2604.19111}, archivePrefix = {arXiv}
}
```
- **What it does:** It proposes a workflow where LLMs help refine framing codebooks, surfacing ambiguities and borderline cases through researcher-data dialogue. It is human-in-the-loop and has no gold-driven loop.
- VERIFIED: https://arxiv.org/abs/2604.19111 [AX]. It is a preprint.

```bibtex
@misc{zambrano2025data,
  title = {Data Plus Theory Equals Codebook: Leveraging {LLM}s for Human-{AI} Codebook Development},
  author = {Zambrano, Andres Felipe and Wei, Zhanlan and Zhang, Jiayi and Baker, Ryan S. and Ocumpaugh, Jaclyn and Barany, Amanda and Liu, Xiner and Ginger, Jeffrey and Paquette, Luc and Zhou, Yiqiu and Borchers, Conrad},
  note = {venue and year not shown on the PDF I read}
}
```
- **What it does:** It examines whether GPT-4o can help develop theory-informed qualitative codebooks, comparing four prompting strategies.
- It does not run a disagreement-driven loop; humans merge and refine the codebook (first 100k characters read).
- NOT VERIFIED (venue/year): I read https://jedm.educationaldatamining.org/index.php/JEDM/article/download/1001/268, which does not name the journal. The URL suggests JEDM, but I did not confirm it.

```bibtex
@inproceedings{lam2024concept,
  title = {Concept Induction: Analyzing Unstructured Text with High-Level Concepts Using {LLooM}},
  author = {Lam, Michelle S. and Teoh, Janice and Landay, James and Heer, Jeffrey and Bernstein, Michael S.},
  booktitle = {Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)}, year = {2024}, pages = {1--28},
  doi = {10.1145/3613904.3642830}, note = {arXiv:2404.12259}
}
```
- **What it does:** It introduces "concept induction," where LLooM uses LLMs to iteratively synthesize sampled text into human-interpretable high-level concepts with explicit inclusion criteria. It is unsupervised, with no gold labels.
- VERIFIED: https://arxiv.org/abs/2404.12259 [AX]; https://doi.org/10.1145/3613904.3642830 [CR]

```bibtex
@inproceedings{wan2024tntllm,
  title = {{TnT-LLM}: Text Mining at Scale with Large Language Models},
  author = {Wan, Mengting and Safavi, Tara and Jauhar, Sujay Kumar and Kim, Yujin and Counts, Scott and Neville, Jennifer and Suri, Siddharth and Shah, Chirag and White, Ryen W and Yang, Longqi and Andersen, Reid and Buscher, Georg and Joshi, Dhruv and Rangan, Nagu},
  booktitle = {Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining}, year = {2024}, pages = {5836--5847},
  doi = {10.1145/3637528.3671647}, note = {arXiv:2403.12173}
}
```
- **What it does:** It is a two-phase framework in which an LLM iteratively produces and refines a label taxonomy zero-shot, then acts as a data labeler to train lightweight classifiers (Bing Copilot use case). It has no gold-driven refinement.
- VERIFIED: https://arxiv.org/abs/2403.12173 [AX]; https://doi.org/10.1145/3637528.3671647 [CR]

### A5. Guideline-conditioned IE, "annotation instructions," instruction induction
```bibtex
@inproceedings{huang2025guidener,
  title = {{GuideNER}: Annotation Guidelines Are Better than Examples for In-Context Named Entity Recognition},
  author = {Huang, Shizhou and Xu, Bo and Yu, Yang and Li, Changqun and Lin, Xin Alex},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence}, volume = {39}, number = {23}, pages = {24159--24166}, year = {2025},
  doi = {10.1609/aaai.v39i23.34591}
}
```
- **What it does:** It has LLMs summarize concise annotation guidelines used as in-context instructions in place of examples, and beats prior ICL NER methods with shorter prompts (+12.63 F1 on GENIA).
- VERIFIED: https://ojs.aaai.org/index.php/AAAI/article/view/34591

```bibtex
@inproceedings{fonseca2024can,
  title = {Can Large Language Models Follow Concept Annotation Guidelines? A Case Study on Scientific and Financial Domains},
  author = {Fonseca, Marcio and Cohen, Shay B.},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024}, year = {2024}, pages = {8027--8042},
  doi = {10.18653/v1/2024.findings-acl.478}, url = {https://aclanthology.org/2024.findings-acl.478/}
}
```
- **What it does:** It tests whether instruction-tuned LLMs follow factual, counterfactual and nonsensical in-context concept guidelines for zero-shot sentence classification.
- VERIFIED: https://arxiv.org/abs/2311.08704 [AX]; .bib [ANTH]

```bibtex
@inproceedings{srivastava2025instruction,
  title = {Instruction-Tuning {LLM}s for Event Extraction with Annotation Guidelines},
  author = {Srivastava, Saurabh and Pati, Sweta and Yao, Ziyu},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025}, year = {2025}, pages = {13055--13071},
  doi = {10.18653/v1/2025.findings-acl.677}, url = {https://aclanthology.org/2025.findings-acl.677/}
}
```
- **What it does:** It studies the effect of human-provided and machine-generated annotation guidelines when instruction-tuning LLMs for event extraction.
- VERIFIED: https://arxiv.org/abs/2502.16377 [AX]; .bib [ANTH]

```bibtex
@inproceedings{delafuente2025guidex,
  title = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
  author = {De La Fuente, Neil and Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agirre, Eneko},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025}, year = {2025}, pages = {24248--24262},
  doi = {10.18653/v1/2025.findings-acl.1245}, url = {https://aclanthology.org/2025.findings-acl.1245/}
}
```
- **What it does:** It automatically defines domain-specific schemas, infers guidelines and generates synthetically labeled instances to fine-tune Llama 3.1, setting a new state of the art on seven zero-shot NER benchmarks.
- VERIFIED: https://arxiv.org/abs/2506.00649 [AX]; .bib [ANTH]

```bibtex
@inproceedings{honovich2023instruction,
  title = {Instruction Induction: From Few Examples to Natural Language Task Descriptions},
  author = {Honovich, Or and Shaham, Uri and Bowman, Samuel R. and Levy, Omer},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}, year = {2023}, pages = {1935--1952},
  url = {https://aclanthology.org/2023.acl-long.108/}
}
```
- **What it does:** It shows LMs can infer a task from a few demonstrations by generating a natural-language instruction, with a 24-task dataset and an execution-based metric.
- VERIFIED: https://aclanthology.org/2023.acl-long.108 [ANTH]; https://arxiv.org/abs/2205.10782 [AX]

Marginal items (preprints, [AX] only):
```bibtex
@misc{rishav2026contraprompt,
  title = {{ContraPrompt}: Contrastive Prompt Optimization via Dyadic Reasoning Trace Analysis},
  author = {Rishav, Rishav and Pujari, Pushpak and Rastogi, Pushpendre}, year = {2026}, eprint = {2604.17937}, archivePrefix = {arXiv}
}
@misc{chakma2026two,
  title = {Two-Stage Prompt Optimization for Few-Shot Relation Extraction: From Reasoning-Guided Search to Gradient-Guided Refinement},
  author = {Chakma, Aunabil and Surdeanu, Mihai and Blanco, Eduardo}, year = {2026}, eprint = {2606.29639}, archivePrefix = {arXiv}
}
```
- **ContraPrompt:** It optimizes prompts from contrastive reasoning traces and evaluates on FiNER-139 financial NER, among other benchmarks.
- **Chakma et al.:** It does prompt optimization for few-shot relation extraction (FS-TACRED, FS-FewRel).
- VERIFIED: https://arxiv.org/abs/2604.17937 and https://arxiv.org/abs/2606.29639 [AX]

**A summary.** In everything I found, the edited object is guideline or codebook text, or at most a prompt. None of it edits tools or the chain of LLM calls.

---

## B. LLMs as annotators

```bibtex
@article{gilardi2023chatgpt,
  title = {{ChatGPT} outperforms crowd workers for text-annotation tasks},
  author = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma{\"e}l},
  journal = {Proceedings of the National Academy of Sciences}, volume = {120}, number = {30}, pages = {e2305016120}, year = {2023},
  doi = {10.1073/pnas.2305016120}, note = {arXiv:2303.15056}
}
```
- **What it does:** Using 2,382 tweets, it shows ChatGPT's zero-shot accuracy exceeds crowd-workers on four of five annotation tasks at about 20x lower cost per annotation.
- VERIFIED: https://arxiv.org/abs/2303.15056 [AX]; https://doi.org/10.1073/pnas.2305016120 [CR]. I did not open the PNAS page.

```bibtex
@inproceedings{he2024annollm,
  title = {{AnnoLLM}: Making Large Language Models to Be Better Crowdsourced Annotators},
  author = {He, Xingwei and Lin, Zhenghao and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Lin, Chen and Jiao, Jian and Yiu, Siu Ming and Duan, Nan and Chen, Weizhu},
  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 6: Industry Track)},
  year = {2024}, pages = {165--190}, doi = {10.18653/v1/2024.naacl-industry.15}, url = {https://aclanthology.org/2024.naacl-industry.15/}
}
```
- **What it does:** It proposes an explain-then-annotate approach in which LLMs first explain the gold label for each example and then use those self-generated explanations in few-shot chain-of-thought prompts to annotate.
- VERIFIED: https://arxiv.org/abs/2303.16854 [AX]; .bib [ANTH]

```bibtex
@inproceedings{tan2024large,
  title = {Large Language Models for Data Annotation and Synthesis: A Survey},
  author = {Tan, Zhen and Li, Dawei and Wang, Song and Beigi, Alimohammad and Jiang, Bohan and Bhattacharjee, Amrita and Karami, Mansooreh and Li, Jundong and Cheng, Lu and Liu, Huan},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}, year = {2024}, pages = {930--957},
  doi = {10.18653/v1/2024.emnlp-main.54}, url = {https://aclanthology.org/2024.emnlp-main.54/}
}
```
- **What it does:** It surveys LLM-based annotation generation, assessment and utilization, with a taxonomy of annotatable data types.
- VERIFIED: https://arxiv.org/abs/2402.13446 [AX]; .bib [ANTH]

```bibtex
@article{ziems2024can,
  title = {Can Large Language Models Transform Computational Social Science?},
  author = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
  journal = {Computational Linguistics}, volume = {50}, number = {1}, pages = {237--291}, year = {2024},
  doi = {10.1162/coli_a_00502}, url = {https://aclanthology.org/2024.cl-1.8/}
}
```
- **What it does:** It evaluates 13 language models zero-shot on 25 computational-social-science benchmarks, finding LLMs trail the best fine-tuned models on taxonomic labeling but agree fairly well with humans.
- VERIFIED: https://arxiv.org/abs/2305.03514 [AX]; .bib [ANTH]

```bibtex
@misc{ahtisham2025ai,
  title = {{AI} Annotation Orchestration: Evaluating {LLM} verifiers to Improve the Quality of {LLM} Annotations in Learning Analytics},
  author = {Ahtisham, Bakhtawar and Vanacore, Kirk and Lee, Jinsook and Zhou, Zhuqian and Pietrzak, Doug and Kizilcec, Rene F.},
  year = {2025}, doi = {10.1145/3785022.3785095}, eprint = {2511.09785}, archivePrefix = {arXiv}
}
```
- **What it does:** It tests self- and cross-verification orchestration of GPT, Claude and Gemini for qualitative coding of tutoring discourse (a 58% kappa improvement).
- VERIFIED: https://arxiv.org/abs/2511.09785 [AX]. The venue is not stated on the arXiv record I read.

For 2025-26 codebook/ontology annotation papers, see A4: halterman2026codebook, yuan2026calico, he2026experts, nakamura2026observational, dunivin2026self and kucuk2026llm.

---

## C. Prompt / context / program optimization

```bibtex
@inproceedings{zhou2023large,
  title = {Large Language Models Are Human-Level Prompt Engineers},
  author = {Zhou, Yongchao and Muresanu, Andrei Ioan and Han, Ziwen and Paster, Keiran and Pitis, Silviu and Chan, Harris and Ba, Jimmy},
  booktitle = {The Eleventh International Conference on Learning Representations (ICLR)}, year = {2023}, note = {arXiv:2211.01910}
}
```
- **What it does:** APE treats the instruction as a "program" and searches LLM-proposed candidate instructions to maximize a score function; it is better than or comparable to human instructions on 19 of 24 tasks.
- VERIFIED: https://arxiv.org/abs/2211.01910 [AX]; venue "ICLR 2023" [OR]

```bibtex
@inproceedings{yang2024large,
  title = {Large Language Models as Optimizers},
  author = {Yang, Chengrun and Wang, Xuezhi and Lu, Yifeng and Liu, Hanxiao and Le, Quoc V. and Zhou, Denny and Chen, Xinyun},
  booktitle = {The Twelfth International Conference on Learning Representations (ICLR)}, year = {2024}, note = {arXiv:2309.03409}
}
```
- **What it does:** OPRO prompts an LLM with previously generated solutions and their scores to propose new ones, and uses this for prompt optimization (up to +8% on GSM8K and up to +50% on BBH over human prompts).
- VERIFIED: https://arxiv.org/abs/2309.03409 [AX; comment "ICLR 2024"], [OR]

```bibtex
@inproceedings{pryzant2023automatic,
  title = {Automatic Prompt Optimization with ``Gradient Descent'' and Beam Search},
  author = {Pryzant, Reid and Iter, Dan and Li, Jerry and Lee, Yin and Zhu, Chenguang and Zeng, Michael},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing}, year = {2023}, pages = {7957--7968},
  doi = {10.18653/v1/2023.emnlp-main.494}, url = {https://aclanthology.org/2023.emnlp-main.494/}
}
```
- **What it does:** ProTeGi uses minibatch errors to form natural-language "gradients" that criticize the prompt, edits the prompt in the opposite direction, and guides this with beam search and bandit selection. The abstract says it rewrites "vague task descriptions into more precise annotation instructions."
- VERIFIED: https://arxiv.org/abs/2305.03495 [AX]; .bib [ANTH]

```bibtex
@article{yuksekgonul2025optimizing,
  title = {Optimizing generative {AI} by backpropagating language model feedback},
  author = {Yuksekgonul, Mert and Bianchi, Federico and Boen, Joseph and Liu, Sheng and Lu, Pan and Huang, Zhi and Guestrin, Carlos and Zou, James},
  journal = {Nature}, volume = {639}, number = {8055}, pages = {609--616}, year = {2025}, doi = {10.1038/s41586-025-08661-4},
  note = {TextGrad; arXiv:2406.07496 titled ``TextGrad: Automatic `Differentiation' via Text'' with an author list that omits Pan Lu}
}
```
- **What it does:** TextGrad backpropagates LLM-written textual feedback through a computation graph of a compound AI system to optimize components such as prompts and code.
- VERIFIED: https://arxiv.org/abs/2406.07496 [AX]; https://doi.org/10.1038/s41586-025-08661-4 [CR]. The arXiv v1 author list has 6 authors (Yuksekgonul, Bianchi, Boen, Liu, Huang, Guestrin, Zou, i.e. 7 entries without Lu); the Nature list in Crossref has 8.

```bibtex
@inproceedings{khattab2024dspy,
  title = {{DSPy}: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines},
  author = {Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and Vardhamanan, Sri and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas T. and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher},
  booktitle = {The Twelfth International Conference on Learning Representations (ICLR)}, year = {2024},
  note = {ICLR 2024 spotlight; arXiv:2310.03714 v1 is titled ``...into Self-Improving Pipelines''}
}
```
- **What it does:** DSPy is a programming model that abstracts LM pipelines as text-transformation graphs of declarative modules, with a compiler that optimizes the pipeline for a metric.
- VERIFIED: https://arxiv.org/abs/2310.03714 [AX]; venue and title "ICLR 2024 spotlight" [OR]

```bibtex
@inproceedings{opsahlong2024optimizing,
  title = {Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs},
  author = {Opsahl-Ong, Krista and Ryan, Michael J and Purtell, Josh and Broman, David and Potts, Christopher and Zaharia, Matei and Khattab, Omar},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}, year = {2024}, pages = {9340--9366},
  doi = {10.18653/v1/2024.emnlp-main.525}, url = {https://aclanthology.org/2024.emnlp-main.525/}
}
```
- **What it does:** It introduces MIPRO, which jointly optimizes free-form instructions and few-shot demonstrations of every module in a multi-stage LM program without module-level labels or gradients.
- VERIFIED: https://arxiv.org/abs/2406.11695 [AX]; .bib [ANTH]. The abstract says "MIPRO," not "MIPROv2."

```bibtex
@inproceedings{agrawal2026gepa,
  title = {{GEPA}: Reflective Prompt Evolution Can Outperform Reinforcement Learning},
  author = {Agrawal, Lakshya A and Tan, Shangyin and Soylu, Dilara and Ziems, Noah and Khare, Rishi and Opsahl-Ong, Krista and Singhvi, Arnav and Shandilya, Herumb and Ryan, Michael J and Jiang, Meng and Potts, Christopher and Sen, Koushik and Dimakis, Alexandros G. and Stoica, Ion and Klein, Dan and Zaharia, Matei and Khattab, Omar},
  booktitle = {The Fourteenth International Conference on Learning Representations (ICLR)}, year = {2026}, note = {ICLR 2026 oral; arXiv:2507.19457, first posted 2025-07-25}
}
```
- **What it does:** GEPA samples system trajectories, reflects on them in natural language to diagnose problems and propose prompt updates, and keeps a Pareto frontier of candidates; it beats GRPO by 6% on average with up to 35x fewer rollouts and beats MIPROv2 by over 10%.
- VERIFIED: https://arxiv.org/abs/2507.19457 [AX; comment "Accepted to ICLR 2026 (Oral)"], [OR]

```bibtex
@inproceedings{zhang2026agentic,
  title = {Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models},
  author = {Zhang, Qizheng and Hu, Changran and Upasani, Shubhangi and Ma, Boyuan and Hong, Fenglu and Kamanuru, Vamsidhar and Rainton, Jay and Wu, Chen and Ji, Mengmeng and Li, Hanchen and Thakker, Urmish and Zou, James and Olukotun, Kunle},
  booktitle = {The Fourteenth International Conference on Learning Representations (ICLR)}, year = {2026}, note = {ICLR 2026 poster; arXiv:2510.04618, first posted 2025-10-06}
}
```
- **What it does:** ACE treats contexts as evolving playbooks that accumulate, refine and organize strategies through generation, reflection and curation, using structured incremental updates to avoid brevity bias and context collapse (+10.6% on agents, +8.6% on finance).
- VERIFIED: https://arxiv.org/abs/2510.04618 [AX; comment "ICLR 2026"], [OR]

```bibtex
@inproceedings{suzgun2026dynamic,
  title = {Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory},
  author = {Suzgun, Mirac and Yuksekgonul, Mert and Bianchi, Federico and Jurafsky, Dan and Zou, James},
  booktitle = {Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
  year = {2026}, pages = {7080--7106}, doi = {10.18653/v1/2026.eacl-long.333}, url = {https://aclanthology.org/2026.eacl-long.333/}
}
```
- **What it does:** It gives a black-box LM a persistent, self-curated memory of strategies and code snippets that it reuses at inference time, without ground-truth labels or parameter updates.
- VERIFIED: https://arxiv.org/abs/2504.07952 [AX]; .bib [ANTH]

```bibtex
@inproceedings{zhao2024expel,
  title = {{ExpeL}: {LLM} Agents Are Experiential Learners},
  author = {Zhao, Andrew and Huang, Daniel and Xu, Quentin and Lin, Matthieu and Liu, Yong-Jin and Huang, Gao},
  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence (AAAI-24)}, year = {2024}, note = {arXiv:2308.10144; volume and pages not verified}
}
```
- **What it does:** The agent autonomously gathers experiences from training tasks, extracts natural-language knowledge from them, and recalls those insights and past experiences at inference without parametric updates.
- VERIFIED: https://arxiv.org/abs/2308.10144 [AX; comment "AAAI-24"]

```bibtex
@inproceedings{wang2025agent,
  title = {Agent Workflow Memory},
  author = {Wang, Zora Zhiruo and Mao, Jiayuan and Fried, Daniel and Neubig, Graham},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)}, year = {2025}, note = {arXiv:2409.07429}
}
```
- **What it does:** It induces reusable workflows from past experiences, offline or on the fly, and supplies them to guide an agent on Mind2Web and WebArena (+24.6% and +51.1% relative success).
- VERIFIED: https://arxiv.org/abs/2409.07429 [AX]; venue "ICML 2025" [OR]

Caution for few-gold-document settings:
```bibtex
@misc{singh2026mage,
  title = {{MAGE}: Understanding Stability-Performance Trade-offs in Multi-component Prompt Optimization},
  author = {Singh, Prateek}, year = {2026}, eprint = {2607.11944}, archivePrefix = {arXiv}
}
```
- **What it does:** It is a controlled ablation of reflective prompt optimizers. The abstract states that "in low-data regimes (Ntrain=30), well-designed fixed prompts outperform all reflective optimizers" (tested on GSM8K-Hard).
- VERIFIED: https://arxiv.org/abs/2607.11944 [AX]. It is a single-author preprint.

---

## D. Self-improving agents, harness and workflow search

### D-classic
```bibtex
@inproceedings{shinn2023reflexion,
  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},
  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS 2023)}, year = {2023}, doi = {10.52202/075280-0377}, note = {arXiv:2303.11366}
}
```
- **What it does:** Agents verbally reflect on task feedback and keep the reflective text in an episodic memory buffer to improve later trials without weight updates (91% pass@1 on HumanEval).
- VERIFIED: https://arxiv.org/abs/2303.11366 [AX]; venue [CR] and [OR] ("NeurIPS 2023 poster")

```bibtex
@inproceedings{madaan2023selfrefine,
  title = {Self-Refine: Iterative Refinement with Self-Feedback},
  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS 2023)}, year = {2023}, note = {arXiv:2303.17651}
}
```
- **What it does:** A single LLM generates an output, gives feedback on it, and refines it iteratively with no training data, improving about 20% absolute on average across 7 tasks.
- VERIFIED: https://arxiv.org/abs/2303.17651 [AX]; venue "NeurIPS 2023 poster" [OR]

```bibtex
@article{wang2024voyager,
  title = {Voyager: An Open-Ended Embodied Agent with Large Language Models},
  author = {Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chaowei and Zhu, Yuke and Fan, Linxi and Anandkumar, Anima},
  journal = {Transactions on Machine Learning Research}, year = {2024}, note = {arXiv:2305.16291; volume not verified}
}
```
- **What it does:** It is an LLM-powered lifelong-learning Minecraft agent with an automatic curriculum, an ever-growing library of executable-code skills, and an iterative prompting mechanism using environment feedback and self-verification.
- VERIFIED: https://arxiv.org/abs/2305.16291 [AX]; venue "Trans. Mach. Learn. Res. 2024" [OR]

```bibtex
@inproceedings{hu2025automated,
  title = {Automated Design of Agentic Systems},
  author = {Hu, Shengran and Lu, Cong and Clune, Jeff},
  booktitle = {The Thirteenth International Conference on Learning Representations (ICLR)}, year = {2025}, note = {arXiv:2408.08435}
}
```
- **What it does:** ADAS has a meta agent iteratively program new agents in code, using an archive of earlier discoveries (Meta Agent Search). The search space includes prompts, tool use and workflows.
- VERIFIED: https://arxiv.org/abs/2408.08435 [AX]; venue "ICLR 2025 Poster" [OR]

```bibtex
@inproceedings{zhang2025aflow,
  title = {{AFlow}: Automating Agentic Workflow Generation},
  author = {Zhang, Jiayi and Xiang, Jinyu and Yu, Zhaoyang and Teng, Fengwei and Chen, Xionghui and Chen, Jiaqi and Zhuge, Mingchen and Cheng, Xin and Hong, Sirui and Wang, Jinlin and Zheng, Bingnan and Liu, Bang and Luo, Yuyu and Wu, Chenglin},
  booktitle = {The Thirteenth International Conference on Learning Representations (ICLR)}, year = {2025}, note = {arXiv:2410.10762}
}
```
- **What it does:** It reformulates workflow optimization as Monte Carlo Tree Search over code-represented workflows of LLM-invoking nodes, refining them via code modification, tree-structured experience and execution feedback.
- VERIFIED: https://arxiv.org/abs/2410.10762 [AX]; venue "ICLR 2025 Oral" [OR]

```bibtex
@inproceedings{zhang2026darwin,
  title = {{D}arwin {G}{\"o}del Machine: Open-Ended Evolution of Self-Improving Agents},
  author = {Zhang, Jenny and Hu, Shengran and Lu, Cong and Lange, Robert and Clune, Jeff},
  booktitle = {The Fourteenth International Conference on Learning Representations (ICLR)}, year = {2026}, note = {arXiv:2505.22954, first posted 2025-05-29}
}
```
- **What it does:** It iteratively modifies its own code and empirically validates each change on coding benchmarks, keeping an archive of agents (SWE-bench 20.0% to 50.0%).
- VERIFIED: https://arxiv.org/abs/2505.22954 [AX; the arXiv title spells "Godel"]; venue "ICLR 2026 Poster" [OR]

```bibtex
@misc{robeyns2025self,
  title = {A Self-Improving Coding Agent},
  author = {Robeyns, Maxime and Szummer, Martin and Aitchison, Laurence}, year = {2025}, eprint = {2504.15228}, archivePrefix = {arXiv},
  note = {arXiv comment: submitted as a preprint to NeurIPS 2025; OpenReview lists a workshop oral (SSI-FM)}
}
```
- **What it does:** An agent system equipped with basic coding tools autonomously edits itself, raising a random SWE-Bench Verified subset from 17% to 53%.
- VERIFIED: https://arxiv.org/abs/2504.15228 [AX]

```bibtex
@inproceedings{yang2024sweagent,
  title = {{SWE-agent}: Agent-Computer Interfaces Enable Automated Software Engineering},
  author = {Yang, John and Jimenez, Carlos E. and Wettig, Alexander and Lieret, Kilian and Yao, Shunyu and Narasimhan, Karthik and Press, Ofir},
  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS 2024)}, year = {2024}, note = {arXiv:2405.15793}
}
```
- **What it does:** It shows that a custom agent-computer interface, built for LM agents rather than humans, substantially improves their ability to edit code, navigate repositories and run tests (12.5% pass@1 on SWE-bench).
- VERIFIED: https://arxiv.org/abs/2405.15793 [AX]; venue "NeurIPS 2024 poster" [OR]

```bibtex
@misc{zheng2025skillweaver,
  title = {{SkillWeaver}: Web Agents can Self-Improve by Discovering and Honing Skills},
  author = {Zheng, Boyuan and Fatemi, Michael Y. and Jin, Xiaolong and Wang, Zora Zhiruo and Gandhi, Apurva and Song, Yueqi and Gu, Yu and Srinivasa, Jayanth and Liu, Gaowen and Neubig, Graham and Su, Yu},
  year = {2025}, eprint = {2504.07079}, archivePrefix = {arXiv}
}
```
- **What it does:** Agents autonomously synthesize reusable skills as APIs for a new website, practice them and distill the practice into robust APIs (31.8% relative gain on WebArena).
- VERIFIED: https://arxiv.org/abs/2504.07079 [AX]. I found no published venue; the OpenReview record is "CoRR 2025."

```bibtex
@inproceedings{huang2024large,
  title = {Large Language Models Cannot Self-Correct Reasoning Yet},
  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
  booktitle = {The Twelfth International Conference on Learning Representations (ICLR)}, year = {2024}, note = {arXiv:2310.01798}
}
```
- **What it does:** It shows that LLMs struggle to self-correct reasoning without external feedback and sometimes get worse after "intrinsic" self-correction.
- VERIFIED: https://arxiv.org/abs/2310.01798 [AX; comment "ICLR 2024"], [OR]

```bibtex
@article{kamoi2024when,
  title = {When Can {LLM}s Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of {LLM}s},
  author = {Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},
  journal = {Transactions of the Association for Computational Linguistics}, volume = {12}, pages = {1417--1440}, year = {2024},
  doi = {10.1162/tacl_a_00713}, note = {arXiv:2406.01297}
}
```
- **What it does:** It is a critical survey concluding that no prior work shows successful self-correction with feedback from prompted LLMs, except on tasks exceptionally suited to it. Self-correction works with reliable external feedback or after large-scale fine-tuning.
- VERIFIED: https://arxiv.org/abs/2406.01297 [AX]; https://doi.org/10.1162/tacl_a_00713 [CR]

Surveys on self-evolving agents:
```bibtex
@article{gao2026survey,
  title = {A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence},
  author = {Gao, Huan-ang and Geng, Jiayi and Hua, Wenyue and Hu, Mengkang and Juan, Xinzhe and Liu, Hongzhang and Liu, Shilong and Qiu, Jiahao and Qi, Xuan and Wu, Yiran and Wang, Hongru and Xiao, Han and Zhou, Yuhang and Zhang, Shaokun and Zhang, Jiayi and Xiang, Jinyu and Fang, Yixiong and Zhao, Qiwen and Liu, Dongrui and Ren, Qihan and Qian, Cheng and Wang, Zhenhailong and Hu, Minda and Wang, Huazheng and Wu, Qingyun and Ji, Heng and Wang, Mengdi},
  journal = {Transactions on Machine Learning Research}, year = {2026}, note = {arXiv:2507.21046; arXiv comment: TMLR (01/2026)}
}
@misc{fang2025comprehensive,
  title = {A Comprehensive Survey of Self-Evolving {AI} Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems},
  author = {Fang, Jinyuan and Peng, Yanwen and Zhang, Xi and Wang, Yingxu and Yi, Xinhao and Zhang, Guibin and Xu, Yi and Wu, Bin and Liu, Siwei and Li, Zihao and Ren, Zhaochun and Aletras, Nikos and Wang, Xi and Zhou, Han and Meng, Zaiqiao},
  year = {2025}, eprint = {2508.07407}, archivePrefix = {arXiv}
}
```
- **gao2026survey:** It organizes self-evolving agents around what, when and how to evolve, covering models, memory, tools and architecture.
- **fang2025comprehensive:** It gives a unified feedback-loop framework (System Inputs, Agent System, Environment, Optimisers) and reviews techniques per component.
- VERIFIED: https://arxiv.org/abs/2507.21046 and https://arxiv.org/abs/2508.07407 [AX]. The TMLR venue for the first is from the arXiv comment only.

### D-harness (your items 1-10 plus related)

The user-supplied author names match every record below. Only the Meta-Harness venue (COLM 2026) was found, via OpenReview. Everything else is a preprint with no venue on the record.

```bibtex
@misc{lee2026metaharness,
  title = {Meta-Harness: End-to-End Optimization of Model Harnesses},
  author = {Lee, Yoonho and Nair, Roshen and Zhang, Qizheng and Lee, Kangwook and Khattab, Omar and Finn, Chelsea},
  year = {2026}, eprint = {2603.28052}, archivePrefix = {arXiv}, note = {OpenReview venue string: COLM 2026}
}
```
- **(1) What it does:** It is an outer-loop system in which an agentic proposer reads the source code, scores and execution traces of all prior harness candidates through a filesystem, and searches over harness code for LLM applications.
- **Task fit:** Its tasks are online text classification (LawBench 215-class charges, Symptom2Disease, USPTO-50k, per the full text I read), retrieval-augmented math reasoning and agentic coding (TerminalBench-2). It is not annotation/IE-specific, but "online text classification" is the closest labeling-type evaluation.
- VERIFIED: https://arxiv.org/abs/2603.28052 [AX], [PDF grep]; venue [OR]

```bibtex
@misc{ye2026meta,
  title = {Meta Context Engineering via Agentic Skill Evolution},
  author = {Ye, Haoran and He, Xuning and Arak, Vincent and Dong, Haonan and Song, Guojie},
  year = {2026}, eprint = {2601.21557}, archivePrefix = {arXiv}
}
```
- **(2) What it does:** MCE is a bi-level framework where a meta-level agent refines context-engineering skills via "agentic crossover" while a base-level agent executes them and optimizes context as files and code (5.6-53.8% relative gain over agentic CE baselines).
- **Task fit:** Datasets include FiNER (token labeling of XBRL financial documents with entity types), Symptom2Disease, LawBench and USPTO-50k, per the full text. This is the only one of your list that includes a token-level labeling/NER task, though it is not annotation-guideline or UMR/TimeML work.
- VERIFIED: https://arxiv.org/abs/2601.21557 [AX], [PDF grep]

```bibtex
@misc{zhang2026self,
  title = {Self-Harness: Harnesses That Improve Themselves},
  author = {Zhang, Hangfan and Zhang, Shao and Li, Kangcong and Zhang, Chen and Chen, Yang and Zhang, Yiqun and Bai, Lei and Hu, Shuyue},
  year = {2026}, eprint = {2606.09498}, archivePrefix = {arXiv}
}
```
- **(3) What it does:** An LLM agent improves its own harness through Weakness Mining from execution traces, Harness Proposal, and Proposal Validation, which accepts edits only after regression testing. Every final harness improves both held-in and held-out pass rates on Terminal-Bench-2.0, SWE-bench Verified and AppWorld.
- **Task fit:** No annotation/IE.
- VERIFIED: https://arxiv.org/abs/2606.09498 [AX]

```bibtex
@misc{lin2026agentic,
  title = {Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses},
  author = {Lin, Jiahang and Liu, Shichun and Pan, Chengjun and Lin, Lizhi and Dou, Shihan and Xi, Zhiheng and Huang, Xuanjing and Yan, Hang and Han, Zhenhua and Gui, Tao and Jiang, Yu-Gang},
  year = {2026}, eprint = {2604.25850}, archivePrefix = {arXiv}
}
```
- **(4) What it does:** AHE is a closed loop that evolves coding-agent harness components. It gives each component a file-level representation, distills trajectories into a drill-down evidence corpus, and pairs every edit with a self-declared prediction verified against the next round's outcomes.
- **Task fit:** Terminal-Bench 2 (69.7% to 77.0%) and SWE-bench-verified. No annotation/IE.
- VERIFIED: https://arxiv.org/abs/2604.25850 [AX]

```bibtex
@misc{lin2026harness,
  title = {Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving {LLM} Agents},
  author = {Lin, Minhua and Wu, Juncheng and Wang, Zijun and Shi, Zhan and Sang, Yisi and He, Bing and Liu, Zewen and Wei, Tianxin and Wu, Zongyu and Zhang, Zhiwei and Wang, Dakuo and Zhang, Xiang and Dumoulin, Benoit and Xie, Cihang and Zhou, Yuyin and Wang, Suhang and Lu, Hanqing},
  year = {2026}, eprint = {2605.30621}, archivePrefix = {arXiv}
}
```
- **(5) What it does:** It separates harness-updating (producing useful persistent harness updates) from harness-benefit (gaining from them). Updating is flat across capability tiers: Qwen3.5-9B's updates match Claude Opus 4.6's. Benefit is non-monotonic: mid-tier models benefit most.
- **Task fit:** The abstract names no annotation/IE task; I did not read the full text for task details.
- VERIFIED: https://arxiv.org/abs/2605.30621 [AX]. This is the Lin et al. 2026 paper you meant, a different first-author set from AHE (Jiahang Lin vs Minhua Lin).

```bibtex
@inproceedings{zelikman2024self,
  title = {Self-Taught Optimizer ({STOP}): Recursively Self-Improving Code Generation},
  author = {Zelikman, Eric and Lorch, Eliana and Mackey, Lester and Kalai, Adam Tauman},
  booktitle = {First Conference on Language Modeling (COLM)}, year = {2024}, note = {arXiv:2310.02304}
}
```
- **(6) What it does:** A scaffolding program that queries an LM is used to improve itself, starting from a seed improver. The LM proposes strategies such as beam search and genetic algorithms, and the paper also measures how often generated code bypasses a sandbox.
- **Task fit:** No annotation/IE.
- VERIFIED: https://arxiv.org/abs/2310.02304 [AX; comment "COLM 2024"], [OR]

```bibtex
@inproceedings{fernando2024promptbreeder,
  title = {Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution},
  author = {Fernando, Chrisantha and Banarse, Dylan and Michalewski, Henryk and Osindero, Simon and Rockt{\"a}schel, Tim},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)}, year = {2024}, note = {arXiv:2309.16797}
}
```
- **(7) What it does:** It mutates a population of task-prompts with LLM-generated mutation-prompts that are themselves improved over evolution, evaluating fitness on a training set.
- **Task fit:** Its abstract includes hate speech classification, a labeling-type task.
- VERIFIED: https://arxiv.org/abs/2309.16797 [AX]; venue "ICML 2024" [OR]

```bibtex
@misc{zhang2026hyperagents,
  title = {Hyperagents},
  author = {Zhang, Jenny and Zhao, Bingchen and Yang, Wannan and Foerster, Jakob and Clune, Jeff and Jiang, Minqi and Devlin, Sam and Shavrina, Tatiana},
  year = {2026}, eprint = {2603.19461}, archivePrefix = {arXiv}
}
```
- **(8) What it does:** It integrates a task agent and a meta agent into one editable program whose meta-level modification procedure is itself editable, instantiated as DGM-Hyperagents.
- **Task fit:** No annotation/IE named in the abstract.
- VERIFIED: https://arxiv.org/abs/2603.19461 [AX]

```bibtex
@misc{karten2026continual,
  title = {Continual Harness: Online Adaptation for Self-Improving Foundation Agents},
  author = {Karten, Seth and Zhang, Joel and Upaa, Tersoo and Feng, Ruirong and Li, Wenzhe and Shi, Chengshuai and Jin, Chi and Vodrahalli, Kiran},
  year = {2026}, eprint = {2605.09998}, archivePrefix = {arXiv}
}
```
- **(9) What it does:** A reset-free self-improving harness for embodied agents (Pokemon Red/Emerald) in which the agent alternates between acting and refining its own prompt, sub-agents, skills and memory within a single run.
- **Task fit:** Not annotation/IE.
- VERIFIED: https://arxiv.org/abs/2605.09998 [AX]

```bibtex
@misc{hebbar2026sia,
  title = {{SIA}: Self Improving {AI} with Harness \& Weight Updates},
  author = {Hebbar, Prannay and Manawat, Yogendra and Verboomen, Samuel and Ivanova, Alesia and Palanimalai, Selvam and Bhatia, Kunal and Baskaran, Vignesh},
  year = {2026}, eprint = {2605.27276}, archivePrefix = {arXiv}
}
```
- **(10) What it does:** A Feedback-Agent updates both the harness and the weights of a task-specific agent, evaluated on Chinese legal charge classification, GPU kernel optimisation and single-cell RNA denoising.
- **Task fit:** One of its three domains is classification (LawBench, 191-class top-1 accuracy), but it is not annotation guidelines or IE.
- VERIFIED: https://arxiv.org/abs/2605.27276 [AX], [PDF grep]

Other harness-evolution papers I found (preprints, [AX] only):
```bibtex
@misc{xia2026regularized,
  title = {{RRSI}: Regularized Recursive Self-Improvement of Agent Harnesses},
  author = {Xia, Peng and Han, Rujun and Wang, Zifeng and Chen, Yanfei and Zhuang, Yufan and Lee, Yoonho and Huang, Chengsong and Yu, Han and CuiZhu, Zhongying and Ming, Yifei and Yao, Huaxiu and Gokturk, Burak and Pfister, Tomas and Lee, Chen-Yu},
  year = {2026}, eprint = {2609.24972}, archivePrefix = {arXiv}
}
@misc{chen2026failed,
  title = {From Failed Trajectories to Reliable {LLM} Agents: Diagnosing and Repairing Harness Flaws},
  author = {Chen, Mengzhuo and Wang, Junjie and Liu, Zhe and Wang, Yawen and Zheng, Haiming and Wang, Qing},
  year = {2026}, eprint = {2606.06324}, archivePrefix = {arXiv}
}
@misc{wang2026auditing,
  title = {Auditing Harness Tampering in Self-Improving Agents},
  author = {Wang, Xing and Zhang, Xiaoyi and Shao, Jie}, year = {2026}, eprint = {2609.00069}, archivePrefix = {arXiv}
}
@misc{wang2026do,
  title = {Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0},
  author = {Wang, Wenxiao and Kattakinda, Priyatham and Feizi, Soheil}, year = {2026}, eprint = {2607.14004}, archivePrefix = {arXiv}
}
```
- **RRSI:** It regularizes harness self-improvement against overfitting to training tasks, using a temporally annealed proposal budget, a critic that screens benchmark-specific proposals, and a pruner.
- **HarnessFix:** It diagnoses failed trajectories and repairs harness flaws, accepting patches through regression-aware validation (+6.3% to 18.4%).
- **Auditing Harness Tampering:** It defines "harness tampering," where self-improving agents' edits produce illusory gains or violate integrity constraints, and benchmarks audit methods.
- **Do Agent Optimizers Compound?** It runs a two-phase continual-learning evaluation of GEPA, Meta-Harness and RELAI-VCL on Terminal-Bench 2.0, finding gains compound only when regression control is built into the loop.
- VERIFIED: https://arxiv.org/abs/2609.24972, https://arxiv.org/abs/2606.06324, https://arxiv.org/abs/2609.00069 and https://arxiv.org/abs/2607.14004 [AX]

---

## E. Tool creation / skills

```bibtex
@inproceedings{cai2024large,
  title = {Large Language Models as Tool Makers},
  author = {Cai, Tianle and Wang, Xuezhi and Ma, Tengyu and Chen, Xinyun and Zhou, Denny},
  booktitle = {The Twelfth International Conference on Learning Representations (ICLR)}, year = {2024}, note = {arXiv:2305.17126}
}
```
- **What it does:** LATM is a closed loop where a strong LLM makes reusable tools and a lightweight LLM uses cached tools, cutting inference cost while matching GPT-4-for-both performance.
- VERIFIED: https://arxiv.org/abs/2305.17126 [AX]; venue "ICLR 2024 poster" [OR]

```bibtex
@inproceedings{qian2023creator,
  title = {{CREATOR}: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models},
  author = {Qian, Cheng and Han, Chi and Fung, Yi and Qin, Yujia and Liu, Zhiyuan and Ji, Heng},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023}, year = {2023}, pages = {6922--6939},
  doi = {10.18653/v1/2023.findings-emnlp.462}
}
```
- **What it does:** It lets LLMs create their own tools from documentation and code realization, disentangling abstract tool creation from concrete decision execution, and introduces the Creation Challenge dataset.
- VERIFIED: https://arxiv.org/abs/2305.14318 [AX; "Findings of EMNLP 2023"]. The pages and DOI come from the Semantic Scholar DOI and the Anthology .bib I fetched. Note the author in .bib is "Fung, Yi" whereas arXiv has "Yi R. Fung".

```bibtex
@inproceedings{schick2023toolformer,
  title = {Toolformer: Language Models Can Teach Themselves to Use Tools},
  author = {Schick, Timo and Dwivedi-Yu, Jane and Dess{\`\i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS 2023)}, year = {2023}, note = {arXiv:2302.04761}
}
```
- **What it does:** It trains a model, self-supervised from a handful of demonstrations per API, to decide which APIs to call, when and with what arguments, and how to use the results.
- VERIFIED: https://arxiv.org/abs/2302.04761 [AX]; venue "NeurIPS 2023 oral" [OR]

```bibtex
@inproceedings{wolflein2025llm,
  title = {{LLM} Agents Making Agent Tools},
  author = {W{\"o}lflein, Georg and Ferber, Dyke and Truhn, Daniel and Arandjelovi{\'c}, Ognjen and Kather, Jakob Nikolas},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  year = {2025}, pages = {26092--26130}, doi = {10.18653/v1/2025.acl-long.1266}, url = {https://aclanthology.org/2025.acl-long.1266/}
}
```
- **What it does:** ToolMaker takes a GitHub URL and a task description, installs dependencies and generates code to produce a tool, with closed-loop self-correction for debugging; it implements 80% of a 15-task benchmark with 100+ unit tests.
- VERIFIED: https://arxiv.org/abs/2502.11705 [AX]; .bib [ANTH]. The paper's title is "LLM Agents Making Agent Tools," and "ToolMaker" is the system name.

Anthropic "Agent Skills" (non-archival, official pages):
```bibtex
@misc{zhang2025equipping,
  title = {Equipping agents for the real world with {Agent Skills}},
  author = {Zhang, Barry and Lazuka, Keith and Murag, Mahesh},
  howpublished = {Anthropic Engineering blog}, month = oct, year = {2025},
  url = {https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills},
  note = {Non-archival. Published 2025-10-16; page notes a 2025-12-18 update publishing Agent Skills as an open standard (agentskills.io)}
}
@misc{anthropic2026agent,
  title = {Agent Skills (documentation overview)}, author = {{Anthropic}}, howpublished = {Claude Platform documentation},
  url = {https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview}, note = {Non-archival; accessed 2026-10-10}
}
```
- **Content:** A Skill is a directory with a SKILL.md file (YAML `name` and `description`) plus optional scripts and resources, loaded by progressive disclosure (metadata at startup, body when triggered, bundled files as needed). The docs page carries a security note to audit untrusted Skills.
- VERIFIED: both URLs [fetched]

---

## F. Benchmarks and metrics

```bibtex
@article{vangysel2021designing,
  title = {Designing a Uniform Meaning Representation for Natural Language Processing},
  author = {Van Gysel, Jens E. L. and Vigus, Meagan and Chun, Jayeol and Lai, Kenneth and Moeller, Sarah and Yao, Jiarui and O'Gorman, Tim and Cowell, Andrew and Croft, William and Huang, Chu-Ren and Haji{\v{c}}, Jan and Martin, James H. and Oepen, Stephan and Palmer, Martha and Pustejovsky, James and Vallejos, Rosa and Xue, Nianwen},
  journal = {KI - K{\"u}nstliche Intelligenz}, volume = {35}, number = {3--4}, pages = {343--360}, year = {2021}, doi = {10.1007/s13218-021-00722-w}
}
```
- **What it does:** It presents UMR, a framework built mainly on AMR that extends it to other, especially low-resource and morphologically complex languages and adds sentence-level features plus a companion document-level layer (coreference, temporal and modal dependencies).
- VERIFIED: https://dl.gi.de/items/8cfd8c72-2f52-48b1-a9d9-effd7038924c/full (authors, journal, pages, DOI); https://doi.org/10.1007/s13218-021-00722-w [CR]. The Springer page redirected to an auth endpoint, so I did not read it.

```bibtex
@inproceedings{bonn2024building,
  title = {Building a Broad Infrastructure for Uniform Meaning Representations},
  author = {Bonn, Julia and Buchholz, Matthew and Chun, Jayeol and Cowell, Andrew and Croft, William and Denk, Lukas and Ge, Sijia and Haji{\v{c}}, Jan and Lai, Kenneth and Martin, James H. and Myers, Skatje and Palmer, Alexis and Palmer, Martha and Post, Claire Ben{\'e}t and Pustejovsky, James and Stenzel, Kristine and Sun, Haibo and Ure{\v{s}}ov{\'a}, Zde{\v{n}}ka and Vallejos, Rosa and Van Gysel, Jens E. L. and Vigus, Meagan and Xue, Nianwen and Zhao, Jin},
  booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
  month = may, year = {2024}, address = {Torino, Italia}, publisher = {ELRA and ICCL}, pages = {2537--2547},
  url = {https://aclanthology.org/2024.lrec-main.229/}
}
```
- **What it does:** It reports the first release of the UMR dataset, covering six languages (Arapaho, Chinese, English, Kukama, Navajo, Sanapana), and describes UMR guidelines and tools.
- VERIFIED: https://aclanthology.org/2024.lrec-main.229/ [ANTH]

```bibtex
@inproceedings{sun2024anchor,
  title = {Anchor and Broadcast: An Efficient Concept Alignment Approach for Evaluation of Semantic Graphs},
  author = {Sun, Haibo and Xue, Nianwen},
  booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
  month = may, year = {2024}, address = {Torino, Italia}, publisher = {ELRA and ICCL}, pages = {1052--1062},
  url = {https://aclanthology.org/2024.lrec-main.94/}
}
```
- **What it does:** AnCast is a tool implementing concept F1, unlabeled, labeled and weighted relation F1 for graph meaning representations. Its anchor-broadcast alignment correlates highly with Smatch at about 40% of the compute time.
- VERIFIED: https://aclanthology.org/2024.lrec-main.94/ [ANTH]

```bibtex
@inproceedings{uzzaman2013semeval,
  title = {{S}em{E}val-2013 Task 1: {T}emp{E}val-3: Evaluating Time Expressions, Events, and Temporal Relations},
  author = {UzZaman, Naushad and Llorens, Hector and Derczynski, Leon and Allen, James and Verhagen, Marc and Pustejovsky, James},
  booktitle = {Second Joint Conference on Lexical and Computational Semantics (*{SEM}), Volume 2: Proceedings of the Seventh International Workshop on Semantic Evaluation ({S}em{E}val 2013)},
  month = jun, year = {2013}, address = {Atlanta, Georgia, USA}, publisher = {Association for Computational Linguistics}, pages = {1--9},
  url = {https://aclanthology.org/S13-2001/}
}
```
- **What it does:** It describes the TempEval-3 task, which aims to advance temporal information processing with a three-part structure (temporal expression, event and temporal relation extraction), a larger dataset, and new single overall quality measures.
- VERIFIED: https://aclanthology.org/S13-2001/ [ANTH]; abstract text from the first page of https://aclanthology.org/S13-2001.pdf. The Anthology page itself shows no abstract.

```bibtex
@inproceedings{pustejovsky2003timeml,
  title = {{TimeML}: Robust Specification of Event and Temporal Expressions in Text},
  author = {Pustejovsky, James and Casta{\~n}o, Jos{\'e} and Ingria, Robert and Saur{\'\i}, Roser and Gaizauskas, Robert and Setzer, Andrea and Katz, Graham and Radev, Dragomir},
  booktitle = {AAAI Spring Symposium 2003 (AAAI Technical Report SS-03-07)}, year = {2003},
  url = {https://cdn.aaai.org/Symposia/Spring/2003/SS-03-07/SS03-07-005.pdf},
  note = {Footnote on the paper: also appeared in substantially the same form at IWCS-5. Volume title ``New Directions in Question Answering'' is from a web-search summary, not from the PDF.}
}
```
- **What it does:** It describes TimeML, a specification language for event and temporal expressions that anchors events to temporal expressions, orders events relative to one another, and allows underspecified interpretation.
- VERIFIED: https://cdn.aaai.org/Symposia/Spring/2003/SS-03-07/SS03-07-005.pdf [PDF, title, authors and abstract read]. Pages are not shown in what I read.

```bibtex
@inproceedings{strotgen2010heideltime,
  title = {{H}eidel{T}ime: High Quality Rule-Based Extraction and Normalization of Temporal Expressions},
  author = {Str{\"o}tgen, Jannik and Gertz, Michael},
  booktitle = {Proceedings of the 5th International Workshop on Semantic Evaluation},
  month = jul, year = {2010}, address = {Uppsala, Sweden}, publisher = {Association for Computational Linguistics}, pages = {321--324},
  url = {https://aclanthology.org/S10-1071/}
}
```
- **What it does:** It describes HeidelTime, a rule-based system using regular-expression patterns and knowledge resources to extract and normalize temporal expressions; it was top-ranked in TempEval-2 Task A English (86% F1 extraction).
- VERIFIED: https://aclanthology.org/S10-1071/ [ANTH]; abstract from https://aclanthology.org/S10-1071.pdf first page.

Manifesto resources. I found no ManifestoBERTa paper, only a model card with a citation:
```bibtex
@misc{burst2024manifestoberta,
  title = {manifestoberta. Version 56topics.context.2024.1.1},
  author = {Burst, Tobias and Lehmann, Pola and Franzmann, Simon and Al-Gaddooa, Denise and Ivanusch, Christoph and Regel, Sven and Riethm{\"u}ller, Felicia and We{\ss}els, Bernhard and Zehnter, Lisa},
  publisher = {Wissenschaftszentrum Berlin f{\"u}r Sozialforschung (WZB) / G{\"o}ttinger Institut f{\"u}r Demokratieforschung (IfDem)},
  year = {2024}, doi = {10.25522/manifesto.manifestoberta.56topics.context.2024.1.1},
  url = {https://huggingface.co/manifesto-project/manifestoberta-xlm-roberta-56policy-topics-context-2024-1-1}
}
@misc{lehmann2026manifesto,
  title = {Manifesto Corpus. Version 2026-1},
  author = {Lehmann, Pola and Franzmann, Simon and Al-Gaddooa, Denise and Ivanusch, Christoph and Lewandowski, Jirka and Riethm{\"u}ller, Felicia and Samstag, Svenja and Zehnter, Lisa},
  publisher = {WZB Berlin Social Science Center / Institute for Democracy Research (IfDem)}, year = {2026},
  url = {https://manifesto-project.wzb.eu/information/documents/corpus}
}
```
- **burst2024manifestoberta:** The model card describes an xlm-roberta-large fine-tuned on about 1.7 million annotated statements from the Manifesto Corpus (version 2024a) to classify text into 56 policy topics under Handbook 4. The card's BibTeX is truncated on the page, so the entry above is reconstructed from its prose citation and visible fields.
- **lehmann2026manifesto:** This is the current recommended citation on the Manifesto Project corpus page; the corpus spans 60+ countries and 40 languages, with about 2,000 programmes carrying coded quasi-sentences. The page shows no DOI and names Lehmann et al., not Burst, for version 2026-1.
- VERIFIED: the HuggingFace model card URL above, and https://manifesto-project.wzb.eu/information/documents/corpus

```bibtex
@article{laurer2024less,
  title = {Less Annotating, More Classifying: Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and {BERT-NLI}},
  author = {Laurer, Moritz and van Atteveldt, Wouter and Casas, Andreu and Welbers, Kasper},
  journal = {Political Analysis}, volume = {32}, number = {1}, pages = {84--100}, year = {2024}, doi = {10.1017/pan.2023.20},
  note = {Crossref shows online date 2023-06-09; year 2024 inferred from volume 32}
}
```
- **What it does:** Not seen from an abstract. I only read the Crossref bibliographic record.
- VERIFIED (bibliographic data only): https://doi.org/10.1017/pan.2023.20 [CR]. NOT VERIFIED: the paper's abstract and content.

```bibtex
@misc{wang2024selecting,
  title = {Selecting Between {BERT} and {GPT} for Text Classification in Political Science Research},
  author = {Wang, Yu and Qu, Wen and Ye, Xin}, year = {2024}, eprint = {2411.05050}, archivePrefix = {arXiv}
}
```
- **What it does:** It compares fine-tuned BERT with prompted GPT models across political-science classification tasks in low-data settings, finding zero/few-shot GPT falls short of or at best matches BERT fine-tuning as training sets reach about 1,000 samples.
- **Details from the full text [PDF]:** The experiments use GPT-4o. The 8-class manifesto task uses the Laurer et al. dataset (originally from WZB), and prompting lags fine-tuned RoBERTa-large by a sizeable margin. The paper also covers economic-news sentiment and other tasks.
- VERIFIED: https://arxiv.org/abs/2411.05050 [AX] and https://arxiv.org/pdf/2411.05050 [PDF]

LLMs on UMR / AMR parsing / TempEval-3 (the closest real items):
```bibtex
@inproceedings{sun2024chinese,
  title = {{C}hinese {UMR} annotation: Can {LLM}s help?},
  author = {Sun, Haibo and Xue, Nianwen and Zhao, Jin and Yue, Liulu and Sun, Yao and Xu, Keer and Wu, Jiawei},
  booktitle = {Proceedings of the Fifth International Workshop on Designing Meaning Representations @ LREC-COLING 2024},
  month = may, year = {2024}, address = {Torino, Italia}, publisher = {ELRA and ICCL}, pages = {131--139},
  url = {https://aclanthology.org/2024.dmr-1.14/}
}
```
- **What it does:** It uses few-shot and Think-Aloud prompting of GPT-4 to draft sentence-level Chinese UMR graphs for humans to revise, reducing annotation time by two thirds on average.
- VERIFIED: https://aclanthology.org/2024.dmr-1.14/ [ANTH]

```bibtex
@inproceedings{ettinger2023you,
  title = {``You Are An Expert Linguistic Annotator'': Limits of {LLM}s as Analyzers of Abstract Meaning Representation},
  author = {Ettinger, Allyson and Hwang, Jena and Pyatkin, Valentina and Bhagavatula, Chandra and Choi, Yejin},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023}, year = {2023}, pages = {8250--8263},
  doi = {10.18653/v1/2023.findings-emnlp.553}, url = {https://aclanthology.org/2023.findings-emnlp.553/}
}
```
- **What it does:** It tests GPT-3, ChatGPT and GPT-4 on AMR parsing, directly via zero/few-shot prompts and indirectly via metalinguistic queries (the abstract is not quoted from the page; the Anthology .bib confirms venue and pages).
- VERIFIED: https://arxiv.org/abs/2310.17793 [AX; comment "EMNLP 2023 Findings (short)"]; .bib [ANTH]. My summary of the results came from a search-engine summary rather than the abstract text, so treat the finding "near-0% fully accurate parses" as NOT VERIFIED.

```bibtex
@inproceedings{wein2025can,
  title = {Can Uniform Meaning Representation Help {GPT-4} Translate from Indigenous Languages?},
  author = {Wein, Shira},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  year = {2025}, pages = {278--285}, doi = {10.18653/v1/2025.acl-short.23}, url = {https://aclanthology.org/2025.acl-short.23/}
}
@inproceedings{markle2025generating,
  title = {Generating Text from Uniform Meaning Representation},
  author = {Markle, Emma and Iranmanesh, Reihaneh and Wein, Shira},
  booktitle = {Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
  year = {2025}, pages = {259--271}, doi = {10.18653/v1/2025.ijcnlp-long.16}, url = {https://aclanthology.org/2025.ijcnlp-long.16/}
}
@inproceedings{markle2026setup,
  title = {{SETUP}: Sentence-level English-To-Uniform Meaning Representation Parser},
  author = {Markle, Emma and Gutierrez Bach, Javier and Wein, Shira},
  booktitle = {Proceedings of LREC 2026}, year = {2026}, note = {arXiv:2512.07068; ``LREC 2026 Camera-ready'' per arXiv comment; no Anthology page checked}
}
```
- **wein2025can:** It incorporates UMR annotations into GPT-4 prompts for translation from Navajo, Arápaho and Kukama; UMR gave a significant gain in most cases.
- **markle2025generating:** It studies the first approaches to text generation from multilingual UMR graphs (fine-tuned AMR-to-text models).
- **markle2026setup:** Its English text-to-UMR parser fine-tunes AMR parsers or uses a Universal Dependencies converter, reaching AnCast 84 and SMATCH++ 91. It is not a prompting paper but is useful because it reports AnCast.
- VERIFIED: https://arxiv.org/abs/2502.08900, https://arxiv.org/abs/2502.11973, https://arxiv.org/abs/2512.07068 [AX]; .bib [ANTH] for the first two only.

```bibtex
@inproceedings{gautam2024discourse,
  title = {Discourse-Aware In-Context Learning for Temporal Expression Normalization},
  author = {Gautam, Akash and Lange, Lukas and Str{\"o}tgen, Jannik},
  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},
  month = jun, year = {2024}, address = {Mexico City, Mexico}, publisher = {Association for Computational Linguistics}, pages = {306--315},
  doi = {10.18653/v1/2024.naacl-short.27}, url = {https://aclanthology.org/2024.naacl-short.27/}
}
```
- **What it does:** It explores proprietary and open-source LLMs for temporal-expression normalization using in-context learning with different example-selection strategies.
- **TempEval-3 use [PDF]:** TempEval3 is one of four evaluation datasets, with GPT-3.5-turbo and Zephyr, and the TempEval3 evaluation script is used for temporal tagging setups. This covers TIMEX normalization only, not events or TLINKs.
- The author appears as "Akash Gautam" on the Anthology and as "Akash Kumar Gautam" on arXiv.
- VERIFIED: .bib [ANTH]; https://arxiv.org/abs/2404.07775 [AX]; https://arxiv.org/pdf/2404.07775 [PDF]

```bibtex
@inproceedings{yuan2023zero,
  title = {Zero-shot Temporal Relation Extraction with {ChatGPT}},
  author = {Yuan, Chenhan and Xie, Qianqian and Ananiadou, Sophia},
  booktitle = {Proceedings of the 22nd Workshop on Biomedical Natural Language Processing and BioNLP Shared Tasks},
  year = {2023}, pages = {92--102}, doi = {10.18653/v1/2023.bionlp-1.7}
}
```
- **What it does:** It evaluates ChatGPT on zero-shot temporal relation extraction with three prompt techniques and finds a large gap to supervised methods.
- **Note:** The full text contains no mention of TempEval, so it is not a TempEval-3 evaluation.
- VERIFIED: https://arxiv.org/abs/2304.05454 [AX]; .bib [ANTH]

---

## G. Evaluation methodology

```bibtex
@article{gama2013on,
  title = {On evaluating stream learning algorithms},
  author = {Gama, Jo{\~a}o and Sebasti{\~a}o, Raquel and Rodrigues, Pedro Pereira},
  journal = {Machine Learning}, volume = {90}, number = {3}, pages = {317--346}, doi = {10.1007/s10994-012-5320-9},
  note = {Crossref online-first date 2012-10-24; print year 2013 is not shown in the record I read}
}
@article{dawid1984present,
  title = {Present Position and Potential Developments: Some Personal Views: Statistical Theory: The Prequential Approach},
  author = {Dawid, A. P.}, journal = {Journal of the Royal Statistical Society. Series A (General)}, volume = {147}, number = {2}, pages = {278--}, year = {1984},
  doi = {10.2307/2981683}, note = {end page not shown in Crossref record}
}
```
- **gama2013on:** Not read from an abstract. I only saw the bibliographic record and the title.
- **dawid1984present:** Same: I saw the bibliographic record and the title only. I did not read either paper's text, so I cannot confirm from a page that either paper defines test-then-train evaluation.
- VERIFIED (bibliographic data only): https://doi.org/10.1007/s10994-012-5320-9 and https://doi.org/10.2307/2981683 [CR]. NOT VERIFIED: that these papers define prequential or interleaved test-then-train evaluation (your claim, which I could not check on a page).

Closest "sequential / online" items. No benchmark of continual prompt learning with explicit test-then-train evaluation was found; these are partial matches:
```bibtex
@misc{guan2026continualskillbench,
  title = {{ContinualSkillBench}: Can {LLM} Agents Truly Evolve Their Capabilities?},
  author = {Guan, Tianyi and Wang, Yiding and Yang, Haotong and Cao, Siyuan and Liu, Shirui and Hu, Yi and Li, Jiaqi and Zhang, Muhan},
  year = {2026}, eprint = {2608.03874}, archivePrefix = {arXiv}
}
@misc{bornschein2025fine,
  title = {Fine-Tuned In-Context Learners for Efficient Adaptation},
  author = {Bornschein, Jorg and Lyle, Clare and Li, Yazhe and Rannen-Triki, Amal and He, Xu Owen and Pascanu, Razvan},
  year = {2025}, eprint = {2512.19879}, archivePrefix = {arXiv}
}
```
- **guan2026continualskillbench:** A dynamic framework for in-context continual skill learning with 5 domains of 100 ordered subtasks each. It finds in-context learning comparable to explicit skill maintenance on average.
- **bornschein2025fine:** It proposes prequential evaluation for hyperparameter selection in the low-data regime for adapting LLMs. This is a recent use of prequential evaluation in LLM adaptation, but not a prompt-learning benchmark.
- **wang2026do** (D) is also a sequential evaluation, of harness optimizers.
- VERIFIED: https://arxiv.org/abs/2608.03874 and https://arxiv.org/abs/2512.19879 [AX]. Both are preprints.

---

## H. Brief checks (i)-(iii)

**(i) Harness as the unit of optimization for LLM annotation / IE.** I found none.
- The closest are yuan2026calico (a codebook-to-prompt workflow, edits prompts only) and the generic harness optimizers in D whose tasks include classification or labeling (lee2026metaharness, ye2026meta with FiNER, hebbar2026sia, fernando2024promptbreeder).
- I found no paper that evolves tools plus per-step instructions plus the chain of LLM calls for annotation, UMR or TimeML.
- Targeted arXiv searches combining annotation or IE with ADAS/AFlow-style workflow search returned nothing relevant.

**(ii) Admission control / reviewer / verification gates for self-modifying agents.** Real papers I found:
- Self-Harness: accepts edits only after regression testing (zhang2026self).
- HarnessFix: accepts patches through regression-aware validation (chen2026failed).
- RRSI: a critic screens benchmark-specific proposals and a pruner removes edits (xia2026regularized).
- AHE: every edit carries a prediction verified next round (lin2026agentic).
- DGM: empirically validates each change (zhang2026darwin).
- Auditing Harness Tampering: audits illusory gains (wang2026auditing).
- Do Agent Optimizers Compound?: gains compounded only with regression control in the loop (wang2026do).
- CoEvoSkills (COLM 2026 per OpenReview, arXiv 2604.01687, Zhang et al.): a skill generator co-evolves with a surrogate verifier that gives feedback without ground-truth test content.
- Coalition-Aware Skill Reliability for Self-Evolving Agents (arXiv 2608.22610, Zhao et al.): audits skill banks and finds "coalition pollution" and "cross-domain utility reversal."
- Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries (Yubo Li, TMLR 2026, arXiv 2607.10113): describes a "verify and admit candidates" lifecycle stage.
- Safety in Self-Evolving Agents: A Survey (Jiahao Chen et al., arXiv 2610.00093): lists admission among reusable-state safety stages.
- All of these are verified via [AX]; venues for Li and Zhang are from the arXiv comment and [OR].
- Anthropic's Skills docs also include a security section on auditing untrusted Skills.

**(iii) Data-leakage / contamination guards when an LLM edits its own prompt with gold data.** I found no paper dedicated to this. Related pieces:
- Kim et al. 2026 (A1) separate a 10-document refinement set from a 100-document evaluation set and withhold test sets.
- Self-Harness reports held-in vs held-out pass rates.
- RRSI addresses overfitting by memorizing training tasks.
- Auditing Harness Tampering defines the "illusory gain" failure.
- singh2026mage reports that fixed prompts beat reflective optimizers at Ntrain=30.
- A search snippet attributed a similar overfitting remark to OPRO's paper, but I did not verify it in the paper, so I do not rely on it.

---

## Items NOT found, not verified, or only partly verified

1. **A ManifestoBERTa paper.** Only the HuggingFace model card (Burst et al. 2024 citation; BibTeX truncated on the page) and the Manifesto Corpus citation page.
2. **LLM evaluation on full TempEval-3** (events and TLINKs as well as timexes). Only the TIMEX-normalization study (Gautam et al.) and Su et al. (arXiv 2507.06450, SCATE time normalization on TempEval-2013 data; I only saw it as an arXiv record and did not read it as a prompting study).
3. **LLM prompting for full document-level UMR parsing.** Not found. The nearest are Sun et al. 2024 (GPT-4 drafts sentence-level Chinese UMR), Wein 2025 (UMR as a prompt component for translation) and SETUP (fine-tuned/converter parser, not prompting).
4. **A sequential/online continual prompt-learning benchmark with prequential evaluation.** Not found; only partial matches (G).
5. **Harness-as-unit-of-optimization for LLM annotation/IE** (H-i). **A leakage-guard study for LLM-edited prompts** (H-iii).
6. **Fernandes et al. 2025** (Text2Story, LLM-assisted annotation-scheme development). Seen only in the Kim et al. 2026 reference list; not looked up.
7. **Not opened:**
   - Springer (Van Gysel 2021 KI) article page; verified via GI Digital Library and Crossref instead.
   - PNAS (Gilardi) page; I used arXiv and Crossref.
   - OpenReview forum pages (bot challenge); venue strings for GoLLIE, APE, OPRO, DSPy, GEPA, ACE, DGM, ADAS, AFlow, LATM, Huang et al., AWM, Promptbreeder, STOP, Reflexion, Self-Refine, Voyager, SWE-agent, Toolformer, Meta-Harness, CoEvoSkills and Li (skills survey) come from OpenReview search-API records.
8. **Venue details not verified.**
   - ExpeL (AAAI-24): volume and pages not seen.
   - Voyager (TMLR): volume not seen.
   - Reflexion, Self-Refine, Toolformer and SWE-agent: NeurIPS volume and pages not seen.
   - TimeML: pages not seen, and the symposium volume title is unverified.
   - SkillWeaver, SICA and Hyperagents: no published venue found.
9. **Zambrano et al.** (Data Plus Theory Equals Codebook): journal and year not shown on the page I read; the "does not use a disagreement-driven loop" statement is based on the first 100k of 136k characters.
10. **Ettinger et al.** The "virtually 0% fully accurate parses" finding I saw only in a search summary, not in the abstract text I read.
11. **Laurer et al. and Gama / Dawid.** I saw only bibliographic records; I did not read abstracts, so the one-line contents are not supplied (see F and G).
12. **Gama et al.** The print year 2013 is the user's; Crossref only shows the 2012-10-24 online date for vol. 90 issue 3.
13. **arXiv metadata caveat.** For arXiv-only entries I read the arXiv API record, not the abs web page. That record holds the same title, authors, date, comment and abstract.