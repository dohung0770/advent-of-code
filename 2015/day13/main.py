'''
--- Day 13: Knights of the Dinner Table ---
In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?




--- Part Two ---
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?



'''

from collections import defaultdict
from functools import cache


def parse_input(data: list[str]) -> list[tuple[str, str, int]]:
    prediction = []
    for line in data:
        p = line.split(' ')
        prediction.append((p[0], p[-1][:-1], int(p[3]) * (-1 if p[2] == 'lose' else 1)))
        
    return prediction


def solver(n: int, g: dict[str, dict[str, int]], person_ids: dict[str, int], first_person: str):
    is_all_settled = (1 << n) - 1

    @cache
    def fn(mask: int, prev_person: str) -> int:
        if mask == is_all_settled:
            return g[prev_person][first_person] + g[first_person][prev_person]
        
        cost = float('-inf')
        for neighbor in g[prev_person]:
            submask = 1 << person_ids[neighbor]
            
            if (mask & submask) == 0:
                cost = max(
                    cost,
                    g[prev_person][neighbor] + \
                        g[neighbor][prev_person] + \
                        fn(mask | submask, neighbor)
                )
                
        return cost
    
    return fn(1 << person_ids[first_person], first_person)


def part1(prediction: list[tuple[str, str, int]]) -> int:
    '''
    Calculate the total happiness by setting people to seat in a circular table.
    Every pair of people has the change in happiness calculated

    Parameters:
        prediction (list[tuple[str, str, int]]): (= list [A, B, happiness])
            Calculated happiness change if let person A seats next to person B.
            
    Returns:
        int: total change in happiness
    '''
    
    person_ids = dict()
    pid = 0
    
    g = defaultdict(dict[str, int])
    first_person = None
    
    for person1, person2, happiness in prediction:
        g[person1][person2] = happiness
        
        if person1 not in person_ids:
            person_ids[person1] = pid
            pid += 1
        if person2 not in person_ids:
            person_ids[person2] = pid
            pid += 1
            
        if first_person is None:
            first_person = person1
        
    n = pid # number of people you're inviting
    
    if n == 1:
        return 0 # there is only one person who's comming
    
    return solver(n, g, person_ids, first_person)
    
    
def part2(prediction: list[tuple[str, str, int]]):
    '''
    Same as part 1, except this includes yourself.

    Parameters:
        prediction (list[tuple[str, str, int]]): (= list [A, B, happiness])
            Calculated happiness change if let person A seats next to person B.
            
    Returns:
        int: total change in happiness
    '''
    
    you = 'You'
    person_ids = { 'You': 0 }
    pid = 1
    
    g = defaultdict(dict[str, int])
    
    for person1, person2, happiness in prediction:
        g[person1][person2] = happiness
        
        if person1 not in person_ids:
            person_ids[person1] = pid
            pid += 1
            
            g[you][person1] = g[person1][you] = 0

        if person2 not in person_ids:
            person_ids[person2] = pid
            pid += 1
            
            g[you][person2] = g[person2][you] = 0

        
    n = pid # number of people you're inviting
    
    if n == 1:
        return 0 # there is only one person who's comming
    
    return solver(n, g, person_ids, you)


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
            
    prediction = parse_input(data)

    # print('part 1', part1(prediction))
    print('part 2', part2(prediction))
