import pytest
from Calc import Calc

def test_add():
    calc = Calc()
    assert calc.add(4,3) == 7
