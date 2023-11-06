import operator

ls = open('./input.txt', 'r').read().split('\n\n')

""" Part 1 """

op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
monkeys = []
for monkey_string in ls:
    monkey_string = monkey_string.split('\n')
    items = [int(a) for a in monkey_string[1][18:].split(', ')]
    operation = op[monkey_string[2][23:24]]
    operation_value = monkey_string[2][25:]
    test_num = int(monkey_string[3][21:])
    on_true = int(monkey_string[4][29:])
    on_false = int(monkey_string[5][30:])
    monkeys.append([items, operation, operation_value, test_num, on_true, on_false])

inspects = [0] * len(monkeys)
for i in range(20):
    for idx, monkey in enumerate(monkeys):
        inspects[idx] += len(monkey[0])
        for item in monkey[0]:
            o_v = monkey[2]
            if monkey[2] == 'old':
                o_v = item
            else:
                o_v = int(o_v)
            v = monkey[1](item, o_v)
            v = int(v / 3)
            if v / monkey[3] == v // monkey[3]:
                monkeys[monkey[4]][0].append(v)
            else:
                monkeys[monkey[5]][0].append(v)
        monkeys[idx][0] = []
inspects.sort(reverse=True)
print(inspects[0] * inspects[1])

""" Part 2 """


