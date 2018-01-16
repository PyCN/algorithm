# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/18
# time: O(n^3)

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        res, keys = [], count.keys()
        for a in keys:
            if a * 4 == target and count[a] >= 4: res.append([a, a, a, a])
            for b in keys:
                if b <= a or a * 3 + b > target: continue
                if count[a] > 2 and a * 3 + b == target:
                    res.append([a, a, a, b])
                if count[a] > 1 and count[b] > 1 and a + a + b + b == target:
                    res.append([a, a, b, b])
                if count[b] > 2 and a + b * 3 == target:
                    res.append([a, b, b, b])
                for c in keys:
                    if c <= b or a + a + b + c > target: continue
                    if count[a] > 1 and a + a + b + c == target:
                        res.append([a, a, b, c])
                    if count[b] > 1 and a + b + b + c == target:
                        res.append([a, b, b, c])
                    if count[c] > 1 and a + b + c + c == target:
                        res.append([a, b, c, c])
                    d = target - (a + b + c)
                    if d > c and d in keys : res.append([a, b, c, d])
        return res
