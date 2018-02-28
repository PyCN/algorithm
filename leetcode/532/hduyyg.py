# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/532
# time: o(n)

import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        if k > 0: return len(set(nums) & set(n+k for n in nums))
        return sum(v > 1 for v in collections.Counter(nums).values())
