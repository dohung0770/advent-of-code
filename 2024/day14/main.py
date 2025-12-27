'''
--- Day 14: Restroom Redoubt ---
One of The Historians needs to use the bathroom; fortunately, you know there's a bathroom near an unvisited location on their list, and so you're all quickly teleported directly to the lobby of Easter Bunny Headquarters.

Unfortunately, EBHQ seems to have "improved" bathroom security again after your last visit. The area outside the bathroom is swarming with robots!

To get The Historian safely to the bathroom, you'll need a way to predict where the robots will be in the future. Fortunately, they all seem to be moving on the tile floor in predictable straight lines.

You make a list (your puzzle input) of all of the robots' current positions (p) and velocities (v), one robot per line. For example:

p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
Each robot's position is given as p=x,y where x represents the number of tiles the robot is from the left wall and y represents the number of tiles from the top wall (when viewed from above). So, a position of p=0,0 means the robot is all the way in the top-left corner.

Each robot's velocity is given as v=x,y where x and y are given in tiles per second. Positive x means the robot is moving to the right, and positive y means the robot is moving down. So, a velocity of v=1,-2 means that each second, the robot moves 1 tile to the right and 2 tiles up.

The robots outside the actual bathroom are in a space which is 101 tiles wide and 103 tiles tall (when viewed from above). However, in this example, the robots are in a space which is only 11 tiles wide and 7 tiles tall.

The robots are good at navigating over/under each other (due to a combination of springs, extendable legs, and quadcopters), so they can share the same tile and don't interact with each other. Visually, the number of robots on each tile in this example looks like this:

1.12.......
...........
...........
......11.11
1.1........
.........1.
.......1...
These robots have a unique feature for maximum bathroom security: they can teleport. When a robot would run into an edge of the space they're in, they instead teleport to the other side, effectively wrapping around the edges. Here is what robot p=2,4 v=2,-3 does for the first few seconds:

Initial state:
...........
...........
...........
...........
..1........
...........
...........

After 1 second:
...........
....1......
...........
...........
...........
...........
...........

After 2 seconds:
...........
...........
...........
...........
...........
......1....
...........

After 3 seconds:
...........
...........
........1..
...........
...........
...........
...........

After 4 seconds:
...........
...........
...........
...........
...........
...........
..........1

After 5 seconds:
...........
...........
...........
.1.........
...........
...........
...........
The Historian can't wait much longer, so you don't have to simulate the robots for very long. Where will the robots be after 100 seconds?

In the above example, the number of robots on each tile after 100 seconds has elapsed looks like this:

......2..1.
...........
1..........
.11........
.....1.....
...12......
.1....1....
To determine the safest area, count the number of robots in each quadrant after 100 seconds. Robots that are exactly in the middle (horizontally or vertically) don't count as being in any quadrant, so the only relevant robots are:

..... 2..1.
..... .....
1.... .....
           
..... .....
...12 .....
.1... 1....
In this example, the quadrants contain 1, 3, 4, and 1 robot. Multiplying these together gives a total safety factor of 12.

Predict the motion of the robots in your list within a space which is 101 tiles wide and 103 tiles tall. What will the safety factor be after exactly 100 seconds have elapsed?



--- Part Two ---
During the bathroom break, someone notices that these robots seem awfully similar to ones built and used at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to display the Easter egg?

'''

import os

def part1(m: int, n: int, robots: list[list[int]], velocity: list[list[int]], t: int = 100) -> int:
    '''
    In the 2D coornidate system m*n, viewing from the top-left corner as (0, 0).
    Predict the motion of the robots after exactly t=100ms and return the safety factor
    by multiplying the numbers of robots that are at the each quadrant of the area.
    All the robots at the middle (not in any quadrant) can be safely ignored.
    The robots at initially at 'robots', move with velocity of (dx,dy) given by 'velocity' after every 1ms.
    When the robot faces the edge of the area, it teleports to the other side of the area.
    
    Parameters:
        m (int): height of the area (= 103 units)
        n (int): width of the area (= 101 units)
        robots (list[list[int]]): initial positions of the robots
        velocity (list[list[int]]): movements of the robots
        t (int): the time the robots will be moving (= 100ms)
        
    Returns:
        int
    '''
    
    while t > 0:
        t -= 1
        
        for i, (x, y) in enumerate(robots):
            dx, dy = velocity[i]
            
            robots[i] = [
                (x + dx + n) % n,
                (y + dy + m) % m
            ]
            
    M, N = m // 2, n // 2
    quadrants = [0] * 4
    
    for x, y in robots:
        if x == N or y == M:
            continue # ignore all the robots at are in the middle (horizontally or vertically)
        
        # quadrants[2 * (x // N // 2) + (y // M) % 2] += 1
        if x < N and y < M:
            quadrants[0] += 1
        elif x < N:
            quadrants[2] += 1
        elif y < M:
            quadrants[1] += 1
        else:
            quadrants[3] += 1
        
    if max(quadrants) == 0:
        return 0
    
    safety_factor = 1
    for cnt in quadrants:
        if cnt > 0:
            safety_factor *= cnt
        
    return safety_factor
    

    # b = [[0] * n for _ in range(m)]
    # for x, y in robots:
    #     b[x][y] += 1
        
    # for line in b:
    #     print(''.join([str(v) if v > 0 else '.' for v in line]))
    

def part2(m: int, n: int, robots: list[list[int]], velocity: list[list[int]]):
    '''
    Same with part 1, but returns the minimum number of time elapsed to render to shape of a chrismas tree.
    
    Refer to the chrismas-tree.png file.
    
    Parameters:
        m (int): height of the area (= 103 units)
        n (int): width of the area (= 101 units)
        robots (list[list[int]]): initial positions of the robots
        velocity (list[list[int]]): movements of the robots
        
    Returns:
        int
    '''
    t = 0
    while t < 10000:
        t += 1
        
        for i, (x, y) in enumerate(robots):
            dx, dy = velocity[i]
            
            robots[i] = [
                (x + dx + n) % n,
                (y + dy + m) % m
            ]
            
        if t == 7861: # only render the tree at the appropriate timestamp
            b = [[0] * n for _ in range(m)]
            for x, y in robots:
                b[y][x] += 1
                
            print('\n==============================================================================================================================\nt = ', t)
            for line in b:
                print(''.join('*' if v > 0 else ' ' for v in line))
            


if __name__ == '__main__':
    # sample_data = [
    #     'p=0,4 v=3,-3',
    #     'p=6,3 v=-1,-3',
    #     'p=10,3 v=-1,2',
    #     'p=2,0 v=2,-1',
    #     'p=0,0 v=1,3',
    #     'p=3,0 v=-2,-2',
    #     'p=7,6 v=-1,-3',
    #     'p=3,0 v=-1,-2',
    #     'p=9,3 v=2,3',
    #     'p=7,3 v=-1,2',
    #     'p=2,4 v=2,-3',
    #     'p=9,5 v=-3,-3'
    # ]
    
    # sample_data = [
    #     'p=2,4 v=2,-3'
    # ]
    
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    robots = []
    velocity = []
    
    # Preprocess data
    for line in data:
        left, right = line.split(' ')
        robots.append([int(v) for v in left[2:].split(',')])
        velocity.append([int(v) for v in right[2:].split(',')])
        
    m, n = 103, 101
    # m, n = 7, 11
    
    # print('---- Part 1 ----')
    # print('result = ', part1(m, n, robots, velocity, t=100))
    
    # print('---- Part 2 ----')
    print('result = ', part2(m, n, robots, velocity))
