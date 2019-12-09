# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
#
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0:
                    temp = sorted([nums[i], nums[j], nums[k]])
                    if result.count(temp) == 0:
                        result.append(temp)
                if threeSum > 0:
                    k = k - 1
                else:
                    j = j + 1

        return result


solution = Solution()
# print(solution.threeSum([-3, -2, -2, -1, 0, 1, 2, 4, 5, 8]))
# print(solution.threeSum([-4, -2, -1, 0, 1, 2, 2, 3]))
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
