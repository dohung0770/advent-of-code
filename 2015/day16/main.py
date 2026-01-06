'''
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?



--- Part Two ---
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

'''

from AuntSue import AuntSue


def parse_input(data: list[str]) -> list[AuntSue]:
    lst = []
    for line in data:
        line = line + ','
        p = line.split(' ')
        sue = AuntSue(ordinal=int(p[1][:-1]))
        
        for i in range(2, len(p), 2):
            setattr(sue, p[i][:-1], int(p[i + 1][:-1]))
        
        lst.append(sue)
        
    return lst


def part1(aunts: list[AuntSue]) -> int:
    '''
    Find the Aunt Sue's number that has specs that matches the analysis results.

    Parameters:
        aunts (list[AuntSue]): list of Aunt Sue's specs
        
    Returns:
        int: the Aunt Sue' number who'll receive the gift.    
    '''
    
    # specs = {
    #     'children': 3,
    #     'cats': 7,
    #     'samoyeds': 2,
    #     'pomeranians': 3,
    #     'akitas': 0,
    #     'vizslas': 0,
    #     'goldfish': 5,
    #     'trees': 3,
    #     'cars': 2,
    #     'perfumes': 1,
    # }
    
    for sue in aunts:
        if (sue.children is None or sue.children == 3) and \
            (sue.cats is None or sue.cats == 7) and \
            (sue.samoyeds is None or sue.samoyeds == 2) and \
            (sue.pomeranians is None or sue.pomeranians == 3) and \
            (sue.akitas is None or sue.akitas == 0) and \
            (sue.vizslas is None or sue.vizslas == 0) and \
            (sue.goldfish is None or sue.goldfish == 5) and \
            (sue.trees is None or sue.trees == 3) and \
            (sue.cars is None or sue.cars == 2) and \
            (sue.perfumes is None or sue.perfumes == 1):
            return sue.ordinal
        
    return -1

def part2(aunts: list[AuntSue]) -> int:
    '''
    Same as part 1, except no some field's data represent range instead of exact value

    Parameters:
        aunts (list[AuntSue]): list of Aunt Sue's specs
        
    Returns:
        int: the Aunt Sue' number who'll receive the gift.    
    '''
    
    for sue in aunts:
        if (sue.children is None or sue.children == 3) and \
            (sue.cats is None or sue.cats > 7) and \
            (sue.samoyeds is None or sue.samoyeds == 2) and \
            (sue.pomeranians is None or sue.pomeranians < 3) and \
            (sue.akitas is None or sue.akitas == 0) and \
            (sue.vizslas is None or sue.vizslas == 0) and \
            (sue.goldfish is None or sue.goldfish < 5) and \
            (sue.trees is None or sue.trees > 3) and \
            (sue.cars is None or sue.cars == 2) and \
            (sue.perfumes is None or sue.perfumes == 1):
            return sue.ordinal
        
    return -1


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
            
    aunts = parse_input(data)
    # print('part 1', part1(aunts))
    print('part 2', part2(aunts))
