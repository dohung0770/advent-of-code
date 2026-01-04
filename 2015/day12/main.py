'''
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?



Your puzzle answer was 156366.




--- Part Two ---
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.

'''

def part1(json: str) -> int:
    '''
    Return sum of all numbers within the given json.

    Parameters:
        json (str): given json string (with no object keys containing numbers)

    Returns:
        int
    '''
    n = len(json)

    def parse(i: int) -> tuple[int, int]: # (value, index)
        if i >= n:
            return (0, i)

        tot = 0
        num = 0
        is_negative = False
        while i < n and json[i] != '}' and json[i] != ']':
            if json[i] == '[' or json[i] == '{':
                if num > 0:
                    tot += num * (-1 if is_negative is True else 1)

                val, next_i = parse(i + 1)
                tot += val
                i = next_i
                num = 0
                is_negative = False
            elif '0' <= json[i] <= '9':
                num = num * 10 + int(json[i])
            else:
                if json[i] == '-':
                    is_negative = True
                elif num > 0:
                    tot += num * (-1 if is_negative is True else 1)
                    num = 0
                    is_negative = False

            i += 1

        if num > 0:
            tot += num * (-1 if is_negative is True else 1)

        return (tot, i)

    answer, _ = parse(0)
    return answer


def part2(json: str) -> int:
    '''
    Return sum of all numbers within the given json,
    ignoring any objects having a property with the value "red".

    Parameters:
        json (str): given json string (with no object keys containing numbers)

    Returns:
        int
    '''
    n = len(json)

    def parse(i: int, is_object: bool) -> tuple[int, int]: # (value, index)
        if i >= n:
            return (0, i)

        tot = 0
        num = 0
        is_negative = False
        should_skip = False
        while i < n and json[i] != '}' and json[i] != ']':
            if json[i] == '[' or json[i] == '{':
                if num > 0:
                    tot += num * (-1 if is_negative is True else 1)

                val, next_i = parse(i + 1, json[i] == '{')
                tot += val
                i = next_i
                num = 0
                is_negative = False
            elif '0' <= json[i] <= '9':
                num = num * 10 + int(json[i])
            else:
                if json[i] == ':':
                    if i + 5 < n and json[i + 2:i + 5] == "red":
                        should_skip = True
                        i += 5
                elif json[i] == '-':
                    is_negative = True
                elif num > 0:
                    tot += num * (-1 if is_negative is True else 1)
                    num = 0
                    is_negative = False

            i += 1

        if num > 0:
            tot += num * (-1 if is_negative is True else 1)

        if is_object and should_skip:
            tot = 0

        return (tot, i)

    answer, _ = parse(0, False)
    return answer

import os

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())

    # print('part 1', part1(data[0]))
    print('part 2', part2(data[0]))
