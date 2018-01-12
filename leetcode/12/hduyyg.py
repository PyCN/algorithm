# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/12


class Solution:
    def intToRoman(self, num):
        '''
        :type num: int
        :rtype: str
        '''
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return ''.join([M[num // 1000], C[(num % 1000) // 100], X[(num % 100) // 10], I[num % 10]])