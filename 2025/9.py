ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0
recs = []

for ll in ls:
    a, b = map(int, ll.split(','))
    recs.append((a, b))

for i in range(len(recs)):
    for j in range(i + 1, len(recs)):
        p1 = recs[i]
        p2 = recs[j]
        nd = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        if nd > tt:
            tt = nd

print(tt)

""" Part 2 """

tt = 0

for i in range(len(recs)):
    a = recs[i]
    for j in range(i + 1, len(recs)):
        b = recs[j]
        nd = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if nd > tt:
            for k in range(len(recs)):
                t1 = recs[k]
                t2 = recs[(k + 1) % len(recs)]

                xmin = min(a[0], b[0])
                ymin = min(a[1], b[1])
                xmax = max(a[0], b[0])
                ymax = max(a[1], b[1])

                xtmin = min(t1[0], t2[0])
                ytmin = min(t1[1], t2[1])
                xtmax = max(t1[0], t2[0])
                ytmax = max(t1[1], t2[1])

                if t1[0] == t2[0]:
                    if xmin < t1[0] < xmax:
                        if max(ymin, ytmin) < min(ymax, ytmax):
                            break
                elif t1[1] == t2[1]:
                    if ymin < t1[1] < ymax:
                        if max(xmin, xtmin) < min(xmax, xtmax):
                            break
            else:
                mid_x = (a[0] + b[0]) / 2 + 0.05
                mid_y = (a[1] + b[1]) / 2 + 0.05
                inside = False
                p1x, p1y = recs[0]
                for l in range(1, len(recs) + 1):
                    p2x, p2y = recs[l % len(recs)]
                    if min(p1y, p2y) < mid_y <= max(p1y, p2y) and mid_x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (mid_y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or mid_x <= xinters:
                                inside = not inside
                    p1x, p1y = p2x, p2y
                if inside:
                    tt = nd

print(tt)
