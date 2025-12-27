'''
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?


--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

'''

def part1(board: list[str]):
    '''
    Counts number of time the word 'XMAS' appears in any rows, columns, diagonals, in the board

    Parameters:
        board (list[str]): Given board of uppercase letters
    '''

    m, n = len(board), len(board[0])
    target = 'XMAS'

    tot = 0
    for r in range(m):
        for c in range(n):
            if board[r][c] != target[0]:
                continue

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    target_idx = 1
                    i, j = r + dx, c + dy

                    if dx == 0 and dy == 0:
                        continue

                    while target_idx < len(target) and \
                        0 <= i < m and \
                        0 <= j < n and \
                        board[i][j] == target[target_idx]:
                        target_idx += 1
                        i += dx
                        j += dy
                    if target_idx == len(target):
                        tot += 1

    print('total = ', tot)


def part2(board: list[str]):
    '''
    Counts number of X-MASes that are in board, for example:

    M.S\n
    .A.\n
    M.S
    
    Parameters:
        board (list[str]): Given board of uppercase English letters
    '''

    m, n = len(board), len(board[0])
    tot = 0

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if board[i][j] != 'A':
                continue

            diagonal1 = board[i - 1][j - 1] + board[i + 1][j + 1]
            diagonal2 = board[i - 1][j + 1] + board[i + 1][j - 1]

            if (diagonal1 == 'MS' or diagonal1 == 'SM') and \
                (diagonal2 == 'MS' or diagonal2 == 'SM'):
                tot += 1

    print('total = ', tot)


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())

    # print('----- Part 1 -----')
    # part1(board=[
    #     'MMMSXXMASM',
    #     'MSAMXMSMSA',
    #     'AMXSXMAAMM',
    #     'MSAMASMSMX',
    #     'XMASAMXAMM',
    #     'XXAMMXXAMA',
    #     'SMSMSASXSS',
    #     'SAXAMASAAA',
    #     'MAMMMXMMMM',
    #     'MXMXAXMASX'
    # ])
    # part1(board=data)


    print('----- Part 2 -----')
    # part2(board=[
    #     'MMMSXXMASM',
    #     'MSAMXMSMSA',
    #     'AMXSXMAAMM',
    #     'MSAMASMSMX',
    #     'XMASAMXAMM',
    #     'XXAMMXXAMA',
    #     'SMSMSASXSS',
    #     'SAXAMASAAA',
    #     'MAMMMXMMMM',
    #     'MXMXAXMASX'
    # ])
    part2(board=data)
