import sys

from src.waste_management_system.components.data_ingestion import DataIngestion
from src.waste_management_system.entity.artifact_entity import DataIngestionArtifact
from src.waste_management_system.entity.config_entity import DataIngestionConfig
from src.waste_management_system.utils.exception import CustomException


class TestDataIngestion:
    def test_initiate_data_ingestion(self):
        try:
            data_ingestion_config = DataIngestionConfig()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            assert isinstance(data_ingestion_artifact, DataIngestionArtifact)
        except Exception as e:
            raise CustomException(e, sys)
