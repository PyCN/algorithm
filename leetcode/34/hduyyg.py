# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/34
# time: O(n)

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        L, R = 0, len_nums - 1
        while L <= R:
            mid = (L + R) >> 1
            if nums[mid] < target:
               L = mid + 1
            else:
               R = mid - 1
        if L >= len_nums or nums[L] != target: return -1, -1
        left = L

        L, R = 0, len_nums - 1
        while L <= R:
            mid = (L + R) >> 1
            if nums[mid] <= target:
                L = mid + 1
            else:
                R = mid -1
        right = R
        return left, right
