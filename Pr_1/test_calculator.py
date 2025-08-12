import pytest

from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_sum_positive(calc):
    res = calc.sum(1,3)
    assert res == 4

def test_sum_positive_negative(calc):
    res = calc.sum(1,-3)
    assert res == -2

def test_sum_negative_positive(calc):
    res = calc.sum(-1,3)
    assert res == 2

@pytest.mark.skipif
def test_sum_negative_negative(calc):
    res = calc.sum(-1,-3)
    assert res == -4

def test_devide_(calc):
    res = calc.sum(-1,0)
    assert res == 0
