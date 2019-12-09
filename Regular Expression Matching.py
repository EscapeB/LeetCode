# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false


from utils.Common import printDoubleArray


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(len(p)):
            if j >= 1 and dp[0][j - 1] and p[j] == '*':
                dp[0][j + 1] = True
        for m in range(len(s)):
            for n in range(len(p)):
                if (s[m] == p[n] or p[n] == '.') and dp[m][n]:
                    dp[m + 1][n + 1] = True
                if p[n] == '*':
                    # 前一个字符重复情况
                    if n > 0 and (p[n - 1] == s[m] or p[n - 1] == '.') and (dp[m + 1][n] or dp[m][n + 1]):
                        dp[m + 1][n + 1] = True
                    # 该段为0次
                    if n > 0 and dp[m + 1][n - 1]:
                        dp[m + 1][n + 1] = True
        # printDoubleArray(dp)
        return dp[len(s)][len(p)]


solution = Solution()
print(solution.isMatch("mississippi", "mis*is*p*."))  # False
print(solution.isMatch("aab", "c*a*b"))  # True
print(solution.isMatch("abccc", ".*"))  # True
print(solution.isMatch("aabb", "a*bb*"))  # True
print(solution.isMatch("abc", "a.c*mc*"))  # True
print(solution.isMatch("aaa", "a*"))  # True
print(solution.isMatch("abc", "a.cd"))  # False
# print(solution.isMatch("aaab", "a*aaab"))  # True
# print(solution.isMatch("dssa", "d.s*a"))  # True
# print(solution.isMatch("ddassa", "d.s*a"))  # False
# print(solution.isMatch("aaa", "a*a"))  # True
