import pytest
from main import parse_input, part1, part2


@pytest.mark.skip('test passed')
def test_part1():
    assert part1(*parse_input([
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOH'
    ])) == 4


def test_part2():
    assert part2(*parse_input([
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOH'
    ])) == 3

    assert part2(*parse_input([
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOHOHO'
    ])) == 6
