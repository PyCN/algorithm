# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/17

class Solution:
    sum_res = 0

    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        if len(digits) == 0: return []
        strs = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 
            'mno', 'pqrs', 'tuv', 'wxyz']
        sums = 1
        for num in digits: sums *= len(strs[int(num)])
        res = [None for _ in range(sums)]
        tmp = [None for _ in range(len(digits))]
        self.sum_res = 0
        self.dfs(res, strs, digits, tmp, 0, len(digits))
        return res

    def dfs(self, res, strs, digits, tmp, index, length):
        if index == length:
            res[self.sum_res] = ''.join(tmp)
            self.sum_res += 1
            return
        for c in strs[int(digits[index])]:
            tmp[index] = c
            self.dfs(res, strs, digits, tmp, index + 1, length)
