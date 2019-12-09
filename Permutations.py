# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        i = 0
        stack = []
        position = []
        while i < len(nums):
            for j in range(0, len(nums)):
                # 找到第一个不在stack中的数
                if nums[j] not in stack:
                    # 记录值
                    stack.append(nums[j])
                    # 记录每一位对应的index
                    position.append(j)
                    break
            # 说明已经满了，记录结果，开始回溯
            if len(stack) == len(nums):
                result.append(list(stack))
                position.pop()
                stack.pop()
                while len(position) > 0:
                    # 该位置已经
                    if position[len(position) - 1] >= len(nums) - 1:
                        position.pop()
                        stack.pop()
                    else:
                        find = False
                        for k in range(position[len(position) - 1], len(nums)):
                            if k not in position:
                                position[len(position) - 1] = k
                                stack[len(stack) - 1] = nums[k]
                                find = True
                                break
                        if find:
                            break
                        else:
                            position.pop()
                            stack.pop()
                if len(position) > 0:
                    i = len(position) - 1
                else:
                    break
            i += 1
        return result


solution = Solution()
print(solution.permute([]))
print(solution.permute([1]))
print(solution.permute([1, 2, 3, 4]))
