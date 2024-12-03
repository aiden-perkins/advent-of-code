ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

total = 0
ms = []
ml = []

for ll in ls:
    o, t = ll.split('   ')
    ms.append(int(o))
    ml.append(int(t))

ms.sort()
ml.sort()

for i in range(len(ms)):
    total += abs(ml[i] - ms[i])

print(total)

""" Part 2 """

nt = 0
for v in ms:
    nt += v * ml.count(v)

print(nt)
