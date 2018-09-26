from random import shuffle
from unittest import TestCase

from missing_number import MissingNumber


class TestMissingNumber(TestCase):
    arr = [1, 2, 3, 5, 6, 7, 8]

    def test_get_missing_int_in_sequence(self):
        shuffled_arr = TestMissingNumber.arr[:]
        shuffle(shuffled_arr)
        self.assertEqual(4, MissingNumber.get_missing_int_in_sequence(shuffled_arr))

    def test_get_missing_int_in_sorted(self):
        self.assertEqual(4, MissingNumber.get_missing_int_in_sorted(TestMissingNumber.arr))
