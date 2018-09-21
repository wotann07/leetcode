from unittest import TestCase

from four_numbers import FourNumbers


class TestFourNumbers(TestCase):
    def test_get_four_number_sum(self):
        self.assertEqual([[1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 4, 6], [2, 3, 4, 5]],
                         FourNumbers.get_four_number_sum(14, [1, 2, 3, 4, 5, 6, 7]))
