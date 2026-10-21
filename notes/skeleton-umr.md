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

## 2 UMR and Related Work
### 2.1 What UMR represents
- What UMR adds to AMR
- Eleven layers and four kinds of difficulty
- Figure 1: a UMR annotation and its layers
- Table 1: layers, difficulty types, judge checks

### 2.2 Data and prior systems
- Shared task

### 2.3 Related work
- AMR parsing with language models
- LLMs as annotators and guideline refinement
- Self-improvement

## 3 Method
- Seed annotator
- Feedback per layer
- Edits
- Admission
- One round
- Figure 2: one round of revision

## 4 Experimental Setup
- Data
- Metrics
- Models and baselines
- Reproducibility

## 5 Results
### 5.1 Reading the guideline is not enough
- Where the guideline-prompt baseline loses
- A Chinese-specific failure
- The seed from the guideline

### 5.2 Main results
- Table 2: main results
- Seed to learned annotator
- Against the fine-tuned systems
- Against the guideline in the prompt
- Variation between runs
- Ruling out simpler explanations

### 5.3 How many sentences are needed
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

### 6.3 Which layers moved, and why
- Table 5: per-layer scores
- Conventions transfer almost fully
- Lookups transfer in part
- Rule code fixes format, not meaning

### 6.4 Why some layers do not move
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

## 7 Conclusion
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
- B The judge and the layers
- C Prompts
- D Round-by-round records
- E Edit coding
- F Other annotating models
- G Trajectory excerpts
- H Cost
