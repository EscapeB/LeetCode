# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for i in range(len(strs)):
            tmp = list(strs[i])
            tmp.sort()
            tmp = str(tmp)
            if tmp not in dic:
                dic[tmp] = len(res)
                res.append([strs[i]])
            else:
                res[dic[tmp]].append(strs[i])
        return res


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
