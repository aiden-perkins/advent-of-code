import math

ls = open('./input.txt').read().split('\n\n')

""" Part 1 """

ins = ls[0]
dicts = ls[1].split('\n')[:-1]
d = {}
for line in dicts:
    u = line.split(' = ')
    d[u[0]] = {'L': u[1][1:4], 'R': u[1][6:-1]}

current = 'AAA'
c = 0
while current != 'ZZZ':
    for char in ins:
        current = d[current][char]
        c += 1
print(c)

""" Part 2 """

a_list = [a for a in d.keys() if a.endswith('A')]
z_times = [0] * len(a_list)
c = 0
while 0 in z_times:
    for char in ins:
        c += 1
        for h, n in enumerate(a_list):
            v = d[n][char]
            a_list[h] = d[n][char]
            if v.endswith('Z') and z_times[h] == 0:
                z_times[h] = c
print(math.lcm(*z_times))
