# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai).
#
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
#
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
class Solution:
    def maxArea(self, height) -> int:
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * abs(i - j))
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return maxArea


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea([2, 19, 20, 12, 3]))
