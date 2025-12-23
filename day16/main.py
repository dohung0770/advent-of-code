'''
--- Day 16: Reindeer Maze ---
It's time again for the Reindeer Olympics! This year, the big event is the Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a total of 36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
In this maze, the best paths cost 11048 points; following one such path would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could possibly get?



--- Part Two ---
Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is whether the tile is on one of the best paths through the maze. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of any best path through the maze, including the S and E tiles.

In the first example, there are 45 tiles (marked O) that are part of at least one of the various best paths through the maze:

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############
In the second example, there are 64 tiles that are part of at least one of the best paths:

#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################
Analyze your map further. How many tiles are part of at least one of the best paths through the maze?

'''

import heapq

def part1(grid: list[str]) -> int:
    '''
    Given a map of the reindeer's olympics with '#' represents walls.
    The reindeer is current at 'S' and facing East.
    The reindeer can move forward to an empty cell (.) that earn 1 point, or turn 90 degree clockwise
    or counterclockwise, and earn 1000 points.
    Returns the minimum possible points to each the destination 'E'.
    
    Parameters:
        grid (list[str]): Given map of the Reindeer Olympics
    
    Returns:
        out (int): the least possible points
    '''
    
    m, n = len(grid), len(grid[0])
    x_start, y_start = None, None
    x_target, y_target = None, None
    
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
    else:
        raise ValueError("No starting point ot target found in the given map.")
    
    # Dijkstra
    # dx, dy = 0, 1 # Initially facing East
    heap = [(0, x_start, y_start, 0, 1)] # (points, current x, current y, dx, dy)
    visited = set()
    
    while heap:
        points, x_curr, y_curr, dx, dy = heapq.heappop(heap)
        
        if x_curr == x_target and y_curr == y_target:
            return points
        
        if (x_curr, y_curr, dx, dy) in visited:
            continue
        
        visited.add((x_curr, y_curr, dx, dy))
        
        nx, ny = x_curr + dx, y_curr + dy
        
        if 0 <= nx < m and \
            0 <= ny < n and \
            grid[nx][ny] != '#' and \
            (nx, ny, dx, dy) not in visited:
            
            heapq.heappush(heap, (points + 1, nx, ny, dx, dy))
            
        # Try to turn 90degree clockwise or counterclockwise
        # current      clockwise   counterclockwise
        # -1, 0 (N) -> 0, 1 (E)    0, -1 (W)
        # 0, 1 (E)  -> 1, 0 (S)    -1, 0 (N)
        # 1, 0 (S)  -> 0, -1 (W)   0, 1 (E)
        # 0, -1 (W) -> -1, 0 (N)   1, 0 (S)
        
        ndx, ndy = (dy, dx) if dx == 0 else (dy, -dx)
        cndx, cndy = (-dy, dx) if dx == 0 else (dy, dx)
        
        if (x_curr, y_curr, ndx, ndy) not in visited:
            heapq.heappush(heap, (points + 1000, x_curr, y_curr, ndx, ndy))
        
        if (x_curr, y_curr, cndx, cndy) not in visited:
            heapq.heappush(heap, (points + 1000, x_curr, y_curr, cndx, cndy))
            
    return -1


def part2(grid: list[str]) -> int:
    '''
    Given a map of the reindeer's olympics with '#' represents walls.
    The reindeer is current at 'S' and facing East.
    The reindeer can move forward to an empty cell (.) that earn 1 point, or turn 90 degree clockwise
    or counterclockwise, and earn 1000 points.
    Returns the number of tiles that lie on the path eaching destination 'E' with the minimum possible points.
    
    Parameters:
        grid (list[str]): Given map of the Reindeer Olympics
    
    Returns:
        out (int): the number of nodes on the shortest path
    '''
    
    m, n = len(grid), len(grid[0])
    x_start, y_start = None, None
    x_target, y_target = None, None
    
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
    else:
        raise ValueError("No starting point ot target found in the given map.")
    
    # Dijkstra
    # dx, dy = 0, 1 # Initially facing East
    heap = [(0, x_start, y_start, 0, 1)] # (points, current x, current y, dx, dy)
    visited = set()
    
    best = None # the minimum possible points
    
    while heap:
        points, x_curr, y_curr, dx, dy = heapq.heappop(heap)
        
        if x_curr == x_target and y_curr == y_target:
            best = points
            break
        
        if (x_curr, y_curr, dx, dy) in visited:
            continue
        
        visited.add((x_curr, y_curr, dx, dy))
        
        nx, ny = x_curr + dx, y_curr + dy
        
        if 0 <= nx < m and \
            0 <= ny < n and \
            grid[nx][ny] != '#' and \
            (nx, ny, dx, dy) not in visited:
            
            heapq.heappush(heap, (points + 1, nx, ny, dx, dy))
            
        # Try to turn 90degree clockwise or counterclockwise
        # current      clockwise   counterclockwise
        # -1, 0 (N) -> 0, 1 (E)    0, -1 (W)
        # 0, 1 (E)  -> 1, 0 (S)    -1, 0 (N)
        # 1, 0 (S)  -> 0, -1 (W)   0, 1 (E)
        # 0, -1 (W) -> -1, 0 (N)   1, 0 (S)
        
        ndx, ndy = (dy, dx) if dx == 0 else (dy, -dx)
        cndx, cndy = (-dy, dx) if dx == 0 else (dy, dx)
        
        if (x_curr, y_curr, ndx, ndy) not in visited:
            heapq.heappush(heap, (points + 1000, x_curr, y_curr, ndx, ndy))
        
        if (x_curr, y_curr, cndx, cndy) not in visited:
            heapq.heappush(heap, (points + 1000, x_curr, y_curr, cndx, cndy))
            
    if best is None:
        return -1 # No path found
    
    print('best = ', best)
    
    reachable = [[False] * n for _ in range(m)]
    vis = set()

    def dfs(x: int, y: int, dx: int, dy: int, pts: int) -> bool:
        if x == x_target and y == y_target:
            reachable[x][y] = True
            return True
        
        if reachable[x][y] is True:
            return reachable[x][y]
        
        if pts > best or (x, y, dx, dy) in vis:
            return False
        
        vis.add((x, y, dx, dy))
        
        if 0 <= (nx := x + dx) < m and \
            0 <= (ny := y + dy) < n and \
            grid[nx][ny] != '#' and \
            pts + 1 <= best:
                
            if dfs(nx, ny, dx, dy, pts + 1) is True:
                reachable[x][y] = True
            
        ndx, ndy = (dy, dx) if dx == 0 else (dy, -dx)
        cndx, cndy = (-dy, dx) if dx == 0 else (dy, dx)
        
        if dfs(x, y, ndx, ndy, pts + 1000) is True:
            reachable[x][y] = True
    
        if dfs(x, y, cndx, cndy, pts + 1000) is True:
            reachable[x][y] = True
                
        vis.remove((x, y, dx, dy))
        return reachable[x][y]
    
    dfs(x_start, y_start, dx=0, dy=1, pts=0)
    
    # logging
    g = [list(line) for line in grid]
    
    tot = 0
    for i in range(m):
        for j in range(n):
            if reachable[i][j] is True:
                g[i][j] = 'O'
                tot += 1
                
    for line in g:
        print(''.join(line))
                
    return tot


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    # print('---- Part 1 ----')
    # print('result = ', part1(data))
    
    print('---- Part 2 ----')
    print('result = ', part1(data))
  