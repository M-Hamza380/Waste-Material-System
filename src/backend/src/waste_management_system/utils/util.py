import base64
import os
import sys

import yaml

from waste_management_system.utils.exception import CustomException
from waste_management_system.utils.logger import logger


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a yaml file from the given file path.

    Args:
        file_path (str): The path to read the yaml file from.

    Returns:
        dict: The data read from the yaml file.

    Raises:
        CustomException: If any exception occurs while reading the yaml file.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            logger.info(f"Reading yaml file: {file_path}")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)


def write_yaml_file(file_path: str, data: object, replace: bool = False) -> None:
    """
    Writes a yaml file to the given file path.

    Args:
        file_path (str): The path to write the yaml file to.
        data (object): The data to write to the yaml file.
        replace (bool, optional): Whether to replace the existing file if it exists. Defaults to False.

    Raises:
        CustomException: If any exception occurs while writing the yaml file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as yaml_file:
            logger.info(f"Writing yaml file: {file_path}")
            yaml.dump(data, yaml_file)
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)


def decode_image(image: str, file_path: str) -> None:
    """
    Decodes a base64 encoded image and writes it to a file

    Parameters:
    image (str): Base64 encoded image
    file_path (str): Path to write the image

    Returns:
    None
    """
    try:
        img_data = base64.b64decode(image)
        with open(file_path, "wb") as f:
            logger.info(f"Decoding image: {file_path}")
            f.write(img_data)
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)


def encode_image(file_path: str) -> str:
    """
    Encodes an image at the given file path to a base64 string.

    Args:
        file_path (str): The path to the image file to encode.

    Returns:
        str: The base64 encoded image string.

    Raises:
        CustomException: If any exception occurs while encoding the image.
    """
    try:
        with open(file_path, "rb") as f:
            logger.info(f"Encoding image: {file_path}")
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)
