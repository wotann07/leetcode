from unittest import TestCase

from replace_with_greatest import ReplaceWithGreatest


class TestReplaceWithGreatest(TestCase):
    def test_replace_with_greatest(self):
        arr = [16, 17, 4, 3, 5, 2]
        ReplaceWithGreatest.replace_with_greatest(arr)
        self.assertEqual(arr, [17, 5, 5, 5, 2, -1])
