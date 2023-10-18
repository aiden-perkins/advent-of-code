ll = [ii[:-1].split(',') for ii in open('./input.txt', 'r').readlines()]
dic = {'x': 0, 'y': 1}
folds = []
for i in ll:
    if i[0].startswith('fold'):
        folds.append((dic[i[0].split(' ')[2].split('=')[0]], int(i[0].split(' ')[2].split('=')[1])))
        ll = ll[:-1]
ll = [[int(x), int(y)] for [x, y] in ll[:-1]]

""" Part 1 """

old = ll
p1 = []
for (a, p) in folds:
    new = []
    for m in old:
        if m[a] > p:
            newc = p - (m[a] - p)
            if a == 0:
                new.append((newc, m[1]))
            else:
                new.append((m[0], newc))
        else:
            new.append((m[0], m[1]))
    old = new
    if folds.index((a, p)) == 0:
        p1 += new
t = 0
for crd in p1:
    if p1.count(crd) > 1:
        t += 0.5
print(int(len(p1) - t))

""" Part 2 """

for i in range(max(old)[1] + 1):
    strx = ''
    for oo in range(max(old)[0] + 1):
        if (oo, i) in old:
            strx += '⬜'
        else:
            strx += '⬛'
    print(strx)
