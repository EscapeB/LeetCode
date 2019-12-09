# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        return len(s.lstrip().rstrip().split(' ').pop())
        output = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if output == 0:
                    continue
                else:
                    break
            else:
                output += 1

        return output


solution = Solution()
print(solution.lengthOfLastWord('Hello World'))
print(solution.lengthOfLastWord('    d     '))
print(solution.lengthOfLastWord('         '))
print(solution.lengthOfLastWord(''))
