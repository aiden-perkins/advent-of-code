ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

tt = 0

for ll in ls:
    nums = list(map(int, ll.split()))
    vs = set()
    for i in range(len(nums) - 1):
        vs.add(nums[i] - nums[i + 1])
    if len(vs.difference({1, 2, 3})) < 1:
        tt += 1
    elif len(vs.difference({-1, -2, -3})) < 1:
        tt += 1

print(tt)

""" Part 2 """

tt = 0

for ll in ls:
    nums = list(map(int, ll.split()))
    for i in range(len(nums)):
        n2 = list(nums)
        n2.pop(i)
        vs = set()
        for j in range(len(n2) - 1):
            vs.add(n2[j] - n2[j + 1])
        if len(vs.difference({1, 2, 3})) < 1:
            tt += 1
            break
        elif len(vs.difference({-1, -2, -3})) < 1:
            tt += 1
            break

print(tt)
