from main import part1, part2


def test_part1():
    assert part1(edges=[
        ('London', 'Dublin', 464),
        ('London', 'Belfast', 518),
        ('Dublin', 'Belfast', 141)
    ]) == 605

def test_part2():
    assert part2(edges=[
        ('London', 'Dublin', 464),
        ('London', 'Belfast', 518),
        ('Dublin', 'Belfast', 141)
    ]) == 982
