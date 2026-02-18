import os
import shutil
import sys
from abc import ABC, abstractmethod

from waste_management_system.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
)
from waste_management_system.entity.config_entity import DataValidationConfig
from waste_management_system.utils.exception import CustomException
from waste_management_system.utils.logger import logger


class BaseDataValidation(ABC):
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_validation_config = data_validation_config

    @abstractmethod
    def validate_all_files(self) -> bool | None:
        pass

    @abstractmethod
    def initiate_data_validation(self) -> DataValidationArtifact:
        pass


class DataValidation(BaseDataValidation):

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        super().__init__(data_ingestion_artifact, data_validation_config)

    def validate_all_files(self) -> bool | None:
        try:
            logger.info("Validating all files...")
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_file_path)

            for file in all_files:
                if file in self.data_validation_config.required_file_list:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_dir, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_dir, "w") as f:
                        f.write(f"Validation status: {validation_status}")

            logger.info("All files validated successfully :)")
            return validation_status
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            logger.info("Initiating data validation...")
            status = self.validate_all_files()
            data_validation_artifact = DataValidationArtifact(validation_status=status)

            if status:
                src = self.data_ingestion_artifact.feature_store_file_path
                dst_dir = self.data_validation_config.data_validation_dir
                # Ensure destination directory exists
                os.makedirs(dst_dir, exist_ok=True)

                if os.path.isfile(src):
                    shutil.copy(src, dst_dir)
                elif os.path.isdir(src):
                    dest_path = os.path.join(dst_dir, os.path.basename(src))
                    if os.path.exists(dest_path):
                        shutil.rmtree(dest_path)
                    shutil.copytree(src, dest_path)
                else:
                    logger.warning(f"Source for copying does not exist: {src}")

            logger.info("Data validation completed successfully :)")
            return data_validation_artifact
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
