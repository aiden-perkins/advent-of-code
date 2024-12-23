from functools import *

lss = open('./input.txt').read().strip().split('\n\n')
ls1 = [a.strip() for a in lss[1].split('\n')]
ls2 = [a.strip() for a in lss[0].split(', ')]

""" Part 1 """

@cache
def works(current):
    if current == '':
        return True
    for p in ls2:
        if current.startswith(p) and works(current[len(p):]):
            return True
    return False

tt = 0

for design in ls1:
    if works(design):
        tt += 1

print(tt)

""" Part 2 """

@cache
def works(current):
    if current == '':
        return 1
    nrv = 0
    for p in ls2:
        if current.startswith(p):
            nrv += works(current[len(p):])
    return nrv

tt = 0

for design in ls1:
    tt += works(design)

print(tt)
