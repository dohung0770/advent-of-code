'''
--- Day 7: Bridge Repair ---
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?



--- Part Two ---
The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
192: 17 8 14 can be made true using 17 || 8 + 14.
Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?

'''
    
def solver(operators: list[str]):
    def calc(lhs: int, rhs: int, op: str) -> int:
        if op == '+':
            return lhs + rhs
        if op == '*':
            return lhs * rhs
        if op == '||': # concatenation operator
            return lhs * pow(10, len(str(rhs))) + rhs

        raise ValueError(f"Invalid operator {op}")
    
    def dp(target: int, nums: list[int], prev: int, i: int) -> bool:
        if i == len(nums):
            return prev == target
        
        if prev > target:
            return False
        
        for op in operators:
            if dp(target, nums, calc(prev, nums[i], op), i + 1) is True:
                return True
        
        return False
            
    return dp

def part1(expected: list[int], values: list[list[int]]) -> int:
    '''
    Returns total of expected results expected[i] that can be made True using values[i] with operators + and *
    applied from left-to-right, regardless of the precendence rules (i.e. multiplication first, addition later)
    
    Parameters:
        expected (list[int]): list of expected results
        values (list[list[int]]): list of numbers, values[i] is list of numbers that is expected to produce expected[i]
        
    Returns:
        int
    '''
            
    dp = solver(['+', '*'])
    tot = 0
    for i in range(len(expected)):
        if dp(expected[i], values[i], values[i][0], 1) is True:
            tot += expected[i]
            
    return tot


def part2(expected: list[int], values: list[list[int]]) -> int:
    '''
    Same as part 1, but with one extra operator: the concatenation operator (||) the combines two numbers together,
    i.e 13 || 456 = 13456
    
    Parameters:
        expected (list[int]): list of expected results
        values (list[list[int]]): list of numbers, values[i] is list of numbers that is expected to produce expected[i]
        
    Returns:
        int
    '''
            
    dp = solver(['+', '*', '||'])
    tot = 0
    for i in range(len(expected)):
        if dp(expected[i], values[i], values[i][0], 1) is True:
            tot += expected[i]
            
    return tot


expected = []
values = []

def preprocess_input(data: list[str]):
    for line in data:
        result, rest = line.split(': ')
        expected.append(int(result))
        values.append(list(map(int, rest.split(' '))))


import os

if __name__ == '__main__':
    # sample_data = [
    #     '190: 10 19',
    #     '3267: 81 40 27',
    #     '83: 17 5',
    #     '156: 15 6',
    #     '7290: 6 8 6 15',
    #     '161011: 16 10 13',
    #     '192: 17 8 14',
    #     '21037: 9 7 18 13',
    #     '292: 11 6 16 20'
    # ]
    
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    # preprocess_input(sample_data)
    preprocess_input(data)
    
    # print('---- Part 1 ----')
    # print('result = ', part1(expected, values))
    
    print('---- Part 2 ----')
    print('result = ', part2(expected, values))
