import pytest
import functions

def test_addition():
    x = functions.addition(3, 4)
    assert x == 7


def test_subtraction():
    x = functions.subtraction(3, 4)
    assert x == -1