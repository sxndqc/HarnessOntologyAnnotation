# Manifesto Project classification: published results (literature check)

Collected by a research subagent that opened each paper, model card or report and read the number in it; I did not
re-read the sources myself. Short answer: **nobody has published an 8-way domain result for ManifestoBERTa or for a
prompted LLM on this data**. The best 8-class, English, supervised comparators are about 0.64-0.70 accuracy.

| System | Level | Metric = number | Test data | Source |
|---|---|---|---|---|
| ManifestoBERTa 2024-1-1, sentence | 56 topics | acc .57, macro-F1 .45 | 203 held-out manifestos, 200,920 statements, all languages | HF model card; manifesto-project.wzb.eu/uploads/manifestoberta_sentence_2024_1_1_56topics_perf_report.pdf |
| same, context | 56 | acc .64, macro-F1 .53 (top-3 .88) | same | same, `context` report |
| Assenmacher et al., BERT-base (DistilBERT) | 8 domains, English | acc .6977 (.6866), macro-F1 .5841 (.5694) | random 10% of a 7-country English corpus (11,452) | arXiv 2307.16511 = ACL 2024.swisstext-1.2, Table 2 |
| Osnabruegge, Ash, Morelli, TF-IDF + logistic regression | 8 | acc .641, macro-F1 .523, balanced acc .504 | 25% random hold-out of 115,410 English statements | doi.org/10.1017/pan.2021.37, Table 2 |
| Laurer et al. 2024, DeBERTa-v3-base (NLI) | 8 | acc .644 (.629), macro-F1 .525 (.521) at 10,000 training examples | 33,412 test sentences, document-level 70/30 split, English | doi.org/10.1017/pan.2023.20, Suppl. Table 27 |
| Laurer, BERT-NLI, zero training data | 8 | acc .036, F1 .059 (over-predicts "no topic", their footnote 15) | same | same |
| Policy-DistilBERT-7d (Laurer) | 7 | acc .771, balanced acc .745, weighted F1 .773 | random 15% of 129,669 sentences | huggingface.co/MoritzLaurer/policy-distilbert-7d |
| Chatsiou 2020, CNN+BERT | 7 | acc 87.52%, F1 74.68 | random 15% of 86,500 English sentences | arXiv 2010.10267 (an unreviewed outlier) |
| GPT-4o, zero/few-shot (Wang, Qu, Ye 2024) | 8 | acc <= .488 (six settings, .469-.488); fine-tuned RoBERTa-large .539 / .567 / .582 at 200 / 500 / 1,000 labels | 300 sentences from Laurer's data | arXiv 2411.05050, Fig. 2 |
| Llama-3-8B / Mistral-7B zero-shot (Halterman & Keith) | 142 codes | weighted F1 .21 / .14 | 1,732 dev sentences from 13 English manifestos | arXiv 2407.10747 |
| Dayanik et al. 2022, BERT | 56 | English macro-F1 35.9 | random 20% | ACL Findings 2022.findings-acl.186 |

**ManifestoBERTa and our sentences.** Per the 2024-1-1 context model card, it was trained on all quasi-sentences of the
2024a corpus minus a 10% held-out set of manifestos (1,828 train, 203 test), and the held-out manifestos are not listed.
About 90% of the English sentences of the corpus were therefore in its training data: our run of it
(`baseline manifestoberta`) is a reference, not a fair comparison. No 7- or 8-domain figure is published for it.

**The data.** siacus/manifesto has 34,619 rows, with label shares welfare 31.4%, economy 25.2%, fabric of society 11.0%,
political system 10.1%, social groups 10.0%, external relations 6.6%, freedom and democracy 4.8%, no topic 0.8%. Its
card has only the licence; no accuracy number, paper or model is linked to it. It resembles the English corpus of
Laurer et al. and Osnabruegge et al., but its provenance is not verified. Published 8-class numbers therefore use
other splits of similar data: comparable in kind, not the same test set.

**Not comparable to 8-way domain classification:** all ManifestoBERTa figures (56-way), Dayanik, Halterman & Keith, the
7-way systems (no "no topic" class), and the papers that estimate party positions or code tweets.

**Not verified:** any peer-reviewed validation of ManifestoBERTa; any Claude, GPT-3.5 or GPT-4 result on 56 categories;
any 8-way LLM result other than Wang et al.
