import pytest
from main import part1, part2


@pytest.mark.skip('test passed')
def test_part1():
    assert part1('[1,2,3]') == 6
    assert part1('{"a":2,"b":4}') == 6
    assert part1('[[[3]]]') == 3
    assert part1('{"a":{"b":4},"c":-1}') == 3
    assert part1('{"a":[-1,1]}') == 0
    assert part1('[-1,{"a":1}]') == 0
    assert part1('[]') == 0
    assert part1('{}') == 0
    assert part1('{"a":[1,{"b":2,"c":[3],"d":{"e":"a","f":"b","g":-1}}],"i":"c","j":-3,"h":[-1,"a",5,-2,"f"]}') == 4


def test_part2():
    assert part2('[1,2,3]') == 6
    assert part2('[1,{"c":"red","b":2},3]') == 4
    assert part2('{"d":"red","e":[1,2,3,4],"f":5}') == 0
    assert part2('[1,"red",5]') == 6 
