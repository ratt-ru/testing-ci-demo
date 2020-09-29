import pytest


from testingcidemo import f


@pytest.mark.parametrize("i", range(12))
def test_f(i):
    assert f(i) == i