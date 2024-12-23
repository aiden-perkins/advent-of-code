ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

ra = int(ls[0].strip().split(': ')[1])
rb = int(ls[1].strip().split(': ')[1])
rc = int(ls[2].strip().split(': ')[1])
program = [int(a) for a in ls[4].strip().split(': ')[1].split(',')]
vals = ['0', '1', '2', '3', 'ra', 'rb', 'rc', None]

i = 0
ov = []
while i < len(program):
    opcode = program[i]
    combo_operand = vals[program[i + 1]]
    literal_operand = program[i + 1]
    jumped = False
    if opcode == 0:
        ra = ra // (2 ** eval(combo_operand))
    elif opcode == 1:
        rb = rb ^ literal_operand
    elif opcode == 2:
        rb = eval(combo_operand) % 8
    elif opcode == 3:
        if ra != 0:
            i = literal_operand
            jumped = True
    elif opcode == 4:
        rb = rb ^ rc
    elif opcode == 5:
        ov.append(str(eval(combo_operand) % 8))
    elif opcode == 6:
        rb = ra // (2 ** eval(combo_operand))
    elif opcode == 7:
        rc = ra // (2 ** eval(combo_operand))
    if not jumped:
        i += 2

print(','.join(ov))

""" Part 2 """

# TODO
