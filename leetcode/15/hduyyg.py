# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/15
# time: O(n^2)

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        res, count = [], {}
        for x in nums:
            if not count.get(x):
                count[x] = 1
            else:
                count[x] += 1
        keys = count.keys()
        for key1 in keys:
            if count[key1] > 1:
                if key1 == 0:
                    if count[key1] < 3: continue
                    res.append([0, 0, 0])
                else:
                    key2 = -2 * key1
                    if key2 in keys: res.append([key1, key1, key2])
            for key2 in keys:
                if key2 <= key1: continue
                key3 = -key1 - key2
                if key3 <= key2 or not count.get(key3): continue
                res.append([key1, key2, key3])
        return res
