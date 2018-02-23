# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/190
# time: O(1)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) ^ (n & 1)
            n >>= 1
        return res
