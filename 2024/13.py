from sympy import *
from sympy.solvers.solveset import linsolve
from sympy.core import numbers

ls = open('./input.txt').read().strip().split('\n\n')

""" Part 1 """

tt = 0

for machine_str in ls:
    lls = machine_str.strip().split('\n')
    xy_str = lls[2].split('=')[1:]
    xy_str[0] = xy_str[0][:-3]
    tx, ty = [int(a) for a in xy_str]

    btn_a = lls[0].split('+')[1:]
    btn_a = (int(btn_a[0][:-3]), int(btn_a[1]))

    btn_b = lls[1].split('+')[1:]
    btn_b = (int(btn_b[0][:-3]), int(btn_b[1]))

    min_cost = None
    for i in range(1, 101):
        for j in range(1, 101):
            x_ep = (btn_a[0] * i) + (btn_b[0] * j)
            y_ep = (btn_a[1] * i) + (btn_b[1] * j)
            if (tx, ty) == (x_ep, y_ep):
                if min_cost is None or min_cost > ((i*3)+j):
                    min_cost = ((i*3)+j)
    if min_cost:
        tt += min_cost

print(tt)

""" Part 2 """

tt = 0

for machine_str in ls:
    lls = machine_str.strip().split('\n')
    xy_str = lls[2].split('=')[1:]
    xy_str[0] = xy_str[0][:-3]
    tx, ty = [int(a) + 10000000000000 for a in xy_str]

    btn_a = lls[0].split('+')[1:]
    btn_a = (int(btn_a[0][:-3]), int(btn_a[1]))

    btn_b = lls[1].split('+')[1:]
    btn_b = (int(btn_b[0][:-3]), int(btn_b[1]))

    M = Matrix(((btn_a[0], btn_b[0], tx), (btn_a[1], btn_b[1], ty)))
    out = list(linsolve((M[:, :-1], M[:, -1]), *symbols('x, y, z')))[0]
    if isinstance(out[0], numbers.Integer) and isinstance(out[1], numbers.Integer):
        tt += out[0] * 3 + out[1]

print(tt)
