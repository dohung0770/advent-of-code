from main import part1, part2


def test_part1():
    assert part1([
        'ugknbfddgicrmopn',
        'aaa',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb'
    ]) == 2

def test_part2():
    assert part2([
        'qjhvhtzxzqqjkmpb',
        'xxyxx',
        'uurcxstgmygtbstg',
        'ieodomkazucvgmuy'
    ]) == 2
