'''
--- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is hepxcrrq.

'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
confusing = set(['i', 'o', 'l'])
three_consecutive = []
repeated_pairs = []

for i in range(24):
    if alphabet[i] in confusing or \
        alphabet[i + 1] in confusing or \
        alphabet[i + 2] in confusing:
        continue

    three_consecutive.append(alphabet[i:i+3])

for i in range(26):
    if chr(i + 97) not in confusing:
        repeated_pairs.append(chr(i + 97) * 2)
    

def is_valid(password: list[str]) -> bool:
    '''
    Check if the given password satisfies the security requirements.

    Parameters:
        password (list[str]): attemping password
    
    Returns:
        bool    
    '''
    for sub in three_consecutive:
        if sub in password:
            break
    else:
        return False
    
    prev = -1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            if prev != -1 and prev + 3 < i:
                return True
            
            if prev == -1:
                prev = i - 1
                
    return False
    

def part1(old_password: str) -> str:
    '''
    Brute force?    
    '''

    n = len(old_password)
    a_code = ord('a')
    
    def has_three_consecutive(password: str) -> bool:
        for sub in three_consecutive:
            if sub in password:
                return True
            
        return False

    
    bucket = []
    def gen(pwd: str, repeated_pair_cnt: int):
        if len(pwd) == n:
            if repeated_pair_cnt >= 2 and has_three_consecutive(pwd):
                bucket.append(pwd)

            return
        
        if len(pwd) + 2 <= n:
            for pair in repeated_pairs:
                gen(pwd + pair, repeated_pair_cnt + 1)
                
        for char in alphabet:
            if char not in confusing:
                gen(pwd + char, repeated_pair_cnt)
            
    gen('', 0)
    print(bucket)


    # new_password = list(old_password)
    
    # MAX_TRIES = pow(26, n)
    
    # for _ in range(MAX_TRIES):
    #     for i in range(n - 1, -1, -1):
    #         for __ in range(2):
    #             new_password[i] = chr((ord(new_password[i]) - a_code + 1) % 26 + a_code)
    #             if new_password[i] not in confusing:
    #                 break

    #         if new_password[i] != 'a':
    #             break
            
    #     print(''.join(new_password))
            
    #     if is_valid(new_password):
    #         return ''.join(new_password)

    # raise ValueError("no new valid password found for the given old password")


if __name__ == '__main__':
    print('part 1', part1('hfbyzpnu')) # hfbyzpnu # hepxcrrq
