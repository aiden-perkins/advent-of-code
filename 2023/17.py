import heapq
from collections import defaultdict
from math import inf

ll = [[int(g) for g in list(ii[:-1])] for ii in open('./input.txt').readlines()]

""" Part 1 """


def get_edges(node, seen, cost, start, stop):
    (px, py), vert = node
    d = [(1, 0), (-1, 0)] if vert else [(0, 1), (0, -1)]
    for dx, dy in d:
        x, y = px, py
        line_cost = 0
        for straight in range(1, stop + 1):
            x += dx
            y += dy
            if x not in range(len(ll)) or y not in range(len(ll)):
                break
            line_cost += ll[x][y]
            if straight >= start:
                if ((x, y), not vert) not in seen:
                    yield ((x, y), not vert), line_cost + cost


def find_shortest_path(start, end, min_straight_dis, max_straight_dis):
    bin_heap = [(0, (start, False)), (0, (start, True))]
    finished = {}
    min_distances = defaultdict(lambda: inf)
    while bin_heap:
        current_cost, c_node = heapq.heappop(bin_heap)
        finished[c_node] = current_cost
        for new_node, nc in get_edges(c_node, finished, current_cost, min_straight_dis, max_straight_dis):
            if nc < min_distances[new_node]:
                min_distances[new_node] = nc
                heapq.heappush(bin_heap, (nc, new_node))
    return min(min_distances[(end, True)], min_distances[(end, False)])


print(find_shortest_path((0, 0), (len(ll) - 1, len(ll) - 1), 0, 3))

""" Part 2 """

print(find_shortest_path((0, 0), (len(ll) - 1, len(ll) - 1), 4, 10))
