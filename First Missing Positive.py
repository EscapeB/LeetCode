# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        dic = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                dic[nums[i]] = 1
        index = 1
        while dic.get(index):
            index += 1
        return index


solution = Solution()

print(solution.firstMissingPositive([1, 2, 3, 10, 2147483647, 9]))
print(solution.firstMissingPositive([2147483647]))
print(solution.firstMissingPositive([-1, 2, -2, 12, 4, 1, 2, 5]))
print(solution.firstMissingPositive([3, 4, -1, 1]))
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
