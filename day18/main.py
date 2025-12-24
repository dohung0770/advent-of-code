'''
--- Day 18: RAM Run ---
You and The Historians look a lot more pixelated than you remember. You're inside a computer at the North Pole!

Just as you're about to check out your surroundings, a program runs up to you. "This region of memory isn't safe! The User misunderstood what a pushdown automaton is and their algorithm is pushing whole bytes down on top of us! Run!"

The algorithm is fast - it's going to cause a byte to fall into your memory space once every nanosecond! Fortunately, you're faster, and by quickly scanning the algorithm, you create a list of which bytes will fall (your puzzle input) in the order they'll land in your memory space.

Your memory space is a two-dimensional grid with coordinates that range from 0 to 70 both horizontally and vertically. However, for the sake of example, suppose you're on a smaller grid with coordinates that range from 0 to 6 and the following list of incoming byte positions:

5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
Each byte position is given as an X,Y coordinate, where X is the distance from the left edge of your memory space and Y is the distance from the top edge of your memory space.

You and The Historians are currently in the top left corner of the memory space (at 0,0) and need to reach the exit in the bottom right corner (at 70,70 in your memory space, but at 6,6 in this example). You'll need to simulate the falling bytes to plan out where it will be safe to run; for now, simulate just the first few bytes falling into your memory space.

As bytes fall into your memory space, they make that coordinate corrupted. Corrupted memory coordinates cannot be entered by you or The Historians, so you'll need to plan your route carefully. You also cannot leave the boundaries of the memory space; your only hope is to reach the exit.

In the above example, if you were to draw the memory space after the first 12 bytes have fallen (using . for safe and # for corrupted), it would look like this:

...#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#....
You can take steps up, down, left, or right. After just 12 bytes have corrupted locations in your memory space, the shortest path from the top left corner to the exit would take 22 steps. Here (marked with O) is one such path:

OO.#OOO
.O#OO#O
.OOO#OO
...#OO#
..#OO#.
.#.O#..
#.#OOOO
Simulate the first kilobyte (1024 bytes) falling onto your memory space. Afterward, what is the minimum number of steps needed to reach the exit?



--- Part Two ---
The Historians aren't as used to moving around in this pixelated universe as you are. You're afraid they're not going to be fast enough to make it to the exit before the path is completely blocked.

To determine how fast everyone needs to go, you need to determine the first byte that will cut off the path to the exit.

In the above example, after the byte at 1,1 falls, there is still a path to the exit:

O..#OOO
O##OO#O
O#OO#OO
OOO#OO#
###OO##
.##O###
#.#OOOO
However, after adding the very next byte (at 6,1), there is no longer a path to the exit:

...#...
.##..##
.#..#..
...#..#
###..##
.##.###
#.#....
So, in this example, the coordinates of the first byte that prevents the exit from being reachable are 6,1.

Simulate more of the bytes that are about to corrupt your memory space. What are the coordinates of the first byte that will prevent the exit from being reachable from your starting position? (Provide the answer as two integers separated by a comma with no other characters.)

'''

import os
from collections import deque


def part1(m: int, n: int, falling_bytes: list[list[int]], t: int = None) -> int:
    '''
    Given a memory space of m*n cells,
    and a list of bytes that are going to fall down at the xy-coordinates in the memory space.
    Returns the shortest path to reach the bottom-right corner, when starting from the top-left corner
    after the first 't = 1024 (1KB)' bytes have fallen.
    
    Parameters:
        m (int): height of the memory space
        n (int): width of the memory space
        falling_bytes (list[list[int]]): xy-coordinates of bytes going to fall into the memory space
        t (int): = 1024 the first bytes
        
    Returns:
        output (int): the shortest path.
    '''

    t = len(falling_bytes) if t is None else t
    
    # BFS
    visited = [[False] * n for _ in range(m)]
    for i in range(t):
        x, y = falling_bytes[i]
        visited[x][y] = True
    
    queue = deque([(0, 0, 0)]) # (moves, x, y)
    visited[0][0] = True
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        moves, x, y = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return moves
        
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] is False:
                visited[nx][ny] = True
                queue.append((moves + 1, nx, ny))
    
    return -1


def part2(m: int, n: int, falling_bytes: list[list[int]]) -> str:
    '''
    Returns the earliest byte coordinate that if that coordinate is corrupted, there is no way to exit the memory space.
    
    Parameters:
        m (int): height of the memory space
        n (int): width of the memory space
        falling_bytes (list[list[int]]): xy-coordinates of bytes going to fall into the memory space
        
    Returns:
        output (str): The coordinate of the earliest byte that blocks the exit entirely (x,y separated by comma).
    '''
    
    # Binary Search
    l, r = 0, len(falling_bytes) - 1
    while l <= r:
        mid = (l + r) // 2
        
        if part1(m, n, falling_bytes, t=mid + 1) == -1:
            r = mid - 1
        else:
            l = mid + 1
            
    return ','.join([str(val) for val in falling_bytes[r + 1]])


if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    m, n = 71, 71

    # print('----- Part 1 -----')
    # print('result = ', part1(m, n, [list(map(int, line.split(','))) for line in data], t=1024))

    print('----- Part 2 -----')
    print('result = ', part2(m, n, [list(map(int, line.split(','))) for line in data]))
