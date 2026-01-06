import pytest
from main import part1, part2


@pytest.mark.skip('test passed')
def test_part1():
    assert part1([20, 15, 10, 5, 5], 25) == 4


def test_part2():
    assert part2([20, 15, 10, 5, 5], 25) == 3

# [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
