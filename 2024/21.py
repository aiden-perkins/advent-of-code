from helpers import *
from itertools import *
from functools import *

ls = open('./input.txt').read().strip().split('\n')
keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
]
directional = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]
apply_direction = {
    '^': lambda x: (x[0] - 1, x[1]),
    'v': lambda x: (x[0] + 1, x[1]),
    '>': lambda x: (x[0], x[1] + 1),
    '<': lambda x: (x[0], x[1] - 1),
}

""" Part 1 """


def possible_moves(cpx, cpy, gpx, gpy, bad):
    dx = gpx - cpx
    dy = gpy - cpy
    if dx == 0 and dy == 0:
        return ['A']
    s = ''
    if dy > 0:
        s += '>' * dy
    if dx < 0:
        s += '^' * (dx * -1)
    if dx > 0:
        s += 'v' * dx
    if dy < 0:
        s += '<' * (dy * -1)
    good = []
    for possible_move_set in permutations(s):
        spx, spy = cpx, cpy
        for move in possible_move_set:
            spx, spy = apply_direction[move]((spx, spy))
            if (spx, spy) == bad:
                break
        else:
            good.append(''.join(possible_move_set) + 'A')
    return good


def keypresses(target_keys, robot) -> int:
    avoid = (0, 0) if robot > 0 else (3, 0)
    cp = (3, 2) if robot == 0 else (0, 2)
    search_arr = keypad if robot == 0 else directional
    amount = 0
    for key in target_keys:
        kp = find_one(search_arr, key)
        moves = possible_moves(*cp, *kp, avoid)
        if robot == 2:
            amount += len(min(moves, key=len))
        else:
            amount += min(keypresses(move, robot + 1) for move in moves)
        cp = kp
    return amount


print(sum(keypresses(a.strip(), 0) * int(a.strip()[:-1]) for a in ls))

""" Part 2 """


@cache
def keypresses2(target_keys, robot) -> int:
    avoid = (0, 0) if robot > 0 else (3, 0)
    cp = (3, 2) if robot == 0 else (0, 2)
    search_arr = keypad if robot == 0 else directional
    amount = 0
    for key in target_keys:
        kp = find_one(search_arr, key)
        moves = possible_moves(*cp, *kp, avoid)
        if robot == 25:
            amount += len(min(moves, key=len))
        else:
            amount += min(keypresses2(move, robot + 1) for move in moves)
        cp = kp
    return amount


print(sum(keypresses2(a.strip(), 0) * int(a.strip()[:-1]) for a in ls))
