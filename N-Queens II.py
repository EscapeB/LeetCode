# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Example:
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution:
    def totalNQueens(self, n: int) -> int:
        r = 0
        matrix = [['.'] * n for _ in range(n)]
        queenPos = []

        def canPut(row: int, column: int) -> bool:
            for k in range(len(queenPos)):
                x = int(queenPos[k][0])
                y = int(queenPos[k][1])
                if x == row or y == column or abs(x - row) / abs(y - column) == 1:
                    return False
            return True

        i = 0
        startColumn = 0
        while i < n:
            j = startColumn
            find = False
            # 查找本行是否有符合的位置
            while j < n:
                if canPut(i, j):
                    find = True
                    break
                j += 1
            if find:
                matrix[i][j] = 'Q'
                queenPos.append([i, j])
                # 找到一个完整解，记录
                if len(queenPos) == n:
                    r += 1
                else:
                    # 直接下一行，剪枝
                    i += 1
                    startColumn = 0
                    continue
            # 未找到或者已经找到一个解
            if not find or len(queenPos) == n:
                if len(queenPos) > 0:
                    lastPos = queenPos.pop()
                    lastX, lastY = lastPos[0], lastPos[1]
                    matrix[lastX][lastY] = '.'
                    # 搜索结束了
                    if lastX == 0 and lastY == n - 1:
                        break
                    i = lastX
                    startColumn = lastY + 1
                    continue

            i += 1
            startColumn = 0
        return r


solution = Solution()
print(solution.totalNQueens(4))
