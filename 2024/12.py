import heapq
from helpers import *

ls = open('./input.txt').read().strip().split('\n')
lsl = len(ls)

""" Part 1 """

tt = 0
pos = set()

for i in range(lsl):
    for j in range(lsl):
        if (i, j) not in pos:
            v = ls[i][j]
            nodes = [(i, j)]
            current_area = {(i, j)}
            bad_ar = set()
            while nodes:
                x, y = heapq.heappop(nodes)
                pos.add((x, y))
                current_area.add((x, y))
                for v2, ncrd in value_traverse(x, y, ls, diag=False):
                    if ncrd not in current_area and ncrd not in nodes:
                        if v == v2:
                            heapq.heappush(nodes, ncrd)
                        else:
                            bad_ar.add(ncrd)
            perm = 0
            for a, b in current_area:
                for crdv2 in traverse(a, b, diag=False):
                    if crdv2 in bad_ar:
                        perm += 1
                if a == 0 or a == lsl - 1:
                    perm += 1
                if b == 0 or b == lsl - 1:
                    perm += 1
            tt += perm * len(current_area)

print(tt)

""" Part 2 """

tt = 0
pos = set()

for i in range(lsl):
    for j in range(lsl):
        if (i, j) not in pos:
            v = ls[i][j]
            nodes = [(i, j)]
            current_area = {(i, j)}
            bad_ar = set()

            while nodes:
                x, y = heapq.heappop(nodes)
                pos.add((x, y))
                current_area.add((x, y))
                for v2, ncrd in value_traverse(x, y, ls, diag=False):
                    if ncrd not in current_area and ncrd not in nodes:
                        if v == v2:
                            heapq.heappush(nodes, ncrd)
                        else:
                            bad_ar.add(ncrd)

            outside = set()
            for a, b in current_area:
                for crdv2 in traverse(a, b):
                    if crdv2 not in current_area:
                        outside.add(crdv2)
            corners = 0

            for rot in range(4):

                outside = {(-y, x) for x, y in outside}
                current_area = {(-y, x) for x, y in current_area}

                x_min = min([x for x, _ in outside])
                y_min = min([y for _, y in outside])
                x_max = max([x for x, _ in outside])
                y_max = max([y for _, y in outside])

                for x in range(x_min + 1, x_max):
                    prev_counted = False
                    for y in range(y_min + 1, y_max):
                        if (x, y) in current_area and (x - 1, y) in outside and not prev_counted:
                            prev_counted = True
                            corners += 1
                        elif (x, y) not in current_area or (x - 1, y) in current_area:
                            prev_counted = False

            tt += corners * len(current_area)

print(tt)

"""
(time (for i in {1..10}; do python -m 2024.12; done)) 2>&1 | grep real | awk '{print $2}' | awk '{s+=$1} END {print s/10}'




When this was first released, I wrote the code below to solve it to get an
answer, however, there is a rare bug where it will over count the corners on a
hole in a group of letters, luckily it only happened once and I could find where
it happened during the time so I just manually adjusted my answer to get the
star, but it means this code/approach doesn't work (it's also really really bad)

            dlts = {
                'N': lambda p1, p2: (p1 - 1, p2),
                'E': lambda p1, p2: (p1, p2 + 1),
                'S': lambda p1, p2: (p1 + 1, p2),
                'W': lambda p1, p2: (p1, p2 - 1),
            }
            wtg = {
                (-1, 0): 'S',
                (0, 1): 'W',
                (1, 0): 'N',
                (0, -1): 'E',
            }
            heir = {
                ('E', 'N'): 'N',
                ('E', 'S'): 'E',
                ('N', 'W'): 'W',
                ('S', 'W'): 'S',
            }
            kdlts = list(dlts.keys())
            visited = set()
            ori_outside = list(outside)
            outside = sorted(list(outside))
            while len(visited) < len(ori_outside):
                cpx, cpy = outside[0]
                spx, spy = outside[0]
                current_direction = 'N'
                path_taken = []
                visited.add((cpx, cpy))
                possible_moves = tuple(sorted([wtg[(cpx - dpx, cpy - dpy)] for dpx, dpy in set(traverse(cpx, cpy, diag=False)).intersection(outside)]))
                if possible_moves in heir:
                    current_direction = heir[possible_moves]
                    current_direction = kdlts[(kdlts.index(current_direction) - 1) % 4]
                else:
                    t = [(cpx - dpx, cpy - dpy) for dpx, dpy in set(traverse(cpx, cpy, diag=False)).intersection(current_area)]
                    if len(t) in [4, 1]:
                        t = kdlts[(kdlts.index(wtg[t[0]]) - 1) % 4]
                        current_direction = t
                    else:
                        bad_tups = []
                        tups_to_dir = [wtg[a] for a in t]
                        for d1, d2 in combinations(tups_to_dir, 2):
                            td = tuple(sorted([d1, d2]))
                            if td not in heir:
                                bad_tups.append(d1)
                                bad_tups.append(d2)
                        for bt in tups_to_dir:
                            if bt not in bad_tups:
                                current_direction = kdlts[(kdlts.index(bt) + 1) % 4]
                        t = kdlts[(kdlts.index(current_direction) - 1) % 4]
                        current_direction = t
                loop = False
                while not path_taken or (cpx, cpy) != (spx, spy):
                    new_direction = kdlts[(kdlts.index(current_direction) + 1) % 4]
                    ptx, pty = dlts[new_direction](cpx, cpy)
                    spin = 0
                    while (ptx, pty) not in outside:
                        new_direction = kdlts[(kdlts.index(new_direction) - 1) % 4]
                        ptx, pty = dlts[new_direction](cpx, cpy)
                        spin += 1
                        if spin > 3:
                            loop = True
                            break
                    if loop:
                        break
                    if spin == 3:
                        corners += 1
                    current_direction = new_direction
                    cpx, cpy = ptx, pty
                    visited.add((cpx, cpy))
                    path_taken.append(current_direction)
                if loop:
                    corners += 4
                else:
                    for u in range(len(path_taken) - 1):
                        if path_taken[u] != path_taken[u + 1]:
                            corners += 1
                    if path_taken[-1] != path_taken[0]:
                        corners += 1
                outside = sorted(list(set(outside).difference(visited)))
"""
