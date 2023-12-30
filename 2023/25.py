from itertools import pairwise
from collections import defaultdict, deque

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

graf = defaultdict(list)
for line in ls:
    c = line[:3]
    for cnc in line[5:].split():
        graf[c].append(cnc)
        graf[cnc].append(c)

# This code uses a BFS from each node to every other node, then counts how many times each edge is used in those paths,
# this isn't guaranteed to work on all small inputs, but will for large inputs. This is because you can shift around the
# order of the values in the graph, and on smaller inputs, make it so sometimes an edge might get more flow than the top
# 3 edges just because the order happens to be in its favor. Though this only affects small inputs, so I don't really
# care, and it by chance works on the sample so yeah I'll just leave it.
all_paths = {}
for node in graf:
    seen = {node}
    q = deque([[node]])
    while q:
        c_path = q.popleft()
        for new_node in graf[c_path[-1]]:
            if new_node not in seen:
                h = hash(node) + hash(new_node)
                if h not in all_paths:
                    all_paths[h] = c_path + [new_node]
                seen.add(new_node)
                q.append(c_path + [new_node])
edge_counts_h = defaultdict(int)
for path in all_paths.values():
    for n1, n2 in pairwise(path):
        edge_counts_h[hash(n1) + hash(n2)] += 1

final = list(edge_counts_h.items())
final.sort(key=lambda x: x[1], reverse=True)
final = [a[0] for a in final[:3]]
v = None
for node in graf:
    if final:
        for child in graf[node]:
            if hash(node) + hash(child) in final:
                graf[child].remove(node)
                graf[node].remove(child)
                v = node
                final.remove(hash(node) + hash(child))
seen = {v}
q = deque([[v]])
while q:
    c_path = q.popleft()
    for new_node in graf[c_path[-1]]:
        if new_node not in seen:
            seen.add(new_node)
            q.append(c_path + [new_node])
print(len(seen) * (len(graf) - len(seen)))
