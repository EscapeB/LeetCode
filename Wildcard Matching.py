# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
#
# Example 1:
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
# Example 2:
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
# Example 3:
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#
# Example 4:
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#
# Example 5:
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        for j in range(1, len(p) + 1):
            if dp[0][j - 1] and p[j - 1] == '*':
                dp[0][j] = True
        for m in range(len(s)):
            for n in range(len(p)):
                if p[n] == '*' and (dp[m][n + 1] or dp[m + 1][n]):
                    dp[m + 1][n + 1] = True
                if dp[m][n] and (p[n] == '?' or s[m] == p[n]):
                    dp[m + 1][n + 1] = True
        # print(dp)
        return dp[len(s)][len(p)]


solution = Solution()
print(solution.isMatch("adceb", "*a*b"))
print(solution.isMatch("cb", "?a"))
print(solution.isMatch("acdcb", 'a*c?b'))
print(solution.isMatch("", ""))
