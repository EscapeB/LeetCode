# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnMap = [{} for _ in range(9)]
        subMap = [{} for _ in range(3)]
        for i in range(9):
            rowMap = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if rowMap.get(board[i][j]) or columnMap[j].get(board[i][j]) or subMap[int(j / 3)].get(board[i][j]):
                        return False
                    else:
                        rowMap[board[i][j]] = 1
                        columnMap[j][board[i][j]] = 1
                        subMap[int(j / 3)][board[i][j]] = 1
            if i % 3 == 2:
                subMap = [{} for _ in range(3)]
        return True


solution = Solution()
print(solution.isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
print(solution.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
