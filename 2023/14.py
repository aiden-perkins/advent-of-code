from collections import defaultdict

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """


def move_sat(sat):
    for i in range(1, len(sat)):
        for j in range(len(sat)):
            if sat[i][j] == 'O':
                e = 0
                while sat[i + e - 1][j] == '.' and i + e - 1 > -1:
                    e -= 1
                if e != 0:
                    sat[i + e][j] = 'O'
                    sat[i][j] = '.'
    return sat


satt = move_sat([list(a) for a in ls])
t = 0
for x, row in enumerate(satt):
    for y, v in enumerate(row):
        if v == 'O':
            t += (len(satt) - x)
print(t)

""" Part 2 """

same = defaultdict(int)
sattelite = [list(a) for a in ls]
while 2 not in same.values():
    for _ in range(4):
        sattelite = move_sat(sattelite)
        sattelite = [list(r) for r in zip(*sattelite[::-1])]  # Rotate it clockwise.
    same['\n'.join([''.join(a) for a in sattelite])] += 1
offset = list(same.values()).index(2)
cycle_values = list(same.keys())[offset:]
satt = [list(w) for w in (cycle_values[(1000000000 - offset - 1) % len(cycle_values)].split('\n'))]
t = 0
for x, row in enumerate(satt):
    for y, v in enumerate(row):
        if v == 'O':
            t += (len(satt) - x)
print(t)
