h = list(i[:-1].split('-') for i in open('./input.txt', 'r').readlines())

""" Part 1 """

dic = {}
for x in range(len(h)):
    for y in range(len(h[0])):
        dic[h[x][y]] = []
for x in range(len(h)):
    for y in range(len(h[0])):
        dic[h[x][y]].append(h[x][y+1] if y == 0 else h[x][y-1])

def lower_check1(p, bb):
    return p not in bb

def path(char, ll, part):
    total = 0
    for y in dic[char]:
        mm = []
        mm += ll
        if y != 'start':
            if y == 'end':
                mm.append('end')
                total += 1
            else:
                if not y.isupper():
                    if (lower_check2(y, mm) and part == 2) or (lower_check1(y, mm) and part == 1):
                        mm.append(y)
                        total += path(y, mm, part)
                else:
                    mm.append(y)
                    total += path(y, mm, part)
    return total

def main(part):
    total = 0
    for item in dic['start']:
        ll = ['start', item]
        total += path(item, ll, part)
    print(total)

""" Part 2 """

def lower_check2(p, bb):
    v = True
    for u in bb:
        if not u.isupper() and u != 'start' and u != 'end':
            if bb.count(u) > 1:
                if p in bb:
                    v = False
    return v

main(1)
main(2)
