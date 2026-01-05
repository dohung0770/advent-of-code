import pytest
from main import parse_input, part1, part2


@pytest.mark.skip('test passed')
def test_part1():
    assert part1(race_time=1000, reindeers=parse_input([
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
    ])) == 1120
    
    
def test_part2():
    assert part2(race_time=1000, reindeers=parse_input([
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
    ])) == 689
