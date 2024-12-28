ls = open('./input.txt').read().strip()
lsl = len(ls)

""" Part 1 """

tt = 0
ps = []

for i, v in enumerate(ls):
    if i % 2 == 0:
        ps += [str(i // 2)] * int(v)
    else:
        ps += ['.'] * int(v)
psl = len(ps)
ops = ps[:]

for i in range(psl):
    if i >= len(ps):
        break

    j = len(ps) - 1
    while ps[j] == '.':
        ps.pop()
        j -= 1

    num = ps[i]
    if num == '.':
        rv = ps.pop()
        tt += int(rv) * i
    else:
        tt += int(num) * i

print(tt)

""" Part 2 """

tt = 0
ps = ops[:]
i = 0
last_dot_idx = len(ps) - 1

while '.' in ps and last_dot_idx >= 0:
    i += 1

    j = last_dot_idx
    while ps[j] == '.':
        j -= 1

    first_group_num = [ps[j]]
    afgn = ps[j]
    j -= 1
    while ps[j] == afgn:
        first_group_num += [ps[j]]
        j -= 1

    last_dot_idx = j

    dot_gr = ''
    dot_gr_idx = None
    for k, v in enumerate(ps):
        if v == '.':
            if dot_gr == '':
                dot_gr_idx = k
            dot_gr += v
            if len(dot_gr) >= len(first_group_num):
                break
        else:
            dot_gr = ''

    if dot_gr_idx < j:
        for k in range(len(dot_gr)):
            ps[k + dot_gr_idx] = first_group_num[k]
            ps[j + 1 + k] = '.'

for i, v in enumerate(ps):
    if v != '.':
        tt += int(v) * i

print(tt)
