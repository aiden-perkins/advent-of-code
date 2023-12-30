from itertools import pairwise
from collections import deque

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

garden = [list(a) for a in ls]
s_pos_i = ''.join(ls).index('S')
positions = deque([(s_pos_i // len(garden[0]), s_pos_i % len(garden[0]))])
for _ in range(64):
    new = set()
    while positions:
        px, py = positions.popleft()
        for (x, y) in [(px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)]:
            if garden[x][y] != '#' and len(new.intersection((x, y))) == 0:
                new.add((x, y))
    positions = deque(new)
print(len(positions))

""" Part 2 """


def steps_at_x(steps):  # Had to switch to caching the results instead of just brute forcing every step.
    pos = deque([(s_pos_i // len(garden[0]), s_pos_i % len(garden[0]), steps)])
    even = set()
    odd = set()
    visited = {(s_pos_i // len(garden[0]), s_pos_i % len(garden[0]))}
    while pos:
        ox, oy, os = pos.popleft()
        if os % 2 == 0:
            even.add((ox, oy))
        else:
            odd.add((ox, oy))
        if os > 0:
            for (nx, ny) in [(ox + 1, oy), (ox - 1, oy), (ox, oy + 1), (ox, oy - 1)]:
                if garden[nx % len(garden)][ny % len(garden)] != '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    pos.append((nx, ny, os - 1))
    if steps % 2 == 0:
        return len(odd)
    return len(even)


def second_diff_check(vals):
    if len(vals) == 4:
        second = [s - f for f, s in pairwise([s - f for f, s in pairwise(vals)])]
        if second[0] == second[1]:
            return True
    return False


quads = []
count = 0
step_c = 26501365
csc = step_c % (2 * len(garden))

while not second_diff_check(quads[-4:]):
    quads.append(steps_at_x(csc))
    csc += 2 * len(garden)
    count += 1

quads = quads[-4:]
count -= len(quads)
a = (quads[2] - 2 * quads[1] + quads[0]) / 2
b = quads[1] - quads[0] - a
print(int(a * (step_c // (2 * len(garden)) - count) ** 2 + b * (step_c // (2 * len(garden)) - count) + quads[0]))
