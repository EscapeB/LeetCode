# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        if len(nums) % 2 == 1:
            middle = int((left + right) / 2)
        else:
            middle = int((left + right - 1) / 2)
        while True:
            if nums[middle] == target:
                return middle
            if abs(right - left) <= 1:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    break
            if nums[middle] > target:  # 中间比目标大
                # 左边是递增 ，判断是否左边最小值小于目标值
                if nums[middle] > nums[left]:
                    # 判断左边最小值是否大于目标值，是的话向左，否则向右
                    if nums[left] <= target:
                        right = middle
                    else:
                        left = middle
                # 右边递增，左边有拐点 因为当前值已经大于目标值了，所以向左
                else:
                    right = middle
            else:  # 中间值比目标值小
                # 左边是递增，中间比目标值小，所以往右
                if nums[middle] > nums[left]:
                    left = middle
                # 右边递增，左边有拐点，判断最大值否是大于目标值
                else:
                    if nums[right] >= target:
                        left = middle
                    else:
                        right = middle
            if (left + right) % 2 == 0:
                middle = int((left + right) / 2)
            else:
                middle = int((left + right - 1) / 2)
        return -1


solution = Solution()
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(solution.search([4, 5, 6, 7, 0, 1, 2, 3], 3))
print(solution.search([3, 1], 3))
print(solution.search([5, 1, 3], 3))

# print(solution.search([], 1))
# print(solution.search([1], 0))
