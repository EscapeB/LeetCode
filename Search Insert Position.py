# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if (left + right) % 2 == 0:
            middle = int((left + right) / 2)
        else:
            middle = int((left + right - 1) / 2)
        while left <= right:
            # find one target
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
            if (left + right) % 2 == 0:
                middle = int((left + right) / 2)
            else:
                middle = int((left + right - 1) / 2)
        return left


solution = Solution()

print(solution.searchInsert([1, 3, 5, 6], 7))
print(solution.searchInsert([1, 3, 5, 6], 0))
print(solution.searchInsert([1, 3, 5, 6], 2))
print(solution.searchInsert([1, 3, 5, 6], 5))
print(solution.searchInsert([1, 3], 1))
print(solution.searchInsert([], 3))
