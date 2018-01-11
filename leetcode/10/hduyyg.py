# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/10

import re

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return True if re.match(p + '$', s) else False
