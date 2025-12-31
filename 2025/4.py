from helpers import *

ls = open('./input.txt').read().strip().split('\n')
lsl = len(ls)

""" Part 1 """

tt = 0

for i in range(lsl):
    for j in range(lsl):
        if ls[i][j] == '@':
            sr = 0
            for v, _ in value_traverse(i, j, ls):
                if v == '@':
                    sr += 1
            if sr < 4:
                tt += 1
print(tt)

""" Part 2 """

for i in range(lsl):
    ls[i] = list(ls[i])

tt = 0
ch = True
while ch:
    ch = False
    for i in range(lsl):
        for j in range(lsl):
            if ls[i][j] == '@':
                sr = 0
                for v, _ in value_traverse(i, j, ls):
                    if v == '@':
                        sr += 1
                if sr < 4:
                    ls[i][j] = '.'
                    tt += 1
                    ch = True
print(tt)
