ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

def calc_result(tv, cv, other_val):
    if len(other_val) == 0:
        return tv == cv
    return calc_result(tv, cv * other_val[0], other_val[1:]) or calc_result(tv, cv + other_val[0], other_val[1:])

tt = 0

for ll in ls:
    ans, vs = ll.strip().split(': ')
    ans = int(ans)
    vs = [int(a) for a in vs.split(' ')]
    if calc_result(ans, vs[0], vs[1:]):
        tt += ans

print(tt)

""" Part 2 """

def calc_result_p2(tv, cv, other_val):
    if len(other_val) == 0:
        return tv == cv
    return calc_result_p2(tv, cv * other_val[0], other_val[1:]) or \
        calc_result_p2(tv, cv + other_val[0], other_val[1:]) or \
        calc_result_p2(tv, int(str(cv) + str(other_val[0])), other_val[1:])

tt = 0

for ll in ls:
    ans, vs = ll.strip().split(': ')
    ans = int(ans)
    vs = [int(a) for a in vs.split(' ')]
    if calc_result_p2(ans, vs[0], vs[1:]):
        tt += ans

print(tt)
