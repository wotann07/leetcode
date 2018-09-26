from unittest import TestCase

from binary_tree import BinaryTree


class TestBinaryTree(TestCase):
    def test_is_bst(self):
        bt = BinaryTree(10)
        leaf = bt.add_left(7)
        bt.add_right(11, leaf)
        bt.add_right(39)

        self.assertFalse(bt.is_bst())

        bt = BinaryTree(10)
        leaf = bt.add_left(7)
        bt.add_right(8, leaf)
        bt.add_right(39)

        self.assertTrue(bt.is_bst())
