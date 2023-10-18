ls = [ii[:-1] for ii in open('./input.txt', 'r').readlines()]

""" Part 1 """

total = 0
for line in ls:
    for char in line[:(len(line)//2)]:
        if char in line[(len(line)//2):]:
            if char.islower():
                total += (ord(char)-96)
            else:
                total += (ord(char)-38)
            break
print(total)

""" Part 2 """

total = 0
for group in [ls[n:n+3] for n in range(0, len(ls), 3)]:
    for badge in group[0]:
        if badge in group[1] and badge in group[2]:
            if badge.islower():
                total += (ord(badge)-96)
            else:
                total += (ord(badge)-38)
            break
print(total)
