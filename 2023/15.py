from collections import OrderedDict

ls = open('./input.txt').read()[:-1].split(',')

""" Part 1 """


def hash_s(sequence):
    hash_value = 0
    for c in sequence:
        hash_value += ord(c)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


t = 0
for seq in ls:
    t += hash_s(seq)
print(t)

""" Part 2 """

boxes = OrderedDict()
[boxes.setdefault(i, default={}) for i in range(256)]
for seq in ls:
    chash = seq.replace('=', '-').split('-')[0]
    cv = hash_s(chash)
    if '=' in seq:
        boxes[cv][chash] = seq.split('=')[1]
    else:
        if chash in boxes[cv].keys():
            del boxes[cv][chash]
t = 0
for box_num, box_v in boxes.items():
    labels = list(box_v.keys())
    for label, focal_len in box_v.items():
        t += ((box_num + 1) * (labels.index(label) + 1) * int(focal_len))
print(t)
