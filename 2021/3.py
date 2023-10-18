lines = open('./input.txt', 'r').readlines()

""" Part 1 """

str1 = ''
str2 = ''
for x in range(0, len(lines[0])-1):
    c = 0
    u = 0
    for i in lines:
        if i[x] == '1':
            c += 1
        if i[x] == '0':
            u += 1
    if u > c:
        str1 += '0'
        str2 += '1'
    else:
        str1 += '1'
        str2 += '0'
print(int(str1, 2) * int(str2, 2))

""" Part 2 """

def t(h, j):
    for x in range(0, len(lines[0])-1):
        u = 0
        c = 0
        g = lines
        k = []
        for i in g:
            if i[x] == h:
                c += 1
            if i[x] == j:
                u += 1
        if u == c:
            if h == '0':
                c -= 1
            else:
                u -= 1
        if u < c:
            for i in g:
                if i[x] == '1':
                    k.append(i)
        else:
            for i in g:
                if i[x] == '0':
                    k.append(i)
        if len(g) == 1:
            break
    return g
print(int(t('1', '0')[0][:-1], 2) * int(t('0', '1')[0][:-1], 2))