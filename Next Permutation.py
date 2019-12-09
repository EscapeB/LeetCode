# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def findMinThan(numsArr, start, target) -> int:
            minInRange = -1
            for i in range(start, len(nums)):
                if target < nums[i]:
                    minInRange = i
            return minInRange

        if len(nums) <= 1:
            print(nums)
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = findMinThan(nums, i, nums[i - 1])
                tmp = nums[i - 1]
                nums[i - 1] = nums[index]
                nums[index] = tmp
                nums[i:] = sorted(nums[i:])
                print(nums)
                return
        nums.sort()
        print(nums)


solution = Solution()
solution.nextPermutation([])
solution.nextPermutation([1])
solution.nextPermutation([1, 2])
solution.nextPermutation([1, 2, 3])
solution.nextPermutation([1, 1, 5])
solution.nextPermutation([3, 2, 1])
