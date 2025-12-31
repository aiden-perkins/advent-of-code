ls = list(open('./input.txt').read().strip().split('\n'))
ls1 = [a.split(' ') for a in ls]

""" Part 1 """

tt = 0

ci = [0, 0, 0, 0, 0]

for i in range(len(ls1[0])):
    vs = []
    try:
        for j in range(5):
            while ls1[j][ci[j]].strip() == '':
                ci[j] = ci[j] + 1
            vs.append(ls1[j][ci[j]])
        for j in range(5):
            ci[j] = ci[j] + 1
        tt += eval(f' {vs[-1]} '.join(map(str, vs[:-1])))
    except IndexError:
        break

print(tt)

""" Part 2 """

nums = []
allnums = []
signs = [ls[-1][0]]
tt = 0

for j in range(max(len(a) for a in ls)):
    if j + 1 in range(len(ls[-1])):
        s = ls[-1][j + 1]
    else:
        s = ' '
    if s == ' ':
        s2 = ''
        for i in range(len(ls) - 1):
            s2 += ls[i][j]
        nums.append(int(s2))
    else:
        allnums.append(nums)
        signs.append(ls[-1][j + 1])
        nums = []

allnums.append(nums)
print(sum(eval(f' {signs[e]} '.join(map(str, allnums[e]))) for e in range(len(allnums))))
