import json
from pathlib import Path

# -----------------------------
# Expected input files
# -----------------------------

EXPECTED_INPUT_FILES = sorted([
    "1746179179-causes-effects-and-solutions.pdf",
    "(10)B-3643-Final.pdf",
    "1851_9781351115629_previewpdf.pdf",
    "646717.pdf",
    "8398.pdf",
    "ace3.pdf",
    "Handbook.pdf",
    "Management BFSc-608.pdf",
    "attachment_69951686907167.pdf",
    "AUJES_Volume 2_Issue 4_Pages 218-239.pdf",
    "BALLAYAN 2000.pdf",
    "book.pdf",
    "Clean.pdf",
    "egm-report.pdf",
    "epdf.pub.pdf",
    "Hassan2812024JGEESI111906.pdf",
    "isfr_book_eng-vol-1_2023.pdf",
    "L-0025804346-pdf.pdf",
    "main work.pdf",
    "Pollution.pdf",
    "pollution__FAO.pdf",
    "report-2001.pdf",
    "sustainability-07-03528.pdf",
    "te_1094_prn.pdf"
])

EXPECTED_SOURCE_FILES_USED = EXPECTED_INPUT_FILES

# -----------------------------
# Paths
# -----------------------------

INPUT_DIR = Path("/environment/input_artifacts")
OUTPUT_PATH = Path("/logs/agent/output.json")
REWARD_DIR = Path("/logs/verifier")
REWARD_PATH = REWARD_DIR / "reward.txt"

# -----------------------------
# Expected values
# -----------------------------

EXPECTED_WATER_DOMAIN_SCORE = 93
EXPECTED_SOIL_DOMAIN_SCORE = 78
EXPECTED_FOREST_DOMAIN_SCORE = 72
EXPECTED_MIXED_DOMAIN_SCORE = 56
EXPECTED_RETRIEVAL_SCORE = 21
EXPECTED_FINAL_SYNTHESIS_VALUE = 51

# -----------------------------
# Weights
# -----------------------------

SOURCE_FILES_USED_WEIGHT = 0.1
VALUE_CHECK_WEIGHT = 0.85 / 5
RETERIEVAL_CHECK_WEIGHT = 0.05

score = 0.0
checks = []


def add_check(name, passed, weight):
    global score
    checks.append((name, passed, weight))
    if passed:
        score += weight


def approx_match(actual, expected, tolerance):
    try:
        return abs(float(actual) - float(expected)) <= tolerance
    except Exception:
        return False


def exact_match(actual, expected):
    return actual == expected


def write_reward():
    final_score = min(score, 1.0)

    REWARD_DIR.mkdir(parents=True, exist_ok=True)
    REWARD_PATH.write_text(str(round(final_score, 4)))

    for name, passed, weight in checks:
        print(f"{name}: {'PASS' if passed else 'FAIL'} ({weight})")

    print(f"FINAL SCORE: {round(final_score, 4)}")


# -----------------------------
# Input files present check
# -----------------------------

actual_input_files = []

if INPUT_DIR.exists():
    actual_input_files = sorted([
        path.name
        for path in INPUT_DIR.iterdir()
        if path.is_file()
    ])



# -----------------------------
# Load output lightly
# -----------------------------

if not OUTPUT_PATH.exists():
    write_reward()
    raise SystemExit(0)

try:
    data = json.loads(OUTPUT_PATH.read_text())
except Exception:
    write_reward()
    raise SystemExit(0)

# -----------------------------
# Value checks
# -----------------------------


add_check(
    "all_source_files_used",
    sorted(data.get("source_files_used", [])) == EXPECTED_SOURCE_FILES_USED,
    SOURCE_FILES_USED_WEIGHT
)

add_check(
    "water_domain_score_correct",
    approx_match(data.get("water_domain_score"), EXPECTED_WATER_DOMAIN_SCORE, 10),
    VALUE_CHECK_WEIGHT
)

add_check(
    "soil_domain_score_correct",
    approx_match(data.get("soil_domain_score"), EXPECTED_SOIL_DOMAIN_SCORE, 10),
    VALUE_CHECK_WEIGHT
)

add_check(
    "forest_domain_score_correct",
    approx_match(data.get("forest_domain_score"), EXPECTED_FOREST_DOMAIN_SCORE, 10),
    VALUE_CHECK_WEIGHT
)

add_check(
    "mixed_domain_score_correct",
    approx_match(data.get("mixed_domain_score"), EXPECTED_MIXED_DOMAIN_SCORE, 10),
    VALUE_CHECK_WEIGHT
)

add_check(
    "retrieval_score_correct",
    exact_match(data.get("retrieval_score"), EXPECTED_RETRIEVAL_SCORE),
    RETERIEVAL_CHECK_WEIGHT
)

add_check(
    "final_synthesis_value_correct",
    approx_match(data.get("final_synthesis_value"), EXPECTED_FINAL_SYNTHESIS_VALUE, 12),
    VALUE_CHECK_WEIGHT
)

write_reward()
