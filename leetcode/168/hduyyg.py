# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/168

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n != 0:
            tmp = (n - 1) % 26
            res, n = res + chr(ord('A') + tmp), (n - 1) // 26
        return res[::-1]
