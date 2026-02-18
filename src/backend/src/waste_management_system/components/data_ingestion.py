import os
import sys
from abc import ABC, abstractmethod
from zipfile import ZipFile

import gdown  # type: ignore

from waste_management_system.entity.artifact_entity import DataIngestionArtifact
from waste_management_system.entity.config_entity import DataIngestionConfig
from waste_management_system.utils.exception import CustomException
from waste_management_system.utils.logger import logger


class BaseDataIngestion(ABC):
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    @abstractmethod
    def download_data_from_gdrive(self) -> str:
        pass

    @abstractmethod
    def extract_zip_file(self, zip_downlaod_path: str) -> str:
        pass

    @abstractmethod
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        pass


class DataIngestion(BaseDataIngestion):
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        super().__init__(data_ingestion_config)

    def download_data_from_gdrive(self) -> str:
        try:
            logger.info("Downloading data from google drive...")
            gdrive_url = self.data_ingestion_config.data_download_url
            zip_downlaod_dir = self.data_ingestion_config.data_ingestion_dir

            if not os.path.exists(zip_downlaod_dir):
                os.makedirs(zip_downlaod_dir, exist_ok=True)

            data_file_name = "waste-material-dataset.zip"
            zip_downlaod_path = os.path.join(zip_downlaod_dir, data_file_name)

            # ID of the file you want to download
            file_id = gdrive_url.split("/")[-2]

            # Download format
            prefix = "https://drive.google.com/uc?/export=download&id="

            # Output you want
            url = prefix + file_id

            # Download file
            gdown.download(url, zip_downlaod_path, quiet=False)

            logger.info("Download completed successfully :)")
            return zip_downlaod_path
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def extract_zip_file(self, zip_downlaod_path: str) -> str:
        try:
            logger.info("Extracting zip file...")
            feature_store_dir = self.data_ingestion_config.feature_store_dir

            if not os.path.exists(feature_store_dir):
                os.makedirs(feature_store_dir, exist_ok=True)

            with ZipFile(zip_downlaod_path, "r") as zip_ref:
                zip_ref.extractall(feature_store_dir)
            logger.info("Extraction completed successfully :)")
            return feature_store_dir
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("Initiating data ingestion...")
            zip_downlaod_path = self.download_data_from_gdrive()
            feature_store_dir = self.extract_zip_file(zip_downlaod_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_downlaod_path, feature_store_file_path=feature_store_dir
            )
            logger.info("Data ingestion completed successfully :)")
            return data_ingestion_artifact
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
