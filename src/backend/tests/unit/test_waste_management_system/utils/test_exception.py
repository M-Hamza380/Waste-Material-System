import sys

import pytest

from src.waste_management_system.utils.exception import CustomException


def test_custom_exception():
    with pytest.raises(CustomException) as exc_info:
        try:
            3 / 0
        except Exception as e:
            raise CustomException(e, sys)

    assert "division by zero" in str(exc_info.value)
