# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/29

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            i, tmp = 1, divisor
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if not sign: res = -res
        return min(max(-2147483648, res), 2147483647)
