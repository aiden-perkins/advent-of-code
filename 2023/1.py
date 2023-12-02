ls = open('./input.txt', 'r').read().split('\n')[:-1]

""" Part 1 55386"""

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
t = 0
for line in ls:
    mn = -1
    mx = -1
    s = '00'
    for num in nums:
        if num in line:
            if line.index(num) < mn or mn == -1:
                mn = line.index(num)
                s = num + s[1:2]
            if line.rindex(num) > mx:
                mx = line.rindex(num)
                s = s[:1] + num
    t += int(s)
print(t)

""" Part 2 54824"""

t = 0
for line in ls:
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    min_idx = -1
    max_idx = -1
    v = ''
    v2 = ''
    for p in nums + words:
        if p in line:
            if line.index(p) < min_idx or min_idx == -1:
                min_idx = line.index(p)
                v = str(words.index(p) + 1) if p.isalpha() else p
            if line.rindex(p) > max_idx:
                max_idx = line.rindex(p)
                v2 = str(words.index(p) + 1) if p.isalpha() else p
    t += int(v + v2)

print(t)
