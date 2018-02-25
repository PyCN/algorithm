# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/278
# time: O(logn)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while L <= R:
            mid = (L + R) >> 1
            if isBadVersion(mid):
                R = mid - 1
            else:
                L = mid + 1
        return L
