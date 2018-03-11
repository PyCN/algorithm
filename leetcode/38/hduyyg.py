# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/38

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ['1']
        for i in range(n - 1): res = self.build(res)
        return ''.join(res)

    def build(self, s):
        count, res = 1, []
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res.extend([str(count), s[i - 1]])
                count = 1
            else:
                count += 1
        res.extend([str(count), s[len(s) - 1]])
        return res
