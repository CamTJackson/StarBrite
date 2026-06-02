import pandas as pd

from config import (
    TARGETS_CSV,
    GPT_RESULTS_CSV
)

from lightcurve_loader import (
    download_kepler_lightcurve,
    extract_features
)

from prompt_builder import build_classification_prompt
from gpt_classifier import classify_target


def run_gpt_benchmark():

    targets = pd.read_csv(TARGETS_CSV)

    results = []

    for _, row in targets.iterrows():

        target_id = str(row["target_id"])

        try:

            lc = download_kepler_lightcurve(target_id)

            features = extract_features(lc)

            prompt = build_classification_prompt(
                target_id,
                features
            )

            response = classify_target(prompt)

            results.append({
                "item_id": row["item_id"],
                "target_id": target_id,
                "gpt_raw_response": response,
                **features
            })

            print(f"Completed {target_id}")

        except Exception as exc:

            results.append({
                "item_id": row["item_id"],
                "target_id": target_id,
                "error": str(exc)
            })

            print(f"Failed {target_id}: {exc}")

    pd.DataFrame(results).to_csv(
        GPT_RESULTS_CSV,
        index=False
    )

    print("GPT benchmark complete.")
