import pytest

from calculator import sum, div, mul, sub;

def test_sum():
    assert sum(2,3) == 5

def test_sub():
    assert sub(2,3) == -1


def test_mul():
    assert mul(2,3) == 6


def test_div():
    assert div(5,0) == "2.5"
    assert div(5,2) == 2.5

# python -m pytest test_calculator.py