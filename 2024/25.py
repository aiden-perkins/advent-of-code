from itertools import *
from helpers import *

ls = open('./input.txt').read().strip().split('\n\n')

""" Part 1 """

tt = 0
locks = []
keys = []

for p in ls:
    if p[:5] == '#####':
        locks.append(p.strip().split('\n'))
    else:
        keys.append(p.strip().split('\n'))

for lock, key in product(locks, keys):
    for dx, dy in find_val(key, lambda x: x == '#'):
        if lock[dx][dy] == '#':
            break
    else:
        tt += 1

print(tt)
