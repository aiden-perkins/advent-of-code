from collections import *
import math

ls = open('./input.txt').read().strip().split('\n')
lsl = len(ls)

""" Part 1 """

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

tt = 0

boxes = []
distances = defaultdict(dict)

for ll in ls:
    a, b, c = map(int, ll.strip().split(','))
    boxes.append((a, b, c))

d2 = []

for i in range(len(boxes)):
    for j in range(i, len(boxes)):
        if i != j:
            a = boxes[i]
            b = boxes[j]
            d2.append((a, b, dist(a, b)))

connections = []
d2.sort(key=lambda t: t[2])

for a, b, d in d2[:1001]:
    ca = []
    cb = []
    for c, con in enumerate(connections):
        if a in con:
            ca.append(c)
        if b in con:
            cb.append(c)
    if len(ca) == 1 and len(cb) == 1:
        if ca[0] == cb[0]:
            continue
        connections[ca[0]] |= connections[cb[0]]
        connections.pop(cb[0])
    elif len(ca) == 1 and len(cb) == 0:
        connections[ca[0]].add(b)
    elif len(ca) == 0 and len(cb) == 1:
        connections[cb[0]].add(a)
    else:
        connections.append({a, b})

print(eval(' * '.join(map(str, sorted([len(c) for c in connections], reverse=True)[:3]))))


""" Part 2 """

t = 0
for a, b, d in d2:
    t += 1
    ca = []
    cb = []
    for c, con in enumerate(connections):
        if a in con:
            ca.append(c)
        if b in con:
            cb.append(c)
    if len(ca) == 1 and len(cb) == 1:
        if ca[0] == cb[0]:
            continue
        connections[ca[0]] |= connections[cb[0]]
        connections.pop(cb[0])
    elif len(ca) == 1 and len(cb) == 0:
        connections[ca[0]].add(b)
    elif len(ca) == 0 and len(cb) == 1:
        connections[cb[0]].add(a)
    else:
        connections.append({a, b})
    if len(connections) == 1 and len(connections[0]) == 1000:
        print(a[0] * b[0])
        break
