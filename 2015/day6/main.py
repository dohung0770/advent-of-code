'''
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?




--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.

'''

def part1(m: int, n: int, instructions: list[tuple[str, int, int, int, int]]) -> int:
    '''
    Count number of lights that are lit in the xy coordinates (m*n),
    after following the instructions [on|off|toggle, top, left, bottom, right].

    Parameters:
        m (int): height of grid
        n (int): width of grid
        instructions (list[tuple[str, int, int, int, int]]): Given list of instructions.
    
    Returns:
        int: number of lights that are lit.
    '''
    
    # 300 * 1000 * 1000 ~ 3*10^8
    
    # Brute force
    mat = [[0] * n for _ in range(m)]
    
    for ins, x1, y1, x2, y2 in instructions:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if ins == 'on':
                    mat[x][y] = 1
                elif ins == 'off':
                    mat[x][y] = 0
                else: # 'toggle'
                    mat[x][y] ^= 1
                    
    tot = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                tot += 1
                
    return tot


def part2(m: int, n: int, instructions: list[tuple[str, int, int, int, int]]) -> int:
    '''
    Count total brightness of all the lights after following the instructions.

    Parameters:
        m (int): height of grid
        n (int): width of grid
        instructions (list[tuple[str, int, int, int, int]]): = [on|off|toggle, top, left, bottom, right]
            - on = increase the brightness of the light by 1
            - off = decrease the brightness of the light by 1
            - toggle = increase the brightness of the light by 2
        
    Returns:
        int: total brightness
    '''
    
    mat = [[0] * n for _ in range(m)]
    
    for action, x1, y1, x2, y2 in instructions:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == 'on':
                    mat[x][y] += 1
                elif action == 'toggle':
                    mat[x][y] += 2
                elif mat[x][y] > 0: # off
                    mat[x][y] -= 1
                    
    tot = 0
    for i in range(m):
        for j in range(n):
            tot += mat[i][j]
            
    return tot


import os

if __name__ == '__main__':
    data = []
    
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            # _, action, top_left, __, bottom_right = line.strip().split(' ')
            p = line.strip().split(' ')
            if p[0] == 'toggle':
                data.append((p[0], *[int(val) for val in p[1].split(',')], *[int(val) for val in p[3].split(',')]))
            else:
                data.append((p[1], *[int(val) for val in p[2].split(',')], *[int(val) for val in p[4].split(',')]))
            
    m, n = 1000, 1000

    # print('part 1', part1(m, n, data))
    print('part 2', part2(m, n, data))
