import os
from dataclasses import dataclass

from waste_management_system.constants.artifact_constants import (
    ARTIFACTS_DIR,
    DATA_DOWNLOAD_URL,
    DATA_INGESTION_DIR,
    DATA_INGESTION_FEATURE_STORE_DIR,
)


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_DIR)

    feature_store_dir: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url: str = DATA_DOWNLOAD_URL
