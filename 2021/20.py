from collections import Counter

ls = open('./input.txt').read().split('\n\n')

""" Part 1 """

input_image = [a.replace('.', '0').replace('#', '1') for a in ls[1].split('\n')[:-1]]
code = list(ls[0].replace('.', '0').replace('#', '1'))


def transform_image(og_image, iimage, flip_amount, transform):
    expanded = 0
    for flipped in range(flip_amount):
        new_image = []
        for row_i in range((flip_amount + 2) - 1 - expanded, len(og_image) + (flip_amount + 2) + expanded + 1):
            new_row = []
            for column_i in range((flip_amount + 2) - 1 - expanded, len(og_image) + (flip_amount + 2) + expanded + 1):
                num = ''
                for x in range(row_i - 1, row_i + 2):
                    for y in range(column_i - 1, column_i + 2):
                        num += iimage[x][y]
                new_row.append(transform[int(num, 2)])
            new_image.append(new_row)
        bg = transform[int(iimage[0][0] * 9, 2)]
        expanded += 1

        img = []
        for i in range(-(flip_amount + 2), len(og_image) + (flip_amount + 2)):
            s = bg * ((flip_amount + 2) - expanded)
            if i not in range(-expanded, len(og_image) + expanded):
                s += bg * (len(og_image) + (2 * expanded))
            else:
                s += ''.join(new_image[i + expanded])
            s += bg * ((flip_amount + 2) - expanded)
            img.append(list(s))
        iimage = img
        # [print(''.join(a).replace('0', '.').replace('1', '#')) for a in iimage]
    return iimage


def make_bounded_image(image, extend_by):
    iimage = []
    for i in range(-extend_by, len(image) + extend_by):
        s = '0' * extend_by
        if i not in range(len(image)):
            s += '0' * len(image)
        else:
            s += image[i]
        s += '0' * extend_by
        iimage.append(list(s))
    return iimage


flip_a = 2
starting_image = make_bounded_image(input_image, flip_a + 2)
final = transform_image(input_image, starting_image, flip_a, code)
total = 0
for ige in final:
    total += Counter(ige)['1']
print(total)

""" Part 2 """

flip_a = 50
starting_image = make_bounded_image(input_image, flip_a + 2)
final = transform_image(input_image, starting_image, flip_a, code)
total = 0
for ige in final:
    total += Counter(ige)['1']
print(total)  # Might take ~3 seconds
