pos = list(int(i) for i in open('./input.txt', 'r').readlines()[0][:-1].split(','))

""" Part 1 """

def solve(part):
    t = 0
    for i in range(sorted(pos)[::-1][0] + 1):
        total = 0
        for g in pos:
            if part:
                total += abs(i - int(g))
            else:
                total += sum(range(1 + abs(i - int(g))))
        if total < t or t == 0:
            t = total
    return t

print(solve(True))

""" Part 2 """

print(solve(False))
