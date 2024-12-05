from collections import *

ls = open('./input.txt').read().strip().split('\n\n')

""" Part 1 """

tt = 0
bad = defaultdict(list)

for ll in ls[0].split('\n'):
    ll = ll.split('|')
    bad[ll[1]].append(ll[0])

for ll in ls[1].split('\n'):
    vs = ll.split(',')
    fail = False
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if vs[j] in bad[vs[i]]:
                fail = True
    if not fail:
        tt += int(vs[len(vs) // 2])

print(tt)

""" Part 2 """

tt = 0

for ll in ls[1].split('\n'):
    vs = ll.split(',')
    fail = False
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if vs[j] in bad[vs[i]]:
                fail = True
                vs[i], vs[j] = vs[j], vs[i]
    if fail:
        tt += int(vs[len(vs) // 2])

print(tt)
