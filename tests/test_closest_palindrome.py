from unittest import TestCase

from closest_palindrome import ClosestPalindrome


class TestClosestPalindrome(TestCase):
    def test_get_closest_palindrome(self):
        self.assertTrue(1234321 == ClosestPalindrome.get_closest_palindrome(1234567))
        self.assertTrue(33 == ClosestPalindrome.get_closest_palindrome(29))
        self.assertTrue(828 == ClosestPalindrome.get_closest_palindrome(832))
        self.assertTrue(22 == ClosestPalindrome.get_closest_palindrome(27))
