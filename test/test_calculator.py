import pytest
from app.calculator import divide, power


def test_power_success():
    assert power(2, 3) == 8


def test_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power_edge_case_zero_exponent():
    assert power(2, 0) == 1
