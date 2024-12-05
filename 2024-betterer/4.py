from itertools import product

ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

lss = len(ls)
tt = 0

for i in range(lss):
    for j in range(lss):
        for k, l in product([-1, 1, 0], repeat=2):
            s = ''
            for m in range(4):
                if i + (m * k) in range(lss) and j + (m * l) in range(lss):
                    s += ls[i + (m * k)][j + (m * l)]
            if s == 'XMAS':
                tt += 1

print(tt)
