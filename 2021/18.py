from helpers import BinaryTree
import math
import time

ls = open('./input.txt', 'r').read().split('\n')[:-1]


def make_tree(line):
    tree = BinaryTree()
    tree.r = tree.Node()
    current = tree.r
    for char in line:
        if char == '[':
            current = current.insert_left(tree.Node())
        elif char == ',':
            current.set_val(',')
            current = current.insert_right(tree.Node())
        elif char == ']':
            current = current.parent
        else:
            current.set_val(int(char))
            current = current.parent
    return tree


hw = []
hw2 = []
for snail_num in ls:
    hw.append(make_tree(snail_num))
    hw2.append(snail_num)

""" Part 1 """


def is_depth_5(b_tree, post_order: list[BinaryTree.Node]):
    return [node for node in post_order if node.v != ',' and b_tree.depth(node) >= 5]


def is_greater_9(post_order: list[BinaryTree.Node]) -> list[BinaryTree.Node]:
    return [node for node in post_order if node.v != ',' and node.v > 9]


def add_trees(tree1, tree2):
    combined = BinaryTree()
    combined.r = combined.Node(val=',')
    combined.r.insert_left(tree1.r)
    combined.r.insert_right(tree2.r)
    p_order = combined.post_order()
    pd5_order = is_depth_5(combined, p_order)
    while True:
        while len(pd5_order) > 0:
            explode_pair_2 = pd5_order[:2]
            left_node = None
            for i in range(p_order.index(explode_pair_2[0]) - 1, -1, -1):
                if p_order[i].v != ',':
                    left_node = p_order[i]
                    break
            if left_node is not None:
                left_node.v += explode_pair_2[0].v
            right_node = None
            for i in range(p_order.index(explode_pair_2[1]) + 1, len(p_order)):
                if p_order[i].v != ',':
                    right_node = p_order[i]
                    break
            if right_node is not None:
                right_node.v += explode_pair_2[1].v
            explode_pair_2[0].parent.v = 0
            explode_pair_2[0].parent.right = None
            explode_pair_2[0].parent.left = None
            p_order.remove(explode_pair_2[0])
            p_order.remove(explode_pair_2[1])
            pd5_order = pd5_order[2:]
        greater_9 = is_greater_9(p_order)
        if len(greater_9) == 0:
            break

        l = greater_9[0].insert_left(combined.Node(val=greater_9[0].v // 2))
        r = greater_9[0].insert_right(combined.Node(val=math.ceil(greater_9[0].v / 2)))
        greater_9[0].v = ','
        g_i = p_order.index(greater_9[0])
        p_order.insert(g_i, r)
        p_order.insert(g_i, l)
        greater_9 = is_greater_9(p_order)
        pd5_order = is_depth_5(combined, p_order)
        if len(greater_9) == 0 and len(pd5_order) == 0:
            break
    return combined


prev_tree = False
for tree in hw:
    if not prev_tree:
        prev_tree = tree
        continue
    prev_tree = add_trees(prev_tree, tree)


def mag(node):
    if node.left.v == ',':
        left = mag(node.left)
    else:
        left = node.left.v
    if node.right.v == ',':
        right = mag(node.right)
    else:
        right = node.right.v
    return (3 * left) + (2 * right)


print(mag(prev_tree.r))

""" Part 2 """

largest = 0
for i in range(len(hw2)):
    for j in range(len(hw2)):
        if i != j:
            t1 = make_tree(hw2[i])
            t2 = make_tree(hw2[j])
            m = mag(add_trees(t1, t2).r)
            if m > largest:
                largest = m
print(largest)
