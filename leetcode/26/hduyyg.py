# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/26
# time: O(n)

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0: return 0
        res = 1
        for i in range(1, len_nums):
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        return res
