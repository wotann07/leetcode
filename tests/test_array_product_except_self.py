import unittest

from array_product_except_self import ArrayProductExceptSelf


class TestArrayProductExceptSelf(unittest.TestCase):
    def test_product_except_self(self):
        self.assertListEqual([24, 12, 8, 6], ArrayProductExceptSelf.product_except_self([1, 2, 3, 4]))
