import pytest
def add_two_numbers(a, b):
    summ = a + b
    return summ

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 2) == 30, "The sum of 1 and 2 should be 3"

@pytest.mark.math
def test_large_number():
    assert add_two_numbers(100, 300 ) == 400, "Should be 400"
