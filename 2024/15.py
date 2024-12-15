from helpers import *

ls = open('./input.txt').read().strip().split('\n\n')
lsl = len(ls)
dk = {
    '>': lambda x: (x[0], x[1] + 1),
    'v': lambda x: (x[0] + 1, x[1]),
    '<': lambda x: (x[0], x[1] - 1),
    '^': lambda x: (x[0] - 1, x[1]),
}
warehouse = [list(a) for a in ls[0].strip().split('\n')]
new_warehouse = []
for i in range(len(warehouse)):
    cl = []
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '.':
            cl.append('.')
            cl.append('.')
        elif warehouse[i][j] == 'O':
            cl.append('[')
            cl.append(']')
        elif warehouse[i][j] == '#':
            cl.append('#')
            cl.append('#')
        elif warehouse[i][j] == '@':
            cl.append('@')
            cl.append('.')
    new_warehouse.append(cl)

""" Part 1 """

moves = ''.join(ls[1].strip().split('\n'))
ix, iy = list(find_val(warehouse, lambda x: x == '@'))[0]
tt = 0

cx, cy = ix, iy
for move in moves:
    nx1, ny1 = dk[move]((cx, cy))
    nx, ny = nx1, ny1
    while warehouse[nx][ny] == 'O':
        nx, ny = dk[move]((nx, ny))
    if warehouse[nx][ny] == '.':
        warehouse[nx][ny] = 'O'
        warehouse[cx][cy] = '.'
        warehouse[nx1][ny1] = '@'
        cx, cy = nx1, ny1

for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == 'O':
            tt += (100 * i) + j

print(tt)

""" Part 2 """

ix, iy = list(find_val(new_warehouse, lambda x: x == '@'))[0]
cx, cy = ix, iy
tt = 0

for move in moves:
    if move in '<>':
        nx1, ny1 = dk[move]((cx, cy))
        nx, ny = nx1, ny1
        to_move = []
        while new_warehouse[nx][ny] in ['[', ']']:
            nx, ny = dk[move]((nx, ny))
            to_move.append((nx, ny))
        if new_warehouse[nx][ny] == '.':
            new_warehouse[nx].pop(ny)
            new_warehouse[cx].insert(cy, '.')
            cx, cy = nx1, ny1
    else:
        nx1, ny1 = dk[move]((cx, cy))
        nx, ny = nx1, ny1
        heads = [(nx, ny, new_warehouse[nx][ny])]
        all_heads = []
        if new_warehouse[nx][ny] == ']':
           heads.append((nx, ny - 1, '['))
        if new_warehouse[nx][ny] == '[':
            heads.append((nx, ny + 1, ']'))
        all_heads += heads
        vals = [new_warehouse[ax][ay] for ax, ay, _ in heads]
        fail = False
        while (vals.count(']') > 0 or vals.count('[') > 0) and not fail:
            nh = []
            for hx, hy, _ in heads:
                phx, phy = dk[move]((hx, hy))
                nv = new_warehouse[phx][phy]
                if nv == '[':
                    nh.append((phx, phy, '['))
                    nh.append((phx, phy + 1, ']'))
                elif nv == ']':
                    nh.append((phx, phy, ']'))
                    nh.append((phx, phy - 1, '['))
                elif nv == '#':
                    fail = True
                    break
            heads = nh
            all_heads += nh
            vals = [new_warehouse[ax][ay] for ax, ay, _ in heads]
        change = -1 if move == '^' else 1
        if not fail and new_warehouse[cx + change][cy] != '#':
            for mhx, mhy, hv in all_heads:
                if hv != '.':
                    new_warehouse[mhx][mhy] = '.'
            for mhx, mhy, hv in all_heads:
                if hv != '.':
                    new_warehouse[mhx + change][mhy] = hv
            new_warehouse[cx + change][cy] = '@'
            new_warehouse[cx][cy] = '.'
            cx = cx + change

for i in range(len(new_warehouse)):
    for j in range(len(new_warehouse[i])):
        if new_warehouse[i][j] == '[':
            tt += (100 * i) + j

print(tt)

