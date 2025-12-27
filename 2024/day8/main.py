'''
--- Day 8: Resonant Collinearity ---
You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

So, for these two antennas with frequency a, they create the two antinodes marked with #:

..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........
Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, but two are off the right side of the map, so instead it adds only two:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........
Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However, antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A creates no antinodes but has a lowercase-a-frequency antinode at its location:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........
The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an antinode overlapping the topmost A-frequency antenna:

......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that contain an antinode within the bounds of the map.

Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?



--- Part Two ---
Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?

'''

from collections import defaultdict

def part1(grid: list[str]) -> int:
    '''
    Counts number of antinodes can place inside grid's bound.
    The two same frequency antennas can have 2 antinodes on the same line with the same distance between the two antennas
    
    Parameters:
        grid (list[str]): Given map of antennas marked with digits, lowercase and uppercase letters
        
    Returns:
        int
    '''
    
    m, n = len(grid), len(grid[0])
    antinodes = set()
    loc = defaultdict(list[tuple[int, int]]) # Store positions of antennas grouped by their frequencies
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                loc[grid[i][j]].append((i, j))
                
    # . X . . . . . . . .
    # . . . . . . . . . .
    # . . . A . . . . . . (2, 3)
    # . . . . . . . . . .           dx, dy = -2, -2
    # . . . . . A . . . . (4, 5)
    # . . . . . . . . . .
    # . . . . . . . X . .
    for pos in loc.values():
        size = len(pos)
        if size == 1:
            continue
        
        for i in range(size - 1):
            x1, y1 = pos[i]
            for j in range(i + 1, size):
                x2, y2 = pos[j]
                dx, dy = x1 - x2, y1 - y2

                if 0 <= (x := x1 + dx) < m and 0 <= (y := y1 + dy) < n:
                    antinodes.add((x, y))
                    
                if 0 <= (x := x2 - dx) < m and 0 <= (y := y2 - dy) < n:
                    antinodes.add((x, y))
                
    return len(antinodes)


def part2(grid: list[str]) -> int:
    '''
    Counts number of antinodes can place inside grid's bound 
    that lie in the same line of any two antennas with the same frequency
    
    The distance between two antinodes or antinodes to antennas should be equal
    
    Parameters:
        grid (list[str]): Given map of antennas marked with digits, lowercase and uppercase letters
        
    Returns:
        int
    '''
    
    m, n = len(grid), len(grid[0])
    antinodes = set()
    loc = defaultdict(list[tuple[int, int]]) # Store positions of antennas grouped by their frequencies
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                loc[grid[i][j]].append((i, j))
                
    # . X . . . . . . . .
    # . . . . . . . . . .
    # . . . A . . . . . . (2, 3)
    # . . . . . . . . . .           dx, dy = -2, -2
    # . . . . . A . . . . (4, 5)
    # . . . . . . . . . .
    # . . . . . . . X . .
    for pos in loc.values():
        size = len(pos)
        if size == 1:
            continue
        
        for i in range(size - 1):
            x1, y1 = pos[i]
            antinodes.add((x1, y1))

            for j in range(i + 1, size):
                x2, y2 = pos[j]
                antinodes.add((x2, y2))
                
                dx, dy = x1 - x2, y1 - y2

                k = 1
                while 0 <= (x := x1 + k * dx) < m and 0 <= (y := y1 + k * dy) < n:
                    antinodes.add((x, y))
                    k += 1
                    
                k = 1
                while 0 <= (x := x2 - k * dx) < m and 0 <= (y := y2 - k * dy) < n:
                    antinodes.add((x, y))
                    k += 1
    
    # tmp = [['#' if (i, j) in antinodes and grid[i][j] == '.' else grid[i][j] for j in range(n)] for i in range(m)]
    # for line in tmp:
    #     print(''.join(line))
            
    return len(antinodes)


import os

if __name__ == '__main__':
    # sample_data = [
    #     '............',
    #     '........0...',
    #     '.....0......',
    #     '.......0....',
    #     '....0.......',
    #     '......A.....',
    #     '............',
    #     '............',
    #     '........A...',
    #     '.........A..',
    #     '............',
    #     '............'
    # ]
    
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    
    # print('---- Part 1 ----')
    # # print('result = ', part1(sample_data))
    # print('result = ', part1(data))
    
    
    print('---- Part 2 ----')
    # print('result = ', part2(sample_data))
    print('result = ', part2(data))
