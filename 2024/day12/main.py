'''
--- Day 12: Garden Groups ---
Why not search for the Chief Historian near the gardener and his massive farm? There's plenty of food, so The Historians grab something to eat while they search.

You're about to settle near a complex arrangement of garden plots when some Elves ask if you can lend a hand. They'd like to set up fences around each region of garden plots, but they can't figure out how much fence they need to order or how much it will cost. They hand you a map (your puzzle input) of the garden plots.

Each garden plot grows only a single type of plant and is indicated by a single letter on your map. When multiple garden plots are growing the same type of plant and are touching (horizontally or vertically), they form a region. For example:

AAAA
BBCD
BBCC
EEEC
This 4x4 arrangement includes garden plots growing five different types of plants (labeled A, B, C, D, and E), each grouped into their own region.

In order to accurately calculate the cost of the fence around a single region, you need to know that region's area and perimeter.

The area of a region is simply the number of garden plots the region contains. The above map's type A, B, and C plants are each in a region of area 4. The type E plants are in a region of area 3; the type D plants are in a region of area 1.

Each garden plot is a square and so has four sides. The perimeter of a region is the number of sides of garden plots in the region that do not touch another garden plot in the same region. The type A and C plants are each in a region with perimeter 10. The type B and E plants are each in a region with perimeter 8. The lone D plot forms its own region with perimeter 4.

Visually indicating the sides of plots in each region that contribute to the perimeter using - and |, the above map's regions' perimeters are measured as follows:

+-+-+-+-+
|A A A A|
+-+-+-+-+     +-+
              |D|
+-+-+   +-+   +-+
|B B|   |C|
+   +   + +-+
|B B|   |C C|
+-+-+   +-+ +
          |C|
+-+-+-+   +-+
|E E E|
+-+-+-+
Plants of the same type can appear in multiple separate regions, and regions can even appear within other regions. For example:

OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
The above map contains five regions, one containing all of the O garden plots, and the other four each containing a single X plot.

The four X regions each have area 1 and perimeter 4. The region containing 21 type O plants is more complicated; in addition to its outer edge contributing a perimeter of 20, its boundary with each X region contributes an additional 4 to its perimeter, for a total perimeter of 36.

Due to "modern" business practices, the price of fence required for a region is found by multiplying that region's area by its perimeter. The total price of fencing all regions on a map is found by adding together the price of fence for every region on the map.

In the first example, region A has price 4 * 10 = 40, region B has price 4 * 8 = 32, region C has price 4 * 10 = 40, region D has price 1 * 4 = 4, and region E has price 3 * 8 = 24. So, the total price for the first example is 140.

In the second example, the region with all of the O plants has price 21 * 36 = 756, and each of the four smaller X regions has price 1 * 4 = 4, for a total price of 772 (756 + 4 + 4 + 4 + 4).

Here's a larger example:

RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
It contains:

A region of R plants with price 12 * 18 = 216.
A region of I plants with price 4 * 8 = 32.
A region of C plants with price 14 * 28 = 392.
A region of F plants with price 10 * 18 = 180.
A region of V plants with price 13 * 20 = 260.
A region of J plants with price 11 * 20 = 220.
A region of C plants with price 1 * 4 = 4.
A region of E plants with price 13 * 18 = 234.
A region of I plants with price 14 * 22 = 308.
A region of M plants with price 5 * 12 = 60.
A region of S plants with price 3 * 8 = 24.
So, it has a total price of 1930.

What is the total price of fencing all regions on your map?



--- Part Two ---
Fortunately, the Elves are trying to order so much fence that they qualify for a bulk discount!

Under the bulk discount, instead of using the perimeter to calculate the price, you need to use the number of sides each region has. Each straight section of fence counts as a side, regardless of how long it is.

Consider this example again:

AAAA
BBCD
BBCC
EEEC
The region containing type A plants has 4 sides, as does each of the regions containing plants of type B, D, and E. However, the more complex region containing the plants of type C has 8 sides!

Using the new method of calculating the per-region price by multiplying the region's area by its number of sides, regions A through E have prices 16, 16, 32, 4, and 12, respectively, for a total price of 80.

The second example above (full of type X and O plants) would have a total price of 436.

Here's a map that includes an E-shaped region full of type E plants:

EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
The E-shaped region has an area of 17 and 12 sides for a price of 204. Including the two regions full of type X plants, this map has a total price of 236.

This map has a total price of 368:

AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
It includes two regions full of type B plants (each with 4 sides) and a single region full of type A plants (with 4 sides on the outside and 8 more sides on the inside, a total of 12 sides). Be especially careful when counting the fence around regions like the one full of type A plants; in particular, each section of fence has an in-side and an out-side, so the fence does not connect across the middle of the region (where the two B regions touch diagonally). (The Elves would have used the Möbius Fencing Company instead, but their contract terms were too one-sided.)

The larger example from before now has the following updated prices:

A region of R plants with price 12 * 10 = 120.
A region of I plants with price 4 * 4 = 16.
A region of C plants with price 14 * 22 = 308.
A region of F plants with price 10 * 12 = 120.
A region of V plants with price 13 * 10 = 130.
A region of J plants with price 11 * 12 = 132.
A region of C plants with price 1 * 4 = 4.
A region of E plants with price 13 * 8 = 104.
A region of I plants with price 14 * 16 = 224.
A region of M plants with price 5 * 6 = 30.
A region of S plants with price 3 * 6 = 18.
Adding these together produces its new total price of 1206.

What is the new total price of fencing all regions on your map?

'''

import os


def part1(grid: list[str]) -> int:
    '''
    Returns total cost of fencing the regions of the same plant.
    A region is formed by group the adjacent plots of the same plant
    in the 4 directional cells together.
    Cost of fencing each region = regions' area * regions' perimeter.
    Area of a region is number of plots in it.
    Perimeter of a region is the outter sides of the cells that cover the region.
    
    Parameters:
        grid (list[str]): map of plants represented by uppercase letters, each letter represents a plant type
        
    Returns:
        int
    '''
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # DFS
    def dfs(r: int, c: int, plant_type: str) -> tuple[int, int]: # (area, perimeter)
        area, perimeter = 1, 4
        visited[r][c] = True
        
        for dx, dy in delta:
            x, y = r + dx, c + dy
            
            if 0 <= x < m and 0 <= y < n and grid[x][y] == plant_type:
                perimeter -= 1 # subtract 1 side that shared with the another plot
                
                if not visited[x][y]:
                    next_area, next_perimeter = dfs(x, y, plant_type)
                
                    area += next_area
                    perimeter += next_perimeter
                
        return (area, perimeter)
    
    tot = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            
            area, perimeter = dfs(i, j, grid[i][j])
            tot += area * perimeter
            
    return tot


def part2(grid: list[str]) -> int:
    '''
    Calculates the total price of fencing all the regions.
    One thing different now is the price of fencing a region is it's area * number of sides that region has.
    A side is a straight line that surrounds that region. e.g.
        |   or __ or |
        |
    
    Parameters:
        grid (list[str]): map of plants represented by uppercase letters, each letter represents a plant type
        
    Returns:
        int
    '''
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Store all plots that lie in the border of region, then calculate the sides
    def dfs(r: int, c: int, plant_type: str, border: list[tuple[int, int]]) -> tuple[int, int]:
        '''
        Returns the area and sides of a region while also stores all the plots in that region's border
        
        Parameters:
            r (int): current row
            c (int): current column
            plant_type (str): Region's plant type
            border (list[tuple[int, int]]): list of cells that lie in region border

        Returns:
            output (tuple[int, int]): area and sides of region
        '''
        
        # cell lie in the border of map or is adjacent to a cell of different plant type
        if r == 0 or grid[r - 1][c] != plant_type or \
            r == m - 1 or grid[r + 1][c] != plant_type or \
            c == 0 or grid[r][c - 1] != plant_type or \
            c == n - 1 or grid[r][c + 1] != plant_type:
            border.append((r, c))
            
        visited[r][c] = True
        
        area, sides = 1, 4
        for dx, dy in delta:
            if 0 <= (x := r + dx) < m and \
                0 <= (y := c + dy) < n and \
                grid[x][y] == plant_type:
                    
                sides -= 1
                
                if not visited[x][y]:
                    next_area, next_sides = dfs(x, y, plant_type, border)
                    area += next_area
                    sides += next_sides
                
        return (area, sides)
    
    tot = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            
            border = []
            area, sides = dfs(i, j, grid[i][j], border)
            border_set = set(border)
            
            for x, y in border:
                # on the same top horizontal side
                if (x == 0 or grid[x - 1][y] != grid[i][j]) and \
                    (x, y + 1) in border_set and \
                    (x == 0 or grid[x - 1][y + 1] != grid[i][j]):
                    sides -= 1
                    
                # on the same bottom horizontal side
                if (x == m - 1 or grid[x + 1][y] != grid[i][j]) and \
                    (x, y + 1) in border_set and \
                    (x == m - 1 or grid[x + 1][y + 1] != grid[i][j]):
                    sides -= 1
                    
                # on the same left vertical side
                if (y == 0 or grid[x][y - 1] != grid[i][j]) and \
                    (x + 1, y) in border_set and \
                    (y == 0 or grid[x + 1][y - 1] != grid[i][j]):
                    sides -= 1
                    
                # on the same right vertical side
                if (y == n - 1 or grid[x][y + 1] != grid[i][j]) and \
                    (x + 1, y) in border_set and \
                    (y == n - 1 or grid[x + 1][y + 1] != grid[i][j]):
                    sides -= 1
            
            # print(i, j, grid[i][j], f'area={area}, sides={sides}')
                    
            tot += area * sides
            
    return tot


if __name__ == '__main__':
    sample_data1 = [
        'AAAA',
        'BBCD',
        'BBCC',
        'EEEC'
    ] # Expected: part1 = 140, part2 = 80
    
    sample_data2 = [
        'OOOOO',
        'OXOXO',
        'OOOOO',
        'OXOXO',
        'OOOOO'
    ] # Expected: part1 = 772, part2 = 436
    
    sample_data3 = [
        'RRRRIICCFF',
        'RRRRIICCCF',
        'VVRRRCCFFF',
        'VVRCCCJFFF',
        'VVVVCJJCFE',
        'VVIVCCJJEE',
        'VVIIICJJEE',
        'MIIIIIJJEE',
        'MIIISIJEEE',
        'MMMISSJEEE'
    ] # Expected: part1 = 1930, part2 = 1206
    
    sample_data4 = [
        'EEEEE',
        'EXXXX',
        'EEEEE',
        'EXXXX',
        'EEEEE'
    ] # Expected: part2 = 236
    
    sample_data5 = [
        'AAAAAA',
        'AAABBA',
        'AAABBA',
        'ABBAAA',
        'ABBAAA',
        'AAAAAA'
    ] # Expected: part2 = 368
    
    data = []

    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())

    # Preprocess data

    # print('---- Part 1 ----')
    # print('result = ', part1(sample_data1))
    # print('result = ', part1(sample_data2))
    # print('result = ', part1(sample_data3))
    # print('result = ', part1(data))


    print('---- Part 2 ----')
    print('result = ', part2(data))
