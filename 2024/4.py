ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

lss = len(ls)
tt = 0

for i in range(lss):
    for j in range(lss):
        if ls[i][j] == 'X':
            # right
            if i + 3 in range(lss):
                word = f'{ls[i][j]}{ls[i+1][j]}{ls[i+2][j]}{ls[i+3][j]}'
                if word == 'XMAS':
                    tt += 1
            # right down
            if i + 3 in range(lss) and j + 3 in range(lss):
                word = f'{ls[i][j]}{ls[i+1][j+1]}{ls[i+2][j+2]}{ls[i+3][j+3]}'
                if word == 'XMAS':
                    tt += 1
            # right up
            if i + 3 in range(lss) and j - 3 in range(lss):
                word = f'{ls[i][j]}{ls[i+1][j-1]}{ls[i+2][j-2]}{ls[i+3][j-3]}'
                if word == 'XMAS':
                    tt += 1
            # left
            if i - 3 in range(lss):
                word = f'{ls[i][j]}{ls[i-1][j]}{ls[i-2][j]}{ls[i-3][j]}'
                if word == 'XMAS':
                    tt += 1
            # left down
            if i - 3 in range(lss) and j + 3 in range(lss):
                word = f'{ls[i][j]}{ls[i-1][j+1]}{ls[i-2][j+2]}{ls[i-3][j+3]}'
                if word == 'XMAS':
                    tt += 1
            # left up
            if i - 3 in range(lss) and j - 3 in range(lss):
                word = f'{ls[i][j]}{ls[i-1][j-1]}{ls[i-2][j-2]}{ls[i-3][j-3]}'
                if word == 'XMAS':
                    tt += 1
            # up
            if j - 3 in range(lss):
                word = f'{ls[i][j]}{ls[i][j-1]}{ls[i][j-2]}{ls[i][j-3]}'
                if word == 'XMAS':
                    tt += 1
            # down
            if j + 3 in range(lss):
                word = f'{ls[i][j]}{ls[i][j+1]}{ls[i][j+2]}{ls[i][j+3]}'
                if word == 'XMAS':
                    tt += 1

print(tt)

""" Part 2 """

tt = 0

for i in range(1, lss - 1):
    for j in range(1, lss - 1):
        if ls[i][j] == 'A':
            vs = [ls[i+1][j+1], ls[i-1][j+1], ls[i-1][j-1], ls[i+1][j-1]]
            if vs.count('M') == 2 and vs.count('S') == 2 and vs[0] != vs[2] and vs[1] != vs[3]:
                tt += 1

print(tt)
