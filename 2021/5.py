from collections import Counter

f = open('../input.txt', 'r')
lines = f.readlines()

""" Part 1 """

def loop(do_diag):
    moves = []
    crd = []
    for i in lines:
        i = i[:-1]
        x1, y1, x2, y2 = (int(x) for x in ','.join(i.split(' -> ')).split(','))
        if (do_diag is True) or (x1 == x2 or y1 == y2):
            moves.append(((x1, y1), (x2, y2)))

    for (x1, y1), (x2, y2) in moves:
        total_diff = (x2 - x1) + (y2 - y1)
        a = 1 if total_diff > 0 else -1
        total_diff += 1 if total_diff > 0 else -1
        for i in range(0, total_diff, a):
            if x1 == x2:
                crd.append((x1, y1 + i))
            if y1 == y2:
                crd.append((x1 + i, y1))

        if do_diag is True:
            total_diff = x2 - x1
            a = 1 if total_diff > 0 else -1
            total_diff += 1 if total_diff > 0 else -1
            for i in range(0, total_diff, a):
                if x1 < x2 and y1 != y2:
                    if y1 < y2:
                        crd.append((x1 + i, y1 + i))
                    else:
                        crd.append((x1 + i, y1 - i))
                elif x1 != x2 and y1 != y2:
                    if y1 < y2:
                        crd.append((x1 + i, y1 - i))
                    else:
                        crd.append((x1 + i, y1 + i))

    c = Counter(crd)
    print(len([x for (x,y) in c.items() if y>1]))

loop(False)

""" Part 2 """

loop(True)