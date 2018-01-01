# author:2632158294@qq.com
# github:pyCN/algorithm/leetcode/3

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        nums = [None for _ in range(len1 + len2)]
        p1, p2, p3 = 0, 0, 0
        
        while p1 < len1 and p2 < len2:
            if nums1[p1] < nums2[p2]:
                nums[p3] = nums1[p1]
                p1 += 1
            else:
                nums[p3] = nums2[p2]
                p2 += 1
            p3 += 1
        while p1 < len1:
            nums[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        while p2 < len2:
            nums[p3] = nums2[p2]
            p2 += 1
            p3 += 1
        
        if p3 % 2 == 0:
        	return (nums[p3 // 2] + nums[p3 // 2 - 1]) / 2
        else:
            return nums[p3 // 2] * 1.0

