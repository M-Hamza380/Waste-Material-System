import logging
import os
from pathlib import Path

logging.basicConfig(
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s: %(lineno)d : %(message)s] ]",
    level=logging.INFO,
)

PROJECT_NAME = "waste_management_system"

list_of_files = [
    "src/backend/src/__init__.py",
    "src/backend/src/api/__init__.py",
    "src/backend/src/api/routes/__init__.py",
    "src/backend/src/api/routes/waste_management_system_route.py",
    f"src/backend/src/{PROJECT_NAME}/utils/__init__.py",
    f"src/backend/src/{PROJECT_NAME}/utils/utils.py",
    f"src/backend/src/{PROJECT_NAME}/utils/logger.py",
    f"src/backend/src/{PROJECT_NAME}/utils/exception.py",
    f"src/backend/src/{PROJECT_NAME}/components/__init__.py",
    f"src/backend/src/{PROJECT_NAME}/components/data_ingestion.py",
    f"src/backend/src/{PROJECT_NAME}/components/data_validation.py",
    f"src/backend/src/{PROJECT_NAME}/components/model_trainer.py",
    f"src/backend/src/{PROJECT_NAME}/components/model_evaluation.py",
    f"src/backend/src/{PROJECT_NAME}/components/model_export.py",
    f"src/backend/src/{PROJECT_NAME}/components/model_pusher.py",
    f"src/backend/src/{PROJECT_NAME}/entity/__init__.py",
    f"src/backend/src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/backend/src/{PROJECT_NAME}/entity/artifact_entity.py",
    f"src/backend/src/{PROJECT_NAME}/constants/__init__.py",
    f"src/backend/src/{PROJECT_NAME}/constants/artifact_constants.py",
    f"src/backend/src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/backend/src/{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    f"src/backend/src/{PROJECT_NAME}/pipeline/train_pipeline.py",
    "src/backend/Dockerfile",
    "src/backend/.dockerignore",
    "src/backend/.flake8",
    "src/backend/.pre-commit-config.yaml",
    "src/backend/Makefile",
    "src/backend/datasets/.gitkeep",
    "src/backend/notebooks/explore_data.ipynb",
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
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already exists")
