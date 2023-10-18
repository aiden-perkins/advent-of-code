import time
ls = open('./input.txt', 'r').read().split('\n')[:-1]

""" Part 1 """

start_time = time.time()
cavern = []
for line in ls:
    cavern.append([int(i) for i in line])

class Node:
    def __init__(self, pos, prev):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.prev = prev
        self.distance = -1

queue = [Node([x, y], []) for x in range(len(cavern)) for y in range(len(cavern[0]))]
finished = []

def should_i_go_here(loc):
    for node in finished:
        if node.pos == loc:
            return False
    return True

def get_node(loc):
    for node in queue:
        if node.pos == loc:
            return node

def get_possible_locations(loc):
    m = []
    if loc[1] < len(cavern[loc[0]]) - 1 and should_i_go_here([loc[0], loc[1]+1]):
        m.append([loc[0], loc[1]+1])
    if loc[1] > 0 and should_i_go_here([loc[0], loc[1]-1]):
        m.append([loc[0], loc[1]-1])
    if loc[0] < len(cavern) - 1 and should_i_go_here([loc[0]+1, loc[1]]):
        m.append([loc[0]+1, loc[1]])
    if loc[0] > 0 and should_i_go_here([loc[0]-1, loc[1]]):
        m.append([loc[0]-1, loc[1]])
    return m

queue[0].distance = 0
while queue != []:
    for location in get_possible_locations(queue[0].pos):
        node = get_node(location)
        node.prev = [queue[0].pos] + queue[0].prev
        if node.distance == -1 or node.distance > queue[0].distance + cavern[location[0]][location[1]]:
            node.distance = cavern[location[0]][location[1]] + queue[0].distance
            queue.remove(node)
            for i in range(1, len(queue)):
                current = queue[i]
                if current.distance == -1 or node.distance < current.distance:
                    queue.insert(i, node)
                    break
            else:
                queue.append(node)
    removed = queue.pop(0)
    finished.append(removed)

# try switching to binary heap
# if thats too hard, change how often i use a for loop just to find the node

for node in finished:
    if node.pos == [len(cavern) - 1, len(cavern[0]) - 1]:
        print(f'{node.pos} has distance {node.distance}')
print(f'Took {time.time() - start_time} seconds')

""" Part 2 """
