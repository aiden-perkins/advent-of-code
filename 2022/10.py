ls = open('./input.txt', 'r').read().split('\n')[:-1]

""" Part 1 """

x = 1
lsi = 0
doline = True
t = 0
for cycle in range(220):
    if cycle+1 in [20, 60, 100, 140, 180, 220]:
        t += (cycle+1) * x
    if doline:
        if ls[lsi].startswith('noop'):
            lsi += 1
        elif ls[lsi].startswith('addx'):
            lsi += 1
            doline = False
    else:
        doline = True
        x += int(ls[lsi-1].split(' ')[1])
print(t)
        
""" Part 2 """

x = 1
lsi = 0
doline = True
pos = ['', '', '', '', '', '']
for i in range(240):
    if i%40 in [x+1, x-1, x]:
        pos[i//40] += '⬜'
    else:
        pos[i//40] += '⬛'
    if doline:
        if ls[lsi].startswith('noop'):
            lsi += 1
        elif ls[lsi].startswith('addx'):
            lsi += 1
            doline = False
    else:
        doline = True
        x += int(ls[lsi-1].split(' ')[1])
    
for m in pos:
    print(m)
