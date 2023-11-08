ls = open('./input.txt', 'r').read().split(', ')

""" Part 1 """

max_v = abs(int(ls[1].split('..')[0].split('=')[1]))
print(sum(range(1, max_v)))

""" Part 2 """

x1 = int(ls[0].split('..')[0].split('x=')[1])
x2 = int(ls[0].split('..')[1])
y1 = int(ls[1].split('..')[0].split('=')[1])
y2 = int(ls[1].split('..')[1][:-1])
possible_x = []
for i in range(x1):
    x_coords = []
    steps = list(range(i + 1))
    for j in range(1, len(steps)):
        x_coords.append(sum(steps[len(steps) - j:]))
    for x_c in x_coords:
        if x_c in range(x1, x2 + 1) and i not in possible_x:
            possible_x.append(i)
points = [(a, b) for a in range(x1, x2 + 1) for b in list(range(y1, y2 + 1))]
for p_x in possible_x:
    for p_y in range(y2 + 1, max_v):
        x = p_x
        y = p_y
        s_x = p_x - 1
        s_y = p_y - 1
        while x <= x2 and y >= y1:
            if x in range(x1, x2 + 1) and y in list(range(y1, y2 + 1)):
                if (p_x, p_y) not in points:
                    points.append((p_x, p_y))
            x += s_x
            y += s_y
            if s_x != 0:
                s_x -= 1 * (s_x // abs(s_x))
            s_y -= 1
print(len(points))
