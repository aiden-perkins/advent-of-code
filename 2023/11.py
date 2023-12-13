import copy
from collections import defaultdict

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

inter = [list(ll) for ll in ls]
new_i = []
clm = defaultdict(list)
for j, row in enumerate(inter):
    if '#' not in row:
        new_i.append(copy.deepcopy(row))
    new_i.append(copy.deepcopy(row))
columns = defaultdict(list)
for row in new_i:
    for i in range(len(row)):
        columns[i].append(row[i])
double_c = []
for k in columns:
    if '#' not in columns[k]:
        double_c.append(k)
for i in range(len(new_i)):
    for v in double_c[::-1]:
        new_i[i].insert(v, '.')
galaxy_pos = set()
for x, row in enumerate(new_i):
    for y, g in enumerate(row):
        if g == '#':
            galaxy_pos.add((x, y))
mn = {}
for g_pos in galaxy_pos:
    for g_pos2 in galaxy_pos:
        if (g_pos, g_pos2) not in mn and (g_pos2, g_pos) not in mn and g_pos2 != g_pos:
            mn[(g_pos, g_pos2)] = ((abs(g_pos2[0] - g_pos[0])) + (abs(g_pos2[1] - g_pos[1])))
print(sum(mn.values()))

""" Part 2 """

double_r = []
for j, row in enumerate(inter):
    if '#' not in row:
        double_r.append(j)
columns = defaultdict(list)
for row in inter:
    for i in range(len(row)):
        columns[i].append(row[i])
double_c = []
for k in columns:
    if '#' not in columns[k]:
        double_c.append(k)
galaxy_pos = set()
for x, row in enumerate(inter):
    for y, g in enumerate(row):
        if g == '#':
            galaxy_pos.add((x, y))
mn = {}
for g_pos in galaxy_pos:
    for g_pos2 in galaxy_pos:
        if (g_pos, g_pos2) not in mn and (g_pos2, g_pos) not in mn and g_pos2 != g_pos:
            v = ((abs(g_pos2[0] - g_pos[0])) + (abs(g_pos2[1] - g_pos[1])))
            for er in double_r:
                if g_pos[0] < er < g_pos2[0] or g_pos2[0] < er < g_pos[0]:
                    v += 999999
            for ec in double_c:
                if g_pos[1] < ec < g_pos2[1] or g_pos2[1] < ec < g_pos[1]:
                    v += 999999
            mn[(g_pos, g_pos2)] = v
print(sum(mn.values()))
