# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # if x == 0:
        #     return 0
        # x = x if n >= 0 else 1 / x
        # n = abs(n)
        #
        # def subPow(x, n) -> float:
        #     if n == 1:
        #         return x
        #     else:
        #         tmp = subPow(x, n >> 1)
        #         return tmp * tmp * (tmp if int(tmp) & 1 else 1)
        if n == 0:
            return 1
        if x == 0:
            return 0
        x = x if n >= 0 else 1 / x
        n = abs(n)

        def subPow(var, level) -> float:
            if level == 1:
                return var
            else:
                if level % 2 == 0:
                    tmp = subPow(var, level / 2)
                    return tmp * tmp
                else:
                    return subPow(var, (level + 1) / 2) * subPow(var, (level - 1) / 2)

        return subPow(x, n)


solution = Solution()
print(solution.myPow(0, 1))
print(solution.myPow(0, 0))
print(solution.myPow(2.000, 10))
print(solution.myPow(2.10000, 3))
print(solution.myPow(2.00000, -2))
print(solution.myPow(0.00001, 2147483647))
