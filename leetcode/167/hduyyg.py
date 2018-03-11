# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/167
# time: O(n)

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L, R = 0, len(numbers) - 1
        while L < R:
            tmp = numbers[L] + numbers[R]
            if tmp == target: return [L + 1, R + 1]
            if tmp < target:
                L += 1
            else:
                R -= 1
        return None
