import pytest

@pytest.mark.parametrize("param1",[10,2,3,4])
def test_method1(param1):
    assert param1 > 1