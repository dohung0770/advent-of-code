import pytest
from main import preprocess_data, part1, part2


sample = [
    'Register A: 729',
    'Register B: 0',
    'Register C: 0',
    '',
    'Program: 0,1,5,4,3,0',
]

@pytest.mark.skip("test passed")
def test_part1():
    assert part1(*preprocess_data(sample)) == '4,6,3,5,6,3,5,2,1,0'
    assert part1(A=0, B=0, C=9, program=[2, 6]) == ''
    assert part1(A=10, B=0, C=0, program=[5,0,5,1,5,4]) == '0,1,2'
    assert part1(A=2024, B=0, C=0, program=[0,1,5,4,3,0]) == '4,2,5,6,7,7,7,7,3,1,0'
    assert part1(A=0, B=29, C=0, program=[1,7]) == ''
    assert part1(A=2024, B=0, C=43690, program=[4,0]) == ''
    
def test_part2():
    assert part2(0, 0, [0,3,5,4,3,0]) == 117440