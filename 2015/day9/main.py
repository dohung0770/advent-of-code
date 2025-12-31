'''
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?



--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

'''

import os
from collections import defaultdict


def part1(edges: list[tuple[str, str, int]]) -> int:
    '''
    Find the shortest path to finish deliver all the presents to houses starting and ending
    from any 2 different houses.

    Parameters:
        edges (list[tuple[str, str, int]]):
            Given edge list [location 1, location 2, move cost] of an undirected weighted graph
        
    Returns:
        int
    '''
    
    g = defaultdict(dict[str, int])
    
    for from_loc, to_loc, cost in edges:
        g[from_loc][to_loc] = g[to_loc][from_loc] = cost
        
    locations = list(g.keys())
    n = len(locations)
    

    def dfs(curr_loc: str, cost: int, visited: set[str]) -> int:
        if len(visited) == n - 1:
            return cost

        visited.add(curr_loc)
            
        output = float('inf')
        for next_loc in g[curr_loc]:
            if next_loc not in visited:
                output = min(output, dfs(next_loc, cost + g[curr_loc][next_loc], visited))

        visited.remove(curr_loc)
                    
        return output

    answer = float('inf')
    visited = set()
    for start in locations:
        answer = min(answer, dfs(start, 0, visited))
        
    return answer


def part2(edges: list[tuple[str, str, int]]) -> int:
    '''
    Find the longest path to finish deliver all the presents to houses starting and ending
    from any 2 different houses.

    Parameters:
        edges (list[tuple[str, str, int]]):
            Given edge list [location 1, location 2, move cost] of an undirected weighted graph
        
    Returns:
        int
    '''
    
    g = defaultdict(dict[str, int])
    
    for from_loc, to_loc, cost in edges:
        g[from_loc][to_loc] = g[to_loc][from_loc] = cost
        
    locations = list(g.keys())
    n = len(locations)
    

    def dfs(curr_loc: str, cost: int, visited: set[str]) -> int:
        if len(visited) == n - 1:
            return cost

        visited.add(curr_loc)
            
        output = -1
        for next_loc in g[curr_loc]:
            if next_loc not in visited:
                output = max(output, dfs(next_loc, cost + g[curr_loc][next_loc], visited))

        visited.remove(curr_loc)
                    
        return output

    answer = -1
    visited = set()
    for start in locations:
        answer = max(answer, dfs(start, 0, visited))
        
    return answer
    
    
if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            from_loc, _, to_loc, __, distance = line.strip().split(' ')
            data.append((from_loc, to_loc, int(distance)))
            
    # print('part 1', part1(data))
    print('part 2', part2(data))
