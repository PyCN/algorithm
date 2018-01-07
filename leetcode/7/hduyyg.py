# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/7

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res, sign = 0, 1
        if x < 0: x, sign = -x, -1
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        res *= sign
        if res > 2147483647 or res < -2147483648: res = 0
        return res
