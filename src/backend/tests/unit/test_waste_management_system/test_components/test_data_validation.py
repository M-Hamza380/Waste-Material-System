import sys

from src.waste_management_system.components.data_validation import DataValidation
from src.waste_management_system.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
)
from src.waste_management_system.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
)
from src.waste_management_system.utils.exception import CustomException


class TestDataValidation:
    def test_initiate_data_validation(self):
        try:
            data_ingestion_config = DataIngestionConfig()
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=data_ingestion_config.data_ingestion_dir,
                feature_store_file_path=data_ingestion_config.feature_store_dir,
            )
            data_validation_config = DataValidationConfig()
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=data_validation_config,
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            assert data_validation_artifact is not None
            assert data_validation_artifact.validation_status is not None
            data_validation_artifact = DataValidationArtifact(validation_status=True)
            assert isinstance(data_validation_artifact, DataValidationArtifact)
        except Exception as e:
            raise CustomException(e, sys)
