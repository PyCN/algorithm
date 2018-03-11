# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/189
# time: O(n)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0: return
        st = range(self.gcd(k, len(nums)))
        for pos in st: self.rotate_from_st(nums, k, pos)

    def rotate_from_st(self, nums, k, st):
        len_nums, pre_val = len(nums), nums[st]
        i = (st + k) % len_nums
        while i != st:
            pre_val, nums[i] = nums[i], pre_val
            i = (i + k) % len_nums
        nums[i] = pre_val
    
    def gcd(self, a, b):
        while b != 0: a, b = b, a % b
        return a