from main import part1


def test_part1():
    assert part1(["", "abc", "aaa\"aaa", "\x27"]) == 12
