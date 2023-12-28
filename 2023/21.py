from collections import deque

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

garden = [list(a) for a in ls]
s_pos_i = ''.join(ls).index('S')
positions = deque([(s_pos_i // len(garden[0]), s_pos_i % len(garden[0]))])
for _ in range(64):
    new = set()
    while positions:
        px, py = positions.popleft()
        for (x, y) in [(px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)]:
            if garden[x][y] != '#' and len(new.intersection((x, y))) == 0:
                new.add((x, y))
    positions = deque(new)
print(len(positions))

""" Part 2 """

# 💀
