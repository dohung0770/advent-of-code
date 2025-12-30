'''
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Your puzzle answer was 16076.



--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

'''

from collections import defaultdict
import os


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def part1(instructions: list[list[str]], output: list[str]) -> int:
    '''
    Return the signal provided to 'wire a' followed the instructions.
    -          x -> y: assign x to wire y
    -    x AND y -> z: assign value of x AND y to wire z
    - p LSHIFT x -> q: assign value of the left shift operator of p to x to wire q
    -      NOT e -> f: assign value of NOT e to wire f
    -     x OR y -> e: assign value of x OR y to wire e
    - y RSHIFT x -> g: assign value of the right shift operator y to x to wire g

    Parameters:
        instructions (list[list[str]]): list of instructions [variables, ... [operator]]
        output (list[str]): list of output wire
        
    Returns:
        int: signal value of wire a
    '''
    
    operators = set(['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT'])
    
    # DFS
    values = defaultdict(lambda: None)
    g = defaultdict(list[list[str]])
    
    for i, ins in enumerate(instructions):
        g[output[i]].append(ins)
    
    visited = set()

    def dfs(node: str):
        if is_number(node):
            values[node] = int(node)
        
        if values[node] is not None:
            return
        
        if node in visited:
            return
        
        visited.add(node)

        for ins in g[node]:
            for token in ins:
                if token not in operators:
                    dfs(token)
                    
        for ins in g[node]:
            if ins[-1] not in operators:
                values[node] = values[ins[0]]
                continue

            if ins[-1] == 'NOT':
                values[node] = (-values[ins[0]] - 1)
            elif ins[-1] == 'AND':
                values[node] = values[ins[0]] & values[ins[1]]
            elif ins[-1] == 'OR':
                values[node] = values[ins[0]] | values[ins[1]]
            elif ins[-1] == 'LSHIFT':
                values[node] = values[ins[0]] << (values[ins[1]])
            elif ins[-1] == 'RSHIFT':
                values[node] = values[ins[0]] >> (values[ins[1]])

    dfs('a')
    print(values)
    return values['a']



def part2(instructions: list[list[str]], output: list[str]) -> int:
    '''
    Return the signal provided to 'wire a' followed the instructions (with b = answer of part1 = 16076).
    -          x -> y: assign x to wire y
    -    x AND y -> z: assign value of x AND y to wire z
    - p LSHIFT x -> q: assign value of the left shift operator of p to x to wire q
    -      NOT e -> f: assign value of NOT e to wire f
    -     x OR y -> e: assign value of x OR y to wire e
    - y RSHIFT x -> g: assign value of the right shift operator y to x to wire g

    Parameters:
        instructions (list[list[str]]): list of instructions [variables, ... [operator]]
        output (list[str]): list of output wire
        
    Returns:
        int: signal value of wire a
    '''
    
    operators = set(['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT'])
    
    # DFS
    values = defaultdict(lambda: None)
    values['b'] = 16076

    g = defaultdict(list[list[str]])
    
    for i, ins in enumerate(instructions):
        g[output[i]].append(ins)
    
    visited = set()

    def dfs(node: str):
        if is_number(node):
            values[node] = int(node)
        
        if values[node] is not None:
            return
        
        if node in visited:
            return
        
        visited.add(node)

        for ins in g[node]:
            for token in ins:
                if token not in operators and token != 'b':
                    dfs(token)
                    
        for ins in g[node]:
            if ins[-1] not in operators:
                values[node] = values[ins[0]]
                continue

            if ins[-1] == 'NOT':
                values[node] = (-values[ins[0]] - 1)
            elif ins[-1] == 'AND':
                values[node] = values[ins[0]] & values[ins[1]]
            elif ins[-1] == 'OR':
                values[node] = values[ins[0]] | values[ins[1]]
            elif ins[-1] == 'LSHIFT':
                values[node] = values[ins[0]] << (values[ins[1]])
            elif ins[-1] == 'RSHIFT':
                values[node] = values[ins[0]] >> (values[ins[1]])

    dfs('a')
    print(values)
    return values['a']


def preprocess_data(data: list[str]) -> tuple[list[list[str]], list[str]]:
    instructions = []
    output = []
    
    for line in data:
        left, right = line.split(' -> ')
        output.append(right)
        
        p = left.split(' ')
        if len(p) == 3:
            # x AND|OR|LSHIFT|RSHIFT y
            instructions.append([p[0], p[2], p[1]])
        elif len(p) == 2:
            # NOT x
            instructions.append([p[1], p[0]])
        else:
            instructions.append(p)
    
    return (instructions, output)


if __name__ == '__main__':
    data = []
    with open(os.path.join(os.path.dirname(__file__), 'input2.txt'), 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
            
    instructions, output = preprocess_data(data)
    # print(instructions)
    # print(output)
    
    # print('part 1', part1(instructions, output))
    print('part 2', part2(instructions, output))
