ls = open('./input.txt').read().strip().split('\n\n')
ls1 = ls[0].strip().split('\n')
ls2 = ls[1].strip().split('\n')

""" Part 1 """

gates = {
    'AND': lambda x: int(x[0] == 1 and x[1] == 1),
    'OR': lambda x: int(x[0] == 1 or x[1] == 1),
    'XOR': lambda x: int(x[0] != x[1]),
}

vrs = {0: 0, 1: 1}
for ip in ls1:
    ip = ip.split(': ')
    vrs[ip[0]] = int(ip[1])

targets = {}
for ll in ls2:
    ll = ll.strip().split()
    targets[ll[4]] = (ll[0], ll[2], ll[1])


def ev_gt(req1, req2, g):
    if req1 not in vrs:
        req1 = ev_gt(*targets[req1])
    if req2 not in vrs:
        req2 = ev_gt(*targets[req2])
    return gates[g]((vrs[req1], vrs[req2]))


res = {}
for t in targets:
    if t.startswith('z'):
        res[t] = str(ev_gt(*targets[t]))

res = [a[1] for a in sorted(list(res.items()))]
print(str(int(''.join(res[::-1]), base=2)))

""" Part 2 """

fin = {}

for ll in ls2:
    ll = ll.strip().split()
    fin[(ll[0], ll[2], ll[1])] = ll[4]
    fin[(ll[2], ll[0], ll[1])] = ll[4]

carry = fin[('x00', 'y00', 'AND')]

to_swap = [
    # ('rpv', 'z11'),
    # ('rpb', 'ctg'),
    # ('z31', 'dmh'),
    # ('z38', 'dvq')
]

for s1, s2 in to_swap:
    bs11, bs12, bs13 = targets[s1]
    bs21, bs22, bs23 = targets[s2]
    fin[(bs11, bs12, bs13)] = s2
    fin[(bs12, bs11, bs13)] = s2
    fin[(bs21, bs22, bs23)] = s2
    fin[(bs22, bs21, bs23)] = s1
    targets[s1] = (bs11, bs12, bs13)
    targets[s2] = (bs21, bs22, bs23)

for i in range(1, 45):

    xi = 'x' + '{:02}'.format(i)
    yi = 'y' + '{:02}'.format(i)
    zi = 'z' + '{:02}'.format(i)

    found = []
    to_find = [
        (xi, yi, 'XOR'),
        (xi, yi, 'AND'),
        ('found[0]', carry, 'AND'),
        ('found[1]', 'found[2]', 'OR'),
        ('found[0]', carry, 'XOR'),
    ]

    for t1, t2, t3 in to_find:
        tp = (eval(t1) if t1.startswith('found') else t1, eval(t2) if t2.startswith('found') else t2, t3)
        if tp in fin:
            found.append(fin[tp])
        else:
            found.append('BAD')

    z1, z2, z3 = targets[zi]

    if 'BAD' in found:
        print(f'            └ {carry} ┐┌ XOR -> {found[4]} (this should be {zi})')
        print(f'{xi} ┬┬ XOR -> {found[0]} ┴┴ AND -> {found[2]} ┐')
        print(f'{yi} ┘└ AND -> {found[1]} ──────────────┴ OR -> {found[3]} ┐')
        # if not found[3].startswith('z'):
        #     print('            ┌───────────────────────────────┘ ')
        # uncomment the above 2 lines and move lines 93-97 outside the if statement for a visual of the ripple adder.
        print(f'Stopping because bad wires, zXX: {z1} {z3} {z2} -> {zi}')
        break

    carry = found[3]

    if found[3] == 'z45':
        print(','.join(sorted(sum([[a, b] for a, b in to_swap], []))))

# This does not solve the problem automatically, you have to manually look at
# the outputted bad wires, identify which to swap, and then manually type the
# wires to swap. I want to make this automatic in the future but this is how I
# got the answer initially so I will just leave it here and put the real
# solution in 2024-betterer. This solution also assumes the first and last bit
# in the ripple adder from the input are always correct, which was true for my
# input but may not be true for all inputs.
