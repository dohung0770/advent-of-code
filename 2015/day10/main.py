'''
--- Day 10: Elves Look, Elves Say ---
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 3113322113.

'''

def part1(s: str, k: int) -> int:
    '''
    Return length of the final string after k times of look-and-say.
    
    Parameters:
        s (str): Given input string consisting of digits only
        k (int): number of rounds
        
    Returns:
        int
    '''
    
    curr = [int(char) for char in s]
    
    while k > 0:
        next = []
        k -= 1
        
        cnt, prev = 0, curr[0]
        for char in curr:
            if char == prev:
                cnt += 1
            else:
                next.append(cnt)
                next.append(prev)
                cnt = 1
                prev = char
                
        next.append(cnt)
        next.append(char)
        curr = next
        
    return len(curr)


if __name__ == '__main__':
    data = '3113322113'
    
    # print('part 1', part1(data, 40))
    print('part 2', part1(data, 50))
