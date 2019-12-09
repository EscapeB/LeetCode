# Merge two sorted linked lists and return it as a new list.
#
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Example:
#
# Input: 1->4->6, 2->3->5
# Output: 1->2->3->4->5->6

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils.Common import ListNode, array2linked, liked2array


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        r = ListNode(None)
        result = r
        while p or q:
            if p is None:
                r.next = q
                r = r.next
                q = q.next
            elif q is None:
                r.next = p
                r = r.next
                p = p.next
            else:
                if p.val <= q.val:
                    r.next = p
                    r = r.next
                    p = p.next
                else:
                    r.next = q
                    r = r.next
                    q = q.next
        return result.next


solution = Solution()
print(liked2array(solution.mergeTwoLists(array2linked([1, 2, 4]), array2linked([1, 3, 4]))))
print(liked2array(solution.mergeTwoLists(array2linked([1, 4, 6]), array2linked([2, 3, 5]))))
