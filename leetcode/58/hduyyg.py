# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/58
# time: O(n)

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s: return 0
        st = s.rfind(' ')
        if st == -1: return len(s)
        return len(s) - st -1
