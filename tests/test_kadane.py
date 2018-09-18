from unittest import TestCase

from kadanes_algorithm import Kadane


class TestKadane(TestCase):
    def test_get_max_contiguous_sum(self):
        self.assertTrue(14 == Kadane.get_max_contiguous_sum([1, 2, -1, 3, 4, 5, -10]))
        self.assertTrue(3 == Kadane.get_max_contiguous_sum([1, 2, -1, -1, -1, -1, -1]))
        self.assertTrue(16 == Kadane.get_max_contiguous_sum([1, 10, -1, -1, -1, -1, -1, 10]))
