ls = open('./input.txt').read().split('\n\n')

""" Part 1 """

seeds = [int(a) for a in ls[0].split()[1:]]
maps = ls[1:]
seed_maps = []
for mm in maps:
    s_d = []
    m = mm.split('\n')[1:]
    for nums_s in m:
        nums = [int(a) for a in nums_s.split()]
        s_d.append(nums)
    seed_maps.append(s_d)


def transform(seedss):
    vs = []
    for seed in seedss:
        value = seed
        for t in seed_maps:
            for r in t:
                if r[1] + r[2] > value >= r[1]:
                    value = (value - r[1]) + r[0]
                    break
        vs.append(value)
    return vs


print(min(transform(seeds)))

""" Part 2 """


def seed_check(v, rg):
    for ran in rg:
        if ran[1] >= v >= ran[0]:
            return True
    return False


s2 = []
s2m = []
for seed_i in range(len(seeds)//2):
    s2.append([seeds[seed_i*2], seeds[seed_i*2] + seeds[(seed_i*2)+1] - 1])
    s2m.append(seeds[seed_i*2])
trs = transform(s2m)

Max = min(trs)
Min = 0

end = 99750000  # I need to find a way to not hardcode this value
start = 0
while not seed_check(start, s2):
    value = end
    for t in seed_maps[::-1]:
        for r in t:
            if r[0] + r[2] > value >= r[0]:
                value = (value - r[0]) + r[1]
                break
    start = value
    end += 1
print(end - 1)
