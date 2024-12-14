from collections import *

ls = [int(a) for a in open('./input.txt').read().strip().split(' ')]

""" Part 1 """

os = ls

for i in range(25):
    ns = []
    for s in os:
        if s == 0:
            ns.append(1)
        elif len(str(s)) % 2 == 0:
            ns.append(int(str(s)[:len(str(s))//2]))
            ns.append(int(str(s)[len(str(s))//2:]))
        else:
            ns.append(s * 2024)
    os = ns

print(len(os))

""" Part 2 """

vals = defaultdict(int)
for v in ls:
    vals[v] += 1

for i in range(75):
    ns = defaultdict(int)
    for s in vals:
        if s == 0:
            ns[1] += vals[s]
        elif len(str(s)) % 2 == 0:
            ns[int(str(s)[:len(str(s))//2])] += vals[s]
            ns[int(str(s)[len(str(s))//2:])] += vals[s]
        else:
            ns[s * 2024] += vals[s]
    vals = ns

print(sum(vals.values()))
