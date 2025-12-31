ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 50
ttt = 0

for ll in ls:
    p = ll[0]
    o = int(ll[1:])
    if p == 'R':
        tt = tt + o
    if p == 'L':
        tt = tt - o

    tt %= 100

    if tt == 0:
        ttt += 1

print(ttt)

""" Part 2 """

tt = 50
ttt = 0

for ll in ls:
    p = ll[0]
    o = int(ll[1:])
    if p == 'R':
        if tt == 100:
            tt = 0
        tt = tt + o
    if p == 'L':
        if tt == 0:
            tt = 100
        tt = tt - o

    if tt > 99:
        ttt += tt // 100
    elif tt < 0:
        ttt += (abs(tt) // 100) + 1
    elif tt == 0:
        ttt += 1

    if tt != 100 and tt != 0:
        tt %= 100

print(ttt)
