ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

maze = [list(a) for a in ls]
s_pos_i = ''.join(ls).index('S')
sx = s_pos_i // len(maze[0])
sy = s_pos_i % len(maze[0])

# Solving for what the start position should actually be
sides = []
for idx, direction in zip([(sx + 1, sy), (sx - 1, sy), (sx, sy + 1), (sx, sy - 1)], ['S', 'N', 'E', 'W']):
    if maze[idx[0]][idx[1]] in {'W': 'LF-', 'E': '7J-', 'N': '7F|', 'S': 'LJ|'}[direction]:
        sides.append(direction)
maze[sx][sy] = {'SN': '|', 'EW': '-', 'SW': '7', 'NW': 'J', 'SE': 'F', 'NE': 'L'}[''.join(sides)]

# Making the pipe loop
new_direction = {
    '-': {'E': 'E', 'W': 'W'},
    '|': {'N': 'N', 'S': 'S'},
    'J': {'S': 'W', 'E': 'N'},
    'L': {'S': 'E', 'W': 'N'},
    '7': {'N': 'W', 'E': 'S'},
    'F': {'N': 'E', 'W': 'S'}
}
# special = {
#     '7': '┓',
#     'F': '┏',
#     'J': '┛',
#     'L': '┗',
#     '-': '━',
#     '|': '┃',
# }
side_switch = {
    'J': {'W': 'N', 'E': 'S', 'N': 'W', 'S': 'E'},
    'F': {'W': 'N', 'E': 'S', 'N': 'W', 'S': 'E'},
    'L': {'W': 'S', 'E': 'N', 'N': 'E', 'S': 'W'},
    '7': {'W': 'S', 'E': 'N', 'N': 'E', 'S': 'W'},
}
crd_manip = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
cx, cy = sx, sy
c_loop = set()
a1d, a2d = {'S': ['W', 'E'], 'N': ['W', 'E'], 'W': ['N', 'S'], 'E': ['N', 'S']}[sides[0]]  # Part 2 code
a1_loop, a2_loop = set(), set()  # Part 2 code
while len(c_loop) == 0 or (cx, cy) != (sx, sy):
    a1_loop.add((cx + crd_manip[a1d][0], cy + crd_manip[a1d][1]))  # Part 2 code
    a2_loop.add((cx + crd_manip[a2d][0], cy + crd_manip[a2d][1]))  # Part 2 code
    c_loop.add((cx, cy))
    cx, cy = (lambda m: (cx + m[0], cy + m[1]))(crd_manip[sides[0]])
    old = maze[cx][cy]
    sides[0] = new_direction[old][sides[0]]
    if old in 'LF7J':  # Part 2 code
        a1_loop.add((cx + crd_manip[a1d][0], cy + crd_manip[a1d][1]))  # Part 2 code
        a2_loop.add((cx + crd_manip[a2d][0], cy + crd_manip[a2d][1]))  # Part 2 code
        a1d = side_switch[old][a1d]  # Part 2 code
        a2d = side_switch[old][a2d]  # Part 2 code
    # maze[cx][cy] = special[old]  # Uncomment this and the dictionary above for a cool visual
print(len(c_loop) // 2)

""" Part 2 """

hit_a1_c = 0
hit_a2_c = 0
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if (i, j) not in c_loop:
            w, z = i, j
            while (w, z) not in a1_loop and (w, z) not in a2_loop and w > -1:
                w -= 1
            if (w, z) not in a1_loop and (w, z) in a2_loop:
                hit_a2_c += 1
            if (w, z) in a1_loop and (w, z) not in a2_loop:
                hit_a1_c += 1
# The answer to part 2 is probably the smallest of these 2 values, however there can be extreme cases where this isn't
# true, but given all the test inputs, my input, and inputs from other people I have seen, this should never happen.
print(min(hit_a1_c, hit_a2_c))
