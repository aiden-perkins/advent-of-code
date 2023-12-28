import copy
from collections import deque

ls = open('./input.txt').read().split('\n\n')
ls[-1] = ls[-1][:-1]

""" Part 1 """

workflows = {}
for line in ls[0].split('\n'):
    line = line.split('{')
    name = line[0]
    rules = []
    for r_s in line[1][:-1].split(','):
        nr = r_s.split(':')
        if len(nr) == 1:
            rules.append(nr[0])
        else:
            rules.append((nr[0], nr[1]))
    workflows[name] = rules
t = 0
for line in ls[1].split('\n'):
    line = line[1:-1].split(',')
    part = {'x': int(line[0][2:]), 'm': int(line[1][2:]), 'a': int(line[2][2:]), 's': int(line[3][2:])}
    dest = 'in'
    while dest not in ['A', 'R']:
        new_wf = workflows[dest]
        for flow in new_wf[:-1]:
            if '<' in flow[0]:
                if part[flow[0][:1]] < int(flow[0][2:]):
                    dest = flow[1]
                    break
            if '>' in flow[0]:
                if part[flow[0][:1]] > int(flow[0][2:]):
                    dest = flow[1]
                    break
        else:
            dest = new_wf[-1]
    if dest == 'A':
        t += sum(part.values())
print(t)

""" Part 2 """

t = 0
not_leaf = deque([['in', [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]]])
while not_leaf:
    r = not_leaf.popleft()
    if r[0] in ['A', 'R']:
        if r[0] == 'A':
            prd = 1
            for rng in r[1]:
                prd *= rng[1] - rng[0] + 1
            t += prd
        continue
    new_wf = workflows[r[0]]
    for flow in new_wf[:-1]:
        sign = flow[0][1:2]
        v = int(flow[0][2:])
        l_i = ['x', 'm', 'a', 's'].index(flow[0][:1])
        new_r = copy.deepcopy(r)
        new_r[0] = flow[1]
        if sign == '<':
            new_r[1][l_i][1] = v - 1
            r[1][l_i][0] = v
        if sign == '>':
            new_r[1][l_i][0] = v + 1
            r[1][l_i][1] = v
        not_leaf.append(new_r)
    r[0] = new_wf[-1]
    not_leaf.append(r)
print(t)
