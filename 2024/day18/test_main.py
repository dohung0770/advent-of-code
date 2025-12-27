import pytest
from main import part1, part2

sample = [
    '5,4',
    '4,2',
    '4,5',
    '3,0',
    '2,1',
    '6,3',
    '2,4',
    '1,5',
    '0,6',
    '3,3',
    '2,6',
    '5,1',
    '1,2',
    '5,5',
    '2,5',
    '6,5',
    '1,4',
    '0,4',
    '6,4',
    '1,1',
    '6,1',
    '1,0',
    '0,5',
    '1,6',
    '2,0'
]


@pytest.mark.skip("test passed")
def test_part1():
    assert part1(7, 7, [list(map(int, line.split(','))) for line in sample], t=12) == 22
    
def test_part2():
    assert part2(7, 7, [list(map(int, line.split(','))) for line in sample]) == '6,1'