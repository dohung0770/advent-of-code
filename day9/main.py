'''
--- Day 9: Disk Fragmenter ---
Another push of the button leaves you in the familiar hallways of some friendly amphipods! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.

While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.

He shows you the disk map (your puzzle input) he's already generated. For example:

2333133121414131402
The disk map uses a dense format to represent the layout of files and free space on the disk. The digits alternate between indicating the length of a file and the length of free space.

So, a disk map like 12345 would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like 90909 would represent three nine-block files in a row (with no free space between them).

Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged, starting with ID 0. So, the disk map 12345 has three files: a one-block file with ID 0, a three-block file with ID 1, and a five-block file with ID 2. Using one character for each block where digits are the file ID and . is free space, the disk map 12345 represents these individual blocks:

0..111....22222
The first example above, 2333133121414131402, represents these individual blocks:

00...111...2...333.44.5555.6666.777.888899
The amphipod would like to move file blocks one at a time from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map 12345, the process looks like this:

0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
The first example requires a few more steps:

00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
The final step of this file-compacting process is to update the filesystem checksum. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position 0. If a block contains free space, skip it instead.

Continuing the first example, the first few blocks' position multiplied by its file ID number are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. In this example, the checksum is the sum of these, 1928.

Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum? (Be careful copy/pasting the input for this puzzle; it is a single, very long line.)



--- Part Two ---
Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving whole files instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?

'''

import math
import os

def part1(disk_map: str) -> int:
    '''
    There is a disk map that represents length of files and spaces alternatively
        disk_map[0] = length of the first file
        disk_map[1] = length of the space
        ...
        and so on
    Assign each file an ID starting from 0
    Defragment the disk by moving right most files into the leftmost space
    and return the checksum by summing the file blocks' positions with their file ID
    
    Parameters:
        disk_map (str): Given disk map containing file lengths and spaces
        
    Returns:
        int
    '''
  
    n = len(disk_map)
    num_files = math.ceil(n / 2)
    id_left, id_right = 0, num_files - 1
    pos = 0
    tot = 0
    
    i, j = 0, n - 1
    if j % 2 == 1:
        j -= 1 # ignore trailing spaces
        
    blocks = int(disk_map[j])

    while i <= j:
        if i % 2 == 1 and i == j: # all are remaining spaces
            break
        
        # 2 + 3 + 4 = 2*3 + (1 + 2) = 2*3 + 3*2/2
        
        if i % 2 == 0: # file
            cnt = int(disk_map[i]) if i < j else blocks
            
            # print(f'{cnt} blocks with ID={id_left} from {pos} to {pos + cnt - 1} yields {id_left * (pos * cnt + (cnt - 1) * cnt // 2)}')

            tot += id_left * (pos * cnt + (cnt - 1) * cnt // 2)
            pos += cnt
            id_left += 1
            i += 1
        else: # spaces
            spaces = int(disk_map[i])
            
            if spaces == 0:
                i += 1
                continue

            while i <= j and spaces > 0:
                if blocks == 0:
                    id_right -= 1
                    j -= 2
                    
                    if j > i:
                        blocks = int(disk_map[j])
                        continue
                    else:
                        break


                cnt = min(spaces, blocks)

                # print(f'{cnt} blocks with ID={id_right} from {pos} to {pos + cnt - 1} yields {id_right * (pos * cnt + (cnt - 1) * cnt // 2)}')

                tot += id_right * (pos * cnt + (cnt - 1) * cnt // 2)
                pos += cnt

                blocks -= cnt
                spaces -= cnt
                
                if spaces == 0:
                    i += 1
                    break
                
    return tot


def part2(disk_map: str) -> int:
    '''
    Returns the checksum value after trying to move the rightmost files into the leftmost space span that the files' lengths
    
    Parameters:
        disk_map (str): Given disk map
        
    Returns:
        int
    '''
    
    n = len(disk_map)
    
    spaces = [] # store space size and starting index
    file_pos = dict() # map file's original index in disk map to new indices that have spaces before it for allowing insertion
    file_id_map = dict() # map file's original index to an id
    prev = 0
    file_id = 0
    for i in range(n):
        size = int(disk_map[i])

        if i % 2 == 0: # file
            file_id_map[i] = file_id
            file_pos[i] = prev
            file_id += 1
        else: # space
            spaces.append([size, prev])
        
        prev += size
            

    j = n - 1
    if j % 2 == 1:
        j -= 1 # ignore trailing spaces
        
    while j > 0:
        file_size = int(disk_map[j])

        idx = 0
        while idx < len(spaces) and spaces[idx][0] < file_size and spaces[idx][1] < file_pos[j]:
            idx += 1
            
        if idx < len(spaces) and spaces[idx][1] < file_pos[j]:
            file_pos[j] = spaces[idx][1]
            spaces[idx][0] -= file_size
            spaces[idx][1] += file_size
            
        j -= 2
    
    tot = 0
    
    for disk_index, new_index in file_pos.items():
        sz = int(disk_map[disk_index])
        tot += file_id_map[disk_index] * (new_index * sz + sz * (sz - 1) // 2)
    
    return tot


if __name__ == '__main__':
    # sample_data = '2333133121414131402'
    
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())


    # print('---- Part 1 ----')
    # print('result = ', part1(sample_data))
    # print('result = ', part1(data[0]))
    
    
    print('---- Part 2 ----')
    # print('result = ', part2(sample_data))
    print('result = ', part2(data[0]))
