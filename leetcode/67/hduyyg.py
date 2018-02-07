# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/67
# time: O(n)

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b): a, b = b, a
        lena, lenb = len(a), len(b)        
        a = [int(a[i]) for i in range(lena - 1, -1, -1)]
        b = [int(b[i]) for i in range(lenb - 1, -1, -1)]
        res = [0 for _ in range(lena + 1)]
        for i in range(lenb): res[i] = a[i] + b[i]
        for i in range(lenb, lena): res[i] = a[i]
        for i in range(lena):
            res[i + 1] += res[i] // 2
            res[i] %= 2
        if res[lena] == 0:
            return ''.join([str(res[i]) for i in range(lena - 1, -1, -1)])
        return ''.join([str(res[i]) for i in range(lena, -1, -1)])
