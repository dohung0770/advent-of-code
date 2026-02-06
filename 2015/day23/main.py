'''
--- Day 23: Opening the Turing Lock ---
Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a
What is the value in register b when the program in your puzzle input is finished executing?




--- Part Two ---
The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

'''

def part1(instructions: list[list[any]], a_value: int = 0) -> tuple[str, int]:
    '''
    Return the value of registers after all the instructions have been finished

    Parameters:
        instructions (list):
            - hlf | tpl | inc (register)
            - jmp (offset)
            - jio | jie (register) (offset)
            
    Returns:
        tuple[str, int]: values of the registers
    '''
    
    registers = { 'a': a_value, 'b': 0 } # values of registers a and b
    
    n = len(instructions)
    ins_idx = 0
    
    while 0 <= ins_idx < n:
        cmd = instructions[ins_idx][0]
        reg = instructions[ins_idx][1]
        offset = int(instructions[ins_idx][2]) if len(instructions[ins_idx]) >= 3 else 0
        
        
        match cmd:
            case 'hlf': # half
                registers[reg] //= 2
                ins_idx += 1
            case 'tpl': # tripple
                registers[reg] *= 3
                ins_idx += 1
            case 'inc': # increase
                registers[reg] += 1
                ins_idx += 1
            case 'jmp': # jump
                if int(reg) != 0:
                    ins_idx += int(reg) # offset
                else:
                    break
            case 'jie': # jump if even
                if registers[reg] % 2 == 0:
                    ins_idx += offset
                else:
                    ins_idx += 1
            case 'jio': # jump if r is one
                if registers[reg] == 1:
                    ins_idx += offset
                else:
                    ins_idx += 1
                
    return registers


import os
import re

if __name__ == '__main__':
    instructions = []

    with open(os.path.join(os.path.dirname(__file__), 'input2.txt')) as file:
        for line in file.readlines():
            instructions.append(re.split(r'(?:,?)\s', line.strip()))

    # for line in instructions:
    #     print(line)
    
    # print('Part 1', part1(instructions))
    print('Part 2', part1(instructions, a_value=1))
