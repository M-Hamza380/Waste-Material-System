from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_file_path: str


@dataclass(frozen=True)
class DataValidationArtifact:
    validation_status: bool | None


@dataclass(frozen=True)
class ModelTrainerArtifact:
    pass


@dataclass(frozen=True)
class ModelEvaluationArtifact:
    pass


@dataclass(frozen=True)
class ModelExportArtifact:
    pass


@dataclass(frozen=True)
class ModelPusherArtifact:
    pass
