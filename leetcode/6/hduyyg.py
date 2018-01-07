# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/6
# time: O(n)


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if numRows == 1 or numRows >= lens: return s
        ss = ['#' for _ in range(lens)]
        add1 = 2 * numRows - 2
        add2, id = add1, 0
        for i in range(0, lens, add1):
            ss[id] = s[i]
            id += 1
        for i in range(1, numRows - 1):
            add2 -= 2
            for j in range(i, lens, add1):
                ss[id] = s[j]
                id += 1
                if j + add2 < lens:
                    ss[id] = s[j + add2]
                    id += 1
        for i in range(numRows - 1, lens, add1):
            ss[id] = s[i]
            id += 1
        return ''.join(ss)
