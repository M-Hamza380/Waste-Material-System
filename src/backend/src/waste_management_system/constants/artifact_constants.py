"""
Artifacts related constants, defined in artifact_entity and mostly used in config_entity scripts.
"""

from pathlib import Path

# Common constants
BASE_DIR: Path = Path(__file__).parent.parent.parent.parent
ARTIFACTS_DIR: Path = BASE_DIR / "artifacts"

# Data ingestion constants
DATA_INGESTION_DIR: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1y50gri4vFI3y1WZTEly1nlBA5pih-DPL/view?usp=sharing"

# Data validation constants
DATA_VALIDATION_DIR: str = "data_validation"
VALID_STATUS_DIR: str = "valid_status"
REQUIRED_FILE_LIST: list[str] = ["train", "valid", "test", "data.yaml"]
