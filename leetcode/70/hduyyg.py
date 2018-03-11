# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/70
# time: O(n)

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1, 1, 0]
        for i in range(2, n + 1):
            f[i % 2] = f[(i - 1) % 2] + f[(i - 2) % 2]
        return f[n % 2]
