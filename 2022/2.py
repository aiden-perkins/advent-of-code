ls = [ii[:-1] for ii in open('./input.txt', 'r').readlines()]

""" Part 1 """

map = {'X': 1,'Y': 2,'Z': 3}
map2 = {'A': 'X', 'B': 'Y', 'C': 'Z'}
score = 0
for round in ls:
    me = round.split(' ')[1]
    them = round.split(' ')[0]
    score += map[me]
    if map2[them] == me:
        score += 3
    else:
        if (them == 'A' and me == 'Z') or (them == 'B' and me == 'X') or (them == 'C' and me == 'Y'):
            continue
        elif (them == 'A' and me == 'Y') or (them == 'B' and me == 'Z') or (them == 'C' and me == 'X'):
            score += 6
    
print(score)

""" Part 2 """

score = 0
map3 = {'X': 0, 'Y': 3, 'Z': 6}
win = {'A': 2, 'B': 3, 'C': 1}
lose = {'A': 3, 'B': 1, 'C': 2}
for round in ls:
    me = round.split(' ')[1]
    them = round.split(' ')[0]
    score += map3[me]
    if me == 'Y':
        score += map[map2[them]]
    else:
        if me == 'Z':
            score += win[them]
        elif me == 'X':
            score += lose[them]
            
print(score)
