from unittest.mock import patch, Mock

from src.calculations.calc3 import calculate_func_area


def test_calculate_func_area_1():
    result = calculate_func_area(1)
    assert result == 3.14159


@patch("src.calculations.calc3.get_pi", Mock(return_value=0))
def test_calculate_func_area_2():
    result = calculate_func_area(1)
    assert result == 0
