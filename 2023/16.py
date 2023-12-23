from collections import deque

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

cavern = [list(a) for a in ls]
xl = len(cavern)
yl = len(cavern[0])
delta = {
    '\\': {'N': 'W', 'S': 'E', 'E': 'S', 'W': 'N'},
    '/': {'N': 'E', 'S': 'W', 'E': 'N', 'W': 'S'},
    '|': ['N', 'S'],
    '-': ['W', 'E']
}
crd_manip = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

""" Part 2 """

start_pos = []
for i in range(len(cavern)):
    start_pos.append([len(cavern) - 1, i, 'N'])
    start_pos.append([0, i, 'S'])
    start_pos.append([i, 0, 'E'])
    start_pos.append([i, len(cavern) - 1, 'W'])

mx = 0
for start in start_pos:
    lasers = deque([start])
    tv = {}
    tiles = {}
    while lasers:
        x, y, d = lasers.popleft()
        while 0 <= x < xl and 0 <= y < yl:
            vk = (x, y, d)
            tiles[(x, y)] = 1
            if vk not in tv:
                tv[vk] = 1
            else:
                break
            v = cavern[x][y]
            if v in ['\\', '/']:
                d = delta[v][d]
            elif (v == '|' and d in ['E', 'W']) or (v == '-' and d in ['N', 'S']):
                d, nd = delta[v]
                dx, dy = crd_manip[nd]
                lasers.append([x + dx, y + dy, nd])
            dx, dy = crd_manip[d]
            x += dx
            y += dy
    nmx = len(tiles)
    if nmx > mx:
        mx = nmx
    if start == [0, 0, 'E']:  # Part 1
        print(nmx)
print(mx)
