ls = open('./input.txt').read().strip().split('\n\n')
ls1, ls2 = ls

""" Part 1 """

tt = 0

ing = []

for ll in ls1.strip().split('\n'):
    a = ll.split('-')
    ing.append((int(a[0]), int(a[1])))

for ll in ls2.strip().split('\n'):
    a = int(ll)
    for g1 in ing:
        if a in range(g1[0], g1[1] + 1):
            tt += 1
            break

print(tt)

""" Part 2 """

tt = 0

ing.sort(key=lambda x: x[0])

while tt < len(ing) - 1:
    in1 = ing[tt]
    in2 = ing[1 + tt]
    if in2[0] <= in1[1] + 1:
        ing[tt:tt+2] = [(in1[0], max(in1[1], in2[1]))]
    else:
        tt += 1

ttt = 0

for x, y in ing:
    ttt += (y - x + 1)
print(ttt)
