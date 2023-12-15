ls = open('./input.txt').read().split('\n\n')

""" Part 1 """

patterns = [[list(a) for a in p.split('\n')] for p in ls]
patterns[-1] = patterns[-1][:-1]


def reflection_point(ll):
    possible = set()
    for i in range(len(ll) - 1):
        # Making these variables saves me time so that's why I made them, this function gets called a lot.
        left = ll[:i + 1][::-1]
        right = ll[i + 1:]
        for j in range(min(len(right), len(left))):
            if left[j] != right[j]:
                break
        else:
            possible.add(len(left))
    return possible


t = 0
for pattern in patterns:
    c_rp = reflection_point([[row[i] for row in pattern] for i in range(len(pattern[0]))])
    r_rp = set(v * 100 for v in reflection_point(pattern))
    t += max(r_rp, c_rp).pop()
print(t)

""" Part 2 """

t = 0
for pattern in patterns:
    c_rp = reflection_point([[row[i] for row in pattern] for i in range(len(pattern[0]))])
    r_rp = set(v * 100 for v in reflection_point(pattern))
    p1_a = max(r_rp, c_rp).pop()
    possible_new = []
    for a in range(len(pattern)):
        for b in range(len(pattern[a])):
            pattern[a][b] = '.' if pattern[a][b] == '#' else '#'
            possible_new += list(reflection_point([[j[i] for j in pattern] for i in range(len(pattern[0]))]))
            possible_new += list(set(v * 100 for v in reflection_point(pattern)))
            pattern[a][b] = '.' if pattern[a][b] == '#' else '#'
    possible_new = list(set(possible_new))  # Remove duplicates
    possible_new.remove(p1_a)  # Remove the known reflection point
    t += possible_new[0]
print(t)
