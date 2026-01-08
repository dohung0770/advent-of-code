'''
--- Day 19: Medicine for Rudolph ---
Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH
Given the replacements above and starting with HOH, the following molecules could be generated:

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).
So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?



--- Part Two ---
Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH
If you'd like to make HOH, you start with e, and then make the following replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH
So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

'''

import os
from collections import defaultdict
from functools import cache


def parse_input(data: list[str]) -> tuple[list[tuple[str, str]], str]:
    flag = False
    replacements = []
    molecule = None
    
    for line in data:
        if line == '':
            flag = True
            continue
        
        if flag is True:
            molecule = line
        else:
            replacements.append(line.split(' => '))
            
    return (replacements, molecule)
    

def part1(replacements: list[list[str]], molecule: str) -> int:
    '''
    Count number of distinct molecules that can be generated after 1 replacement.

    Parameters:
        replacements (list[list[str]]): list of replacements [from, to] = 'from' can generate 'to'
        molecule (str): current molecule
        
    Returns:
        int
    '''
    
    max_char_length = 0
    replacement_dict = defaultdict(list[str])
    for from_char, to_char in replacements:
        replacement_dict[from_char].append(to_char)
        max_char_length = max(max_char_length, len(from_char))
        

    n = len(molecule)
    generated = set[str]()
    for i in range(n):
        j = i
        
        while j - i + 1 <= max_char_length:
            if (curr_char := molecule[i:j + 1]) in replacement_dict:
                for rep in replacement_dict[curr_char]:
                    generated.add(molecule[:i] + rep + molecule[j + 1:])
                    
                break
                
            j += 1
            
    return len(generated)


def part2(replacements: list[list[str]], molecule: str) -> int:
    '''
    Count the fewest replacements it takes to make the medicine molecule from 'e'

    Parameters:
        replacements (list[list[str]]): list of replacements [from, to] = 'from' can generate 'to'
        molecule (str): current molecule
        
    Returns:
        int
    '''
    
    max_char_length = 0
    replacement_dict = defaultdict(list[str])
    for from_char, to_char in replacements:
        replacement_dict[from_char].append(to_char)
        max_char_length = max(max_char_length, len(from_char))
        
        
    @cache
    def solve(curr: str) -> int:
        if curr == molecule:
            return 0
        
        if len(curr) > len(molecule):
            return float('inf')
        
        ans = float('inf')
        for i in range(len(curr)):
            j = i
        
            while j - i + 1 <= max_char_length:
                if (curr_char := curr[i:j + 1]) in replacement_dict:
                    for rep in replacement_dict[curr_char]:
                        ans = min(
                            ans,
                            1 + solve(curr[:i] + rep + curr[j + 1:])
                        )
                        
                    break
                    
                j += 1
                
        return ans
    
    return solve('e')


if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
            
    replacements, molecule = parse_input(data)

    # print('part 1', part1(replacements, molecule))
    print('part 2', part2(replacements, molecule))
