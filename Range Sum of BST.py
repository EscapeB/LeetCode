from utils.Common import TreeNode, array2tree


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        tree_sum = 0
        visit_arr = []
        now = root
        while now or len(visit_arr) != 0:
            while now:
                visit_arr.append(now)
                print(now.val)
                if L <= now.val <= R:
                    tree_sum += now.val
                now = now.left
            now = visit_arr.pop()
            while not now.right and len(visit_arr) > 0:
                now = visit_arr.pop()
            now = now.right
        return tree_sum


solution = Solution()
print(solution.rangeSumBST(array2tree([15, 9, 21, 7, 13, 19, 23, 5, None, 11, None, 17]), 21, 32))
