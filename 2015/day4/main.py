'''
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle input is bgvyzdsv.



--- Part Two ---
Now find one that starts with six zeroes.

'''

import hashlib

def part1(secret_key: str, prefix: str) -> int:
    '''
    Return the smallest positive integer num, such that the result of 
    MD5(secret_key + str(num)) is a string that matches 'prefix' as it's prefix.

    Parameters:
        secret_key (str): input secret key
        prefix (str): expected output prefix
        
    Returns:
        int
    '''
    
    curr = 1
    while True:
        data = secret_key + str(curr)
        hash_str = hashlib.md5(data.encode('utf-8')).hexdigest()
        print(curr, hash_str)
        
        if hash_str[:5] == prefix:
            return curr
        
        curr += 1
        
if __name__ == '__main__':
    # print('part 1', part1('bgvyzdsv', '00000'))

    print('part 2', part1('bgvyzdsv', '000000'))
