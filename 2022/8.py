import numpy
ls = [ii[:-1] for ii in open('./input.txt', 'r').readlines()]

""" Part 1 """

t = 0
for y in range(len(ls)):
    for x in range(len(ls[0])):
        if y in [0, len(ls)-1] or x in [0, len(ls)-1]:
            t += 1
            continue
        for u in range(y-1, -1, -1):
            if int(ls[y][x]) <= int(ls[u][x]):
                break
        else:
            t += 1
            continue
        for d in range(y+1, len(ls)):
            if int(ls[y][x]) <= int(ls[d][x]):
                break
        else:
            t += 1
            continue
        for l in range(x-1, -1, -1):
            if int(ls[y][x]) <= int(ls[y][l]):
                break
        else:
            t += 1
            continue
        for r in range(x+1, len(ls)):
            if int(ls[y][x]) <= int(ls[y][r]):
                break
        else:
            t += 1
            continue
print(t)

""" Part 2 """

high = 0
for y in range(len(ls)):
    for x in range(len(ls[0])):
        t = [0, 0, 0, 0]
        for u in range(y-1, -1, -1):
            t[0] += 1
            if int(ls[y][x]) <= int(ls[u][x]):
                break
        for d in range(y+1, len(ls)):
            t[1] += 1
            if int(ls[y][x]) <= int(ls[d][x]):
                break
        for l in range(x-1, -1, -1):
            t[2] += 1
            if int(ls[y][x]) <= int(ls[y][l]):
                break
        for r in range(x+1, len(ls)):
            t[3] += 1
            if int(ls[y][x]) <= int(ls[y][r]):
                break
        if numpy.prod(t) > high:
            high = numpy.prod(t)
print(high)
