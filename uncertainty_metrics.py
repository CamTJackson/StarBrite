def calculate_unknown_rate(df):

    if "gpt_classification" not in df.columns:
        return 0

    unknown_rate = (
        df["gpt_classification"]
        .fillna("")
        .str.lower()
        .eq("unknown")
        .mean()
    ) * 100

    return round(unknown_rate, 2)


def calculate_uncertainty_presence(df):

    if "gpt_uncertainty" not in df.columns:
        return 0

    presence = (
        df["gpt_uncertainty"]
        .fillna("")
        .str.strip()
        .ne("")
        .mean()
    ) * 100

    return round(presence, 2)
