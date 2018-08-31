from unittest import TestCase
from spiral_matrix import SpiralMatrix


class TestSpiralMatrix(TestCase):
    def test_spiral_order(self):
        self.assertListEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], SpiralMatrix.spiral_order([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))
