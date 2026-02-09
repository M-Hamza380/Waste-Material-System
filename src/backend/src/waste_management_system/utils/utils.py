import base64
import os
import sys

import yaml

from .exception import CustomException
from .logger import logger


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logger.info(f"Reading yaml file: {file_path}")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e, sys)


def write_yaml_file(file_path: str, data: object, replace: bool = False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as yaml_file:
            logger.info(f"Writing yaml file: {file_path}")
            yaml.dump(data, yaml_file)
    except Exception as e:
        raise CustomException(e, sys)


def decode_image(image: str, file_path: str):
    try:
        img_data = base64.b64decode(image)
        with open(file_path, "wb") as f:
            logger.info(f"Decoding image: {file_path}")
            f.write(img_data)
    except Exception as e:
        raise CustomException(e, sys)


def encode_image(file_path: str):
    try:
        with open(file_path, "rb") as f:
            logger.info(f"Encoding image: {file_path}")
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        raise CustomException(e, sys)
