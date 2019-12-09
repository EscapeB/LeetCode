# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that pofsition.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:
#
# You can assume that you can always reach the last index.

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        step = 0
        while i < len(nums):
            maxIndex = i
            maxValue = 0
            for j in range(nums[i] + 1):
                if i + nums[i] >= len(nums) - 1:
                    step += 1
                    return step
                if i + j < len(nums):
                    if nums[i + j] + j >= maxValue:
                        maxValue = nums[i + j] + j
                        maxIndex = i + j
            i = maxIndex
            step += 1
            # print(maxIndex)
        return step


solution = Solution()
# print(solution.jump([2, 3, 1, 1, 4, 2, 3, 1, 1, 4, 2, 3, 1, 1, 4, 2, 3, 1, 1, 4, 2, 3, 1, 1, 4]))
print(solution.jump([2, 3, 0, 1, 4]))
print(solution.jump([1, 2, 1, 1, 1]))
print(solution.jump([2, 3, 1, 1, 4]))
print(solution.jump([1, 2]))
print(solution.jump([1, 1, 1, 1]))
print(solution.jump([6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]))
