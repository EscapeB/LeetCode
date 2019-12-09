# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.


from typing import List


class Solution:
    # Greedy

    # def canJump(self, nums: List[int]) -> bool:
    #     i = 0
    #     if len(nums) == 1:
    #         return True
    #     while i < len(nums) - 1:
    #         if i + nums[i] >= len(nums) - 1:
    #             return True
    #         if nums[i] == 0:
    #             break
    #         maxIndex = 0
    #         maxValue = 0
    #         for j in range(1, nums[i] + 1):
    #             if j + nums[i + j] >= maxValue:
    #                 maxIndex = j
    #                 maxValue = j + nums[i + j]
    #         i = i + maxIndex
    #     return False

    # slide window
    def canJump(self, nums: List[int]) -> bool:
        reachMax = 0
        for i in range(len(nums)):
            if i <= reachMax <= i + nums[i]:
                reachMax = i + nums[i]
            if reachMax >= len(nums) - 1:
                return True
        return False


solution = Solution()
print(solution.canJump([3, 2, 1, 1, 4]))
print(solution.canJump([1, 1, 0, 1]))
print(solution.canJump([1, 1, 2, 2, 0, 1, 1]))
