# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/121
# time: O(n^2)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        res, max_price = 0, prices[len(prices) - 1]
        for i in range(len(prices) - 2, -1, -1):
            res = max(res, max_price - prices[i])
            max_price = max(max_price, prices[i])
        return res
