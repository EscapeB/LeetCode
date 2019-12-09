# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from utils.Common import ListNode, array2linked


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        virtualHead = ListNode(None)
        virtualHead.next = head
        p = virtualHead
        length = 0
        while p:
            length = length + 1
            p = p.next
        p = virtualHead
        step = 0
        while p:
            step = step + 1
            if step == length - n:
                if p.next.next:
                    p.next = p.next.next
                else:
                    p.next = None
                break
            p = p.next

        return virtualHead.next


solution = Solution()
# print(solution.removeNthFromEnd(array2linked([1]), 1).val)
print(solution.removeNthFromEnd(array2linked([1, 2]), 2).val)
