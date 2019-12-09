# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


from typing import List


class Solution:
    # Solution 1
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     i = 0
    #     stack = []
    #     position = []
    #     while i < len(nums):
    #         for j in range(0, len(nums)):
    #             # 找到第一个不在stack中的数
    #             if j not in position:
    #                 # 记录值
    #                 stack.append(nums[j])
    #                 # 记录每一位对应的index
    #                 position.append(j)
    #                 break
    #         # 说明已经满了，记录结果，开始回溯
    #         if len(stack) == len(nums):
    #             if stack not in result:
    #                 result.append(list(stack))
    #             position.pop()
    #             stack.pop()
    #             while len(position) > 0:
    #                 # 该位置已经
    #                 if position[len(position) - 1] >= len(nums) - 1:
    #                     position.pop()
    #                     stack.pop()
    #                 else:
    #                     find = False
    #                     for k in range(position[len(position) - 1], len(nums)):
    #                         if k not in position:
    #                             position[len(position) - 1] = k
    #                             stack[len(stack) - 1] = nums[k]
    #                             find = True
    #                             break
    #                     if find:
    #                         break
    #                     else:
    #                         position.pop()
    #                         stack.pop()
    #             if len(position) > 0:
    #                 i = len(position) - 1
    #             else:
    #                 break
    #         i += 1
    #     return result

    # Solution 2
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permute(prevStack: List[int], pos: List[int], cursor: int):
            for i in range(len(nums)):
                if i in pos:
                    continue
                if cursor == len(nums) - 1:
                    if prevStack + [nums[i]] not in res:
                        res.append(prevStack + [nums[i]])
                else:
                    permute(prevStack + [nums[i]], pos + [i], cursor + 1)

        permute([], [], 0)
        return res


solution = Solution()
print(solution.permuteUnique([]))
print(solution.permuteUnique([1, 1, 2]))
# print(solution.permute([1, 2, 3, 4]))
