# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] > target:
                continue
            elif candidates[i] == target:
                result.append([candidates[i]])
            else:
                tmp = self.combinationSum(candidates, target - candidates[i])
                if len(tmp) > 0:
                    for j in range(len(tmp)):
                        tmp[j] += [candidates[i]]
                        tmp[j].sort()
                    result += tmp
        return [i for n, i in enumerate(result) if i not in result[:n]]


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
print(solution.combinationSum([2, 3, 5], 8))
