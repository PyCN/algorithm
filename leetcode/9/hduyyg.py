# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/9

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if not x.isdigit(): return False
        lenx = len(x)
        for i in range(lenx // 2):
            if x[i] != x[lenx - 1 - i]: return False
        return True
