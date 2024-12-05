ll = open('./input.txt').read()

""" Part 1 """

tt = 0
possible = ll.split('mul')

for p in possible:
    ss = ''
    full = False
    fr = False
    cm = False
    for c in p:
        if c == '(':
            fr = True
        elif c.isnumeric():
            ss += c
        elif c == ',':
            ss += ' '
            cm = True
        elif c == ')':
            full = True
        else:
            break
    if full and cm and fr:
        g = [int(a) for a in ss.split()]
        tt += g[0] * g[1]

print(tt)

""" Part 2 """

tt = 0
nl = ''
do_add = True

for i in range(len(ll)):
    if i + 7 in range(len(ll)):
        word = ll[i:i+7]
        if word == 'don\'t()':
            do_add = False
        elif word.startswith('do()'):
            do_add = True
    if do_add:
        nl += ll[i]

possible = nl.split('mul')

for p in possible:
    ss = ''
    full = False
    fr = False
    cm = False
    for c in p:
        if c == '(':
            fr = True
        elif c.isnumeric():
            ss += c
        elif c == ',':
            ss += ' '
            cm = True
        elif c == ')':
            full = True
        else:
            break
    if full and cm and fr:
        g = [int(a) for a in ss.split()]
        tt += g[0] * g[1]

print(tt)
