# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/22

class Solution:
    sum_res = 0

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        self.sum_res = self.Catalan_number(n)
        res = [None for _ in range(self.sum_res)]
        tmp = [None for _ in range(n * 2)]
        tmp[0], index, sum_left = '(', 1, 1
        self.sum_res = 0
        self.dfs(res, tmp, index, sum_left, n * 2)
        return res
    
    def dfs(self, res, tmp, index, sum_left, length):
        if index == length:
            res[self.sum_res] = ''.join(tmp)
            self.sum_res += 1
            return

        if sum_left + sum_left < length:
            tmp[index] = '('
            self.dfs(res, tmp, index + 1, sum_left + 1, length)

        if sum_left + sum_left > index:
            tmp[index] = ')'
            self.dfs(res, tmp, index + 1, sum_left, length)

    def Catalan_number(self, n):
        res = 1
        for i in range(2, n + 1): res = res * (4 * i -2) // (i + 1)
        return res

res = Solution().generateParenthesis(1)
print(res)