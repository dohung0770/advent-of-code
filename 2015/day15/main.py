'''
--- Day 15: Science for Hungry People ---
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?




--- Part Two ---
Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

'''

from ingredient import Ingredient


def parse_input(data: list[str]) -> list[Ingredient]:
    ingredients = []
    for line in data:
        p = line.split(' ')
        ingredients.append(
            Ingredient(
                name=p[0][:-1],
                capacity=int(p[2][:-1]),
                durability=int(p[4][:-1]),
                flavor=int(p[6][:-1]),
                texture=int(p[8][:-1]),
                calories=int(p[10]),
            )
        )
        
    return ingredients

def calculate_score(ingredients: list[Ingredient], amount: list[int]) -> int:
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0
            
    for i, cnt in enumerate(amount):
        total_capacity += cnt * ingredients[i].capacity
        total_durability += cnt * ingredients[i].durability
        total_flavor += cnt * ingredients[i].flavor
        total_texture += cnt * ingredients[i].texture
        
    return max(0, total_capacity) * \
        max(total_durability, 0) * \
        max(total_flavor, 0) * \
        max(total_texture, 0)


def part1(ingredients: list[Ingredient], k: int):
    '''
    Return the total score of a cookie by multiplying the sum of
        ingredients' capacity, durability, texture and flavor
        with exactly 'k' teaspoons of ingredients.
    
    Parameters:
        ingredients (list[Ingredient]): given list of ingredients
        k (int): number of teaspoons
        
    Returns:
        int
    '''
    
    n = len(ingredients)
    def solve(i: int, count: int, amount: list[int]) -> int:
        # Backtracking
        
        if i == n:
            return calculate_score(ingredients, amount)
        
        if i == n - 1:
            amount[i] = count
            return solve(i + 1, 0, amount)

        score = 0
        for cnt in range(count + 1):
            amount[i] = cnt
            score = max(score, solve(i + 1, count - cnt, amount))
            
        return score
    
    return solve(0, k, [0] * n)


def part2(ingredients: list[Ingredient], k: int, total_calories: int):
    '''
    Same as part 1, except now the total calories in ingredients must be exactly 'total_calories'.

    Parameters:
        ingredients (list[Ingredient]): given list of ingredients
        k (int): number of teaspoons
        total_calories (int): the expected total calories of all ingredients
        
    Returns:
        int: the maximum score by combining the ingredients wisely.
    '''
    
    n = len(ingredients)
    def solve(i: int, k_remain: int, calories_remain: int, amount: list[int]) -> int:
        if i == n:
            if calories_remain == 0 and k_remain == 0:
                return calculate_score(ingredients, amount)
            
            return 0
        
        if i == n - 1:
            if k_remain * ingredients[i].calories != calories_remain:
                return 0
            
            amount[i] = k_remain
            return solve(i + 1, 0, 0, amount)
        
        score = 0
        for cnt in range(k_remain + 1):
            calories_consumed = ingredients[i].calories * cnt
            if calories_consumed > calories_remain:
                break
            
            amount[i] = cnt
            score = max(
                score,
                solve(i + 1, k_remain - cnt, calories_remain - calories_consumed, amount)
            )
            
        return score
    
    return solve(0, k, total_calories, [0] * n)


import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
            
    ingredients = parse_input(data)
    # print('part 1', part1(ingredients, 100))
    print('part 2', part2(ingredients=ingredients, k=100, total_calories=500))
