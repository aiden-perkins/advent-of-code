ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

races = [[int(a) for a in line.split()[1:]] for line in ls]
ways = 1
for i in range(len(races[0])):
    count = 0
    for j in range(races[0][i]):
        if j * (races[0][i] - j) > races[1][i]:
            count += 1
    ways *= count
print(ways)

""" Part 2 """

time = int(ls[0].split(':')[1].replace(' ', ''))
distance = int(ls[1].split(':')[1].replace(' ', ''))
start = 0
for j in range(distance // time, time):
    if j * (time - j) > distance:
        start = j
        break
print(time - (start * 2 - 1))
