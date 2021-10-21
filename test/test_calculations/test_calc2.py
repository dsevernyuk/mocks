from unittest import mock

from src.calculations.calc2 import calculate_approx_area


def test_calculate_approx_area_1():
    result = calculate_approx_area(1)
    assert result == 3.14


@mock.patch("src.calculations.calc2.APPROX_PI", 2.17)
def test_calculate_approx_area_2():
    result = calculate_approx_area(1)
    assert result == 2.17
