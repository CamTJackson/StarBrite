import pandas as pd


def merge_human_and_gpt(
    targets_df,
    human_df,
    gpt_df
):

    merged = human_df.merge(
        targets_df,
        on=["item_id", "target_id"],
        how="left"
    )

    merged = merged.merge(
        gpt_df,
        on=["item_id", "target_id"],
        how="left"
    )

    return merged
