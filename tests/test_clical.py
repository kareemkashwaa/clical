import pytest
from clical.main import calc

@pytest.mark.parametrize("expr, res",[("1+1", 5)])
def test_addition(expr, res):
    assert calc(expr) == res