from unittest import TestCase

from sorter import Sorter


class TestSorter(TestCase):
    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], Sorter.merge_sort([3, 2, 5, 1, 4]))

    def test_bubble_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], Sorter.bubble_sort([3, 2, 5, 1, 4]))

    def test_heap_sort(self):
        self.fail()

    def test_selection_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], Sorter.selection_sort([3, 2, 5, 1, 4]))

    def test_insertion_sort(self):
        self.fail()

    def test_shell_sort(self):
        self.fail()

    def test_quick_sort(self):
        self.fail()
