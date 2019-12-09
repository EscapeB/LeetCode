# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils.Common import ListNode, liked2array, array2linked


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        count = 0
        pos = 0
        p = q = head
        # 计算总数，同时p指向尾
        while p:
            count += 1
            if p.next:
                p = p.next
            else:
                break
        while q:
            pos += 1
            if pos == count - (k % count):
                p.next = head
                head = q.next
                q.next = None
                break
            if q.next:
                q = q.next
            else:
                break
        return head


solution = Solution()
print(liked2array(solution.rotateRight(array2linked([1, 2, 3, 4, 5]), 2)))
print(liked2array(solution.rotateRight(array2linked([1]), 2)))
print(liked2array(solution.rotateRight(array2linked([0, 1, 2]), 4)))
