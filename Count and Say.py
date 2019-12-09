# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"


class Solution:
    def countAndSay(self, n: int) -> str:
        def sayStr(s: str) -> str:
            if len(s) == 0:
                return ''
            else:
                s = s + '#'
                repeatedChar = s[0]
                count = 1
                tmpStr = ''
                for j in range(1, len(s)):
                    if s[j] != repeatedChar:
                        tmpStr += str(count) + repeatedChar
                        repeatedChar = s[j]
                        count = 1
                    else:
                        count += 1
            return tmpStr

        if n == 1:
            return '1'
        else:
            dp = [''] * n
            dp[0] = '1'
            for i in range(1, n):
                dp[i] = sayStr(dp[i - 1])
            return dp[n - 1]


solution = Solution()
print(solution.countAndSay(5))
