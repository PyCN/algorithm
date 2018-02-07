# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/69
# time: O(logn)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        L, R = 0, x
        while L <= R:
            mid = (L + R) // 2
            mul = mid * mid
            if mul == x: return mid
            if mul < x:
                L = mid + 1
            else:
                R = mid - 1
        return R
