import pytest
import simple_module

simple_class = simple_module.SimpleClass()


@pytest.mark.parametrize(
    "x, y, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9), (5, 6, 11)]
)
def test_sum(x, y, expected):
    assert simple_class.sum(x, y) == expected
