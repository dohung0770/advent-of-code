'''
--- Day 13: Claw Contraption ---
Next up: the lobby of a resort on a tropical island. The Historians take a moment to admire the hexagonal floor tiles before spreading out.

Fortunately, it looks like the resort has a new arcade! Maybe you can win some prizes from the claw machines?

The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons labeled A and B. Worse, you can't just put in a token and play; it costs 3 tokens to push the A button and 1 token to push the B button.

With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the right (along the X axis) and a specific amount forward (along the Y axis) each time that button is pressed.

Each machine contains one prize; to win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.

You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every machine's button behavior and prize location (your puzzle input). For example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
This list describes the button configuration and prize location of four different claw machines.

For now, consider just the first claw machine in the list:

Pushing the machine's A button would move the claw 94 units along the X axis and 34 units along the Y axis.
Pushing the B button would move the claw 22 units along the X axis and 67 units along the Y axis.
The prize is located at X=8400, Y=5400; this means that from the claw's initial position, it would need to move exactly 8400 units along the X axis and exactly 5400 units along the Y axis to be perfectly aligned with the prize in this machine.
The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.

For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is by pushing the A button 38 times and the B button 86 times. Doing this would cost a total of 200 tokens.

So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is 480.

You estimate that each button would need to be pressed no more than 100 times to win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?

'''

import os
import heapq
import re
from functools import cache


def part1(A: list[list[int]], B: list[list[int]], prize: list[list[int]]) -> int:
    '''
    There are some claw machines with two buttons A, B on each.
    Returns the minimum tokens needed to win the most prizes at the claw machines, within at most 100 presses per button.
    It's also impossible to win the prize under any combination of buttons presses.

    Parameters:
        A (list[list[int]]): A[i] = (x, y), upon each press, it moves the claw position to +x, +y, and costs <b>3</b> tokens.
        B (list[list[int]]): A[i] = (x, y), upon each press, it moves the claw position to +x, +y, and costs <b>1</b> token.
        prize (list[list[int]]): position (x, y) of prize at each claw machine.

    Returns:
        tokens (int): fewest tokens needed to win the most prizes
    '''
    
    def solve(machine_index: int) -> int:
        tx, ty = prize[machine_index]
        ax, ay = A[machine_index]
        bx, by = B[machine_index]
        heap = [(0, 0, 0, 0, 0)] # (tokens, number of button A presses, number of button B presses, current x, current y)
        visited = set([(0, 0)]) # (A presses, B presses)
        
        while heap:
            tokens, a_presses, b_presses, x, y = heapq.heappop(heap)
            if x == tx and y == ty:
                return tokens
            
            if a_presses < 100 and \
                (nx := x + ax) <= tx and \
                (ny := y + ay) <= ty and \
                (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(heap, (tokens + 3, a_presses + 1, b_presses, nx, ny))
                
            if b_presses < 100 and \
                (nx := x + bx) <= tx and \
                (ny := y + by) <= ty and \
                (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(heap, (tokens + 1, a_presses, b_presses + 1, nx, ny))
                
        return 0
    
    tot = 0
    for i in range(len(prize)):
        t = solve(i)
        # print(f'machine #{i + 1}', t)
        tot += t
        
    return tot


def part2(A: list[list[int]], B: list[list[int]], prize: list[list[int]]) -> int:
    '''
    Same with part 1, except that the prizes' positions are shifted 10000000000000 away in the x and y coordinates,
    and there is not limitation on how many presses on each button.

    Parameters:
        A (list[list[int]]): A[i] = (x, y), upon each press, it moves the claw position to +x, +y, and costs <b>3</b> tokens.
        B (list[list[int]]): A[i] = (x, y), upon each press, it moves the claw position to +x, +y, and costs <b>1</b> token.
        prize (list[list[int]]): position (x, y) of prize at each claw machine.

    Returns:
        tokens (int): fewest tokens needed to win the most prizes
    '''
    
    def solve(machine_index: int) -> int:
        tx, ty = prize[machine_index]
        tx += 10000000000000
        ty += 10000000000000

        ax, ay = A[machine_index]
        bx, by = B[machine_index]
        
        @cache
        def dp(a_presses: int, b_presses: int) -> int:
            x, y = a_presses * ax + b_presses * bx, a_presses * ay + b_presses * by
            
            if x == tx and y == ty:
                return 0
            
            if x > tx or y > ty:
                return -1
            
            press_a = dp(a_presses + 1, b_presses)
            press_b = dp(a_presses, b_presses + 1)
            
            if press_a != -1 and press_b != -1:
                return min(3 + press_a, 1 + press_b)
            
            if press_a != -1:
                return 3 + press_a
            
            if press_b != -1:
                return 1 + press_b
            
            return -1
                
        return dp(0, 0)
    
    tot = 0
    for i in range(len(prize)):
        t = solve(i)
        
        if t != -1:
            # print(f'machine #{i + 1}', t)
            tot += t
        
    return tot


if __name__ == '__main__':
    A, B, prize = [], [], []
    
    sample_data = [
        'Button A: X+94, Y+34',
        'Button B: X+22, Y+67',
        'Prize: X=8400, Y=5400',
        '',
        'Button A: X+26, Y+66',
        'Button B: X+67, Y+21',
        'Prize: X=12748, Y=12176',
        '',
        'Button A: X+17, Y+86',
        'Button B: X+84, Y+37',
        'Prize: X=7870, Y=6450',
        '',
        'Button A: X+69, Y+23',
        'Button B: X+27, Y+71',
        'Prize: X=18641, Y=10279'
    ]

    # data = []

    # with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
    #     for line in file.readlines():
    #         data.append(line.strip())

    # Preprocess data
    regexp = r'\d+'
    
    f = lambda x: [int(val) for val in re.findall(regexp, x)]
    
    for i in range(0, len(sample_data), 4):
        A.append(f(sample_data[i]))
        B.append(f(sample_data[i + 1]))
        prize.append(f(sample_data[i + 2]))
    
    # print('---- Part 1 ----')
    # print('result = ', part1(A, B, prize))


    print('---- Part 2 ----')
    print('result = ', part2(A, B, prize))