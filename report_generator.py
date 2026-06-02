import pandas as pd


def generate_summary_report(
    merged_df,
    output_file
):

    report = {
        "rows": len(merged_df),
        "targets": merged_df["target_id"].nunique(),
        "reviewers": merged_df["reviewer_name"].nunique(),
        "avg_confidence": round(
            merged_df["confidence"].mean(),
            2
        )
    }

    pd.DataFrame(
        [report]
    ).to_csv(
        output_file,
        index=False
    )

    print(
        f"Summary saved to {output_file}"
    )
