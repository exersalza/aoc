"""
        [G]         [D]     [Q]
[P]     [T]         [L] [M] [Z]
[Z] [Z] [C]         [Z] [G] [W]
[M] [B] [F]         [P] [C] [H] [N]
[T] [S] [R]     [H] [W] [R] [L] [W]
[R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
[C] [N] [H] [R] [N] [H] [D] [J] [Q]
[N] [D] [M] [G] [Z] [F] [W] [S] [S]
 1   2   3   4   5   6   7   8   9
"""
import pprint

stacks1 = {
    1: ['P', 'Z', 'M', 'T', 'R', 'C', 'N'],
    2: ['Z', 'B', 'S', 'T', 'N', 'D'],
    3: ['G', 'T', 'C', 'F', 'R', 'Q', 'H', 'M'],
    4: ['Z', 'R', 'G'],
    5: ['H', 'R', 'N', 'Z'],
    6: ['D', 'L', 'Z', 'P', 'W', 'S', 'H', 'F'],
    7: ['M', 'G', 'C', 'R', 'Z', 'D', 'W'],
    8: ['Q', 'Z', 'W', 'H', 'L', 'F', 'J', 'S'],
    9: ['N', 'W', 'P', 'Q', 'S'],
}
stacks2 = {
    1: ['P', 'Z', 'M', 'T', 'R', 'C', 'N'],
    2: ['Z', 'B', 'S', 'T', 'N', 'D'],
    3: ['G', 'T', 'C', 'F', 'R', 'Q', 'H', 'M'],
    4: ['Z', 'R', 'G'],
    5: ['H', 'R', 'N', 'Z'],
    6: ['D', 'L', 'Z', 'P', 'W', 'S', 'H', 'F'],
    7: ['M', 'G', 'C', 'R', 'Z', 'D', 'W'],
    8: ['Q', 'Z', 'W', 'H', 'L', 'F', 'J', 'S'],
    9: ['N', 'W', 'P', 'Q', 'S'],
}


def crateMover9000(_c: int, _stack: int, _to: int):
    for i in range(_c):
        stacks1[_to].insert(0, stacks1[_stack].pop(0))


def crateMover9001(_c: int, _stack: int, _to: int):
    t = stacks2[_stack][:_c]
    stacks2[_stack] = stacks2[_stack][_c:]
    stacks2[_to] = t + stacks2[_to]


with open("input", 'r') as f:
    for line in f:
        nl = line.split()
        c, stack, to = nl[1], nl[3], nl[5]
        crateMover9000(int(c), int(stack), int(to))
        crateMover9001(int(c), int(stack), int(to))


    # part one
    ret = ''
    for _, v in stacks1.items():
        ret += v[0]

    ret += ', '

    for _, v in stacks2.items():
        ret += v[0]

    print(ret)
