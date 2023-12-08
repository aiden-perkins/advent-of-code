from collections import Counter

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

hand_bets = [[line.split()[0], int(line.split()[1])] for line in ls]
strength = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
hand_types = {5: [], 4: [], 'fh': [], 3: [], 'tp': [], 2: [], 1: []}
for hand_bet in hand_bets:
    top2 = [a[1] for a in list(Counter(hand_bet[0]).most_common())[:2]]
    if top2[0] == 3 and top2[1] == 2:
        hand_types['fh'].append(hand_bet)
    elif top2[0] == 2 and top2[1] == 2:
        hand_types['tp'].append(hand_bet)
    else:
        hand_types[top2[0]].append(hand_bet)
combined = []
for hand_type in hand_types.values():
    hand_type.sort(
        key=lambda x: (strength[x[0][0]], strength[x[0][1]], strength[x[0][2]], strength[x[0][3]], strength[x[0][4]]),
        reverse=True
    )
    combined = hand_type + combined
total = 0
for i in range(len(combined)):
    total += (i + 1) * combined[i][1]
print(total)

""" Part 2 """

strength = {'A': 1, 'K': 2, 'Q': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12, 'J': 13}
hand_types = {5: [], 4: [], 'fh': [], 3: [], 'tp': [], 2: [], 1: []}
for hand_bet in hand_bets:
    top2 = [a[1] for a in list(Counter(hand_bet[0]).most_common())[:2]]
    j_count = Counter(hand_bet[0])['J']
    # This is what I used to find these specific if statements: https://imgur.com/a/0Eeb5ne
    if top2[0] + j_count in [5, 8, 10] or (top2[1] == 2 and top2[0] + j_count == 6):
        hand_types[5].append(hand_bet)
    elif top2[0] + j_count == 6 or (top2[0] + j_count == 4 and sum(top2) > 3):
        hand_types[4].append(hand_bet)
    elif top2[0] + j_count in [3, 4] and top2[1] == 1:
        hand_types[3].append(hand_bet)
    elif top2[0] + j_count == 3:
        hand_types['fh'].append(hand_bet)
    elif top2[0] + j_count == 2 and top2[1] == 2:
        hand_types['tp'].append(hand_bet)
    elif top2[0] + j_count == 2:
        hand_types[2].append(hand_bet)
    else:
        hand_types[1].append(hand_bet)
combined = []
for hand_type in hand_types.values():
    hand_type.sort(
        key=lambda x: (strength[x[0][0]], strength[x[0][1]], strength[x[0][2]], strength[x[0][3]], strength[x[0][4]]),
        reverse=True
    )
    combined = hand_type + combined
total = 0
for i in range(len(combined)):
    total += (i + 1) * combined[i][1]
print(total)
