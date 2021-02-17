# coding: utf-8
import pytest


def add(x: int, y: int) -> int:
    return x + y


def raise_exception(enable: bool = True):
    if enable:
        raise RuntimeError("Exception test.")


@pytest.fixture
def setup_teardown():
    print("\nSet up.\n")
    yield
    print("\nTear down.\n")


@pytest.mark.parametrize(
    "x, y, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9), (5, 6, 11)]
)
def test_add(setup_teardown, x, y, expected):
    assert add(x, y) == expected


def test_raise_exception_success():
    # do not raise RuntimeError
    raise_exception(enable=False)


def test_raise_exception_error():
    with pytest.raises(RuntimeError):
        raise_exception(enable=True)
