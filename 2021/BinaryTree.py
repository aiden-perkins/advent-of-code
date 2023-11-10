# import SLLQueue


class BinaryTree:
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return str(self.v)

    def __init__(self):
        self.r = None

    def depth(self, u: Node) -> int:
        if u is None:
            return -1
        d = 0
        current_node = u
        while current_node != self.r:
            current_node = current_node.parent
            d += 1
        return d

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        if u is None:
            return -1
        return 1 + max(self._height(u.left), self._height(u.right))

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        if u is None:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def bf_order(self):
        # The commented out code is if you want to use a SLLQueue instead of a python list.
        nodes = []
        # q = SLLQueue.SLLQueue()
        q = []
        if self.r is not None:
            # q.add(self.r)
            q.append(self.r)
        # while q.size() > 0:
        while len(q) > 0:
            # u = q.remove()
            u = q.pop(0)
            nodes.append(u)
            if u.left is not None:
                # q.add(u.left)
                q.append(u.left)
            if u.right is not None:
                # q.add(u.right)
                q.append(u.right)
        return nodes

    def in_order(self) -> list:
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        nodes = []
        if u.left is not None:
            nodes.extend(self._in_order(u.left))
        nodes.append(u)
        if u.right is not None:
            nodes.extend(self._in_order(u.right))
        return nodes

    def post_order(self) -> list:
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        nodes = []
        if u.left is not None:
            nodes.extend(self._post_order(u.left))
        if u.right is not None:
            nodes.extend(self._post_order(u.right))
        nodes.append(u)
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        nodes = []
        nodes.append(u)
        if u.left is not None:
            nodes.extend(self._pre_order(u.left))
        if u.right is not None:
            nodes.extend(self._pre_order(u.right))
        return nodes

    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)
