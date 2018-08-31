from unittest import TestCase
from two_sum import TwoSum


class TestTwoSum(TestCase):
    def test_two_sum(self):
        self.assertEqual([0, 1], TwoSum.two_sum(nums=[2, 7, 11, 15], target=9))
