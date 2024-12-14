from operator import mul
from functools import reduce

ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

wd = 101
hi = 103
og_robots = []

for ll in ls:
    lls = ll.split(' ')
    px, py = lls[0][2:].split(',')
    v1, v2 = lls[1][2:].split(',')
    og_robots.append((int(px), int(py), int(v1), int(v2)))

robots = og_robots
for i in range(100):
    new_pos = []
    for robot in robots:
        px, py, vx, vy = robot
        px += vx
        py += vy
        if px < 0:
            px += wd
        if px > (wd - 1):
            px %= wd
        if py < 0:
            py += hi
        if py > (hi - 1):
            py %= hi
        new_pos.append((px, py, vx, vy))
    robots = new_pos

quads = [0, 0, 0, 0]

for robot in robots:
    px, py, _, _ = robot
    if py < hi // 2 and px < wd // 2:
        quads[0] += 1
    elif py < hi // 2 and px > wd // 2:
        quads[1] += 1
    elif py > hi // 2 and px > wd // 2:
        quads[2] += 1
    elif py > hi // 2 and px < wd // 2:
        quads[3] += 1

print(reduce(mul, quads, 1))

""" Part 2 """

robots = og_robots
for i in range(1000000):
    new_pos = []
    for robot in robots:
        px, py, vx, vy = robot
        px += vx
        py += vy
        if px < 0:
            px += wd
        if px > (wd - 1):
            px %= wd
        if py < 0:
            py += hi
        if py > (hi - 1):
            py %= hi
        new_pos.append((px, py, vx, vy))
    robots = new_pos
    poss = [(px, py) for px, py, _, _ in robots]
    if len(poss) == len(set(poss)):
        print(i + 1)
        break
