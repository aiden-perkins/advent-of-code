import functools

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """


@functools.cache
def poss_from_ss(row, broken, building):
    if not row:  # Check if we have solved all broken springs.
        return 1 if len(broken) == 0 or (len(broken) == 1 and broken[0] == 0) else 0
    first = row[0]
    if first == '?':  # Expand the possibilities
        return poss_from_ss('#' + row[1:], broken, building) + poss_from_ss('.' + row[1:], broken, building)
    elif first == '#':
        if len(broken) > 0 and broken[0] > 0:  # We might have a broken spring section, lets continue.
            return poss_from_ss(row[1:], (broken[0]-1, *broken[1:]), True)
    elif first == '.':
        if len(broken) > 0 and broken[0] == 0:  # Start checking the next broken spring.
            return poss_from_ss(row[1:], broken[1:], False)
        elif len(broken) == 0 or not building:  # We might be done, advance to next row.
            return poss_from_ss(row[1:], broken, False)
    return 0


t = 0
for line in ls:
    broken_springs = tuple(int(a) for a in line.split()[1].split(','))
    t += poss_from_ss(line.split()[0], broken_springs, False)
print(t)

""" Part 2 """

t = 0
for line in ls:
    line = line.split()
    o_row = '?'.join([line[0] for _ in range(5)])
    o_broken = tuple(int(a) for a in ','.join([line[1] for _ in range(5)]).split(','))
    t += poss_from_ss(o_row, o_broken, False)
print(t)
