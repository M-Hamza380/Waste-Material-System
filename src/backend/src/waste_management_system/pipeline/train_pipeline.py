import sys
from abc import ABC, abstractmethod

from waste_management_system.components.data_ingestion import DataIngestion
from waste_management_system.entity.artifact_entity import DataIngestionArtifact
from waste_management_system.entity.config_entity import DataIngestionConfig
from waste_management_system.utils.exception import CustomException
from waste_management_system.utils.logger import logger


class BaseTrainPipeline(ABC):

    @abstractmethod
    def start_data_ingestion(self) -> DataIngestionArtifact:
        pass

    @abstractmethod
    def run_pipeline(self):
        pass


class TrainPipeline(BaseTrainPipeline):
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("Starting data ingestion...")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logger.info("Data ingestion completed successfully :)")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self) -> None:
        try:
            logger.info("Starting train pipeline...")
            self.start_data_ingestion()
            logger.info("Train pipeline completed successfully :)")
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
