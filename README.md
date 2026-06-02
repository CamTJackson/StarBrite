# STAR-BRiTE

## Belief Revision in Time-Series Evaluation

STAR-BRiTE is a benchmark designed to evaluate human factors in AI-assisted scientific discovery using Kepler light curve data.

Unlike traditional astronomy benchmarks that focus solely on classification accuracy, STAR-BRiTE measures how AI systems influence scientific reasoning, uncertainty handling, confidence calibration, and belief revision.

## Research Motivation

Scientists increasingly use AI systems to assist with data analysis and interpretation. While many benchmarks evaluate whether an AI system produces the correct answer, fewer evaluate how AI affects the scientific decision-making process.

STAR-BRiTE focuses on:
- Scientific reasoning quality
- Human-AI agreement
- Confidence calibration
- Uncertainty communication
- Belief revision

## Scientific Domain

Astronomy (Astrophysics)

### Classes
- Eclipsing_Binary
- False_Positive
- Triple_System
- Multi_Star
- Unknown

## Human Reviewers

- Professor A
- Professor B
- Graduate Student A
- Graduate Student B
- Industry Professional

## Benchmark Workflow

Kepler Target
→ Human Classification
→ Human Confidence
→ GPT Evaluation
→ Merge Results
→ Agreement Analysis
→ Belief Revision Metrics
→ Benchmark Report

## Evaluation Metrics

- Classification Accuracy
- Human Accuracy
- Human-AI Agreement
- Belief Revision Score
- Uncertainty Score
- Confidence Calibration

## Running

```bash
pip install pandas numpy matplotlib lightkurve openai
python main.py
```
