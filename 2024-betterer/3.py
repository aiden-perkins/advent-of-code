import re

i = open('./input.txt').read().strip()

""" Part 1 """

print(sum([eval(f'{a}*{b}') for a, b in re.findall(r'mul\((\d+),(\d+)\)', i)]))

""" Part 2 """

t, do = 0, True
for m in re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', i):
    do = not m[3] and (True if m[2] else do)
    t += eval(f'{m[0]}*{m[1]}') if do and m[0] else 0
print(t)
