'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?




--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

'''

import os
from typing import Callable


vowels = set(['a', 'e', 'i', 'o', 'u'])
disallowed = set(['ab', 'cd', 'pq', 'xy'])

def is_nice(s: str) -> bool:
    '''
    Check if the given string s is nice or naughty.
    A nice string must:
    - contain at least 3 vowels (aeiou)
    - contain at least one letter that appears twice in a row. i.e. xx
    - not contain any words in disallowed set

    Parameters:
        s (str): given string
        
    Returns:
        bool        
    '''
    
    vowel_cnt, xx = 0, False
    for i, char in enumerate(s):
        if char in vowels:
            vowel_cnt += 1
        
        if i > 0:
            if s[i - 1:i + 1] in disallowed:
                return False
            
            if s[i - 1] == char:
                xx = True
                
    return vowel_cnt >= 3 and xx is True


def is_nice2(s: str) -> bool:
    '''
    Check if the given string is nice or naughty.
    A string is nice if:
    - it contains a pair of any two letters that appears at least twice (not overlapping). i.e. xy__xy, aa____aa
    - it contains at least one letter which repeats with exactly one letter between them. i.e. xyx, efe, aaa

    Parameters:
        s (str): given string
        
    Returns:
        int    
    '''
    
    import re
    
    return re.search(r'((\w)(\w)).*(\1)', s) and re.search(r'(\w).(\1)', s)
    
    # if len(s) < 4:
    #     return False
    
    # repeated_two_letters, repeated_with_middle = False, False
    # seen = dict()
    
    # for i in range(1, len(s)):
    #     curr = s[i - 1: i + 1]
    #     if curr in seen and seen[curr] + 2 < i:
    #         repeated_two_letters = True
    #     seen[curr] = i - 1
            
    #     if i >= 2 and s[i - 2] == s[i]:
    #         repeated_with_middle = True
            
    #     if repeated_two_letters is True and repeated_with_middle is True:
    #         return True
        
    # return False


def solve(checker: Callable[[str], bool]) -> Callable[[list[str]], int]:
    
    def caller(strings: list[str]) -> int:
        print('checker', checker)
        tot = 0
        for word in strings:
            chk = checker(word)
            print(word, chk)
            if chk:
                tot += 1
                
        return tot

    return caller


def part1(data: list[str]) -> int:
    return solve(is_nice)(data)


def part2(data: list[str]) -> int:
    return solve(is_nice2)(data)



if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    # print('part 1', part1(data))
    print('part 2', part2(data))

