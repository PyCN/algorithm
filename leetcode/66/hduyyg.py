# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/66
# time: O(n)


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for x in digits: number = number * 10 + x
        return [int(x) for x in list(str(number + 1))]

