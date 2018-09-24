from unittest import TestCase

from fibonacci import Fibonacci


class TestFibonacci(TestCase):
    def test_get_fibonacci(self):
        self.assertEqual(75025, Fibonacci.get_fibonacci(25))
