ls = open('./input.txt', 'r').read().split('\n')[:-1]
posd = {
    'U': [1, 0],
    'D': [-1, 0],
    'L': [0, -1],
    'R': [0, 1],
}
moves = [(posd[g.split(' ')[0]], int(g.split(' ')[1])) for g in ls]

""" Part 1 """

hpos = [0, 0]
tpos = [0, 0]
places = []
for (where, amount) in moves:
    for i in range(amount):
        hpos[0] += where[0]
        hpos[1] += where[1]
        if tpos[0] in [hpos[0]+1, hpos[0]-1, hpos[0]] and tpos[1] in [hpos[1]+1, hpos[1]-1, hpos[1]]:
            continue
        else:
            if hpos[0] > tpos[0]:
                tpos[0] += 1
            if hpos[0] < tpos[0]:
                tpos[0] -= 1
            if hpos[1] > tpos[1]:
                tpos[1] += 1
            if hpos[1] < tpos[1]:
                tpos[1] -= 1
        if str(tpos) not in places:
            places.append(str(tpos))

print(len(places)+1)

""" Part 2 """

amount_of_knots = 9
knots = {}
places = []
for x in range(amount_of_knots + 1):
    knots[x] = (0, 0)
for (where, amount) in moves:
    for i in range(amount):
        for knot in knots:
            if knot == 0:
                knots[knot] = (knots[knot][0]+where[0], knots[knot][1]+where[1])
                continue
            if knots[knot][0] in [knots[knot-1][0]+1, knots[knot-1][0]-1, knots[knot-1][0]] and knots[knot][1] in [knots[knot-1][1], knots[knot-1][1]-1, knots[knot-1][1]+1]:
                continue
            else:
                if knots[knot-1][0] > knots[knot][0]:
                    knots[knot] = (knots[knot][0]+1, knots[knot][1])
                if knots[knot-1][0] < knots[knot][0]:
                    knots[knot] = (knots[knot][0]-1, knots[knot][1])
                if knots[knot-1][1] > knots[knot][1]:
                    knots[knot] = (knots[knot][0], knots[knot][1]+1)
                if knots[knot-1][1] < knots[knot][1]:
                    knots[knot] = (knots[knot][0], knots[knot][1]-1)
            if knot == amount_of_knots:
                if knots[knot] not in places:
                    places.append(knots[knot])
print(len(places)+1)

