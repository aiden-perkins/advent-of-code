ls = open('./input.txt').read()[:-1].split('\n\n')

seeds = [int(a) for a in ls[0].split()[1:]]
seed_maps = [[[int(a) for a in nums_s.split()] for nums_s in maps.split('\n')[1:]] for maps in ls[1:]]

""" Part 1 """

vs = []
for seed in seeds:
    value = seed
    for t in seed_maps:
        for r in t:
            if r[1] + r[2] > value >= r[1]:
                value = (value - r[1]) + r[0]
                break
    vs.append(value)
print(min(vs))

""" Part 2 """

seeds2 = [[seeds[seed_i*2], seeds[seed_i*2] + seeds[(seed_i*2)+1] - 1] for seed_i in range(len(seeds)//2)]
for transitions in seed_maps:
    new_seeds = []
    for destination, source, length in transitions:
        outside = []
        for start, end in seeds2:
            if source + length > start >= source and source + length > end >= source:
                # The transition fully encapsulates the seed range.
                # Seed range:               |----|
                # Transition range:     |-----------|
                new_seeds.append([(start - source) + destination, (end - source) + destination])
            elif source + length > start >= source and not source + length > end >= source:
                # The start of the seed range is in the transition range but not the end.
                # Seed range:               |-------|
                # Transition range:     |-------|
                middle = source + length - 1
                new_seeds.append([(start - source) + destination, (middle - source) + destination])
                outside.append([middle + 1, end])
            elif not source + length > start >= source and source + length > end >= source:
                # The start of the seed range is not in the transition range but the end is.
                # Seed range:       |-------|
                # Transition range:     |-------|
                new_seeds.append([(source - source) + destination, (end - source) + destination])
                outside.append([start, source - 1])
            elif start < source and end >= source + length:
                # The seed range fully encapsulates the transition range.
                # Seed range:       |---------------|
                # Transition range:     |-------|
                new_seeds.append([(source - source) + destination, ((source + length - 1) - source) + destination])
                outside.append([start, source - 1])
                outside.append([source + length, end])
            elif start >= source + length - 1 or end < source:
                # The seed range does not intersect the transition range at all.
                # Seed range:      |------|
                # Transition range:              |-------|
                outside.append([start, end])
        seeds2 = outside
    new_seeds += seeds2
    seeds2 = new_seeds
print(min([a[0] for a in seeds2]))
