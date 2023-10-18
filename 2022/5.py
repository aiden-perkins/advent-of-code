ls = open('./input.txt', 'r').read()[:-1].split('\n\n')
moves = [[int(move.split(' from ')[0].split(' ')[1]), int(move.split(' from ')[1].split(' to ')[0]), int(move.split(' from ')[1].split(' to ')[1])] for move in ls[1].split('\n')]
crates = dict.fromkeys([int(char) for char in ls[0].split('\n')[len(ls[0].split('\n')) - 1].replace(' ', '')], '')
for line in ls[0].split('\n')[:-1]:
    lll = [line[i:i+4] for i in range(0, len(line), 4)]
    for y in range(len(lll)):
        if lll[y][1] != ' ':
            crates[y+1] =  lll[y][1] + crates[y+1]

""" Part 1 """

p1 = dict(crates)
for mv in moves:
    for i in range(mv[0]):
        p1[mv[2]] = p1[mv[2]] + p1[mv[1]][(len(p1[mv[1]]) - 1)]
        p1[mv[1]] = p1[mv[1]][:-1]

print(''.join([p1[g][(len(p1[g]) - 1)] for g in p1]))

""" Part 2 """

p2 = dict(crates)
for mv in moves:
    p2[mv[2]] = p2[mv[2]] + p2[mv[1]][-mv[0]:]
    p2[mv[1]] = p2[mv[1]][:-mv[0]]

print(''.join([p2[g][(len(p2[g]) - 1)] for g in p2]))
