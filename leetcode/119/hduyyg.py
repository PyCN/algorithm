# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/119
# time: O(k^2)

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0 for _ in range(rowIndex + 1)]
        res[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(rowIndex, 0, -1):
                res[j] = res[j - 1] + res[j]
        return res
