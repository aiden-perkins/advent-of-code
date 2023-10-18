
f = open('../input.txt', 'r')
lines = f.readlines()

""" Part 1 """

a = 0
total = 0
for i in lines:
    i = int(i)
    if i > a:
        total += 1
    a = i
print(total - 1)

""" Part 2 """

a = 0
b = 0
c = 0
total = 0
for i in lines:
    i = int(i)
    if i + a + b > a + b + c:
        total += 1
    c = b
    b = a
    a = i
print(total - 3)