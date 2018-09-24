from unittest import TestCase

from sorter import Sorter


class TestSorter(TestCase):

    def test_sorts(self):
        sorted_arr = [1, 2, 3, 4, 5]
        for sorter in [Sorter.merge_sort, Sorter.bubble_sort, Sorter.quick_sort, Sorter.selection_sort]:
            print('Testing: ' + sorter.__name__)
            self.assertEqual(sorted_arr, sorter([3, 2, 5, 1, 4]))
