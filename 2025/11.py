from collections import defaultdict
from functools import cache

ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0

g = defaultdict(list)

for ll in ls:
    s, nods = ll.split(': ')
    g[s] += nods.split(' ')

def find_paths(gr, s, e, p=[]):
    p = p + [s]
    if s == e:
        return [p]
    if s not in gr:
        return []
    paths = []
    for new in gr[s]:
        if new not in p:
            newpaths = find_paths(gr, new, e, p)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

print(len(find_paths(g, 'you', 'out')))

""" Part 2 """

@cache
def path_count(s, e):
    if s == e:
        return 1
    ttt = 0
    for new in g[s]:
        ttt += path_count(new, e)
    return ttt

print((path_count('svr', 'fft') * path_count('fft', 'dac') * path_count('dac', 'out')) + (path_count('svr', 'dac') * path_count('dac', 'fft') * path_count('fft', 'out')))
