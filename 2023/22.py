from collections import defaultdict, deque
from itertools import product

ls = open('./input.txt').read().split('\n')[:-1]

""" Part 1 """

bricks: list = [tuple([int(a) for a in line.replace('~', ',').split(',')]) for line in ls]
bricks.sort(key=lambda x: x[2])


def fall(hit_z, fax, fay, faz, fbx, fby, fbz):
    d = faz - hit_z - 1
    faz -= d
    fbz -= d
    return fax, fay, faz, fbx, fby, fbz


for i in range(len(bricks)):
    ax, ay, az, bx, by, bz = bricks[i]
    max_z = 0
    for j in range(i - 1, -1, -1):
        ax2, ay2, az2, bx2, by2, bz2 = bricks[j]
        if bz2 < az:
            axy = set(product(range(ax, bx + 1), range(ay, by + 1)))
            bxy = set(product(range(ax2, bx2 + 1), range(ay2, by2 + 1)))
            if axy.intersection(bxy):
                max_z = max(max_z, bz2)
    bricks[i] = fall(max_z, *bricks[i])

bricks.sort(key=lambda x: x[2])
tree = defaultdict(list)
p2_tree = {}
for i in range(len(bricks)):
    ax, ay, _, bx, by, bz = bricks[i]
    supporting = []
    for j in range(i + 1, len(bricks)):
        ax2, ay2, az2, bx2, by2, _ = bricks[j]
        b_highest_z = bz
        b2_lowest_z = az2
        if b2_lowest_z - b_highest_z > 3:
            break
        if (b2_lowest_z - b_highest_z) == 1:
            axy = set(product(range(ax, bx + 1), range(ay, by + 1)))
            bxy = set(product(range(ax2, bx2 + 1), range(ay2, by2 + 1)))
            if axy.intersection(bxy):
                supporting.append(bricks[j])
    for s_brick in supporting:
        tree[s_brick].append(bricks[i])
    p2_tree[bricks[i]] = supporting

for k, v in tree.items():
    if len(v) == 1:
        if v[0] in bricks:
            bricks.remove(v[0])
print(len(bricks))

""" Part 2 """

t = 0
for key in p2_tree.keys():
    chain = []
    current = deque([key])
    while current:
        crd = current.popleft()
        chain.append(crd)
        for new_crd in p2_tree[crd]:
            if new_crd not in current and all(item in chain for item in tree[new_crd]):
                t += 1
                current.append(new_crd)
print(t)
