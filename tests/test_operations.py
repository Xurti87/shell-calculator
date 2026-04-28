import pytest
from operations import (
    addition,
    subtraction,
    multiplication,
    division,
    exponentiation)

def test_addition():
    assert addition(2,3) == 5

def test_subtraction():
    assert subtraction(2,3) == -1

def test_multiplication():
    assert multiplication(2,3) == 6

def test_division():
    assert division(8, -4) == -2

def test_exponentiation():
    assert exponentiation(0, 0) == 1

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)