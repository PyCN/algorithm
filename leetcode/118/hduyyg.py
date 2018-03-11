# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/118
# time: O(n^2)

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([1 for _ in range(i + 1)])
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
            res[i][i] = res[i - 1][i - 1]
        return res
