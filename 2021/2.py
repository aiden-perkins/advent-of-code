f = open('./input.txt', 'r')
lines = f.readlines()

""" Part 1 """

depth = 0
horizontal = 0
for i in lines:
    i = i[:-1]
    if 'forward' in i:
        horizontal += int(i[-1])
    if 'down' in i:
        depth += int(i[-1])
    if 'up' in i:
        depth -= int(i[-1])
print(horizontal * depth)

""" Part 2 """

aim = 0
depth = 0
horizontal = 0
for i in lines:
    i = i[:-1]
    v = int(i[-1])
    if 'down' in i:
        aim += v
    if 'up' in i:
        aim -= v
    if 'forward' in i:
        horizontal += v
        depth += v * aim
print(horizontal * depth)