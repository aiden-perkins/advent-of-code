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


forks = [(0, 1), (len(ls) - 1, len(ls) - 2)]
for i in range(1, len(ls) - 1):
    for j in range(1, len(ls[0]) - 1):
        if ls[i][j] != '#':
            if len(find_edges(i, j)) > 2:
                forks.append((i, j))

converter = {}
for i, f in enumerate(forks):
    converter[f] = 2 ** (i + 1)

graf = defaultdict(list)
for fork in forks:
    for start_edge in find_edges(*fork):
        path = [fork, start_edge]
        distance = 1
        while path[-1] not in forks:
            distance += 1
            path.append([a for a in find_edges(*path[-1]) if a not in path][0])
        graf[converter[fork]].append((converter[path[-1]], distance))

end_vertex = converter[(len(ls) - 1, len(ls) - 2)]
stack = [(converter[(0, 1)], 0, 0)]
max_distance = 0

while stack:
    current_vertex, cost, seen = stack.pop()
    seen |= current_vertex
    if current_vertex == end_vertex:
        if cost > max_distance:
            max_distance = cost
    for next_vertex, next_cost in graf[current_vertex]:
        if next_vertex & seen:
            continue
        stack.append((next_vertex, cost + next_cost, seen))

print(max_distance)  # Takes about 10 seconds.
