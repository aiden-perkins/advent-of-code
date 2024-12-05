ls = open('./input.txt').read().strip().split('\n')

""" Part 1 """

ms, ml = zip(*[map(int, ll.split('   ')) for ll in ls])
print(sum(abs(l - s) for l, s in zip(sorted(ml), sorted(ms))))
