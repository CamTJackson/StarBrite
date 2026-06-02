# STAR-BRiTE
## Scientific Time-series Analysis and Belief Revision in Time-series Evaluation

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5.5-green)
![Kepler](https://img.shields.io/badge/NASA-Kepler-orange)
![Status](https://img.shields.io/badge/Project-Research_Benchmark-purple)

---

# Overview

STAR-BRiTE is a human-factors benchmark designed to evaluate how AI systems influence scientific reasoning during astronomical discovery tasks.

Unlike traditional benchmarks that focus only on prediction accuracy, STAR-BRiTE measures:

- Classification Accuracy
- Scientific Reasoning Quality
- Confidence Calibration
- Human-AI Agreement
- Uncertainty Communication
- Belief Revision

The benchmark uses real NASA Kepler light curve observations and compares human judgments against AI-generated classifications and explanations.

---

# Research Question

Can AI systems support scientific reasoning without encouraging overreliance or automation bias?

STAR-BRiTE investigates how scientists and AI systems interpret stellar light curves and whether AI appropriately expresses uncertainty when evidence is ambiguous.

---

# Dataset Composition

| Category | Count |
|-----------|---------|
| Likely False Positives | 20 |
| Likely Genuine Eclipsing Binaries | 30 |
| Triple Star Systems | 1 |
| Multi-Star Systems | 1 |
| Unknown / Ambiguous Cases | Included |

Total benchmark targets: **52**

Source:
- NASA Kepler Mission
- Kepler Input Catalog (KIC)

---

# Human Reviewers

Five independent reviewers participate in the benchmark.

| Reviewer |
|-----------|
| Professor A |
| Professor B |
| Graduate Student A |
| Graduate Student B |
| Industry Professional |

Human reasoning is optional.

Human confidence is required.

Confidence scale:

1 = Very Low Confidence

5 = Very High Confidence

---

# Benchmark Workflow

```text
Kepler Target
      |
      v
Lightkurve Download
      |
      v
Feature Extraction
      |
      v
Human Classification
      |
      v
Human Confidence
      |
      v
GPT Classification
      |
      v
GPT Reasoning
      |
      v
Human vs AI Comparison
      |
      v
Belief Revision Analysis
      |
      v
Benchmark Results
```

---

# Light Curve Processing

The project uses Lightkurve to download real Kepler observations.

Extracted features include:

- Mean Flux
- Standard Deviation
- Minimum Flux
- Maximum Flux
- Number of Observations

These features are provided to GPT for scientific interpretation.

---

# AI Evaluation

GPT is required to return:

- Classification
- Confidence Score
- Scientific Reasoning
- Uncertainty Statement

Possible classifications:

- Eclipsing Binary
- False Positive
- Triple Star System
- Multi-Star System
- Unknown

The Unknown category is intentionally included to evaluate uncertainty calibration.

---

# Metrics

## 1. Classification Accuracy

Measures whether classifications match benchmark labels.

## 2. Human-AI Agreement

Measures how frequently human reviewers and GPT reach the same conclusion.

## 3. Confidence Calibration

Measures whether confidence levels align with correctness.

## 4. Uncertainty Reporting

Measures whether GPT appropriately communicates limitations.

## 5. Belief Revision Score

Measures disagreement between initial human judgment and AI judgment.

---

# Example Visualizations

## Reviewer Accuracy

Tracks performance across all reviewers.

## Confidence Distribution

Visualizes reviewer confidence levels.

## Human vs GPT Agreement

Evaluates consensus and disagreement.

## Belief Revision Analysis

Measures shifts between human and AI conclusions.

---

# Installation

Additional dependency:

```bash
pip install lightkurve
```

---

# Running the Benchmark

Generate GPT outputs:

```bash
python gpt_runner.py
```

Run evaluation:

```bash
python main.py
```

---

# Project Contribution

STAR-BRiTE contributes a reusable benchmark for evaluating human factors in AI-assisted scientific discovery.

The benchmark extends beyond accuracy-based evaluation by measuring how AI influences scientific reasoning, confidence, uncertainty, and decision-making.

---

# Author

Cameron T. Jackson
