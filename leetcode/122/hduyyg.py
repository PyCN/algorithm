# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/122
# time: O(n)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        f = [0 for _ in prices]
        max_tmp = -prices[0]
        for i in range(1, len(prices)):
            f[i] = max(f[i - 1], prices[i] + max_tmp)
            max_tmp = max(max_tmp, f[i - 1] - prices[i])
        return f[len(prices) - 1]
