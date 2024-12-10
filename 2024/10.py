from helpers import *
import heapq

ls = [[int(b) for b in a.strip()] for a in open('./input.txt').read().strip().split('\n')]

""" Part 1 """

tt = 0

for x, y in find_val(ls, lambda q: q == 0):
    nodes = [(0, (x, y))]
    visited = set()
    while nodes:
        h, crd = heapq.heappop(nodes)
        for v, ncrd in value_traverse(*crd, ls, diag=False):
            if v == 9 and h == 8:
                visited.add(ncrd)
            elif v == h + 1:
                heapq.heappush(nodes, (v, ncrd))
    tt += len(visited)

print(tt)

""" Part 2 """

paths = set()

for x, y in find_val(ls, lambda q: q == 0):
    nodes = [(0, ((x, y),))]
    while nodes:
        h, path = heapq.heappop(nodes)
        for v, ncrd in value_traverse(*path[-1], ls, diag=False):
            if v == 9 and h == 8:
                paths.add((*path, ncrd))
            elif v == h + 1:
                heapq.heappush(nodes, (v, (*path, ncrd)))

print(len(paths))
