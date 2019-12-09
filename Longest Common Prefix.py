# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

import sys


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        commonPrefix = ''
        lengthArray = []
        if len(strs) == 0:
            return ''
        for i in strs:
            lengthArray.append(len(i))
        for i in range(min(lengthArray)):
            str_temp = ""
            for j in strs:
                if str_temp:
                    if str_temp != j[:i + 1]:
                        return commonPrefix
                else:
                    str_temp = j[:i + 1]
            commonPrefix = str_temp
        return commonPrefix


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["abc", "dxs", "bdc"]))
print(solution.longestCommonPrefix([]))
