code, ll = open('./input.txt', 'r').read().split('\n\n')
rules = dict([g.split(' -> ') for g in ll.split('\n')][:-1])

""" Part 1 """

def solve(loop):
    pairs = {}
    for char in range(len(code)):
        if char+1 in range(len(code)):
            pairs[code[char]+code[char+1]] = 1
    for r in range(loop):
        pairs2 = {}
        for pair in pairs:
            pairs2[pair[0] + rules[pair]] = pairs[pair] + pairs2.get(pair[0] + rules[pair], 0)
            pairs2[rules[pair] + pair[1]] = pairs[pair] + pairs2.get(rules[pair] + pair[1], 0)
        pairs = pairs2

    total = {}
    for pairC in pairs2:
        total[pairC[0]] = pairs[pairC] + total.get(pairC[0], 0)
    total[code[-1]] += 1
    print(sorted(total.values())[len(total)-1]-sorted(total.values())[0])

solve(10)

""" Part 2 """

solve(40)
