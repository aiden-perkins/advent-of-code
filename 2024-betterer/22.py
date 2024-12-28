from collections import *

ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0

for ll in ls:
    sn = int(ll.strip())
    for i in range(2000):
        sn ^= sn * (2 ** 6)
        sn %= 2 ** 24
        sn ^= sn // (2 ** 5)
        sn ^= sn * (2 ** 11)
        sn %= 2 ** 24
    tt += sn

print(tt)

""" Part 2 """

monkeys = defaultdict(dict)

for j, ll in enumerate(ls):
    sn = int(ll.strip())
    pr = []
    for i in range(2000):
        initial = sn % 10
        sn ^= sn * (2 ** 6)
        sn %= 2 ** 24
        sn ^= sn // (2 ** 5)
        sn ^= sn * (2 ** 11)
        sn %= 2 ** 24
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
