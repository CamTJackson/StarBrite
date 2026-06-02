import pandas as pd

from config import (
    TARGETS_CSV,
    GPT_RESULTS_CSV,
    FINAL_DATASET_CSV,
    OUTPUT_DIR
)

from data_loader import (
    load_targets,
    load_all_human_reviews,
    validate_human_reviews
)

from merge_results import (
    merge_human_and_gpt
)

from belief_revision import (
    calculate_belief_revision
)

from metrics import (
    reviewer_accuracy
)

from visualizations import (
    plot_reviewer_accuracy,
    plot_confidence_distribution
)

from report_generator import (
    generate_summary_report
)


def main():

    print("Loading targets...")
    targets_df = load_targets()

    print("Loading human reviews...")
    human_df = load_all_human_reviews()
    human_df = validate_human_reviews(
        human_df
    )

    print("Loading GPT results...")
    gpt_df = pd.read_csv(
        GPT_RESULTS_CSV
    )

    print("Merging datasets...")

    merged = merge_human_and_gpt(
        targets_df,
        human_df,
        gpt_df
    )

    print(
        "Calculating belief revision..."
    )

    merged = calculate_belief_revision(
        merged
    )

    merged.to_csv(
        FINAL_DATASET_CSV,
        index=False
    )

    reviewer_scores = reviewer_accuracy(
        merged
    )

    plot_reviewer_accuracy(
        reviewer_scores,
        OUTPUT_DIR / "reviewer_accuracy.png"
    )

    plot_confidence_distribution(
        merged,
        OUTPUT_DIR / "confidence_distribution.png"
    )

    generate_summary_report(
        merged,
        OUTPUT_DIR / "summary_report.csv"
    )

    print("Done.")
    print(
        f"Final dataset: {FINAL_DATASET_CSV}"
    )


if __name__ == "__main__":
    main()
