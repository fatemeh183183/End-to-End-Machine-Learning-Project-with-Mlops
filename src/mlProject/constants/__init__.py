from pathlib import Path

# ── Project root (…/your-repo) no matter where code runs ───────────────
ROOT_DIR: Path = Path(__file__).resolve().parents[3]

# ── Top-level folders / files ───────────────────────────────────────────
CONFIG_FILE_PATH: Path = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH: Path = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH: Path = ROOT_DIR / "schema.yaml"

# ── Artifacts (pipeline outputs) ────────────────────────────────────────
ARTIFACTS_DIR: Path = ROOT_DIR / "artifacts"

# Data ingestion defaults (you can still override via YAML)
DATA_INGESTION_DIR: Path = ARTIFACTS_DIR / "data_ingestion"
DATA_INGESTION_LOCAL_ZIP: Path = DATA_INGESTION_DIR / "data.zip"
DATA_INGESTION_UNZIP_DIR: Path = DATA_INGESTION_DIR / "unzipped"
