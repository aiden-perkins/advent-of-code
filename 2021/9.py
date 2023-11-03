ll = open('./input.txt', 'r').readlines()

""" Part 1 """

h = []
u = []
for i in range(len(ll)-1):
    for g in range(len(ll[0])-1):
        num = int(ll[i][g])
        for (c1, c2) in [(i+1,g), (i-1,g), (i,g-1), (i,g+1)]:
            if c1 in range(len(ll)-1) and c2 in range(len(ll[0])-1):
                if ll[c1][c2] <= ll[i][g]:
                    break
        else:
            h.append(int(num))
            u.append([i, g])

total = 0
for m in h:
    total += m + 1
print(total)

""" Part 2 """

row = []
for g in ll:
    k = []
    for j in g[:-1]:
        k.append(int(j))
    row.append(k)

new = []

def basin(ind):
    if ind in new:
        return -1
    new.append(ind)
    num = row[ind[0]][ind[1]]
    d = 0
    
    if ind[0] == 99:
        bot = 9
    else:
        bot = row[ind[0] + 1][ind[1]]
    if ind[1] == 0:
        left = 9
    else:
        left = row[ind[0]][ind[1] - 1]
    if ind[1] == 99:
        right = 9
    else:
        right = row[ind[0]][ind[1] + 1]
    if ind[0] == 0:
        top = 9
    else:
        top = row[ind[0] - 1][ind[1]]
    
    if num < top and top != 9:
        d += basin([ind[0] - 1, ind[1]]) + 1
    if num < bot and bot != 9:
        d += basin([ind[0] + 1, ind[1]]) + 1
    if num < right and right != 9:
        d += basin([ind[0], ind[1] + 1]) + 1
    if num < left and left != 9:
        d += basin([ind[0], ind[1] - 1]) + 1
    return d

max = []
for o in u:
    max.append((basin(o) + 1))

mid = 1
for num in sorted(max)[len(max) - 3:]:
    mid *= num
print(mid)