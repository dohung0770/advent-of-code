import pytest
from main import preprocess_input, part1, part2


sample_data = [
    'r, wr, b, g, bwu, rb, gb, br',
    '',
    'brwrr',
    'bggr',
    'gbbr',
    'rrbgbr',
    'ubwu',
    'bwurrg',
    'brgr',
    'bbrgwb'
]

@pytest.mark.skip("test passed")
def test_part1():
    towels, designs = preprocess_input(sample_data)
    assert part1(towels, designs) == 6
    
def test_part2():
    towels, designs = preprocess_input(sample_data)
    assert part2(towels, designs) == 16
