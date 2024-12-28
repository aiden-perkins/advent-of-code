import heapq
from helpers import *

ls = open('./input.txt').read().strip().split('\n')
lsl = len(ls)
sx, sy = list(find_val(ls, lambda x: x == 'S'))[0]
ex, ey = list(find_val(ls, lambda x: x == 'E'))[0]

""" Part 1 """

tt = 0
queue = [(sx, sy)]
track = [(sx, sy)]
cheats = []

while queue:
    cx, cy = heapq.heappop(queue)
    for v, nc in value_traverse(cx, cy, ls, diag=False):
        if nc not in track and v in ['.', 'E']:
            track.append(nc)
            heapq.heappush(queue, nc)
            break
    for v, nc in value_traverse(cx, cy, ls, diag=False, d=2):
        if v in ['.', 'E']:
            cheats.append(((cx, cy), nc))

time_saved = set()
for cheat in cheats:
    save_time = track.index(cheat[1]) - track.index(cheat[0]) - 2
    time_saved.add(save_time)
    if save_time > 99:
        tt += 1

print(tt)

""" Part 2 """

tt = 0
queue = [(sx, sy)]
track = [(sx, sy)]
cheats = []
idxd = {}

while queue:
    cx, cy = heapq.heappop(queue)
    for v, nc in value_traverse(cx, cy, ls, diag=False):
        if nc not in track and v in ['.', 'E']:
            idxd[(cx, cy)] = len(track) - 1
            track.append(nc)
            heapq.heappush(queue, nc)
            break
    ry1 = max(0, cy-20)
    ry2 = min(lsl - 1, cy+21)
    for i in range(max(0, cx-20), min(lsl - 1, cx+21)):
        for j in range(ry1, ry2):
            p = abs(cx - i) + abs(cy - j)
            if p <= 20:
                if ls[i][j] != '#':
                    if (i, j) not in track:
                        if (cx, cy) != (i, j):
                            cheats.append(((cx, cy), (i, j), p, len(track) - 2))

idxd[(ex, ey)] = len(track) - 1

for sc, ec, p, t1 in cheats:
    if idxd[ec] - t1 - p > 99:
        tt += 1

print(tt)
