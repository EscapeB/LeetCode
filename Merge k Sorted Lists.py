# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from utils.Common import ListNode, liked2array, array2linked


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        def should_continue(nodes) -> bool:
            for i in nodes:
                if i is not None:
                    return True
            return False

        r = ListNode(None)
        result = r
        # pointer arrary
        ps = [None] * len(lists)
        for i in range(len(lists)):
            ps[i] = lists[i]
        # print(should_continue(ps))
        while should_continue(ps):
            minVal = 9999999
            minIndex = None
            for j in range(len(ps)):
                if ps[j] is not None:
                    if ps[j].val <= minVal :
                        minIndex = j
                        minVal = ps[j].val
            # print(minVal, minIndex)
            r.next = ListNode(minVal)
            r = r.next
            ps[minIndex] = ps[minIndex].next
        return result.next


solution = Solution()
print(liked2array(solution.mergeKLists([
    array2linked([1, 4, 5]),
    array2linked([1, 3, 4]),
    array2linked([1]),
])))
