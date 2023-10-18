ls = [ii[:-1] for ii in open('./input.txt', 'r').readlines()][0]

def no_repeat(amount):
    for char in range(amount, len(ls)):
        for ch in ls[char-amount:char]:
            if ls[char-amount:char].count(ch) > 1:
                break
        else:
            return char
    

""" Part 1 """

print(no_repeat(4))

""" Part 2 """

print(no_repeat(14))
