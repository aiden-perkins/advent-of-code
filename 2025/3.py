ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0

for ll in ls:
    fn = max(set(ll[:-1]))
    tt += int(fn + str(max(set(ll[ll.index(fn) + 1:]))))

print(tt)

""" Part 2 """

tt = 0

for ll in ls:
    cl = len(ll)
    nd = 12
    start = 0
    res = ''
    while nd > 0:
        end = cl - (nd - 1)
        ns = ll[start:end]
        nm = max(ns)
        pos = start + ns.index(nm)
        res += nm
        start = pos + 1
        nd -= 1
    tt += int(res)

print(tt)
