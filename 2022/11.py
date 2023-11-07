import operator
import copy

ls = open('./input.txt', 'r').read().split('\n\n')

""" Part 1 """

op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
monkeys = []
for monkey_string in ls:
    monkey_string = monkey_string.split('\n')
    items = [int(a) for a in monkey_string[1][18:].split(', ')]
    if monkey_string[2][25:] == 'old':
        operation = operator.pow
        operation_value = 2
    else:
        operation = op[monkey_string[2][23:24]]
        operation_value = int(monkey_string[2][25:])
    test_num = int(monkey_string[3][21:])
    on_true = int(monkey_string[4][29:])
    on_false = int(monkey_string[5][30:])
    monkeys.append([items, operation, operation_value, test_num, on_true, on_false])
m2 = copy.deepcopy(monkeys)

inspects = [0] * len(monkeys)
for i in range(20):
    for idx, monkey in enumerate(monkeys):
        inspects[idx] += len(monkey[0])
        for item in monkey[0]:
            v = int(monkey[1](item, monkey[2]) / 3)
            if v % monkey[3] == 0:
                monkeys[monkey[4]][0].append(v)
            else:
                monkeys[monkey[5]][0].append(v)
        monkeys[idx][0] = []
inspects.sort(reverse=True)
print(inspects[0] * inspects[1])

""" Part 2 """

total_d = 1
for m in m2:
    total_d *= m[3]
inspects = [0] * len(m2)
for i in range(10000):
    for idx, monkey in enumerate(m2):
        inspects[idx] += len(monkey[0])
        for item in monkey[0]:
            v = monkey[1](item, monkey[2]) % total_d
            if v % monkey[3] == 0:
                m2[monkey[4]][0].append(v)
            else:
                m2[monkey[5]][0].append(v)
        m2[idx][0] = []
inspects.sort(reverse=True)
print(inspects[0] * inspects[1])

