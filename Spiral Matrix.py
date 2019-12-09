# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        row, col = len(matrix), len(matrix[0])
        r = []
        level = 0
        while len(r) < row * col:
            if len(r) < row * col:
                for j in range(level, col - 1 - level):
                    r.append(matrix[level][j])
            if len(r) < row * col:
                for i in range(level, row - level):
                    r.append(matrix[i][col - 1 - level])
            if len(r) < row * col:
                for j in range(col - 2 - level, level, -1):
                    r.append(matrix[row - 1 - level][j])
            if len(r) < row * col:
                for i in range(row - 1 - level, level, -1):
                    r.append(matrix[i][level])
            level += 1
        return r


solution = Solution()
# print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.spiralOrder(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
))
print(solution.spiralOrder(
    [
        [1]
    ]
))
print(solution.spiralOrder(
    [
        [1],
        [2],
        [3]
    ]
))
print(solution.spiralOrder(
    [
        [1, 2, 3],
    ]
))
