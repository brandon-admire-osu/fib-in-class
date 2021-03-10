from fibonacci import *
import pytest


def test_bad_in():
    with pytest.raises(ValueError):
        fact("Gun")
        fact(float)
        fact(list)

    with pytest.raises(ZeroDivisionError):
        fact(-1)
        fact(-2)


def test_good_in():
    assert fact(5) == 120
    assert fact(10) == 3628800
