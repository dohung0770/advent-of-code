import pytest
from main import part1


sample_data = [
    '###############',
    '#...#...#.....#',
    '#.#.#.#.#.###.#',
    '#S#...#.#.#...#',
    '#######.#.#.###',
    '#######.#.#...#',
    '#######.#.###.#',
    '###..E#...#...#',
    '###.#######.###',
    '#...###...#...#',
    '#.#####.#.###.#',
    '#.#...#.#.#...#',
    '#.#.#.#.#.#.###',
    '#...#...#...###',
    '###############'
]

def test_part1():
    # actual shortest path costs 84 picoseconds
    assert part1(sample_data, 64) == 1
    assert part1(sample_data, 40) == 1 + 1
    assert part1(sample_data, 10) == 2 + 3 + 1 + 1 + 1 + 1 + 1
    assert part1(sample_data, 2) == 14 + 14 + 2 + 4 + 2 + 3 + 1 + 1 + 1 + 1 + 1
