from fuel import convert, gauge
import pytest

def test_middle():
    assert gauge(41) == "41%"

def test_nominotor():
   assert convert([3, 4]) == 75.0

def test_denominator():
    with pytest.raises(ZeroDivisionError):
        3/ 0

def test_nominator_greater_denominator():
    with pytest.raises(ValueError):
        convert([3, 2])
