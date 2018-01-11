# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/11
# time: o(n)


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, L, R = 0, 0, len(height) - 1
        while L < R:
            if height[L] <= height[R]:
                res = max(res, height[L] * (R - L))
                tmp, L = height[L], L + 1
                while L < R and height[L] <= tmp: L += 1
            else:
                res = max(res, height[R] * (R - L))
                tmp, R = height[R], R - 1
                while L < R and height[R] <= tmp: R -= 1
        return res
