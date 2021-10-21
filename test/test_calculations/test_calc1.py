from unittest import mock

from src.calculations.calc1 import calculate_area


def test_calculate_area_1():
    result = calculate_area(1)
    print(result)
    assert 3.14 < result
    assert result < 3.15


@mock.patch("math.pi", 4)
def test_calculate_area_2():
    result = calculate_area(1)
    assert result == 4


@mock.patch("math.pi", -1)
def test_calculate_area_3():
    result = calculate_area(1)
    assert result == -1
