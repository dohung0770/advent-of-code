import pytest
from main import parse_input, part1, part2


@pytest.mark.skip('test passed')
def test_part1():
    assert part1(parse_input([
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ]), 100) == 62842880


def test_part2():
    assert part2(ingredients=parse_input([
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ]), k=100, total_calories=500) == 57600000