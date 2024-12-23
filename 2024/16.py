import heapq
from collections import *
from helpers import *

ls = open('./input.txt').read().strip().split('\n')
lsl = len(ls)

""" Part 1 """

sx, sy = find_one(ls, 'S')
ex, ey = find_one(ls, 'E')
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = [(0, sx, sy, 1)]
shortest = defaultdict(lambda: float('inf'))
finished = set()

while queue:
    cost, cx, cy, ld = heapq.heappop(queue)
    if (cx, cy, ld) in finished:
        continue
    finished.add((cx, cy, ld))
    if shortest[(cx, cy)] > cost:
        shortest[(cx, cy)] = cost
    fx, fy = deltas[ld]
    nx, ny = cx + fx, cy + fy
    if in_bounds(nx, ny, lsl) and ls[nx][ny] != '#':
        heapq.heappush(queue, (cost + 1, nx, ny, ld))
    heapq.heappush(queue, (cost + 1000, cx, cy, (ld + 3)%4))
    heapq.heappush(queue, (cost + 1000, cx, cy, (ld + 1)%4))

print(shortest[(ex, ey)])

""" Part 2 """

# TODO
