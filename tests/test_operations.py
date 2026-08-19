import pytest
from operations import add, sub, mul, div, exp, operations


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -2, 1),
    (0, 0, 0),
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 2, -2),
    (0, 5, 0),
])
def test_mul(a, b, expected):
    assert mul(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-6, 3, -2),
    (1, 4, 0.25),
])
def test_div(a, b, expected):
    assert div(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (0, 0, 1),
    (5, 0, 1),
])
def test_exp(a, b, expected):
    assert exp(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_operations_keys():
    assert set(operations.keys()) == {"+", "-", "*", "/", "^"}
