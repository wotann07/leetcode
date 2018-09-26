class Node:
    def __init__(self, value, index: int = 0):
        self.value = value
        self.index = index


class BinaryTree:
    def __init__(self, value):
        self.tree = [Node(value)]

    @staticmethod
    def _new_index(curr_i: int, pos: str):
        new_index = 2 * curr_i + 1
        if pos in ('left', 'right'):
            if pos == 'right':
                new_index += 1
            return new_index
        else:
            return None

    def _add(self, value, pos, parent: Node = None):
        if parent is None:
            parent = self.tree[0]
        new_index = BinaryTree._new_index(parent.index, pos)
        if 0 <= parent.index < len(self.tree):
            if self.tree[parent.index] == parent:
                if new_index >= len(self.tree):
                    self.tree += [None] * 10

                if self.tree[new_index] is None:
                    ret = Node(value, new_index)
                    self.tree[new_index] = ret
                    return ret

        return None

    def _get(self, pos, parent: Node = None):
        if parent is None:
            parent = self.tree[0]
        target = BinaryTree._new_index(parent.index, pos)
        if target:
            if target < len(self.tree):
                return self.tree[target]
            else:
                return None
        return None

    def get_head(self):
        return self.tree[0]

    def add_left(self, value, parent: Node = None):
        """
        Adds left children to parent
        :param parent: Parent Node
        :param value: Value of node to be inserted
        :return: Added Node, otherwise None
        """
        return self._add(value, 'left', parent)

    def add_right(self, value, parent: Node = None):
        """
        Adds right children to parent
        :param parent: Parent Node
        :param value: Value of node to be inserted
        :return: Added Node, otherwise None
        """
        return self._add(value, 'right', parent)

    def get_left(self, parent: Node = None):
        return self._get('left', parent)

    def get_right(self, parent: Node = None):
        return self._get('right', parent)

    def _in_order(self, parent: Node, result: [], proceed=True, break_fnc=None):
        if not proceed:
            return False
        if parent is None:
            return True

        self._in_order(self.get_left(parent), result, proceed, break_fnc)
        result.append(parent.value)
        if break_fnc:
            proceed = not break_fnc(result)
        return self._in_order(self.get_right(parent), result, proceed, break_fnc)

    def is_bst(self):
        """
        In order traversal
        :return: True if this tree is a binary search tree, False otherwise
        """
        in_order = []
        ret = self._in_order(self.tree[0], in_order,
                             break_fnc=lambda x: x[len(x) - 1] < x[len(x) - 2] if len(x) > 1 else False)

        print(in_order)
        return ret
