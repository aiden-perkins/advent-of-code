from itertools import product, repeat

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

steps = []
small_steps = []
mx = 0
for line in ls:
    rs = [True if line.split()[0] == 'on' else False] + [tuple(map(int, r[2:].split('..'))) for r in line.split()[1].split(',')]
    steps.append(rs)
    for v in [rs[1][0], rs[1][1], rs[2][0], rs[2][1], rs[3][0], rs[3][1]]:
        if abs(v) > mx:
            mx = abs(v)
        if abs(v) > 50:
            break
    else:
        small_steps.append(rs)
print(mx)

""" Part 2 """

