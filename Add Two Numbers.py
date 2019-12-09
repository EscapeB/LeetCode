# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#  You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from utils.Common import ListNode, array2linked
import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)
        root = p
        upper = 0
        while l1 or l2:
            if l1:
                p.val += l1.val
                l1 = l1.next
            if l2:
                p.val += l2.val
                l2 = l2.next
            upper = math.floor(p.val / 10)
            p.val = p.val % 10
            if l1 or l2:
                p.next = ListNode(upper)
                p = p.next
        if upper >= 1:
            p.next = ListNode(upper)
        return root


solution = Solution()
r = solution.addTwoNumbers(array2linked([9, 9]), array2linked([9]))
while r:
    print(r.val)
    r = r.next
