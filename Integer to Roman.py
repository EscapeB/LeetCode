# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
#
# 12 is written as, XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
#
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

import math


class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        outputStr = ''
        for i in range(3, -1, -1):
            divider = math.pow(10, i)
            char = mapping[divider]
            remain = math.floor(num / divider)
            if remain == 4:
                outputStr += mapping[divider] + mapping[divider * 5]
            elif remain == 9:
                outputStr += mapping[divider] + mapping[divider * 10]
            else:
                if remain >= 5:
                    outputStr += mapping[divider * 5]
                    remain -= 5
                for j in range(remain):
                    outputStr += char
            num = num % divider
        return outputStr
        # print(outputStr)


solution = Solution()
print(solution.intToRoman(1))
print(solution.intToRoman(3))
print(solution.intToRoman(4))
print(solution.intToRoman(58))
print(solution.intToRoman(1994))
print(solution.intToRoman(3999))
