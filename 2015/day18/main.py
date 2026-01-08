'''
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?




--- Part Two ---
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

'''


def part1(grid: list[str], steps: int) -> int:
    '''
    Animate the lights and count number of lights which are 'on' after 'steps' steps.
    At each state:
    - If a light which is 'on' and it has 2 or 3 neighbors (in 8 adjacent cells) are 'on',
        it stays 'on', otherwise it turns 'off'
    - If a light which is 'off' and it has exactly 3 neighbors are 'on',
        it turns 'on', otherwise stays 'off'

    Parameters:
        grid (list[str]): Given current lights state. '#' = on, '.' = off
        steps (int): number of steps to animate the grid
        
    Returns:
        int: number of lights which are on.
    '''

    m, n = len(grid), len(grid[0])
    for _ in range(steps):
        new_grid = [['.'] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                lights_on = 0
                
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        
                        if 0 <= (x := i + dx) < m and \
                            0 <= (y := j + dy) < n and \
                            grid[x][y] == '#':
                            lights_on += 1
                            
                if grid[i][j] == '#':
                    if lights_on < 2 or lights_on > 3:
                        new_grid[i][j] = '.'
                    else:
                        new_grid[i][j] = '#'
                else:
                    if lights_on == 3:
                        new_grid[i][j] = '#'
                    else:
                        new_grid[i][j] = '.'
                        
        grid = new_grid
                        
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                cnt += 1
                
    return cnt


def part2(grid: list[str], steps: int) -> int:
    '''
    Same as part 1, the rules follow the Conway's Game of life.
    At each state:
    - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies, as if by overpopulation.
    - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    (in this case, live cell = light which is on, dead cell = light which is off).
    But this time, the 4 lights in the corners are always 'on'.

    Parameters:
        grid (list[str]): Given current lights state. '#' = on, '.' = off
        steps (int): number of steps to animate the grid
        
    Returns:
        int: number of lights which are on.
    '''
    
    m, n = len(grid), len(grid[0])
    grid = [list(line) for line in grid]
    grid[0][0] = grid[0][n - 1] = grid[m - 1][0] = grid[m - 1][n - 1] = '#'

    for _ in range(steps):
        new_grid = [['.'] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i in (0, m - 1) and j in (0, n - 1):
                    new_grid[i][j] = '#'
                    continue
                
                lights_on = 0
                
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        
                        if 0 <= (x := i + dx) < m and \
                            0 <= (y := j + dy) < n and \
                            grid[x][y] == '#':
                            lights_on += 1
                            
                if grid[i][j] == '#':
                    if lights_on < 2 or lights_on > 3:
                        new_grid[i][j] = '.'
                    else:
                        new_grid[i][j] = '#'
                else:
                    if lights_on == 3:
                        new_grid[i][j] = '#'
                    else:
                        new_grid[i][j] = '.'
                        
        grid = new_grid
                        
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                cnt += 1
                
    return cnt


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
            
    # print('part 1', part1(data, 100))
    print('part 2', part2(data, 100))
