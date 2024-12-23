import heapq
from helpers import *
from collections import *

ls1 = [(int(x.split(',')[1]), int(x.split(',')[0])) for x in open('./input.txt').read().strip().split('\n')]
lsn = 1024
lsl2 = 70
# lsn = 12
# lsl2 = 6
lsl2 += 1
ls = ls1[:lsn]

""" Part 1 """

queue = [(0, 0, 0)]
finished = set()
costs = defaultdict(lambda: float('inf'))

while queue:
    cost, cx, cy = heapq.heappop(queue)
    if (cx, cy) in finished:
        continue
    finished.add((cx, cy))
    for nx, ny in traverse(cx, cy, diag=False):
        if 0 <= nx < lsl2 and 0 <= ny < lsl2:
            if (nx, ny) not in ls and costs[(nx, ny)] > cost + 1:
                costs[(nx, ny)] = cost + 1
                heapq.heappush(queue, (cost + 1, nx, ny))

print(costs[(lsl2 - 1, lsl2 - 1)])

""" Part 2 """

lss = set(ls)
goal_path = None

for i, new_c in enumerate(ls1[lsn - 1:]):

    lss.add(new_c)
    if goal_path and new_c not in goal_path:
        continue
    queue = [(0, 0, 0, [(0, 0)])]
    finished = set()
    costs = defaultdict(lambda: float('inf'))

    while queue:
        cost, cx, cy, path = heapq.heappop(queue)
        if (cx, cy) in finished:
            continue
        finished.add((cx, cy))
        for nx, ny in traverse(cx, cy, diag=False):
            if 0 <= nx < lsl2 and 0 <= ny < lsl2:
                if (nx, ny) not in lss and costs[(nx, ny)] > cost + 1:
                    costs[(nx, ny)] = cost + 1
                    if (cx, cy) == (lsl2 - 1, lsl2 - 1):
                        goal_path = path + [(nx, ny)]
                    heapq.heappush(queue, (cost + 1, nx, ny, path + [(nx, ny)]))

    if costs[(lsl2 - 1, lsl2 - 1)] == float('inf'):
        print(f'{new_c[1]},{new_c[0]}')
        break
