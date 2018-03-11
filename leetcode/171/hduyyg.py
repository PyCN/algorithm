# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/171
# time: O(n)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = res * 26 + ord(c) - ord('A') + 1
        return res
