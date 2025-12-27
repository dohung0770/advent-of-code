'''
--- Day 15: Warehouse Woes ---
You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 4 = 104.

#######
#...O..
#......
The lanternfish would like to know the sum of all boxes' GPS coordinates after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of all boxes' GPS coordinates?



--- Part Two ---
The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is twice as wide! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
After appropriately resizing this map, the robot would push around these boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of 1 from the top edge of the map and 5 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........
In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?

'''

import os
    
def get_velocity(ins: str) -> tuple[int, int]:
    if ins == '^':
        return (-1, 0)
    if ins == 'v':
        return (1, 0)
    if ins == '<':
        return (0, -1)
    return (0, 1)

def part1(grid: list[str], moves: str) -> int:
    '''
    Returns sum of all boxes's GPS coordinates (= 100 * distance to top edge + distance to left edge)
    after the robot finishes moving the boxes.
    
    Parameters:
        grid (list[str]): Given initial state, the robot is at @, boxes are O, # are the warehouse borders.
        moves (str): The movements of the robot up (^), down (v), left (<), and right (>).
        
    Returns:
        int
    '''
    x_robot, y_robot = None, None
    
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                x_robot, y_robot = i, j
                break
        
        if x_robot is not None:
            break
    else:
        raise ValueError("No position of the robot found in given grid.")
    
    g = [list(line) for line in grid]
    
    for ins in moves:
        dx, dy = get_velocity(ins)
        x_next, y_next = x_robot + dx, y_robot + dy
        
        while 0 <= x_next < m and \
            0 <= y_next < n and \
            g[x_next][y_next] == 'O':
            x_next += dx
            y_next += dy
            
        # print(x_robot, y_robot, x_next, y_next)
            
        if x_next < 0 or x_next >= m or y_next < 0 or y_next >= n or g[x_next][y_next] == '#':
            # out of bound or can't push forward
            continue
        
        i, j = x_next, y_next
        while i - dx != x_robot or j - dy != y_robot:
            # Pushing boxes forward or moving forward
            g[i][j] = g[i - dx][j - dy]
            i -= dx
            j -= dy
            
        g[x_robot][y_robot] = '.'
        x_robot += dx
        y_robot += dy
        
    for i, line in enumerate(g):
        print(''.join('@' if i == x_robot and j == y_robot else line[j] for j in range(n)))
    
    tot = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 'O' and (i != x_robot or j != y_robot):
                tot += 100 * i + j

    return tot


def part2(grid: list[str], moves: str) -> int:
    '''
    Same with part 1, except everything (except the robot) is twice in width.
    
    Parameters:
        grid (list[str]): Given initial state, the robot is at @, boxes are O, # are the warehouse borders.
        moves (str): The movements of the robot up (^), down (v), left (<), and right (>).
        
    Returns:
        int
    '''
    
    def extend(cell: str) -> str:
        if cell == '#':
            return '##'
        if cell == 'O':
            return '[]'
        if cell == '.':
            return '..'

        return '@.'
    
    g = [list(''.join([extend(char) for char in line])) for line in grid]
    m, n = len(g), len(g[0])
    
    x_robot, y_robot = None, None
    for i in range(m):
        for j in range(n):
            if g[i][j] == '@':
                x_robot, y_robot = i, j
                break
        
        if x_robot is not None:
            break
    else:
        raise ValueError("No position of the robot found in grid.")
        
    for i, line in enumerate(g):
        print(''.join('@' if i == x_robot and j == y_robot else line[j] for j in range(n)))

    
    def push_up_down(dx: int, dy: int) -> bool:
        nx = x_robot + dx
        ranges = [(y_robot, y_robot)] # impact range
        
        can_push = True
        while 0 <= nx < m:
            push_left, push_right = ranges[-1]
            next_left, next_right = push_left, push_right
            has_boxes_front = False
            
            for j in range(push_left, push_right + 1):
                if g[nx][j] == '#':
                    # can't push forward
                    can_push = False
                    break
                
                if g[nx][j] == '[':
                    has_boxes_front = True
                    next_right = max(
                        next_right,
                        j + 1
                    )
                elif g[nx][j] == ']':
                    has_boxes_front = True
                    next_left = min(
                        next_left,
                        j - 1
                    )
            else:
                if has_boxes_front is False:
                    break
                
                ranges.append((next_left, next_right))
                nx += dx
                continue
                
            break
        
        if nx < 0 or nx >= m or not can_push:
            return False
        
        i, range_idx = nx, len(ranges) - 1
        while i != x_robot:
            push_left, push_right = ranges[range_idx]
            range_idx -= 1

            for j in range(push_left, push_right + 1):
                if g[i - dx][j] == '[' or g[i - dx][j] == ']':
                    g[i][j] = g[i - dx][j]
                    g[i - dx][j] = '.' # reset cell
                    
            i -= dx
                    
        return True
                    
    def push_left_right(dx: int, dy: int) -> int:
        nx, ny = x_robot + dx, y_robot + dy
        
        while 0 <= ny < n and (g[nx][ny] == '[' or g[nx][ny] == ']'):
            ny += 2 * dy
            
        if ny < 0 or ny >= n or g[nx][ny] == '#':
            # out of bound or faced a wall block
            return False
        
        j = ny
        while j - dy != y_robot:
            g[nx][j] = g[nx][j - dy]
            g[nx][j - dy] = g[nx][j - 2 * dy]
            g[nx][j - 2 * dy] = '.' # reset cell
            j -= 2 * dy
            
        return True

        
    for ins in moves:
        dx, dy = get_velocity(ins)
        
        if dy == 0:
            if not push_up_down(dx, dy):
                continue
        else:
            if not push_left_right(dx, dy):
                continue

        print(f'Move {ins}:')
        g[x_robot][y_robot] = '.'
        x_robot += dx
        y_robot += dy
        
        for i, line in enumerate(g):
            print(''.join('@' if i == x_robot and j == y_robot else line[j] for j in range(n)))
    
    return [''.join('@' if i == x_robot and j == y_robot else line[j] for j in range(n)) for i, line in enumerate(g)]
    
    # accumulate total GPS distances
    tot = 0
    for i in range(m):
        j = 0
        while j < n - 1:
            if g[i][j] == '[' and g[i][j + 1] == ']':
                tot += 100 * i + j
                j += 2
            else:
                j += 1
            
    return tot


if __name__ == '__main__':
    # sample_data = [
    #     '########',
    #     '#..O.O.#',
    #     '##@.O..#',
    #     '#...O..#',
    #     '#.#.O..#',
    #     '#...O..#',
    #     '#......#',
    #     '########',
    #     '',
    #     '<^^>>>vv<v>>v<<'
    # ]

    sample_data2 = [
        '#######',
        '#...#.#',
        '#.....#',
        '#..OO@#',
        '#..O..#',
        '#.....#',
        '#######',
        '',
        '<vv<<^^<<^^'
    ] # Expected (part 2): 618
    
    sample_data3 = [
        '##########',
        '#..O..O.O#',
        '#......O.#',
        '#.OO..O.O#',
        '#..O@..O.#',
        '#O#..O...#',
        '#O..O..O.#',
        '#.OO.O.OO#',
        '#....O...#',
        '##########',
        '',
        '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^',
        'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v',
        '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<',
        '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^',
        '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><',
        '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^',
        '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^',
        '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>',
        '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>',
        'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'
    ] # Expected (part 2): 9021
    
    # data = []
    # with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
    #     for line in file.readlines():
    #         data.append(line.strip())
    
    # Preprocess data
    grid = []
    moves = []
    
    flag = False
    for line in sample_data3:
        if line == '':
            flag = True
            continue
        
        if flag:
            moves.append(line)
        else:
            grid.append(line)
    
  
    # print('---- Part 1 ----')
    # print('result = ', part1(grid, ''.join(moves)))
    
    
    print('---- Part 2 ----')
    print('result = ', part2(grid, ''.join(moves)))
