ls = [ii[:-1] for ii in open('./input.txt', 'r').readlines()]

""" Part 1 """

c = 0
for pair in ls:
    m = pair.split(',')
    if (int(m[0].split('-')[0]) <= int(m[1].split('-')[0])) and (int(m[0].split('-')[1]) >= int(m[1].split('-')[1])):
        c += 1
    elif (int(m[0].split('-')[0]) >= int(m[1].split('-')[0])) and (int(m[0].split('-')[1]) <= int(m[1].split('-')[1])):
        c += 1
print(c)

""" Part 2 """

c = 0
for pair in ls:
    m = pair.split(',')
    if int(m[0].split('-')[0]) <= int(m[1].split('-')[0]) and (int(m[0].split('-')[1]) >= int(m[1].split('-')[0])):
        c += 1
    elif int(m[0].split('-')[0]) >= int(m[1].split('-')[0]) and int(m[0].split('-')[0]) <= int(m[1].split('-')[1]):
        c += 1
print(c)