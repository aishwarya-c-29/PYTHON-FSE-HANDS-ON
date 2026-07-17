#Testcases
import pytest
from calculator import *

# Test 1
def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 30

# Test 2
def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 10

# Test 3
def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 200

# Test 4
def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 2

# Test 5
def test_divide_by_zero(zero):
    with pytest.raises(ValueError):
        divide(5, zero)

# Test 6
def test_add_negative():
    assert add(-5, -5) == -10

# Test 7
def test_add_float():
    assert add(2.5, 3.5) == 6.0

# Test 8
def test_subtract_negative():
    assert subtract(5, 10) == -5

# Test 9
def test_multiply_zero():
    assert multiply(50, 0) == 0

# Test 10
def test_divide_float():
    assert divide(5, 2) == 2.5

# Test 11
def test_large_numbers():
    assert multiply(100000, 100000) == 10000000000

# Test 12
def test_add_zero():
    assert add(0, 0) == 0

Output:
================== test session starts ==================
collected 12 items

test_calculator.py ............

12 passed

pytest cov--calculator

Output:
----------- coverage: platform win32 -----------

Name             Stmts   Miss  Cover
------------------------------------
calculator.py       8      0   100%
