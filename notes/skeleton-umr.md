# Learning to Parse Uniform Meaning Representation from Its Guideline and Fifty Sentences

## Abstract

## 1 Introduction
- UMR and why it matters
- A complex scheme with little data
- Reading the guideline is not enough
- Approach
- Results
- What we learn
- Contributions

## 2 Uniform Meaning Representation
- What UMR adds to AMR
- 11 fine-grained judges
- 4 possible sources of difficulty
- The shared task and prior systems
- Figure 1: a UMR annotation
- Table 1: the 11 judges and their possible sources of difficulty

## 3 Method
### 3.1 Seed
- Seed annotator written from the guideline

### 3.2 Improvement
- Feedback from the fine-grained judges
- Edits that improve the existing generator
- Edits that add steps
- Admission
- Figure 2: seed and improvement

## 4 Experiments
- Data
- Metrics: AnCast++ and juːmæʧ
- Models and baselines

## 5 Results
### 5.1 Comparison with the baselines
- Table 2: main results

### 5.2 Errors of the baselines
- Where the guideline-prompt baseline loses
- A Chinese-specific failure
- The seed from the guideline

### 5.3 Our results
- Seed to learned annotator
- Against the fine-tuned systems
- Against the guideline in the prompt
- Variation between runs
- Ruling out simpler explanations

### 5.4 RSI learning curves
- Figure 3: learning curves
- The gain comes in the first rounds

## 6 Analysis: What Was Learned and What Was Not
### 6.1 The annotator before and after
- Table 3: instructions before and after
- Size
- From the guideline's notation to the data's
- The critic had to be restrained
- Learned instructions are rules with words, not examples

### 6.2 What kinds of edits were made
- Table 4: edits by type
- Most edits state conventions

### 6.3 Which judges moved, and why
- Table 5: scores per judge
- Conventions transfer almost fully
- Lookups transfer in part
- Rule code fixes format, not meaning

### 6.4 Why some judges do not move
- Criteria fit the training group, not the test
- Temporal anchoring: rules that contradict each other
- Side effects of consolidation
- Not noisy gold
- What the builder said about the gold

### 6.5 What is learned is about UMR
- Other annotating models

### 6.6 Ablations
- Table 6: ablations
- The instructions carry the gain

## 7 Related Work
- AMR and UMR parsing with language models
- LLMs as annotators and guideline refinement
- Self-improvement

## 8 Conclusion
- Answers
- For UMR annotation projects

## Limitations
- Scale and variance
- Edit coding
- Models and data
- Design choices

## Ethics Statement

## Appendix
- A Data and splits
- B The fine-grained judges
- C Prompts
- D Round-by-round records
- E Edit coding
- F Other annotating models
- G Trajectory excerpts
- H Cost
