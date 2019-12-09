# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
from utils.Common import printDoubleArray
from typing import List
import math


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        if obstacleGrid[0][0]:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for j in range(1, m):
            if obstacleGrid[0][j] != 1 and dp[0][j - 1]:
                dp[0][j] = 1
        for i in range(1, n):
            if obstacleGrid[i][0] != 1 and dp[i - 1][0]:
                dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if dp[i][j - 1] != 0:
                        dp[i][j] += dp[i][j - 1]
                    if dp[i - 1][j] != 0:
                        dp[i][j] += dp[i - 1][j]
        # printDoubleArray(dp)
        return dp[n - 1][m - 1]


solution = Solution()
print(solution.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
print(solution.uniquePathsWithObstacles([[0]]))
print(solution.uniquePathsWithObstacles([[1]]))
