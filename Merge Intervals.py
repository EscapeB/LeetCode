# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019.
# Please reset to default code definition to get new method signature.


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort()
        print(intervals)
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
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge([[1, 4], [4, 5]]))
print(solution.merge([[0, 4], [1, 5]]))
print(solution.merge([[1, 4], [0, 0]]))
