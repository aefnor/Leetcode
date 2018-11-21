import math


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x < 0:
            neg = -1
            x *= -1
        else:
            neg = 1
        while x > 0:
            result += math.floor(x % 10)
            result *= 10
            x = math.floor(x / 10)
        result = int(result / 10) * neg
        if result >= 2147483647 or result <= -2147483647:
            return 0
        return result




####################################################################################
test = Solution()

print(test.reverse(123))
