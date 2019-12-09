# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minIndex, maxIndex = -1, -1
        left, right = 0, len(nums) - 1
        if (left + right) % 2 == 0:
            middle = int((left + right) / 2)
        else:
            middle = int((left + right - 1) / 2)
        while left <= right:
            # find one target
            if nums[middle] == target:
                minIndex = maxIndex = middle
                # scan in left and right to find all
                step = 1
                # right scan
                while middle + step < len(nums) and nums[middle + step] == target:
                    maxIndex = middle + step
                    step += 1
                # left scan
                step = 1
                while middle - step > 0 and nums[middle - step] == target:
                    minIndex = middle - step
                    step += 1

                break

            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
            if (left + right) % 2 == 0:
                middle = int((left + right) / 2)
            else:
                middle = int((left + right - 1) / 2)
        return [minIndex, maxIndex]


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
print(solution.searchRange([1], 1))
print(solution.searchRange([], 1))
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
print(solution.searchRange([5, 7, 8, 8, 8, 10], 8))
