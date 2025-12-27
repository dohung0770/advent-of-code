'''
--- Day 20: Race Condition ---
The Historians are quite pixelated again. This time, a massive, black building looms over you - you're right outside the CPU!

While The Historians get to work, a nearby program sees that you're idle and challenges you to a race. Apparently, you've arrived just in time for the frequently-held race condition festival!

The race takes place on a particularly long and twisting code path; programs compete to see who can finish in the fewest picoseconds. The winner even gets their very own mutex!

They hand you a map of the racetrack (your puzzle input). For example:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
The map consists of track (.) - including the start (S) and end (E) positions (both of which also count as track) - and walls (#).

When a program runs through the racetrack, it starts at the start position. Then, it is allowed to move up, down, left, or right; each such move takes 1 picosecond. The goal is to reach the end position as quickly as possible. In this example racetrack, the fastest time is 84 picoseconds.

Because there is only a single path from the start to the end and the programs all go the same speed, the races used to be pretty boring. To make things more interesting, they introduced a new rule to the races: programs are allowed to cheat.

The rules for cheating are very strict. Exactly once during a race, a program may disable collision for up to 2 picoseconds. This allows the program to pass through walls as if they were regular track. At the end of the cheat, the program must be back on normal track again; otherwise, it will receive a segmentation fault and get disqualified.

So, a program could complete the course in 72 picoseconds (saving 12 picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...12....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Or, a program could complete the course in 64 picoseconds (saving 20 picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...12..#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
This cheat saves 38 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.####1##.###
#...###.2.#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
This cheat saves 64 picoseconds and takes the program directly to the end:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..21...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Each cheat has a distinct start position (the position where the cheat is activated, just before the first move that is allowed to go through walls) and end position; cheats are uniquely identified by their start position and end position.

In this example, the total number of cheats (grouped by the amount of time they save) are as follows:

There are 14 cheats that save 2 picoseconds.
There are 14 cheats that save 4 picoseconds.
There are 2 cheats that save 6 picoseconds.
There are 4 cheats that save 8 picoseconds.
There are 2 cheats that save 10 picoseconds.
There are 3 cheats that save 12 picoseconds.
There is one cheat that saves 20 picoseconds.
There is one cheat that saves 36 picoseconds.
There is one cheat that saves 38 picoseconds.
There is one cheat that saves 40 picoseconds.
There is one cheat that saves 64 picoseconds.
You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible, you'll need a list of the best cheats. How many cheats would save you at least 100 picoseconds?

'''

import os
from collections import deque


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def part1(grid: list[str], threshold: int) -> int:
    '''
    Returns number of distinct cheat-applied paths that save you at least 'threshold' picoseconds
    compared to taking the normal shortest path to each 'E'.
    Each path can have 2 picoseconds disabling collision (= passing through walls) once.

    Parameters:
        grid (list[str]): Given racing map -
            'S' = starting point, 'E' = destination, '.' = race track, '#' = walls.
        threshold (int): Expected picoseconds saved using cheat
    
    Returns:
        output (int):
    '''
    
    m, n = len(grid), len(grid[0])
    x_start, y_start, x_target, y_target = None, None, None, None
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                x_start, y_start = i, j
            elif grid[i][j] == 'E':
                x_target, y_target = i, j
                
            if x_start is not None and x_target is not None:
                break
                
        if x_start is not None and x_target is not None:
            break
        
    if x_start is None:
        raise ValueError("No starting point found in given map")
    
    if x_target is None:
        raise ValueError("No destination point found in given map")

    
    # finding the shortest path
    queue = deque([(x_start, y_start, 0)]) # (x, y, cost)
    visited = [[False] * n for _ in range(m)]
    visited[x_start][y_start] = True
    
    actual = None
    
    while queue:
        x, y, cost = queue.popleft()
        if x == x_target and y == y_target:
            actual = cost
            break
        
        for dx, dy in delta:
            if 0 <= (nx := x + dx) < m and \
                0 <= (ny := y + dy) < n and \
                grid[nx][ny] != '#' and \
                visited[nx][ny] is False:
                visited[nx][ny] = True
                queue.append((nx, ny, cost + 1))
    
    print(f'S = ({x_start},{y_start}), E = ({x_target},{y_target})')
    print('actual = ', actual)

    # finding alternative paths with cheats
    queue = deque([(x_start, y_start, 0, 0)]) # (x, y, moves, t = cheat time used)
    visited = set()
    visited.add((x_start, y_start, 0))
    
    tot = 0
    while queue:
        x, y, cost, t = queue.popleft()
        # print(x, y, cost, t)
        
        if x == x_target and y == y_target:
            # visited.remove((x, y, t))
            print(cost)
            
            if cost <= actual - threshold:
               tot += 1
               
            # if t == 0:
            #     break
            
            continue
            
        if cost + 1 > actual - threshold:
            continue

        for dx, dy in delta:
            if 0 <= (nx := x + dx) < m and \
                0 <= (ny := y + dy) < n:
                    
                if t < 2 and (state := (nx, ny, t + 1)) not in visited:
                    visited.add(state)
                    queue.append((nx, ny, cost + 1, t + 1)) # go to the next cell, even it's a wall
                    
                    if t > 0:
                        continue
                    
                if (t == 0 or t == 2) and grid[nx][ny] != '#' and (state := (nx, ny, t)) not in visited:
                    visited.add(state)
                    queue.append((nx, ny, cost + 1, t))

    return tot
    

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt') ,'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    print('---- Part 1 ----')
    print('result = ', part1(data, 100))
