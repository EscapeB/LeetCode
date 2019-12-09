class Solution:
    def twoSum(self, nums, target):
        result = [None] * 2
        temp_map = dict()
        for i in range(len(nums)):
            remain = target - nums[i]
            # print(remain, temp_map, temp_map.get(remain))
            if temp_map.get(remain) is not None:
                result[0] = temp_map.get(remain)
                result[1] = i
                break
            else:
                temp_map[nums[i]] = i
        return result


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
