# https://leetcode.com/problems/add-two-numbers/description/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if isinstance(other, ListNode):
            this_pointer = self.next
            other_pointer = other.next
            if other.val != self.val:
                return False
            else:
                while this_pointer is not None:
                    if this_pointer.val != other_pointer.val:
                        return False
                    this_pointer = this_pointer.next
                    other_pointer = other_pointer.next

            return other_pointer is None
        return NotImplemented


class AddTwoNumbers:
    @staticmethod
    def _add_helper(l, val1, val2):
        """
        :type l: ListNode
        :type val1: Integer
        :type val2: Integer
        """
        addition = val1 + val2 + l.val
        l.next = ListNode(0)
        if addition >= 10:
            addition = addition - 10
            l.next.val = 1

        l.val = addition
        return l.next

    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        initial_sum = l1.val + l2.val
        if initial_sum >= 10:
            carry_over = 1
            initial_sum = initial_sum - 10

        to_return = ListNode(initial_sum)
        to_return_pointer = to_return

        l1_pointer = l1.next
        l2_pointer = l2.next
        while l1_pointer is not None and l2_pointer is not None:
            addition = l1_pointer.val + l2_pointer.val + carry_over
            carry_over = 0
            if addition >= 10:
                carry_over = 1
                addition = addition - 10

            to_return_pointer.next = ListNode(addition)
            to_return_pointer = to_return_pointer.next
            l1_pointer = l1_pointer.next
            l2_pointer = l2_pointer.next

        # only one of this loops will be entered
        while l1_pointer is not None:
            to_return_pointer.next = ListNode(l1_pointer.val + carry_over)
            to_return_pointer = to_return_pointer.next
            carry_over = 0
            l1_pointer = l1_pointer.next
        while l2_pointer is not None:
            to_return_pointer.next = ListNode(l2_pointer.val + carry_over)
            to_return_pointer = to_return_pointer.next
            carry_over = 0
            l2_pointer = l2_pointer.next

        if carry_over > 0:
            to_return_pointer.next = ListNode(1)

        return to_return
