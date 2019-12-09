# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

from typing import List
import math


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            s = add + digits[i]
            digits[i] = s % 10
            if s >= 10:
                add = math.floor(s / 10)
            else:
                add = 0
        if add > 0:
            digits.insert(0, add)
        return digits


solution = Solution()
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))
print(solution.plusOne([9, 9, 9]))
