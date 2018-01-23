# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/32
# time: O(n)

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target: return i
        return -1
