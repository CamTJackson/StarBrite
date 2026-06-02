def calculate_belief_revision(df):

    if "gpt_classification" not in df.columns:
        df["belief_revision_score"] = 0
        return df

    df["belief_revision_score"] = (
        df["classification"].str.lower()
        != df["gpt_classification"].str.lower()
    ).astype(int)

    return df
