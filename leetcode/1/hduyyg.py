# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/1
# time: O(n)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        order = {}
        for i, x in enumerate(nums):
            if target - x in order: return order[target - x], i
            order[x] = i

