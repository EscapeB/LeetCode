# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            inter1 = intervals[i]
            inter2 = intervals[i + 1]
            if inter1[1] >= inter2[0]:
                intervals.remove(inter1)
                intervals.remove(inter2)
                intervals.insert(i, [min(inter1[0], inter2[0]), max(inter1[1], inter2[1])])
                continue
            else:
                i += 1

        return intervals


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))
