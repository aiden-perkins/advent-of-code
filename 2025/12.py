import math

ls = open('./input.txt').read().strip().split('\n\n')

""" Part 1 """

tt = 0
presents = []

for i, ll in enumerate(ls):
    if i < 6:
        presents.append(sum(r.count('#') for r in ls[i].split('\n')[1:]))
    else:
        print(sum(1 for l in ll.split('\n') if sum(am * presents[i] for i, am in enumerate(map(int, l.split(': ')[1].split(' ')))) <= math.prod(map(int, l.split(': ')[0].split('x')))))
