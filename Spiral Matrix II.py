# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

from typing import List
from utils.Common import printDoubleArray


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        level = 0
        num = 0
        while num < n * n:
            for j in range(level, n - 1 - level):
                num += 1
                matrix[level][j] = num
            for i in range(level, n - level):
                num += 1
                matrix[i][n - 1 - level] = num
            for j in range(n - 2 - level, level, -1):
                num += 1
                matrix[n - 1 - level][j] = num
            for i in range(n - 1 - level, level, -1):
                num += 1
                matrix[i][level] = num
            level += 1
        return matrix


solution = Solution()

printDoubleArray(solution.generateMatrix(4))
printDoubleArray(solution.generateMatrix(1))
printDoubleArray(solution.generateMatrix(2))
