import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_smoke():
    assert all_division(10) == 10


def test_my():
    assert all_division(10, 5) == 2


def test_my2():
    assert all_division(10, 5, 2) == 1


def test_my3():
    assert all_division(10, 5, 2, 2) == 0.5


@pytest.mark.smoke
def test_not_my():
    try:
        all_division(10, 5, 2, 2, 0)
    except ZeroDivisionError:
        assert True
