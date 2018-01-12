# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/13

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }
        res = roman[s[0]]
        for i in range(0, len(s) - 1):
            res += roman[s[i + 1]]
            if roman[s[i]] < roman[s[i + 1]]: res -= 2 * roman[s[i]] 
        return res
