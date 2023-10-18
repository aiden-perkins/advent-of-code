f = open('../input.txt', 'r')
lines = f.readlines()

""" Part 1 """

dic = {'(': ')', '[': ']', '{': '}', '<': '>'}
dict2 = {')': 3, ']': 57, '}': 1197, '>': 25137}
h = []


for i in lines:
    i = i[:-1]
    u = []
    for m in i:
        u.append(m)
    h.append(u)
total = 0
k = []
for line in h:
    v = True
    while v:
        v = False
        ppp = []
        for sign in range(len(line)):
            try:
                if len(line) != sign + 1:
                    if dic[line[sign]] == line[sign + 1]:
                        v = True
                        ppp.append([sign, sign + 1])
            except KeyError:
                pass
        ppp = ppp[::-1]
        for item in ppp:
            line.pop(item[1])
            line.pop(item[0])
    r = True
    for i in line:
        if not i in dic:
            total += dict2[i]
            r = False
            break
    if r:
        k.append(line)
        

print(total)

""" Part 2 """

dic2 = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for it in k:
    z = 0
    it = it[::-1]
    for piece in it:
        z *= 5
        z += dic2[dic[piece]]
    scores.append(z)

print(sorted(scores)[int(len(scores) / 2 - .5)])
