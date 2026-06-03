import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import confusion_matrix

# Load data
file_path = Path(__file__).resolve().parent / "star_brite_results.csv"
df = pd.read_csv(file_path)

# Create output folder one level above the results CSV file
output_dir = file_path.parent.parent / "graphs"
output_dir.mkdir(exist_ok=True)

# 1. Ground Truth Distribution
plt.figure(figsize=(8, 5))
df["ground_truth"].value_counts().sort_index().plot(kind="bar")
plt.title("Ground Truth Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(output_dir / "ground_truth_distribution.png")
plt.close()

# 2. Human Classification Distribution
plt.figure(figsize=(8, 5))
df["classification"].value_counts().sort_index().plot(kind="bar")
plt.title("Human Classification Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(output_dir / "human_classification_distribution.png")
plt.close()

# 3. GPT Classification Distribution
plt.figure(figsize=(8, 5))
df["gpt_classification"].value_counts().sort_index().plot(kind="bar")
plt.title("GPT Classification Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(output_dir / "gpt_classification_distribution.png")
plt.close()

# 4. Accuracy Comparison
human_acc = ((df["classification"] == df["ground_truth"]).mean() * 100)
gpt_acc = ((df["gpt_classification"] == df["ground_truth"]).mean() * 100)

plt.figure(figsize=(6, 5))
plt.bar(["Human Reviewer", "GPT"], [human_acc, gpt_acc])
plt.ylabel("Accuracy (%)")
plt.title("Accuracy Comparison")
plt.ylim(0, 100)

for i, v in enumerate([human_acc, gpt_acc]):
    plt.text(i, v + 1, f"{v:.1f}%", ha="center")

plt.tight_layout()
plt.savefig(output_dir / "accuracy_comparison.png")
plt.close()

# 5. Human Confusion Matrix
labels = sorted(df["ground_truth"].unique())
cm = confusion_matrix(df["ground_truth"], df["classification"], labels=labels)

plt.figure(figsize=(8, 6))
plt.imshow(cm)
plt.title("Human Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks(range(len(labels)), labels, rotation=45)
plt.yticks(range(len(labels)), labels)

for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.colorbar()
plt.tight_layout()
plt.savefig(output_dir / "human_confusion_matrix.png")
plt.close()

# 6. GPT Confusion Matrix
cm = confusion_matrix(df["ground_truth"], df["gpt_classification"], labels=labels)

plt.figure(figsize=(8, 6))
plt.imshow(cm)
plt.title("GPT Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks(range(len(labels)), labels, rotation=45)
plt.yticks(range(len(labels)), labels)

for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.colorbar()
plt.tight_layout()
plt.savefig(output_dir / "gpt_confusion_matrix.png")
plt.close()

# 7. Correct vs Incorrect Predictions
human_correct = (df["classification"] == df["ground_truth"]).sum()
human_incorrect = len(df) - human_correct
gpt_correct = (df["gpt_classification"] == df["ground_truth"]).sum()
gpt_incorrect = len(df) - gpt_correct

comparison = pd.DataFrame({
    "Correct": [human_correct, gpt_correct],
    "Incorrect": [human_incorrect, gpt_incorrect]
}, index=["Human", "GPT"])

comparison.plot(kind="bar", figsize=(8, 5))
plt.title("Correct vs Incorrect Predictions")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig(output_dir / "correct_vs_incorrect.png")
plt.close()

print("Graphs saved to:", output_dir.resolve())
