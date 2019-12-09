# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# 1、The length of both num1 and num2 is < 110.
# 2、Both num1 and num2 contain only digits 0-9.
# 3、Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# 4、You must not use any built-in BigInteger library or convert the inputs to integer directly.

import math


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        result = []
        # 乘法补位
        bits = 0
        # 最大位数
        maxBit = 0
        resultStr = ''
        for i in range(len(num1) - 1, -1, -1):
            # 乘法进位
            addNum = 0
            tmp = ''
            for j in range(len(num2) - 1, -1, -1):
                r = int(num2[j]) * int(num1[i]) + addNum
                addNum = math.floor(r / 10)
                tmp = str(r % 10) + tmp
            if addNum != 0:
                tmp = str(addNum) + tmp
            tmp = tmp + '0' * bits
            maxBit = max(len(tmp), maxBit)
            bits += 1
            result.append(tmp)
        addNum = 0
        for j in range(maxBit):
            r = 0
            for i in range(len(result)):
                if j <= len(result[i]) - 1:
                    r += int(result[i][len(result[i]) - j - 1])
            r += addNum
            addNum = math.floor(r / 10)
            resultStr = str(r % 10) + resultStr
        if addNum != 0:
            resultStr = str(addNum) + resultStr
        return resultStr


solution = Solution()
print(solution.multiply('123', '456'))
print(solution.multiply('12', '241'))
