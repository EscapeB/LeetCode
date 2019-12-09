# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                if i < 2:
                    dp[i] = 2
                else:
                    dp[i] = dp[i - 2] + 2
            elif s[i] == ")":
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        # print(dp)
        return max(dp)


solution = Solution()
print(solution.longestValidParentheses("()(()()"))
print(solution.longestValidParentheses(""))
# print(solution.longestValidParentheses("("))
# print(solution.longestValidParentheses(")"))
# print(solution.longestValidParentheses("(()"))
# print(solution.longestValidParentheses(")()())"))
print(solution.longestValidParentheses("(())()(())"))
