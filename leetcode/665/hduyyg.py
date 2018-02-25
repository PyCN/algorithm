# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/665
# time: O(n)

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        res = self.check(nums, 0, len_nums - 1)
        if res[0]: return True
        if res[1] > 0:
            if nums[res[1] + 1] >= nums[res[1] - 1]:
                nums[res[1]] = nums[res[1] + 1]
            else:
                nums[res[1] + 1] = nums[res[1]]
        else:
            nums[res[1]] = nums[res[1] + 1]
        res = self.check(nums, res[1], len_nums - 1)
        return res[0]

    def check(self, nums, st, ed):
        for i in range(st, ed):
            if nums[i] > nums[i + 1]: return False, i
        return True, None
