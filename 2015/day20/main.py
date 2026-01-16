'''
--- Day 20: Infinite Elves and Infinite Houses ---
To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is 33100000.





--- Part Two ---
The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

'''

import math


def part1(gifts: int) -> int:
    '''
    Return the least house number that receives at least 'gifts' presents from the Elves.

    Parameters:
        gifts (int): least number of presents
    
    Returns:
        int:    
    '''
    
    # each Elf gives 10 times of his or her number of gifts to each house
    gifts //= 10
    
    if gifts <= 1:
        return 1
    
    num = 2
    
    def count_gifts(curr: int) -> int:
        cnt = 0

        for d in range(1, math.floor(math.sqrt(curr)) + 1):
            if curr % d == 0:
                cnt += d
                if curr // d != d:
                    cnt += curr // d
                    
        return cnt
    
    while True:
        tot_gifts = count_gifts(num)
                
        # print(f'House {num} got {tot_gifts * 10} presents')
                
        if tot_gifts >= gifts:
            return num
        
        num += 1


def part2(gifts: int):
    '''
    Same with part 1, except now the Elves only deliver gifts to 50 houses with 11 presents each house.
    Return the least house number that receive at least 'gifts' presents.

    Parameters:
        gifts (int): least number of presents.
    
    Returns:
        int: least house number that receive at least the input presents.
    '''
    
    # Now each Elf gives 11 times of his or her number of gifts to each house
    if gifts <= 11:
        return 1
    
    num = math.ceil(gifts / 11)
    
    def count_gifts(curr: int) -> int:
        cnt = 0
        
        start = 1
        print('start = ', start)

        for d in range(start, math.floor(math.sqrt(curr)) + 1):
            if curr % d == 0:
                cnt += d
                
                compl = curr // d
                print(d, compl)
                if compl >= start and compl != d:
                    cnt += compl
                    
        return cnt * 11
    
    print(count_gifts(gifts))
    return 0
    
    while True:
        tot_gifts = count_gifts(num)
                
        print(f'House {num} got {tot_gifts * 11} presents')
                
        if tot_gifts >= gifts:
            return num
        
        num += 1


if __name__ == '__main__':
    # print('part 1', part1(33100000)) # 776160
    print('part 2', part2(33100000))
