from collections import *

ls = [list(a) for a in open('./input.txt').read().strip().split('\n')]

""" Part 1 """

tt = 0
beacons = defaultdict(int)
beacons[ls[0].index('S')] += 1

for i in range(1, len(ls)):
    newb = defaultdict(int)
    for b, a in beacons.items():
        if ls[i][b] == '^':
            tt += 1
            newb[b - 1] += a
            newb[b + 1] += a
        else:
            newb[b] += a
    beacons = newb

print(tt)

""" Part 2 """

print(sum(beacons.values()))
