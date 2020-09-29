import pytest


from testingcidemo import f, multi


@pytest.mark.parametrize("i", list(range(0, 4)) + list(range(5, 11)))
def test_f_success(i):
    assert f(i) == i


@pytest.mark.parametrize("i", [4])
def test_f_4(i):
    assert f(i) == "Apples"


@pytest.mark.xfail
@pytest.mark.parametrize("i", [-1, 11])
def test_f_4(i):
    assert f(i) == i


@pytest.mark.parametrize("i, o", [
    (0, 0),
    (1, 1),
    (4, "Apples"),
    pytest.param(11, 11, marks=pytest.mark.xfail),
])
def test_f_success_another(i, o):
    assert f(i) == o


@pytest.mark.parametrize("x", [0, 1, 3, 6, 8])
@pytest.mark.parametrize("y", range(1, 10))
def test_outer_product(x, y):
    assert multi(x, y) == x*y
