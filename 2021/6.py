f = open('./input.txt', 'r')
lines = f.readlines()

""" Part 1 """

def fishes(days):
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in lines[0][:-1].split(','):
        fish[int(f)] += 1
    for j in range(days):
        fish8 = fish[0]
        fish.pop(0)
        fish[6] += fish8
        fish.append(fish8)
    return fish

print(sum(fishes(80)))

""" Part 2 """

print(sum(fishes(256)))
