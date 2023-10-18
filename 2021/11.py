h = list(list(int(d) for d in i[:-1]) for i in open('../input.txt', 'r').readlines())

""" Part 1 """

def flash(g, k):
    total = 0
    for (x, y) in [(g+1,k), (g-1,k), (g,k+1), (g,k-1), (g+1,k+1), (g-1,k-1), (g-1,k+1), (g+1,k-1)]:
        if x in range(len(h)) and y in range(len(h[0])):
            if h[x][y] == 9:
                h[x][y] = 0
                total += flash(x, y) + 1
            elif h[x][y] == 0:
                h[x][y] = 0
            else:
                h[x][y] += 1
    return total
def step():
    total = 0
    o = []
    for g in range(len(h)):
        for k in range(len(h[0])):
            if h[g][k] == 9:
                h[g][k] = 0
                o.append([g, k])
            else:
                h[g][k] += 1
    for item in o:
        total += flash(item[0], item[1]) + 1
    return total
def main(steps):
    f = 0
    for y in range(steps):
        f += step()
    print(f)
main(100)

""" Part 2 """

z = 0
while True:
    z += 1
    if step() == 100:
        print(z + 100)  # adding 100 because we already did 100 steps above
        break
