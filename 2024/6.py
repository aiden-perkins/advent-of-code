ls = open('./input.txt').read().strip().split('\n')

move = {
    '^': lambda x: (x[0] - 1, x[1]),
    '>': lambda x: (x[0], x[1] + 1),
    'v': lambda x: (x[0] + 1, x[1]),
    '<': lambda x: (x[0], x[1] - 1),
}
mk = list(move.keys())

p = ''.join(ls).index('^')
opx, opy = p // len(ls[0]), p % len(ls[0])
ls[opx] = ls[opx].replace('^', '.')

""" Part 1 """

cv = '^'
px, py = opx, opy
poss = {(px, py)}

while 0 <= px < len(ls) and 0 <= py < len(ls):
    npx, npy = move[cv]((px, py))
    if 0 > npx or npx >= len(ls) or 0 > npy or npy >= len(ls):
        break
    if ls[npx][npy] == '#':
        cv = mk[(mk.index(cv) + 1) % 4]
    else:
        poss.add((npx, npy))
        px, py = npx, npy

print(len(poss))

""" Part 2 """

tt = 0

for i, j in poss:
    if ls[i][j] != '#':

        ls[i] = ls[i][:j] + '#' + ls[i][j+1:]
        cv = '^'
        px, py = opx, opy
        places = set()

        while 0 <= px < len(ls) and 0 <= py < len(ls):
            if (px, py, cv) in places:
                tt += 1
                break
            places.add((px, py, cv))
            npx, npy = move[cv]((px, py))
            if 0 > npx or npx >= len(ls) or 0 > npy or npy >= len(ls):
                break
            if ls[npx][npy] == '#':
                cv = mk[(mk.index(cv) + 1) % 4]
            else:
                px, py = npx, npy

        ls[i] = ls[i][:j] + '.' + ls[i][j+1:]

print(tt)
