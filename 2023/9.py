from itertools import pairwise

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """


def predict(nums):
    next_set = [y - x for x, y in pairwise(nums)]
    return nums[-1] + (predict(next_set) if any(next_set) else 0)


numsl = [list(map(int, ll.split())) for ll in ls]
print(sum(map(predict, numsl)))

""" Part 2 """

print(sum(map(lambda x: predict(x[::-1]), numsl)))
