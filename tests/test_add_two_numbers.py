from unittest import TestCase
from add_two_numbers import ListNode
from add_two_numbers import AddTwoNumbers


class TestAddTwoNumbers(TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = ListNode(7)
        result.next = ListNode(0)
        result.next.next = ListNode(8)

        self.assertTrue(AddTwoNumbers.add_two_numbers(l1, l2) == result)
