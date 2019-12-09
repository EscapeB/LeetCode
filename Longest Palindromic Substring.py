# Given a string s, find the longest palindromic substring in s.
#
# You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
#
# Input: "cbbd"
# Output: "bb"


# print(s.join('#'))
# maxStr = ''
# for i in range(len(s)):
#     j = i
#     k = i
#     temp = ""
#     while j >= 0 or k < len(s):
#         if j == i and k == i:
#             temp = s[i]
#         else:
#             if s[j] == s[k]:
#                 temp = s[j] + temp + s[k]
#             else:
#                 if s[j] == temp[len(temp) - 1]:
#                     temp = s[j] + temp
#                 if s[k] == temp[0]:
#                     temp = temp + s[k]
#         if len(temp) > len(maxStr):
#             maxStr = temp
#         # if s[j] != s[k]:
#         #     break
#         j = j - 1
#         k = k + 1
# return maxStr

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if j < 1:
                    t = None
                else:
                    t = j - 1
                # 直接从最长开始截取，倒转后比较
                if s[j:j + i] == s[j + i - 1:t:-1]:
                    return s[j:j + i]
        return s


solution = Solution()
print(solution.longestPalindrome("baab"))
print(solution.longestPalindrome('ac'))
print(solution.longestPalindrome("aaaabaaa"))
print(solution.longestPalindrome("bvbf"))
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("aaabaa"))
