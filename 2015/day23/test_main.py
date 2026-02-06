from main import part1

def test_part1():
    assert part1([
        ['inc', 'a'],
        ['jio', 'a', 2],
        ['tpl', 'a'],
        ['inc', 'a']
    ]) == { 'a': 2, 'b': 0 }
    