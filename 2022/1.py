ll = open('./input.txt', 'r').read()[:-1].split('\n\n')
elves = []
for line in ll:
    total = 0
    i = line.split('\n')
    for num in i:
        total += int(num)
    elves.append(total)

""" Part 1 """

print(max(elves))

""" Part 2 """

one = max(elves)
elves.remove(one)
one1 = max(elves)
elves.remove(one1)
one2 = max(elves)
print(one + one1 + one2)

