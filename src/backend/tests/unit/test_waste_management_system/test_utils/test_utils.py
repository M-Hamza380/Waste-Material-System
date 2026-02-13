import os

import pytest
import yaml

from src.waste_management_system.utils.util import (
    decode_image,
    encode_image,
    read_yaml_file,
    write_yaml_file,
)


def test_write_yaml_file():
    # Test that the function writes to the correct file path
    test_file_path = "test.yaml"
    test_data = {"test_key": "test_value"}

    write_yaml_file(test_file_path, test_data)
    assert os.path.exists(test_file_path)

    # Test that the function writes the correct data to the file
    with open(test_file_path, "r") as f:
        data = yaml.safe_load(f)
    assert data == test_data

    # Test that the function raises an error if the file path is invalid
    with pytest.raises(FileNotFoundError):
        write_yaml_file("invalid_path.yaml", test_data)

    # Test that the function raises an error if the data is not a dictionary
    with pytest.raises(TypeError):
        write_yaml_file(test_file_path, "not a dictionary")


def test_read_yaml_file():
    # Test that the function reads from the correct file path
    test_file_path = "test.yaml"
    test_data = {"test_key": "test_value"}

    with open(test_file_path, "w") as f:
        yaml.dump(test_data, f)

    assert read_yaml_file(test_file_path) == test_data

    # Test that the function raises an error if the file path is invalid
    with pytest.raises(FileNotFoundError):
        read_yaml_file("invalid_path.yaml")

    # Test that the function raises an error if the file is not a YAML file
    with pytest.raises(yaml.YAMLError):
        read_yaml_file("test.txt")


def test_encode_image():
    # Test the function encodes an image
    test_file_path = "test_image.jpg"
    test_encode_image = encode_image(test_file_path)
    assert isinstance(test_encode_image, str)

    # Test the function raises an error if the image path is invalid
    with pytest.raises(FileNotFoundError):
        encode_image("invalid_path.jpg")


def test_decode_image():
    # Test the function decodes an image
    test_image = "test_image.jpg"
    test_file_path = "test_data_files"
    test_decode_image = decode_image(test_image, test_file_path)
    assert isinstance(test_decode_image, str)

    # Test the function raises an error if the image path is invalid
    with pytest.raises(FileNotFoundError):
        decode_image("invalid_path.jpg", test_file_path)

    # Test the function raises an error if the file path is invalid
    with pytest.raises(FileNotFoundError):
        decode_image(test_image, "invalid_path")
