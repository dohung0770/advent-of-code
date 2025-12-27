import pytest
from main import part1, part2

sample_data1 = [
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC'
] # Expected: part1 = 140, part2 = 80

sample_data2 = [
    'OOOOO',
    'OXOXO',
    'OOOOO',
    'OXOXO',
    'OOOOO'
] # Expected: part1 = 772, part2 = 436

sample_data3 = [
    'RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE'
] # Expected: part1 = 1930, part2 = 1206

sample_data4 = [
    'EEEEE',
    'EXXXX',
    'EEEEE',
    'EXXXX',
    'EEEEE'
] # Expected: part2 = 236

sample_data5 = [
    'AAAAAA',
    'AAABBA',
    'AAABBA',
    'ABBAAA',
    'ABBAAA',
    'AAAAAA'
] # Expected: part2 = 368

@pytest.mark.skip(reason="Passed test")
def test_part1():
    assert part1(sample_data1) == 140
    assert part1(sample_data2) == 772
    assert part1(sample_data3) == 1930
    
def test_part2():
    assert part2(sample_data1) == 80
    assert part2(sample_data2) == 436
    assert part2(sample_data3) == 1206
    assert part2(sample_data4) == 236
    assert part2(sample_data5) == 368