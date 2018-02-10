# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/111
# time: O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        min_depth_left = self.minDepth(root.left)
        min_depth_rigth = self.minDepth(root.right)
        if min_depth_left == 0: return min_depth_rigth + 1
        if min_depth_rigth == 0: return min_depth_left + 1
        return min(min_depth_left, min_depth_rigth) + 1
