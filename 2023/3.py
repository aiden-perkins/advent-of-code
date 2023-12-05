ls = open('./input.txt', 'r').read().split('\n')[:-1]
parts = [list(line) for line in ls]

""" Part 1 """

total = 0
for i in range(len(parts)):
    nums_used = []
    for j in range(len(parts)):
        if parts[i][j].isnumeric() and j not in nums_used:
            nums_used.append(j)
            num_s = parts[i][j]
            t = 1
            while j + t in range(len(parts)) and parts[i][j+t].isnumeric():
                num_s += parts[i][j+t]
                nums_used.append(j + t)
                t += 1
            for x in range(i-1, i+2):
                for y in range(j-1, j+1+len(num_s)):
                    if x in range(len(parts)) and y in range(len(parts)):
                        if not parts[x][y].isnumeric() and parts[x][y] != '.':
                            total += int(num_s)
                            break
print(total)

""" Part 2 """

gears = {}
total = 0
for i in range(len(parts)):
    nums_used = []
    for j in range(len(parts)):
        if parts[i][j].isnumeric() and j not in nums_used:
            nums_used.append(j)
            num_s = parts[i][j]
            t = 1
            while j + t in range(len(parts)) and parts[i][j+t].isnumeric():
                num_s += parts[i][j+t]
                nums_used.append(j + t)
                t += 1
            for x in range(i-1, i+2):
                for y in range(j-1, j+1+len(num_s)):
                    if x in range(len(parts)) and y in range(len(parts)):
                        if parts[x][y] == '*':
                            if (x, y) in gears:
                                gears[(x, y)].append(int(num_s))
                            else:
                                gears[(x, y)] = [int(num_s)]
for k, v in gears.items():
    if len(v) == 2:
        total += v[0] * v[1]
print(total)
