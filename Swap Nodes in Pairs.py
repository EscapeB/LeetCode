# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils.Common import ListNode, liked2array, array2linked


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        vHead = ListNode(None)
        vHead.next = head
        p = head
        r = vHead
        while p:
            q = p.next
            if q is None:
                break
            else:
                p.next = q.next
                q.next = p
                r.next = q
                r = p
                p = p.next
        return vHead.next


solution = Solution()
print(liked2array(solution.swapPairs(array2linked([1, 2, 3, 4]))))
print(liked2array(solution.swapPairs(array2linked([2, 3, 4]))))
print(liked2array(solution.swapPairs(array2linked([1]))))
