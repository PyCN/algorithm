# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/31
# time: O(n)

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums < 2: return
        for i in range(len_nums - 2, -1, -1):
            if nums[i] >= nums[i + 1]: continue
            for j in range(len_nums - 1, i, -1):
                if nums[j] <= nums[i]: continue
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return
        return nums.sort()
