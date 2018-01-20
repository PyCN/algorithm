# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/27
# time: O(n)

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for x in nums:
            if x != val:
                nums[index] = x
                index += 1
        return index