import pytest
from main import part1, part2


@pytest.mark.skip('test passed')
def test_part1():
    assert part1([
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..'
    ], 4) == 4

def test_part2():
    assert part2([
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..'
    ], 5) == 17
