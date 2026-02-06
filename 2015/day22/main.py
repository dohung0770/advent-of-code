'''
--- Day 22: Wizard Simulator 20XX ---
Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)



--- Part Two ---
On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?

'''

from collections import namedtuple
import heapq


Spell = namedtuple('Spell', ['code', 'name', 'cost', 'duration', 'damage', 'armor', 'hp', 'mana'])

class Player:
    def __init__(self, hp: int, damage: int, armor: int, mana: int):
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.mana = mana

    def copy(self) -> 'Player':
        return Player(self.hp, self.damage, self.armor, self.mana)
    
    def __repr__(self) -> str:
        return f'Player(hp={self.hp},mana={self.mana},armor={self.armor})'

missile = Spell(code='missile', name='Magic Missile', cost=53, duration=1, damage=4, armor=0, hp=0, mana=0)
drain = Spell(code='drain', name='Drain', cost=73, duration=1, damage=2, armor=0, hp=2, mana=0)
shield = Spell(code='shield', name='Shield', cost=113, duration=6, damage=0, armor=7, hp=0, mana=0)
poison = Spell(code='poison', name='Poison', cost=173, duration=6, damage=3, armor=0, hp=0, mana=0)
recharge = Spell(code='recharge', name='Recharge', cost=229, duration=5, damage=0, armor=0, hp=0, mana=101)


def part1(player: Player, boss: Player, hp_decrease_per_turn: int = 0) -> int:
    '''
    Return least amount of starting mana the player can spend to defeat the boss.
    The player casts spell first. Then the boss's turn to attack
    
    Parameters:
        player (Player): Given player's stats
        boss (Player): Given boss's stats
        hp_decrease_per_turn (int): Amount of hp the player looses at starting of his turns
        
    Returns:
        int:
    '''
    
    # def solve(turn: int, stats: Player, boss_hp: int, effects: list[tuple[int, int]]) -> int:
    #     next_effects = []
    #     curr = stats.copy()
    #     curr.armor = 0

    #     for index, duration in effects:
    #         sp = spells[index]
            
    #         if sp.code == 'missile':
    #             boss_hp -= sp.damage
    #         elif sp.code =='drain':
    #             boss_hp -= sp.damage
    #             curr.hp += 2
    #         elif sp.code == 'shield':
    #             curr.armor = sp.armor
    #         elif sp.code == 'poison':
    #             boss_hp -= sp.damage
    #         elif sp.code == 'recharge':
    #             curr.mana += sp.mana
            
    #         duration -= 1
            
    #         if duration > 0:
    #             next_effects.append((index, duration))

    #     # print(turn, curr, boss_hp, [(spells[index].code, duration) for index, duration in next_effects])

    #     if stats.hp <= 0:
    #         return float('inf') # Player looses
                
    #     if boss_hp <= 0:
    #         return 0
        
    #     if turn == 1: # Boss'turn
    #         curr.hp -= max(1, boss.damage - curr.armor)
    #         return solve(0, curr, boss_hp, next_effects)


    #     # Player's turn
    #     best = float('inf')
    #     for i, sp in enumerate(spells):
    #         if curr.mana < sp.cost:
    #             continue # Can't afford that spell
            
    #         if any(idx == i for idx, _ in next_effects):
    #             continue # Spell still has effect
            
    #         next_stats = curr.copy()
    #         next_stats.mana -= sp.cost
    #         next_effects.append((i, sp.duration))
    #         best = min(
    #             best,
    #             sp.cost + solve(1, next_stats, boss_hp, next_effects)
    #         )
    #         next_effects.pop()
            
    #     return best
                
    # return solve(0, player, boss_hp=boss.hp, effects=[])
    

    
    class State:
        def __init__(self, player_hp: int = 0, armor: int = 0, mana: int = 0, boss_hp: int = 0, missile: int = 0, drain: int = 0, shield: int = 0, poison: int = 0, recharge: int = 0):
            self.player_hp = player_hp
            self.armor = armor
            self.mana = mana
            self.boss_hp = boss_hp
            self.missile = missile
            self.drain = drain
            self.shield = shield
            self.poison = poison
            self.recharge = recharge
            
        def copy(self) -> 'State':
            return State(
                self.player_hp,
                self.armor,
                self.mana,
                self.boss_hp,
                self.missile,
                self.drain,
                self.shield,
                self.poison,
                self.recharge
            )
            
        def __lt__(self, other) -> int:
            return 0
            
        def __repr__(self) -> str:
            return f'player (hp={self.player_hp}, armor={self.armor}, mana={self.mana}), boss hp={self.boss_hp}, (m={self.missile}, d={self.drain}, s={self.shield}, p={self.poison}, r={self.recharge})'
            

    heap = [(0, 0, State(
        player_hp=player.hp,
        mana=player.mana,
        boss_hp=boss.hp,
    ), [])]
    visited = set()
    
    while heap:
        mana_spent, turn, curr, logs = heapq.heappop(heap)
        
        state = (turn, curr)
        if state in visited:
            continue
        
        visited.add(state)
        
        if turn == 0:
            curr.player_hp -= hp_decrease_per_turn
            
        if curr.player_hp <= 0:
            continue
        
        # reset player's armor
        curr.armor = 0
        
        if curr.missile:
            curr.boss_hp -= missile.damage
            curr.missile -= 1
        if curr.drain:
            curr.boss_hp -= drain.damage
            curr.player_hp += drain.hp
            curr.drain -= 1
        if curr.shield:
            curr.armor = shield.armor
            curr.shield -= 1
        if curr.poison:
            curr.boss_hp -= poison.damage
            curr.poison -= 1
        if curr.recharge:
            curr.mana += recharge.mana
            curr.recharge -= 1

        # print(mana_spent, turn, curr)
            
        if curr.player_hp <= 0:
            continue
            
        if curr.boss_hp <= 0:
            print(logs)
            return mana_spent
        
        if turn == 1:
            curr.player_hp -= max(1, boss.damage - curr.armor)
            
            l = [*logs] + [f'\nBoss attack: {curr.__repr__()}']
            
            if curr.player_hp > 0:
                heapq.heappush(heap, (mana_spent, 0, curr, l))

            continue

        if curr.mana >= missile.cost:
            nxt = curr.copy()
            nxt.mana -= missile.cost
            nxt.missile = 1
            
            l = [*logs] + [f'\nCast missile: {nxt.__repr__()}, spent={mana_spent + missile.cost} ({mana_spent} + {missile.cost})']
            heapq.heappush(heap, (mana_spent + missile.cost, 1 - turn, nxt, l))
            
        if curr.mana >= drain.cost:
            nxt = curr.copy()
            nxt.mana -= drain.cost
            nxt.drain = 1
            
            l = [*logs] + [f'\nCast drain: {nxt.__repr__()}, spent={mana_spent + drain.cost} ({mana_spent} + {drain.cost})']
            heapq.heappush(heap, (mana_spent + drain.cost, 1 - turn, nxt, l))
            
        if curr.shield == 0 and curr.mana >= shield.cost:
            nxt = curr.copy()
            nxt.mana -= shield.cost
            nxt.shield = shield.duration
            
            l = [*logs] + [f'\nCast shield: {nxt.__repr__()}, spent={mana_spent + shield.cost} ({mana_spent} + {shield.cost})']
            heapq.heappush(heap, (mana_spent + shield.cost, 1 - turn, nxt, l))
            
        if curr.poison == 0 and curr.mana >= poison.cost:
            nxt = curr.copy()
            nxt.mana -= poison.cost
            nxt.poison = poison.duration
            
            l = [*logs] + [f'\nCast poison: {nxt.__repr__()}, spent={mana_spent + poison.cost} ({mana_spent} + {poison.cost})']
            heapq.heappush(heap, (mana_spent + poison.cost, 1 - turn, nxt, l))
            
        if curr.recharge == 0 and curr.mana >= recharge.cost:
            nxt = curr.copy()
            nxt.mana -= recharge.cost
            nxt.recharge = recharge.duration
            
            l = [*logs] + [f'\nCast recharge: {nxt.__repr__()}, spent={mana_spent + recharge.cost} ({mana_spent} + {recharge.cost})']
            heapq.heappush(heap, (mana_spent + recharge.cost, 1 - turn, nxt, l))
            
    return -1


if __name__ == '__main__':
    # Boss stats
    # Hit Points: 51
    # Damage: 9
    
    # print('Part 1', part1(
    #     Player(50, 0, 0, 500),
    #     Player(51, 9, 0, 0)
    # ))
    
    print('Part 2', part1(
        Player(50, 0, 0, 500),
        Player(51, 9, 0, 0),
        1
    ))
