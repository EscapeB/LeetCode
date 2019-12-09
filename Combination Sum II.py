# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(filter(lambda x: x <= target, candidates))
        # print(candidates)
        # dp = [[] for _ in range(len(candidates))]
        result = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                result.append([candidates[i]])
            else:
                tmp = self.combinationSum2(candidates[i + 1:], target - candidates[i])
                if len(tmp) > 0:
                    for j in range(len(tmp)):
                        tmp[j] += [candidates[i]]
                        tmp[j].sort()
                result += tmp
        return [i for n, i in enumerate(result) if i not in result[:n]]
        # print()


solution = Solution()
print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
