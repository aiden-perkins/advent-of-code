from collections import *

ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0

for ll in ls:

    sn = int(ll.strip())
    for i in range(2000):
        nn = sn * 64
        sn ^= nn
        sn %= 16777216
        n2 = sn // 32
        sn ^= n2
        sn %= 16777216
        nn = sn * 2048
        sn ^= nn
        sn %= 16777216
    tt += sn

print(tt)

""" Part 2 """

monkeys = defaultdict(dict)

for j, ll in enumerate(ls):
    sn = int(ll.strip())
    pr = []
    for i in range(2000):
        initial = sn % 10
        nn = sn * 64
        sn ^= nn
        sn %= 16777216
        n2 = sn // 32
        sn ^= n2
        sn %= 16777216
        nn = sn * 2048
        sn ^= nn
        sn %= 16777216
        pr.append((sn % 10) - initial)
        if i > 2:
            if j not in monkeys[tuple(pr)]:
                monkeys[tuple(pr)][j] = sn % 10
            pr.pop(0)

mx = 0
mt = None
for a in monkeys:
    c = 0
    for m in monkeys[a]:
        c += monkeys[a][m]
    if c > mx:
        mx = c
        mt = a

print(mx)
