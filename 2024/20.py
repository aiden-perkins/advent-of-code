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
cheats = set()

while queue:
    cx, cy = heapq.heappop(queue)
    for v, nc in value_traverse(cx, cy, ls, diag=False):
        if nc not in track and v in ['.', 'E']:
            track.append(nc)
            heapq.heappush(queue, nc)
            break
    for i in range(cx-20, cx+21):
        for j in range(cy-20, cy+21):
            cheats.add(((cx, cy), (i, j)))

for sc, ec in cheats:
    if sc != ec:
        if in_bounds(*ec, lsl):
            if ls[ec[0]][ec[1]] != '#':
                if ls[sc[0]][sc[1]] != '#':
                    tri1 = track.index(ec)
                    tri2 = track.index(sc)
                    if tri1 > tri2:
                        path = abs(sc[0] - ec[0]) + abs(sc[1] - ec[1])
                        if path <= 20:
                            save_time = tri1 - tri2 - path
                            if save_time > 99:
                                tt += 1

print(tt)
