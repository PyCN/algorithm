# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/1
# time: O(nlong)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]