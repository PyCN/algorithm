# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/191
# time: O(1)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            if n & 1: res += 1
            n >>= 1
        return res
