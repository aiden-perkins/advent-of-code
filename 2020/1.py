
f = open('./input.txt', 'r')
lines = f.readlines()

""" Part 1 """

for g in lines:
    for h in lines:
        if int(g) + int(h) == 2020:
            print(int(g) * int(h))

""" Part 2 """

for g in lines:
    for h in lines:
        for m in lines:
            if int(g) + int(h) + int(m) == 2020:
                print(int(g) * int(h) * int(m))