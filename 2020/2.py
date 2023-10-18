f = open('../input.txt', 'r')
lines = f.readlines()

""" Part 1 """

g = []
for i in lines:
    g.append(i[:-1].split(' '))
total = 0
for m in g:
    h = m[0].split('-')
    ls = []
    for x in range(int(h[0]), int(h[1]) + 1):
        ls.append(x)
    if m[2].count(m[1][:-1]) in ls:
        total += 1
print(total)

""" Part 2 """

g = []
for i in lines:
    g.append(i[:-1].split(' '))
total = 0
for m in g:
    h = m[0].split('-')
    if (m[2][int(h[0]) - 1] == m[1][:-1] and m[2][int(h[1]) - 1] != m[1][:-1]) or (m[2][int(h[0]) - 1] != m[1][:-1] and m[2][int(h[1]) - 1] == m[1][:-1]):
        total += 1
print(total)