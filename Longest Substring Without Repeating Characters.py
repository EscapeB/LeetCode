# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        op = [0] * (len(s) + 1)
        substr = ""
        for i in range(len(s) - 1, -1, -1):
            index = substr.find(s[i])
            if index < 0:
                op[i] = op[i + 1] + 1
                substr = s[i] + substr
            else:
                substr = s[i] + substr[0:index]
                op[i] = len(substr)
        return max(op)

    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        answer = 0
        n = len(s)
        charDic = {}
        while i < n and j < n:
            if charDic.get(s[j]) is not None:
                # print(j, i)
                answer = max(j - i, answer)
                i = charDic.get(s[j]) + 1
                charDic.clear()
                j = i
            elif j == n - 1:
                answer = max(j - i + 1, answer)
                j = j + 1
            else:
                charDic[s[j]] = j
                j = j + 1
        return answer


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("   "))
print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring("abddcaswbas"))
