import os
from dataclasses import dataclass, field
from functools import partial

from waste_management_system.constants.artifact_constants import (
    ARTIFACTS_DIR,
    DATA_DOWNLOAD_URL,
    DATA_INGESTION_DIR,
    DATA_INGESTION_FEATURE_STORE_DIR,
    DATA_VALIDATION_DIR,
    REQUIRED_FILE_LIST,
    VALID_STATUS_DIR,
)


@dataclass(frozen=True)
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_DIR)

    feature_store_dir: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url: str = DATA_DOWNLOAD_URL


@dataclass(frozen=True)
class DataValidationConfig:
    data_validation_dir: str = os.path.join(ARTIFACTS_DIR, DATA_VALIDATION_DIR)

    valid_status_dir: str = os.path.join(data_validation_dir, VALID_STATUS_DIR)

    required_file_list: list[str] = field(default_factory=partial(list, REQUIRED_FILE_LIST))
