import sympy
from itertools import combinations

ls = open('./input.txt').read().split('\n')[:-1]
bl = 200000000000000
bh = 400000000000000

""" Part 1 """

hail_balls = [tuple(int(a) for a in line.replace(' @', ',').split(',')) for line in ls]
equations = {}
for x, y, z, vx, vy, vz in hail_balls:
    equations[(vy/vx, y - (vy/vx) * x)] = (x, y, z, vx, vy, vz)

t = 0
for (m, b), (m2, b2) in combinations(equations.keys(), 2):
    if m != m2:
        x_intersect = (b2 - b) / (m - m2)
        y_intersect = m * x_intersect + b
        x, _, _, vx, _, _ = equations[(m, b)]
        x2, _, _, vx2, _, _ = equations[(m2, b2)]
        if (vx // abs(vx) == -1 and x_intersect < x) or (vx // abs(vx) == 1 and x_intersect > x):
            if (vx2 // abs(vx2) == -1 and x_intersect < x2) or (vx2 // abs(vx2) == 1 and x_intersect > x2):
                if bl <= x_intersect <= bh and bl <= y_intersect <= bh:
                    t += 1
print(t)

""" Part 2 """

rx, ry, rz, rvx, rvy, rvz = sympy.symbols('rx, ry, rz, rvx, rvy, rvz')
equations = []
for x, y, z, vx, vy, vz in hail_balls[:4]:
    equations.append((rx - x) * (vy - rvy) - (ry - y) * (vx - rvx))
    equations.append((ry - y) * (vz - rvz) - (rz - z) * (vy - rvy))
print(sum(list(sympy.solve(equations)[0].values())[-3:]))
