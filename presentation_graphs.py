
"""
presentation_graphs.py

Creates polished presentation graphs from:
    combined_human_ai_results.csv

Outputs:
    graphs/
        accuracy_by_source.png
        confidence_comparison.png
        class_distribution.png
        agreement_rate.png
        confusion_like_comparison.png

Usage:
    python presentation_graphs.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "combined_human_ai_results.csv"

OUTPUT_DIR = Path("graphs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# --------------------------------------------------
# Graph 1: Human vs GPT Accuracy
# --------------------------------------------------

human_acc = (
    (df["human_classification"] == df["ground_truth"])
    .mean() * 100
)

gpt_acc = (
    (df["gpt_classification"] == df["ground_truth"])
    .mean() * 100
)

plt.figure(figsize=(7, 5))
plt.bar(
    ["Human", "GPT"],
    [human_acc, gpt_acc]
)
plt.ylabel("Accuracy (%)")
plt.title("Classification Accuracy")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "accuracy_by_source.png")
plt.close()

# --------------------------------------------------
# Graph 2: Confidence Comparison
# --------------------------------------------------

human_conf = df["human_confidence"].mean()
gpt_conf = df["gpt_confidence"].mean()

plt.figure(figsize=(7, 5))
plt.bar(
    ["Human", "GPT"],
    [human_conf, gpt_conf]
)
plt.ylabel("Average Confidence")
plt.title("Average Confidence Comparison")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "confidence_comparison.png")
plt.close()

# --------------------------------------------------
# Graph 3: Ground Truth Distribution
# --------------------------------------------------

counts = df["ground_truth"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(
    counts.index,
    counts.values
)
plt.ylabel("Count")
plt.title("Benchmark Dataset Composition")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "class_distribution.png")
plt.close()

# --------------------------------------------------
# Graph 4: Human-AI Agreement
# --------------------------------------------------

agreement = (
    (df["human_classification"]
     == df["gpt_classification"])
    .mean() * 100
)

plt.figure(figsize=(6, 5))
plt.bar(
    ["Agreement"],
    [agreement]
)
plt.ylim(0, 100)
plt.ylabel("Agreement (%)")
plt.title("Human vs GPT Agreement")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "agreement_rate.png")
plt.close()

# --------------------------------------------------
# Graph 5: Category-Level Accuracy
# --------------------------------------------------

rows = []

for category in df["ground_truth"].unique():

    subset = df[df["ground_truth"] == category]

    human = (
        (subset["human_classification"]
         == subset["ground_truth"])
        .mean() * 100
    )

    gpt = (
        (subset["gpt_classification"]
         == subset["ground_truth"])
        .mean() * 100
    )

    rows.append(
        {
            "Category": category,
            "Human": human,
            "GPT": gpt
        }
    )

acc_df = pd.DataFrame(rows)

x = range(len(acc_df))

plt.figure(figsize=(10, 5))

width = 0.4

plt.bar(
    [i - width/2 for i in x],
    acc_df["Human"],
    width=width,
    label="Human"
)

plt.bar(
    [i + width/2 for i in x],
    acc_df["GPT"],
    width=width,
    label="GPT"
)

plt.xticks(x, acc_df["Category"], rotation=20)
plt.ylabel("Accuracy (%)")
plt.title("Accuracy by Classification Category")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "confusion_like_comparison.png")
plt.close()

print("Graphs written to graphs/")
