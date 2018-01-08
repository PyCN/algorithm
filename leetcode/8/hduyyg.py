# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/8

class Solution:
    def myAtoi(self, ss):
        """
        :type str: str
        :rtype: int
        """
        ss, st, res, sign = ss.strip(), 0, 0, 1
        if len(ss) == 0: return 0
        if not ss[0].isdigit():
            if ss[0] == '-':
                sign = -1
            elif ss[0] != '+':
                return 0
            st = 1
        for i in range(st, len(ss)):
            if not ss[i].isdigit(): break
            res = res * 10 + int(ss[i])
        return max(-2**31, min(res * sign, 2**31-1))
