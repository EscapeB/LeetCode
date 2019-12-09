# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# [-4, -1, 1, 2]  target=1


class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return
        nums.sort()
        # i = 0
        # j = len(nums) - 1
        distance = 99999999
        result = None
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threePlus = nums[i] + nums[j] + nums[k]
                currentDistance = abs(target - threePlus)
                if currentDistance < distance:
                    distance = currentDistance
                    result = threePlus
                if target - threePlus >= 0:
                    j = j + 1
                else:
                    k = k - 1

        return result


solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))
