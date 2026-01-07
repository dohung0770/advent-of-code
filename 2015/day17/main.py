'''
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?



--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

'''

def part1(containers: list[int], liters: int) -> int:
    '''
    Return number of combinations of containers that fit exactly 'liters' liters of eggnog.

    Parameters:
        containers (list[int]): list of container sizes
        liters (int): number of eggnog liters
        
    Returns:
        int
    '''
    
    n = len(containers)
    
    # def dp(i: int, liter: int) -> int:
    #     if liter == 0:
    #         return 1
        
    #     if i == n:
    #         return 0
        
    #     tot = dp(i + 1, liter)
        
    #     if liter >= containers[i]:
    #         tot += dp(i + 1, liter - containers[i])
            
    #     return tot
    
    # return dp(0, liters)
    
    dp = [[0] * (liters + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for l in range(1, liters + 1):
            dp[i][l] = dp[i - 1][l]
            
            if l >= containers[i - 1]:
                dp[i][l] += dp[i - 1][l - containers[i - 1]]
                
    return dp[n][liters]


def part2(containers: list[int], liters: int) -> int:
    '''
    Find number of way to fit 'liters' of eggnog into the smallest number containers.
    The number of containers each size is unlimited.

    Parameters:
        containers (list[int]): list of container sizes
        liters (int): number of eggnog liters
        
    Returns:
        int 
    '''
    
    n = len(containers)
    inf = 10 ** 9
    # dp = [inf] * (liters + 1)
    # dp[0] = 0
    
    # for c in containers:
    #     for l in range(c, liters + 1):
    #         if 1 + dp[l - c] < dp[l]:
    #             dp[l] = 1 + dp[l - c]

    # min_containers = dp[liters]
    
    
    dp = [[inf] * (liters + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
        
    for i in range(1, n + 1):
        c = containers[i - 1]
        for l in range(c, liters + 1):
            dp[i][l] = min(
                dp[i - 1][l],
                1 + dp[i - 1][l - c]
            )
    
    min_containers = dp[n][liters]
    print('min containers = ', min_containers)
    

    # ways = [[0] * (liters + 1) for _ in range(min_containers + 1)]
    # ways[0][0] = 1
    
    # for c in containers:
    #     for k in range(1, min_containers + 1):
    #         for l in range(c, liters + 1):
    #             ways[k][l] += ways[k - 1][l - c]
                
    # return ways[min_containers][liters]
    
    
    def dfs(i: int, rem_containers: int, rem_liters: int) -> int:
        if rem_liters == 0:
            return 1 if rem_containers == 0 else 0
        
        if i == n or rem_containers == 0:
            return 0
        
        tot = dfs(i + 1, rem_containers, rem_liters)
        if containers[i] <= rem_liters:
            tot += dfs(i + 1, rem_containers - 1, rem_liters - containers[i])
            
        return tot
            
    return dfs(0, min_containers, liters)


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(int(line.strip()))
            
    # print('part 1', part1(data, 150))
    print('part 2', part2(data, 150))
