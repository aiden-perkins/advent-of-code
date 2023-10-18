lines = open('../input.txt', 'r').readlines()
dra = lines[0][:-1]
lines.pop(0)
lines.pop(0)

""" Part 1 """

def calculate(h, v):
    for i in dra.split(','):
        if i in h:
            h.remove(i)
        if i == v:
            break
    las = 0
    for o in h:
        las += int(o)
    return las * int(v)

def board_check(board):
    dr = []
    low = 0
    lowest = 0
    y = 0
    for j in range(0, 5):
        f = j * 5
        row = []
        colum = []
        for g in range(0 + f, 5 + f):
            row.append(board[g])
        for g in range(0, 5):
            colum.append(board[g * 5 + j])
        for i in dra.split(','):
            dr.append(i)
            low += 1
            if all(item in dr for item in row) is True:
                break
        if low < lowest or lowest == 0:
            lowest = low
            y = i
        dr = []
        low = 0
        for i in dra.split(','):
            dr.append(i)
            low += 1
            if all(item in dr for item in colum) is True:
                break
        if low < lowest or lowest == 0:
            lowest = low
            y = i
        dr = []
        low = 0
    return lowest, y

def start(win_lose):
    board = []
    c = 0          
    m = 0
    v = 0
    final = 0
    for i in lines:
        c += 1
        for x in i.replace('\n', '').split(' '):
            if x != '':
                int(x)
                board.append(x)
        if c == 6:
            if ((board_check(board)[0] < m or m == 0) and win_lose == True) or ((board_check(board)[0] > m) and win_lose == False):
                m, v = board_check(board)
                final = calculate(board, v)
            board = []
            c = 0
    print(final)

start(True)

""" Part 2 """

start(False)
