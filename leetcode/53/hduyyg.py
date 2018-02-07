# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/53
# time: O(n)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        count, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            count = max(nums[i], count + nums[i])
            res = max(count, res)
        return res
