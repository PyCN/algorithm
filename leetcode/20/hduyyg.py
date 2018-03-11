# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/20
# time: O(n)

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = {'(':-1,')':1,'[':-2,']':2,'{':-3,'}':3}
        index, s, lens = -1, list(s), len(s)
        for i in range(lens):
            if f[s[i]] < 0:
                index += 1
                s[index] = s[i]
            else:
                if index < 0 or f[s[i]] + f[s[index]] != 0: return False
                index -= 1
        return True if index == -1 else False
