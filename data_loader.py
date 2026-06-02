import pandas as pd
from config import TARGETS_CSV, HUMAN_FILES

def load_targets():
    return pd.read_csv(TARGETS_CSV)

def load_all_human_reviews():
    frames = []

    for file in HUMAN_FILES:
        frames.append(pd.read_csv(file))

    return pd.concat(frames, ignore_index=True)

def validate_human_reviews(df):

    required_columns = [
        "item_id",
        "target_id",
        "reviewer_name",
        "reviewer_role",
        "classification",
        "confidence"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    return df
