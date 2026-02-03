'''
--- Day 21: RPG Simulator 20XX ---
Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?




--- Part Two ---
Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?

'''

from collections import namedtuple
import math
import os


Item = namedtuple('Item', ['name', 'cost', 'damage', 'armor'])

weapons = [
    Item(name='Dagger', cost=8, damage=4, armor=0),
    Item(name='Shortsword', cost=10, damage=5, armor=0),
    Item(name='Warhammer', cost=25, damage=6, armor=0),
    Item(name='Longsword', cost=40, damage=7, armor=0),
    Item(name='Greataxe',  cost=74, damage=8, armor=0)
]

armors = [
    Item(name='Leather', cost=13, damage=0, armor=1),
    Item(name='Chainmail', cost=31, damage=0, armor=2),
    Item(name='Splintmail', cost=53, damage=0, armor=3),
    Item(name='Bandedmail', cost=75, damage=0, armor=4),
    Item(name='Platemail', cost=102, damage=0, armor=5)
]

rings = [
    Item(name='Damage +1', cost=25, damage=1, armor=0),
    Item(name='Damage +2', cost=50, damage=2, armor=0),
    Item(name='Damage +3', cost=100, damage=3, armor=0),
    Item(name='Defense +1', cost=20, damage=0, armor=1),
    Item(name='Defense +2', cost=40, damage=0, armor=2),
    Item(name='Defense +3', cost=80, damage=0, armor=3)
]


def attack(
    boss_hit_points: int,
    boss_damage: int,
    boss_armor: int,
    player_hit_points: int,
    player_damage: int,
    player_armor: int
) -> bool:
    '''
    Return True if player can defeat the boss.
    Player can attack first
    
    Parameters:
        boss_hit_points (int):
        boss_damage (int):
        boss_armor (int):
        player_hit_points (int):
        player_damage (int):
        player_armor (int):
        
    Returns:
        bool:
    '''
    
    player_dmg = max(1, player_damage - boss_armor)
    boss_dmg = max(1, boss_damage - player_armor)
    
    player_hit_counts = math.ceil(player_hit_points / boss_dmg)
    boss_hit_counts = math.ceil(boss_hit_points / player_dmg)
    
    return boss_hit_counts <= player_hit_counts
    
    # while player_hit_points > 0 and boss_hit_points > 0:
    #     boss_hit_points -= player_dmg
        
    #     if boss_hit_points <= 0: break
    #     player_hit_points -= boss_dmg
        
    # return boss_hit_points <= 0


def part1(
    boss_hit_points: int,
    boss_damage: int,
    boss_armor: int,
    player_hit_points: int = 100,
) -> int:
    '''
    Return least number of golds needed to buy items that help the player to defeat the Boss
    Each attach = max(1, attacker's damage - enemy's defense).
    Player starts with 0 damage and 0 armor.
    Can only by at 1 weapons, at most 1 armor and at most 2 rings.
    Each item can only be sold once.
    
    Parameters:
        boss_hit_points (int): Boss' hit points
        boss_damage (int): Boss' damage
        boss_armor (int): Boss' armor
        player_hit_points (int): Initial player's hit points
    
    Returns:
        int:
    '''
    
    if attack(
        boss_hit_points,
        boss_damage,
        boss_armor,
        player_hit_points,
        player_damage=0,
        player_armor=0
    ) is True:
        return 0
    
    M, N, K = len(weapons), len(armors), len(rings)
    
    best = float('inf')
    for i in range(M):
        dmg = weapons[i].damage
        c1 = weapons[i].cost
            
        for j in range(N + 1):
            armor, c2 = 0, 0
            
            if j < N:
                armor = armors[j].armor
                c2 = armors[j].cost
                
            for k in range(K + 1):
                d3, a3, c3 = 0, 0, 0
                
                if k < K:
                    d3 = rings[k].damage
                    a3 = rings[k].armor
                    c3 += rings[k].cost
                
                for l in range(k + 1, K + 1):
                    d4, a4, c4 = 0, 0, 0
                    
                    if l < K:
                        d4 = rings[l].damage
                        a4 = rings[l].armor
                        c4 = rings[l].cost
                        
                    if attack(
                        boss_hit_points,
                        boss_damage,
                        boss_armor,
                        player_hit_points,
                        player_damage=dmg + d3 + d4,
                        player_armor=armor + a3 + a4
                    ) is True:
                        best = min(best, c1 + c2 + c3 + c4)
                        
    return best


def part2(
    boss_hit_points: int,
    boss_damage: int,
    boss_armor: int,
    player_hit_points: int = 100,
) -> int:
    '''
    Return most number of golds the player can spend buy items but still lost to the fight.
    Each attach = max(1, attacker's damage - enemy's defense).
    Player starts with 0 damage and 0 armor.
    Can only by at 1 weapons, at most 1 armor and at most 2 rings.
    Each item can only be sold once.
    
    Parameters:
        boss_hit_points (int): Boss' hit points
        boss_damage (int): Boss' damage
        boss_armor (int): Boss' armor
        player_hit_points (int): Initial player's hit points
    
    Returns:
        int:
    '''
    
    M, N, K = len(weapons), len(armors), len(rings)
    
    best = 0
    for i in range(M):
        dmg = weapons[i].damage
        c1 = weapons[i].cost
            
        for j in range(N + 1):
            armor, c2 = 0, 0
            
            if j < N:
                armor = armors[j].armor
                c2 = armors[j].cost
                
            for k in range(K + 1):
                d3, a3, c3 = 0, 0, 0
                
                if k < K:
                    d3 = rings[k].damage
                    a3 = rings[k].armor
                    c3 += rings[k].cost
                
                for l in range(k + 1, K + 1):
                    d4, a4, c4 = 0, 0, 0
                    
                    if l < K:
                        d4 = rings[l].damage
                        a4 = rings[l].armor
                        c4 = rings[l].cost
                        
                        
                    if attack(
                        boss_hit_points,
                        boss_damage,
                        boss_armor,
                        player_hit_points,
                        player_damage=dmg + d3 + d4,
                        player_armor=armor + a3 + a4
                    ) is False:
                        # print(f'cost={c1 + c2 + c3 + c4}, weapon={weapons[i] if i < M else 'None'}, armor={armors[j] if j < N else 'None'}, rings={rings[k] if k < K else 'None'},{rings[l] if l < K else 'None'}')
                        best = max(best, c1 + c2 + c3 + c4)
                        
    return best


if __name__ == '__main__':
    boss_hit_points, boss_damage, boss_armor = 0, 0, 0
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt')) as file:
        boss_hit_points = int(file.readline().strip().split(': ')[1])
        boss_damage = int(file.readline().strip().split(': ')[1])
        boss_armor = int(file.readline().strip().split(': ')[1])
        
    print(boss_hit_points, boss_damage, boss_armor)
    # print('Part 1', part1(boss_hit_points, boss_damage, boss_armor))
    print('Part 2', part2(boss_hit_points, boss_damage, boss_armor))
            
