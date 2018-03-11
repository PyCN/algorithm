# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/151

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split()
        ss.reverse()
        res = ' '.join(ss)
        return res
