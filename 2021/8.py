f = open('./input.txt', 'r')
ll = f.readlines()

""" Part 1 """

after = []
for i in ll:
    after.append([i.split(' | ')[0], i.split(' | ')[1][:-1]])
total = 0
for x in after:
    for g in x[1].split(' '):
        if len(g) in [2, 3, 4, 7]:
            total += 1
print(total)

""" Part 2 """

total = 0
for x in after:
    for g in x[0].split(' '):
        if len(g) in [2, 3, 4, 7]:
            if len(g) == 2:
                one = sorted([g[0], g[1]])
            if len(g) == 3:
                seven = sorted([g[0], g[1], g[2]])
            if len(g) == 4:
                four = sorted([g[0], g[1], g[2], g[3]])
            if len(g) == 7:
                eight = sorted([g[0], g[1], g[2], g[3], g[4], g[5], g[6]])
    for g in x[0].split(' '):
        if len(g) == 6:
            if all(x in list(g) for x in four):
                nine = sorted([g[0], g[1], g[2], g[3], g[4], g[5]])
                continue
            if not all(x in list(g) for x in one):
                six = sorted([g[0], g[1], g[2], g[3], g[4], g[5]])
            if all(x in list(g) for x in one):
                zero = sorted([g[0], g[1], g[2], g[3], g[4], g[5]])
    for g in x[0].split(' '):
        if len(g) == 5:
            if all(x in list(g) for x in one):
                three = sorted([g[0], g[1], g[2], g[3], g[4]])
                continue
            if all(x in six for x in list(g)):
                five = sorted([g[0], g[1], g[2], g[3], g[4]])
            if not all(x in six for x in list(g)):
                two = sorted([g[0], g[1], g[2], g[3], g[4]])
    str1 = ''
    for y in x[1].split(' '):
        str1 += str([zero, one, two, three, four, five, six, seven, eight, nine].index(sorted(list(y))))
    total += int(str1)
print(total)