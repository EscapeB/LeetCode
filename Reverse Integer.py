# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(abs(x))[::-1]
        if x < 0:
            num = -int(x_str)
        else:
            num = int(x_str)
        if num < -pow(2, 31) or num > pow(2, 31) - 1:
            return 0
        return num


solution = Solution()
print(solution.reverse(0))
print(solution.reverse(12344))
print(solution.reverse(-1992123))
print(solution.reverse(1534236469))
# print(pow(2, 31))
