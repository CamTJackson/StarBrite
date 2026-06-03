from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

TARGETS_CSV = DATA_DIR / "data/targets/kepler_targets.csv"

HUMAN_FILES = [
    DATA_DIR / "data/human_reviews/professor_a_v2.csv",
    DATA_DIR / "data/human_reviews/professor_b_v2.csv",
    DATA_DIR / "data/human_reviews/graduate_student_a_v2.csv",
    DATA_DIR / "data/human_reviews/graduate_student_b_v2.csv",
    DATA_DIR / "data/human_reviews/industry_professional_v2.csv"
]

GPT_RESULTS_CSV = OUTPUT_DIR / "gpt_predictions.csv"
FINAL_DATASET_CSV = OUTPUT_DIR / "star_brite_results.csv"

MODEL_NAME = "gpt-5.5"
TEMPERATURE = 0.2

KEPLER_MISSION = "Kepler"
