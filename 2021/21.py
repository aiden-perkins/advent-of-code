ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

p1 = int(ls[0][-2:])
p1s = 0
p2 = int(ls[1][-2:])
p2s = 0
die = 1
dr = 0


def n(current):
    v = 0
    for _ in range(3):
        if current == 100:
            current = 0
        v += current
        current += 1
    return v, current


while p2s < 1000:
    mv = n(die)
    die = mv[1]
    p1 += mv[0]
    p1 = ((p1 - 1) % 10) + 1
    p1s += p1
    dr += 3
    if p1s > 999:
        break
    mv = n(die)
    die = mv[1]
    p2 += mv[0]
    p2 = ((p2 - 1) % 10) + 1
    p2s += p2
    dr += 3
print(p1s * dr)
print(p2s * dr)

""" Part 2 """

