# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        total = nums1 + nums2
        total.sort()
        if len(total) % 2 == 0:
            return (total[int(len(total) / 2)] + total[int((len(total) / 2) - 1)]) / 2
        else:
            return total[int((len(total) - 1) / 2)]

        # return total[len(total)]
        # print(total)


solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [1, 3, 5]))
