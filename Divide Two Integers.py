# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3

# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit
# signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

import time


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1
        if dividend == 0:
            return 0
        if dividend < 0:
            dividend = abs(dividend)
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        tmp = divisor
        while tmp <= dividend:
            bit = 1
            while tmp << 1 <= dividend:
                bit = bit << 1
                tmp = tmp << 1
            dividend -= tmp
            tmp = divisor
            result += bit

        return min(2147483647, max(-result if sign < 0 else result, -2147483648))


# def divide(self, dividend: int, divisor: int) -> int:
#     is_negative = (dividend < 0) != (divisor < 0)
#     divisor, dividend = abs(divisor), abs(dividend)
#
#     quotient = 0
#     the_sum = divisor
#
#     while the_sum <= dividend:
#         current_quotient = 1
#         while (the_sum << 1) <= dividend:
#             the_sum <<= 1
#             current_quotient <<= 1
#         dividend -= the_sum
#         the_sum = divisor
#         quotient += current_quotient
#
#     return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))


solution = Solution()
print(solution.divide(10, 3))
print(solution.divide(21, 3))
print(solution.divide(15, 3))
print(solution.divide(4, 1))
print(solution.divide(0, 3))

now = time.time()
print(solution.divide(-2147483648, -3))
print(time.time() - now)
