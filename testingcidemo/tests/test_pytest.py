import pytest


from testingcidemo import f

def test_f():
    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 2
    assert f(3) == 3
    assert f(4) == 4
    assert f(5) == 5
    assert f(6) == 6
    assert f(7) == 7
    assert f(8) == 8
    assert f(9) == 9
    assert f(10) == 10

    with pytest.raises(ValueError):
        assert f(11) == 11
