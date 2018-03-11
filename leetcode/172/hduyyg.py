# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/172
# time: O(logn)

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            n //= 5
            res += n
        return res
