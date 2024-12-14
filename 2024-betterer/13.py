import re
from fractions import Fraction

ls = open('./input.txt').read().strip().split('\n\n')

p1 = 0
p2 = 0

for machine_str in ls:
    t1 = tuple(int(s1) for s1 in re.findall(r': X=(\d+), Y=(\d+)', machine_str)[0])
    a, b = [(int(s1), int(s2)) for s1, s2 in re.findall(r': X\+(\d+), Y\+(\d+)', machine_str)]

    """ Part 1 """

    Y = Fraction(Fraction(t1[0] * a[1], a[0]) - t1[1], Fraction((b[0] * a[1]), a[0]) - b[1])
    X = Fraction(-b[0] * Y, a[0]) + Fraction(t1[0], a[0])

    if X.denominator == 1 and Y.denominator == 1:
        p1 += X * 3 + Y

    """ Part 2 """

    t2 = tuple(ot + 10000000000000 for ot in t1)
    Y = Fraction(Fraction(t2[0] * a[1], a[0]) - t2[1], Fraction((b[0] * a[1]), a[0]) - b[1])
    X = Fraction(-b[0] * Y, a[0]) + Fraction(t2[0], a[0])

    if X.denominator == 1 and Y.denominator == 1:
        p2 += X * 3 + Y

print(p1)
print(p2)
