"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = None
        p1 = l1
        p2 = l2

        carry_on = 0
        digit_value = 0

        while p1 is not None or p2 is not None:
            if p1 is None:
                digit_value = p2.val + carry_on
                if digit_value > 9:
                    carry_on = 1
                    digit_value -= 10
                else:
                    carry_on = 0
                head_node = ListNode(digit_value, head_node)
                p2 = p2.next
            elif p2 is None:
                digit_value = p1.val + carry_on
                if digit_value > 9:
                    carry_on = 1
                    digit_value -= 10
                else:
                    carry_on = 0
                head_node = ListNode(digit_value, head_node)
                p1 = p1.next
            else:
                digit_value = p1.val + p2.val + carry_on
                if digit_value > 9:
                    carry_on = 1
                    digit_value -= 10
                else:
                    carry_on = 0
                head_node = ListNode(digit_value, head_node)
                p1 = p1.next
                p2 = p2.next

        # Accounts for the case where the number of digits in the result surpasses max(number of digits in the inputs)
        if carry_on == 1:
            head_node = ListNode(1, head_node)

        # The final answer should be in reverse order
        reversed_digits = None
        while head_node is not None:
            reversed_digits = ListNode(head_node.val, reversed_digits)
            head_node = head_node.next

        return reversed_digits


# this is the
class BetterSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        tail = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            tail.next = ListNode(digit)

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            tail = tail.next

        result = dummy_head.next
        return result
