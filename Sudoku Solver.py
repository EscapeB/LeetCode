# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

from typing import List
import math


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def test(row, column, value) -> bool:
            for i in range(9):
                if board[i][column] == str(value):
                    return False
            for j in range(9):
                if board[row][j] == str(value):
                    return False
            startR = math.floor(row / 3)
            startC = math.floor(column / 3)
            for p in range(3):
                for q in range(3):
                    if board[startR * 3 + p][startC * 3 + q] == str(value):
                        return False
            return True

        i, j = 0, 0
        fixed = [[int] * 2]
        while i < 9:
            j = 0
            while j < 9:
                # 预记录所有预设值
                if board[i][j] != '.' and [i, j] not in fixed:
                    fixed.append([i, j])
                # 在预设值位置
                elif [i, j] in fixed:
                    None
                # 不在预设位置
                else:
                    isFind = False
                    # 从0到9进行尝试
                    for k in range(1, 10):
                        if test(i, j, k):
                            board[i][j] = str(k)
                            isFind = True
                            break
                    # 本次没有找到，退回非固定上一列,且上一列数字加一,
                    if not isFind:
                        while i >= 0:
                            if [i, j] not in fixed:
                                board[i][j] = "."
                            # 回退一列
                            j -= 1
                            # 如果回退至第一列，换上一行继续
                            if j < 0:
                                i -= 1
                                j = 8
                            # 回退至起点
                            if i < 0:
                                break

                            # 已经尝试该位置所有可能性，或者说明是预设位置
                            if board[i][j] == '9' or [i, j] in fixed:
                                continue
                            # 否则该空位值加一,继续探索
                            else:
                                start = int(board[i][j]) + 1
                                isFindBack = False
                                for k in range(start, 10):
                                    if test(i, j, k):
                                        board[i][j] = str(k)
                                        isFindBack = True
                                        break
                                if isFindBack:
                                    break
                j += 1
            i += 1
        print(board)


solution = Solution()

solution.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                      [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                      ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                      [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                      [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
