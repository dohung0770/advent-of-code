'''
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?



--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?


'''

import os

def kmp(s: str, sub: str) -> list[int]:
    n = len(sub)
    lps = [0] * n
    i, prev_lps = 1, 0

    while i < n:
        if sub[i] == sub[prev_lps]:
            lps[i] = prev_lps + 1
            prev_lps += 1
            i += 1
        elif prev_lps == 0:
            i += 1
        else:
            prev_lps = lps[prev_lps - 1]

    found = [] # store all possible 'mul' instructions starting indices
    i, j = 0, 0
    while i < len(s):
        if s[i] == sub[j]:
            i += 1
            j += 1
            if j == n:
                # found.append(i - n)
                found.append(i)
                j = lps[j - 1]

        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]

    return found

def part1(data: str) -> int:
    '''
    Implements mul(x, y) of all valid 'mul' instructions within given data, and returns the total

    Parameters:
        data (str): Given corrupted instructions

    Returns:
        int  
    '''

    found = kmp(data, 'mul(')

    tot = 0
    for idx in found:
        j = idx
        lhs, rhs = 0, 0
        while j < len(data) and data[j] != ',':
            if not ('0' <= data[j] <= '9'):
                lhs = None
                break

            lhs = lhs * 10 + int(data[j])
            j += 1

        if lhs is None:
            continue

        j += 1
        while j < len(data) and data[j] != ')':
            if not ('0' <= data[j] <= '9'):
                rhs = None
                break

            rhs = rhs * 10 + int(data[j])
            j += 1

        if rhs is None:
            continue

        print(f'{lhs} x {rhs}')
        tot += lhs * rhs
    
    print('total = ', tot)


def part2(data: str) -> int:
    '''
    Implements mul(x, y) of all valid 'mul' instructions within given data
        with preceeding 'do' or at the begining of the instruction,
            and returns the total

    Parameters:
        data (str): Given corrupted instructions

    Returns:
        int  
    '''

    found = kmp(data, 'mul(') # starting indices of mul instructions
    dos = [-1] + kmp(data, 'do') # list of 'do' instructions indices, starting of data can be treated as a 'do'
    donts = kmp(data, "don't")

    # print(dos)
    # print(donts)
    # print(found)

    tot = 0
    do_idx = 0
    dont_idx = 0
    for idx in found:
        while do_idx + 1 < len(dos) and dos[do_idx + 1] < idx:
            do_idx += 1

        while dont_idx + 1 < len(donts) and donts[dont_idx + 1] < idx:
            dont_idx += 1

        # print(f'idx={idx}, do_idx={do_idx}, dont_idx={dont_idx}')

        if dont_idx < len(donts) and dos[do_idx] < donts[dont_idx] < idx:
            continue

        j = idx
        lhs, rhs = 0, 0
        while j < len(data) and data[j] != ',':
            if not ('0' <= data[j] <= '9'):
                lhs = None
                break

            lhs = lhs * 10 + int(data[j])
            j += 1

        if lhs is None:
            continue

        j += 1
        while j < len(data) and data[j] != ')':
            if not ('0' <= data[j] <= '9'):
                rhs = None
                break

            rhs = rhs * 10 + int(data[j])
            j += 1

        if rhs is None:
            continue

        print(f'{lhs} x {rhs}')
        tot += lhs * rhs
    
    print('total = ', tot)


if __name__ == '__main__':
    data = None
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        data = file.readlines()

    # print('----- Part 1 -----')
    # part1('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
    # part1(''.join(data))

    print('----- Part 2 -----')
    # part2('''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))''')
    part2(''.join(data))
