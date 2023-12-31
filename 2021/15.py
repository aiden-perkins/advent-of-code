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
        for next_location in get_edges(current_pos, (len(map_area) ** (1 / 2)) - 1, finished):
            next_node = map_area[next_location]
            if map_area[current_pos].distance + next_node.cost < next_node.distance or next_node.distance == -1:
                next_node.distance = map_area[current_pos].distance + next_node.cost
                heapq.heappush(heap, next_node)
        finished[current_pos] = map_area[current_pos].distance
        if current_pos == end:
            return finished[end]
        current_pos = heapq.heappop(heap).pos


cavern = {}
for x, row in enumerate(ll):
    for y, num in enumerate(row):
        cavern[(x, y)] = Node((x, y), num)
print(find_shortest_path(cavern, (0, 0), ((len(cavern) ** (1 / 2)) - 1, (len(cavern) ** (1 / 2)) - 1)))

""" Part 2 """

cavern = {}
for i in range(len(ll) * 5):
    for j in range(len(ll[0]) * 5):
        num = (ll[i % len(ll)][j % len(ll)] + ((i // len(ll)) + (j // len(ll)))) % 9
        if num == 0:
            num = 9
        cavern[(i, j)] = Node((i, j), int(num))

# May take a few seconds.
print(find_shortest_path(cavern, (0, 0), ((len(cavern) ** (1 / 2)) - 1, (len(cavern) ** (1 / 2)) - 1)))
