def reviewer_accuracy(df):

    output = {}

    for reviewer in df["reviewer_name"].unique():

        subset = df[
            df["reviewer_name"] == reviewer
        ]

        score = (
            subset["classification"].str.lower()
            == subset["ground_truth"].str.lower()
        ).mean() * 100

        output[reviewer] = round(score, 2)

    return output


def average_confidence(df):

    return round(
        df["confidence"].mean(),
        2
    )


def agreement_rate(df):

    if "gpt_classification" not in df.columns:
        return 0

    agreement = (
        df["classification"].str.lower()
        == df["gpt_classification"].str.lower()
    )

    return round(
        agreement.mean() * 100,
        2
    )
