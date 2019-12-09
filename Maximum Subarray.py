# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        dp = [-999] * len(nums)
        dp[0] = nums[0]
        lastIndex = 0
        for i in range(1, len(nums)):
            sumFromLast = sum(nums[lastIndex + 1:i + 1])
            if dp[i - 1] + sumFromLast <= nums[i]:
                dp[i] = nums[i]
                lastIndex = i
            elif sumFromLast > 0:
                dp[i] = sumFromLast + dp[i - 1]
                lastIndex = i
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return max(dp)


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
