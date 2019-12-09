# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                k = i + 1
                l = j - 1
                while k < l:
                    # print(i, k, j, l)
                    fourSum = nums[i] + nums[j] + nums[k] + nums[l]
                    if fourSum == target:
                        temp = sorted([nums[i], nums[j], nums[k], nums[l]])
                        if result.count(temp) == 0:
                            result.append(temp)
                    if target - fourSum >= 0:
                        k = k + 1
                    else:
                        l = l - 1
        return result


solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
