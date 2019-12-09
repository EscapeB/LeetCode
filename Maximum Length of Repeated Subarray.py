# Given two integer arrays A and B,
# return the maximum length of an subarray that appears in both arrays.
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].


class Solution:

    def findLength(self, A, B) -> int:
        maxLength = 0
        dp = [[0] * (len(A) + 1) for i in range(len(B) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                if dp[i][j] > maxLength:
                    maxLength = dp[i][j]
        # print(dp)
        return maxLength


solution = Solution()
print(solution.findLength([0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]))
