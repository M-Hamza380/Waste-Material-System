from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionArtifact:
    pass


@dataclass(frozen=True)
class DataValidationArtifact:
    pass


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
