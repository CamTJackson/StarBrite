import matplotlib.pyplot as plt


def plot_reviewer_accuracy(score_dict, output_file):

    plt.figure(figsize=(8, 4))

    plt.bar(
        list(score_dict.keys()),
        list(score_dict.values())
    )

    plt.ylabel("Accuracy (%)")
    plt.title("Reviewer Accuracy")

    plt.xticks(rotation=25)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def plot_confidence_distribution(
    df,
    output_file
):

    plt.figure(figsize=(8, 4))

    plt.hist(
        df["confidence"],
        bins=5
    )

    plt.xlabel("Confidence")
    plt.ylabel("Count")

    plt.title(
        "Human Confidence Distribution"
    )

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
