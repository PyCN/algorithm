# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/4
# time: O(log(min(m,n)))

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            len1, nums1, len2, nums2 = len2, nums2, len1, nums1
        half = (len1 + len2) // 2
        L, R = 0, len1 - 1
        while L <= R:
            p1 = (L + R) // 2
            p2 = half - p1 - 2
            if p2 >= len2 or (p1 + 1 < len1 and nums1[p1 + 1] < nums2[p2]): 
                L = p1 + 1
            elif p2 + 1 < len2 and nums2[p2 + 1] < nums1[p1]:
                R = p1 - 1
            else:
                L, R = p1 + 1, p1 
        
        p1, p2 = R, half - R - 2
        if p1 + 1 < len1 and (p2 + 1 >= len2 or nums1[p1 + 1] < nums2[p2 + 1]):
            tmp = nums1[p1 + 1]
        else:
            tmp = nums2[p2 + 1]
        if (len1 + len2) % 2 != 0:
            return tmp
        else:
            if p1 < 0 or p1 >= len1:
                return (tmp + nums2[p2]) / 2
            elif p2 < 0:
                return (tmp + nums1[p1]) / 2
            else:
                return (tmp + max(nums1[p1], nums2[p2])) / 2
