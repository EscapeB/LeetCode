# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r1 = r2 = 1
        for i in range(min(m, n) - 1):
            r1 *= i + 1
            r2 *= m + n - 2 - i
        return int(r2 / r1)


solution = Solution()
# print(solution.uniquePaths(2, 3))
# print(solution.uniquePaths(3, 2))
print(solution.uniquePaths(7, 3))
print(solution.uniquePaths(3, 7))
