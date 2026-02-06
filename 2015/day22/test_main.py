from main import part1, Player


def test_part1():
    assert part1(
        player=Player(hp=10, mana=250, damage=0, armor=0),
        boss=Player(hp=13, damage=8, armor=0, mana=0)
    ) == 173 + 53 # Posion + Missile

    assert part1(
        player=Player(hp=10, mana=250, damage=0, armor=0),
        boss=Player(hp=14, damage=8, armor=0, mana=0)
    ) == 229 + 113 + 73 + 173 + 53 # Recharge + Shield + Drain + Poison + Missile
