import copy
from collections import deque, defaultdict

ls = open('./input.txt').read().split('\n')[:-1]
crd_manip = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
flip = {'v': '^', '^': 'v', '<': '>', '>': '<'}

""" Part 1 """


def find_edges(current_path):
    edges = []
    x, y = current_path[-1]
    for k, (nx, ny) in crd_manip.items():
        if nx + x in range(len(ls)) and ny + y in range(len(ls[0])):
            v = ls[nx + x][ny + y]
            if v != '#' and (nx + x, ny + y) not in current_path:
                if v not in flip or flip[v] != k:
                    edges.append((nx + x, ny + y))
    return edges


completed_paths = []
paths = deque([[(0, 1)]])
while paths:
    path = paths.popleft()
    while path[-1] != (len(ls) - 1, len(ls[0]) - 2):
        ptx, pty = path[-1]
        val = ls[ptx][pty]
        while val in crd_manip.keys():
            dx, dy = crd_manip[val]
            ptx += dx
            pty += dy
            path.append((ptx, pty))
            val = ls[ptx][pty]
        new_trails = find_edges(path)
        if len(new_trails) > 1:
            for new_trail in new_trails[1:]:
                paths.append(copy.deepcopy(path) + [new_trail])
        path.append(new_trails[0])
    completed_paths.append(path)

lengths = set()
for comp_p in completed_paths:
    lengths.add(len(comp_p) - 1)
print(max(lengths))

""" Part 2 """


def find_edges(x, y):
    edges = []
    for nx, ny in crd_manip.values():
        if nx + x in range(len(ls)) and ny + y in range(len(ls[0])):
            if ls[nx + x][ny + y] != '#':
                edges.append((nx + x, ny + y))
    return edges


forest = [list(a) for a in ls]
forks = [(0, 1), (len(ls) - 1, len(ls) - 2)]
for i in range(1, len(ls) - 1):
    for j in range(1, len(ls[0]) - 1):
        if ls[i][j] != '#':
            if len(find_edges(i, j)) > 2:
                forks.append((i, j))

graf = defaultdict(dict)
for fork in forks:
    for start_edge in find_edges(*fork):
        path = [fork, start_edge]
        distance = 1
        while path[-1] not in forks:
            distance += 1
            path.append([a for a in find_edges(*path[-1]) if a not in path][0])
        graf[fork][path[-1]] = distance

mx = 0
q = deque([[0, (0, 1)]])
while q:
    current = q.popleft()
    c_node = current[-1]
    for new_node, cost in graf[c_node].items():
        if new_node not in current:
            new_cost = current[0] + cost
            q.append([new_cost] + current[1:] + [new_node])
    if c_node == (len(ls) - 1, len(ls) - 2) and current[0] > mx:
        print(mx)
        mx = current[0]
print(mx)
