ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

cards = [[set(int(a) for a in l1.split()) for l1 in line.split(':')[1].split('|')] for line in ls]
print(sum([int(2 ** (len(card[0].intersection(card[1])) - 1)) for card in cards]))

""" Part 2 """

copies = {}
for i in range(len(cards)):
    copies[i] = 1
for j, card in enumerate(cards):
    for k in range(len(card[0].intersection(card[1]))):
        if j + k + 1 in copies:
            copies[j + k + 1] += copies[j]
print(sum(copies.values()))
