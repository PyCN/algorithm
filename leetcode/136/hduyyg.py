# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/136
# time: O(n)

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for x in nums: res ^= x
        return res
