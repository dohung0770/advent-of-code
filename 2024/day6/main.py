'''
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?



--- Part Two ---
While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:


....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?

'''

def part1(grid: list[list[str]]) -> int:
    '''
    Counts number of cells the Guard will visit, including that Guard's initial position (^)
    before she moves out of the map
    
    Parameters:
        grid (list[str]): A map filled with obstacles (#) or empty spaces (.)
        
    Returns:
        int
    '''
    
    m, n = len(grid), len(grid[0])
    start_x, start_y = None, None
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '^':
                start_x, start_y = i, j
                break
            
        if start_x is not None:
            break
        
    if start_x is None:
        return 0
        
    visited = set()
    x, y = start_x, start_y
    dx, dy = -1, 0
    
    while 0 <= x < m and 0 <= y < n and (x, y, dx, dy) not in visited:
        # print(x, y, dx, dy)
        visited.add((x, y, dx, dy))
        grid[x][y] = 'X'
        
        if 0 <= (i := x + dx) < m and 0 <= (j := y + dy) < n and grid[i][j] == '#':
            # (-1, 0) -> (0, 1)
            # (0, 1) -> (1, 0)
            # (1, 0) -> (0, -1)
            # (0, -1) -> (-1, 0)
            dx, dy = dy if dx == 0 else 0, -dx if dy == 0 else 0
            
        x += dx
        y += dy
    
    tot = 0
    for line in grid:
        for char in line:
            if char == 'X':
                tot += 1

    return tot


def part2(grid: list[list[str]]) -> int:
    '''
    Counts how many ways to place an obstacles in some cells, such that the Guard will get stuck in a loop after that
    
    Parameters:
        grid (list[str]): A map filled with obstacles (#) or empty spaces (.)
        
    Returns:
        int
    '''

    # . . # . . . . .
    # . . + ----+ # .
    # . . | . . | . .
    # . . | . . | . .
    # . # + --- + . .
    # . . . . . # . .
    
    m, n = len(grid), len(grid[0])
    start_x, start_y = None, None
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '^':
                start_x, start_y = i, j
                break
            
        if start_x is not None:
            break
        
    if start_x is None:
        return 0
        
    visited = set()
    x, y = start_x, start_y
    dx, dy = -1, 0
    tot = 0
    
    while 0 <= (i := x + dx) < m and 0 <= (j := y + dy) < n:
        visited.add((x, y, dx, dy))
        
        if grid[i][j] == '#':
            # (-1, 0) -> (0, 1)
            # (0, 1) -> (1, 0)
            # (1, 0) -> (0, -1)
            # (0, -1) -> (-1, 0)
            dx, dy = dy if dx == 0 else 0, -dx if dy == 0 else 0
            visited.add((i, j, dx, dy))
        
        else:
            # try to place an obstacle at [i, j] to create an infinite loop
            ddx, ddy = dy if dx == 0 else 0, -dx if dy == 0 else 0
            xx, yy = x, y # simulate moving after obstruction
            grid[i][j] = '#'
            
            while 0 <= xx + ddx < m and \
                0 <= yy + ddy < n and \
                (xx + ddx, yy + ddy, ddx, ddy) not in visited:
                if grid[xx + ddx][yy + ddy] != '#':
                    ddx, ddy = ddy if ddx == 0 else 0, -ddx if ddy == 0 else 0
                    
                xx += ddx
                yy += ddy
                visited.add((xx, yy, ddx, ddy))
                # print(f'simulately moving to [{xx},{yy}]')

            if (xx + ddx, yy + ddy, ddx, ddy) in visited:
                print(f'place obstacle at [{i}, {j}]')
                tot += 1
                
            grid[i][j] = '.'

        x += dx
        y += dy
        
    # place obstacle at [6, 3]
    # place obstacle at [7, 6]
    # place obstacle at [8, 1]
    # place obstacle at [7, 7]
    # place obstacle at [9, 7]
    # place obstacle at [8, 3]
    
    return tot


import os

if __name__ == '__main__':
    # sample_data = [
    #     '....#.....',
    #     '.........#',
    #     '..........',
    #     '..#.......',
    #     '.......#..',
    #     '..........',
    #     '.#..^.....',
    #     '........#.',
    #     '#.........',
    #     '......#...'
    # ]
    
    # sample_data = [
    #     '..#...',
    #     '.....#',
    #     '.#^...',
    #     '......'
    # ]
    
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    # print('---- Part 1 ----')
    # print('total = ', part1([list(line) for line in sample_data]))
    # print('total = ', part1([list(line) for line in data]))
    
    print('---- Part 2 ----')
    # print('total = ', part2([list(line) for line in sample_data]))
    print('total = ', part2([list(line) for line in data]))
    
    
