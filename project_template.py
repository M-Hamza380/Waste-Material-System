import os, logging
from pathlib import Path

logging.basicConfig(
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s: %(lineno)d : %(message)s] ]",
    level=logging.INFO
)

list_of_files = [
    "src/backend/__init__.py",
    "src/backend/src/__init__.py",
    "src/backend/src/api/__init__.py",
    "src/backend/src/api/routers/__init__.py",
    "src/backend/src/utils/__init__.py",
    "src/backend/src/utils/utils.py",
    "src/backend/src/utils/logger.py",
    "src/backend/src/utils/exception.py",
    "src/backend/src/constant/__init__.py",
    "src/backend/src/components/__init__.py",
    "src/backend/src/components/data_ingestion.py",
    "src/backend/src/components/data_validation.py",
    "src/backend/src/components/model_trainer.py",
    "src/backend/src/components/model_evaluation.py",
    "src/backend/src/components/model_conversion.py",
    "src/backend/src/components/model_pusher.py",
    "src/backend/src/entity/__init__.py",
    "src/backend/src/entity/config_entity.py",
    "src/backend/src/entity/artifact_entity.py",
    "src/backend/src/constants/__init__.py",
    "src/backend/src/constants/training_pipeline/__init__.py",
    "src/backend/src/pipeline/__init__.py",
    "src/backend/src/pipeline/prediction_pipeline.py",
    "src/backend/src/pipeline/train_pipeline.py",
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")



