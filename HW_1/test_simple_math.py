"""
1.  Напишите в нём тесты для методов square и cube.
    Проверьте корректность работы методов для разных входных значений (например, положительных, отрицательных и нуля).
Пример ожидаемого поведения:
    Метод square (2) должен возвращать 4.
    Метод cube (-3) должен возвращать -27.
"""
import pytest
from simple_math import SimpleMath

error_format = "Error! Invalid data format"

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square_positive(simple_math):
    assert simple_math.square(2) == 4

def test_square_negative(simple_math):
    assert simple_math.square(-2) == 4

def test_square_0(simple_math):
    assert simple_math.square(0) == 0

def test_square_none(simple_math):
    assert simple_math.square(None) == error_format

def test_square_type(simple_math):
    assert simple_math.square("/") == error_format

def test_square_float(simple_math):
    assert simple_math.square(1.009) == pytest.approx(1.018081) # нашёл как проверять для формата float

def test_square_negative_float(simple_math):
    assert simple_math.square(-1.009) == pytest.approx(1.018081) # нашёл как проверять для формата float


def test_cube_positive(simple_math):
    assert simple_math.cube(2) == 8

def test_cube_negative(simple_math):
    assert simple_math.cube(-2) == -8

def test_cube_0(simple_math):
    assert simple_math.cube(0) == 0

def test_cube_none(simple_math):
    assert simple_math.cube(None) == error_format

def test_cube_type(simple_math):
    assert simple_math.cube(".") == error_format

def test_cube_float(simple_math):
    assert simple_math.cube(1.009) == pytest.approx(1.02724373) # нашёл как проверять для формата float

def test_cube_negative_float(simple_math):
    assert simple_math.cube(-1.009) == pytest.approx(-1.02724373)

