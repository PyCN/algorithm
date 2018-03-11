# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/16
# time: O(n^2)

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == target: return tmp
                if abs(tmp - target) < abs(res - target): res = tmp
                if tmp < target:
                    j += 1
                else:
                    k -= 1
        return res
