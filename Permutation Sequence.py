# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note:
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:
#
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
#
# Input: n = 4, k = 9
# Output: "2314"

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i + 1 for i in range(n)]
        r = ''
        fac = n
        remain = k
        while fac >= 1:
            fac -= 1
            mod = math.factorial(fac)
            nth = math.floor((remain - 1) / mod)
            r += str(nums.pop(nth))
            if remain > nth * mod:
                remain -= nth * mod
        return r


solution = Solution()
print(solution.getPermutation(4, 9))
print(solution.getPermutation(3, 3))
print(solution.getPermutation(3, 1))
print(solution.getPermutation(1, 1))
print(solution.getPermutation(3, 2))
print(solution.getPermutation(3, 5))
print(solution.getPermutation(4, 1))
print(solution.getPermutation(4, 2))
