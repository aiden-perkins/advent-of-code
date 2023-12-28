from itertools import pairwise
from collections import deque

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

positions = set()
cx, cy = 0, 0
crd_manip = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
for direction in ls:
    dx, dy = crd_manip[direction.split()[0]]
    for amt in range(1, 1 + int(direction.split()[1])):
        positions.add((cx + dx, cy + dy))
        cx, cy = cx + dx, cy + dy
xs = min([a[0] for a in positions])
ys = [a[1] for a in positions]
inner = set()
to_check = []
for j in range(min(ys), max(ys) + 1):
    if len(positions.intersection({(xs + 1, j)})) != 0:
        continue
    if len(positions.intersection({(xs, j)})) == 0:
        continue
    to_check.append((xs + 1, j))
    break
to_check = deque(to_check)
while to_check:
    next_x, next_y = to_check.popleft()
    inner.add((next_x, next_y))
    for new_pos in [(next_x - 1, next_y), (next_x + 1, next_y), (next_x, 1 + next_y), (next_x, next_y - 1)]:
        if len(inner.intersection({new_pos})) != 0:
            continue
        if len(positions.intersection({new_pos})) != 0:
            continue
        if new_pos not in to_check:
            to_check.append(new_pos)
print(len(positions) + len(inner))

""" Part 2 """

p = 0
positions = []
cx, cy = 0, 0
crd_manip = {'3': (-1, 0), '1': (1, 0), '0': (0, 1), '2': (0, -1)}
for direction in ls:
    dx, dy = crd_manip[direction.split()[2][7:-1]]
    a = int(direction.split()[2][2:-2], 16)
    cx, cy = cx + (a * dx), cy + (a * dy)
    positions.append((cx, cy))
    p += a
area = 0
for (x1, y1), (x2, y2) in pairwise(positions):
    area += (y2 - y1) * x1
print(abs(area) + p // 2 + 1)
