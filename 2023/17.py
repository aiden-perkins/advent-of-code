import heapq

ll = [[int(g) for g in list(ii[:-1])] for ii in open('./input.txt').readlines()]

""" Part 1 """


class Node:
    def __init__(self, pos, cost) -> None:
        self.pos = pos
        self.cost = cost
        self.distance = -1

    def __lt__(self, a):
        return self.distance < a.distance


def get_edges(pos, edge, finished):
    e = []
    if pos[0] < edge and (pos[0] + 1, pos[1]) not in finished:
        e.append((pos[0] + 1, pos[1]))
    if pos[1] < edge and (pos[0], pos[1] + 1) not in finished:
        e.append((pos[0], pos[1] + 1))
    if pos[0] > 0 and (pos[0] - 1, pos[1]) not in finished:
        e.append((pos[0] - 1, pos[1]))
    if pos[1] > 0 and (pos[0], pos[1] - 1) not in finished:
        e.append((pos[0], pos[1] - 1))
    return e


def find_shortest_path(map_area, start, end):
    finished = {}
    current_pos = start
    map_area[current_pos].distance = 0
    heap = []
    heapq.heapify(heap)
    while len(finished) != len(map_area):
        for next_location in get_edges(current_pos, len(ll) - 1, finished):
            next_node = map_area[next_location]
            if map_area[current_pos].distance + next_node.cost < next_node.distance or next_node.distance == -1:
                next_node.distance = map_area[current_pos].distance + next_node.cost
                heapq.heappush(heap, next_node)
        finished[current_pos] = map_area[current_pos].distance
        if current_pos == end:
            return finished[end]
        current_pos = heapq.heappop(heap).pos


city = {}
for x, row in enumerate(ll):
    for y, num in enumerate(row):
        city[(x, y)] = Node((x, y), num)
print(find_shortest_path(city, (0, 0), (len(ll) - 1, len(ll) - 1)))
# TODO: Add the 3 same direction constraint, dunno how I am going to do that but this is a basic shortest path finder.

""" Part 2 """
