import re

ls = open('./input.txt').read().strip().split(',')

""" Part 1 """

tt = 0

for ll in ls:
    a, b = map(int, ll.split('-'))
    for i in range(a, b + 1):
        si = str(i)
        if si[0:len(si) // 2] == si[len(si) // 2:]:
            tt += i

print(tt)

""" Part 2 """

tt = 0

for ll in ls:
    a, b = map(int, ll.split('-'))
    for i in range(a, b + 1):
        if bool(re.fullmatch(r'(.+)\1+', str(i))):
            tt += i

print(tt)


# a potential faster way may be to just get all of them from the min to the max,
# then just check if they are in any of the ranges, as there doesn't seem to be many invalid
