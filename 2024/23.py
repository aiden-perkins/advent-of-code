from collections import *

ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0
g = defaultdict(list)

for p in ls:
    p = p.split('-')
    g[p[0]].append(p[1])
    g[p[1]].append(p[0])

poss = set()
for s1 in g:
    for s2 in g[s1]:
        for s3 in g[s2]:
            if s1 in g[s3]:
                poss.add(tuple(sorted([s1, s2, s3])))

for a, b, c in poss:
    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
        tt += 1

print(tt)

""" Part 2 """

cliques = set()

for s in g:
    current = []
    for new_v in g[s]:
        for v in current:
            if new_v not in g[v]:
                break
        else:
            current.append(new_v)
    cliques.add(tuple(sorted(current + [s])))

print(','.join(max(cliques, key=len)))
