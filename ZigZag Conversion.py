# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arrays = [''] * numRows
        zigzagFlag = False
        row = 0
        for i in range(len(s)):
            arrays[row] += s[i]
            if row >= numRows - 1:
                zigzagFlag = True
                row = row - 1
            else:
                if row == 0:
                    zigzagFlag = False
                if zigzagFlag:
                    row = max(row - 1, 0)
                else:
                    row = min(row + 1, numRows)
        result_str = ''
        for j in range(len(arrays)):
            for k in range(len(arrays[j])):
                result_str += arrays[j][k]
        # print(arrays)
        return result_str


solution = Solution()
print(solution.convert('PAYPALISHIRING', 3))
print(solution.convert('PAYPALISHIRING', 4))
print(solution.convert('ABC', 1))
