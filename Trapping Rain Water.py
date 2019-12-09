# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
# 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        i = 0
        while i < len(height):
            if height[i] > 0:
                j = i + 1
                # 找到右侧第一个比i个位置高的位置
                while j < len(height):
                    if height[j] >= height[i]:
                        break
                    j += 1
                # 没找到比该位置高的，说明是左高右低情况，则应该找右侧最大值
                if j >= len(height):
                    j = i + 1
                    maxValue = 0
                    maxIndex = None
                    while j < len(height):
                        if height[j] >= maxValue:
                            maxValue = height[j]
                            maxIndex = j
                        j += 1
                    if maxIndex is None:
                        break
                    j = maxIndex
                # i到j之间的水量
                t = 0
                # 宽度
                w = j - i - 1
                # 高度： 存在左高右低和左低右高两种情况，应该取小值
                h = min(height[i], height[j])
                filled = 0
                for k in range(i + 1, j):
                    filled += height[k]
                t = w * h - filled
                total += t
                # 从j位置继续开始计算
                i = j
                continue
            i += 1
        return total


solution = Solution()
# print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(solution.trap([0, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(solution.trap([0, 1, 0, 4, 1, 0, 1, 3, 2, 1, 2, 1]))
