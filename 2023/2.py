from functools import reduce
import operator

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

games = [line.split(':')[1] for line in ls]
t = 0
for game_num, game in enumerate(games):
    ck = {'red': 12, 'green': 13, 'blue': 14}
    add = True
    for color in ck.keys():
        while color in game:
            i = game.index(color)
            if int(game[i - 3:i]) > ck[color]:
                add = False
            game = game[0:i - 3] + game[i + len(color):]
    if add:
        t += game_num + 1
print(t)

""" Part 2 """

t = 0
for game_num, game in enumerate(games):
    ck = {'red': 0, 'green': 0, 'blue': 0}
    for color in ck.keys():
        while color in game:
            i = game.index(color)
            if int(game[i - 3:i]) > ck[color]:
                ck[color] = int(game[i - 3:i])
            game = game[0:i - 3] + game[i + len(color):]
    t += reduce(operator.mul, ck.values(), 1)
print(t)
