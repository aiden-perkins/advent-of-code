import copy
import math
from itertools import repeat
from collections import deque

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

ff = {}
conj = {}
bc = []
for line in ls:
    line = line.split(' -> ')
    dest = line[1].split(', ')
    if line[0] == 'broadcaster':
        bc = dest
        continue
    mtype = line[0][:1]
    if mtype == '&':
        conj[line[0][1:]] = [{}, dest]
    if mtype == '%':
        ff[line[0][1:]] = [False, dest]
for k, v in list(conj.items()) + list(ff.items()):
    for d in v[1]:
        if d in conj:
            conj[d][0][k] = False


def press_button(broadcaster, flipflop, conjunction, middle_4):
    lw = 1
    hg = 0
    m4_high = []
    pulses = deque(zip(broadcaster, repeat(False, len(broadcaster)), repeat('b', len(broadcaster))))
    while pulses:
        pulse = pulses.popleft()
        if pulse[1]:
            hg += 1
        else:
            lw += 1
        if pulse[0] == 'rx':
            continue
        if pulse[2] in middle_4 and pulse[1]:
            m4_high.append(pulse[2])
        if pulse[0] in flipflop:
            if not pulse[1]:
                old = flipflop[pulse[0]][0]
                flipflop[pulse[0]][0] = not old
                for destination in flipflop[pulse[0]][1]:
                    pulses.append((destination, not old, pulse[0]))
        if pulse[0] in conjunction:
            conjunction[pulse[0]][0][pulse[2]] = pulse[1]
            new_p = True
            if False not in conjunction[pulse[0]][0].values():
                new_p = False
            for destination in conjunction[pulse[0]][1]:
                pulses.append((destination, new_p, pulse[0]))
    return lw, hg, m4_high


high = 0
low = 0
p2_conj = copy.deepcopy(conj)
p2_ff = copy.deepcopy(ff)
for _ in range(1000):
    press = press_button(bc, ff, conj, [])
    low += press[0]
    high += press[1]
print(high * low)

""" Part 2 """

i4 = []
final = ''
for k, v in p2_conj.items():
    if 'rx' in v[1]:
        final = k
for k, v in p2_conj.items():
    if final in v[1]:
        i4.append(k)
c = 0
a = []
while len(a) < 4:
    c += 1
    p = press_button(bc, p2_ff, p2_conj, i4)[2]
    if len(p) > 0:
        a.append(c)
print(math.lcm(*a))
