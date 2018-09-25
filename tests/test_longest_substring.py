from unittest import TestCase

from longest_substring import LongestSubstring


class TestLongestSubstring(TestCase):
    def test_get_length_of_longest_substring(self):
        self.assertEqual(4, LongestSubstring.get_length_of_longest_substring_hash('abcad'), 'Input "abcad"')
        self.assertEqual(3, LongestSubstring.get_length_of_longest_substring_hash('dvdf'), 'Input "dvdf"')
        self.assertEqual(3, LongestSubstring.get_length_of_longest_substring_hash('abcabcbb'), 'Input "abcabcbb"')
